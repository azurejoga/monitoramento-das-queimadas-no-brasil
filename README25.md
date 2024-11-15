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
| b2a94242-08c8-3f2f-a197-18844aac31b1 | -17.69702 | -57.54691 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e99d6c40-b7df-3acd-900f-f197e5f44225 | -17.25248 | -57.47513 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c6b201f2-eb2a-3e2b-89b0-ad2740b4e3ac | -17.58302 | -57.44922 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c9045ee9-b9b8-38ff-b39f-f5c01aadd8cb | -17.69202 | -57.48748 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 38ab6310-5877-30b3-a00c-dc55a4328b8c | -17.58467 | -57.48355 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 93af5bc4-24a3-36a2-bde4-60172e050595 | -17.6185 | -57.55116 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f9fd12a8-58c9-343d-baab-cab549afda57 | -17.69994 | -57.55237 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 72af2d5c-90a5-315a-879c-bb122d6d28de | -17.6436 | -57.54137 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0c738295-a569-3589-a1b7-136a0d6fb688 | -15.90706 | -59.10803 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 902d9440-2bcc-3266-be67-9bfc2707b959 | -17.04605 | -57.43603 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b7a5b398-a539-31f2-a5d2-12eb5d56de9d | -17.62892 | -57.55808 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| b5d8ef7a-6528-3f1e-89d4-8a7a2ea4e20b | -17.63985 | -57.54064 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| f6e6f054-77d7-3f9f-afa4-86ac199bb091 | -15.71256 | -59.10879 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6487a790-cb65-3887-93d3-d65db00a7ac6 | -17.25917 | -57.48133 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ad70937b-42b4-32e3-8a5a-b457e17a626b | -17.5851 | -57.45933 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3667665e-e179-39f6-b9ec-e02e877525bb | -21.34245 | -54.41756 | 2024-11-15 04:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e44f584-127b-32bd-bca6-4e083d2f5fd3 | -17.63148 | -57.54389 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e4f2458f-6cc1-303f-93f0-e847ca9b18e3 | -17.65047 | -57.45999 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| eb761cc1-3ff3-3fec-8dcf-aac379d78fdb | -16.01991 | -59.37884 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8bf296e-97ee-3d82-b336-2c1ed3fe8cf1 | -17.29359 | -57.30849 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4bc6f8a3-510d-3713-9c74-e1b9eb1c3479 | -17.23451 | -57.46675 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 87e1d621-59bc-3561-8aa4-9fbfaf30ca58 | -17.62351 | -57.54971 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d6f7bcf9-655f-3d48-a46f-8f78460c53d6 | -16.95889 | -57.63779 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3cabbfe9-e1ed-31b3-bca7-57b894087427 | -17.69743 | -57.52258 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| af84527a-42b3-3a49-8af4-939755088d79 | -17.64076 | -57.4508 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 996148d5-1c61-3a24-8ac3-45f52483f59a | -17.57627 | -57.57486 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0eadcc25-873a-3698-9220-dbf6aefdbe30 | -15.85449 | -59.29743 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41eb5f3d-2390-3bd6-bf2b-9cce9884bd63 | -17.5738 | -57.5449 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2ffdd0e1-5bb4-372a-b265-e705c97bb11a | -17.57796 | -57.56535 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 2625052c-bc57-3ff2-8acf-c1279b75e002 | -17.25416 | -57.46566 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 6cd0265a-e04d-3f71-99fe-b8ec31b77f34 | -16.9533 | -57.64678 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 846729bf-dd40-3899-9c59-d17c339474bb | -16.02016 | -59.40125 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef2353ba-a6c1-3e42-8911-7ee512b2ab59 | -17.63268 | -57.55882 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ca7a36c3-d992-37a2-9292-f9867dae3dd0 | -17.61936 | -57.54643 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 25a88e7e-67f4-3854-9118-7d28f955547f | -17.55584 | -57.5365 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a1e6764a-3819-3312-a8b0-b545e17ecde1 | -17.5672 | -57.5557 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| c9b3be33-a94a-3d12-b996-0aed82bb7b82 | -17.235 | -57.4516 | 2024-11-15 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| d21589e8-d580-3c71-b38c-427228c72da5 | -17.2543 | -57.4698 | 2024-11-15 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| 0d01a1fa-c060-3a52-a675-362dab0b0bbb | -17.646 | -57.5463 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| a5276e07-44f4-3847-ba59-4f8a06a3e908 | -17.2547 | -57.4493 | 2024-11-15 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| fc289d16-24e7-3541-94b1-5b632cb1f3c9 | -17.5675 | -57.5351 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| 949535ba-85d8-3818-becf-5e040682503f | -17.2347 | -57.4721 | 2024-11-15 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 89e2111b-0541-36aa-a8fe-3e9b7d0405f4 | -17.626 | -57.5692 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 2d66e0ef-1757-3c81-9222-554d28d55d34 | -17.5882 | -57.4711 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 6e3b7444-c37c-317e-bd87-8cf691827e04 | -17.5869 | -57.5533 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.6 |
| 8c9202bf-811e-328f-aa8c-a1c22918aed6 | -17.5668 | -57.5762 | 2024-11-15 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| c7b55710-108a-3343-80ad-ce2c09b70053 | -17.5879 | -57.4917 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 3f935e61-57d3-3530-96ab-139f4d26d158 | -17.6263 | -57.5486 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 12e9031b-dcaa-391e-bc0c-42e74ae1f2ed | -17.5865 | -57.5739 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.2 |
| 784c99b6-0424-3ddf-933d-6464e548b5b9 | -17.5678 | -57.5146 | 2024-11-15 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| ea13647a-eb92-3759-ac62-fbfed7caa168 | -23.59816 | -54.73862 | 2024-11-15 04:50:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 707ff0d2-df34-3f51-b278-bf40c86ab0b6 | -22.86781 | -54.65586 | 2024-11-15 04:50:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c73c6860-cba6-37d7-a69e-f9d0f4b4bfb9 | -22.87055 | -54.66022 | 2024-11-15 04:50:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a4a4b134-b8ed-3ddc-a75e-20f06e3fa8f3 | -22.86722 | -54.65961 | 2024-11-15 04:50:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| fe5bb7be-252d-3cd3-8148-9313622aa202 | -23.71373 | -55.16608 | 2024-11-15 04:50:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eab87fa6-8acf-3b64-88cb-b391fe93cfd1 | -23.64692 | -54.55717 | 2024-11-15 04:50:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a0e73594-5a3f-3800-9882-7ee1ba338e8a | -23.59424 | -54.74179 | 2024-11-15 04:50:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 78bb7a0b-254c-3b15-8632-48431664e19c | -23.64924 | -54.5799 | 2024-11-15 04:50:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7dbe12f5-5b1b-3cc6-932b-26ffadf91ed1 | -23.73393 | -55.38385 | 2024-11-15 04:50:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f1bfc33-ea9b-3e67-871e-00c021f715bc | -23.7358 | -55.38713 | 2024-11-15 04:50:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 317fc175-dbf5-32ce-b610-307fc0a0cea5 | -23.7104 | -55.16545 | 2024-11-15 04:50:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69519ed9-9572-3913-8df3-78c836432c25 | -24.2434 | -50.74194 | 2024-11-15 04:50:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 623952c5-a479-3fcb-9e3a-0a8d27b03459 | -23.64983 | -54.57612 | 2024-11-15 04:50:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 54f71625-f6a0-3271-9aa8-f478c9b0c71a | -22.86996 | -54.66397 | 2024-11-15 04:50:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 651c5dc9-eb9b-30d2-9ce3-59f5c21effbd | -23.73333 | -55.38763 | 2024-11-15 04:50:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ead35892-44d7-3007-8f37-4265d24fa36e | -25.46694 | -52.74709 | 2024-11-15 04:50:00 | NPP-375D | RIO BONITO DO IGUAÇU | PARANÁ | Brasil | 4122156 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e0fd558-665c-3088-b459-372fa49fd072 | -23.59483 | -54.73801 | 2024-11-15 04:50:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf5268c0-6801-3382-ba6f-9590c111aa58 | -30.52094 | -51.65512 | 2024-11-15 04:50:00 | NPP-375D | SENTINELA DO SUL | RIO GRANDE DO SUL | Brasil | 4320354 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b813e464-2ec2-33af-bee6-adcc9506bc9f | -31.5908 | -52.93665 | 2024-11-15 04:53:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 9ff08551-e892-399b-8f04-c5f16cf2a64b | -17.2547 | -57.4493 | 2024-11-15 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 74bd4294-1b82-3d28-bb3d-6bac4de640ed | -17.5882 | -57.4711 | 2024-11-15 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 4bc545a2-209b-3466-a1dd-4ee71e5fecb1 | -17.2543 | -57.4698 | 2024-11-15 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 3151735f-431a-3afa-b7ea-8a21a6cfe14c | -17.235 | -57.4516 | 2024-11-15 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 782a9a4f-63ae-36fd-9d8e-03ead87dcdd7 | -17.2347 | -57.4721 | 2024-11-15 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| a53f9991-996b-350c-b647-87cb76fba216 | 1.0749 | -59.24042 | 2024-11-15 05:05:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db17ee3f-3778-3cec-a36a-d0b45aeabdb7 | 1.0763 | -51.14521 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9dc1536d-b2d7-3821-a51d-abea97e7d344 | 0.43541 | -50.9287 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14a71711-dc74-3312-b95d-6debdafa49b8 | 1.06836 | -51.12361 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42295542-7b7a-379a-be1e-7abbc98740b3 | 0.90547 | -50.14363 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e38b4e-1a1d-3994-9e26-4e3cb9f36859 | 1.19956 | -51.29567 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0297485-78be-3261-9aa0-cb8301a8d03c | 1.08252 | -51.13416 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15836bcf-00ac-3eda-9194-0a156a4387c7 | 0.8505 | -50.21043 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45fdbec0-8b06-395d-ba9b-4c103d60b4ba | 1.0747 | -51.13533 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d0f8be3-2e80-3880-a02e-be0c536c4b30 | 1.04339 | -51.09189 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00f4e778-dff1-30ab-b502-8e66268fbb96 | 0.43886 | -50.92466 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56e27ddf-c704-3235-ad93-681db4418a8e | 1.30028 | -60.41195 | 2024-11-15 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 802280a5-8c11-30eb-8005-41af80f50654 | 0.90965 | -50.14298 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a2c2c37-79e2-3004-94cb-a1ca8b9f27cc | 1.07143 | -51.14345 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63b56e71-5159-3327-a78b-f4deffee123c | 1.0761 | -51.14777 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d329f935-6a51-37b6-a676-ff6f7cdea14e | 0.11665 | -49.84798 | 2024-11-15 05:05:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 348575e3-3106-3e05-ba1b-a72f4232745c | 1.8241 | -56.43976 | 2024-11-15 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09f1b54d-0d69-3f88-a045-0eeb4f86365d | 0.44686 | -50.92342 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a5e5406-23cf-3816-a28a-43341f0182d6 | 1.0755 | -51.14028 | 2024-11-15 05:05:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa07a601-b141-367f-987f-b919906e1ab5 | 0.4434 | -50.9275 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| baba6766-6392-3fb5-aabd-712775b1d143 | 1.30424 | -60.41133 | 2024-11-15 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e746f96-463f-3ae8-b70d-8d12c1d0de6f | 0.3871 | -50.88288 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7cdb614d-1917-3864-855e-aec62c63a680 | 2.58085 | -60.69551 | 2024-11-15 05:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61215e4f-06c9-3efa-9640-611623ca358b | 0.12097 | -49.84731 | 2024-11-15 05:05:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec79c33e-7fe1-3d17-81e3-f107ccca0bdd | 0.60722 | -50.85184 | 2024-11-15 05:05:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3314cb37-7868-360f-98ec-2f1141144b06 | 0.4394 | -50.92809 | 2024-11-15 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README26.md)
