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

## Dados Diários - Página 217

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afde612a-1107-3fae-b8df-70a82442eb3f | -18.59941 | -57.24307 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 87c9cf94-c80b-39e9-b968-4cf122db00f6 | -16.77411 | -56.70298 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5d657b4d-23e9-305a-94db-f9ce449c1124 | -16.77098 | -56.69957 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 99416ec2-9f7c-3f0a-a5dc-4bf584de74d5 | -16.76699 | -56.70218 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 965e62fd-f4f4-3743-8388-a41612ef90f0 | -16.76386 | -56.69879 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 247ac7bd-1139-34fb-a68c-201ada2b3035 | -17.14601 | -57.44728 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| ec0b0bed-2b9e-33dc-a47e-4fdf16e9a02b | -17.15529 | -57.43014 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 74c75dc3-cb7e-348c-bf03-1f53d0f945e5 | -17.15472 | -57.43665 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 514a6e22-6190-3275-ad97-aa4430681663 | -17.15468 | -57.42854 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 26d0c604-cd7a-3cea-bb55-50a289155d1b | -17.15415 | -57.44318 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 4913e876-a317-305d-8f05-3c93dbfb05b2 | -17.15408 | -57.43503 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 92b36032-f1bc-3734-b742-f04cc87f762d | -17.15359 | -57.44968 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 218e7bd6-9dc7-309d-bfbe-354f1e0fe64e | -17.15347 | -57.44153 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| ec3efd36-dec0-3d06-a243-7f758d34a269 | -17.15286 | -57.44803 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 907fc2d7-a975-3844-ad27-184d9c2444a7 | -17.15226 | -57.4545 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2f4e0ecf-6167-3edb-b753-bb34dde5cd48 | -17.14786 | -57.43594 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 899f97f1-2412-3187-9f85-75d49cf7a6b6 | -17.1473 | -57.44242 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 2e5bc80f-93da-36c7-b108-65448679b5f3 | -17.14722 | -57.43435 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5fecb00f-626b-37bc-9b43-e2f850454c05 | -17.14674 | -57.44891 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 2af82efb-d73f-366c-848d-cb1e5d69f989 | -17.14662 | -57.44082 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7e808f72-6d64-3650-9ef6-e463270a1f5c | -17.141 | -57.43514 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 61f4d16b-75be-330f-b30e-bda9e376fd48 | -17.14045 | -57.44164 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 419a90db-abb0-3709-bdda-54c5e2dd4e6f | -17.14036 | -57.43358 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 932b4da6-cb28-3653-9768-6870077e97ee | -17.13988 | -57.44814 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 887d7ce0-cfcb-3ec6-8509-6d6efa4388e8 | -17.13976 | -57.44005 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 3473bfbe-f41a-3caa-b4e0-c7c575b418e1 | -17.13933 | -57.45462 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 09f4521a-a3d8-3d9f-b5d2-2a7b708408e0 | -17.13857 | -57.453 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 4a78504b-743a-338f-a922-c902129a8a9b | -16.95444 | -56.78522 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3898d2f9-342c-3684-b8c1-a8fe0de3c469 | -16.94797 | -56.77731 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 76fe1156-bf59-3c37-bb38-4b38c89e071c | -16.89009 | -56.73461 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d5958996-a5a9-3404-aa2f-369531eb6c6c | -16.88769 | -56.72699 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 874eab72-08da-3c84-a50d-329d533706dd | -16.88708 | -56.73425 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fe9d7c71-4efc-3fa1-8fd8-680833e19b7d | -16.88363 | -56.72663 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| f35b5843-1146-3e1f-b31a-d089d9289e92 | -16.88297 | -56.73386 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 347fa86f-e433-32fa-8ed7-189250d722ad | -16.88057 | -56.72626 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5fc7ea6d-6d1a-3be6-b143-317917e535f4 | -16.87996 | -56.73346 | 2024-10-09 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4c60248c-13d6-385a-8ee1-44873edcf290 | -18.65402 | -57.20916 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e0493df9-b3da-3ca0-bd8e-58c6e4521e24 | -18.59779 | -57.2641 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 8efe98f2-9053-32a2-adca-f6621ad594e9 | -18.59475 | -57.23835 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 1be10f01-0071-304b-ac35-a3690128bad7 | -18.59417 | -57.24536 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b66984ef-0aae-38bf-bb86-ab2342318c75 | -18.59359 | -57.25234 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 6d7f35ad-be3e-3e9d-9a18-1922a23f0865 | -18.59301 | -57.25933 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 42758d42-f160-3c1e-8786-2d7d30df5d96 | -18.59242 | -57.26632 | 2024-10-09 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9b4fde10-430a-31d2-86e1-604816c20731 | -16.56891 | -58.25813 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 33f81b6b-a07a-3eb3-9d1a-95992d3666c5 | -16.56848 | -58.25955 | 2024-10-09 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 0c580ae1-145e-3320-a3bd-da7d7a023cdc | -15.71854 | -59.44788 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca3b7fce-f609-3567-ae81-b8f01f302d0f | -15.71257 | -59.44702 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc5db63-dbf8-3e0e-83a4-eea80474dfa1 | -15.71211 | -59.45144 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c0fa36-482c-3eec-85b9-2ddfc5591b79 | -15.71174 | -59.37403 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e3313d-7299-3d84-8bb6-dce2e1bd703f | -15.70834 | -59.36983 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45ce2f74-3abb-3b99-8df3-d382f58d4deb | -15.70784 | -59.3748 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bfce5dd-9c6e-333a-adbb-18e139586866 | -15.70612 | -59.45074 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40078b49-1509-3d45-a0f3-d36f53df90a2 | -15.70567 | -59.37386 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57fb8a6a-97f4-3bea-8a92-a1e5a399c25d | -15.70513 | -59.37878 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 565de6bf-4ad9-3071-a51d-0ede2601f7f9 | -15.70193 | -59.4081 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bd7c23-8087-38ae-8675-45ec41dc940f | -15.7018 | -59.3743 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fffd45c-7bc1-355c-9590-5cde55ec969e | -15.70143 | -59.41272 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e12334-55af-39f6-ac9e-034bbe2dc352 | -15.70132 | -59.37905 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f35f125b-693f-3762-b6b9-b7645be3f7cb | -15.69916 | -59.3777 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 245cff28-5a5b-3f11-9c9f-2281186e7a12 | -15.69863 | -59.3826 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d57807c1-b7e2-3584-b7ad-22453bebedaa | -15.69503 | -59.41571 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75102831-27ac-3c0f-bf6e-09363ecaccf8 | -15.69488 | -59.38259 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e5c20e3-c65c-31d9-9f2a-6c1c1020d231 | -15.69455 | -59.42012 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82394805-b63e-35ae-9904-a99b8c693797 | -15.69242 | -59.40681 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3907b5c2-d3be-3c5f-b725-ff2e096518c1 | -15.69216 | -59.38617 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6bd4d64-e757-365b-85de-2e0375990ada | -15.69008 | -59.40532 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da9d48fa-c1ea-362c-ada4-3bb5c79bd93b | -15.68857 | -59.41922 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66e8868-8d88-3aeb-957b-47fd8cc34a03 | -15.68844 | -59.38607 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4de55c92-2f22-37da-b254-1917926b53bc | -15.68792 | -59.39126 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a83588f-3902-3b13-8991-bd39910f8a45 | -15.68649 | -59.4054 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f63fcc35-8de7-398a-a4c2-89c5e4d07f95 | -15.68569 | -59.38972 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd6809d-1baa-377c-a83b-5603c280a47c | -15.68514 | -59.39482 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48c50d3e-a152-34f9-9d88-b9cf6a4dfa23 | -15.68149 | -59.3947 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57d31024-5364-3823-8e7a-b3b1a04edaf5 | -15.67869 | -59.39829 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b273cd0-805e-308b-bdbd-afda5a5b4a55 | -15.67504 | -59.39838 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b01a0385-ce4c-306b-9196-978ba35596fb | -15.67167 | -59.40711 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eb6ae4f-5d94-31ec-bd18-91b089ec2366 | -15.67113 | -59.41205 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6093779-2f73-33b1-83d9-6a3c48ee6b83 | -15.66563 | -59.4068 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f608547d-bc43-3926-b155-3f8423051778 | -15.6651 | -59.41173 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9806bee-9bee-30b6-a81e-231f03c68ff3 | -15.65961 | -59.40626 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1c36b35-25e7-333a-92d6-f62db6d85e69 | -15.6591 | -59.41112 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f06b503-261f-34e4-ae69-4b540f1953fb | -15.65858 | -59.41592 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c48ec03-be38-3e1b-8737-e94e9447b7d3 | -15.65808 | -59.4207 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d843d3b-4a19-330d-ad91-b14d42e817b8 | -15.65757 | -59.42543 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f12be94-32b8-38a1-bf7a-68f2ec462020 | -15.65578 | -59.4422 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a46118-1386-3dac-b549-5b0b4f11043d | -15.65538 | -59.4459 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 580371c7-c9b6-353f-b9d8-f0388d914825 | -15.65112 | -59.42901 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9629e4d2-f303-3170-a9df-0ed8c3ba9443 | -15.65064 | -59.43352 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a3e5a5f-8018-3ab5-81cd-416d3a10c40b | -15.65019 | -59.4378 | 2024-10-09 05:57:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc81d5f8-2182-3aa1-b1b8-ceff3465e537 | -14.7417 | -60.03391 | 2024-10-09 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97daa861-3fbd-3eba-9c82-97b46db4cf5c | -13.90811 | -60.22542 | 2024-10-09 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a2171bc-6b72-30b0-8122-dcb2d270e70f | -13.90766 | -60.22918 | 2024-10-09 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02134320-5460-3b02-bef6-4b0dab0a09e5 | -13.90674 | -60.22874 | 2024-10-09 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604c9495-1d68-357e-9391-00385171ac9f | -13.3576 | -60.56888 | 2024-10-09 05:57:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edb2af04-03d7-3cad-8815-0729b44e4e9d | -13.38645 | -61.97037 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0f61116f-1830-3ac4-8e67-1353f1f073bd | -13.38572 | -61.97604 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c5fde385-09c6-3a0c-be84-00e57b3f6bc9 | -13.38347 | -61.97158 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f1443143-f8f4-3144-9d09-5d49cc20e3ae | -13.38154 | -61.9697 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6a920e48-60af-3800-963c-2e42e2e7b72d | -13.35722 | -60.57212 | 2024-10-09 05:57:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6f7339f-20bf-33ae-b202-482b2da4cd71 | -13.52363 | -61.73739 | 2024-10-09 05:57:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README218.md)
