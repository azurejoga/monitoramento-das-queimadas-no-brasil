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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe7e076d-56fc-32e0-8920-f57529aa6481 | -19.6457 | -56.7471 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 49e71b60-814a-3566-ae05-e80f58100313 | -19.6461 | -56.7261 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| f9bc83b6-3788-3877-8f0d-a4ef43a3f28e | -19.6655 | -56.7653 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| a6a63ee9-1299-3261-905e-a6179cd9bdf2 | -19.6658 | -56.7443 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 387e5e71-ecc4-3cd4-b133-2320f5179020 | -19.6662 | -56.7233 | 2024-10-24 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 8b58c778-9f00-3b72-a53d-6da08fdf6b3c | -16.9596 | -57.5245 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| ab93b17b-e2e3-331e-ad49-be9631de059a | -16.9792 | -57.5223 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 7bd6877b-d64e-3f1f-b2d9-30641685e218 | -16.9795 | -57.5018 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| c21f6cf1-6369-33e6-bf62-4cea32b661bd | -17.0184 | -57.5178 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 7faca652-fa4d-3b48-b7d6-3cbe8711a93b | -17.0188 | -57.4973 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| e7259dc4-286a-31f1-ae4b-fff9731578ef | -17.039 | -57.454 | 2024-10-24 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 08a90a23-5f5c-3326-bf66-cd2d0445b3b1 | -19.5071 | -56.6619 | 2024-10-24 08:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| bda8c75a-53d4-3d1b-81e0-47b45199e3e7 | -19.5465 | -56.6983 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| a6665bf7-93a9-35ac-8d46-2ac6082cfcbd | -19.5469 | -56.6773 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.3 |
| d59aef8b-a2de-3f3e-b52f-49ea21658109 | -19.5666 | -56.6954 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| ae7122b6-0873-3204-ad9c-e0ea297cae3c | -19.5669 | -56.6744 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 2818be2d-42a7-3510-ac71-90d4a55ce64a | -19.5866 | -56.6926 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 072ad12c-3204-3e78-b76e-d3b556e7e645 | -19.587 | -56.6716 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| b4d554d1-e5d3-3c91-bf3e-43bd30b948b1 | -19.6453 | -56.7681 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| f2bd1cb1-0d09-3636-8a6f-04c487dad4c6 | -19.6457 | -56.7471 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 126.6 |
| 9cec3dc2-f562-3cf2-b51e-feacebc9f0ab | -19.6461 | -56.7261 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 2e8db62b-5747-3dc7-a6c7-c6bbe0af17bb | -19.6655 | -56.7653 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 9b73a3e9-4bea-33db-97b6-7eca539682f7 | -19.6658 | -56.7443 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| f08e267d-950d-35d6-af1a-322828d30aab | -19.6662 | -56.7233 | 2024-10-24 08:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 254c8686-e542-32ca-ab6a-8814e41f92f7 | -16.9596 | -57.5245 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| c447fc2b-6003-3149-808c-0b9af79e0930 | -17.0387 | -57.4745 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| e0fdec5d-8907-3780-ae5f-806fdf72ded7 | -16.9792 | -57.5223 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| e3017cd1-e8a5-3ec8-87fe-aa06dadcdbe0 | -16.9795 | -57.5018 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| ea9bb3a7-d41c-3bcc-86ab-e3d9aab11c2e | -17.0184 | -57.5178 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 9d2d9b0d-d7ee-36aa-bc27-5b92b408b05b | -17.0188 | -57.4973 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 5d9b6ca8-302c-3d16-8ed2-7e4d9044c8d6 | -17.0381 | -57.5155 | 2024-10-24 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| a1c812a5-86d2-39f7-8103-547a55d6ec4f | -19.5669 | -56.6744 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 713d8c4f-922c-3331-8c18-2e8d17538999 | -19.5866 | -56.6926 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 3f40d557-0237-3c9f-ba0c-a0fbb44443c3 | -19.587 | -56.6716 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| c28bb87d-432a-3a23-b67a-1dc04f3999ee | -19.6453 | -56.7681 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 82c7ac63-0d41-392e-80bb-8bdf62c9d7ef | -19.6457 | -56.7471 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 133.7 |
| 7b3515a7-961f-35e0-947f-a3333085ada4 | -19.6461 | -56.7261 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 9c0d5b13-88b0-36d0-a534-16eb4cbb3f48 | -19.6658 | -56.7443 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 66d675b7-4adf-3b2f-9110-f1efd0765371 | -19.5465 | -56.6983 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 67b4d67d-82c9-3ef6-87f8-58d46b4bc30b | -19.5469 | -56.6773 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 0182c54d-7333-353f-92b1-2ee271f38469 | -19.5666 | -56.6954 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 4218d9f0-1d56-36f8-93c7-0e7a9bdef2f7 | -19.6662 | -56.7233 | 2024-10-24 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 0ad9d30e-2fce-31dd-9f4b-066a60b0539b | -16.9596 | -57.5245 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 70abb8e2-fbd5-33f1-bd5b-4f4053fccee9 | -16.9792 | -57.5223 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| b588a108-ff55-32ec-91be-f0764d557f86 | -16.9795 | -57.5018 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 39ab63b6-9b6b-367f-b0da-06fdd54828b3 | -17.0184 | -57.5178 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 8367db09-9010-3ec8-9fa0-aa2f1d3c89c6 | -17.0188 | -57.4973 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 57447f75-fefa-3000-afc0-8e96c0e2ff82 | -17.0381 | -57.5155 | 2024-10-24 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 3a99cc3a-a39c-3308-9d96-6fb60bb9e54a | -19.5469 | -56.6773 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| d9cfb25b-d250-3dbf-8566-9e337f50f8b0 | -19.5666 | -56.6954 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 46cebef5-b2b0-34cb-a091-0166c2d5d940 | -19.5669 | -56.6744 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 4f79cb11-1b56-358b-98a0-51f6567012d6 | -19.5866 | -56.6926 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| e3757ab2-25d9-370b-9360-48682b676862 | -19.6453 | -56.7681 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 4ccb2ba0-4aa0-3878-be66-43184f1058ca | -19.6457 | -56.7471 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.0 |
| 514ae1ac-ecf0-3d43-96b3-0fa1877e971b | -19.6461 | -56.7261 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 72568637-677d-3281-8864-9d258d0d8c69 | -19.6658 | -56.7443 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 954ffd9c-a1aa-3dde-b1f9-cd4d4fd669d1 | -19.6662 | -56.7233 | 2024-10-24 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 32b1ac70-0156-32af-988a-83c31d7b54c0 | -17.0188 | -57.4973 | 2024-10-24 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 7147093a-ec16-3af4-9cb2-a601253f877e | -17.0184 | -57.5178 | 2024-10-24 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 2a93cf15-3df1-30b4-87c1-4a7644fe9de1 | -16.9795 | -57.5018 | 2024-10-24 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 1e928082-25da-3c26-b95d-3c3ebda42867 | -16.9792 | -57.5223 | 2024-10-24 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.8 |
| 8141eb69-82ad-39ed-a11a-f855eb00f8ec | -16.9596 | -57.5245 | 2024-10-24 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 94b01855-de04-356d-95cc-41523a149657 | -19.6662 | -56.7233 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 1c142313-e813-37f4-87ee-5cdca7e592be | -19.6655 | -56.7653 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| c9aadcec-0b07-3c75-b414-4250c02b2d15 | -19.6461 | -56.7261 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 1dadfb87-ffa2-3a7c-a23a-7f457800d4b3 | -19.6457 | -56.7471 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 97b2efe0-2f5d-398c-8a87-11c99647d88d | -19.6453 | -56.7681 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| bd0eecc0-d638-3dc0-9466-71189feb443b | -19.5465 | -56.6983 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| c2125685-241f-3703-ae06-291af62e4ac7 | -19.5469 | -56.6773 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 8c0d12ee-3e64-3946-bea5-f2d9a6b37af1 | -19.5666 | -56.6954 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| a770f334-4e05-30fd-b29e-730ba2330993 | -19.5669 | -56.6744 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 9c321718-7344-3714-b818-fe41ab1680db | -19.5866 | -56.6926 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 170bc8ab-e078-3fc9-b68d-2a2fb477e7ba | -19.587 | -56.6716 | 2024-10-24 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| fbd1098d-bb58-3916-8bf3-a31bf65d832d | -16.9792 | -57.5223 | 2024-10-24 09:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| ef1187c5-5a3a-3d7e-8967-87784ef15bbe | -16.9596 | -57.5245 | 2024-10-24 09:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 625f26d8-1ca8-3e2b-ad58-131e8aac32b0 | -19.6457 | -56.7471 | 2024-10-24 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 138af841-bb3a-3304-b98a-7bc4b5349ca9 | -19.5669 | -56.6744 | 2024-10-24 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 7f6475a2-b8d7-3fac-89ed-a5e011216d39 | -16.9792 | -57.5223 | 2024-10-24 09:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 214a54e3-a95a-3d60-91f5-04c735432792 | -16.9596 | -57.5245 | 2024-10-24 09:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| d8a30560-bc7f-3c80-ad96-80566859b114 | -19.6457 | -56.7471 | 2024-10-24 09:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| ef451e02-aeaf-3f00-8f80-18b9463f1dd1 | -19.5669 | -56.6744 | 2024-10-24 09:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| ac5cdd9f-1307-3eb1-b781-1b63d760322e | -16.9792 | -57.5223 | 2024-10-24 09:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.6 |
| f95d9fbc-870e-3cec-bad3-c813ec60a854 | -19.6461 | -56.7261 | 2024-10-24 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 9d12d7e7-f00b-301c-8669-c556f041952b | -19.6457 | -56.7471 | 2024-10-24 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 36b5134a-dfea-314c-80a9-6f2db5c52eb9 | -19.5866 | -56.6926 | 2024-10-24 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 8859f50a-d954-338f-b2ad-130c28329009 | -16.9792 | -57.5223 | 2024-10-24 09:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 166.8 |
| 7059a93d-2202-34ca-a5b3-44165b545e3d | -19.6457 | -56.7471 | 2024-10-24 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 7e182611-2604-33fd-a2ee-f6013af56ac1 | -19.5866 | -56.6926 | 2024-10-24 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 3df26a15-3ff3-3c64-94db-53039b3d4232 | -19.6461 | -56.7261 | 2024-10-24 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 4d418468-57a1-390b-81d3-df314b6268e3 | -19.5669 | -56.6744 | 2024-10-24 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 85964eba-5357-38f9-864a-bb7a24ecab46 | -16.9596 | -57.5245 | 2024-10-24 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 9a3946a7-d4a1-3aa5-9252-22ca00e4d1ea | -16.9792 | -57.5223 | 2024-10-24 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.2 |
| b57af6f2-0b28-3f6f-99e1-3b15483a028f | -19.5669 | -56.6744 | 2024-10-24 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| c61b985c-01b3-3239-ad8a-2d0f92a1418b | -19.6457 | -56.7471 | 2024-10-24 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 2345307b-da7f-353c-8db9-a8d6fe1332f2 | -16.9792 | -57.5223 | 2024-10-24 10:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.5 |
| b35aabe7-d2d7-3a6b-961b-f6afe60e2396 | -19.5469 | -56.6773 | 2024-10-24 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 525d1f3c-8cfd-3553-b97c-1083c296054e | -19.6457 | -56.7471 | 2024-10-24 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| 45ba8976-90ed-3ddf-a72a-252526a5cf13 | -19.6461 | -56.7261 | 2024-10-24 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 8fb95f62-635c-38f8-b4f2-61aae7fa00f3 | -16.9792 | -57.5223 | 2024-10-24 10:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.2 |
| 63e996d0-4d69-3562-9cbe-fd1e981c1e0e | -19.6461 | -56.7261 | 2024-10-24 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |


[Clique aqui para ver as próximas entradas](README113.md)
