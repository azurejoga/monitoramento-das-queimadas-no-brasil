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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56b3c869-14a4-3f3a-a1e4-f433b5d109e2 | -6.2026 | -57.7778 | 2026-09-21 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 619d919f-9b76-35b0-9952-1c4066659d1b | -7.4092 | -44.7885 | 2026-09-21 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| ce532343-4e1c-37f6-b7cd-c09ce41ba96c | -9.831 | -48.4292 | 2026-09-21 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ed6cd7a7-b20c-3c2b-b089-5e8fb4c5acf6 | -8.7726 | -44.28 | 2026-09-21 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| c670bdae-dcad-39b6-a5a5-9167716a29a7 | -9.4567 | -45.4178 | 2026-09-21 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a43ec7a1-f29a-32fd-9616-83d0f1377c53 | -9.8307 | -48.451 | 2026-09-21 12:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 19859060-f837-3682-a8ef-f530d317bdbe | -12.9091 | -50.9672 | 2026-09-21 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 305.4 |
| 774fee57-de9e-36b4-93f4-5115676b3878 | -10.7626 | -50.8069 | 2026-09-21 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 63df246d-8356-345c-8118-648cc9c424a7 | -12.9283 | -50.9648 | 2026-09-21 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ae34950c-802f-3a59-b9ed-cddd1cf03218 | -5.9335 | -59.9515 | 2026-09-21 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| b25927bf-a94a-3092-a5e8-daadae188fbd | -6.7464 | -59.4223 | 2026-09-21 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 12d5e344-ae14-3cd0-abff-9ef006314e4e | -11.041 | -54.1567 | 2026-09-21 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8fade416-7fe2-391d-864e-b06f7758294c | -10.3924 | -50.2275 | 2026-09-21 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5b6629dd-d68a-3649-88d2-7581d042192d | -7.4124 | -49.853 | 2026-09-21 12:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 156000d3-2345-32eb-aa40-680adb3ef354 | -10.4486 | -50.2644 | 2026-09-21 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| f4c1822b-4404-36ea-b563-92bea2973e06 | -7.4092 | -44.7885 | 2026-09-21 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 60e6c2af-4657-3233-89f2-cb30ae3c6f6a | -10.7064 | -50.7703 | 2026-09-21 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1ed562bd-aec7-3ada-89ba-1ae674ec2c2d | -6.7464 | -59.4223 | 2026-09-21 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e1c2d50a-5763-3606-a6b1-3632c32bebba | -12.5415 | -50.046 | 2026-09-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 58ae4ad8-a773-3abe-9ac5-27c942e1b649 | -7.5661 | -42.656 | 2026-09-21 12:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 191.4 |
| 6de7b828-fedf-389b-8dee-4fb1ef51c7cd | -7.428 | -44.7867 | 2026-09-21 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 17f1b277-b8db-3a8c-b3d5-c05711388d23 | -11.8682 | -46.8529 | 2026-09-21 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b78b1dcf-e71f-3c43-ab7b-6479d87ed831 | -10.3917 | -48.8915 | 2026-09-21 12:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1934ce07-7567-3201-963f-37012afdd8c5 | -7.3289 | -55.2155 | 2026-09-21 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| aff365be-8e31-3533-bade-95c6a7fd5a13 | -9.2383 | -46.1668 | 2026-09-21 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a249b672-72a4-3491-984d-281ff44a7a92 | -10.0898 | -50.2795 | 2026-09-21 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d035ae21-8e4b-31b6-ad6c-0e9c67ce9bb5 | -7.3291 | -55.1955 | 2026-09-21 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| d7f566e5-0deb-3cef-904e-32d2eefce0b4 | -8.7726 | -44.28 | 2026-09-21 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| e99fe020-f853-324d-9f5e-b25102a065d1 | -10.8011 | -50.7604 | 2026-09-21 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 33d01390-edd9-3423-a113-34b9321ed0df | -9.4567 | -45.4178 | 2026-09-21 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7cb41899-834a-3a3e-8356-aa7147d99966 | -11.9969 | -58.0622 | 2026-09-21 12:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5b318bc4-4b69-3040-9cc6-35ab06dea2e2 | -12.8437 | -54.0422 | 2026-09-21 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 648.4 |
| b705f14e-3080-3b18-a03b-87858c185d60 | -8.7729 | -44.2568 | 2026-09-21 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f1e70b61-3ba2-341a-89da-fc1dfbbd72f5 | -12.8246 | -54.0442 | 2026-09-21 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 497.0 |
| b233c95e-ec0e-3144-a0a2-9cc381909e52 | -6.8263 | -55.5421 | 2026-09-21 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fc072130-5151-333d-baa8-5a6d0c5bfb13 | -10.3914 | -48.9133 | 2026-09-21 12:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8bbf4905-b598-3b1f-a192-ffaa3eeacc0f | -11.041 | -54.1567 | 2026-09-21 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 49c70472-b8ff-3752-a111-6c1548784e50 | -6.2026 | -57.7778 | 2026-09-21 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f94699a1-e5ae-3c38-87b5-b49c0c64a7af | -9.8307 | -48.451 | 2026-09-21 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 807d6763-c206-3f8c-a16a-08de717f2f34 | -10.8096 | -50.1407 | 2026-09-21 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4fbabe42-d574-3308-b17e-be12d4e6316d | -8.7911 | -48.7502 | 2026-09-21 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 68.9 |
| be2fed04-eb88-3f5a-8f98-5a1c95adc22f | -10.7626 | -50.8069 | 2026-09-21 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e8d839dd-d474-3d14-be53-e65300beca63 | -10.3728 | -48.8936 | 2026-09-21 12:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2cf2e2d9-203b-34e8-9068-457e1e8eb359 | -12.8899 | -50.9695 | 2026-09-21 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 5d76f4bf-1173-30dd-a33b-8db8f371bc60 | -8.7537 | -44.2821 | 2026-09-21 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 9104b746-a3bf-3696-89de-b84dcb9faa59 | -9.831 | -48.4292 | 2026-09-21 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0982a89e-df75-3239-8183-896a16fcf8d4 | -6.5569 | -45.566 | 2026-09-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 7c4c6792-d71e-332b-adbc-3f1fea169eef | -6.5759 | -45.5419 | 2026-09-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d2ce9bf2-ec62-3179-9f39-1b5166bebdb7 | -5.9335 | -59.9515 | 2026-09-21 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ae8311ef-b9fd-3691-bc7e-cf2d41ddf8e8 | -11.8014 | -49.8129 | 2026-09-21 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8f2c2029-9c02-3f1e-aefd-31ac67ced881 | -5.9334 | -59.9707 | 2026-09-21 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 268d0d71-fda4-3a27-b74d-44abe4a20640 | -5.9151 | -59.9522 | 2026-09-21 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| adc453b7-e85a-35d6-a58a-7ddce66c112c | -12.9091 | -50.9672 | 2026-09-21 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 190.5 |
| f5fd7cf0-a1ba-3c1f-8440-c9422317faef | -8.754 | -44.2589 | 2026-09-21 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 231bb647-f94c-32ef-9ce5-351bc960f247 | -10.4675 | -50.2624 | 2026-09-21 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c1daf60e-f458-3a0d-8c58-108083adb03b | -12.9283 | -50.9648 | 2026-09-21 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| cefe97f6-c6ef-37fc-8be9-ce031fe37f6d | -10.744 | -50.7876 | 2026-09-21 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 721d687d-ab92-3d6b-9e6f-2d58d2db7ae1 | -11.9507 | -46.5033 | 2026-09-21 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8cf25bb-b714-308b-84f4-c83f3b6a5373 | -10.7262 | -50.7044 | 2026-09-21 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6b916cf6-00db-3176-88b3-384e544d6af7 | -6.8448 | -55.5411 | 2026-09-21 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 24d2539e-6e07-3988-a2fb-518c24d263fb | -12.4204 | -47.0228 | 2026-09-21 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f991cbb4-6eaa-3c39-bc38-17ffbf0855cc | -10.8662 | -50.156 | 2026-09-21 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3a4ef844-a523-36f9-b6d9-823b2fc1ea63 | -11.9967 | -58.0821 | 2026-09-21 12:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f2ad5776-5394-3449-97f7-7c0d204b2b4d | -7.4124 | -49.853 | 2026-09-21 12:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 76633104-f819-3529-8e00-23316a9cb092 | -6.5571 | -45.5434 | 2026-09-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 63d7a7fd-74f6-34fc-bbee-c157fc601702 | -13.2794 | -51.7524 | 2026-09-21 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 770f33dd-ede5-357f-84fc-d2f7fa40f95b | -12.5419 | -50.0243 | 2026-09-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 76777b40-3ec5-38ca-b8b6-7a94c7cbab6d | 2.10002 | -55.86388 | 2026-09-21 12:42:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b53f06d2-9e26-3df2-890f-0fa02e48d817 | 3.60702 | -60.65671 | 2026-09-21 12:42:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3ef39987-bb2f-397e-af12-5d3dbccf3295 | 4.53854 | -60.86054 | 2026-09-21 12:42:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9343d5c8-b453-38ea-9a71-371cc265a5ac | 1.91302 | -50.83223 | 2026-09-21 12:42:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4f1ef64b-c264-3e3c-881c-1899799ab709 | 0.68828 | -59.54569 | 2026-09-21 12:42:00 | TERRA_M-T | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62c5299d-ae32-3f2d-8789-08afab01094f | -1.68625 | -60.36117 | 2026-09-21 12:42:00 | TERRA_M-T | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fce85b0b-4462-31d6-9c70-837e3eef3286 | 0.78717 | -59.20673 | 2026-09-21 12:42:00 | TERRA_M-T | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a501c7ab-11ac-3709-85c2-8ef3b7d03e57 | 4.96135 | -60.44778 | 2026-09-21 12:42:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af2cdaea-5634-320a-b1c7-23ee0dc3792a | 1.55421 | -55.83112 | 2026-09-21 12:42:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| e95b0784-fc0e-3c98-a6f1-154055a2ff86 | 3.27634 | -60.54781 | 2026-09-21 12:42:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0344fc76-82ed-3429-b716-09cd3c38ee68 | 1.53892 | -55.80442 | 2026-09-21 12:42:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 20e761dd-0611-3bd3-a18c-7cf4e1d69587 | 3.28515 | -60.54659 | 2026-09-21 12:42:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a2416d71-d60d-3e51-a75d-a8bdab6a22fc | 0.78585 | -59.19742 | 2026-09-21 12:42:00 | TERRA_M-T | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7fff126b-5b3e-39c4-8d9c-91adc83ab1cd | -8.05185 | -61.32517 | 2026-09-21 12:44:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 697e97f1-8bf8-3ace-9ab3-613c41ba5e7e | -9.41088 | -65.92154 | 2026-09-21 12:44:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b8636eef-fb98-36f5-8371-e39af4e45004 | -7.3123 | -54.92005 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 53865738-1879-33c5-a13d-97da2c86462c | -7.8181 | -61.80758 | 2026-09-21 12:44:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df4bbfe7-323c-356b-9b5b-4c7660885ce1 | -5.21679 | -56.1005 | 2026-09-21 12:44:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1d28cefe-381e-3b1d-ac93-ef8f7a444715 | -3.40105 | -59.5803 | 2026-09-21 12:44:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82ba2045-8ee3-36fe-976c-453ba36f534e | -6.28685 | -56.03128 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2fe0fe5c-26e3-3c68-8d20-950cce8ed3e9 | -5.92701 | -59.96597 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 816516a2-5a10-3725-b2b5-113c1b84318d | -6.14248 | -59.94641 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a86aaf21-0175-3487-842d-397040b69a41 | -10.87851 | -54.07323 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 8a50c25b-28b6-30ae-bda1-22f7bac7fc12 | -10.22256 | -59.39531 | 2026-09-21 12:44:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 31250569-1468-3248-8037-4468d900d3aa | -4.46311 | -55.66857 | 2026-09-21 12:44:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 41f27dbf-5bb6-3103-b08c-f2447993a230 | -6.64848 | -59.96379 | 2026-09-21 12:44:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7076ea1f-e358-30cc-b34b-f5bf0ff73cad | -6.75475 | -59.05794 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d7876425-7c92-3ba0-860f-714b31058cd9 | -4.01428 | -53.48039 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c1f01903-26cf-3a91-bdbf-abb48f0f4a5f | -11.03865 | -54.16263 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a9f173e0-c9f4-3f79-ba44-c29530316734 | -6.49729 | -58.38147 | 2026-09-21 12:44:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 582865ea-575c-3702-9cc5-2a8eae0f24f1 | -6.74785 | -59.41615 | 2026-09-21 12:44:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 805f890e-d898-3166-aed4-3df2d5e5b2a4 | -11.04237 | -54.13047 | 2026-09-21 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| fa71b01c-952a-3f1d-90c4-3278261547d8 | -7.32164 | -55.18584 | 2026-09-21 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README115.md)
