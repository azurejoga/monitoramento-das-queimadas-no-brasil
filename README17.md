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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf2ebd87-4fea-3714-80d0-568236a38559 | -17.045 | -56.0667 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5dfa0054-ed7b-3372-b804-3695e90c4077 | -17.0804 | -56.377899 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 861df152-38e4-3780-bd7a-cf506257f8e1 | -17.147301 | -56.744099 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79807427-985b-37b9-bf70-3385714a0384 | -17.137501 | -56.7463 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 835e374a-6212-3db1-8b77-0e035b055365 | -16.931499 | -55.824001 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd4d018c-6006-305c-9762-c8edd5667a56 | -16.933001 | -55.8312 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ec5fcce-3d95-30eb-9028-cfd0ff96f699 | -17.1245 | -56.7332 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce0d16f4-becd-31cc-a6ef-3db7368bee1a | -17.126101 | -56.740799 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f87234ee-b841-30c4-916d-6937d0959f23 | -17.127701 | -56.748501 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75ee175b-1ccf-3e1b-b344-51b49c22590a | -16.918501 | -55.8116 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc36c242-6ab5-3bdc-9cb0-47f0e8975f0c | -16.920099 | -55.818901 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d9bacd11-489e-34d9-ab55-8e4d5c158e81 | -16.9217 | -55.826199 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccbd9fe7-2573-3462-9ced-89e0333f78e6 | -16.923201 | -55.8335 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f55ff709-1493-33d9-acbc-38c8fb9e0d94 | -17.1131 | -56.727699 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1742551a-2250-31d5-b8fc-66c444a2395e | -17.1147 | -56.735401 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 477dc73c-872f-3a7e-a675-7aff11746e26 | -17.116301 | -56.743 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ddf45ef0-c13d-3135-a58b-5ad310b7b1c1 | -17.117901 | -56.750702 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03e39433-5e4c-36f1-96af-754d5cba02bd | -17.16 | -56.952 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81aff667-e6a7-3832-85e2-8738efda4dbb | -17.161699 | -56.9599 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bfa0d74-4387-3b7a-a64d-1ee10842675f | -16.9072 | -55.806599 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8009bf71-5d33-30e4-9869-5caa700bf339 | -16.908701 | -55.8139 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1995284-654f-356e-a25c-819d82eb8a5a | -16.977699 | -56.1362 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32e7a76d-aa08-372c-98dc-63f70b1dd196 | -16.9793 | -56.143501 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5b1c559-3ba2-3db8-978f-38f2eaa3d373 | -16.9809 | -56.150902 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9abf494-c25c-3ac6-a868-b637e4d418f6 | -17.106501 | -56.745201 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0396cdfb-3a03-3f9d-8333-a461296b87d5 | -17.108101 | -56.752899 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9b3ca4a-731a-33c9-b1f8-18ed7f65a64a | -17.1098 | -56.760601 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23490ffb-8fb8-3264-9f11-58ed91871756 | -17.111401 | -56.768299 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a78f4b56-c78d-3a6e-933b-b9d06e403fc6 | -17.113001 | -56.776001 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 845ec12a-0fe2-3440-a931-3830ac5fd003 | -17.114599 | -56.783699 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3845318-2ac7-3ca5-8b2e-1307fdfab2e4 | -17.116199 | -56.791401 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ed40900-ea9d-3959-b0bb-868874c07c41 | -16.966299 | -56.1311 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf6df405-ead2-3594-92c2-3145ad2e609a | -16.967899 | -56.1385 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b6f30ce-7891-31a1-a5a8-312cf12f37f1 | -16.9695 | -56.145802 | 2024-10-05 01:07:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 153f2924-b1a9-365e-92bd-b0b3a4621668 | -17.0791 | -56.6633 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 640c6c2d-9529-3e78-95b0-73d4e6ea7194 | -17.0807 | -56.670898 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb86ffdd-93b6-3fc2-9aa6-6a15c48080b0 | -17.0823 | -56.678501 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1abff098-306a-33c7-9a03-412955748540 | -17.103201 | -56.778198 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8e885ab-7d12-3f8c-9fa0-ecc476699b3a | -17.104799 | -56.7859 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c33e3be6-368a-35bd-bff1-1daab46772d5 | -17.1064 | -56.793598 | 2024-10-05 01:07:48 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8338615d-f46a-3f88-9ada-b9002d8951ce | -17.0693 | -56.665501 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fbb8e88-3ec1-3648-9eec-d320ea557ac9 | -17.0709 | -56.6731 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 573ffb0d-75ad-3ac3-b282-8e0dac707b6d | -17.0725 | -56.680698 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c511adb-117f-39fe-8f5e-9fa46b742115 | -17.0886 | -56.757301 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43439b9e-e9fc-3e71-ad1c-db07dd3e80d2 | -17.0902 | -56.764999 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17b14ad2-ded5-3dc5-a19e-28a33c07f7cd | -17.091801 | -56.772701 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3fd8ff6-5c87-34ce-a245-adc646ac843e | -17.093399 | -56.780399 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 241fd846-6422-3c01-99f4-5db3869b20db | -17.094999 | -56.788101 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7860295-f0f9-3ca8-ac9a-8d31658e86b3 | -16.884001 | -55.842499 | 2024-10-05 01:07:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af46dd92-90b3-375a-88d8-c765ab538ef4 | -16.885599 | -55.8498 | 2024-10-05 01:07:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0082865-915b-3f41-b0f0-0fbdb6823114 | -17.0595 | -56.667702 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de84b597-b764-39fb-a7b6-a19d3df0d4e7 | -17.0611 | -56.675301 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0696e2e-d82b-3975-874d-73da2e703420 | -17.0772 | -56.751801 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19b22af8-7c2f-3b49-a7f5-7501f07f80ff | -17.0788 | -56.759499 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74af6736-2f70-3a1b-beff-f7d79659221f | -17.0804 | -56.7672 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a212571-9c4e-327c-a8dc-89116a823052 | -17.082001 | -56.774899 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29665fb8-3c8a-3fbf-a6fd-c00a87415087 | -17.083599 | -56.7826 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68eaaf57-3770-3dd4-934d-b81803968883 | -17.085199 | -56.790298 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 827d1d9f-29c2-3645-a211-15b7c4cc9cf7 | -17.0497 | -56.669899 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68d40074-eed4-3aa8-aaa8-f87083c7d85f | -17.0513 | -56.677601 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21a5d0ff-dd02-3105-8b35-f82207480097 | -17.0529 | -56.6852 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 413d2a3f-8b22-346f-a632-41fc02258628 | -17.054501 | -56.692799 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b431799-a4f5-3cc7-8faa-5dc14cf80758 | -17.073799 | -56.784801 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60847e01-2cb1-3777-9a5e-61eb4d6f8118 | -17.075399 | -56.7925 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eac5519a-d585-3210-bac7-e9ee9c9910db | -17.190201 | -57.3437 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c0aa448-0869-34d9-8d2a-10ce5f0bd839 | -17.0399 | -56.6721 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2bbe757-6b20-3fa0-878b-bfc86f8c37a4 | -17.0415 | -56.679798 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 179b7275-e410-3a74-89c1-f33119e89cdd | -17.0431 | -56.687401 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6d051c9-3e62-3653-89b3-3ca426c7455e | -17.063999 | -56.786999 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b9701ae-00d8-33d7-94d5-419eeea4e678 | -17.065599 | -56.794701 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b90f503b-d51e-3177-9206-a3117041716c | -17.188801 | -57.386299 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8186c533-9aac-3038-90c0-94fa7443ee39 | -17.0285 | -56.666698 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff164a77-45ad-3dfa-af2a-83c23a7b6d1f | -17.0301 | -56.674301 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a02b4e24-26e1-3f72-b445-fff2a273b85e | -17.0317 | -56.681999 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73285d3e-5994-3b86-a778-ee492a7e7335 | -17.0333 | -56.689602 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f08a9284-cb6d-3b98-9a03-df75e1c2d1aa | -17.034901 | -56.697201 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08e7c7d5-e527-3f8b-861a-65aafe7649c3 | -17.036501 | -56.704899 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ebf89f54-add3-389c-8c3c-cc1f94996b30 | -17.0397 | -56.7202 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4b9ef8b-61e8-36cc-8438-74d8d08d03b9 | -17.0413 | -56.727798 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cb32961-9a4f-3068-86af-2cc118f62014 | -17.052601 | -56.781502 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ad7b592-c023-39e3-a786-bd318a1625de | -17.054199 | -56.7892 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91045f8a-7d94-399f-be96-cb401708f799 | -17.170601 | -57.348 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd30cb8f-9f9c-3a37-bc36-a3344180b692 | -17.1723 | -57.356098 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec2e14a3-0a85-3979-9b55-5ca0aed7bb0a | -17.174 | -57.364201 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f16fa5c-b621-38e2-ab14-b63d86fad5fb | -17.179001 | -57.3885 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea9be4ff-f820-3912-a551-25f0bc03e394 | -17.0203 | -56.676498 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7320bc5-224b-3f4c-902e-2d21c2f941b9 | -17.0219 | -56.6842 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88825cc9-9ab7-398e-9428-c4b89f02443c | -17.0235 | -56.691799 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9a43005-3e4d-3b18-8b14-8a7f4daac198 | -17.0299 | -56.722401 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e02b689-84f4-3084-90bb-f821a3670cfb | -17.0315 | -56.73 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1612b5a6-168f-3978-87da-f7c92c7db093 | -17.0331 | -56.737701 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cfe8e1a-a839-3e16-8733-45a55d251ae7 | -17.041201 | -56.776001 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5c961ff-7af9-3b6d-b77c-042ff7cbc86d | -17.042801 | -56.783699 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a0251ba-cd95-319b-8731-d7ea1e4fe883 | -17.044399 | -56.791401 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aab9cad5-1164-371f-8e49-ee772b3625aa | -17.160801 | -57.350201 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cafaccb9-f9fc-32f9-a76f-8e6733007185 | -17.1625 | -57.358299 | 2024-10-05 01:07:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57b12fe0-a2a6-3f06-8fc4-c66100ea3952 | -17.1642 | -57.366402 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf2d48fe-1bef-30fe-bb1b-e908df7f1128 | -17.169201 | -57.390598 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e046636e-5383-3e79-8338-3fcf690f1054 | -17.170799 | -57.398701 | 2024-10-05 01:07:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c657ab65-b8ec-3f83-988b-414cc315d199 | -17.0186 | -56.7169 | 2024-10-05 01:07:50 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README18.md)
