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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a25c24f-4675-3658-bc3a-82bdb97170ee | -4.9311 | -43.1857 | 2024-10-30 01:25:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 66503610-f5c8-3cd2-94dd-4c58c96e38e5 | -5.2306 | -47.9566 | 2024-10-30 01:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ac5dd43e-9bfa-35fc-9e16-2c724703dbae | -5.2308 | -47.9349 | 2024-10-30 01:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a5822f30-665f-39dd-aa31-1beda1ac29ac | -5.9788 | -45.3621 | 2024-10-30 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c2be91a4-48d8-3529-8c03-e9a4c02b58d9 | -6.8408 | -59.0519 | 2024-10-30 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 909e497e-fe44-3d2f-afba-c368e4b3632f | -6.8409 | -59.0326 | 2024-10-30 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 9f308c26-b573-32a7-9db4-bb9a746a3123 | -6.8592 | -59.0511 | 2024-10-30 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ec8ab8fe-8568-3445-a8c4-4fb22cd3ea0e | -6.8593 | -59.0318 | 2024-10-30 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5f449fb8-7af0-3f86-a2ad-871cf3be44ae | -10.3434 | -49.6536 | 2024-10-30 01:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c9351baf-053c-3f4a-a327-0468d58db57e | -10.6984 | -44.9186 | 2024-10-30 01:26:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 26d58bb8-d323-37e8-a5c6-5b18a1e2e6ba | -10.7171 | -44.9391 | 2024-10-30 01:26:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 771c6066-8a92-32a7-ac63-c0e3c33a6c93 | -10.7175 | -44.916 | 2024-10-30 01:26:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 12de46c2-0042-308f-9534-105ac78b86d9 | -12.899 | -45.0549 | 2024-10-30 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 31c78bd6-8acb-35ce-9ca6-06db23e7e889 | -18.2652 | -55.9766 | 2024-10-30 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 3b1c0f3f-334a-3dd3-ab40-63add7f9f945 | -19.6063 | -56.7108 | 2024-10-30 01:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| f6f3fe7c-9c9a-3c35-9586-d33a271a7e6b | -19.6264 | -56.7079 | 2024-10-30 01:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 91ca2896-1241-3104-8695-753b0ab396c8 | -23.9917 | -54.1329 | 2024-10-30 01:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 3cc3f042-7ccb-367a-af95-2027928d6f52 | -23.9923 | -54.1106 | 2024-10-30 01:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 147.4 |
| f539780a-72be-322c-9ece-5d853cc73cda | -2.3906 | -48.9337 | 2024-10-30 01:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 308b657b-76fe-3c22-b916-da35b64d26e2 | -2.833 | -49.2413 | 2024-10-30 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 321007b1-3d1f-39e7-8a73-4976adf794ac | -2.8331 | -49.22 | 2024-10-30 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 806b035e-7e17-3560-8382-5dbc312c74eb | -2.8515 | -49.2408 | 2024-10-30 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8c8a04bb-e9e0-3968-b0ac-b6f20270a917 | -3.0734 | -54.167 | 2024-10-30 01:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f3f50ee9-dc04-3349-9269-9b6321f8044a | -3.0913 | -54.287 | 2024-10-30 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2cd47abb-e490-3a93-807b-a5fa08badee9 | -3.0914 | -54.2669 | 2024-10-30 01:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 248e0966-f1ef-37e4-bb1f-30e43c78bab0 | -3.1028 | -51.1041 | 2024-10-30 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 901f7f19-94dc-3ea9-ae41-78e36c4487ae | -3.1097 | -54.2865 | 2024-10-30 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 61b4851b-4ac2-391a-a48e-cde84321327e | -3.1098 | -54.2665 | 2024-10-30 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 92122029-a08e-3640-a9ea-141fa1662780 | -3.1281 | -54.266 | 2024-10-30 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e6469e35-6d23-3202-9ebd-ac38b1eaac9a | -3.16 | -50.6231 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b2cee5b8-b04a-3ba9-a321-0952ff874db5 | -3.1601 | -50.6021 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f785aab3-7782-36bd-b4d0-875d4577fb7a | -3.1602 | -50.5812 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5d5827b7-a40b-31b4-89d4-7f4445422f49 | -3.1786 | -50.6016 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 4406e5c1-058f-3d2a-8e2f-0e9e961b5789 | -3.1787 | -50.5807 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2c44038c-9926-328f-899f-8468f9777c21 | -3.234 | -50.5999 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 7d4c27df-9f4a-3016-b021-43576639403c | -3.234 | -50.5789 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d62ec495-07d0-3cb1-b72f-1d584dfde117 | -3.2535 | -50.3479 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| fe567b22-6f34-3512-84f3-5f95bd2433a2 | -3.2719 | -50.3473 | 2024-10-30 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cf01f3c2-109f-3fe4-90a2-36823c5a6742 | -3.5631 | -47.3847 | 2024-10-30 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 358.0 |
| 6f291ea9-a49b-3b18-8de1-52cfb261c964 | -3.5632 | -47.3629 | 2024-10-30 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 219.3 |
| c60cd2a5-77c1-3b63-a565-45e87cf2e5bb | -3.5688 | -50.043 | 2024-10-30 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 6f2d6cd7-2561-30ce-9132-123d2f8cbf2b | -3.5689 | -50.0219 | 2024-10-30 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| c4a2b688-b839-3a61-8539-8ad4c010d499 | -3.5817 | -47.384 | 2024-10-30 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| a55507d1-030b-3a57-855b-1ddfdff2a247 | -3.5818 | -47.3621 | 2024-10-30 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 8af6c7b1-a14c-3712-90fe-b40574988630 | -3.8037 | -51.1644 | 2024-10-30 01:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0b9cef66-fa8e-3541-b4b5-d022e4551ccc | -3.9326 | -41.4957 | 2024-10-30 01:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| a6ef9bf3-b0e0-3c56-85af-66d92cf9733f | -3.8925 | -51.9061 | 2024-10-30 01:35:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6ce29254-c97f-318b-8591-785d2d43e637 | -3.9486 | -48.1291 | 2024-10-30 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2a947947-69c3-3b21-bcf8-aac2756094ed | -4.2748 | -43.4589 | 2024-10-30 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a7098a50-ca40-31d1-af2a-3269f5fc9d1a | -4.2563 | -43.4368 | 2024-10-30 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7edb57ed-68a3-3cd8-b3e7-154eeaebc091 | -4.2749 | -43.4357 | 2024-10-30 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c4e192dc-7178-3963-ae96-f8f6c12f0267 | -4.3473 | -43.779 | 2024-10-30 01:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e67efc32-9729-3f8e-a9c6-fe23f27ec76e | -4.2679 | -50.6879 | 2024-10-30 01:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 88d66084-a8c8-307f-9e8d-33c60c7a5c8c | -4.2681 | -50.6669 | 2024-10-30 01:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 2bf67d60-6adb-35ca-bf92-907e65c455fb | -4.4971 | -46.4618 | 2024-10-30 01:35:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 3a06f007-4f41-3b83-b857-7edb07c0096b | -4.4972 | -46.4396 | 2024-10-30 01:35:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9b7e5bb3-7313-33ae-b21d-30dcfbd015f2 | -4.5157 | -46.4608 | 2024-10-30 01:35:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a1d2e706-36cb-3ee4-b98c-cd054d902f07 | -5.2306 | -47.9566 | 2024-10-30 01:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 03582c01-1012-3865-b286-29da522974b7 | -5.2308 | -47.9349 | 2024-10-30 01:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 30d0cde4-261b-3fd7-9b00-af3d03dc1f53 | -5.9788 | -45.3621 | 2024-10-30 01:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 90886899-2115-3a84-aece-ab3189d670b3 | -6.8408 | -59.0519 | 2024-10-30 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7692627b-e568-39cc-80fa-2902c30379e6 | -6.8591 | -59.0705 | 2024-10-30 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f93e842d-d871-3a74-9720-038c9e4c2e47 | -6.8592 | -59.0511 | 2024-10-30 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3fc1cf12-075c-383d-8a47-591972dbd531 | -6.8593 | -59.0318 | 2024-10-30 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 375c11ea-dc81-3544-a913-e054c07edbdf | -7.8736 | -46.9065 | 2024-10-30 01:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5d8e22e8-cff2-3059-84ce-3cc8ef573f2c | -10.3434 | -49.6536 | 2024-10-30 01:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| e61dbcc0-ae76-3f59-951f-21d51017cb8e | -10.7175 | -44.916 | 2024-10-30 01:36:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| e5e3f751-e1d3-3959-a494-c3fc2c2c13cf | -18.2652 | -55.9766 | 2024-10-30 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 7525b1ca-1118-30ee-8c58-d4f459657c34 | -19.5662 | -56.7164 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| e8668341-151a-3a6d-aa7b-60c077d673fa | -19.5862 | -56.7136 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.2 |
| e3f6febf-3f54-3d37-9699-b2aa09ae9160 | -19.6063 | -56.7108 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.3 |
| a3002b8d-016f-37b2-923a-2d2e765d5595 | -19.6067 | -56.6898 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| e246642d-a6b6-3bf6-b7a2-20391b5df890 | -19.6264 | -56.7079 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 11845e97-49f5-3a87-aa98-5c35f0c6da19 | -19.6268 | -56.6869 | 2024-10-30 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| ccd6c308-7f7e-37fc-ae35-e2328d683448 | -23.9923 | -54.1106 | 2024-10-30 01:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| e30f5dc4-45b4-3e75-9e27-839cbc10a544 | -24.026199 | -54.133598 | 2024-10-30 01:42:33 | METOP-C | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a09c66c8-cc04-3dbc-952d-fa7507fd9e32 | -24.028999 | -54.144402 | 2024-10-30 01:42:33 | METOP-C | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 011a16af-9751-36ac-b1fe-cff77d946238 | -24.0056 | -54.093399 | 2024-10-30 01:42:33 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df244415-c757-3418-b55e-42af104158d5 | -24.0084 | -54.104198 | 2024-10-30 01:42:33 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2427425f-21f3-3eaf-a0aa-cba6e36c85d2 | -24.011101 | -54.115002 | 2024-10-30 01:42:33 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e23b30e0-b5f9-32b7-9ab2-3448aaf0ffbf | -21.583099 | -54.185001 | 2024-10-30 01:43:13 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 28e8219a-75ad-3448-a80f-855c27ebc9e9 | -21.586 | -54.196499 | 2024-10-30 01:43:13 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| adadf752-5ad3-33e9-a314-479ad098a909 | -19.6488 | -56.6763 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bc8270f0-db54-3297-a8c8-25028ef7e27f | -19.6196 | -56.6842 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0aaa1572-527b-3bf6-a5a7-8e22ef2d238a | -19.6217 | -56.693199 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d74f2d7a-819e-38ec-9359-ee20e86523be | -19.623899 | -56.702099 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 25814129-f2f3-3d26-9d69-61fa3c058b1d | -19.626101 | -56.710999 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6d7f5e27-aaf7-3f25-a80b-7d44d3e0db3e | -19.612 | -56.695801 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bca96edb-f981-3c83-b10f-1402eb16b051 | -19.614201 | -56.7047 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 13b4259c-2df7-34c0-97c9-95a243962fe4 | -19.600201 | -56.6894 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10e5d82c-a549-3432-9c36-2dcb984ef82e | -19.602301 | -56.698399 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18f32746-4e75-3d24-a17d-34c3760046b4 | -19.6045 | -56.707298 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52d7a2b7-3758-3447-b495-15eb69ee34cf | -19.606701 | -56.716202 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cfa5e201-50da-3016-b64f-5cd2f094d3a3 | -19.6509 | -56.685299 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d8f07b64-5feb-365b-8d40-060d65d36e3a | -19.639099 | -56.678902 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 700fb143-01b9-3659-8d4c-e9dbe4afab3a | -19.641199 | -56.687901 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2fab64b1-1e23-3015-9af2-da0feeefd58b | -19.6434 | -56.6968 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bb09048d-a07e-37f3-b735-2f8a72c937cd | -19.645599 | -56.705799 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 01276679-4e42-3d95-894f-4e91d5b27e42 | -19.6294 | -56.681499 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2fcd2650-8627-36e6-bfc6-58439ecb3445 | -19.6315 | -56.690498 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README21.md)
