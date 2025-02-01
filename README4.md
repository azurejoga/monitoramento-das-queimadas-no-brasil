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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5adec3d5-873f-3702-b11b-1163ffba79ee | -15.25313 | -60.2351 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a26df35f-01de-3fa7-8c43-e576a85eedc8 | -16.09009 | -60.06116 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 792ff976-647d-3efb-8da6-a8e42b4138c8 | -15.39853 | -60.17437 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4194ace8-806a-3cc2-b2ff-6e10e492114c | -12.40561 | -63.99133 | 2025-02-01 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd2cfcba-85ff-3876-b432-fc222769aee4 | -15.3944 | -60.1779 | 2025-02-01 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47ed6454-9fde-375c-b274-d5faacfd2046 | -21.25357 | -57.32525 | 2025-02-01 05:27:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55209810-2a47-3eec-afab-ea2fd9fd0107 | -21.41704 | -55.77834 | 2025-02-01 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae1858b4-99f7-3916-b7c6-95a2ceab224e | -22.15288 | -56.6762 | 2025-02-01 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdf60bb3-6744-3d01-af1e-7804ee07be7e | -21.29829 | -55.90508 | 2025-02-01 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d12708f-8db7-3202-bae3-bc94d0436c42 | 1.4134 | -59.9504 | 2025-02-01 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f24cee47-0d68-3bf6-9702-7a83bb4ad822 | 1.4134 | -59.9504 | 2025-02-01 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 637c22bc-4e4a-3510-8a90-0f3a9a0b2a62 | 1.41809 | -59.94373 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2899552d-0e8d-3734-aa9d-c6d7dda3af68 | 1.93929 | -60.39003 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d5aafde-d130-3095-ab14-8a355f847442 | 0.79163 | -60.09201 | 2025-02-01 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae787770-a4de-3062-8470-4da277ac272c | 1.42096 | -59.9617 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 21a5a6e2-797e-3cad-aec8-919676f71484 | 0.79572 | -60.09137 | 2025-02-01 05:44:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be9ea694-15b9-3b24-a389-003447de4735 | 1.41515 | -59.95155 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ef9d7ff-669a-3d5d-a9fb-1a48ebb68066 | 1.41279 | -59.96297 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab1a2d9e-58ee-33cd-bbca-6aa3af03b558 | 1.93847 | -60.3849 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b60559eb-8676-3f8c-a75b-d00b5d6e088b | 1.42626 | -59.94249 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 656be885-49fa-39fa-ab75-2f086c7bdfb3 | 2.43859 | -60.65211 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e951ff6d-24fe-3c32-8f1e-8123143ffe89 | 1.4163 | -59.95875 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f11b9a22-ea75-31d0-91c5-e2df695341a7 | 1.42389 | -59.95387 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40ce7ea1-864a-3319-9b63-49a4a2d1ead7 | 1.42332 | -59.95029 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98e78fe5-6fea-3ce5-92db-db1746ca2479 | 1.41981 | -59.95452 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db768110-928e-3641-9dd8-4c873b90465f | 1.94325 | -60.3896 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ac8fbb0-74b9-3f5b-886b-387bf0621a24 | 2.14481 | -60.8516 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c0c0a3-c5a1-359a-a232-51abf61592b1 | 1.41866 | -59.94732 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7693f5a8-76c2-31c2-90fa-334cf5e006d4 | 1.41573 | -59.95515 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef9554da-525c-3c5d-8276-b0a7865cfc94 | 1.41164 | -59.95578 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd615780-ca57-3f40-b2aa-d818153aaf18 | 1.41457 | -59.94794 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bed49e0-7aad-3488-beab-6458774026b9 | 1.41923 | -59.95091 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ac6f398-adca-31f5-aabd-c4a2b5291afe | 1.41222 | -59.95938 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7f31aca-b07a-3831-a4e6-521b534da056 | 1.414 | -59.94436 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e17a1fd1-499c-377f-8d16-130a0065a58b | 1.42217 | -59.94311 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c885eb44-91c6-30de-80b2-33d0a27762a1 | 1.94241 | -60.38432 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9865fc6-77d8-3d40-985c-7bdffbce1b1f | 2.14099 | -60.85213 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c71a61ae-8b14-398c-a5da-630c1003aebc | 3.45165 | -59.97828 | 2025-02-01 05:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11d363ea-6754-3da3-ad25-49eb38816e88 | 1.41688 | -59.96234 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08bb88af-9481-31d4-9276-3a3c5e7eef27 | 1.42038 | -59.95811 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| de4f7fd3-eea3-3d11-ab7b-745b321bc29a | 2.44244 | -60.6515 | 2025-02-01 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7dd830b0-6ebe-3659-abd0-0a97a06a3e3c | 1.42275 | -59.9467 | 2025-02-01 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dfaf429a-6dc6-3c25-b70d-4428005fe8c8 | -12.77355 | -61.45504 | 2025-02-01 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d2a3992-bc73-323d-996c-ac21164293e3 | 1.4134 | -59.9504 | 2025-02-01 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 50885016-5a93-3426-9534-49842bf1f883 | -15.39818 | -60.17873 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 945114ea-e296-3e20-9ed3-2e1652ac4d7d | -15.25134 | -60.23479 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be15823a-d8c5-3001-8037-1f4951e495fc | -15.39855 | -60.17552 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 000b472e-cc32-38dd-8eb8-22852a3fc41d | -15.2561 | -60.23847 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92c92ca2-ef54-3294-85d3-2ac742e3827c | -15.25647 | -60.23536 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ce1686-8c32-38be-b06e-8e9e17a24921 | -15.39301 | -60.17815 | 2025-02-01 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ddc222e8-d77b-3763-ae81-3d517f18a4a8 | 1.4134 | -59.9504 | 2025-02-01 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 947ea847-9515-3940-8408-19b70eb45888 | 1.4134 | -59.9504 | 2025-02-01 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a9dde6d4-27b8-3331-b37e-5e5d4d55deff | 1.4134 | -59.9504 | 2025-02-01 06:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 27853e03-35dc-3720-b5f2-73d7c30d0583 | 1.4134 | -59.9504 | 2025-02-01 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f0712568-62a4-33e5-9d71-9456daf42c5c | 1.4134 | -59.9504 | 2025-02-01 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 906ba7d9-76a5-3a67-9cc8-9d56597bbb8c | 1.4134 | -59.9504 | 2025-02-01 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 30f2965e-5b1c-38dc-9675-8a27a324e9bb | 2.44175 | -60.64687 | 2025-02-01 06:56:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d000a02a-dc32-3b74-9155-c88dbce00ff9 | 1.42784 | -59.94046 | 2025-02-01 06:56:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0b783c7f-034f-3255-baf7-80995c968186 | 1.41773 | -59.96398 | 2025-02-01 06:56:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 3264e50c-818e-353f-9093-0b2eb76f600a | 1.94209 | -60.38448 | 2025-02-01 06:56:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3b155e88-205b-302d-9611-31a5d413bc13 | 1.41445 | -59.94247 | 2025-02-01 06:56:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6495a039-f100-391a-a101-36f6056a8973 | 1.4134 | -59.9504 | 2025-02-01 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 385bcb2d-0c44-3f92-b2a0-7e220e1d0eb6 | 1.4134 | -59.9504 | 2025-02-01 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c2cee6fb-fb35-3fd3-abc2-4ddeef80f339 | 1.4134 | -59.9504 | 2025-02-01 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f274a2fc-110e-3255-a8ca-470c729827b8 | 1.4134 | -59.9504 | 2025-02-01 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e3e0d612-e0d7-3435-882b-47fcc54a00d6 | 1.4134 | -59.9504 | 2025-02-01 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 84d6e23e-a89a-3c28-851c-52169c598d02 | 1.4134 | -59.9504 | 2025-02-01 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ff7bbacd-2ed0-342c-952d-bd11d967fb57 | 1.4134 | -59.9504 | 2025-02-01 08:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1154585f-a781-32c9-9262-352f8f92524c | 1.4134 | -59.9504 | 2025-02-01 08:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7c0f0b71-bd69-3581-9cb5-6ab48b03b897 | 1.4134 | -59.9504 | 2025-02-01 08:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1ec05c11-3cec-3f35-9842-d6fc0592afae | 1.4134 | -59.9504 | 2025-02-01 08:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b8750e96-1598-36be-9f12-40ef168e2758 | 1.4134 | -59.9504 | 2025-02-01 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 502fd784-d090-3ed5-8969-23b415d91301 | 1.4134 | -59.9504 | 2025-02-01 08:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 302ba9c8-e9c3-3a04-bf79-b2b60e6db5f7 | 1.4134 | -59.9504 | 2025-02-01 09:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fbf37107-7f66-3fa0-9a8e-c4aeb28ecf1c | 1.4134 | -59.9504 | 2025-02-01 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1f929498-e772-3c96-9465-846537b70099 | 1.4134 | -59.9504 | 2025-02-01 09:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4a49e965-0965-3a02-9e03-c742d798f372 | -7.85822 | -38.83133 | 2025-02-01 11:29:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 38.7 |


