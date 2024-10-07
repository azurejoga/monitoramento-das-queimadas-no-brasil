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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97e83178-be30-3f4b-9dc4-1ddcd2203124 | -16.52013 | -57.73813 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7fa4d5be-4407-3573-8728-03da8105b679 | -16.51994 | -57.72165 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 93657b30-fbb9-34c1-9a0f-fb556c375baf | -16.51952 | -57.74252 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b24e2c46-d1f2-3d33-9d8d-f4fe1fe6e929 | -16.51931 | -57.72603 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 57d0898e-622e-38c2-9b5d-cb67592b156b | -16.51889 | -57.72002 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ff72f0ac-2060-38d7-9172-e35e99c93c4e | -16.51828 | -57.7244 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 78e4bfac-f1b4-36c3-8314-10a8b86e721d | -16.51805 | -57.73482 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 33293a5d-40d8-3c0e-ab0b-b84bf5152661 | -16.51768 | -57.72877 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 447dce03-554b-3043-bd2a-3484a43e151a | -16.51742 | -57.73922 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5466f11b-38c8-3075-96f4-2e3106cd07a8 | -16.51707 | -57.73317 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d43b99b4-4b6f-303f-9b5d-3b7e4b836a74 | -16.51678 | -57.74363 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7f124602-4881-3126-8828-7d1a10e558e5 | -16.51646 | -57.73758 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0fd49bb2-b83a-3eff-8216-c6637d38431c | -16.51626 | -57.72116 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f84cfc10-03dd-320d-a6fe-7f444fab0723 | -16.51586 | -57.74201 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6a08e250-6d59-3161-ae78-ab30158b91ba | -16.51525 | -57.74642 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 21b4fcb1-d56a-37f8-9546-9302c548a84f | -16.51521 | -57.71952 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1ce5626c-f4a1-317a-85bd-a4de19d99e73 | -16.51375 | -57.73869 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fcb807b4-d8a0-336e-90e4-c9069532e9e5 | -16.51311 | -57.74311 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3879b189-1ba2-3700-a23f-c36ff2865d58 | -16.5128 | -57.73705 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1a77ed7b-1b8c-3902-87df-75332fba9634 | -16.51259 | -57.72066 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8dcc09f4-e4f1-3601-8967-70727602ee9c | -16.51219 | -57.74148 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 773ec8bd-75a3-3184-bf8b-93a96f79cdc6 | -16.51158 | -57.74591 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b68d33b2-3a2f-3929-a3a2-0deeb28e09fa | -16.51154 | -57.71901 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1fc5b315-44f0-3046-a838-8b20520e9871 | -16.50945 | -57.7426 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bfad77ea-cbd0-3163-af91-37f73ed52da7 | -16.50892 | -57.72012 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 61384a80-7e3e-3476-8f98-8919259c1925 | -16.50852 | -57.74095 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c6c4a34a-942f-3ffc-ad83-b6648964a4c7 | -16.50641 | -57.73763 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 16e865e2-3bb6-35fe-a4d0-e063e0251e32 | -16.50578 | -57.74208 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fc899d8e-3377-371d-ae2c-1b1006016f27 | -16.50463 | -57.7239 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 06952b7f-3bfb-3749-adae-d9ad9d468619 | -16.50339 | -57.73265 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9778c66d-d337-318d-8947-219f40c7881a | -16.50275 | -57.73708 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2310207c-69a7-3b24-ae87-c337b82b70ea | -16.50212 | -57.74152 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a44ef100-e3b4-3485-a10a-2517387bbb9a | -16.50097 | -57.72332 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5e71245d-6784-3ffd-9909-14a7f3185905 | -16.50035 | -57.72766 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4007da7c-c2b6-3c8d-98f2-4ae4cd90e1bf | -16.49972 | -57.73207 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| abffa7d0-d68d-3a97-b051-883d9cd3624c | -16.49909 | -57.73651 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2d4764d8-505a-3df6-931d-d7a3cacffdee | -16.49846 | -57.74094 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e63df3a4-e9bb-3fd0-b4ac-38fe5d997a3a | -16.49731 | -57.7227 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9a27fdd0-ec70-3dff-8170-ebfcf642c6d4 | -16.49669 | -57.72709 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ed9ec3a5-95b0-3db0-9872-ca55389c2a12 | -16.49606 | -57.73151 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f64f6e5b-4653-33a6-a220-bd31dff864ba | -16.49543 | -57.73594 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 80d564da-152b-35ed-967f-a3ffc4bddc39 | -16.4948 | -57.74036 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ac8d570a-37e1-3139-991b-b473ba272421 | -16.49302 | -57.72655 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 25b8aee2-28d7-3c35-beae-efcb4342f1a5 | -16.50207 | -57.25456 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e9bb66d2-c552-31ee-b825-de633f2833b1 | -16.502 | -57.28305 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5bc9b8b8-589e-38ac-bdc4-998e6b242c10 | -16.49952 | -57.27318 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b308bce3-5c5c-3376-aef8-40a63357db67 | -16.49888 | -57.27785 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 664271ed-d0a8-35f2-b6ce-294442350cff | -16.49825 | -57.2825 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9de3e698-4c4d-3b3c-a0eb-41e162600dff | -16.49576 | -57.27263 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f9ed68e7-98ad-364b-bba4-2a1d74e18312 | -16.49512 | -57.27731 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 23381e35-f641-35bf-b4c1-0e955899326b | -16.49449 | -57.28197 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 87aa7baa-361d-3ac8-a634-4b74a538cf98 | -16.49385 | -57.2866 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 14dff698-4581-34b5-aaee-6d5749bb306f | -16.49264 | -57.26743 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c99ca2ae-26ce-3f5a-8e20-21a6a5bdea74 | -16.492 | -57.27211 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ccb1b18b-76af-3d72-92a2-b3f43f37c185 | -16.49137 | -57.27678 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2794d0b9-ee7b-3728-9cc5-5f1eae00753a | -16.49073 | -57.28143 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9b9a44a6-c9ca-3545-b4fa-bfbec110eacd | -16.4901 | -57.28606 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6c3013ca-f797-3919-a237-b773ffa94ba1 | -16.48888 | -57.2669 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d0735785-b230-34aa-ba5a-e58ab079af3f | -16.4883 | -57.24298 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| be8401e3-02e5-3d9e-880e-dc367a0a7790 | -16.48824 | -57.27157 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3eb65f99-e9b8-39ec-ad16-e3ec95072f91 | -16.48767 | -57.24764 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1958ac5b-5add-31a5-8651-407d3f50d338 | -16.48761 | -57.27624 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5e4504d1-c95c-31dd-93d7-613d49c6a6ce | -16.48697 | -57.28088 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 66f00226-f2d9-3d2c-a4c6-d736e5ab7536 | -16.48634 | -57.28551 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1b82bee7-4ba3-3261-8001-108fc3101cc1 | -16.48571 | -57.29015 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fc33ec4-e87a-3f8a-be6a-3cd108d1a9af | -16.48512 | -57.26635 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3ebb628-9428-3c0b-9097-1292737832b0 | -16.48449 | -57.27103 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b018c49b-39d7-3443-a7de-e21f5c20830a | -16.48385 | -57.27568 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 653c8535-0ee0-3aa7-bcd9-a4fe3b3c25ad | -16.48322 | -57.28032 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1fd1bc38-91c3-309f-be2a-eb1c627f4e85 | -16.48259 | -57.28496 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 206d3400-fa86-3860-8cb2-d4efa558a933 | -16.48196 | -57.28959 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e094d630-1ee0-3ef5-9452-9f614b3d9511 | -16.48073 | -57.27047 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 896222aa-e08f-33af-a2e0-c79fec2c2143 | -16.4801 | -57.27512 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 795a47c1-f32f-3d93-b7fd-f499839bb09e | -16.47947 | -57.27977 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cbefabff-8871-3fe7-8d45-e940f87385e7 | -16.47884 | -57.2844 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 99414bb8-720c-3540-93a8-cce6a8b9bffc | -16.47821 | -57.28903 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8d5eb756-9b90-3147-be04-11a2b7ce0403 | -16.47634 | -57.27458 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 72df8bbf-6368-3871-9ae7-8c679a644907 | -16.47571 | -57.2792 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f63482f0-5c76-3634-bac6-1135029ed923 | -16.47544 | -57.27702 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a5cd9c04-3aea-31f2-8902-8f3c3e796f87 | -16.47509 | -57.28382 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d0c04b9b-fa41-38b8-81e0-b43dcde27d2a | -16.47478 | -57.28164 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0158e2c8-de53-3a41-9ef2-98162111312e | -16.47413 | -57.28624 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 56782182-3d61-3c81-925b-be84dc37a35a | -16.47321 | -57.2694 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6eab77d4-8dd6-3b69-8074-1c128ebaaaf3 | -16.47258 | -57.27403 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a9523cce-69ad-3840-a033-3282fd4d603f | -16.47233 | -57.27188 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| caf26aca-7cca-30c6-821d-d55d8bdca41b | -16.47196 | -57.27864 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ea9f851a-4e4e-3113-9fe7-7e827e6bfc8b | -16.47168 | -57.27648 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a96fad14-20a8-32e3-8251-593cf1c46b82 | -16.46883 | -57.27348 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f7efe87c-4535-3948-8af7-a6700ad830c4 | -16.45817 | -57.35216 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b966c1a0-3df9-3e1b-9543-4a411ffc1182 | -16.45746 | -57.34986 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8c91a65f-ad9c-3ffe-b1d9-abe2ab52d7cb | -16.45443 | -57.35162 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0a6f73d9-b863-380b-baea-9bb69014a9b7 | -16.44641 | -57.31997 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 188ade53-51fc-3f4e-b859-3c97b67a6911 | -16.44542 | -57.27251 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1a73b114-23cd-317a-b5a5-80638000b043 | -16.44332 | -57.31477 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1e259d2f-fc6c-31b3-b0f5-c2669f7fa191 | -16.44267 | -57.3194 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3c2dcab9-c4db-38be-8876-35b120b97b1d | -16.44231 | -57.26735 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 064cdad3-6047-3b56-9dcd-320b4bc11e3c | -16.44167 | -57.27195 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e8e6fcf5-726e-34ff-b0a2-1d1b2f5854b3 | -16.43856 | -57.26678 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ef624ab5-bd5c-3a61-8069-707e4ba1a9a1 | -16.43792 | -57.27139 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 891e77d2-8291-3d25-b5f1-4d36598f5df8 | -16.43727 | -57.27604 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |


[Clique aqui para ver as próximas entradas](README117.md)
