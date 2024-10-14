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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a7a396-57f4-3078-a74f-8a4dd3bef03e | -17.86596 | -57.39217 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 869b37c2-d473-33b7-9921-d6bcc8739ffa | -17.8647 | -57.37757 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 62b5c747-58dd-3f9a-b32a-fc690b826d15 | -17.86389 | -57.38219 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ccf9a2ef-47c5-3191-95f4-950c96453c66 | -17.86307 | -57.38682 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1be57c56-9f80-3ed7-9d1d-86b9808c03e8 | -17.86225 | -57.39144 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 7e376feb-ed8a-3ebd-9ccc-53c44399d757 | -17.86099 | -57.37685 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d1d9735c-b7c0-39b8-bdd8-88b74f3e8798 | -17.86017 | -57.38147 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| de721aa5-530f-3f39-b44b-e4c21c0c980c | -17.85935 | -57.3861 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6b20c7c7-5060-3701-9ab7-5490c3c5adc7 | -17.85853 | -57.39072 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 2b07a7b7-2949-3637-84af-d6d226574ad6 | -17.85727 | -57.37613 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1851f623-03c7-3611-b5a1-27116d5d6c46 | -17.85563 | -57.38537 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c840ed9b-d6f2-3ac3-ad3a-f9d64cdf50c1 | -17.85481 | -57.39 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 759732cc-07ad-3676-89dc-8be3b5f0d082 | -17.85399 | -57.39463 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f421999e-dc77-3da2-a4d1-30c13ec20a37 | -17.8511 | -57.38928 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 14f13b6e-4f4e-3b14-a4ca-823a4571fb75 | -17.84656 | -57.39318 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 16895bd7-2343-3451-933c-39e0aacae0e1 | -17.84573 | -57.39782 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d53077b4-7119-3c5b-9794-d7522e288b7b | -17.84201 | -57.39709 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 20a01cb8-9238-3074-97e6-92eb584f8045 | -17.83333 | -57.38104 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 948da492-6a69-36b9-bf9a-ee8474d04e60 | -17.82962 | -57.38031 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5f6fb4e5-9ee5-3551-b44d-1714e55f57aa | -17.84119 | -57.40172 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4386a3e1-e84b-304f-82e9-c0e816d85743 | -17.8259 | -57.37959 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 34201c57-3ee6-38fc-a838-d28e47c3b7fd | -17.20406 | -57.45303 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1682d803-d08d-3ea4-9c89-a85bc32aa03b | -17.2007 | -57.472 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 4405eab9-307a-36a1-b6e9-e6a664a9ab21 | -17.2003 | -57.4523 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 712aa77d-0d84-3dbd-877c-4cb214699e09 | -17.19737 | -57.44684 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 2a56feec-41d2-3d81-b453-968365ed01ad | -17.19609 | -57.47602 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e453039a-a6d8-3d03-b794-c29e4a04409c | -17.19529 | -57.43665 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9b22984f-6480-3651-8ef7-dd27dc0697f0 | -17.19485 | -57.46105 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 079a5f15-2c2e-3262-853b-d17fd354b25b | -17.19361 | -57.44611 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| c3152103-f17a-3989-b12f-b5b9208a676f | -17.19321 | -57.42647 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2153240d-a35e-3a90-b103-dcea069c7c68 | -17.19316 | -57.47054 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fb015c34-ed92-320c-960e-c828b04d3b9b | -17.19277 | -57.45084 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 8e36f533-883e-3e30-a19a-3398a534d4e1 | -17.19237 | -57.43119 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d83db549-7447-36c0-9dda-6feef66a481f | -17.19232 | -57.47529 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1f9e7f93-62f4-3fc9-af5e-07499aef87c8 | -17.19147 | -57.48005 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e70ba7f3-ad10-3561-9f29-94a6ac35d0d6 | -17.18984 | -57.44539 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| a70a3210-a4e7-394a-a86e-030f6e8dd793 | -17.18945 | -57.42574 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b6d61164-d729-359f-ac04-210099895746 | -17.18855 | -57.47456 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b92d6784-7305-3e95-98c3-15217178d934 | -17.18692 | -57.43992 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 595bd60e-17a8-3374-babf-2ea4ce414a98 | -17.18439 | -57.45412 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 73cc3074-a0c4-39a7-bf2c-1a3e94f46f37 | -17.18401 | -57.43447 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 02e40006-9226-356a-a3ee-1d8997c60e7b | -17.18394 | -57.47858 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 85bb0c7e-ea1a-38eb-9afc-372ab0988458 | -17.8592 | -57.3004 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 4d2d6f34-14de-3cab-876b-d990f0ab7478 | -17.18361 | -57.41485 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3399a66b-edab-3f1a-af36-ef29c3f67a12 | -17.18316 | -57.4392 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 33ee7049-1b9a-3392-83b2-9290e7b5d960 | -17.18193 | -57.42429 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bd3946c7-8705-3cff-a5f6-62399b90b0da | -17.18024 | -57.43374 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ca89d33f-04c4-3cfd-8f5e-aa6ccea17735 | -17.17978 | -57.45813 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 901decab-701d-3d88-a546-deeea1fa555a | -17.17262 | -57.47638 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f1ec7d75-a53a-39e0-9f55-ec89d6f2822e | -17.17177 | -57.48114 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b6e4a384-a2c8-36a9-b1e0-911a7eec2742 | -17.168 | -57.48041 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7afac7ea-b36d-39e9-8ac4-f9a387d9aace | -17.08234 | -57.46074 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e8dbd7e-22a8-3b54-b0ca-ee3803e91c49 | -17.07065 | -57.43882 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4558b46a-c10e-3b0e-b648-e97c57b154ea | -17.0698 | -57.44357 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fa2e543a-fdd5-30fd-aa0d-28b12f42ecb3 | -17.06895 | -57.44832 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 999ec49d-4ee5-342a-ae08-a305fb55e70a | -17.06518 | -57.44759 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4fb628f5-1e3d-3696-817d-d9b208f8fe7b | -17.02874 | -57.43865 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4ab77d99-3f83-3442-b607-c48bc02f7463 | -17.0279 | -57.44341 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.2 |
| ce61587a-3018-3f0a-9488-c15f2e62cb37 | -17.02662 | -57.42843 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e7f82271-b410-328e-a1c0-5ad45b772a9b | -17.02413 | -57.44268 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8936a70a-83d8-3621-abb9-e2e115a48307 | -17.02286 | -57.4277 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6c7c255a-743a-3331-8ada-52e0cf8163bc | -17.01781 | -57.41201 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4abc1d18-96f4-30d3-9c6c-41f53aed266a | -17.01698 | -57.41675 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 585ed629-1850-370c-91f5-2fec2c93af6f | -17.01615 | -57.4215 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3aecbf27-c12f-34dd-9a16-3205fa6ea34c | -17.01532 | -57.42624 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5185e76-91ff-3e92-8ca9-18cfedddd161 | -17.01321 | -57.41603 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8c980bc9-9329-3cb7-a6e3-5ed92b26753e | -17.01155 | -57.42551 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 03053589-0507-3165-b2f2-ad1289b217e2 | -17.01028 | -57.41056 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 53da992a-f4d5-3a8e-83fd-9699a2508a1e | -17.00945 | -57.4153 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ef2d3667-2f5f-3933-8986-2fc591edd1cf | -17.00861 | -57.42003 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f7678ba4-e093-3a1c-94a2-61463a756742 | -17.00778 | -57.42478 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f32aeab4-44e8-3744-818c-ed6755e2bd09 | -17.00694 | -57.42953 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7473ef3f-9ada-3fc1-9a7d-88cb3c1600a0 | -17.00611 | -57.43428 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a5628f48-4796-37e9-8eaa-794506a553ea | -17.00568 | -57.41457 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 97248e08-6046-3571-bc3d-b6108de0b79e | -17.00484 | -57.41931 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 96b4f89a-766c-370f-9a50-bb02814cc0c6 | -17.00317 | -57.4288 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4cd81d53-082b-30ae-a8a4-f839b06ed975 | -17.00191 | -57.45807 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e3864ef1-176c-3ea2-b660-f2aa64efda37 | -17.00108 | -57.41859 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fe5368c8-cf4b-30b8-b07c-02af100c2eb0 | -17.00107 | -57.46284 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a927cb78-4853-3dbc-aca4-6a4084d1cee2 | -16.99939 | -57.47238 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cf7ea61e-8435-344e-adea-76e171df3cde | -16.99855 | -57.47717 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 20f6658a-3746-39a1-936d-8f36899342a6 | -16.9973 | -57.46211 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2c1045f4-68e0-3c5c-be50-e09cc7a1bd90 | -16.99688 | -57.44232 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 524f750c-d686-36bb-84f8-03da245847ea | -16.99645 | -57.46688 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ca645aa9-0010-3685-8aaf-865484e0e0a2 | -16.99438 | -57.41238 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 95b588ae-4ea3-3b60-9629-babe4e2580e2 | -16.99099 | -57.4757 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 243e269a-d954-398b-996d-eadc5528fb66 | -16.99061 | -57.41166 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7c56070c-ab1e-30cf-a8b7-37a6e087d55a | -16.98552 | -57.48452 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19840671-1f89-3601-be03-4a512efbaa57 | -16.9539 | -57.50814 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 968ce995-1662-3843-ab4e-444cfde8f487 | -16.93999 | -57.69631 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ddad6759-3791-37af-a2f8-8372e4afdaa1 | -16.65738 | -57.45444 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4413dec6-b05f-329c-bc66-5698b80ac9ad | -17.86741 | -57.29726 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 37e4d1ab-3f07-3e6f-b676-3f7e4aa8c91f | -17.86659 | -57.30185 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 1e62c4f9-741d-3dda-91ed-47e724c83b51 | -17.86578 | -57.30642 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d0e0eb1a-f510-3a8a-8095-8dc21887402d | -17.86533 | -57.28739 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.8 |
| d34ed4ca-dccc-3655-829f-5cd1b41a7a87 | -17.86452 | -57.29197 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.8 |
| 884b40f7-ba78-3e77-894a-5b39c86150f6 | -17.86371 | -57.29654 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 2ce3aef7-beee-3bfe-8909-41d644ec8656 | -17.8629 | -57.30112 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.2 |
| a0919017-9118-3d77-8adc-5b389a046c24 | -17.86208 | -57.3057 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 911cb76b-a464-339b-8172-39d26744328a | -17.86163 | -57.28668 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.8 |


[Clique aqui para ver as próximas entradas](README97.md)
