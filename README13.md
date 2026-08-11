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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e58e5cca-a2b0-325c-a3bf-90c8da32a736 | -12.47838 | -45.33748 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1f8b75f6-1ac4-3fac-8c6b-3c3f733728db | -8.94587 | -60.53683 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 46b57d26-3101-342b-86aa-241cbd928912 | -10.4242 | -46.67299 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58d18faa-4c6e-34e3-ae9a-363219b8049d | -11.29118 | -44.87492 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b23ef4e-3bd0-3e23-8de6-9d63884dc58a | -11.24042 | -54.87455 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4506a620-874d-3a72-ab37-415dd5e1b1eb | -11.25846 | -44.89122 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cbe802a-f854-3d71-9f93-d1931e85fd19 | -12.56544 | -46.52193 | 2026-08-11 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6186ef53-5434-3cb2-afc4-fee531bf004f | -11.23279 | -54.84446 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b910a8c1-3ac4-344b-af42-15bdb32b08b2 | -11.14079 | -49.03968 | 2026-08-11 04:34:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f2c2ae-e29c-3c5b-a52b-a596d72d0fe2 | -12.4938 | -45.28259 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9db7ccee-cb1b-3f4d-9afa-95e0830801aa | -6.83854 | -56.40509 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aafc5ab-394c-368a-9353-34b44b12f0cf | -7.38429 | -42.86237 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01aaf327-1091-3932-9712-2e35e4a0b54f | -13.59224 | -46.25316 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 008ded76-3c90-37ab-97c1-5e796ba053bb | -13.57345 | -46.27448 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dfaee3bd-8b78-3f24-9d57-ca832de3a376 | -13.59167 | -46.2509 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3eeebb5d-1cdb-3218-a1dc-126c7907d5dc | -10.41215 | -46.68284 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66c57432-4b93-3159-8b4d-0cee4bd7fd0c | -9.47355 | -60.52158 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56be6bf5-c123-3319-aa69-d5db67efe5b1 | -8.9435 | -60.51498 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 75885a73-ab99-3ee3-8aac-e0a43f0722e1 | -11.23311 | -54.84112 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3c5e167-4dd7-314d-82c8-e53f38279f80 | -12.48214 | -45.33804 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4ec0dc02-f873-3822-b337-6ea1707877a8 | -12.46269 | -45.33982 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7319fd6b-9b31-3e0d-8bac-bc430b4210ae | -13.59708 | -46.24507 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ea3a8c2-0de4-3860-adee-8770a629ea1a | -8.89474 | -60.59735 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 81c8d66a-1eb0-32d9-8dda-2b8951652d9a | -8.95118 | -60.54334 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 17fdd045-f7cc-3900-82c6-686660c37897 | -11.31513 | -45.22482 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcd8dddf-fc3e-38a4-b4cb-0aaa672b1526 | -6.01279 | -47.40364 | 2026-08-11 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4282b28f-d1b9-3d79-9196-c623238cd683 | -10.72954 | -47.91827 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eefb0c6d-45b9-34b3-8e7d-6b5e7854ae9a | -9.39757 | -47.47026 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba09e658-d899-39fe-b712-7c2d7f8a9e5c | -13.56197 | -46.2771 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a86c90c-a937-3ee2-91cf-73b956abf8c8 | -13.48533 | -43.07763 | 2026-08-11 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5904dfec-bdbb-33bb-afd8-b9d02a996ce5 | -12.47773 | -45.34211 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b062c168-5dc5-3e25-9bf0-93d777bf65d1 | -11.02503 | -45.65641 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 257e0987-0ede-3342-ba41-123ec5605a9d | -6.84346 | -56.4117 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4957df2f-366a-3c72-a07e-7c67bc8ce938 | -13.57105 | -46.26542 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3e3d34d-dad8-3b1e-a236-29e9aa4062d8 | -11.61057 | -54.65583 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 538b26b1-5c50-3291-b71d-4758ad153437 | -10.90647 | -50.28741 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d4d7dd0-1f0d-3c7e-bbf6-719c446c0463 | -13.56797 | -46.28675 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e4c3f465-2d8f-3e57-9cd1-ba318ae9d936 | -13.56436 | -46.28619 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d7709878-3b05-3fd6-acca-40f2bffce808 | -10.43671 | -46.63631 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e74b7cf3-fda6-3f93-a7ee-4768b2d3a982 | -10.50776 | -46.60325 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c0b01f-59a9-3086-b110-673b4ab96c33 | -8.95181 | -60.50581 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7be6cd0c-8ee3-3a00-bb69-84523e3a6ae2 | -8.64167 | -45.85657 | 2026-08-11 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 756c8510-917e-3a84-a74f-69a26649d093 | -13.57513 | -46.31396 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ab55c9-b43a-332f-98fd-ea077db2d3f0 | -8.59775 | -45.40186 | 2026-08-11 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7607485-ea47-3327-923a-e493949d0408 | -9.39405 | -47.47733 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3d2d8491-3da8-32bb-a980-788a0f550df9 | -9.13809 | -46.39476 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34a8c560-1923-3e73-b728-0756be1f0b1d | -11.97595 | -46.34861 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b7a618c-7262-3424-a4ac-074581ecf35a | -11.46992 | -46.6644 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 510ddd18-5f51-3eae-8b14-4072b6110ac8 | -10.89315 | -50.37094 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b4b52fde-fe41-3ab9-8b76-fd20798da97e | -11.45659 | -46.68215 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 59281a62-375d-3234-9635-5b30c8f32eba | -6.84812 | -56.40959 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c875c56-04ca-3d01-9f41-05fe0219bb7f | -8.89358 | -60.55784 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fde07d8c-3511-3a3f-a472-0347f2281022 | -10.41905 | -46.6839 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e7547e6-4c97-3632-b94c-ffa492b49406 | -9.13865 | -46.39094 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e85dcd6-9ad2-3211-bb98-71d317822d7a | -8.30556 | -46.38746 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f1c029d-ca0d-3399-a873-cd438e29208c | -11.46805 | -44.57508 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0eb6130-a894-3f34-ad7d-781f3a6b89d7 | -11.47634 | -46.62145 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07fe946b-c738-3274-b8b8-723b87b1d0ba | -13.60919 | -46.31699 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc4c718-7ef2-3c2e-be12-088aa789302c | -10.41849 | -46.68772 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc1474b1-4f23-3187-b1fe-be30e6a21468 | -9.39624 | -47.46309 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 85779fbc-bbbc-3cea-84f2-cbed379338bc | -12.48099 | -45.31891 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bf62c19-dffa-3428-a9ed-68bb4a62e3ef | -8.94742 | -60.49453 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3f5e23d-4168-3741-a5e2-d896ba928ab4 | -7.92132 | -49.07415 | 2026-08-11 04:34:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d26592-3c71-39cc-808f-9f0b7e9e2cff | -8.95812 | -60.50702 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37d95c2c-2da8-3673-828e-dbc27da1b1bc | -11.47788 | -46.62055 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3db1f5b-d9d3-3df9-afaa-e96062808736 | -12.3632 | -44.12628 | 2026-08-11 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15c29ead-ba2f-36d7-9ef8-bbe6330b4952 | -10.22401 | -45.8708 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6abdbda8-4a8d-31f8-a7e3-a88d55028449 | -10.23584 | -45.86462 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 143279fc-0f1f-3bf7-8abe-ae65701765b7 | -8.55486 | -45.34489 | 2026-08-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 195a718a-e769-332e-ba53-39bbb9eea5ef | -10.83809 | -50.3694 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee7f27e0-a587-319b-9601-1e9f39419fb3 | -11.88569 | -46.81163 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbdbb096-5fe4-37bc-8aed-03b7ed9a948f | -11.60576 | -54.65887 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6ea6dad-4fec-315f-8d4d-d07b0830f958 | -13.57831 | -46.26643 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5cd9dc7d-fda1-3b5e-8c6d-bb60c008b629 | -13.62246 | -46.22281 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| abd67e9a-9907-3117-872f-53797aeaa860 | -11.19178 | -54.85415 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4da4c818-aeaa-3b82-b999-b3a72f07f514 | -6.84396 | -56.40873 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a15e18be-df7a-3b7d-aa31-e37d00f79590 | -8.53347 | -49.69555 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 003b18d8-605c-3554-b711-bfef49953e24 | -7.62635 | -42.76736 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ea84fa1-f697-315c-85b3-d7e0ddfee2b8 | -8.8944 | -60.56524 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3fbcbb7a-a54f-3c6e-9252-fb9ec54f41da | -11.97185 | -46.35187 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98d2bc6c-48af-309b-bbe4-25bce6be57eb | -13.48529 | -43.07651 | 2026-08-11 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| fea46b04-9d20-3bd7-bf0a-110bf95120dd | -11.22687 | -54.85216 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9509463-3a29-39c8-b70d-26910a6a28ec | -10.49451 | -50.30226 | 2026-08-11 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88990136-c882-38a9-a4f3-f95956ac620c | -10.88862 | -50.37767 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6694842-4340-3c9c-b0ed-812b8fd4a38f | -6.88886 | -43.71569 | 2026-08-11 04:34:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 935964e5-0671-3f2b-927f-6b4fff8a0b0e | -12.46347 | -45.3067 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdf90118-5cec-3074-8f1c-c94b254324af | -13.06074 | -43.06603 | 2026-08-11 04:34:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e8677fc-efb7-3ad5-8d72-a49a57165c51 | -8.95654 | -60.54964 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7652d57e-9eed-34c0-85e1-2f900f97a09b | -12.50003 | -45.29307 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7a8c1824-f058-3465-bd17-2f62bcfa43df | -11.02692 | -45.64331 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52d6a24-45a4-3744-b2a0-e8e674fbb64f | -11.45717 | -46.67827 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8815804c-9a14-3ca2-9850-6da7559cdab9 | -9.13633 | -50.90034 | 2026-08-11 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f11fb7af-c98d-3aa0-b91d-d4a1b265cd8c | -12.45906 | -45.31076 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10d447cb-dcf3-3b2c-9432-bc2f0cbda579 | -13.57159 | -46.28732 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e177801e-4dfc-3679-b955-8b3aa73a08c3 | -12.48164 | -45.31426 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd1b7c21-b3ed-3224-b3bc-bc2fca4a57a5 | -11.03057 | -45.64373 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98222715-2725-37bb-9f11-a91a94c64a80 | -10.42821 | -46.6697 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efd3d1fb-f2fc-345c-a3fd-690a471032cd | -12.11983 | -47.18769 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfc8384a-79c4-3c8e-a312-ef0ccfa7069a | -7.62125 | -42.74359 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65ad8fc1-d57f-30db-b953-e23656fa6ec4 | -8.94013 | -60.49841 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README14.md)
