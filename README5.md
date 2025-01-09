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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 972d46cf-14d6-34b4-a7b8-c7e150198990 | -19.30013 | -53.73986 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 450d0c56-e73a-3958-9819-768b4e993ec7 | -19.30075 | -53.73609 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8ec7d28f-ce3f-3f82-9447-c94ff395a486 | -19.29616 | -53.74299 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e625212e-60a3-3bb2-ba9d-7fc82c183c06 | -19.30287 | -53.74426 | 2025-01-09 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a6ebe840-6136-3dba-83ff-a7d46e5ac046 | -21.19415 | -44.93563 | 2025-01-09 04:40:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42bd68e1-2823-3bdb-84b6-d79b7f92a631 | -19.83854 | -53.92148 | 2025-01-09 04:40:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb015358-9d78-35e8-b49f-877ffe48637d | -26.87329 | -52.33786 | 2025-01-09 04:42:00 | NOAA-20 | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd659421-7121-3d2c-a920-99a44bbc89b9 | -22.01767 | -49.11837 | 2025-01-09 04:42:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5057c094-7f4a-3489-94c6-0db238115f54 | -20.55882 | -54.65629 | 2025-01-09 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b2ddf75-9bdc-3f02-af0d-0c98069e2cb3 | -20.05144 | -57.19804 | 2025-01-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 623922fa-f9ee-3ac5-b899-ea2633eb0966 | -21.1999 | -56.91854 | 2025-01-09 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba0ed5b3-0fef-3486-b080-b43961affce8 | -22.25309 | -50.03878 | 2025-01-09 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b7daa64-65da-3ee8-a769-c66ba80d8ee6 | -23.17215 | -50.66005 | 2025-01-09 04:42:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6b05a3dc-d16e-3131-b242-9ecea9e632fa | -23.28101 | -51.11847 | 2025-01-09 04:42:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 367cd7e7-dd58-30d6-898d-5468c6457187 | -22.01905 | -49.11621 | 2025-01-09 04:42:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f578263b-5956-3ac2-afb2-8c12e7c32c29 | -21.88372 | -56.11375 | 2025-01-09 04:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f759e216-6b62-3135-b77d-6a05f4c73ff3 | -21.10759 | -51.20229 | 2025-01-09 04:42:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 015389c4-7fac-34d9-9206-31b54fcd17d5 | -20.57896 | -55.57468 | 2025-01-09 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d91550-6961-3620-8814-166fe71d68b9 | -20.57545 | -55.57397 | 2025-01-09 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db6857e1-880e-3d97-bd33-b2a8e77fe33d | -22.53949 | -48.81167 | 2025-01-09 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f79f24c-c13b-3757-90ff-318d460cd20b | -23.32828 | -50.12562 | 2025-01-09 04:42:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8eee6b11-da3b-3095-ae43-d40cea325c36 | -22.8464 | -49.38295 | 2025-01-09 04:42:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54318a1b-6f47-3fef-9e43-db5fc00af1fb | -27.04281 | -50.94722 | 2025-01-09 04:42:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30fc448d-fd31-35d0-8669-37ae1a7652ca | -29.14141 | -54.85788 | 2025-01-09 04:44:00 | NOAA-20 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 8c6e4581-9f46-32f6-84d6-75cb08f5a1aa | -30.52674 | -53.964 | 2025-01-09 04:44:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| d32b3512-6fcd-3eec-b06c-39adb0c44786 | -30.10427 | -51.61778 | 2025-01-09 04:44:00 | NOAA-20 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9a8c9eff-fd01-38fa-86c4-86fd34736e48 | -30.46605 | -56.391 | 2025-01-09 04:44:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e2f748d3-1a06-3e6a-87bc-2751b16fbc9a | -30.52734 | -53.9599 | 2025-01-09 04:44:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| f3219981-472b-3f2e-94fb-61a3e4392075 | -29.49724 | -51.98371 | 2025-01-09 04:44:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9bdc4246-cdbc-368b-8a78-d5986813439e | -30.555 | -52.88248 | 2025-01-09 04:44:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| f04ee4e1-3b07-321d-b386-13285675ad18 | -30.52568 | -53.96523 | 2025-01-09 04:44:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 520cbfce-ef3a-3860-9c9e-2fbe73cb12e3 | -29.80948 | -51.22607 | 2025-01-09 04:44:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 2efb0155-814c-361d-bbdd-4e166e003672 | -30.52628 | -53.96114 | 2025-01-09 04:44:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 52bb36ba-44e5-30b6-ac46-a89b4737c93e | -19.3052 | -53.7443 | 2025-01-09 04:50:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2544b4e1-2b57-3810-b353-c048ca2eda5c | -7.56945 | -39.00297 | 2025-01-09 04:59:00 | AQUA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 74ab483f-ee94-3b37-b203-beccadb7f478 | -7.56813 | -39.0118 | 2025-01-09 04:59:00 | AQUA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8e1d7db9-ec8e-3b2b-8da7-f2cbae9045b4 | -19.3052 | -53.7443 | 2025-01-09 05:00:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3ed73633-2152-382e-b984-a72003f7f44e | -19.3052 | -53.7443 | 2025-01-09 05:10:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5b4c1378-9ee3-32f2-8104-6e1ca6862a7d | -19.3052 | -53.7443 | 2025-01-09 05:20:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 805fabc1-16af-3d9b-9fb1-1730cd567c48 | 1.94135 | -60.86891 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c0803f-567d-3e73-9aab-39b604fb1705 | 3.42896 | -60.54525 | 2025-01-09 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5677485-07dc-340b-906a-a22a55c40ebb | 4.18364 | -60.51888 | 2025-01-09 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 685127be-bade-3544-a79e-9e22df337de9 | -1.33294 | -53.22113 | 2025-01-09 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 098b053f-7d13-3d75-b60b-4a0cc0d75f31 | 1.94581 | -60.85413 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572cf8cf-5f84-364c-86a1-54d4131fcb2b | 0.74893 | -60.20602 | 2025-01-09 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a8ce7cb-7919-34d1-95b9-72f9bc473819 | -1.33605 | -53.21817 | 2025-01-09 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ebada96e-72cb-3d9b-8560-ea1d65833559 | 1.94519 | -60.87185 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 982e8e28-2cc1-38b3-beb2-d86fa5db77ad | -1.33379 | -53.2157 | 2025-01-09 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eee26b14-1705-3902-91c4-a83aecf3c71c | 4.19355 | -60.51727 | 2025-01-09 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 285d8734-8d8a-3d0a-9cb4-00ac5461edc9 | 2.97496 | -60.51376 | 2025-01-09 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3cf9173-d044-3467-bdce-843f635c17cb | 4.18866 | -60.63879 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d452d5e3-5e60-3acd-ab28-98a8c696226b | 2.92118 | -61.11033 | 2025-01-09 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eefa8997-6910-3abe-a879-2dc2a6066473 | 4.05301 | -61.17021 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1988b90-c267-3e79-bc2f-61e2d3ff98d2 | 0.79647 | -60.5319 | 2025-01-09 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab642c9e-e138-3ebe-ab93-f88a229274b0 | 4.17281 | -60.47089 | 2025-01-09 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 044b5c07-b03f-30be-bc27-66d47d993bff | 2.56409 | -60.69404 | 2025-01-09 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aab000e2-3d73-30dd-a046-a88d51f42f69 | 2.57016 | -60.68958 | 2025-01-09 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23e6f041-debe-3b48-b85b-7ea025557b3a | 4.05355 | -61.17376 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d672cde4-4adb-3b01-a335-809a9d6fdb6d | 3.53533 | -60.48584 | 2025-01-09 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f62d1fdd-f7ce-3e51-9e6b-5411d940e1bf | 2.92559 | -61.11682 | 2025-01-09 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42b5a909-580a-3a63-b10e-353299ac209b | 0.74947 | -60.20945 | 2025-01-09 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0da077e-fdc4-341d-bba1-242766cee237 | 1.34468 | -60.03173 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42823630-8aaf-340c-9728-17df8e4a8a8b | 0.75223 | -60.20551 | 2025-01-09 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df057516-163f-34e6-973d-62916c61d713 | 1.34522 | -60.03517 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef81ff9f-c894-36f9-950f-ed7324065605 | 3.52898 | -61.36752 | 2025-01-09 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd6f58e5-0944-3e34-bf94-c1a252a0a674 | 3.53587 | -60.48929 | 2025-01-09 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89efb5bb-d575-3560-9d15-a91f3fb6445c | 4.1941 | -60.52076 | 2025-01-09 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9715b8ed-1efd-3dbb-b2f5-918aae9a8c85 | 4.13599 | -61.00203 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb58abc5-5b6f-3d9d-bbfd-1bd030bd35ef | 4.13211 | -60.99901 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8345a56-8cb3-3d55-81dd-26545e23f857 | 4.12598 | -61.00357 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfe4cfff-19d2-32ec-80c0-41cefd933a57 | 0.75277 | -60.20894 | 2025-01-09 05:29:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33d6895-590a-30ef-a29d-bf369be90c4e | 0.80691 | -60.27436 | 2025-01-09 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e3b62ea-5abc-36a0-b97e-e395dce307cc | 2.92505 | -61.11332 | 2025-01-09 05:29:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b9fc73-abf0-3e05-83e4-ae8b32f56025 | 2.56686 | -60.69008 | 2025-01-09 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef0d8dd0-dd32-3050-b42b-9d1779f1d2ee | 1.94189 | -60.87236 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0cd435a-dbd1-35b1-b42b-0c3efcd85a2b | -1.33463 | -53.21026 | 2025-01-09 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd7a8c21-2aff-385d-a732-48397fc31262 | 3.70336 | -60.07987 | 2025-01-09 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28b6cffa-3fb4-3f6b-aecf-0fe59c7a0867 | 3.18486 | -60.46308 | 2025-01-09 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ed06cf6-d13f-3c31-bcc3-9649237dcbab | 1.94465 | -60.8684 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d666cfa-72b7-33cd-9f0c-d4b259b57035 | 1.30507 | -60.4104 | 2025-01-09 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7415dfa7-8897-37a0-a35c-78aaa9836344 | 4.13675 | -60.61195 | 2025-01-09 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed3d68f8-92fa-3f1d-bde5-5cab4230eaf0 | -1.28776 | -53.08958 | 2025-01-09 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26353122-974b-3c6c-9458-38e2f8670b46 | -19.3052 | -53.7443 | 2025-01-09 05:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 49cf4b4a-141e-3568-a6a1-fa8661ebe3bc | -19.29867 | -53.73892 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 87a91894-e095-35ea-8338-49287ecf742e | -19.3065 | -53.74403 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c0607ed9-9b85-3ac7-a33e-284df89cb64b | -19.30515 | -53.73478 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 76f9dab2-3249-340a-88b9-7eb77879fcf4 | -19.29824 | -53.7435 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e213373c-05a5-335f-86d7-9d46a98086c0 | -19.3069 | -53.73947 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4f4df48-1a8c-3f47-b39b-0bdeed3b7419 | -19.2991 | -53.73436 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 20456df0-36c0-3d74-8e5a-e34f49fcee65 | -19.30429 | -53.74386 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3005d6b4-5479-3f65-9f81-735cccbcf381 | -19.30473 | -53.73931 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6e5ea993-b956-3093-9a26-3e119b2cff55 | -19.3073 | -53.73492 | 2025-01-09 05:33:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 364fb117-71bd-39b1-8eb1-44eb4e56e58a | -18.76093 | -55.96084 | 2025-01-09 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a2a33dd7-4c15-30b3-ace0-c619f1b7f2fa | -30.53134 | -53.96433 | 2025-01-09 05:35:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 34fcaf9b-2b3b-3aa1-bcd8-db4830eef471 | -30.52677 | -53.96007 | 2025-01-09 05:35:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 1767a177-6986-3564-8159-efd3d98b86de | -30.52649 | -53.96588 | 2025-01-09 05:35:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| c57a12a4-724a-36d3-9a14-6cd8b195bc95 | -30.52471 | -53.96455 | 2025-01-09 05:35:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| af62cae2-0739-3833-b445-071bb9504e78 | -30.52496 | -53.95885 | 2025-01-09 05:35:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| f65f3092-7640-358b-8136-78a7aa9f0e22 | 2.56605 | -60.69529 | 2025-01-09 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5685df2-4ecd-3063-b135-ed56290eef0e | 4.09362 | -60.61583 | 2025-01-09 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README6.md)
