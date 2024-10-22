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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7eaa58d-45d1-356d-ba12-c13a85de2ea7 | -6.26699 | -39.45238 | 2024-10-22 00:07:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7be6c744-ef9a-3634-a5c1-1128733be9f0 | -5.54199 | -35.58067 | 2024-10-22 00:07:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 12edfd48-1b8c-32d5-a21c-d5ebe93702ae | -5.48676 | -39.12255 | 2024-10-22 00:07:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7e83696a-ffc2-3697-9c6f-2b631dedefa2 | -5.24445 | -35.56027 | 2024-10-22 00:07:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e28527c8-2f22-3632-902a-51267bc071ce | -5.2432 | -35.55137 | 2024-10-22 00:07:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d74e8d92-796a-3531-8868-2b9d9a5306cc | -5.23464 | -43.18821 | 2024-10-22 00:07:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 8c3f5599-07b4-377c-a79c-f3f0abd8919b | -5.23164 | -43.16591 | 2024-10-22 00:07:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 30a5f53d-6bc2-3d3d-ba0f-28e99c934384 | -5.23163 | -43.20493 | 2024-10-22 00:07:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| b2231532-743f-3738-9e68-b265e6c9f72b | -6.26538 | -39.4404 | 2024-10-22 00:07:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 22dbb6f7-06d1-3c67-a007-df055a894d9b | -5.22876 | -43.18224 | 2024-10-22 00:07:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 9ce607ae-b621-3dfb-b3fb-c1bf8f4c8c9e | -4.93782 | -43.02197 | 2024-10-22 00:07:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b2c534c4-84dd-3ed4-98dc-daa8efc92801 | -4.93378 | -43.01728 | 2024-10-22 00:07:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ef19a7e0-ddb4-3f62-881e-ff181f3760d8 | -4.61623 | -42.38037 | 2024-10-22 00:07:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 629c711d-b172-39ea-88d1-c6ea20126135 | -4.54886 | -43.57761 | 2024-10-22 00:07:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a5985aff-b20d-3532-b1a0-f4d1b852b11e | -4.46655 | -42.92159 | 2024-10-22 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c398f7d9-116e-3bd1-9b96-bc72c9932eba | -4.464 | -42.91559 | 2024-10-22 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a21a314b-ab82-3a7b-a7cc-fbdb0f43421f | -4.46378 | -42.90131 | 2024-10-22 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e54898f7-c6e0-3d79-8f68-dbd4b91b768c | -22.8552 | -43.7243 | 2024-10-22 00:12:17 | METOP-B | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3521f4dc-e1e4-31db-8da9-78e832af0070 | -20.194401 | -40.240002 | 2024-10-22 00:12:48 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8687d33-74f9-3184-81e5-2ccd1af98081 | -20.195999 | -40.247398 | 2024-10-22 00:12:48 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbe16ce4-8a22-3a75-8e66-b2c5a184cbca | -20.184601 | -40.242401 | 2024-10-22 00:12:48 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9733a5cd-4baf-32e4-9f09-615e11b71d1b | -13.3332 | -40.466099 | 2024-10-22 00:14:40 | METOP-B | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f7cd645-ccbb-3393-88a0-cdc61703f0d6 | -13.335 | -40.473701 | 2024-10-22 00:14:40 | METOP-B | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c2f5c48-deb2-3a8e-9900-31da10364e3d | -12.4848 | -39.0014 | 2024-10-22 00:14:48 | METOP-B | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4bae915-1d52-3945-94f5-0ec0d822cfd5 | -1.165 | -53.6571 | 2024-10-22 00:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ca15366e-7f27-334d-866a-9d305110d71a | -1.1834 | -53.6569 | 2024-10-22 00:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| e80dcceb-f7de-3baf-86fb-1b6add5266e3 | -10.2498 | -36.636002 | 2024-10-22 00:15:15 | METOP-B | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0dd2254-2b00-3a08-812c-99b590fd3cc3 | -10.2531 | -36.6493 | 2024-10-22 00:15:15 | METOP-B | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8e594d1-4f92-357b-91b1-0f14a8242227 | -10.2368 | -36.625301 | 2024-10-22 00:15:15 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f38b5db2-b07e-36e3-a0e5-0a79ecb463c3 | -10.2401 | -36.6385 | 2024-10-22 00:15:15 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 010347b3-55f0-3716-a48a-587f3eb104d3 | -10.2434 | -36.651798 | 2024-10-22 00:15:15 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bc0c371-7656-3598-bec0-024d45abe8ca | -10.2304 | -36.6409 | 2024-10-22 00:15:15 | METOP-B | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3cb58b3-fa3f-38a6-8e0f-60094cc3edb9 | -10.2401 | -36.6805 | 2024-10-22 00:15:15 | METOP-B | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eef78369-cbb6-3541-9cca-743e63a94757 | -1.9849 | -48.6865 | 2024-10-22 00:15:17 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ddeb042d-71b9-355d-b21c-b88bebecbccb | -2.4824 | -49.1233 | 2024-10-22 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| e603ad81-bfda-30b1-93c5-640576ab23be | -2.4824 | -49.102 | 2024-10-22 00:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| fe185fa0-0975-3e78-817f-dff32089a71f | -2.5123 | -45.8773 | 2024-10-22 00:15:20 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f8de771c-ada1-323a-ae64-26260da7c6c4 | -2.7867 | -58.1492 | 2024-10-22 00:15:22 | GOES-16 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 78a8d417-694d-3158-81a0-ada45f16b780 | -2.8482 | -45.4637 | 2024-10-22 00:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7bb3dcbc-3274-3df7-a1b8-eb4e0bdfee47 | -2.8668 | -45.4631 | 2024-10-22 00:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| bd031184-b8cb-32e2-85e4-bccc5647d9df | -2.8703 | -54.4725 | 2024-10-22 00:15:22 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 75b8f9fd-f299-36a2-965f-f5ad23d5ab13 | -3.0581 | -53.2395 | 2024-10-22 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 30a4f455-96d0-31a1-bdd0-3ce14334b8da | -3.0654 | -51.2506 | 2024-10-22 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1618f0f7-997e-3ac8-ab49-9660c73dcade | -3.0765 | -53.2593 | 2024-10-22 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9bf19387-7b9a-3d8b-a60c-59ec7754944c | -3.0765 | -53.239 | 2024-10-22 00:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d2dcdd46-7971-3246-a91b-8d9be6f40c9a | -3.0837 | -51.2708 | 2024-10-22 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7768ccc3-cded-36db-937e-fdff8430508b | -3.0838 | -51.25 | 2024-10-22 00:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 4fd01697-2c8d-3098-acc1-376a5d09486e | -3.0917 | -54.1867 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 241737ef-8c40-34aa-9aef-fb970526dc97 | -3.0917 | -54.1666 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 19f538ca-8ca5-3936-9a72-e71ee90c5c18 | -3.0918 | -54.1465 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 825a0530-11cc-3aa7-a3aa-fdcd553699ce | -3.11 | -54.1862 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f7730656-1db1-3e95-9c0c-00a319a3a48e | -3.1101 | -54.1661 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 8df12371-9a84-35e2-84c5-ddd1f3abe10b | -3.1102 | -54.146 | 2024-10-22 00:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 79f5a97c-5e0d-3ee4-9a61-bd3f13f2aa78 | -3.4392 | -54.6382 | 2024-10-22 00:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 37137678-821d-3e56-9ac0-2d601df62b55 | -3.9977 | -46.0202 | 2024-10-22 00:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 642979c2-af79-303c-8cc5-5d53d417b763 | -4.0161 | -46.0416 | 2024-10-22 00:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4d36bc4a-d68a-3ef4-b2f7-0e66a4500ce7 | -4.0163 | -46.0193 | 2024-10-22 00:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 2a20675d-2356-3db4-8891-78a901861d9f | -4.1085 | -46.1484 | 2024-10-22 00:15:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fc33bf8e-4d5c-3cdb-85ca-9e21f2919058 | -4.4655 | -42.9112 | 2024-10-22 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0d0f7052-feec-31fe-a791-b1bce44d33f6 | -4.4657 | -42.8877 | 2024-10-22 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 72131fa3-bfc5-3cab-8d00-6dd84482d55c | -4.5572 | -45.8128 | 2024-10-22 00:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 510b75f2-af99-31d1-88eb-9eedd16c24bb | -4.5574 | -45.7905 | 2024-10-22 00:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 401f16df-4556-3f38-8069-aee1491f69c2 | -4.9513 | -45.4309 | 2024-10-22 00:15:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| f30d044f-2880-3c55-bccf-c316066f582d | -4.9514 | -45.4084 | 2024-10-22 00:15:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 691cb80e-a8be-39ea-bc0e-81351776fae2 | -5.1514 | -46.0911 | 2024-10-22 00:15:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 83f23854-fa65-3b23-a247-4aed9dfebe24 | -5.2305 | -43.1886 | 2024-10-22 00:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 42226f31-3bfe-3aad-ab63-560847932b8c | -5.5718 | -44.87 | 2024-10-22 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 237ba92e-0785-3377-aded-8bc0da04091d | -5.5903 | -44.8914 | 2024-10-22 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0883f677-bd20-3151-bb56-332f351eb1c0 | -5.5905 | -44.8687 | 2024-10-22 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8a614e22-f203-3e57-8809-5b277b3cad53 | -5.9034 | -45.4353 | 2024-10-22 00:15:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d9965996-8685-3b8f-87fe-8150c0c1da0f | -5.9036 | -45.4127 | 2024-10-22 00:15:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6ce10f1b-0d2c-3309-a481-9819b172256e | -6.2334 | -44.1565 | 2024-10-22 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 798ae3d8-97de-306b-85ad-8de90e52b758 | -6.2336 | -44.1335 | 2024-10-22 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 604aa046-eea2-397d-bf68-9e4ac3da9c9f | -6.2522 | -44.155 | 2024-10-22 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9f893cc8-6261-398b-aa20-7254f00e77aa | -6.2524 | -44.132 | 2024-10-22 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3dc5e5e3-7f57-3196-8353-58bac77be48e | -10.3874 | -44.887901 | 2024-10-22 00:15:43 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3fee72-c832-3c46-8f7e-754a3ebbd194 | -10.389 | -44.895302 | 2024-10-22 00:15:43 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23c75419-ea87-3f55-8186-3daab6e68ecc | -7.8245 | -61.3709 | 2024-10-22 00:15:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f6f02406-79b4-375f-acc5-2e7cdd94e447 | -10.3087 | -36.6491 | 2024-10-22 00:16:03 | GOES-16 | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 132.4 |
| e61952bc-2cf6-38e3-86d6-8a9583c77b80 | -10.3092 | -36.6222 | 2024-10-22 00:16:03 | GOES-16 | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 152.3 |
| 5f2b4859-af77-32d5-84bb-7a35ee6e7b3f | -8.842 | -44.2225 | 2024-10-22 00:16:06 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c514f9aa-8f51-3366-8f52-c3431be50abd | -12.5167 | -63.0521 | 2024-10-22 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| efb32af0-1ac1-3aef-930a-4bcfa3645701 | -14.3029 | -59.3399 | 2024-10-22 00:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 252.4 |
| cd37b69c-0364-308b-8211-e1c2eab37fe4 | -14.3031 | -59.32 | 2024-10-22 00:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 046293ac-97f7-3078-8698-8dda12495bbf | -14.3218 | -59.3581 | 2024-10-22 00:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c12a3296-78be-3623-9fdc-d7ef9137d219 | -14.322 | -59.3382 | 2024-10-22 00:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 22149c9f-191f-3b3d-ac71-bbdd78564863 | -14.3223 | -59.3184 | 2024-10-22 00:16:27 | GOES-16 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| aa226ea8-4baa-3548-b51d-e8e181254fc3 | -6.666 | -40.4631 | 2024-10-22 00:16:27 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 53774fa2-f5ff-3b37-934c-4d70f0631891 | -6.668 | -40.471802 | 2024-10-22 00:16:27 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 42f17153-2a9d-3f05-a2cb-03e491b716ac | -6.67 | -40.480499 | 2024-10-22 00:16:27 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9d70c3f5-eceb-3f1b-9b8a-cb7226451f67 | -6.2011 | -39.445099 | 2024-10-22 00:16:31 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 765b3df5-7845-3394-b025-456e8d037fea | -7.1156 | -45.486801 | 2024-10-22 00:16:39 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7320368-8a6f-31a5-a6c3-3eca0ce5c46f | -17.0213 | -57.3333 | 2024-10-22 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 67851539-307a-3b3e-9553-6fb2a65d8ecf | -6.2295 | -42.643299 | 2024-10-22 00:16:43 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4591bb0d-dce7-36ec-9303-1aaab43ede0b | -6.2312 | -42.650501 | 2024-10-22 00:16:43 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6352c81b-b9f4-3749-a03c-3163036bad61 | -6.1581 | -43.281399 | 2024-10-22 00:16:46 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6d54d23f-894f-3c58-96e5-d83d8695bb97 | -6.1844 | -44.128502 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebccab98-6e6c-3ec6-9ac4-82cea7113846 | -6.1859 | -44.1353 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61e23392-8b80-3f34-8077-52d3719e8574 | -6.1875 | -44.1422 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f37d2bbc-082e-3f2a-a71d-e01e3a94b20f | -6.189 | -44.148998 | 2024-10-22 00:16:49 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
