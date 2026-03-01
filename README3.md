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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f420c14d-d929-3669-a9bf-2e96f629f1b3 | -23.27298 | -55.34447 | 2026-03-01 03:55:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b97ce153-99d9-3724-b69b-0c3eda909ffe | -24.06594 | -49.77891 | 2026-03-01 03:55:00 | NOAA-21 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a510c1d-c718-3083-aac9-51081f5d8056 | -23.28311 | -55.33323 | 2026-03-01 03:55:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ade9eafa-eeaf-369c-a980-0c923b5dc800 | -23.27963 | -55.34667 | 2026-03-01 03:55:00 | NOAA-21 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 02123503-1138-3aea-a8ed-cd241fa7bbcb | -31.46406 | -53.66822 | 2026-03-01 03:57:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 469872bc-fd14-37c1-bc6e-c4a4c72fbcbc | -31.45895 | -53.66642 | 2026-03-01 03:57:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f155f855-9385-30c1-ad1a-371bf875ff41 | 1.5046 | -59.9306 | 2026-03-01 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 11ba3fb5-6262-3f78-bbfd-555372a16e44 | 1.4681 | -59.9309 | 2026-03-01 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ebc0c8c6-7804-3001-8bbe-6f99c6ec0621 | 1.4864 | -59.9308 | 2026-03-01 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 96f93aae-3387-36a3-9475-2442a60c2923 | 1.4864 | -59.9117 | 2026-03-01 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.9 |
| f1e92f79-3d4f-3eb6-a850-324b35c0ef8b | 1.5047 | -59.9116 | 2026-03-01 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.6 |
| f9e47811-8517-33a8-aee0-242504e1e29c | 1.4864 | -59.9117 | 2026-03-01 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 140.7 |
| dbb83e25-9f39-3f6b-a1ac-5cc473fd8949 | 1.5047 | -59.9116 | 2026-03-01 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 4b563203-1fb7-3244-916b-6a59a5735947 | 1.4681 | -59.9309 | 2026-03-01 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 62be2cb9-a09d-3896-ba7a-c3ec8c17a4c3 | 1.4864 | -59.9308 | 2026-03-01 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.6 |
| bc4b3ac0-3afa-3ce7-b481-56c5748d80c1 | 1.5046 | -59.9306 | 2026-03-01 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 356ff37b-4c01-3704-a4b7-14a69b3119d9 | 1.4681 | -59.9309 | 2026-03-01 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ebcc604e-0e55-3600-8cc4-a0e7cbcb1652 | 1.5047 | -59.9116 | 2026-03-01 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 2c743d51-8d7e-37a6-851e-4a4a4f63f6d0 | 1.5046 | -59.9306 | 2026-03-01 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 42455993-372f-3143-906f-374f9c3759e4 | 1.4864 | -59.9117 | 2026-03-01 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 03a7d7c1-5e3c-31e9-a10f-4747468db7b9 | 1.4864 | -59.9308 | 2026-03-01 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 85978fbc-2be6-3199-8656-0395ef279bae | -21.70697 | -56.31607 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4743b2d6-dea1-3e65-8565-cc0a36677b9e | -21.69147 | -56.3119 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81d70ea4-7371-3eed-80a6-1d6f21851e44 | -21.7018 | -56.31472 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0176a2fd-4cc3-332d-add8-9c3040b996a8 | -18.81038 | -57.63592 | 2026-03-01 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a6890877-7fe0-34b2-8b99-d1056a831267 | -21.69298 | -56.305 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 374856dc-f657-3787-8107-6358e8e7dc84 | -21.71291 | -56.31394 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3d0763e-e6ce-377f-a901-3ccb75bc8b2f | -21.71064 | -56.32438 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 512db8da-169f-31a9-8342-4ac5d435e035 | -21.68552 | -56.31404 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba81536-760e-3b8b-aa51-b79dd08abd65 | -21.4141 | -48.73333 | 2026-03-01 04:23:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a04e0f0-3e4d-3796-93f8-7ea939e9447f | -21.71729 | -56.31894 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2d0a727-ee93-37c9-b8b6-2ce22203ec14 | -21.68628 | -56.3106 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d79a4b52-5b9c-3951-9a59-5f0e5ea05726 | -21.70848 | -56.30917 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d8548a9-0808-3d30-83d2-f390c2d2bfbb | -21.71142 | -56.3208 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fce9333-4011-3e9b-aa4e-ca5da9a31fd6 | -21.69816 | -56.30634 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 439bb23a-7800-317a-a6a6-0a4d499d5fba | -21.69222 | -56.30844 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4857aee4-e50b-3042-98aa-28c9a8bca7ef | -21.68919 | -56.32228 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3763fe-73d4-3710-b229-99a9e1e600ba | -21.68995 | -56.31883 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc9e0d41-5fd8-3e46-bdfc-dbf06bcc3204 | -21.70621 | -56.3196 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 034833f0-6c30-3892-97a1-70d22485c2c6 | -21.71217 | -56.31736 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffca0f97-ca19-3e9a-af7d-7dc93552320b | -21.41821 | -48.73005 | 2026-03-01 04:23:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7fd92b4-5bde-3761-b400-aae51bd52f20 | -21.68844 | -56.32572 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66f621c4-9d28-314c-b5e0-ed813a515866 | -21.68324 | -56.32442 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d870d42-9b7c-3020-872d-b86a010c110a | -21.6907 | -56.31537 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64eb533f-5664-3a97-b07f-bb98e4647e10 | -21.3204 | -48.5369 | 2026-03-01 04:23:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32a80bf2-8475-384c-bb53-518f04792fb5 | -21.6989 | -56.30295 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95ae618e-d7bd-3e20-b818-12f117502fa1 | -21.6974 | -56.3098 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c56769c7-508c-3b70-a3b4-64acfcdaa8b4 | -21.70773 | -56.31259 | 2026-03-01 04:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c50a998-4e8a-3201-80f1-537bae9b44ad | -21.41753 | -48.73403 | 2026-03-01 04:23:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfbc53d6-98b0-3379-b3a0-0969fad4f480 | -18.97862 | -52.93226 | 2026-03-01 04:25:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d2ffbb6-46f2-37a5-bf53-ed17bd6aadca | -23.4652 | -52.80821 | 2026-03-01 04:25:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cdead873-fda3-3fc0-8ccf-44631befe983 | -24.06844 | -49.78014 | 2026-03-01 04:25:00 | NPP-375D | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24625a83-1079-3016-9a83-3217d5ef3c67 | -23.28103 | -55.34978 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69b7d72c-d32d-38a2-a70d-c179d9455435 | -23.46531 | -52.80998 | 2026-03-01 04:25:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5011620-df6e-3c35-ab2d-2fd3ce870d76 | -23.46606 | -52.80609 | 2026-03-01 04:25:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf453b46-97e9-378c-a000-f9e52a5a0d08 | -23.27631 | -55.3485 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2003ee0d-4758-39a2-a9cd-e12ce6e76f94 | -23.28456 | -55.33231 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5e677f1f-ece9-39b5-9725-ccfa24d1d4a7 | -23.28218 | -55.34429 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6317f8f-d885-35e5-9434-5f32293a8441 | -23.27273 | -55.34091 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cbb6d1d6-6f39-38f7-aef1-3bb5da9ce8f4 | -18.9742 | -52.93124 | 2026-03-01 04:25:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da80ce15-1b3d-36d7-b77d-72c111601f1c | -18.95677 | -45.3805 | 2026-03-01 04:25:00 | NPP-375D | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95ac097a-cce1-3d0b-934d-c5a1768d0996 | -23.28098 | -55.34892 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4625a0f9-3bbe-3672-b696-9587f4917084 | -18.80752 | -51.61338 | 2026-03-01 04:25:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aa3de79-3e9c-39a9-a150-407de92f4e58 | -23.28449 | -55.33314 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 95b30893-97a0-3caa-b683-40e472e03c9d | -28.41939 | -49.20335 | 2026-03-01 04:25:00 | NPP-375D | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8902a116-fffa-34c4-a823-4fc3c921334a | -23.28217 | -55.34343 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 66067fdc-7715-3796-b7fc-afdf438154c2 | -18.97662 | -52.93246 | 2026-03-01 04:25:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d50c5d90-9c13-366d-b16a-7bc718a4293c | -23.27159 | -55.34724 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46775139-b9c0-388a-9bdb-c8196b724e97 | -28.41874 | -49.20733 | 2026-03-01 04:25:00 | NPP-375D | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2056adf1-dd82-3e6b-a392-072b8587a08c | -23.27626 | -55.34766 | 2026-03-01 04:25:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ba55ca8-a0b9-3339-8047-5a00fd0a4ddf | -31.46287 | -53.6672 | 2026-03-01 04:27:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 154baad5-f654-3ecf-a165-82da90651c44 | -31.45917 | -53.66619 | 2026-03-01 04:27:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 499c2a4a-f9ba-3b55-ac89-3914bdf979c6 | 1.4864 | -59.9117 | 2026-03-01 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.7 |
| f9f73fab-5e93-3fc7-a59a-9ae92075e11f | 1.4681 | -59.9309 | 2026-03-01 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e088847d-427a-3313-9fcf-ea19e7532971 | 1.5046 | -59.9306 | 2026-03-01 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.3 |
| aa780ed5-120d-3932-997e-08d27c82a0b0 | 1.5047 | -59.9116 | 2026-03-01 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 91f0b6c0-266a-35ed-a69e-85817afe3377 | 1.4864 | -59.9308 | 2026-03-01 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.0 |
| e948fc94-04ca-31a9-bdca-7f51ce3c1218 | 3.45192 | -60.80962 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 73239874-4075-33f2-a95a-400b30453525 | 3.45003 | -60.79621 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a420343-0266-33d8-88a3-9a7cfd51a826 | 2.90942 | -60.42991 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2196c590-5da8-3571-816c-c6dea41ee990 | 3.45172 | -60.79763 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f04a9ddd-d69a-32e3-9af4-c8bdf1fd499c | 3.45271 | -60.80431 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cc6c6dd9-65cb-3f67-8aa3-f900259b5fcd | 3.32288 | -59.89903 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fa9c410-a36f-30ce-8d03-cc28f696da73 | 3.4477 | -60.81882 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d27b7f5-6af3-3e94-9675-c2452667234a | 2.91037 | -60.4361 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1a2b9f93-fbd7-348a-a939-5463f9da2749 | 3.45799 | -60.80198 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44f1f17c-8eae-32cd-8032-da299daa800c | 3.15559 | -59.92751 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 43094d3c-c328-3e11-8910-f858ec191514 | 3.168 | -59.91978 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7ee35c67-60eb-315f-94e8-46b20c2eed7c | 3.16137 | -59.92077 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8918d6a7-9628-36e4-9bb9-fe408e65424b | 3.4449 | -60.81058 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5509745-ea6e-33b5-b1b8-5d55114136ac | 3.16054 | -59.91505 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a75650ab-12b7-3dd3-8786-45701ecaa043 | 3.31876 | -59.90207 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc915481-0cd8-3995-a444-4dfd4197b03a | 3.48576 | -60.78604 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6cdd70d9-4c44-3bc6-a9f6-5d506671b96b | 3.45571 | -60.8246 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed73bc28-cff0-37d7-ae29-e43010032d16 | 3.32206 | -59.89326 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 040b3f0c-7068-3c44-8999-5b82a2811e01 | 2.52327 | -60.81371 | 2026-03-01 04:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4aa2c4e1-74e3-3b4b-afb0-b194373e2236 | 2.91176 | -60.4356 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a10b8c5-4db7-37f5-be13-140a70156a0a | 3.45371 | -60.81108 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a7611b60-9c13-37e0-b25c-f8a9278c8a16 | 3.45472 | -60.81786 | 2026-03-01 04:38:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fac5e515-c32b-3b45-a683-1e6a1e493dd9 | 3.32452 | -59.89532 | 2026-03-01 04:38:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
