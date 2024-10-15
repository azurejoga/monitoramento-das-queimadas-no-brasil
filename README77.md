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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21a6689b-9b49-3488-88e1-efca32653719 | -10.9005 | -69.62739 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd0d22e5-c8d3-3cfd-bed5-693dc0ce0e8b | -10.88273 | -68.43622 | 2024-10-15 06:08:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9161b27f-1637-3fa2-bacf-9fa1c9e98e8f | -10.86473 | -62.33017 | 2024-10-15 06:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 705ddffa-ef8f-35e6-81a3-17a6eb407d51 | -10.86423 | -62.33427 | 2024-10-15 06:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a79cf2c4-fa96-3310-8a32-25dd1ed26341 | -10.8637 | -62.33218 | 2024-10-15 06:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 954310ea-469d-3325-845a-3d59a38297dc | -10.86005 | -69.50289 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6612f256-0b1f-368a-9add-b756be62c6f7 | -10.85852 | -62.33345 | 2024-10-15 06:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 184b4f4f-f962-3479-b515-fb82015d7919 | -10.85799 | -62.33126 | 2024-10-15 06:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8954cb1f-d4ed-300d-ae59-0305aa43334d | -10.85345 | -69.49764 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5accf5e1-df09-3b35-a6dc-ca1d7e8ecac4 | -10.85188 | -69.49895 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58b47f89-f698-302f-b6fc-6184c430c833 | -10.80614 | -69.53455 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4385b57-07bb-300f-9e10-338224ef5895 | -10.78995 | -69.54478 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83c1b4c5-5c41-3c53-8070-ad695fd66cd4 | -10.78903 | -68.78928 | 2024-10-15 06:08:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdd5942b-9835-3be7-a0cd-a7b0b66cdaf1 | -10.78837 | -68.79382 | 2024-10-15 06:08:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bef3f82-5153-3b9d-8bee-43beecdac10e | -10.68546 | -69.37296 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc2d8930-141e-3c7d-bf58-0a8292c19e8d | -10.68123 | -69.37663 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1628203d-3c7f-3449-9d5b-2d4d900f2261 | -10.68062 | -69.38081 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0e50db-8a3a-38bc-ba92-835c3d7444fc | -10.6571 | -69.39023 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15d2bdf0-ee36-33c5-a281-d41d94e9c15f | -10.65592 | -69.39088 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02231f90-2ad7-3d36-820f-f534c478c21f | -10.65491 | -69.04633 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09d49be0-84d7-32b9-80f8-f777f0f2b16c | -10.65349 | -69.38967 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 048d259a-fb30-3700-aaa3-29196bea8150 | -10.65231 | -69.39032 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43cdfbc8-47b4-3876-811b-b40bb6778787 | -10.62983 | -61.43056 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c922b1a9-a340-3ac5-b022-3fc916938d78 | -10.62382 | -61.42947 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0585e61-9e3f-3436-8e07-881585c6e26d | -10.60442 | -69.13585 | 2024-10-15 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 578ca40c-6781-375e-9067-96b7cdee017e | -10.58222 | -69.68698 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e759f16-9b54-3e58-8e6b-b505f149b1a3 | -10.58161 | -69.69102 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8879d92f-ff1d-3848-93bb-64eef6680ce6 | -10.46732 | -69.36426 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 508a3344-dda7-3163-b866-de1e4e160867 | -10.46526 | -69.72422 | 2024-10-15 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a805b4-8fd4-36ff-ac82-65bb023506f4 | -10.45148 | -61.27194 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcd356c0-d183-30a6-a711-30364acaa6af | -10.45097 | -61.2704 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ade30a7c-4d8c-33ab-81af-60265793f719 | -10.44596 | -61.26627 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa1cb864-0b11-3337-96e7-eca38abb1082 | -10.44552 | -61.2645 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86617529-f063-3b8b-a816-fc178b81f4f8 | -10.44536 | -61.27139 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0bd9e84-fc8e-3b93-85ff-81d379f8813b | -10.44487 | -61.26969 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdd148eb-7781-36d1-92fd-05836aee073f | -10.44484 | -61.27576 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f077fa-3142-3c62-b7e0-1d3ea64ec51e | -10.44429 | -61.27425 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d95acee9-892a-36b6-aa84-e0d1e6ac932f | -10.44375 | -61.27859 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7af23ee-9049-3286-833d-9894a6a31351 | -10.42401 | -69.5352 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 652b03b6-2fca-3ff7-90cb-61f2a0ea5b23 | -10.38188 | -69.50936 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e5a2241-b87c-3efc-b2fe-2eb5636ee16a | -10.3783 | -69.50882 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f47e2b0c-8100-3ec5-a6f5-83a34e5f94f0 | -10.3777 | -69.5129 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67d2d092-e9a1-3ff6-a812-749b513c08a7 | -10.37486 | -61.18683 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d8a4f41-dfd5-3974-bf0a-88f7497f8d2d | -10.37425 | -61.19162 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 69445e57-cac9-3bfc-a97c-101327f0bdf1 | -10.3742 | -61.18781 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e3a478a-0413-3fdd-904c-1c01faece91c | -10.37364 | -61.1964 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c5cca9c8-f68d-372a-98f7-e252037f02de | -10.37363 | -61.1926 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10fb9276-d6b5-36da-bb6b-96c6a9a5e203 | -10.37305 | -61.19738 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a9f9d54-862b-3269-a79c-5149e97817a7 | -10.36933 | -61.1813 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8023c5e4-ec26-3e1d-943b-abce27a3e7d5 | -10.36921 | -61.17749 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af9c77cf-2904-3464-8397-2a403aac2e36 | -10.36873 | -61.1861 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a3805c8-b61f-3979-a9c0-08071b596c98 | -10.36864 | -61.18225 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4aae6a6-d466-3673-817e-673f60431a0f | -10.36812 | -61.19086 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e0061f8-91db-33ac-acaf-ec7b70d32b69 | -10.36807 | -61.18705 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f8b44221-f66f-3a34-8d4a-50290e34a931 | -10.36752 | -61.19561 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8fd03554-6ef3-3b0c-8b70-90f662621c2e | -10.3675 | -61.1918 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75709b25-a633-3a27-bb97-5436398d84d6 | -10.36694 | -61.19656 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5040cd02-322a-3f6b-96ee-fde30172c353 | -10.3632 | -61.18057 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75987ad6-1301-35bd-8e84-4b19957075a7 | -10.3626 | -61.18534 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c94ec076-eafb-30ad-857e-2690093b87f8 | -10.362 | -61.19007 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d86d73b-33af-3cd2-be1c-74e150cbffed | -10.36195 | -61.18626 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 870da59a-3e81-3ec4-8de0-f4ddb5a6168b | -10.36141 | -61.19477 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53c2eaba-824a-30d8-be26-2313ff8c2061 | -10.36138 | -61.19099 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b86c6af8-6a61-374f-9421-b58c19fd8022 | -10.36082 | -61.1957 | 2024-10-15 06:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d90db1d5-ba58-34d4-aa59-ea0e7cc60b14 | -10.32523 | -69.47133 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd5ed1dc-4cd7-362a-863e-fc141f68a29f | -10.32463 | -69.47545 | 2024-10-15 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac29e0f5-40dd-30f1-9bcf-164b83ff3f10 | -10.2611 | -63.10717 | 2024-10-15 06:08:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73a2941f-ae42-3690-9846-4fa97427cfbd | -10.25568 | -63.10655 | 2024-10-15 06:08:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fa8a9ab-154a-3721-9b48-5b4c2d417153 | -10.0102 | -62.10252 | 2024-10-15 06:08:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdcd1046-56db-32b4-9b3a-6e47114af77d | -10.00968 | -62.10658 | 2024-10-15 06:08:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62acbb55-76bc-36da-a9aa-031416a6bdf1 | -10.00393 | -62.10584 | 2024-10-15 06:08:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f332ad9a-47f5-3402-99b1-44eb1425434b | -11.6917 | -65.2243 | 2024-10-15 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9755f382-e8c1-3692-b154-337aac72ad52 | -10.37864 | -69.51433 | 2024-10-15 06:31:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44e1b29-465b-37eb-81a3-4d7b592db4d0 | -10.37906 | -69.51089 | 2024-10-15 06:31:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf13a24-fd6e-328f-a088-ec62810661f7 | -10.42781 | -69.76941 | 2024-10-15 06:31:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e184aded-033e-3681-b8fa-8f683bff9f96 | -10.42824 | -69.76612 | 2024-10-15 06:31:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a7a0143-2bd0-3027-9249-655ab28db141 | -10.57735 | -69.6905 | 2024-10-15 06:31:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32651faf-c308-3300-81b9-f9e474556a67 | -10.58271 | -69.69111 | 2024-10-15 06:31:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb2a1123-e40f-3c64-9f50-6459a3883d76 | -10.65131 | -69.39188 | 2024-10-15 06:31:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f2539d-348c-32f9-a36d-def151cbf6bf | -10.65677 | -69.39262 | 2024-10-15 06:31:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fecd1f41-6426-327c-b1d6-b9441769646d | -10.78621 | -68.79138 | 2024-10-15 06:31:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6910dce3-4c67-3619-adf0-d7aeeefa7253 | -10.79189 | -68.79215 | 2024-10-15 06:31:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ce59084e-c045-33d5-a9df-2ebd0f1b3f1f | -10.92592 | -68.36903 | 2024-10-15 06:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 872f45f3-520b-333a-9f5e-5408765226c4 | -10.9318 | -68.36966 | 2024-10-15 06:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de2ffa3-773f-3d0b-9198-184e8a3e8b7f | -10.95113 | -68.2496 | 2024-10-15 06:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3e43d286-0352-3d97-8fbd-e883dee11973 | -10.95705 | -68.25025 | 2024-10-15 06:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0953dd0-f8fe-3f3c-bea5-f32c8f322d08 | -11.68956 | -65.23956 | 2024-10-15 06:31:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| adee74db-1fc9-3730-89df-4e2fb7598f2d | -11.69034 | -65.23248 | 2024-10-15 06:31:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ccce288b-1665-3287-b545-999454769271 | -13.3786 | -61.9582 | 2024-10-15 06:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5aae47db-c599-35f3-ad1c-18dd58d0397a | -17.8648 | -57.4171 | 2024-10-15 06:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 05cdf16e-21a7-37b5-af01-2f7cd4a7d568 | -17.8644 | -57.4377 | 2024-10-15 06:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 811d6d5b-f2ae-31cb-b422-696eb0d1c7aa | -17.8845 | -57.4146 | 2024-10-15 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.5 |
| f69f0895-7ba0-3f97-9e89-1cb3bef65b90 | -17.8842 | -57.4352 | 2024-10-15 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 9719a7e8-1310-3821-8e22-96025227709d | -17.8648 | -57.4171 | 2024-10-15 06:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 5e86f332-db5f-31b2-93ab-c21195d45996 | -17.845 | -57.4195 | 2024-10-15 06:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| cfd73607-4dd9-3dce-a461-ff56ea21f3ef | -17.8644 | -57.4377 | 2024-10-15 06:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 092a3b89-b437-339d-bc0f-b84d7d3560cd | -17.8842 | -57.4352 | 2024-10-15 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| b912bd5f-29eb-3fba-baf9-c7e544b74261 | -17.8845 | -57.4146 | 2024-10-15 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.8 |
| c6bef75c-2be5-3af4-beb7-1b952cf448c2 | -17.8849 | -57.394 | 2024-10-15 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 536eb367-6ec9-3fa0-b365-9386a86b9448 | -9.35053 | -63.57056 | 2024-10-15 06:57:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |


[Clique aqui para ver as próximas entradas](README78.md)
