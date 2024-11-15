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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739b1cdf-6089-3fe4-bf8d-d6cc0862b5fb | -17.6473 | -57.464 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| b72e18ab-0271-3a79-8650-974681a3832d | -4.2005 | -40.6815 | 2024-11-15 12:30:00 | GOES-16 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 95.7 |
| b7c3af7c-954e-36fc-aa57-cae415cfeb78 | -17.235 | -57.4516 | 2024-11-15 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| ff86ce4e-068c-3e29-b726-7a352e1a6f35 | -17.2547 | -57.4493 | 2024-11-15 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |
| f6293fca-2549-39af-9e89-be76db96fc18 | -17.2543 | -57.4698 | 2024-11-15 12:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 87a3767a-b9d6-3f4d-8c1a-1715bb353782 | -19.5426 | -56.908 | 2024-11-15 12:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 18b8ba74-6f9a-3882-a3ef-ffb5a927e77b | -17.6671 | -57.4616 | 2024-11-15 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| e9fe8f60-3fe3-3057-a273-b2fc3ca98924 | -17.6473 | -57.464 | 2024-11-15 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 0aae7d88-7887-3e87-902b-f95789bc38da | -17.6477 | -57.4434 | 2024-11-15 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| fe317e1d-e9cf-381d-8288-dd273abe9f44 | -17.2543 | -57.4698 | 2024-11-15 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.0 |
| 0b1a9da1-dcbd-3f4d-a64a-f9c8dd48855c | -17.274 | -57.4675 | 2024-11-15 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 3a95f2f0-b19b-3131-9a35-93c9bfc62bd3 | -17.235 | -57.4516 | 2024-11-15 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 49d6096f-6a33-3907-a97b-5111420d9474 | -4.2005 | -40.6815 | 2024-11-15 12:40:00 | GOES-16 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 1beaeb86-d73e-3b46-ac38-448f4010ca19 | -17.2547 | -57.4493 | 2024-11-15 12:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| ebdbec74-b9a3-34c6-8f60-996a2ed9ceeb | -19.5426 | -56.908 | 2024-11-15 12:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 17bcb639-2970-3d7e-9a2a-eace2295ea0b | -17.628 | -57.4458 | 2024-11-15 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| ae098be5-7763-3279-9786-b80ee55b3af4 | -4.4038 | -43.7064 | 2024-11-15 12:40:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e6054b6b-4129-334a-b6be-1b5600c8b513 | -17.6477 | -57.4434 | 2024-11-15 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.6 |
| f653106d-fb7d-3102-b5a0-77e2afa09274 | -17.7256 | -57.4956 | 2024-11-15 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| ac47fd5f-6ba1-36e2-bf29-237cd20ad2cf | -17.6671 | -57.4616 | 2024-11-15 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 7995d86c-3bc8-3271-9153-68baa93bdb1b | -17.6473 | -57.464 | 2024-11-15 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| c88e47d4-dbf4-30d0-a61f-7d8abbcc5944 | -3.442 | -42.1892 | 2024-11-15 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| eb0f64e1-a2b1-3d24-8bb3-9990d733764f | -17.2547 | -57.4493 | 2024-11-15 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 3644511f-16ce-3ff5-9448-8239688b5e35 | -17.235 | -57.4516 | 2024-11-15 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 5b5c2296-70b1-31a7-bcef-323e70e4e378 | -4.4038 | -43.7064 | 2024-11-15 12:50:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| de57cd48-325c-3de1-ac7e-eb1331856a5f | -17.7256 | -57.4956 | 2024-11-15 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 107ee0e1-483b-3aa5-a269-beeefdc3c821 | -17.6477 | -57.4434 | 2024-11-15 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.4 |
| 0b1b624e-c8e8-336e-b165-f18bebf9e4da | -19.5426 | -56.908 | 2024-11-15 12:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 5fdf30b1-4f8b-3cbb-a692-fd82eec6d45c | -2.196 | -46.1532 | 2024-11-15 12:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a8525983-fed7-3db1-8704-8068a200fde1 | -17.6671 | -57.4616 | 2024-11-15 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 4908c695-1978-35c0-b96d-8f563e8e7cac | -17.5478 | -57.5375 | 2024-11-15 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 7b0a6d46-3c36-3bec-a585-c2a7bad231f1 | -17.6473 | -57.464 | 2024-11-15 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| 4387e042-3f72-3de2-8005-1068ecf8362e | -17.274 | -57.4675 | 2024-11-15 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| a60cf570-8e93-3597-97ce-bd5f3714398f | -4.3851 | -43.7075 | 2024-11-15 12:50:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b0767935-cdfb-3a4f-b773-98554d90a98c | -16.9384 | -57.6291 | 2024-11-15 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 5cf642e9-99ab-3b63-ad8c-b0337e8d2605 | -17.2543 | -57.4698 | 2024-11-15 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.0 |
| 20fe9d6a-73fa-37ff-a941-1c8bb36c4b53 | -17.2547 | -57.4493 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| 8ed0728b-43ec-3aae-9975-7bdff6caf585 | -3.7052 | -41.9384 | 2024-11-15 13:00:00 | GOES-16 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 3a1c5ddc-ae33-3b1d-b2d4-8902d4054689 | -4.3851 | -43.7075 | 2024-11-15 13:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 70f8b2ad-78ae-3c03-a509-5c00929e443e | -1.4703 | -47.3784 | 2024-11-15 13:00:00 | GOES-16 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| be6c63f0-c2cb-3f37-8433-aa821dec174a | -17.7256 | -57.4956 | 2024-11-15 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 09fddf40-6f41-3d74-b250-9cec3b03e49a | -17.274 | -57.4675 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 21328333-281c-39f5-8816-95fc70ab7a98 | -4.4038 | -43.7064 | 2024-11-15 13:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8b872bf4-3d42-3116-a2c5-f3bc2f828060 | -7.27 | -39.1214 | 2024-11-15 13:00:00 | GOES-16 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 16d1c6e3-0203-3964-8588-96d8b5354fa9 | -17.2543 | -57.4698 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.6 |
| 5522a0a3-1c6c-33f7-bb0a-fc0b2decac7d | -17.235 | -57.4516 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| f0b763d2-bbac-3e60-99ea-2cbfbc2942c2 | -17.2347 | -57.4721 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 5cfb267a-15c6-3b0c-9b9e-ffe33549074b | -19.5426 | -56.908 | 2024-11-15 13:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 409a1532-07d2-3203-a71f-63086120fc7e | -17.5478 | -57.5375 | 2024-11-15 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 08e46a2a-0403-35a3-88d2-a8a2eb76593e | -16.9384 | -57.6291 | 2024-11-15 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 0d5b11f2-fae8-35b4-9592-a6b83deccd7f | -3.48 | -42.02 | 2024-11-15 13:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 36e3799b-45e5-3c58-8a7b-05daeb0520ea | -3.48 | -41.97 | 2024-11-15 13:00:00 | MSG-03 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 308be958-6164-3961-b267-cdf0f8c1357a | -19.5426 | -56.908 | 2024-11-15 13:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 4a96fc70-429a-3d6b-94e2-7a35afbde31f | -7.7105 | -37.4495 | 2024-11-15 13:20:00 | GOES-16 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 153.3 |
| b052eb2f-766d-3699-8d95-1b3b84a3677a | -17.2543 | -57.4698 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 170.7 |
| ce26f524-17fa-31bd-b7f8-435ef4aebccb | -17.274 | -57.4675 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 0001aa65-71a8-32f8-904c-eaca5067c0f5 | -16.9384 | -57.6291 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 3bee09d0-185d-3bed-a41d-cd731acc80f0 | -17.254 | -57.4903 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| ecc5e6c2-8124-360f-9830-c6b09d997026 | -17.5478 | -57.5375 | 2024-11-15 13:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| adc422fe-45d3-365a-9114-07e3a04f092f | -17.235 | -57.4516 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 6f93b7ff-78b4-35ea-85eb-9210eaa48905 | -17.2547 | -57.4493 | 2024-11-15 13:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.9 |
| 2a885e2c-c8cc-30a1-b810-464f3f368ddc | -17.2737 | -57.488 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 0cce4361-c613-31a3-a78e-299bbf2c96e3 | -3.4233 | -42.1901 | 2024-11-15 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| d87988b7-d3d0-3008-9344-e59c144cb747 | -17.5478 | -57.5375 | 2024-11-15 13:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| ad0c3fdb-d38f-3ae5-bb87-e11c602c8dbe | -16.9384 | -57.6291 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 20a2be1d-b92f-3ba9-a191-b1255ee063bd | -3.442 | -42.1892 | 2024-11-15 13:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 37eac6df-a897-34ba-82be-da4dcd6c6fb1 | -17.235 | -57.4516 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| bc238f1a-7fce-3d82-bcf2-4556fec876c4 | -17.274 | -57.4675 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.7 |
| 07118543-bbbb-3f44-8219-a48ffc3a353a | -16.958 | -57.6269 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 5d2b537a-352c-31e1-9a70-ab94c1d6edcf | -17.2547 | -57.4493 | 2024-11-15 13:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.1 |
| 926bd5c0-d818-36db-8e82-4ca07d192aa9 | -19.5426 | -56.908 | 2024-11-15 13:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 8b03e1a9-91c8-36ce-960d-0d3dc8038a19 | -17.274 | -57.4675 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 43ab64f0-e727-3e04-bbbe-649f6eeaf7c4 | -3.4233 | -42.1901 | 2024-11-15 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 156.2 |
| 4a48f77e-0b07-395b-b597-1de36c29a60c | -17.8066 | -57.3625 | 2024-11-15 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 38de3f62-124b-3f40-b4c9-01f1225c63ff | -16.9384 | -57.6291 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 4c31d383-cb15-3b98-b2b6-3b4f16b0acdd | -17.219 | -57.228 | 2024-11-15 13:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 5d452cc9-ec8e-38cc-a870-513ed3ebe29c | -19.543 | -56.887 | 2024-11-15 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| d1c00f25-3141-361c-b8ef-93a8e74126f4 | -17.2737 | -57.488 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 6ea5985c-8a85-3683-9b51-77b748d393cd | -16.958 | -57.6269 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| e9dc223e-de6f-3a16-a3b3-c1df615c9b6b | -17.2547 | -57.4493 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.0 |
| 52e23868-b799-3c8b-924b-2bda18ac2933 | -19.5426 | -56.908 | 2024-11-15 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| efa093e7-6b71-327e-b4de-800b3dbde2c6 | -17.235 | -57.4516 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 87a0ae79-0646-3e7d-8e7b-b48c34366fff | -3.442 | -42.1892 | 2024-11-15 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 0f777876-9e75-3bd5-bff8-daa9da5b8512 | -16.9577 | -57.6473 | 2024-11-15 13:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 514269c3-5071-3852-b20e-41efcc6b2bb2 | -17.8454 | -57.3989 | 2024-11-15 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| a2cd89bc-8ee8-339e-8461-a3e108a4d995 | -17.6066 | -57.551 | 2024-11-15 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| a6208c3e-0ab0-3683-9895-1e8b7d6dfd06 | -17.2547 | -57.4493 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.4 |
| 6a95c446-be38-3c83-8070-de6f92457f1c | -3.4467 | -41.3533 | 2024-11-15 13:50:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| f6ff5a96-5489-3f27-a1c7-4337dd3abcd0 | -19.5426 | -56.908 | 2024-11-15 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| b187256b-547a-34f7-99d4-1658ce4c6601 | -17.2963 | -57.3008 | 2024-11-15 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 85cfd4ae-3c68-3542-a2b4-de5855b0f01f | -3.442 | -42.1892 | 2024-11-15 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 40d8e08a-a14c-3875-a597-1780c3080ada | -17.8457 | -57.3783 | 2024-11-15 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 782c9dcb-d4e6-3e29-b37f-604fb4631d46 | -16.958 | -57.6269 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 77e03a5f-9e02-3317-955d-a9184c410459 | -17.8066 | -57.3625 | 2024-11-15 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| fe234f50-dc5e-3913-8331-d6d48eb73c35 | -17.2737 | -57.488 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.0 |
| 45081519-e9b2-39d7-8a1b-fdf4042ccf47 | -23.9517 | -54.0521 | 2024-11-15 13:50:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| ede35093-8c2e-3d7d-bb32-40e99fb83ab3 | -7.7105 | -37.4495 | 2024-11-15 13:50:00 | GOES-16 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 162.2 |
| e568a88a-1a9a-3bdd-bd8a-d03bd22817a9 | -17.219 | -57.228 | 2024-11-15 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 0525d086-08e0-323b-bf7f-8b4f324afb5d | -16.9384 | -57.6291 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| c46bdbba-892e-317d-a3f4-248b389404f2 | -17.235 | -57.4516 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |


[Clique aqui para ver as próximas entradas](README37.md)
