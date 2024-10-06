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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c1a9d4b-a863-3af0-9f68-9ec0dd571ea4 | -16.95132 | -56.62294 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ea536ad-fc78-3750-9ac9-5de138bef71e | -16.94709 | -56.61182 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 903d65a2-97ef-3d05-a7a1-90a515e22917 | -16.94595 | -56.6223 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c77c3a6e-6e0e-3d82-9f1d-34408e6637d2 | -16.94557 | -56.62577 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cfd574fe-805a-34f8-9bff-f20e7c754889 | -16.9452 | -56.62924 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 68e0d3be-234c-3366-8ff2-ff580f797a39 | -16.94172 | -56.61116 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9a787f74-cac8-33ae-9298-37060f4fdf0c | -16.94096 | -56.61814 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f137c117-08e3-3841-bfb6-84f2550e374f | -16.94059 | -56.62162 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ad8e908a-a683-35bd-8754-3415d7651306 | -16.69852 | -55.91766 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 62f0ee1c-5d95-39dd-93e3-4cd4613117db | -16.69811 | -55.9215 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3e968e2d-5463-330a-83f3-246202d0c89a | -16.69608 | -55.91116 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2b9f5e88-80b8-3f3b-8156-9fc3c5d97ba7 | -16.69564 | -55.915 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c6532a6e-d4ef-35f7-a0de-253ed74bbd64 | -16.69521 | -55.91884 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b15cdbe6-6806-3bb2-b4d0-507d6c41a896 | -16.69477 | -55.92269 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dc277d9d-16f0-30d2-8fef-dd4546cf4548 | -16.69373 | -55.90927 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f502bd67-ed79-3b2c-8e1d-fd6e66be8c0a | -16.69333 | -55.91311 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eaf70abb-c7c2-3946-a50f-de917082d5c9 | -16.69292 | -55.91696 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8d33d38f-86b9-3f93-a7da-91c863d1d231 | -16.69047 | -55.91053 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d37a0d09-7525-3e9b-a901-96572f7b03b4 | -16.69004 | -55.91435 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d53b72a9-cbb1-3535-8f21-4ec3a80bc3cd | -16.68934 | -55.89706 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c4ff95ed-25d1-36e1-bcd0-4dca9efff40d | -16.68893 | -55.90092 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 68eecf8c-3a63-3223-bf53-2db18df0770f | -16.68853 | -55.90479 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fb909aa7-80a8-3d49-90c7-520efc5eade5 | -16.68812 | -55.90862 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0dfb785f-59fd-3334-9581-4d34611388cf | -16.68772 | -55.91247 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6561ae80-eeee-36bd-a1bf-a84643b8ebcd | -16.68656 | -55.86937 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0df24267-50ff-3686-8905-02b46eff605e | -16.68573 | -55.90221 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 94ea2818-0429-3b40-9278-0511c263ffae | -16.6853 | -55.90604 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6874a000-2f7d-36bb-95ba-5c92b6b8d864 | -16.68357 | -55.87069 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4b46a911-eced-3066-8a71-6362158242e6 | -16.68333 | -55.90024 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8173fa80-31c8-361f-bb53-77a400d0ced7 | -16.68292 | -55.9041 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c382806d-a7e9-355c-a858-9d5e4834e04b | -16.68094 | -55.86868 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d827196a-92ea-3a62-b401-8522ad612365 | -16.68054 | -55.87255 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c3932adb-aea3-3707-b89b-81418ff0c418 | -16.68014 | -55.87641 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1dee9499-5f54-36e4-ad85-6034190a12b4 | -16.68012 | -55.90153 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ad4bae29-c47d-3005-8cc3-ca1baaf4d7c5 | -16.6797 | -55.90537 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 63489aed-9a5c-3b51-95b9-3877b8333af6 | -16.67772 | -55.89955 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0bb868a2-9ba8-3479-9383-dd0125d11383 | -16.67753 | -55.87388 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c91c938c-ab1f-37cc-8d77-2c9ae4eb3c11 | -16.67732 | -55.9034 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 23cc71eb-cdfc-3da8-afb4-6f708ffbe829 | -16.6771 | -55.87775 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 83ca4f5a-03d9-34bb-95bf-585d499dada6 | -16.67452 | -55.90085 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 54232e6a-0d77-3a16-af8d-ca280aab90fd | -16.67452 | -55.87574 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ecc95c01-8728-3ada-9e02-d1713e0438fc | -16.67409 | -55.90468 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6395ea20-961b-3296-b5c9-8c47a3037bde | -16.67171 | -55.90269 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 96c41a78-cb25-30c9-ad61-5a3d6aa38eb1 | -16.67148 | -55.87709 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ae9d2b8a-b1da-32bd-a66b-32972a6063ee | -16.65125 | -55.90588 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 55362ce3-86ad-3c06-b279-685de3057947 | -16.64607 | -55.90137 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 981726bb-0bc6-318d-90d4-9cf3c88831fe | -16.64565 | -55.9052 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9b89506e-d037-3f20-9d6f-6e73e040980b | -16.62284 | -55.90631 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 55471e1c-bbfa-39b6-ae1f-165bc1137e50 | -16.622 | -55.914 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| eb5f337d-5cee-3a8b-bda3-77f58161ec67 | -16.61723 | -55.90562 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2901efdf-bd93-3171-a119-6e12d6fd8b18 | -16.61682 | -55.90946 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4a541e61-e07e-35e2-83cd-911c88f8d1a8 | -16.61641 | -55.9133 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6c6ff81c-54e8-3bc8-9597-c6d67bfdbf58 | -16.61599 | -55.91712 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eb79c325-e338-3c00-880f-5779237e822f | -16.61558 | -55.92094 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0e1c91f8-7c96-3eb2-94eb-39aafe09c237 | -16.61123 | -55.90876 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3112344c-0932-3920-941d-8d4c029723b3 | -16.61081 | -55.91259 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 76b3782e-69df-364c-8b64-33b4249dc301 | -16.6104 | -55.91641 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 50d8cfd6-c002-3055-ad22-82b2b39989e9 | -16.60999 | -55.92025 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| de95436b-700a-3e35-86fd-8ee497a012fb | -16.60958 | -55.92406 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 52457dcf-f133-3611-ac95-3e10c4fee295 | -17.01633 | -56.69645 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0d775568-99ca-3d10-86e1-af8506c4c2d0 | -17.01518 | -56.68335 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a59a7e4d-8cf2-384f-ae44-3149deee4278 | -17.01479 | -56.68679 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0ef8acae-f089-3000-affd-d103b2aeb245 | -17.014 | -56.69369 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f23ff695-35f5-3f8f-a9b3-6a2890ec5a7b | -17.01361 | -56.69714 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d77e3ef6-71f3-3aa0-bf71-1503cb9a82b4 | -17.01246 | -56.68197 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 96d9d615-d8e9-3730-b1a9-8ad0d4b71ac8 | -17.01209 | -56.68542 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 500f4c78-c580-3fe9-8698-58a1b5543d25 | -17.01135 | -56.69234 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 929ed9f6-25a4-3541-a874-9ad8bae77fe1 | -17.01099 | -56.6958 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 08147187-c2bf-3d94-b5dd-cccee94a4092 | -17.00983 | -56.6827 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ec791ca6-7344-30ff-a22b-ecd2394d7534 | -17.00944 | -56.68615 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 00bbb9cd-bf0e-3ab0-9b52-11cf1c30ce04 | -17.00865 | -56.69305 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5ec23d8e-f642-3043-ab32-912557e0d766 | -17.15291 | -56.1483 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 81d78441-39d2-31e4-b9de-5076bd6fae02 | -17.1525 | -56.15205 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8deb551d-d8fe-3cd1-a8f7-3d2b4d596232 | -17.15137 | -56.47741 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 608d1c1d-7244-3cec-b9b3-3cf45d8241bd | -17.15127 | -56.16329 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| faf3ba19-9657-3341-9b20-012cffedc923 | -17.15086 | -56.16702 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 863d99fb-b4d8-3b40-b49d-d42cf653d801 | -17.14959 | -56.47815 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f60229e2-d292-308d-a21c-60c3ea984ea5 | -17.14614 | -56.15886 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ce24b2b3-4fdf-330a-89c6-ed4342ad2428 | -17.14594 | -56.47674 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6ae6f73a-f3ff-30c4-95bd-ecdea97a3833 | -17.14573 | -56.1626 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 475816ae-4dee-38e3-bf32-93f690490e8a | -17.14532 | -56.16633 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f1c994b8-fddb-3234-9ebb-81541b669252 | -17.06253 | -56.06267 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2885926a-c2a5-3427-bd93-9acb93f38015 | -17.05737 | -56.05819 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9cf650fd-3094-3369-b597-78b836f4faf1 | -16.97023 | -56.14108 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 051de00b-a372-39f4-b456-47477c1434f0 | -16.96987 | -56.13945 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 104b48d6-2b19-3fbc-bd0f-60b64b104389 | -16.96981 | -56.14481 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dc5697eb-fd9f-35e0-a6f5-7a7021941659 | -16.96948 | -56.1432 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 28c6aeed-b70f-31eb-86b0-f26c2e3a1023 | -16.96428 | -56.14413 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7a5e191a-ac61-3002-b032-79cae6ea1412 | -16.96394 | -56.1425 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 06f2421f-92b5-3aa1-a7e2-35ae1f1cc983 | -16.93562 | -55.83461 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 831ba45b-ee3e-3f19-b2b2-a5dd76c5182b | -16.9352 | -55.83852 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 273df37b-61c5-364b-9e2e-568056f952fc | -16.93479 | -55.84243 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d3d60a74-42f8-3679-8ab0-55852c126df7 | -16.93121 | -55.82215 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 94908075-6aa5-364d-80c3-8f9b2745b2c7 | -16.9308 | -55.82609 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e4d4c1c9-20c5-3907-a9ee-9e66b1577fac | -16.93038 | -55.83004 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 288ccc22-d9d5-3d56-bf8e-8e95098cc4be | -16.92997 | -55.83396 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dc9922c4-478a-3ebc-ba37-d38ebe54b021 | -16.92955 | -55.83788 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb23bfc4-1f25-3b6b-a918-3aa67441d025 | -16.92556 | -55.8215 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 83dc5254-af9e-37cf-aad4-3486713731a0 | -16.92514 | -55.82544 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 496d8b2f-23e4-36fb-8daa-d1b7c477ea0f | -16.92473 | -55.82937 | 2024-10-06 05:38:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README141.md)
