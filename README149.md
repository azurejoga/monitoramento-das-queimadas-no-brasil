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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bda6f1b-f3b9-34d5-a577-e8416499909a | -10.35316 | -55.86245 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d74eb964-a970-3231-b866-719540b43b2f | -10.35307 | -55.86207 | 2024-10-09 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ee796d40-796a-345e-970b-c3b807208177 | -10.33439 | -57.50407 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b452ee-9d38-3a64-88d0-a423505e5108 | -10.33349 | -57.50906 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cc1388d-5b67-316c-a083-5adf62d72f2e | -10.3297 | -57.50326 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc2f98a-94b7-34ba-a7b3-aec3881717df | -10.3288 | -57.50825 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3591729-ce96-3547-b6eb-8266d67bc1e8 | -10.28121 | -58.19906 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 368b3104-513b-3555-96c2-a5c92820ff53 | -10.25621 | -56.75798 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52000a4-bffa-30c6-af94-95000e79e2ef | -10.25542 | -56.76248 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b92aea0-85bf-3c8e-a842-9d8c1f633f90 | -10.24023 | -54.96406 | 2024-10-09 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e2b1e76-8aa4-3de4-9e28-77fa1b25ff78 | -10.23994 | -59.14339 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c761a6a-a058-3138-9898-86f1b2ea91c9 | -10.23936 | -59.14656 | 2024-10-09 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cc95a24-3ff0-3947-9d11-990740ca0b81 | -10.23207 | -57.82424 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabdaa5d-f406-397c-afdb-4041455d3445 | -10.22963 | -57.81712 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae59df0-5019-3222-a413-0b6701503e25 | -10.22921 | -57.81288 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a63f5a9e-7a9a-3312-a9ca-17700db25672 | -10.22871 | -57.82233 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 128f44a7-a159-3f16-a6db-0bc2715759f9 | -10.22827 | -57.81801 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce20c4d5-d1ad-38e4-96b0-1a8d8d62341b | -10.22777 | -57.82771 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af46508b-a709-3e6d-89d7-5e7db616fcb2 | -10.2273 | -57.82325 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e438b8c9-36fe-3aa5-be2a-65d6e32dcf14 | -10.22631 | -57.82862 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db1f41c3-5079-3623-a12e-9e1a335f281d | -10.22576 | -57.81104 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a84f8e5-8a00-392a-8f2e-63f9262c0986 | -10.22484 | -57.81623 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffccd6b6-dc74-3d51-8dd4-14030137a7b8 | -10.22443 | -57.81194 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cf27de3-946e-3594-86d0-93a5d365ce50 | -10.22392 | -57.82146 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df556d9e-3a77-38dc-affa-dc05a59335c5 | -10.22347 | -57.81714 | 2024-10-09 04:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fa136ad-bd81-3ce0-ad8b-2720cf0797bb | -10.22285 | -54.26936 | 2024-10-09 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29f04692-5aa0-334a-8969-e0ece9d76626 | -10.21608 | -54.15462 | 2024-10-09 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a1f3feea-8ad6-3349-a206-57a268378d75 | -10.21556 | -54.15271 | 2024-10-09 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17fee47-db0f-3797-a640-be31625863f6 | -10.21477 | -54.1573 | 2024-10-09 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af400ff2-fb6e-3c34-89f2-2cb0d3316af2 | -10.2123 | -54.15396 | 2024-10-09 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ee6c00b-590c-3ed1-a8e0-eb7e3cbf0d3f | -10.20129 | -58.80061 | 2024-10-09 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39f9b7e4-6642-3fb6-91cb-d74cd48a5101 | -20.10504 | -55.95402 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f454a1ce-70e3-384c-9409-bb4231363551 | -20.10424 | -55.95848 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e2a79cb-50d9-39c7-9183-dec7bae079eb | -20.1022 | -55.94883 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 408edb39-e3ef-3867-a6aa-d80de9f6924e | -20.1014 | -55.9533 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 267508cd-9973-3701-a88c-011b77f8d77c | -20.1006 | -55.95776 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 56420ac3-080c-3c30-a03b-acb3c1cd5ff1 | -20.0998 | -55.96223 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e206a5b3-d1c5-3b0a-9601-df0a704018f4 | -20.09856 | -55.9481 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| be2cd332-969d-3b79-8c11-7a0c2667f50e | -20.09776 | -55.95257 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 952b7379-fa82-3cec-aca8-8c499272f6fb | -20.09696 | -55.95704 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 215c4ea5-6651-36cd-88ff-17c38e20ed66 | -20.09616 | -55.96151 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a480aa7d-ec02-3c01-a6f6-33e7b81f303c | -20.09526 | -55.94991 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7e7921ad-ae5e-3c9d-8d1d-188cf68d4b64 | -20.09448 | -55.95438 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| edc4b4e7-c09c-301f-9174-86a23d4e2557 | -20.09413 | -55.95184 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 86a3dbf8-ada7-3902-8835-5ebc24c40fe6 | -20.0937 | -55.95886 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2bc5f4c9-76a7-3bcd-8e4c-f3f90bf6fe8e | -20.09332 | -55.95631 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1f97815e-8e4c-302a-b6e3-ad2433f7fa80 | -20.09252 | -55.96078 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 052c94b4-5f3d-3afc-af99-4564610d3ac5 | -20.09085 | -55.95366 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 510c9e60-f0c5-36bd-a0c4-0c73b008b8a0 | -20.09049 | -55.95112 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1fcb7193-75d9-3828-9a20-9522074ef952 | -20.09007 | -55.95813 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 75bfcc9f-553a-3eb9-9f4f-651e9d42b073 | -20.08968 | -55.95559 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e9ead93-0dbb-34c8-9adf-611e1778100b | -20.08888 | -55.96006 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7c2dd029-e2b7-36c5-8596-238ab4561d1e | -20.08721 | -55.95293 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 23030ae1-aca6-323c-b93e-c43f1fc6a15e | -20.08643 | -55.95741 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d684c406-dbca-356a-9bcf-10da1a7ac6d2 | -20.08604 | -55.95487 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| acb9837e-3c80-3a0c-9e85-99529b262d1b | -20.08524 | -55.95934 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 406fbf2e-0a2b-3d1f-87a0-ddae76e28947 | -20.08279 | -55.95668 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9b8a4b91-e5b3-323d-ab41-f893c228bb4b | -20.08201 | -55.96115 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3f806175-82b1-3e4c-8c56-1a60957fcc14 | -20.07915 | -55.95595 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 31cdfc3c-96ee-3571-8d84-b74fd290039a | -20.07837 | -55.96041 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5bc51f03-2502-3122-b0dd-2b18b89d9261 | -20.07758 | -55.9649 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 97bd0326-e43f-3b36-b4d8-ab71d4fc4602 | -20.07472 | -55.95969 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 88b2d5f1-ff7d-305e-89fe-c74a5456d8cb | -20.07187 | -55.95449 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 85951f9e-2484-3368-be15-16cd69c566f3 | -20.07108 | -55.95897 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 999a051d-5d30-35e5-a9aa-3e4e8c9d26f7 | -20.06823 | -55.95377 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 76575693-e9c8-3bb3-961c-5931f4611da0 | -20.06744 | -55.95824 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4a18888-cac3-3f14-93c9-518c670b8d66 | -20.06459 | -55.95304 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a24d5c2f-f898-3380-89f6-7b07030a7e20 | -20.0638 | -55.95752 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b7317c83-f4b7-374f-9e13-60f5585f3ce2 | -19.67659 | -56.47813 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a80d8fa8-7e98-3f3e-bf07-af35bec80699 | -19.65265 | -56.57079 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7ad18bce-7dab-324b-bb86-56695f35e1ff | -19.65179 | -56.57564 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 77720ff9-59f3-3e0b-96c3-fe829336fc56 | -19.6514 | -56.57276 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 705ca309-1652-3eb1-bbd4-ebf4e97404c7 | -19.6506 | -56.56034 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b9697f75-bcd8-3676-ad10-df52bf1c0b26 | -19.64973 | -56.56517 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1b9217fa-79c1-3aac-8322-63040f8e6772 | -19.6494 | -56.56234 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| baa4ee93-957b-326c-b07f-74ef36345011 | -19.64887 | -56.57002 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a75672dc-1428-378c-bb9b-f044524f3165 | -19.64851 | -56.56717 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4500de24-9dc4-342c-b2cf-6ee259d9e20b | -19.64596 | -56.56441 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef2c316a-653d-30aa-bd53-d9c4e9ecfd36 | -19.64219 | -56.56364 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7eed98af-a620-3827-b1f9-59aa17c138d1 | -19.58906 | -56.53281 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 04c7b349-3794-38d3-a14f-57c2c3632d2f | -19.58528 | -56.53205 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8c501e2c-68e9-3e13-bbfd-092796b019a2 | -19.58151 | -56.53129 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 103d4b9d-e4f9-39c4-9acc-a05279a15ec1 | -19.57774 | -56.53053 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 39460b11-9cae-3e39-b9cb-524ec78a521e | -19.57309 | -56.5346 | 2024-10-09 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d720e2b8-c848-3377-8dc5-168e11e0a5e0 | -18.13552 | -56.38264 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4262a390-79f6-30c5-a0a3-9cdf45d38c21 | -18.13464 | -56.38757 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a1fbdeb8-2300-3755-91b8-e6fc4514708c | -18.1317 | -56.38188 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 614c8d15-c958-357f-ba20-d993ba4cfbde | -18.13082 | -56.38681 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5ce6b100-61fb-314f-a491-51f165def96b | -18.12788 | -56.38111 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| be607061-a576-3dac-8bde-5149b0e8f901 | -18.12699 | -56.38605 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 731131b2-65f2-3bb3-9ec0-f0de3879cb54 | -18.12611 | -56.39098 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d3952188-5840-386c-b298-75bf109c3a3d | -18.12522 | -56.39592 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 42ae1ac4-c7f8-32b4-a53a-8416224e792b | -18.12317 | -56.38528 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6d8b3762-484c-3d89-9b37-68697bd89775 | -18.12228 | -56.39022 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9da19075-54d2-39a5-aeb4-3655afada715 | -18.1214 | -56.39515 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 86beeb46-62ac-3902-8410-78f50f6e082c | -18.11934 | -56.38452 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c865dd0d-2cff-38ec-b372-4603b92e70b0 | -18.11846 | -56.38945 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| cf5ac41d-f0e1-3ee8-a5f3-52f0f020309c | -18.11757 | -56.39439 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 142eba16-6194-36c9-8ea2-7df656611f42 | -18.11463 | -56.38869 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f243fd47-e5cc-361a-a336-745eb617fbbf | -18.11374 | -56.39362 | 2024-10-09 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |


[Clique aqui para ver as próximas entradas](README150.md)
