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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c477b117-3bdc-3281-8cd2-0d8df7f94d91 | -7.8727 | -45.3593 | 2024-10-17 01:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 924b18ca-e397-3ae2-9f4c-96a76b1fc6cb | -10.129 | -56.7722 | 2024-10-17 01:36:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 26db4994-d617-355d-8f28-dda835a521ae | -11.7103 | -65.2424 | 2024-10-17 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5d68be7f-794d-3b07-89a1-5cb2ec93527f | -11.7104 | -65.2235 | 2024-10-17 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ad7d2129-50b6-361f-a500-213a6c9e5e92 | -11.7308 | -64.9769 | 2024-10-17 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2d41cf11-d1c1-3b28-910e-bf22b1dcbb60 | -11.7309 | -64.9579 | 2024-10-17 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d65335ac-bc6d-3808-8ad1-7d816e0bc46f | -17.1667 | -56.8232 | 2024-10-17 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 5c9a6d17-6a1a-37d9-b3ba-5c5862a365d4 | -17.2373 | -57.3079 | 2024-10-17 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| ec37de0a-e1ad-3ff5-83a7-807fcbcb3b33 | -17.8049 | -57.4655 | 2024-10-17 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 8adca444-5243-3ca1-b6dc-38ffaa21b409 | -17.8052 | -57.4449 | 2024-10-17 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 69d2d73b-8df9-3c3e-ad6e-6eec98f1b790 | -17.8246 | -57.4631 | 2024-10-17 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 6ca8c4cb-9c3a-383f-b2c7-b7e4786a5bf6 | -17.8249 | -57.4425 | 2024-10-17 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 5c8820b7-4d97-3159-be2a-ba3b2c440c9f | -17.8444 | -57.4607 | 2024-10-17 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| d8f1c0ab-eef8-36ba-9029-2759ed14a5d6 | -23.0908 | -51.63704 | 2024-10-17 01:37:00 | TERRA_M-M | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| a00c2c8f-9cca-31ad-a3e1-9e63899a160c | -23.08859 | -51.62369 | 2024-10-17 01:37:00 | TERRA_M-M | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| d6b5a5d5-acbe-3dbe-921b-e89f931f524d | -23.0098 | -50.41591 | 2024-10-17 01:37:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 92184d43-3eaa-3f38-8797-421799947954 | -20.81353 | -56.58961 | 2024-10-17 01:37:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc2ac512-8a30-325e-8dbf-3f2b834ef882 | -20.81223 | -56.5802 | 2024-10-17 01:37:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1bf98eda-d507-3830-a9d9-63c50b900463 | -20.25262 | -55.42554 | 2024-10-17 01:37:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7df3558-5006-3d36-a97f-89a767fcf7f0 | -20.19506 | -52.14282 | 2024-10-17 01:37:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 65876428-9963-3323-9294-1ca80549591c | -18.26706 | -56.61482 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3737c410-1557-3db8-97f3-e529594fd0fc | -18.26574 | -56.60552 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1b7b5913-2f16-3269-8d98-31459f35bbd6 | -18.25037 | -56.36963 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 08324c18-e21e-3ecc-9ece-4aa8ad10ccfe | -18.24933 | -56.61763 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| d1d1ecb9-c028-3cd4-b7e2-b83c39e45003 | -18.24903 | -56.36028 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 55547b30-be3b-3a44-b352-42dde8adf6b2 | -18.24801 | -56.60833 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.9 |
| bc987875-e6de-3927-ad0a-717fd16f4762 | -18.22724 | -56.33506 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| a7a7c1da-dc12-30f0-97e2-6d311d1c007d | -17.87695 | -56.85873 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 53960395-8255-330a-8e4e-5f66abfe67b4 | -17.87304 | -56.83095 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 99474605-8f0e-34e9-bc7d-e79ce08f7667 | -17.86549 | -56.8416 | 2024-10-17 01:37:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e97d5cc6-948a-3b7b-b7e7-7f111846f99e | -17.80784 | -57.41431 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| fe0b8e3d-fe25-3432-b56a-1b151ada50a6 | -17.79956 | -57.43138 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 0ca77d9f-abc4-3975-b853-2ec788e75b6d | -17.23152 | -57.31917 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| aac49a85-d86e-3547-a7ad-fe8f9868a5cc | -17.23024 | -57.30995 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.1 |
| f2674bbf-b6c6-3504-a4a7-3e56c2be101c | -17.22266 | -57.32053 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| a66408ad-63b8-3854-b4d4-b7e438479aeb | -17.22138 | -57.31131 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 5c6b15a2-b718-34df-9654-4d09e2dc5a42 | -17.2201 | -57.30209 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 0aa447b9-e59f-3e7f-8f82-1bcb4acbcdab | -17.21637 | -56.68318 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 3989c850-a5cb-331d-b8bd-b4d8d54cc8b5 | -17.20864 | -56.94906 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 19e13d38-08ec-3374-b568-420a2ab9c07a | -17.20749 | -56.68458 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 660c4cb3-6deb-37fd-bbe6-39e93da3f36c | -17.20618 | -56.6753 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| bd475e91-c029-3b43-ba9a-56dad69fad72 | -17.17266 | -56.82255 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| beab872f-117e-3462-801b-3290c96d3884 | -17.17135 | -56.8133 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 29f7a306-059e-32d4-9434-46550c562a3d | -17.17004 | -56.80406 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| d55a8198-353d-3481-8c68-25c0d8061fca | -17.16441 | -56.83969 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 0411b4c1-3060-37b2-bab1-cb5114846c91 | -17.16311 | -56.83044 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 6657ad32-7b9a-310d-aab6-c7dcf5874dbd | -17.1618 | -56.8212 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 6884e0cf-75c2-34f4-aa6d-f7a4dc6fb3cc | -17.1592 | -56.8027 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| ccb8df18-2f40-3b87-87c7-0794d46a21cb | -17.14929 | -56.86095 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 886366ec-e159-357d-bfea-f59ce31eff92 | -17.06264 | -55.99637 | 2024-10-17 01:37:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d376d973-e3bb-39dd-bcf7-dd94df2c1a81 | -17.06124 | -55.9868 | 2024-10-17 01:37:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9bae6700-ee47-3a7c-80d1-239032f0bd33 | -17.05741 | -56.8623 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9ff7c756-f1dd-3250-bc92-7c5fe288b1a0 | -17.01935 | -56.84938 | 2024-10-17 01:37:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 599c3d9a-16a9-3761-9452-d5ee342a6f41 | -9.92561 | -57.5243 | 2024-10-17 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd274df2-d23f-3ac4-a251-c6d651a6e8bb | -9.92427 | -57.51498 | 2024-10-17 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e80087dc-3ca3-3737-9080-5f9e447e158c | -9.9166 | -57.52564 | 2024-10-17 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3e2fc1b1-1548-36b8-94f5-a62174f7db0f | -9.91526 | -57.51633 | 2024-10-17 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 72765812-b640-3d92-8bea-44e6d79fab33 | -9.61259 | -55.81406 | 2024-10-17 01:39:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91670440-f530-34a8-96e1-bfaa1bc0677d | -9.60277 | -55.81571 | 2024-10-17 01:39:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6f8db9de-7fbf-3bd7-891c-efe0fa79c676 | -9.57157 | -55.80906 | 2024-10-17 01:39:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7c83e939-30bc-3d82-965d-75d86d5c03a3 | -9.56989 | -55.79789 | 2024-10-17 01:39:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c2acaac3-c208-37d1-b52e-a89248e4e785 | -9.18981 | -59.3714 | 2024-10-17 01:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3fef5e4e-7231-32f9-89e5-3b8c6581ea83 | -9.18858 | -59.36247 | 2024-10-17 01:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9da880af-b094-3a92-be5b-935067d6b491 | -8.45204 | -66.95286 | 2024-10-17 01:39:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 61a6204e-aa59-3cec-b647-a9c1cf9bf750 | -8.44971 | -66.95866 | 2024-10-17 01:39:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| da3f2837-808d-3130-83b7-bdeb2442f27f | -17.01377 | -57.46837 | 2024-10-17 01:39:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| cee94b72-0704-3b72-b6f5-803c4ad5de3e | -16.95633 | -56.79941 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 8b3674b5-efaa-32ba-9b76-a644080210d6 | -16.94746 | -56.8008 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 9afdd61b-d89b-3e9b-b18f-5af194ceaa55 | -16.94615 | -56.79155 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 79b28339-b5cc-3cda-abdb-2711bbb2303c | -16.88503 | -56.74438 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 80951e9c-cab6-38b9-9e39-aef0816eea36 | -16.83717 | -56.67255 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 308219ae-298d-37e3-bc63-439b1f7d2409 | -16.07079 | -56.98917 | 2024-10-17 01:39:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8246407a-c258-318c-b6c6-18a072a7fa73 | -15.10402 | -56.41413 | 2024-10-17 01:39:00 | TERRA_M-M | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6cef3238-6693-369a-a702-ae32853412a3 | -15.09501 | -56.41557 | 2024-10-17 01:39:00 | TERRA_M-M | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5de75cb-2463-3956-a843-157c589f4cfe | -14.57632 | -56.7164 | 2024-10-17 01:39:00 | TERRA_M-M | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 525499f9-3e70-38ca-becc-47e1c7218a5c | -14.57496 | -56.70704 | 2024-10-17 01:39:00 | TERRA_M-M | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 540dfc6f-2ff0-3853-a4ee-e69afbe63582 | -12.50392 | -55.202 | 2024-10-17 01:39:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8db584fe-1c89-3b48-80d4-1608db016813 | -12.50219 | -55.19076 | 2024-10-17 01:39:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4d0d665a-a2d1-3de6-9b4f-70d1fb04c6e4 | -12.50137 | -55.19729 | 2024-10-17 01:39:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| d9524165-aa86-3f68-8989-9f6c6c6e47cc | -10.58869 | -67.77293 | 2024-10-17 01:39:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 63ec91ca-26cf-321d-b899-5a8f8fc705e9 | -10.57936 | -67.77922 | 2024-10-17 01:39:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 995ce8c2-87f7-3d21-9b8a-236a338fcc23 | -10.35336 | -67.95161 | 2024-10-17 01:39:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 39.5 |
| c32a1fc6-d41f-3bba-946b-8aeb875ef0dc | -10.29116 | -56.99394 | 2024-10-17 01:39:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 636a690c-f33f-31d9-aadf-28fb049fa643 | -10.19864 | -52.33731 | 2024-10-17 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a3d64a74-be2f-3833-947f-981d6a5b8df3 | -10.19553 | -52.32423 | 2024-10-17 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e78e87f9-b25d-3355-bc78-934f626d6377 | -10.19538 | -52.31768 | 2024-10-17 01:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b3c359ef-92f7-3684-b29e-a15ee464d019 | -10.13235 | -56.78123 | 2024-10-17 01:39:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 4494a946-3ca6-3e9f-bde9-bc020f6cee0e | -10.13093 | -56.77133 | 2024-10-17 01:39:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 4d2f0848-941c-31ae-9a94-dadb40e76bee | -10.12166 | -56.77273 | 2024-10-17 01:39:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 43dd6868-9d1b-3ecd-b187-7dc72166f1dd | -3.83211 | -51.91074 | 2024-10-17 01:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 16a2000c-5a7a-3a3f-9d9e-bb83c6c1cfde | -3.83202 | -51.90519 | 2024-10-17 01:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5c6dc7c9-2a27-3280-9540-e2e2378cecfa | -3.51186 | -51.11948 | 2024-10-17 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| bf188199-41f7-32ad-a836-236863a07f65 | -3.50257 | -51.12633 | 2024-10-17 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 06e0f755-a722-3578-aa49-195b6650bc31 | -3.49782 | -51.09444 | 2024-10-17 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 90b70a5e-3da8-3f7d-8ca9-c8006b8bc52b | -3.4961 | -51.12197 | 2024-10-17 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b923014f-dbc4-3695-a6e9-f94c19ec47ee | -3.35447 | -53.22565 | 2024-10-17 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| f77d701d-4a42-3589-af39-f1eb5fb185a3 | -3.35123 | -53.2034 | 2024-10-17 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 860858e2-1265-34e9-a0c8-f6957f2116bf | -3.34945 | -53.22002 | 2024-10-17 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 653a436a-ca66-3e68-b9ba-76c5655b27ea | -3.11602 | -53.74952 | 2024-10-17 01:41:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9070c966-0c3c-3ccf-b2bc-3861ec23ea15 | -3.08602 | -51.21548 | 2024-10-17 01:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |


[Clique aqui para ver as próximas entradas](README13.md)
