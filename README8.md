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
| b872ef64-23bd-3bfd-88db-e667f3d3919a | -2.5862 | -51.92198 | 2025-06-15 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44a504c0-90c3-34f8-b038-3b27abc7a5e7 | -5.42849 | -44.23231 | 2025-06-15 04:44:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 942d8ebc-a9f9-3087-8eb7-7106abc11c4f | -4.43523 | -46.11481 | 2025-06-15 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20fba7aa-f807-3cea-979b-261a5bdec540 | -3.70726 | -53.70955 | 2025-06-15 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0e45e4e-a170-3a50-9b00-0b541135a842 | -5.07176 | -43.72623 | 2025-06-15 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad669410-4ad2-3d5f-92c4-645583b0268f | -5.43062 | -44.23375 | 2025-06-15 04:44:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df25c18f-b62b-3575-9658-89ff8ea48150 | -5.07116 | -43.72375 | 2025-06-15 04:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da93e2a8-7ab6-35b7-a214-4d2a3404e3c5 | -2.58677 | -51.91835 | 2025-06-15 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b42849b-4f3a-32f9-bd3d-7c59eace3680 | -4.49641 | -43.77676 | 2025-06-15 04:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 205b739f-bba5-370a-96d2-15ab1b11dcdc | -5.6396 | -44.10823 | 2025-06-15 04:44:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23a7fb87-b144-3db7-900b-2abd914dcd9e | -4.49114 | -43.78074 | 2025-06-15 04:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb729b7c-7c38-3f4b-8247-d18b649ace9c | -5.64415 | -44.10893 | 2025-06-15 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5c68ec4-db60-37da-b913-8ab64568a833 | -5.64347 | -44.11357 | 2025-06-15 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf783a1f-5efd-33ff-addb-c78cd945413a | -2.66335 | -47.40193 | 2025-06-15 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4694a5e0-2c49-34ab-b291-eba24bc50854 | -9.4076 | -48.43413 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2330e3e-0bae-35ba-b4d4-87ae94653ea5 | -10.17488 | -52.6199 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed1c113a-45ff-3b93-a891-97f474fecc8b | -10.8498 | -53.78019 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b61b9672-7a64-3c1b-800f-ec3be1cecc5f | -10.62968 | -49.42763 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 13952039-8090-3a23-9bff-824a5b361cd3 | -10.23556 | -52.23569 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 15b22c54-097c-36a3-870f-093d65844e98 | -7.20956 | -43.10563 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 11bc5f45-a250-349a-b037-ba0a5defc409 | -11.75057 | -46.75207 | 2025-06-15 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b81e6b9d-ee9c-35ff-9dcc-be63cf36dfed | -10.63319 | -49.42818 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 68e7aa56-1dbb-32fa-8488-943847fda945 | -10.91458 | -54.75444 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de205546-013e-37fa-b7fa-856d43fdf911 | -12.97998 | -48.6438 | 2025-06-15 04:46:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16ce9799-d05b-3376-b1b4-d82a6c3d02b2 | -10.07681 | -52.74459 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82183b3d-97b2-33ca-8acc-56fd71f4d928 | -11.8943 | -47.46435 | 2025-06-15 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d5e81ec-fd1f-3262-a04a-fd94c9a19720 | -10.16664 | -48.56235 | 2025-06-15 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82a50080-e5f1-32d9-abbd-1bd5517d8303 | -10.6367 | -49.42874 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34238d09-d7ae-32fd-9313-9a696b1fb0f9 | -8.35365 | -47.08566 | 2025-06-15 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8e04fdc-a4df-3bac-aa04-94e26db8f8b7 | -9.40459 | -48.42931 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5732899d-45ba-3b7d-a1c5-377854bc3376 | -10.84365 | -53.7754 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2678d240-bc6a-3531-aaba-630ec8210624 | -9.79828 | -56.11024 | 2025-06-15 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a3e3782-0c73-3f40-8f50-f00d4d6ee935 | -7.21417 | -43.10928 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c083953-06dc-3d53-aabf-4836f493e8b4 | -11.01176 | -55.0879 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01df6f89-4c8e-3b57-8f4e-e730e4702a2a | -10.30184 | -56.97668 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324faad2-d50c-31e5-a3b3-f9e09803aacf | -10.50504 | -53.58087 | 2025-06-15 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27ee2e96-61c8-34ec-853c-29db3e7f42ba | -11.18574 | -44.4899 | 2025-06-15 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88db6ee5-d07e-335e-b0e4-d0c11feab9b5 | -12.21045 | -49.64766 | 2025-06-15 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 370d5213-fcd2-3f6e-9091-bf9c575ce835 | -12.76555 | -44.40955 | 2025-06-15 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b9a6b60a-01c7-38f6-9699-77dac7279820 | -10.66067 | -49.3629 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b9e53378-bb01-3aa5-a2c5-84cebbff6606 | -10.54225 | -47.00914 | 2025-06-15 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef42f532-2b6c-3e8a-81bb-d945528d4800 | -10.56598 | -52.0176 | 2025-06-15 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 086823f9-3515-33e0-b6f5-6b8cbedac296 | -7.44246 | -44.8245 | 2025-06-15 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2db8e906-7944-3787-ac20-5be781459e05 | -10.85198 | -53.78812 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a88b2bf1-8c3b-38b9-bb55-27a01ab2cc43 | -11.13555 | -53.94812 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab853c55-14a2-3fd4-888d-7fc54952f5cf | -7.08588 | -49.59932 | 2025-06-15 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f802c5e1-6c2f-30ea-9330-5e32f08f9762 | -11.88278 | -54.6834 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc04b38c-53bb-3240-8e04-4204b21c6430 | -10.72055 | -46.56086 | 2025-06-15 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34a3afe3-74f8-33e9-9daa-0c2e79a38c12 | -5.688 | -46.57246 | 2025-06-15 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b160808f-f9a1-30e1-a066-33b5241e4df8 | -9.41727 | -48.44436 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35281b87-e48b-3b1f-8bfe-ff58c86fd864 | -11.00822 | -55.08729 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 98eec126-c2a2-3d76-8f5d-76a43401cc30 | -8.3074 | -46.19997 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e695e3-dc93-3ea4-98c6-d38545b2a367 | -10.91108 | -54.75386 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f4b1dd-416c-3bda-abe3-431d5058a1b1 | -10.85596 | -53.785 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fe50fc2-046b-3c8f-a2ad-0b1ec9fe6a73 | -11.01024 | -55.07505 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7d870140-5a76-3352-a4ef-f2a529d79eb2 | -10.87 | -54.30128 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670828ea-5542-3af8-bb97-46a02d18d9bc | -7.0733 | -43.75058 | 2025-06-15 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b8a1423-cdc7-35c7-96b6-f232a0149c56 | -7.23072 | -44.16285 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0013f720-6297-3491-ae61-57265df892ea | -8.64861 | -48.89842 | 2025-06-15 04:46:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 391a4909-ef52-3b28-91c8-accd72d20427 | -8.96682 | -47.971 | 2025-06-15 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 603ec90c-8dba-362e-9d8f-f93f4a5a7996 | -10.23886 | -52.23621 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 76ea84ff-3d06-3115-ba2a-b08f18b8c155 | -10.45629 | -47.95104 | 2025-06-15 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4013f433-b3a7-33e7-8d5e-1917f8e14c54 | -8.31509 | -46.20487 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95bf45c2-24b6-3f77-945b-9aa8b2ee3c66 | -11.00249 | -55.07791 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46179cb8-a939-3a14-be26-ef6cdd23134a | -8.31458 | -46.20854 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b92bd55-7695-31d4-9216-a19a666e2638 | -5.68413 | -46.57193 | 2025-06-15 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3799afb-2033-3a73-9ca6-16f7ad32c09f | -10.17157 | -52.61937 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fac8d53-a280-3400-81ac-493bdf73f9d3 | -11.13616 | -53.94442 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0bcfcb-6522-33d2-8eb6-b925e875f9b9 | -10.63728 | -49.42473 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca58bee1-ff3f-34fc-9b48-6177e4a84850 | -6.44094 | -45.72847 | 2025-06-15 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae23f0c1-e11b-31a3-9a63-691d51035f7c | -9.4179 | -48.44007 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5075d97c-71ad-3b3b-847d-25021c7983c8 | -10.06932 | -49.69438 | 2025-06-15 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fc0eaf2-6d09-333e-a7d4-9388217996f9 | -9.39855 | -48.41961 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f9d142a-ef76-377d-b67f-c211a8d0c34e | -10.91676 | -54.76294 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a0fc59a-2694-3b0a-9013-375812ab70ec | -8.64807 | -48.89895 | 2025-06-15 04:46:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d231ea-16d7-3873-97ba-58737aa2a8fd | -11.89383 | -47.46783 | 2025-06-15 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeee5f50-c743-345c-9a3d-c0e1ff6c7b65 | -9.05343 | -47.91251 | 2025-06-15 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42419485-c1e3-3a52-b729-96f0c9ae7e10 | -9.14755 | -48.97376 | 2025-06-15 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b8be9d2-e81d-38e2-a18b-f45044d768bf | -11.01092 | -55.07098 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00e90ecb-c4a1-3e90-8b8b-d28e9247891f | -10.66361 | -49.36745 | 2025-06-15 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 70a13759-568f-31d1-b387-233882149cde | -7.20457 | -43.10485 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6b204a3-5e56-3383-9255-051c590de2ad | -7.20368 | -43.10879 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 77e11da2-b6ae-3fbc-87f4-5de0631f07a2 | -10.93116 | -56.84008 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95fb4fd4-0a01-37c7-8fa9-ab56883ba28f | -10.5084 | -53.58142 | 2025-06-15 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f913894a-95df-33f7-9f3e-a5eb7e322472 | -7.20419 | -43.10773 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e3a5426f-e3f2-3212-b062-d46154fe004c | -10.9196 | -54.76749 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0e32400-a51d-3bc2-86ec-23d5d9fcfa02 | -7.21378 | -43.11216 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d565e542-3406-3f9f-8192-eca44144ee56 | -9.42091 | -48.44491 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f81dc402-e2d6-3287-8fca-36e0a86d5f44 | -10.84703 | -53.77595 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c2241b-0189-3e98-8077-bc8884bad8d0 | -8.80495 | -49.82745 | 2025-06-15 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f5b39e-fc7c-3418-a374-c0a1691d6669 | -8.31151 | -46.20059 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7646b67-dd58-34dd-a49e-f983cc736a81 | -11.72904 | -48.87564 | 2025-06-15 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbcc843-76bd-331f-98d2-cf541b974842 | -7.23868 | -44.77182 | 2025-06-15 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc24add8-62ca-36ac-9dfd-535639a04883 | -7.23004 | -44.16769 | 2025-06-15 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc9479ca-b2f8-36d3-8e9a-27f1d7731a29 | -11.78457 | -54.76759 | 2025-06-15 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5091fa9a-52b2-3305-a980-36c4328a760f | -8.37177 | -47.04973 | 2025-06-15 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f815d3-52bf-3abd-8c6b-037b108b4d62 | -10.74784 | -48.57818 | 2025-06-15 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcce2999-ac0f-34b7-86d7-6c6867208ac4 | -10.27989 | -47.61269 | 2025-06-15 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 614bca0d-a01f-33cc-84d1-ce26e660b18d | -12.60638 | -47.07575 | 2025-06-15 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7858685-2739-322e-9229-f5dfc1f6e2e4 | -7.20879 | -43.11139 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README9.md)
