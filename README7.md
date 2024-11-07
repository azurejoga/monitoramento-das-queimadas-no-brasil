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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9606c6a8-8596-3068-ae75-1112f9c4ddff | -3.2231 | -53.0937 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84e01c45-03fb-3f62-b8c2-9b874b1cea22 | -5.1124 | -44.342701 | 2024-11-07 00:31:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c892693b-943e-3a34-a3c0-9d6f77bbc21f | -5.164 | -44.121799 | 2024-11-07 00:31:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd9ab9d0-f567-3ea1-b003-fc0f08a643dd | -3.6601 | -52.3437 | 2024-11-07 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a979be8b-1572-3218-8972-c9c872f1bbaa | -4.2331 | -48.544498 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b740fb16-ee35-32a3-9902-1b4039253e0b | -8.501 | -42.081501 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da2289df-88dd-3404-966d-8aa3660e9a8e | -2.0565 | -46.338001 | 2024-11-07 00:31:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cefa6745-06dd-3347-82c6-802e13a6c0a4 | -4.7444 | -48.9814 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9316077d-cd44-33bd-84e0-9140c7709839 | -3.0101 | -53.423599 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6449b79f-dbc4-3397-ab59-cb8fceed525f | -2.7269 | -51.7118 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee04e23-efac-3cc6-a8b7-787413dffde6 | -8.3082 | -43.618 | 2024-11-07 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 368f0e01-7fb5-36f2-9708-b491ae3ac2d1 | -1.2145 | -46.355202 | 2024-11-07 00:31:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037df898-f272-3415-b8a0-a1e88fa57835 | -7.7892 | -41.6549 | 2024-11-07 00:31:00 | METOP-C | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d395079-5664-315b-a8cd-d5f1c41a84e5 | -2.8203 | -52.944599 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f91098ea-1bce-342d-850e-57dd84d041cd | -2.2358 | -48.0163 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7296c472-e7fb-3f90-88b5-ddb29c7f8617 | -3.0465 | -53.266201 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad47391-cd55-3ce3-861c-12f946f3d366 | -2.7493 | -53.221298 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1c2f5b4-9784-3c2c-a89f-a906107defa2 | -5.1436 | -47.698502 | 2024-11-07 00:31:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a14f005-a0d1-359c-8930-a01bb0dde0a8 | -9.7463 | -43.584099 | 2024-11-07 00:31:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d46f8e89-5a53-3414-897f-fe146ae63d7e | -3.583 | -50.2201 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0601e863-76e9-3d56-85c7-b24ecdef2603 | -2.8113 | -48.683498 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d08b1942-755d-3b33-bb0b-8add79dfe9c2 | -2.849 | -48.667801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12714425-3947-3959-ba5b-a713b1a03861 | -5.4497 | -45.526901 | 2024-11-07 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2e9c8f-74a4-368b-ab1a-d2c1d21b3789 | -4.3781 | -47.237 | 2024-11-07 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0be4bd41-c61b-306b-b7c0-8af002999e75 | -1.1074 | -46.831001 | 2024-11-07 00:31:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85a04590-825e-3c2c-b905-e7cc34d1a89c | -3.6643 | -50.260899 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cae73a77-14f2-3ce9-80e9-8a4ddcd38b1c | -4.087 | -50.995998 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8b1dd8a-9f3b-3afe-9928-c7692e95606d | -5.9693 | -45.363602 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00a46c67-c9ed-3161-8267-180575146ec6 | -3.1958 | -53.383202 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b632e98d-f724-33d1-a95e-24b9015a1e3a | -3.5281 | -50.3414 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8ed19c-f501-31e5-96fe-06e670b0be8d | -1.861 | -47.821201 | 2024-11-07 00:31:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3501e9-4b1f-32f4-8f09-5e555f92549c | -2.2044 | -48.825699 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3849101-41ea-3040-ab8a-94d155f6c651 | -3.6699 | -52.341599 | 2024-11-07 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ce7ce0-143b-3a9d-9dcb-3682cf790d68 | -2.9646 | -48.7229 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b56234-53d4-342f-b685-299d76656175 | -2.1806 | -48.315701 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a680755-2077-3856-b58b-92c0e67820ea | -1.8625 | -47.827999 | 2024-11-07 00:31:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7576f965-f5c8-38c0-8cc2-ec8fa42a4af4 | -5.7007 | -45.943401 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69ae0357-fa51-32eb-ba36-808355e69dca | -4.7346 | -48.983601 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076be059-8521-3339-8a3b-7fbff2caa220 | -5.8465 | -50.038502 | 2024-11-07 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60f61de-4e54-339e-a6f8-fbf35c7f215f | -2.8069 | -51.7924 | 2024-11-07 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754df10a-38c6-39eb-9565-8054ea45113e | -3.2376 | -53.3866 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 454cc79a-3a43-3207-b07d-f5ae7f58e3db | -2.4975 | -49.115799 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f9c1f16-3ca6-3082-b93d-ee57ceb1f878 | -2.4016 | -48.425098 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 755ba9c6-6feb-35e3-bee2-e9ef1e660307 | -6.0387 | -46.605801 | 2024-11-07 00:31:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05c16f60-9c39-35e4-917f-bfd384eef52b | -5.6208 | -43.9571 | 2024-11-07 00:31:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6fd654-3b26-36b3-867f-70c9a35ab91a | -4.3015 | -48.618599 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936b4bac-2d31-36e9-a855-cd2f227247aa | -2.7467 | -53.209702 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d726844-035a-3ee1-90b9-04606244f267 | -3.9612 | -48.165001 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb36a33d-4ea6-31d1-b611-26c8bc9aa2cf | -1.9471 | -47.028099 | 2024-11-07 00:31:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e92a67b-35cd-31f3-80cb-4ad008440497 | -5.4833 | -43.196899 | 2024-11-07 00:31:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f498e7f-5f11-3930-8235-43838a64496f | -8.3101 | -43.6259 | 2024-11-07 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 926ea410-6978-3dc5-ac46-4959a73a51b7 | -3.0447 | -49.5271 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f112d7f-feaa-3ec6-b9c6-9ce562e9e0df | -8.498 | -42.112 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 599cadc7-7b48-37b1-bc6a-316af46681b3 | -3.4497 | -50.3587 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e66ffb-791c-3115-ba56-efd945f86ba7 | -2.8202 | -52.898201 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ddeb9dd-b057-32fe-a5cf-ebdfd3b7ca75 | -4.0206 | -48.2901 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf03fcb3-f85c-3ffc-8a95-f3ed88d8f6c0 | -9.2967 | -43.123001 | 2024-11-07 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7841e332-069d-36ce-9872-b1d224e7ad04 | -6.4829 | -44.6866 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92a5da85-c88e-33ed-94b7-2c4406fd1e3a | -2.809 | -51.801899 | 2024-11-07 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1196ddee-5c9f-34f6-bfb0-c66eafdf266a | -2.7194 | -54.1353 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0578d3-2b28-363b-8ea7-882106b8ac93 | -3.2501 | -53.396599 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4391ecbc-e552-303c-9311-db259ef4745c | -3.2914 | -50.069401 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a00961ff-bc25-34a7-949d-84dda04561f7 | -6.1704 | -44.851898 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caabafdd-720f-3efb-a9a7-2bc1330d6ff1 | -8.684 | -47.956402 | 2024-11-07 00:31:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e07d5e03-5fb0-3925-8190-25d97d974c7e | -5.1065 | -43.9645 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c321af2-638a-359b-a9a5-b4046bf3e286 | -5.6158 | -45.9333 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb95d14-98af-3bb5-baee-72150747262f | -6.2274 | -45.319599 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb21253-72e9-30ca-a357-14ba776dc86c | -5.1658 | -44.129799 | 2024-11-07 00:31:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c71cd1c5-3c89-3b86-830d-239edf83b257 | -9.5917 | -43.1469 | 2024-11-07 00:31:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 30b4d6ad-503d-3af7-86b5-0bbffc9eb4e7 | -3.0368 | -53.268299 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88a160de-46a2-398f-912b-b0b71ab4d20f | -3.5164 | -50.335499 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e8f019-7c16-3a7f-88ce-76b1289ec2b0 | -4.5071 | -42.8633 | 2024-11-07 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c86470e-1f82-31a2-932f-ac0fa908f332 | -4.2867 | -48.6441 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986d2379-831f-363a-a552-5c3dc515cb8d | -6.471 | -39.751801 | 2024-11-07 00:31:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8d225516-3082-31d6-9fb0-19c865d025dc | -12.2833 | -51.209702 | 2024-11-07 00:31:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c204a015-2b54-32d5-8a6b-bbdd142bfae8 | -5.3354 | -46.193901 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc399192-8b91-3d9c-8eb1-da288ae2e4c2 | -3.2023 | -49.223301 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef09032c-b3f1-3b7e-9377-7db595a53c17 | -3.0067 | -53.225899 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4518edb9-de0f-3e90-9518-26b12764bd70 | -7.4089 | -44.806198 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf737f5d-5b6c-32e7-9368-14a3a308844d | -8.4957 | -42.1026 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fdb28f9-5ac5-32b0-a0bc-301667995b48 | -5.4514 | -43.587101 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a6acfdf-3aba-3758-82c3-fc6f1d3bf8d8 | -9.1441 | -43.133301 | 2024-11-07 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2420d742-9134-3693-b5b8-0779d5aff05e | -6.5319 | -44.4543 | 2024-11-07 00:31:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eadd3f32-1f87-34e4-98a9-482a4cb00de3 | -3.2138 | -49.228401 | 2024-11-07 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2162d6cb-9142-3f65-8f12-db321c2b79a0 | -4.2539 | -50.686401 | 2024-11-07 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab5d0946-c0db-3fe3-9701-80b037008b44 | -3.2932 | -50.077202 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9516b258-a117-391d-b5eb-c72362a510ad | -8.0274 | -49.6329 | 2024-11-07 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83797589-ecc5-3587-a98c-6ea96db619d0 | -2.4297 | -48.592999 | 2024-11-07 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076fb40a-2f38-3205-9a0b-79839432ffd0 | -4.6351 | -49.363499 | 2024-11-07 00:31:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d752a8-8b7c-36d6-a033-05a2518504ae | -2.8631 | -49.543999 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa177f21-b46e-32ec-94d5-6c220f5bef27 | -3.5145 | -50.4636 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32b07db-fc5c-3ff8-9979-3dd334a507d3 | -6.9591 | -39.809601 | 2024-11-07 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a65e782c-71f0-372a-9641-7629d66e0c11 | -2.8588 | -48.6656 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1530eb7-96fa-3650-b300-e03e07166b95 | -3.4717 | -49.683498 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9be76cf-8885-34a0-8d39-6e276eb8031e | -7.1324 | -44.816101 | 2024-11-07 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f28feac-3b57-3f02-8f2a-0986bb6aee34 | -5.6142 | -45.926399 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7830efca-b3f0-37f6-9092-45639ea9fdbe | -2.6115 | -51.746899 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e30ff2-ba73-3425-ba01-be69ddf92058 | -5.9905 | -45.366199 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f4f16d4-df7a-3864-91e1-082617f0b991 | -3.4359 | -50.252399 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dee99d2-08bd-30cc-a50f-e46dfc5fe3d6 | -2.8506 | -48.674801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
