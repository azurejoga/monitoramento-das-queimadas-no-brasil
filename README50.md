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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56afe83f-f974-3c85-a2e6-b19ce41290bd | -17.68808 | -57.43208 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f7ba2bbc-751d-387b-9e17-54ee8da540ef | -17.68405 | -57.43125 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d81ef2d8-44d5-3ddd-a552-f02dd587ce68 | -17.25007 | -57.3068 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9123db05-9a2e-3d9d-8433-c1dc260ed99c | -17.22573 | -57.32501 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d590758b-67da-399b-8dac-e6b6e72daac1 | -17.20883 | -57.50537 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a11af5db-068e-30d1-8d0d-9aaca429dc42 | -17.02256 | -57.33508 | 2024-10-21 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1555b8dd-8824-30fa-bcf8-f497fc00f559 | -17.00011 | -57.52378 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 10fd63f8-e37b-37c9-af16-382e0424b6be | -16.99744 | -57.51525 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4f3b9719-9619-3e82-9018-8f8ef3b1fc28 | -16.99334 | -57.51442 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9d69f0c3-7035-31ce-932c-51f4de2847b0 | -16.95042 | -57.52662 | 2024-10-21 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cd7dd7b8-162a-3f13-b826-1a4543418b6f | -11.81366 | -57.36707 | 2024-10-21 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 393826e0-bdb1-3d48-89ff-0797925cf1f7 | -11.50629 | -60.73182 | 2024-10-21 04:40:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bba7e98-465f-33e7-9c51-7414a59f1e19 | -11.50558 | -60.73549 | 2024-10-21 04:40:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa18b9a5-9dc6-3cd5-b8ae-6853dd6f2deb | -12.54417 | -63.28848 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26ef4f87-3204-3723-a12f-5f42d22b7d57 | -12.54306 | -63.29393 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f6f563-54c2-3def-91c3-ac6063dbbf7a | -12.54194 | -63.29936 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4a0713e-0717-37b1-9693-a8d43433c286 | -12.5389 | -63.28163 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f13d86c9-abad-3645-beec-a480f06046fc | -12.51938 | -63.31145 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d98a2117-85b9-38f9-a203-78ee596f028c | -12.51298 | -63.31002 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bfd9240a-a82c-362a-b4b8-6fb652e7cf60 | -12.50658 | -63.3086 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| daffd12d-6d15-3ccf-b79d-d9ce3d39860d | -12.49582 | -63.19297 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcd0b425-6e3a-3419-b382-2a68a0416abb | -12.48443 | -63.19061 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6187d8bc-39ea-3c55-b1fa-836da2a2c7aa | -12.4831 | -63.19014 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e592148-ac09-3988-b517-265cb35fc749 | -12.47807 | -63.18922 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebde1d2-05d6-320b-92b4-cad0af602f5d | -12.47694 | -63.19457 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 212cfd72-f79f-3137-adaa-f7d828b5ef96 | -12.47581 | -63.19992 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d97b53d-0855-3543-84af-38dc752541bc | -12.47565 | -63.19409 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55344e07-723e-306b-becb-15b25507310a | -12.47455 | -63.19946 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2724782a-2df0-33e9-a779-8da9e728a770 | -12.43359 | -63.03376 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18c6aa15-f0ec-3402-93ff-24a700d3d4ad | -12.00817 | -63.51202 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a417258-651d-3f27-8dfb-6f9cc19ebece | -12.00699 | -63.51788 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34765ed-ea6f-3fe9-87b8-baf20ce6312b | -12.00608 | -63.51418 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3522aabd-5130-3795-b673-3410bdda1732 | -12.00486 | -63.52002 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 075241a5-3d59-371e-bc4e-29223d1e6cf0 | -12.00046 | -63.51639 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 565295cf-f918-3379-8d47-3e02c550490c | -11.99929 | -63.52222 | 2024-10-21 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b61073b7-9a31-31db-83be-59dc1cdd50eb | -25.19017 | -49.32705 | 2024-10-21 04:42:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c789fc29-d036-353b-a566-d1f87dbc5bfd | -25.8567 | -50.40331 | 2024-10-21 04:42:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| da7dcced-edb4-3801-8dc9-37e4812ebcb5 | -21.37815 | -55.70944 | 2024-10-21 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b35079f7-f8ca-367c-9eec-82ac6cacf264 | -21.3774 | -55.71372 | 2024-10-21 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d56eb4-6a97-36bb-9971-8520797b622a | -19.58468 | -56.53573 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 44ca6520-c40f-38f7-830a-25296a2e4011 | -19.55803 | -56.61892 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9b652ae4-311f-3309-a384-fa01532355d7 | -19.55716 | -56.62369 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9f24589b-b22e-31c9-822c-bf4933b24613 | -19.55428 | -56.61816 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0fdff46a-c4ea-3b5a-8051-efd7bee8d8bd | -19.55081 | -56.63726 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c69ceff9-5820-31d5-8808-29ded6dc4236 | -19.55054 | -56.6174 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 02d4e73f-038d-3cc8-b6d3-c60583d66ee2 | -19.54994 | -56.64204 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 163a4320-53b8-3670-808e-bfcfe7c038cb | -19.54907 | -56.64683 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af8f1048-85a2-3964-af67-d5a611076084 | -19.5482 | -56.65162 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da1361f5-711b-3811-812f-49251a831f66 | -19.54619 | -56.64129 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0e4c79ce-a7bd-3db8-aa8b-b7c951657aac | -19.54593 | -56.62142 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 78540f7f-7b35-3466-b05b-3f1a39c9fd69 | -19.54532 | -56.64608 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 518c3608-40b4-31e7-ab7e-d2eb6463c2df | -19.54445 | -56.65086 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| de9dd129-75a9-3b0f-8fea-53b57a26b5f7 | -19.54245 | -56.64053 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b0afb4f8-5ee5-3cc5-ae7c-f434bb678116 | -19.54219 | -56.62066 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7e011caf-d40c-31ad-8728-ed171d5f3573 | -19.54158 | -56.64532 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6e762e92-7e64-3017-bbde-c9bfcae4f5cb | -19.54132 | -56.62544 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c7516d77-228c-3acd-ad59-8da1defd8796 | -19.54045 | -56.63021 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0733101e-de74-3c17-b88c-8c44b57a6166 | -19.53958 | -56.63499 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 20506db1-233d-330c-9846-de8a5e2975c2 | -19.5387 | -56.63977 | 2024-10-21 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7f66c57e-637e-33df-be37-54ac39228fab | -2.7885 | -51.3618 | 2024-10-21 04:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a4fad024-6a15-3d93-bd2a-7f715de48d4e | -3.2147 | -50.7884 | 2024-10-21 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| fcfc2edb-2b86-37b9-bf70-74d213a8f74a | -3.1138 | -53.1163 | 2024-10-21 04:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| bfdfc97d-4857-3146-9b3a-a0db1dc45fff | -3.2146 | -50.8093 | 2024-10-21 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 579c982b-67a0-3339-9302-2a344851c34e | -5.6894 | -46.435 | 2024-10-21 04:45:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 81260466-5f8d-3311-800c-e4521ca19b88 | -12.5147 | -63.3014 | 2024-10-21 04:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 75252f23-7fc8-3575-b43a-f481c4499f98 | -12.5336 | -63.3003 | 2024-10-21 04:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ff5b8d03-ef8a-37fb-96eb-c54eb6f1f758 | -17.7065 | -57.4569 | 2024-10-21 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 55a45e76-b127-3254-9995-74656b075ca5 | -18.2828 | -56.0994 | 2024-10-21 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| a5e240c4-5e83-3921-8037-182d9a29d08b | -2.8069 | -51.3613 | 2024-10-21 04:55:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 17b420ee-9cae-317f-a559-494e3276b50d | -3.2146 | -50.8093 | 2024-10-21 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a7350079-a850-3dc5-9d98-77fb9792e582 | -3.1138 | -53.1163 | 2024-10-21 04:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 9203b9b7-b7d3-305a-bc16-58202f340feb | -3.2147 | -50.7884 | 2024-10-21 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a22523bc-b9f8-3306-a98c-b4fb4acb58e3 | -5.6894 | -46.435 | 2024-10-21 04:55:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| d7f2078e-ba3b-3cea-967d-e5f363cd5eba | -12.5336 | -63.3003 | 2024-10-21 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| ab67989c-b52e-3709-ab51-b65d625f65e4 | -12.5147 | -63.3014 | 2024-10-21 04:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 757b107b-522a-3675-ab68-44cf023a0179 | 1.8327 | -50.4879 | 2024-10-21 05:04:56 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4f34b33a-c70d-3941-a8dd-9ecc28bce835 | -2.7885 | -51.3618 | 2024-10-21 05:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a08aa8fa-14fd-33b4-b88a-854be5eb1ebe | -3.3877 | -45.3532 | 2024-10-21 05:05:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 11769ccd-973e-353d-8e49-024a73f71fce | -3.3691 | -45.354 | 2024-10-21 05:05:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b0b8cbb7-b66f-3902-9fd4-9786895b987d | -3.2147 | -50.7884 | 2024-10-21 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 08423b21-340b-36ec-aa69-dbb5ea5f70df | -2.8069 | -51.3613 | 2024-10-21 05:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| df14ccc5-b9b4-3552-95cc-88d8f54db76c | -2.8372 | -53.3261 | 2024-10-21 05:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 627eaa39-ff51-348f-9f4b-15bb2d5ea09b | -3.1138 | -53.1163 | 2024-10-21 05:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| da1d169f-70d8-3270-a6ae-4a7f95151532 | -3.2147 | -50.7884 | 2024-10-21 05:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 6bc2f26a-a67e-3b83-9c36-7159268409c1 | -3.3691 | -45.354 | 2024-10-21 05:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 0a7aad1c-197d-344d-932d-107c00020795 | -2.4824 | -49.102 | 2024-10-21 05:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d52f7830-bbb4-33d6-8c2d-4e4a2a478c51 | -2.8069 | -51.3613 | 2024-10-21 05:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1c6bd7ca-9a7d-3df4-9cf4-53b8b9450bed | -3.0037 | -53.038 | 2024-10-21 05:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0dcf9beb-18fb-38aa-9faf-981bf49e098e | -3.2146 | -50.8093 | 2024-10-21 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6113c560-f442-399d-8305-ccfee7db0465 | -2.97478 | -47.99152 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 623b1358-1f43-3ac6-aca6-78acb115ca8e | -2.97363 | -47.99308 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc0b0fdb-ec8a-35ca-8c37-4855276b053e | -2.96783 | -47.99047 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16758fbb-e8a4-3a72-9b6d-ed7c5535eceb | -2.96687 | -47.99689 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebb68b9b-e733-3ef2-82e9-46f7e3db13d2 | -2.96668 | -47.99197 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03afb2bc-4a43-378a-89fb-a2584e287f8a | -2.95974 | -47.99085 | 2024-10-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9f5fa89-9752-3558-bc4c-a031e4436b45 | -3.55461 | -50.30675 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c905b76b-2e24-3951-ba74-55d34bae7169 | -3.54852 | -50.30581 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28e71115-95b2-3d93-a1ee-e514590a5c7e | -3.54783 | -50.31057 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e761d157-063e-310a-ae05-9ed52279793c | -3.43436 | -49.97641 | 2024-10-21 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c034182e-a013-3b1a-b7bd-09f5bf0d3181 | -2.4692 | -49.09827 | 2024-10-21 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README51.md)
