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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b03525-0505-3c38-add7-1646396fb121 | -17.04531 | -57.41078 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0c6ea1e7-b2c5-3b33-8759-ecb4c8886df3 | -17.04405 | -57.41133 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d1291858-87c8-3f57-be62-5a5134ab8475 | -17.04385 | -57.41704 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 53c0bd5d-0593-38ae-973c-8b7ee104ef8f | -17.04263 | -57.41758 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 8a5a2494-c958-3552-b7c1-3c57c6854d17 | -17.03804 | -57.44207 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fe493fb5-7d26-3425-b0f0-217930c71234 | -17.03697 | -57.44267 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 15180eb4-8971-3b8f-9b0a-612967cf2fa7 | -17.03658 | -57.44833 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b1b19923-2d1d-3aaf-9179-da3a482489bb | -17.02841 | -57.45291 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 0098532b-e9b2-36d7-b7a8-9d8dec8fee19 | -17.02743 | -57.45351 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 5d700e8f-7b14-310e-bddd-4a63c1bbad0c | -17.02695 | -57.45919 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| afe0559a-018a-3fae-9784-b1cb39c2b694 | -17.026 | -57.4598 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 485da4ef-b894-3b4a-9532-66e204140bc8 | -17.02255 | -57.47807 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 692ce2a5-6c0f-3d22-a777-50a54726a359 | -17.02171 | -57.47874 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e8d34115-35eb-351f-a5b1-8309e24ca7c2 | -17.02171 | -57.45121 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 3800300f-3d73-35d6-adf8-0fbe8adfbbb3 | -17.02108 | -57.48436 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| a6aebc71-de77-3f4a-b2ab-96c6dd122d73 | -17.02072 | -57.45178 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| cd314dd6-dbad-3375-97e3-a62300afa98d | -17.02028 | -57.48504 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ccd825e8-6bb7-3d29-83a8-2597e9a1bf89 | -17.02024 | -57.4575 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 266bfc42-f2f3-3c90-b2bc-fede7b6b1f50 | -17.01877 | -57.46378 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 419b8bda-026d-32aa-aebe-4ee8cf3537c4 | -17.01786 | -57.46438 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| c79a2bb0-2de9-3ee8-a6b6-22dfb61d2adf | -17.01731 | -57.47005 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| ccf35ff8-ad7b-3358-b3d8-f950af1dfd57 | -17.01644 | -57.47067 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 44fd4840-dfd0-34ce-9117-8cb72527ac22 | -17.01583 | -57.47634 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| adb18be6-749d-39a1-801b-846cb48e7e0f | -17.01501 | -57.44949 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 2fc2d5a8-6fff-34f3-9741-895142917c10 | -17.015 | -57.47699 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 7bc6746a-baa2-388b-86f5-f5e87578a799 | -17.01436 | -57.48265 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 3a6f7ae5-d950-3a7f-9408-eb0c07bb736a | -17.01402 | -57.45003 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 03b4bf25-9ae6-331b-b85b-be49a5b8b6f4 | -17.01357 | -57.48331 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 5fb9287c-35c9-3c3a-9472-361a99d175bd | -17.01353 | -57.45579 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 63eb20a7-e873-3cad-ba56-2910d523139e | -17.01289 | -57.48896 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 7f9d2192-c387-3284-b7e9-7f39a8410862 | -17.01259 | -57.45635 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| fbb318a5-77c0-3e53-9dce-2b954c6e6ad6 | -17.01213 | -57.48964 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 961fb554-4161-364c-b7ad-3d0c2cc7aaa2 | -17.01206 | -57.46206 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| b9fe2291-2b2e-397a-ac28-e0390097b4c4 | -17.01141 | -57.49528 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| a1d53162-dd4f-3217-bb15-6f82e2aae568 | -17.01116 | -57.46264 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 308b406e-4f6e-3c5a-a3f4-d98827bcc341 | -17.01069 | -57.49596 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 803ee887-72c6-3754-a727-ef7b96bcffb1 | -17.01059 | -57.46835 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| fd5d0de6-b616-348c-a1c5-31c321e8933b | -17.00972 | -57.46894 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| dc522c98-9582-3c32-855f-2c8c4614cf3b | -17.00912 | -57.47465 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| a3024005-d926-35e5-9425-f88b601a357e | -17.00829 | -57.47526 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| e07fada8-93c8-38f4-8d3e-2d7e64242a58 | -17.00764 | -57.48095 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 3a7e5fa0-e8fc-3c5b-921c-664f433aac6f | -17.00685 | -57.48158 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 5b9d1676-6f76-3616-ba01-b2c6760718d7 | -17.00617 | -57.48726 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| ebb31668-71ae-37af-a513-d7acaeb2ca56 | -17.00541 | -57.48791 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 5b85284c-a3ba-3f7a-88e7-03e21d78da9f | -17.00469 | -57.49358 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| fac83602-8e54-3f7b-8bfb-bf33d2700ca5 | -17.00397 | -57.49424 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 83498faa-617d-3873-b5d8-1fa7a629f6e1 | -17.00388 | -57.46666 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| d14bcc9f-a71f-3911-bcd2-8663549e52b1 | -17.00301 | -57.46722 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 79b575a4-607a-3ef8-b8e0-698000e69a6b | -17.0024 | -57.47295 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| d8508c2d-4df7-3151-ba07-41c6c99c1c1c | -17.00157 | -57.47354 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d7e07e1e-2755-3b10-97a7-191043206681 | -17.00092 | -57.47927 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 2b7906a4-3b1e-3623-adea-47a8fc7c6575 | -17.00013 | -57.47987 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3706aad4-5f9d-3a11-b3aa-bbee5e1f43c2 | -16.9987 | -57.48617 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 60da7131-294b-3130-944e-94a75623ff59 | -16.99797 | -57.49186 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 15bb748c-c32a-3414-8d1e-78a3ab495244 | -16.99726 | -57.49249 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 54286679-67f2-3ec0-b557-4a39ee320972 | -16.99198 | -57.48444 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 0022b8fa-1951-3f16-bfdd-9a8b4d9cc193 | -16.99054 | -57.49075 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 042bb7d5-a12c-33d7-adf9-ead9e6735105 | -16.98243 | -57.4021 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c7782de0-2a29-376b-8641-b0f2e3d2cb7a | -16.97573 | -57.40041 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 58b5da9a-3dc4-3808-8060-45c2473e76ed | -17.00994 | -57.5016 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| bb390b67-dc88-3088-8685-91b3083ff13f | -17.00925 | -57.50231 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| 53cf461c-b0be-3514-a9f4-553735560382 | -17.00321 | -57.49989 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 8f671d34-45d9-328b-ae74-89ed06208e94 | -17.00253 | -57.50057 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| d9132eeb-ed80-34af-9c3e-866297aec624 | -17.00173 | -57.50621 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| a253a35a-f32c-30f1-9904-11ab05a079ee | -17.00109 | -57.50692 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| f3e14246-0e69-3583-84be-faafd66e9def | -16.99648 | -57.49818 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 7da5b8a1-31f1-3d70-91a2-261174c347bf | -16.99581 | -57.49883 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| f5dbd2b9-a150-3625-b220-bc912a4ca6c0 | -16.995 | -57.50451 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| e0c7436a-eccf-3b0f-b9e8-4a280b3e0640 | -16.99436 | -57.50518 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 0f29c1cf-95d8-3e73-b3a3-2c0bbac1621e | -16.98909 | -57.4971 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 95eae0e0-3e0f-3606-a434-17eb11c437f1 | -16.98763 | -57.50348 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| e70a789a-adf2-311f-82af-abcef994af08 | -16.98128 | -57.56255 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b98b9d2b-c91b-322f-8414-a60dfe3524c9 | -16.97599 | -57.55442 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 49b5479e-cb00-39c8-bb10-17b36ab8332e | -16.97452 | -57.56083 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4a0ac4be-fa10-3191-9ad7-fc1bf27aba7a | -16.96778 | -57.55909 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e3cf6883-714e-3609-a6d7-6371bc7b9a31 | -16.95634 | -57.51562 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1f5d6092-8f70-3c51-b9c6-96fc1e9c0be5 | -16.95487 | -57.52199 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6cd70e40-a131-3341-b848-d4f41a166d3d | -16.9496 | -57.5139 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ba127f74-2958-3451-b32a-774015440f53 | -16.94813 | -57.52027 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 972f58d9-5f9b-38c1-b687-f968f0ef67d8 | -16.94433 | -57.50583 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a566144-eaa0-338f-a6e6-e9c07508a754 | -16.94286 | -57.51219 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3ceee8fe-7c57-358d-92b1-7ac5943261fe | -16.94284 | -57.50807 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ec8f247b-ad0a-327b-aaac-ba949e14fdeb | -16.94141 | -57.51445 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 392146e5-eaa5-3ca8-bb87-cceb70330710 | -16.94139 | -57.51855 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0065c10f-29e5-3d32-aee9-fd2339a7d97c | -16.93759 | -57.50413 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4f01e4f6-2401-39c8-b8ff-ffd111668bea | -16.93612 | -57.51047 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 96c52d26-eb34-36e1-9c30-134657d8d4e9 | -16.93611 | -57.50633 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 122c4e3e-2422-3bb2-ba0c-be23e5e84ac5 | -16.93468 | -57.5127 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4b029f4d-947c-3b63-a1bd-ad739ea5a558 | -16.92938 | -57.50878 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e3f9f181-6498-33c4-95dd-b7f0bf5a1dcf | -16.92756 | -57.85257 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 04567332-9659-31fc-bf08-69200b039151 | -16.92059 | -57.85926 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| c855e638-a494-320d-ba67-74d13e511ee5 | -16.91912 | -57.85749 | 2024-10-16 04:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e257afeb-d614-3921-aa60-4e78fee14986 | -19.59456 | -56.98377 | 2024-10-16 04:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| db7a4e9c-5fbd-3a15-9525-ba12a9e67100 | -20.45551 | -46.55635 | 2024-10-16 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd1fdfa2-c2f4-3bfb-a4e7-a79ac72c50b0 | -20.45484 | -46.5603 | 2024-10-16 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28b5e98c-c215-398e-9562-81f149653027 | -22.32182 | -46.93592 | 2024-10-16 04:10:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f99c9867-03ca-394b-ab84-4e39f0dfe050 | -22.31841 | -46.93526 | 2024-10-16 04:10:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30aa9f6b-4629-3211-9d8a-bb6bc58df920 | -20.45079 | -46.56343 | 2024-10-16 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de54d433-44d2-3c2c-b596-50c4dd75b7fb | -20.4474 | -46.56264 | 2024-10-16 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b168f16c-c3b7-3696-ab2a-2c0f48804a12 | -20.444 | -46.56192 | 2024-10-16 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README39.md)
