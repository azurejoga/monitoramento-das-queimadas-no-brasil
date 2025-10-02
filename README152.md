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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 041dd03a-eeb1-3905-b893-54017729286e | -11.8238 | -45.0132 | 2025-10-02 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 20d070b0-8d28-379e-aef1-5780fc3d5441 | -10.0145 | -50.2657 | 2025-10-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f74b2a60-ebf0-381e-87ca-8dde638d8c75 | -12.5001 | -50.2453 | 2025-10-02 13:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 12c27836-e86c-32c3-a7fc-d9521341b281 | -9.08 | -46.7215 | 2025-10-02 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 828cd3d9-fe40-392b-8ebb-3f7412977b3e | -16.0417 | -50.8959 | 2025-10-02 13:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 618d66f8-e712-3649-9b20-732997377be9 | -13.7864 | -48.0524 | 2025-10-02 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e7a0f0a6-9391-3699-a1fb-73e05c79aace | -7.5661 | -42.656 | 2025-10-02 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 30653519-31b3-35fd-9b6f-b84488b9055b | -14.4757 | -48.4137 | 2025-10-02 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f1bfdc31-08e0-3cdf-9f87-864f5ef986f4 | -8.1702 | -44.1377 | 2025-10-02 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 305.0 |
| e737589a-7891-39a4-8c72-064290c24ab2 | -10.8622 | -46.5814 | 2025-10-02 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 45138d22-8e3d-3d0c-bce1-b3e1942b037f | -10.8625 | -46.5589 | 2025-10-02 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1775aa79-a74b-3760-8a24-351ea38104b9 | -10.9751 | -46.6569 | 2025-10-02 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 57e57be2-2a09-33e1-92dc-2b9fa75c2a7c | -10.1273 | -50.2971 | 2025-10-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c5ce63ef-f72c-3bc7-9cf8-0f0a2200e8ba | -11.9272 | -47.8941 | 2025-10-02 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b81c9af1-91eb-3526-9a6c-17f244b37768 | -14.3114 | -45.9967 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9ef0daf1-1ee9-3c6c-aa28-c83d72c64ee3 | -9.336 | -45.9305 | 2025-10-02 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 13c36eda-cce4-3b2b-93e8-d9c2fbef324c | -8.5599 | -44.6494 | 2025-10-02 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 170.5 |
| c2c50553-4298-356c-92cb-2302d95de9d5 | -14.5937 | -48.3281 | 2025-10-02 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 05629210-68a5-3c76-848c-1e99e77f54ec | -16.0221 | -50.8989 | 2025-10-02 13:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 66bf4891-6a9c-3080-a7b4-cd2aad54adfc | -9.3392 | -45.7039 | 2025-10-02 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 65ca33d6-ed83-3f84-b24b-336a2bdeda5a | -8.8929 | -46.6072 | 2025-10-02 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 995671a0-29d6-32a2-b490-9129dd114239 | -9.4272 | -47.5722 | 2025-10-02 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ca3977fc-5a79-3a29-96e2-47b15451c73c | -11.9276 | -47.8719 | 2025-10-02 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 077cc10f-f794-3b5d-8e9f-5aa214d20d39 | -8.5596 | -44.6724 | 2025-10-02 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 5f0b39f0-2151-3e56-8ae0-e55e96b43f45 | -15.2542 | -49.3104 | 2025-10-02 13:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 1f000fec-f5ce-3953-ae02-728eb9bfc5bf | -15.2738 | -49.3073 | 2025-10-02 13:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| ad74295e-1061-365d-9e15-97c55002d53f | -11.8234 | -45.0364 | 2025-10-02 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d0a3fd73-e2a5-3e2f-ba90-15d908172201 | -14.4255 | -46.115 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0aaeff91-5d36-3c72-993d-fe9ecf58d71f | -14.4947 | -48.4329 | 2025-10-02 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 293cc34f-f4ae-3577-a32b-0d5923cc1c99 | -8.6911 | -47.6906 | 2025-10-02 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d2b74fb6-9723-3336-83eb-8a40c3e7e88a | -8.2105 | -47.0084 | 2025-10-02 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2d7d9be1-27fd-3846-9433-edfd693e06b6 | -10.4308 | -47.4825 | 2025-10-02 13:00:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7d6651fc-1a4b-3123-a354-fc928fb45449 | -9.3389 | -45.7266 | 2025-10-02 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 19598de7-ad47-3175-a11b-31f65f97244d | -8.5204 | -47.8167 | 2025-10-02 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c59d7bdf-274b-3786-862c-5898c68f6090 | -15.3072 | -45.0477 | 2025-10-02 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 24f21ebe-ce17-3120-ad68-d193871b0b39 | -10.1084 | -50.299 | 2025-10-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 87ae7787-b88d-3a26-ae01-43a78c8687df | -15.3067 | -45.0713 | 2025-10-02 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 320.6 |
| e1ed2fc1-4a26-38c6-8cf9-11ea5b7a766f | -11.8238 | -45.0132 | 2025-10-02 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| dce25254-c98f-3ac3-895c-4e61b85513df | -12.6729 | -46.851 | 2025-10-02 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| c70ab82c-4e82-3f1d-b576-dc5c4a4bba02 | -6.7816 | -45.5703 | 2025-10-02 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 454e0ed2-778b-3027-9bda-62420ef7aede | -14.1917 | -46.1552 | 2025-10-02 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 265.2 |
| b68f9356-e27f-3626-967d-97c1720b3279 | -14.3709 | -45.9403 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 882e0815-82b8-3783-99c3-074d72567e87 | -7.7311 | -46.2289 | 2025-10-02 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ba761ce1-6364-3d61-833f-20941fd926c0 | -14.8212 | -45.8143 | 2025-10-02 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 50b2b6a0-8e9e-3688-b0ba-54f20dba7318 | -9.4083 | -47.5742 | 2025-10-02 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 667a5cd4-e829-3348-8cea-1c75cf37a055 | -7.8882 | -47.281 | 2025-10-02 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 32f20d22-df18-3cfa-8981-de1e03fc1a65 | -14.2924 | -45.977 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b7176ba9-76e7-3283-9667-e0a7acb45631 | -14.3704 | -45.9634 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a3a00622-845b-39bc-8a8b-d8dce42fdb8e | -12.902 | -46.9299 | 2025-10-02 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 72302a11-906b-3267-8102-07bdd4108a08 | -6.6978 | -42.8118 | 2025-10-02 13:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| a310c2f0-ac5c-30fa-8cb7-3a165511ab48 | -14.1921 | -46.1321 | 2025-10-02 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 7f771eb9-ba7d-375e-aa27-b33644e1950b | -7.5472 | -42.6579 | 2025-10-02 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 9d3513dc-b7d3-30e4-a9a4-30524c6fcf3e | -11.2799 | -47.8445 | 2025-10-02 13:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 378d5777-d30c-3183-9753-537b24f4ed04 | -9.4086 | -47.5521 | 2025-10-02 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ab815646-5072-3bd3-b7c7-9a4025efe94f | -14.425 | -46.1381 | 2025-10-02 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e8498cd9-4c42-3271-a531-f668de2b46f8 | -8.6722 | -47.6924 | 2025-10-02 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4f9e3919-9edc-3ba9-a5e6-90127c636482 | -16.0025 | -50.902 | 2025-10-02 13:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 24a87897-b205-325c-9355-528fcd1c01ad | -12.719 | -48.5832 | 2025-10-02 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8ce95098-8ac5-3acd-9148-e8500a3bfbfa | -6.7626 | -45.5944 | 2025-10-02 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e098b8d6-dce7-35e9-a5dc-f9ff9d532dfa | -7.8879 | -47.3031 | 2025-10-02 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d4742f8f-05e6-3e25-b6b5-62c5d5f04ff1 | -12.9024 | -46.9073 | 2025-10-02 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| bab2f97b-c63b-33c1-968a-de232a9732ae | -14.4753 | -48.436 | 2025-10-02 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c8c589fa-8104-3366-93c0-c90e6ef18ace | -13.3089 | -47.8118 | 2025-10-02 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 277ca041-58a9-3aa4-8290-1b3f86362636 | -8.1513 | -44.1397 | 2025-10-02 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 3883f805-3b73-3261-a9ce-9c7c0b1b01b7 | -11.9085 | -47.8745 | 2025-10-02 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8987046f-b69d-37e7-9278-8553c2517d98 | -6.7814 | -45.5929 | 2025-10-02 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 4e4dc50c-cd89-372e-a1b8-ce010d004234 | -10.0906 | -50.2154 | 2025-10-02 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 938b0085-c76f-3bde-b96d-db044db675d3 | -8.5201 | -47.8386 | 2025-10-02 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fd839675-4d21-339d-9724-7768a134ed8b | -8.2094 | -45.5301 | 2025-10-02 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 69a20283-1b68-37e3-8192-162c39c45e46 | -6.6976 | -42.8354 | 2025-10-02 13:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 4d311889-963f-3126-b7f4-ebab23e0578f | -6.679 | -42.8136 | 2025-10-02 13:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| dcc7ffb4-c23a-3496-b65d-d9c3b2b63b49 | -7.7501 | -46.2048 | 2025-10-02 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 99ea35ed-927d-3d34-85a9-e6d3be8a528c | -15.3067 | -45.0713 | 2025-10-02 13:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 0a46b13c-edcd-3915-8360-e429e5acdca1 | -8.1702 | -44.1377 | 2025-10-02 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 61feec3d-c6f6-3e05-8f5a-0e9cda12466a | -16.0421 | -50.874 | 2025-10-02 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9f131781-d934-3d48-8e49-109a0a6e4f6d | -9.08 | -46.7215 | 2025-10-02 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 64ffbd48-521e-30d4-876c-06141fbf3c70 | -11.2803 | -47.8223 | 2025-10-02 13:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 3833a6bc-eb50-30d5-984c-4cf1072635df | -7.8879 | -47.3031 | 2025-10-02 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 43654f0a-f013-3388-a8c4-3c335cec8cb5 | -8.5204 | -47.8167 | 2025-10-02 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a1357148-b137-349a-bd62-e857aff9dba6 | -13.1542 | -47.8568 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8d6d5bd2-3cea-3da7-a08b-36bff64f98ba | -10.1095 | -50.2135 | 2025-10-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c8fea603-3eee-3f95-acba-55c2407be33b | -14.5937 | -48.3281 | 2025-10-02 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 01145470-d814-31c8-aca0-fe82be17c1e1 | -16.023 | -50.8553 | 2025-10-02 13:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 29de2967-4e97-36c3-a3de-d9a97d753f41 | -9.9376 | -43.6953 | 2025-10-02 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 71127deb-d17e-3ba9-b1e2-7a30a6f816d4 | -8.2105 | -47.0084 | 2025-10-02 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 29dff30f-727d-3730-9634-d97048222778 | -13.1928 | -47.8512 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 1c308114-464c-3fa7-860d-2c79542774b3 | -10.1092 | -50.2349 | 2025-10-02 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 83d6079b-7973-3c81-9959-99e3b016c013 | -10.8424 | -46.6289 | 2025-10-02 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 6a30e2ef-d742-3c62-9613-cd4dd17b6bfb | -11.4792 | -45.0174 | 2025-10-02 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 267061ee-d08f-39b3-bbe6-753c33c620c7 | -7.7563 | -42.541 | 2025-10-02 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 708878e2-6b5e-3154-b0f8-464253316f5a | -9.4083 | -47.5742 | 2025-10-02 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 45d12ae2-e74b-3bca-9a95-cf09b440793e | -8.5201 | -47.8386 | 2025-10-02 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5f84f5d7-3604-3dc0-b6ed-d49f625995c6 | -10.8622 | -46.5814 | 2025-10-02 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 19ca4653-dac1-3271-97d9-99911f52f954 | -6.6976 | -42.8354 | 2025-10-02 13:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 7d2b6e23-2f93-39f5-9dd9-ad127fdfc998 | -13.1747 | -47.7869 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8588eae6-4cad-3f8e-9609-f1ec7db84694 | -14.425 | -46.1381 | 2025-10-02 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c183f97a-42ec-36f9-a907-1b20a6a884e4 | -8.5599 | -44.6494 | 2025-10-02 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8f71dc5a-7aad-398f-8684-6fc3f876bf9d | -13.1739 | -47.8317 | 2025-10-02 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 60cddf12-e027-3296-86a4-887270d138ff | -14.4753 | -48.436 | 2025-10-02 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3429e599-de1b-3d5d-9c94-deea6b477a51 | -9.9369 | -43.7422 | 2025-10-02 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 160.3 |


[Clique aqui para ver as próximas entradas](README153.md)
