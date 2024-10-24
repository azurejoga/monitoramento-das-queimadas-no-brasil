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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c85722e2-b51c-3103-9ba3-5d42516d1806 | -17.019 | -57.48944 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 418bc3e2-cefe-336c-b42d-2d90d6b30694 | -17.01817 | -57.51571 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 116d6864-f542-39bb-883f-25e51e92c9b2 | -17.01757 | -57.51939 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2ece91b9-e3e7-3aeb-85d4-f20172775c12 | -17.01698 | -57.52305 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1ab7e9f9-6e80-3c76-9827-9a570d0ea551 | -17.01661 | -57.50412 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 02ad54ac-c942-3d22-bf5f-d0b8affe99dd | -17.01625 | -57.4852 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9e757fa7-e74e-351a-9fd0-45217b78e54c | -17.01602 | -57.50779 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5a65225a-9171-3382-8f5e-f91d514160be | -17.01542 | -57.51146 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4e7b9ab6-fc2c-35dd-a02a-3b135f30f327 | -17.01506 | -57.49252 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b17b1ff6-51ce-36b8-af56-46d9ff088300 | -17.01482 | -57.51513 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e89cdbca-08f8-3958-8357-a47916c06c9c | -17.01423 | -57.5188 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7b591df7-a998-353b-ab99-4477b21f7a90 | -17.01267 | -57.5072 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fd300645-a6ce-3fa9-ab06-dc3d35fc07ac | -17.01231 | -57.48827 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6d0a5e0f-c8ca-37a4-9fb3-cca8798bbb9e | -17.00872 | -57.51028 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5d40b64f-3646-3d54-a2e8-75fbde52977c | -17.00697 | -57.49174 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3a75f204-977c-3753-ab08-fc2517ace689 | -17.00633 | -57.52496 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0a962b5f-c3ba-34ff-ae61-b90fff44a1fc | -17.00401 | -57.5101 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ea3b1f49-941c-3d66-b9bb-5168994ea7ad | -17.00007 | -57.51318 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 758128e5-23da-3345-90d9-a6464a389157 | -16.99612 | -57.51627 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 37bb3154-3417-3b98-8456-f8bf25b2acc5 | -16.99277 | -57.51568 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| abad214f-7b46-33f2-a120-edf4b5970713 | -16.96813 | -57.51891 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 96f0f141-ee4b-397f-9e8e-271d720c5842 | -16.96753 | -57.52258 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 6472abf7-51fd-361f-9603-2698d228949f | -16.96478 | -57.51832 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| a5f4d8ec-45c5-39ba-a475-11fbdb47617a | -16.96083 | -57.52141 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 9c766134-7db9-3e9a-8c5d-b7ab5f14b46f | -16.94899 | -57.53066 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| afcee37e-ca48-3152-961c-c8253eaae9a6 | -16.94839 | -57.53434 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| deb4902c-9722-36e5-8efb-4df30e793092 | -16.94504 | -57.53375 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 19080dfb-57eb-359a-884f-56811a1949b4 | -16.94467 | -57.5148 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 990b26b5-f950-3c3d-a03e-3536d3edbfaf | -16.94407 | -57.51847 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 931e60d5-fe5c-37bf-b543-3b036c7021d2 | -16.94072 | -57.51788 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e235b0a6-f3ad-3690-bcb1-3f90448e3cd4 | -16.94013 | -57.52155 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2cf2fae6-714b-3ca1-b51b-4741a352dc1f | -16.93834 | -57.53257 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c605ff0d-7619-3587-ada7-9b53048cd332 | -16.93737 | -57.5173 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ca1bd8c4-9dab-36c2-9c3f-5425c00098d9 | -16.93283 | -57.52405 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 540aa87a-464a-35d7-967c-18eec9e0be3f | -16.9102 | -57.49366 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| abd1fb34-48d7-3553-9a03-cd9c036e5772 | -16.90685 | -57.49307 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 52ee1153-ea58-34a8-8b95-efb463a351d9 | -16.90625 | -57.49674 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 48fd45c7-b7fa-3861-af6b-1a929fd897ce | -16.82142 | -57.4145 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 75501923-1316-3967-869e-770093c345ac | -16.82082 | -57.41816 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 50555e02-8b23-3edb-8487-3bd4ccbe3db3 | -17.83767 | -57.58555 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 76c2c544-8256-3f6c-9471-20bd24a06a87 | -17.83708 | -57.58923 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 82cc5840-ccd8-3096-bf6d-c87ccbbac0b7 | -17.83669 | -57.5703 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cca6ebe3-69a2-3a59-b4cc-bafa677c2743 | -17.8361 | -57.57396 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 56885656-cf42-3c57-87fe-11e640f08918 | -17.83551 | -57.57763 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 7c1d8de6-35e5-342f-b06e-3900855ecc2b | -17.83492 | -57.5813 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 044a9e3b-06d8-3a86-b0f7-e0195053c48f | -17.83433 | -57.58497 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6ef23d8c-a17c-3782-97ca-649cf56811e4 | -17.83158 | -57.58072 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cac6ea14-5868-3b3b-bd68-c91f6b305536 | -17.82882 | -57.57646 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| a068a63a-5aea-3383-bc2f-a0dd8f1f27d8 | -17.82548 | -57.57587 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f0b81205-2341-3d21-8d30-41b2e0ee8bdd | -17.82489 | -57.57954 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 65409637-8219-3a34-bfce-1fdd4d51e3a7 | -17.82192 | -57.59789 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d922e500-1796-3744-b9bf-7782ec4eaafe | -17.81858 | -57.59731 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| af9ee700-f693-3762-9bf7-ce6186ab7035 | -17.80504 | -57.5534 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1a081be3-0eae-3025-b12d-5054254a8a6a | -17.8017 | -57.55281 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6f24b8f4-dc75-3ac3-a85f-f11dcd56a9bb | -17.79954 | -57.54488 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aeed35be-3310-3ba2-a89a-d51f109f9848 | -17.7962 | -57.5443 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a50f52fe-10c2-3181-b05b-ef959c05512e | -17.79285 | -57.54371 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 876a0995-d9ab-34d6-a49a-c7b503ca0548 | -17.78892 | -57.54679 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fc3dea32-e381-3f9a-a55a-580434ab55c2 | -17.78751 | -57.57673 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 3dee3f09-2fff-367e-9586-45cdeff399f1 | -17.78691 | -57.58039 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 67eb1cdc-49da-3a22-a61c-e49b64ba7547 | -17.78416 | -57.57613 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| adc3d7d6-ff26-387f-89cf-516baaddd1ba | -17.78357 | -57.57981 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4d7eca57-25c8-3cd1-83c2-b9628f03e9b0 | -17.78238 | -57.58714 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 203273ae-2a33-3007-8514-4279e2fb02da | -17.78023 | -57.57921 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5e245960-dc7b-36a7-94a7-73a3eb82bb5a | -17.77963 | -57.58289 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 123c4292-5f2a-34a7-a2c0-3750f2f38e6c | -17.77903 | -57.58656 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0d545587-3e88-3946-b66b-e003e431f3aa | -17.77688 | -57.57862 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc476766-f6b2-3477-857a-3b0ca249538d | -17.77629 | -57.58229 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e9333dd8-31fa-3f08-9904-c904b17cd894 | -17.77569 | -57.58597 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 938c8998-f604-30a0-8c4b-f7a8105b488f | -17.77294 | -57.5817 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 95d6a210-faa1-3db4-8a9e-173a83023ad3 | -17.77234 | -57.58537 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9366c74e-a3b1-31b1-a47b-f74edf35213e | -17.769 | -57.58479 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6f4c0f33-b4a0-324a-887d-5b9bf219b2f6 | -17.76566 | -57.5842 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 132f1da1-f4a4-3b6a-b842-bfcb517218b9 | -17.76231 | -57.5836 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fef15366-37fc-379d-bb80-0316ee1727ed | -17.76158 | -57.54575 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2820f133-ed42-382f-9ff9-406914d8555b | -17.76098 | -57.54941 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 92c26a99-352f-393d-8e68-1afa85bed2b0 | -17.75979 | -57.55674 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f02a29f3-cd21-3e5c-8a13-17ce71e8a886 | -17.75764 | -57.54882 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 53ac05a5-99eb-38ce-b965-5309e39ae7a2 | -17.75704 | -57.55249 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 211c7923-58f3-3f20-b577-463b8c8efd9c | -17.75569 | -57.54892 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4d2834af-52dc-3588-a5f6-7701b3f1fe07 | -17.7551 | -57.55259 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8680d74f-8292-3a02-90b7-134771b97b90 | -17.75451 | -57.55626 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 40898de9-a033-312f-a364-293ee5d0fd0d | -17.75392 | -57.55994 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6459529b-0a02-39cd-80f4-92658baa8db7 | -17.75175 | -57.552 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b7d63f45-b733-3bc4-b6d1-c4fbc1024462 | -17.75168 | -57.58551 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 937fac15-bac8-39d5-bb17-0dbaf1322f9a | -17.75117 | -57.55568 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f9438390-6cd1-3bce-a06f-06a89cb6fb50 | -17.75108 | -57.58918 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a6f7b6d3-bbff-31ee-8458-5902cfcfd275 | -17.75057 | -57.55934 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ba0e98b5-dcb5-38ff-8fa9-5323d63c5cab | -17.74978 | -57.58564 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| fc4128e3-bc01-314f-9732-cd5b99face3b | -17.74919 | -57.58931 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 533e6637-021e-3500-946b-940d6be79089 | -17.74703 | -57.58138 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 372d43e6-d957-3772-837b-3c1f178419a1 | -17.74644 | -57.58505 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 5bac677c-cae0-3054-8dd3-be0bcc47eefd | -17.74584 | -57.58873 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b240f947-37dc-3bda-b4c0-fe855e7c0b60 | -17.74546 | -57.56977 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 277650ef-1937-3549-ab96-70e2ce5600c5 | -17.74487 | -57.57345 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 21bfe3ed-5cf1-37e2-8c3f-47a446cf199e | -17.74427 | -57.57712 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 08f04286-9a08-349a-a15a-a3687659743b | -17.74368 | -57.58079 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2edc5207-50dd-35c3-916d-775c99c1ea5d | -17.74152 | -57.57285 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4b0feac9-0fca-35eb-a359-e2989085f8b6 | -17.00573 | -57.52863 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ae295977-94bd-37dd-bd6a-18458c3d57d7 | -17.00417 | -57.51704 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README88.md)
