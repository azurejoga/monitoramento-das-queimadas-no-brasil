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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6e3158a-471b-3701-8cec-d9de0600bf28 | -2.95406 | -53.71336 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727fa489-f44a-37f4-bdeb-ac808aa918ca | -2.94451 | -53.71192 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67880513-6836-316e-83c2-2bb3668133c5 | -2.94129 | -53.70091 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8293e15f-864f-3c80-b541-c3b68c8ae956 | -2.93651 | -53.70019 | 2024-09-27 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4ac0c12-d666-3b68-b5b8-8bfbe14bf625 | -4.52165 | -54.84513 | 2024-09-27 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7d415fd-6c46-3a1f-80a8-480faa0c4377 | -4.51713 | -54.84449 | 2024-09-27 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f597fc4-7f18-38ec-b3eb-b47a7d6137b8 | -4.50964 | -54.95554 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1697655c-c0e0-3c09-a015-b94646d5f6b4 | -4.50585 | -54.95025 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a96256d8-ef57-3672-8e1d-28321743dea1 | -4.50517 | -54.95474 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c44d26e6-3106-33e0-b7ef-999149d9bd36 | -4.50204 | -54.94503 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 151c42ed-5419-341a-ba76-c171cf0f29a2 | -4.50137 | -54.94949 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c35c2bf-b825-36be-a21c-9d8ad3d129d7 | -4.50071 | -54.95392 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76ab6be5-5c41-3469-a8f8-ed96b4708d4a | -4.49756 | -54.94436 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00fa5e94-4d97-35c2-9f32-f43496e1241a | -4.49689 | -54.94879 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f126773-a538-3da1-8a3d-623de0b411b7 | -4.49242 | -54.94802 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5dd7e3-82fa-3ab9-aeb5-1877c3f39816 | -4.49025 | -54.99314 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30a738ae-bf8a-3e66-9fce-8b8abc734d09 | -4.48958 | -54.99762 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a29090c2-d235-3617-aaed-82232e972581 | -4.48729 | -54.95166 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec59393e-78e8-3989-943d-6960addae383 | -4.48662 | -54.95616 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ade8f6a-f5b1-3727-8384-10a6c65c3aca | -4.48511 | -54.99694 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34283fad-3058-331b-ac0a-fd5f2c68918b | -4.4828 | -54.95101 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dea746f-994e-38de-8912-84028031c2fe | -4.48214 | -54.95547 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf8c9a19-0689-3144-906f-a2e3ae91f8a5 | -4.47961 | -54.94162 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 890192fb-2d71-36b1-91d3-6f8561633125 | -4.47831 | -54.95038 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3406b80f-ce6b-3096-b06e-2aac76c43a47 | -4.47513 | -54.94094 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f21971f-5258-3601-adb7-6e221eff0b3f | -4.47382 | -54.94976 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d73b83d-c4f6-3c28-a280-6eb296a23555 | -4.40702 | -54.85868 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb5f53d1-0697-336c-95be-f4042cdce22a | -4.37473 | -55.43818 | 2024-09-27 05:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06dcc2be-db26-399d-9ed3-09ea6b7168c5 | -1.74807 | -55.2378 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06b02b8b-9ff7-3bb8-80fa-a3d3a2a88977 | -1.74386 | -55.2371 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaedb965-329e-364c-a785-d6c1b68aadec | -1.74326 | -55.241 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e210281-46ee-3d9f-9c02-659fc3a9d9da | -1.69825 | -55.0043 | 2024-09-27 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6574b258-2705-3219-8f9f-7aee32a328ea | -1.46989 | -55.49936 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fd71a17-5696-3737-b767-4428701124fd | -1.46462 | -55.50615 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c16dbf8-7a71-39e2-a307-99afa2cf0e4f | -1.46049 | -55.50551 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51f19d02-eb5b-3d46-8d78-bc0ef42df736 | -1.45694 | -55.50113 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1958fdb0-6c64-350c-bbb9-6c6cd00fb840 | -1.45637 | -55.50483 | 2024-09-27 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee12fd1a-3f3b-3ffc-ad25-d32ced4ba544 | -3.5874 | -55.53479 | 2024-09-27 05:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f33e5cf-0ead-3477-a705-b8461f49590e | -4.2813 | -56.40627 | 2024-09-27 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e069a0f0-0672-38de-8c6b-c6f5ac6974f7 | -3.61472 | -56.80723 | 2024-09-27 05:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc656eb-44fb-3f43-b560-f6dc1ba86a6f | -2.06571 | -56.83032 | 2024-09-27 05:25:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30277a25-6bdd-3f9f-843f-1dfb8ff66ab8 | -3.45233 | -57.98642 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d738d925-6a24-3568-8b7e-1bdf5d9c25fe | -3.37369 | -57.96303 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9070263-4116-3eb2-b82e-4872e7785b2f | -2.9262 | -57.85791 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 530b7850-4624-358f-bf38-845e26bf60b9 | -2.92555 | -57.86214 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39113123-ace7-3d8f-9262-42050ad9184f | -2.92385 | -57.84886 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1fccd86-0551-3089-8d74-e0c86aa68aa3 | -2.92085 | -57.84405 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7db59e-2e47-34e5-bff9-619999ee751e | -2.9202 | -57.84831 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549c73c5-aa89-3cbf-b749-b4068ed4c751 | -3.3514 | -57.93794 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d4a9744-5d20-3f4a-b535-e9ca3dad4382 | -3.30976 | -57.77073 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f06a769-b84c-35ed-bca3-06287d004d61 | -2.9275 | -57.84942 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9da8f3dc-911f-36a4-9b80-2a6134e3e960 | -2.9232 | -57.8531 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52c63ecd-f96e-3aa3-a6f0-206c903950d4 | -2.9172 | -57.84349 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d777876c-18e0-34b2-92df-d283e00042aa | -2.73159 | -57.51334 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d8cff1-97ca-3cde-b7c6-f0f0b5c20461 | -2.72921 | -57.50398 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9edab81d-a783-3f68-99b3-185360e13bb3 | -2.72294 | -57.50526 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b066a36-dd99-37ac-b7ce-b2515157ab5c | -2.68346 | -57.58871 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e7570274-1c5e-38e6-8e97-923040a7fdf2 | -2.67977 | -57.58815 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc6a2743-55a2-3e81-8b57-fd8d992ae3e8 | -2.67708 | -57.60552 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8483376e-046e-3334-95cd-89404d8f8018 | -2.67474 | -57.59628 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 74734ffb-44f0-35ee-9653-6671eb7e0351 | -2.67407 | -57.60062 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c23374e6-132d-3aea-8b6e-8d1db5cf3554 | -2.66768 | -57.51932 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 533ba9f2-dd70-355a-becf-e62071c3ab04 | -2.72855 | -57.50838 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d4c20be-70b4-326c-83b3-0198c52dff41 | -2.72665 | -57.50583 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8ea119e-0481-3735-891b-8399fb79b3d3 | -2.71484 | -57.50853 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9eabfd8e-40f4-31e0-8db0-c9af1714eb0a | -2.71114 | -57.50796 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 664c88a2-9053-3d42-8f1f-41e8350024d4 | -2.71046 | -57.51235 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 295d0cef-6f49-317d-8124-a0af0022877c | -2.70168 | -57.51999 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 880dea41-f53e-3ff8-b494-bb417ac2a4ee | -2.67775 | -57.60118 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae2f939b-c027-3375-ba76-8e834cc7fc5e | -2.67509 | -57.52045 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcdc4655-c5f3-3b41-8be7-c530c97ec78b | -2.6734 | -57.60496 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a2f934d-26f8-37f5-a3cd-b3f2b12e0e62 | -2.67138 | -57.51989 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc3164c-b7b6-357e-b2bd-e501a73c9808 | -2.66331 | -57.52314 | 2024-09-27 05:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ab92186-4530-3270-9dc3-6631794d9987 | -3.66866 | -58.11163 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 321407ac-72aa-3bc1-97ee-887bc44082ab | -3.66802 | -58.11583 | 2024-09-27 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60e13823-6e3c-3727-a4f0-8efcac92fa45 | -3.67397 | -58.57172 | 2024-09-27 05:25:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75e16279-cc88-33a6-a53e-a68c3148c809 | -3.67043 | -58.57117 | 2024-09-27 05:25:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 554a4f9a-2d94-31bd-8ace-48e14a995aeb | -3.63149 | -58.56667 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 4e59092b-c9c7-3c96-befd-7295247eefc8 | -3.62857 | -58.56214 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c9a3376-fca9-34fd-8258-ed9f123e5c70 | -3.62795 | -58.56613 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9909fcc2-c132-3bf1-9e01-edb2e06e4a61 | -3.55041 | -58.76454 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b009e18-716d-379a-9cfe-31a2813a3999 | -3.53221 | -58.67027 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaac1f03-d0eb-33a0-9eae-38d64a71efe1 | -3.5293 | -58.66579 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c45f94d-18ce-3b15-ba5e-3445686324b3 | -3.52898 | -58.66885 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c350f8a-8af4-32b8-9d10-98a7a4b14565 | -3.52868 | -58.66973 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b818297-33f0-3a00-93ca-8a03124a1671 | -3.52291 | -58.75632 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c165e0cf-2be0-3c65-beb1-bbf8691f8d3d | -3.51999 | -58.75186 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32354962-2c31-3608-903f-856bdfc4ea85 | -3.5194 | -58.75579 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9ff884-5042-3e52-8de9-114d1476f7f3 | -3.5188 | -58.75969 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc14c68-768e-3037-aa37-075db8bc613d | -3.4912 | -58.53809 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98b33068-3949-30a7-b181-60c6dbb7928c | -3.48765 | -58.53755 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 482d26e3-f141-382d-82db-f37e6366fc4f | -3.40075 | -58.91712 | 2024-09-27 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b884ed7c-baeb-3c89-825b-33aa5d16a705 | -3.2553 | -59.56476 | 2024-09-27 05:25:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7dcfa5c-15a6-3c2e-ba47-a2490a197760 | -3.12256 | -59.13633 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3aa6d885-3781-3388-b2c5-1d5276a78a5e | -3.12197 | -59.14008 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 745d31cf-0efb-31be-9e7f-53091682d31c | -3.05382 | -58.96346 | 2024-09-27 05:25:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 990358fd-cd28-3d4f-9162-b046e5f60de4 | -2.84595 | -58.33516 | 2024-09-27 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00e044ed-b7a2-355a-b70b-f1dba7c97dbd | -2.84533 | -58.33919 | 2024-09-27 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ef4e186-4812-375c-8c21-0687524b328f | -2.84239 | -58.33463 | 2024-09-27 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9285713-fce2-38f4-aad4-26dd3ad28d0e | -2.84177 | -58.33868 | 2024-09-27 05:25:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README112.md)
