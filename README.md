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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3164de8-4451-357a-8109-c12432fc7681 | 1.8317 | -60.8765 | 2025-03-26 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 92a09336-620d-3f4b-8fe5-eca45200dfac | 1.8135 | -60.8956 | 2025-03-26 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2e5030ac-3f02-3b56-a19e-dde5df26593d | 2.5618 | -60.6975 | 2025-03-26 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5b9b808b-a09b-32ab-b1ac-5bd1bcd95e30 | 1.8317 | -60.8954 | 2025-03-26 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 3bd1789e-f859-3805-a4f8-eb621a516b11 | 4.0028 | -61.505 | 2025-03-26 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 18d0d36d-2acc-3fe0-816f-84108b32f0f3 | 3.9845 | -61.5054 | 2025-03-26 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 99822b46-3c95-332e-b530-433640d41fc4 | 1.8135 | -60.8767 | 2025-03-26 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.3 |
| e1a78e04-ddc7-3221-a8b5-c55c0693d056 | 3.9662 | -61.5058 | 2025-03-26 00:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ba57cb0a-71c8-30a1-b06d-eee950892e8e | -20.2971 | -49.971199 | 2025-03-26 00:03:00 | METOP-B | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dab0b80e-3344-3645-80df-648b1cdab3eb | -20.3001 | -49.988701 | 2025-03-26 00:03:00 | METOP-B | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0c50b655-813b-3da9-b37c-2ab01d11bfde | -17.883101 | -39.843899 | 2025-03-26 00:03:00 | METOP-B | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7b6a9f8-90b8-3cc2-822b-0ab9e8efcddc | -8.1541 | -43.133499 | 2025-03-26 00:03:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6f042283-d100-3905-935e-5a55ffe5562b | -12.2779 | -42.089901 | 2025-03-26 00:03:00 | METOP-B | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b9a3a2d-3a97-335e-99b5-08e1aa7cdf5d | -17.886801 | -39.859798 | 2025-03-26 00:03:00 | METOP-B | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfc06777-7fe1-3516-937d-7b9606697185 | -10.5993 | -45.136501 | 2025-03-26 00:03:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec7e819-e933-3052-865c-fc88164a7d34 | -22.9333 | -43.7211 | 2025-03-26 00:03:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87d09d68-7421-373f-9973-c2998d521b26 | -20.170601 | -47.324501 | 2025-03-26 00:03:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c5678c82-371f-356b-851e-b3d0ac26c11f | -20.1684 | -47.312801 | 2025-03-26 00:03:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ca4d7b2a-2dfc-3d23-8dc5-6e7bb586c512 | -22.938299 | -43.746399 | 2025-03-26 00:03:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd668d7b-d3ec-3d87-88dc-05cc1a85b960 | -22.923599 | -43.723301 | 2025-03-26 00:03:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1a49c93-f54a-3d85-b219-0b1f04b7f056 | -10.5977 | -45.129398 | 2025-03-26 00:03:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2de4beed-878a-3b07-9d78-71a2a901ba26 | -8.1443 | -43.135799 | 2025-03-26 00:03:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee8c6ab3-214c-35c7-ba7c-1843516fed82 | -20.309799 | -49.9869 | 2025-03-26 00:03:00 | METOP-B | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8101fdb3-65ef-3583-86c1-4447ffcc826a | -15.5251 | -42.598999 | 2025-03-26 00:03:00 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa44863-7d17-337d-b6bf-a589423f288e | -20.302999 | -50.006199 | 2025-03-26 00:03:00 | METOP-B | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b24fbb49-473d-3f41-b7fb-ac29cac6c547 | -8.1558 | -43.140701 | 2025-03-26 00:03:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37c98b07-dbe2-3db7-82cd-8440f9c2ad61 | -20.483601 | -47.484001 | 2025-03-26 00:03:00 | METOP-B | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f8fb4f09-d4e7-3160-bf03-d157d1e281be | -17.885 | -39.851799 | 2025-03-26 00:03:00 | METOP-B | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a821cc91-d5d8-31d8-9bfb-acc0116d76b7 | 1.8135 | -60.8956 | 2025-03-26 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 5a386ee2-417d-3ea9-8159-abfec3c64a86 | 2.5618 | -60.6975 | 2025-03-26 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f185915f-d080-3ec4-a5c9-c713c7fecda9 | -17.8666 | -39.8386 | 2025-03-26 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| b0c06720-4443-3013-8197-2e42cd933aa1 | 1.8135 | -60.8767 | 2025-03-26 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 9a5cf9c2-8b22-3709-9c2f-8c1f3bd4b9dc | -17.8658 | -39.8648 | 2025-03-26 00:10:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| 98bcbdcc-188f-32cd-96c3-f55c360155dc | 1.8317 | -60.8954 | 2025-03-26 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e00218d3-9c48-3938-88bb-bf39f61729c0 | -20.3005 | -50.0138 | 2025-03-26 00:10:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 50f811c3-02ec-39ac-80d3-9aeef008035b | 3.9845 | -61.5054 | 2025-03-26 00:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 1142ef18-ec6d-3cde-bf6f-0b86f05e18e0 | 1.8317 | -60.8765 | 2025-03-26 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 2ece9384-d8f3-3bf6-8e98-b9c1913463af | 2.5618 | -60.6975 | 2025-03-26 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fb151da0-b362-3948-ac2f-b5708aaccc68 | -17.8658 | -39.8648 | 2025-03-26 00:20:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| dc6837a9-18b1-3568-b275-6136bf6cd576 | 1.8135 | -60.8767 | 2025-03-26 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 813b2d25-b011-3765-82bc-f1b8a41b8ccc | 1.8317 | -60.8765 | 2025-03-26 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 175.0 |
| cb2eab8e-d931-3817-a946-c36821a2d8c2 | 1.8317 | -60.8954 | 2025-03-26 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| d7a0bccd-192e-37eb-a273-d50dd42772b3 | 1.8135 | -60.8956 | 2025-03-26 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b89af0d7-1cf2-3d2a-8418-e44c0ec195aa | 3.9845 | -61.5054 | 2025-03-26 00:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ea09813d-a7e4-36de-804e-7ae2dbed5216 | 1.8317 | -60.8954 | 2025-03-26 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.4 |
| c5e991a8-8a9c-355e-b503-b6a63fd89c5f | 3.9662 | -61.5058 | 2025-03-26 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 04005ee5-811e-3274-8cab-50edfbc0b49b | 1.8135 | -60.8956 | 2025-03-26 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 078ec206-d638-3675-a998-de8781c159bb | -17.8658 | -39.8648 | 2025-03-26 00:30:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| b473f4a9-1b1c-3ec4-9d82-92de83f11a88 | 2.5618 | -60.6975 | 2025-03-26 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0a5a904c-fa30-3720-b3d3-d9a9d1b9cf57 | 1.8317 | -60.8765 | 2025-03-26 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 9dedee49-94c5-3602-a4f8-6bbccd471eb2 | 3.9845 | -61.5054 | 2025-03-26 00:30:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 9f7d183a-9d55-3aa2-84e2-5291a9ec51db | 1.8135 | -60.8767 | 2025-03-26 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| e0b64b2a-674b-3d09-813e-a0725f8b2bf5 | 1.8135 | -60.8767 | 2025-03-26 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 12908d07-fa76-3d08-8e90-f86a9653152f | 1.8317 | -60.8954 | 2025-03-26 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 1852b655-c38a-314f-a063-10b87e4d13fd | 2.5618 | -60.6975 | 2025-03-26 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fe864cc3-e538-3e39-91fd-9672cda1890a | -17.8658 | -39.8648 | 2025-03-26 00:40:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| ac6460c2-eb16-34ed-b906-d5fcf20b70c0 | 1.8135 | -60.8956 | 2025-03-26 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 02c972d0-72d7-3b7e-817e-50da9482b510 | 1.8317 | -60.8765 | 2025-03-26 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 0faf9512-4828-3cad-8973-94458bcec1a4 | 3.9845 | -61.5054 | 2025-03-26 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 6d029a18-506c-397a-b16d-1c309aae1b24 | 3.9662 | -61.5058 | 2025-03-26 00:40:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| dd51f85a-6b2e-3e54-8707-3843141b1042 | 1.8317 | -60.8765 | 2025-03-26 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.7 |
| e1c3e84e-f5d4-37e0-9102-a3e0d902ae8e | 3.9662 | -61.5058 | 2025-03-26 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3da5b908-a861-3257-8264-8c1a90dfb4a5 | 2.5618 | -60.6975 | 2025-03-26 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 2b4abd6f-9093-313c-a6ce-d20ff858710a | 1.8135 | -60.8767 | 2025-03-26 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| c17d03dc-a095-312c-b6c3-894be904b3ad | 1.8135 | -60.8956 | 2025-03-26 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5f289a29-c5c0-3d88-a984-9c0eaccc53e4 | -20.3005 | -50.0138 | 2025-03-26 00:50:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 5e41e7da-4bda-36d4-8b74-5637f4ad6991 | 3.9845 | -61.5054 | 2025-03-26 00:50:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 42011561-e32f-376b-a15a-12aa8b555a89 | 1.8317 | -60.8954 | 2025-03-26 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 184d5eb0-1ff1-3115-87e3-806d71a2631a | -17.895599 | -39.871899 | 2025-03-26 00:55:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c78b9bd7-7e46-328a-977f-ff719be7b8d1 | -17.8892 | -39.8489 | 2025-03-26 00:55:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72305e8b-940a-305d-97c8-3295b49df957 | -20.315701 | -50.005901 | 2025-03-26 00:55:00 | METOP-C | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9168d152-1e57-3ab0-9f64-17190ec14c6c | -20.317301 | -50.013199 | 2025-03-26 00:55:00 | METOP-C | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f98be454-692e-3216-8928-e1d4eed8b0c1 | -20.3141 | -49.9986 | 2025-03-26 00:55:00 | METOP-C | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3bcc66-14ba-3823-aa06-7af2c0db829a | -22.929899 | -43.7295 | 2025-03-26 00:55:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88dfa59b-576d-365e-8a13-c7cd3bbf3972 | -20.1744 | -47.3288 | 2025-03-26 00:55:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69dad4a6-e198-3a34-95eb-921d1dae8cd9 | -17.879601 | -39.851898 | 2025-03-26 00:55:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c1d9722-8bd1-3bc1-8d88-e59cfcb80feb | 3.9845 | -61.5054 | 2025-03-26 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fab36f66-0dfd-32c3-8b55-507e3fedbfde | 1.8317 | -60.8954 | 2025-03-26 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 39e6e278-e97c-3ed9-beed-c65d0501fdcb | 1.8135 | -60.8767 | 2025-03-26 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 80259d13-86ce-3bf3-a911-fb407066429f | 2.5618 | -60.6975 | 2025-03-26 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 482d32ef-93a3-3df3-91a5-cc5ea4870033 | 3.9662 | -61.5058 | 2025-03-26 01:00:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ae2dd789-198c-3fa0-8457-97a647f23b01 | 1.8317 | -60.8765 | 2025-03-26 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.0 |
| c7a36e12-efbc-32e7-94a9-72e6ede392b4 | -17.8658 | -39.8648 | 2025-03-26 01:00:00 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| 66780d03-7a7f-3e81-9fc1-8aff617b69a8 | -20.3005 | -50.0138 | 2025-03-26 01:00:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| e72ef701-48af-3767-afb5-7a2c38c8263c | 3.9662 | -61.5058 | 2025-03-26 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8a5658c8-b065-3393-85bd-3cb1a71e4b3e | 1.8135 | -60.8767 | 2025-03-26 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 265e1cea-4641-3d83-9353-377ea8338ef1 | 3.9845 | -61.5054 | 2025-03-26 01:10:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 03cf0ea2-805f-3c8b-8226-f037a0360d00 | 1.8317 | -60.8954 | 2025-03-26 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 8e370501-3c1a-3614-9ed4-2430b7fd2aa1 | 1.8317 | -60.8765 | 2025-03-26 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.9 |
| c35b72c7-493b-3876-9ee9-8ebca7c29e20 | 2.5618 | -60.6975 | 2025-03-26 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bd7c4f5c-4dce-3bbd-a6c1-b6d399867f6c | -20.3005 | -50.0138 | 2025-03-26 01:10:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| c9478fff-8e53-344d-8005-33d1f06542cc | 1.8135 | -60.8956 | 2025-03-26 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 76842adb-b607-3e5b-a169-3b4821176417 | -30.81692 | -52.23581 | 2025-03-26 01:17:00 | TERRA_M-M | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 8.5 |
| 5de5d07f-07bb-3ec3-a935-2223be2317b5 | 1.8135 | -60.8767 | 2025-03-26 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 62b5d04e-7a95-361f-a734-edf386965d35 | 2.5618 | -60.6975 | 2025-03-26 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4bd34773-7daa-3494-9933-6820584f9690 | 3.9845 | -61.5054 | 2025-03-26 01:20:00 | GOES-16 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0e70ddb0-f53b-3377-b114-7df4d25c0489 | 1.8317 | -60.8954 | 2025-03-26 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9cd4a266-659a-391a-8a9b-6cc7ccacf7b0 | 1.8135 | -60.8956 | 2025-03-26 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 81b0cb42-635b-3e78-b6a5-4f539fa63fa6 | 1.8317 | -60.8765 | 2025-03-26 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.0 |
| b9e3316f-bafa-3194-be7f-287056fe9c25 | -20.3005 | -50.0138 | 2025-03-26 01:20:00 | GOES-16 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |


[Clique aqui para ver as próximas entradas](README2.md)
