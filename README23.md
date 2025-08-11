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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36bf0ecd-1d6c-37c5-8d4c-71b32d2b6d6e | -7.0635 | -59.19033 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bd9400a-8391-3fe7-a9dd-cec87946916e | -7.08664 | -59.19395 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaf655c3-0942-3482-bf83-2a1cec44f58f | -9.36975 | -61.52706 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea8bee8-455a-3edb-8431-b2874310662c | -7.0861 | -59.19741 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85f12dfa-ca7c-3abd-8430-720deef52838 | -8.56274 | -54.69885 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82916d4f-9011-34aa-accf-262dbba57705 | -9.37535 | -61.53553 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e9846a07-8e7c-3c00-a69b-99c5702d91c8 | -7.07497 | -59.16024 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8781ffd-86f8-3bcf-b71b-13d921b8d928 | -7.06241 | -59.19725 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08ca6e26-c4a7-3628-b727-b3dfb885a1b7 | -7.06025 | -59.21108 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b44dcbc7-495d-3d1f-ab6f-cd9cea69e821 | -11.27111 | -50.18912 | 2025-08-11 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95d0222a-dc8f-38c8-a752-120c9cb4942d | -9.73679 | -63.19344 | 2025-08-11 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91545f21-3d5a-380d-baae-8081ef030fe9 | -8.92809 | -60.74428 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b13e20f-138a-32a5-8c3a-225ad080aef3 | -11.77848 | -49.57223 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 946f74f9-58cc-3f5c-ae4b-6c382131e658 | -7.08273 | -59.17562 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c4ef39-432a-3703-b3eb-94260136441e | -8.5622 | -54.67366 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0244328-d892-3923-ab4c-f53fde14051b | -10.37474 | -50.80642 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e7b04195-c2e3-39d7-bd69-0c9198c26ca8 | -7.07618 | -59.19586 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c48fc4b4-50dc-35e1-85a5-c1f79e4f45f7 | -8.92697 | -60.75139 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca72423b-c0e5-3382-a025-73e19121bde0 | -8.56372 | -54.69186 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af500b1c-3185-354d-b2a2-b0aaa5e1c5ff | -7.08826 | -59.18357 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91823c8b-7c9b-33c5-9ec2-66031bf7da36 | -7.06187 | -59.20071 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37cd0d24-478f-3665-8ecb-fdd861a1cd38 | -7.06626 | -59.19431 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21ac7cc5-421f-39f8-93ac-661884fb8345 | -8.56422 | -54.68836 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfa80937-c079-3f5f-bfa9-3ed86f12a652 | -9.92913 | -60.47903 | 2025-08-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e91404e4-f3f0-39d7-afad-34541a9f51a2 | -7.05742 | -59.18584 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03bcfe42-3e9c-36df-ba6f-1875190b81da | -10.37347 | -50.81665 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8f581c1-ca8f-33e4-919f-4e62b6f0172d | -9.37814 | -61.53977 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cea254d7-443e-3066-b48b-75f5a2329772 | -9.37374 | -61.52393 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5e40a28-b6c5-3ffa-aed8-ed1f2991cd5c | -7.06795 | -59.2052 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 461576c7-24f7-3487-a7c8-867fa9a5b2fd | -8.57573 | -54.69361 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a8b0e7b-1353-30c3-b80d-a398cea7986f | -8.56521 | -54.6813 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd51e29-47ff-33b2-acb9-8c0872190cbc | -8.91804 | -60.76452 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93428329-75e4-341d-b174-a941f394aba7 | -7.07786 | -59.20675 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e715075-ae59-39dd-a63a-f4219adee0f2 | -8.93241 | -60.73408 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| deb8642c-ef42-3052-9fe4-a0bdd5c71601 | -8.56971 | -54.67838 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f69cd56-713c-36f2-af30-34436c4835e1 | -8.92842 | -60.75895 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa953f77-0a62-3e4e-81ae-a78db3ef16ce | -9.21329 | -48.53903 | 2025-08-11 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 269585d8-98a4-3171-a083-bcb98826d833 | -8.57272 | -54.68601 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ecb2e5a-78fe-3581-a264-a7ed50abe42b | -8.5617 | -54.67717 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e765087a-4cfd-3e58-a03b-c3a8e8feca0f | -8.57073 | -54.70007 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c78ae798-4638-3f83-9786-8b8982bb18b4 | -11.7579 | -51.61905 | 2025-08-11 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de8e017-6dd0-3e85-9d0a-87d5a7741bfc | -7.06181 | -59.17944 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33271f66-e3a5-3916-b8b7-e876347ae260 | -8.57024 | -54.70356 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82fd7c54-e3c4-361d-9a03-0749802f1362 | -6.09037 | -59.9287 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8f103d-b0c4-3b3a-b423-b5e11348bf36 | -7.06127 | -59.1829 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad0564f8-2972-3659-b9eb-eeab3d34a45e | -11.71286 | -50.10956 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e19f72d9-73f4-34b9-b7cb-8f92265d59d1 | -11.77948 | -49.56398 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7df41f16-a4b6-333a-ac6e-5a0974803c29 | -9.37135 | -61.53867 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fe29737-398a-3a54-af46-a37f29f6138a | -9.37594 | -61.53185 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 360e9c43-3a83-3e75-9eda-36e14465766d | -7.0668 | -59.19085 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2221e46-2279-32cd-8089-d1675cf2b612 | -9.34427 | -60.32758 | 2025-08-11 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7d84323-2cde-374f-938d-5bf91b0c2d99 | -8.90892 | -60.54174 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6276ab8f-e4d3-3776-bc68-f947a78530da | -10.37262 | -50.82349 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4f8008b-7201-3bd0-9345-57fead7c0aaf | -8.9329 | -60.75237 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d972a7-8fbe-356e-8fe7-01914d8bd712 | -7.06458 | -59.18342 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5bcac35-331b-33c8-b390-f28cde3acac0 | -7.07672 | -59.1924 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fd9ab81-8ad4-3007-84ab-7bf872f5affa | -6.10479 | -59.92376 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27c7e2c5-6a75-33af-8e86-3a8aff90562d | -7.09103 | -59.18755 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4269f925-112b-36b2-89ef-ede4b3728854 | -7.07456 | -59.20623 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6c2659f-2efd-30c1-88d6-0a69cbbcad3a | -8.93034 | -60.73007 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37c39936-a42c-31f1-9093-9c7551be4940 | -7.07774 | -59.16421 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550d84b8-d033-308e-9f3d-854d0cf8225e | -10.30688 | -48.11061 | 2025-08-11 05:18:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79a7cc42-9ba3-3121-882f-09307550eb89 | -9.37874 | -61.53608 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bdb85654-ce42-3d13-adc4-1dae1338c716 | -6.10534 | -59.92025 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68029c00-b1b5-3bd8-8ed1-18a125a08a7a | -8.56121 | -54.68071 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fc09974-1ee0-3962-8609-6ffbbe0eacca | -8.57172 | -54.69306 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f86468d9-c042-371a-b25c-99854ea4565e | -7.06518 | -59.20123 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36c44ee8-a99b-371f-afd1-4df877f2c795 | -7.08225 | -59.20035 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a2a423f-d8bf-3260-be44-6b50add034f3 | -7.05634 | -59.19276 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b594263-0aef-374f-b34f-b3dbc141b243 | -6.10146 | -59.92324 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b38a1e16-268d-33fd-9756-cac8000ddf26 | -12.60874 | -47.13991 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa6c2824-0c6a-3ea6-b8db-d114c435b7d5 | -9.36915 | -61.53075 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b19aa89-2179-3e9b-b53e-a0cc55379197 | -8.56772 | -54.69247 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd000293-cb6f-332a-b265-df2c3fd89fba | -10.3739 | -50.81324 | 2025-08-11 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6ec3bdb7-6b23-37c2-9a9c-b0e8f194bf30 | -8.99465 | -68.46151 | 2025-08-11 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f26e3a-0d85-3d8c-81e6-528d276a6539 | -8.57523 | -54.69711 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c060394-98a5-322c-8343-1066658d9ade | -8.56575 | -54.70645 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c085eb3-0076-30d4-84ef-615496456cfe | -7.08117 | -59.20726 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd0f39a1-de44-310a-bd79-5b954769fb17 | -7.08502 | -59.20433 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e37cdde-54dc-371d-a93c-cf9be847f1a0 | -6.92943 | -60.06547 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb4b00b-752c-35ec-9207-1e9b07c970ac | -11.12002 | -54.65642 | 2025-08-11 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc052b7b-a017-3072-a720-2bfbcfdb5687 | -7.08171 | -59.20381 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86d1277d-46d9-3d36-8a09-05ed46c5241a | -6.10091 | -59.92675 | 2025-08-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70c1ac45-1856-3797-b3c7-e050952dd7a5 | -7.08111 | -59.186 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 102840ab-f372-30f0-a157-a9d756fa09bd | -8.56323 | -54.69535 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9706d357-725a-3c46-af7f-2f7370a4b485 | -8.93517 | -60.73816 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9befd108-2854-3e8f-823b-f5cbeadc30b1 | -8.93404 | -60.74526 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e71838c0-fa79-3d91-a8fb-91757dbc22ee | -12.60919 | -47.13737 | 2025-08-11 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fecdca7-c0c0-3e01-9b63-61d3fc47b46d | -7.07233 | -59.1988 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2a4e162f-d3dc-3534-b156-e50d763a4317 | -8.56225 | -54.70236 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80dd7b16-b46e-3d08-8811-928f94b9e7f4 | -8.93567 | -60.75646 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f7cd49-2c2b-3a67-aca1-f78ea5e6ad2e | -8.93127 | -60.74117 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae836217-2cf1-34ea-b24d-70472d172c30 | -11.77679 | -49.5711 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0dd524d-b848-3dd6-b815-9f5e3fb387bb | -8.92753 | -60.74783 | 2025-08-11 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 147b6f98-6627-3019-a93d-80b7f2ba9254 | -7.06903 | -59.19828 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c58ba24-aa51-3f26-b9a1-e4982d6b3649 | -7.08333 | -59.19343 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 728ca6ef-bbd0-3bc6-bdf2-38c56c646ca9 | -11.69905 | -50.12785 | 2025-08-11 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9bc1c28-1e85-3f4f-bdd1-3e5398bc7285 | -7.07065 | -59.1879 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb24b8bb-20a3-3649-8fdc-94d611c50a59 | -7.07341 | -59.19188 | 2025-08-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05c97d51-31b4-3497-ae89-0961ca8a5d43 | -8.57422 | -54.6754 | 2025-08-11 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
