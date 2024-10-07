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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ebc0ab0-e3bc-3c1e-88bd-539096bccf36 | -17.07042 | -56.81573 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3dc544f7-43d9-37cb-ad52-831fd52cab9e | -17.06979 | -56.81826 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e7a8e498-3156-321e-92b9-162e716f69e9 | -17.06976 | -56.82075 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7eef9dc9-c295-3616-8b3e-814bd5dea18b | -17.0691 | -56.82328 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ec99ff03-d97a-3536-a667-434d82eb49cb | -17.06844 | -56.8308 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e0192481-703f-331b-a617-df8740aa4a1d | -17.06778 | -56.83582 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2641cb83-5182-3300-b208-1b5ac2f14703 | -17.06384 | -56.83275 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 698e4595-6669-339e-b007-4eb5aff21bb6 | -17.06002 | -56.83468 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| eea32c7d-6443-3135-ac94-bcafeda8da0d | -17.05996 | -56.83218 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ef7a6737-d8cd-3e5f-8bfe-2cc2bb553466 | -17.05815 | -56.81658 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 49f15aa3-f4df-3c4d-87f7-0b406d7546a6 | -17.05677 | -56.8266 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 301dca5c-b4a1-3593-a2f4-3f199e4f4412 | -17.05608 | -56.83161 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c105ea6e-322b-3686-936e-207b92630c73 | -17.05564 | -56.80599 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c5b81666-de73-3c0e-8071-288ac28f8c41 | -17.05495 | -56.811 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 173e1616-7b12-34bd-b718-efdf383cdf01 | -17.05289 | -56.82603 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a22f87eb-8548-3f6a-b244-6da17b4e3f49 | -17.05244 | -56.8004 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 247a06bf-4551-3a80-a512-899fd91c3a36 | -17.05175 | -56.80542 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 153e5c9d-8dcb-39d7-8bb1-11f3ca99f6f4 | -17.05107 | -56.81044 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d481c442-9467-38f8-82f1-f0c6d69b58aa | -17.04764 | -56.83548 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6b5859e4-8564-39b7-84f3-c8468286e765 | -17.04376 | -56.83493 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f43b7f5c-1f2d-3dcd-bc7a-984f0ee5ea4c | -17.03805 | -56.81877 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5b8fc04-654c-3c34-b499-8d82ca83dd91 | -17.03668 | -56.8288 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 99a85004-bdd6-3bda-bea0-066e8a669fb2 | -17.036 | -56.8338 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7919139-79c0-3f36-8793-e012b3833f7f | -17.03281 | -56.82822 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1cba20e8-d956-3c31-b638-a124373a544f | -17.02825 | -56.83266 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4803c0b3-7268-32f4-95c9-3a3bdd54f2e3 | -17.02369 | -56.83709 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3457be35-deb7-3ac4-9315-4ca13ea2acff | -17.02301 | -56.8421 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2778dc9d-527d-3fa0-8853-eb7229d7fe81 | -17.02049 | -56.83152 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d60ed583-7a5a-3f08-b10b-f3d26a96bbca | -17.14726 | -57.42178 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ee4c244a-2fdd-37be-bb86-68978ce4347d | -17.1435 | -57.42122 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ac43fb78-3559-3d83-afff-04da4db64208 | -17.14286 | -57.4259 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 45f670af-fc95-32b4-9729-67cc297783f1 | -17.13911 | -57.42533 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 28de3f5e-a7db-389d-8b27-5fbdb99d753d | -17.13535 | -57.42477 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 55fc0085-51d7-363a-8760-224ab8200749 | -17.1316 | -57.42421 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f64589bd-d1dc-3493-b780-bbd704d4e7c3 | -17.12409 | -57.42309 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 74a44fa5-6ee4-3259-ae51-698a0d07de4b | -17.1197 | -57.42719 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9d96094d-3124-3339-9496-d1215916c27e | -17.11283 | -57.42141 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 771363db-a321-35f7-8437-62c005514b21 | -17.10908 | -57.42083 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c2a67f00-a86c-3ce4-99dd-d3f889dc4105 | -17.10533 | -57.42027 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2a8d2317-6cdd-3358-9ffa-f3c5903d81c6 | -17.10469 | -57.42494 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f808f15c-6671-3d73-bac8-05f075d830d8 | -17.10094 | -57.42437 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 2c374ce0-a069-31e5-8431-4d768838e7d7 | -17.09719 | -57.42381 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| c14f5cc4-bcba-3dd7-9a96-8839fb3ff918 | -17.09684 | -57.42157 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 2e501e6e-90f9-3405-a419-6039b1598c96 | -17.09618 | -57.42624 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| d6d44cd6-74b8-3083-8b80-86f9c7760b99 | -17.09309 | -57.42102 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 7d3a3f11-4c85-337d-9b5c-85a9095ca1de | -17.08934 | -57.42046 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| ad5f40e2-c43c-34d8-9719-c1667519160a | -17.08558 | -57.4199 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 471c3567-a159-3b71-8873-1f8ebe47d436 | -17.0432 | -58.03598 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ee6c13fd-2550-39ae-94a8-06d28b064006 | -16.9345 | -57.70256 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 42135710-f083-3f68-9d35-37a155dd2a3c | -16.93386 | -57.70706 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 890989a9-5f9d-39e8-86c7-3ef531dfe0c7 | -16.93081 | -57.70202 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7f401f82-34e4-3492-ac1d-ef2d01a258ba | -16.93017 | -57.70651 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 40dbf4a1-c64d-3d9c-a0ab-5faee3c81a50 | -16.92839 | -57.69247 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| efd79b6d-168c-3928-92ab-ada8c284d6ae | -16.92776 | -57.69696 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 228b3699-3052-33e9-8dd5-2517e21edb40 | -16.92712 | -57.70146 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4fd44d6e-a35f-3673-a21e-2d8e007900b0 | -16.9247 | -57.69191 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a5f086b4-dfe5-36d6-82e2-93279fa5e69a | -16.92164 | -57.68686 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f03291db-ceaf-3c0b-be87-267105f00bb8 | -16.92101 | -57.69136 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 33959e6e-af75-3d56-b9be-bf23fc4eea98 | -16.91795 | -57.6863 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 756ce55d-ee24-334d-9a44-9842317ffb88 | -16.91732 | -57.6908 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b53bd285-c265-3eb6-af3e-4426d3cb9285 | -16.91679 | -57.47695 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 575ed537-5744-34ee-a453-cd6671546d07 | -16.91426 | -57.68574 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 792ace36-88dd-322c-a9c9-8c04d1e7405e | -16.90994 | -57.68968 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a8904429-3d49-38d4-83e6-9ce1b3212876 | -16.89211 | -57.6824 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bb5f006e-2d13-3fa6-bc57-0d312b0f1c4e | -16.89149 | -57.6869 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 014eb797-7369-38b2-866f-f15a263125b2 | -16.8761 | -57.68916 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2a6231e8-9705-3bfe-bec0-26c8b7351f2d | -16.87548 | -57.69366 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c9186983-63c4-3f22-8161-18a1872e1d71 | -16.8389 | -57.45373 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 770b7cb7-aaf2-3a15-925f-f9e48826c2fd | -16.83581 | -57.44856 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 10bd4050-e99a-3345-a927-071516860da3 | -16.82833 | -57.44744 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 83fd3791-e1e3-38f6-93d1-7385e6d75bbc | -16.82769 | -57.45205 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 159d1333-12c6-3797-bb49-5c554356fb3e | -16.8246 | -57.44689 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a83e83d6-9555-380f-b582-c33cf0c5b3c0 | -16.82396 | -57.45149 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a407016d-e05e-38fe-99d0-432bd41a2dc7 | -16.82332 | -57.45611 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 55577be6-1a77-392b-b9a3-554e4df3bdb9 | -16.82278 | -57.43249 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c5a26220-02e8-35c7-92f1-84653fb2d71b | -16.82023 | -57.45094 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e108163-b03b-3694-8630-a9f2ab1cdd2d | -16.81904 | -57.43193 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7b389241-e180-3125-993c-3bc54d49b619 | -16.81822 | -57.49288 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f23d125f-2f75-3cc8-abff-dfad483e3dc8 | -16.81777 | -57.44116 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 46fcaabf-2f24-311b-933b-d50ff8a601ec | -16.81658 | -57.42212 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 561f2670-3fb1-33c9-a358-06928340089f | -16.81467 | -57.43598 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.8 |
| 5f5d7a8b-c3f5-35d2-a8fe-9e637644ef38 | -16.81403 | -57.4406 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| fcfdeb2f-403c-3953-a1fd-92e092af40fc | -16.8122 | -57.42618 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 8d69b70f-13c7-3a68-89de-9f2158873d83 | -16.8103 | -57.44004 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 3680a862-63f2-3e0a-9a3c-e104c4f2530b | -16.80847 | -57.42562 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b2f36be8-b952-397d-ac8f-862d48412ee8 | -16.8072 | -57.43486 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 48d8873a-ba19-3c62-af40-04dcaa456a97 | -16.80346 | -57.4343 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 173ec82f-365d-3699-a87e-3aac05e59470 | -17.00815 | -56.71664 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5f6dbf39-888c-3d27-b66e-5ff9b7889468 | -17.00492 | -56.71099 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3462bfb2-78fe-3330-b0f8-3d52895c8c4e | -17.00425 | -56.71606 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ae919f8c-8d95-3b35-aa75-2a67e85d1c29 | -17.00304 | -56.69517 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dd1a80fd-9693-3a0a-8e73-69390ae3a707 | -17.0029 | -56.72622 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9b9f0209-b186-3bb1-b2a3-467c4a602dc6 | -17.00169 | -56.70533 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b1a86e3a-0b39-38a4-b9dc-0eeea510c751 | -17.00035 | -56.7155 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e7d4ce44-ba46-3c8e-8c5c-eb17ee104b74 | -16.99967 | -56.72057 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 300c9f5c-0fee-39cd-8b73-f359c5b75d42 | -16.99913 | -56.69459 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9aff88b5-1695-3f10-956b-09ccc7243512 | -16.999 | -56.72565 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9eaad79f-d491-3a67-ad10-8245d6a6c3a6 | -16.99779 | -56.70476 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d06bf183-1164-3034-ae11-b0003d69f5a5 | -16.99644 | -56.71492 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 131dc73b-2380-3aca-99f6-c3fe53c423a2 | -16.99577 | -56.72001 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README124.md)
