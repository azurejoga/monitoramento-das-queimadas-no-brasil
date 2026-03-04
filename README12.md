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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45504604-f9c3-3317-b56c-8280f8d7b482 | 0.30797 | -60.44642 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f7f23a-397a-3d78-9e8d-aa1a6b9c0969 | 0.06019 | -60.99041 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f43a6c86-fcb8-3722-ae91-bd0b710c2dbb | 0.27832 | -60.62063 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fcc2cf84-9cdd-3b51-b583-8abd25721304 | 0.27306 | -60.62095 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba41f93d-2130-32aa-aa5b-9c8c86b09991 | 0.05219 | -60.97854 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8c6e0a25-0161-373a-95e7-427a30538fcb | 0.03949 | -60.97572 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a14f9768-d29a-342b-9c5a-6fafdce70256 | 0.457 | -60.39395 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29913c6e-c538-3c5b-9987-7dd5768c6d14 | 0.0402 | -60.98018 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 3b8840bc-881b-3525-b9dc-a647bdf9d1cf | 0.04687 | -60.98361 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 21a1776a-a249-3179-bc64-53cb0779bd0b | 0.30181 | -60.44739 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c42d2890-2360-3619-9919-820943576be3 | 0.05741 | -60.97279 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9b52f528-2cbc-3af4-8ff4-eed2c76a17a7 | 0.05289 | -60.98298 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f5062325-f8be-36cd-94c4-00524d215362 | 0.31412 | -60.4454 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4ee9beb-4f8e-36c1-b08f-c45c90ffc86f | -0.50807 | -64.60683 | 2026-03-04 06:14:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b85cafda-d164-34c5-a574-96738dd618cf | 0.45774 | -60.39871 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 437a5609-b5ed-3f42-8376-fc0072634fb4 | -0.50927 | -64.60844 | 2026-03-04 06:14:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 48d7089e-ea0b-384a-b985-b687e2812dc1 | 0.27841 | -60.61535 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31a37231-6597-3674-9574-1a31357faa5b | 0.2776 | -60.61592 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db9a2d53-ca56-37db-b45e-cfa665de6ed6 | 0.05424 | -60.99147 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66df2e8d-24aa-35eb-b13a-cf6d90bfe36e | 0.05357 | -60.98726 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d270d8d3-c6aa-3d5a-95c2-3ef40e615897 | 0.04617 | -60.97918 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 3a58c038-85cb-3847-9436-886802d1cbff | 0.4933 | -60.50411 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1391f0ee-99a8-32bd-928c-08819b7b4259 | 0.28368 | -60.61488 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2399d9e0-500e-3346-9b05-79a04de93088 | 0.49554 | -60.51804 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 168a9b3c-533a-3cc0-a6de-164bd4181f06 | 0.49406 | -60.5088 | 2026-03-04 06:14:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcc2d279-96aa-3100-8d6c-bb2230061b1f | 1.5047 | -59.9116 | 2026-03-04 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6e8b8764-815a-3861-b8b0-ea03057d2e4b | 1.5047 | -59.9116 | 2026-03-04 06:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2807e349-c7ab-3d48-8cf1-02b4bbbf912a | 0.49883 | -60.50288 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bf2aa44c-e6a1-3a70-a2c0-ae3aa9eac97e | 1.51111 | -59.91751 | 2026-03-04 07:11:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.0 |
| cff7353b-a209-36e6-8b3c-230e767e7df1 | 0.46357 | -60.3895 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 756a6d51-565b-3815-8005-92ff3fa373df | 1.35011 | -60.01662 | 2026-03-04 07:11:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a215aa1-3657-37a0-b100-0ae89913fb14 | 0.31373 | -60.44211 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a9f925ba-6e6f-3586-a7fd-2ca334714a42 | 1.1158 | -59.19281 | 2026-03-04 07:11:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b58db010-ade1-3905-aaba-a7af5b5440aa | 0.05553 | -60.98834 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7e0c9157-40b5-38a6-92d0-b4d786dc0ba9 | 1.50846 | -59.89991 | 2026-03-04 07:11:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2a6605d9-d405-348e-817f-ada95ad56038 | 0.27728 | -60.62115 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b30dc2c3-42a9-38af-97bf-fe6d980cedac | 0.04654 | -60.9897 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 49b0ac26-1fbc-3140-bc60-c9476be75add | 0.05415 | -60.97912 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 91e27e7b-001c-3d04-aca4-6cf33f264935 | 0.73298 | -59.90197 | 2026-03-04 07:11:00 | AQUA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 04a52ff5-211c-366d-9eb3-bf5ac541aae8 | 0.06314 | -60.97785 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bf588e97-40ac-37b7-92d0-b851e4c93f59 | 3.01859 | -60.65152 | 2026-03-04 07:11:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc035f55-5101-3ac7-9cff-55ae20514994 | 0.04517 | -60.9805 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 45eb49df-01b2-3cb2-bf31-607db331ff9f | 0.03582 | -60.98776 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74fcc51b-c56b-37ae-ba1a-47fbdcd5a48f | 1.11711 | -59.20151 | 2026-03-04 07:11:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3fb41662-89dd-34ca-a9d0-b41894baac20 | 1.50978 | -59.90868 | 2026-03-04 07:11:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7cf07562-f7b1-34c6-b5a9-72672dfb26f3 | 0.06176 | -60.96869 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 868f6928-b4aa-3be4-ac23-1a1532e770f8 | 2.95211 | -61.08037 | 2026-03-04 07:11:00 | AQUA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21b811e6-9bfd-3c4e-88bd-a0777783db4c | 0.0438 | -60.97132 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8a468869-fd07-32d1-9604-66353d6643f3 | 0.46491 | -60.3984 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cfe46b4a-716d-387f-81c7-cc1831d130ce | 2.22885 | -60.74895 | 2026-03-04 07:11:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b390592-b455-3487-8318-80dd007b0b1f | 1.51857 | -59.90735 | 2026-03-04 07:11:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0390ac27-0ad6-38f4-99e6-0067645a64a3 | 0.50019 | -60.51183 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6fb3e7da-0d56-3ea0-a564-b6ba07ba7c26 | 2.95357 | -61.09022 | 2026-03-04 07:11:00 | AQUA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3cc527a6-7949-3cc9-9d37-33d54debe19d | 0.28483 | -60.61087 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e009423-63d5-3323-8836-f1bf675d07b7 | 2.92589 | -60.46434 | 2026-03-04 07:11:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6a0c30c-1f1d-325f-a0d1-327ea5d84889 | 0.30623 | -60.45232 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df570ef1-18ce-3b09-8f27-7e2bae56157d | 2.92452 | -60.45507 | 2026-03-04 07:11:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 10b9a144-bbad-313a-9b39-0ba5427c5322 | 0.05278 | -60.97001 | 2026-03-04 07:11:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| fdbadb56-4204-3d72-bf81-83aff4a1f85b | 2.6719 | -60.4114 | 2026-03-04 14:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a68aebc6-e044-34d4-a199-55ffbe09ff65 | 0.0455 | -60.9799 | 2026-03-04 14:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 108.6 |
| af1b0913-2cfa-369a-8edb-c0bb2ee57047 | 0.0455 | -60.9988 | 2026-03-04 14:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 906127ca-03c4-3fcb-b407-32711992eb45 | 0.0455 | -60.9799 | 2026-03-04 14:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 128.0 |


