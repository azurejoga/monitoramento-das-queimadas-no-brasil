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
| a93a7b75-cdab-3585-93a0-fbba44339a9a | -3.7854 | -45.658001 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0713c132-5674-3163-931f-ea68b5f169dd | -4.3106 | -48.082901 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1820fb72-7013-35bb-9065-2dca59d4ae17 | -4.0458 | -46.856098 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf788088-9569-3e3f-ad8f-a0e4e3bbb9d1 | -11.0754 | -44.299801 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb0a6d6-fa8d-31b9-956e-0575dcae0acc | -3.721 | -51.216702 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b70d890-31ac-354f-9c79-cd3bc2a39248 | -3.2983 | -45.2827 | 2024-12-04 00:17:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a724f791-0796-3c47-841d-5e2255aef4dc | -2.7505 | -45.276299 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd0f4a3f-48d2-379c-adf6-19d1686894e0 | -3.6622 | -47.120201 | 2024-12-04 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11dc0f16-5076-3369-be3f-fe65de714ec4 | -2.0187 | -46.322102 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c5134c-bdf2-32a4-a638-d5f62912ae69 | -3.5698 | -50.301102 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f6c581-7af8-37d5-8606-a285deeaf771 | -5.8127 | -44.103802 | 2024-12-04 00:17:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1266f05a-896e-3152-be6e-d20189810605 | -9.1908 | -43.140301 | 2024-12-04 00:17:00 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb8bee3f-55ec-324f-90da-47d981b4f77f | -3.7286 | -51.065102 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a563dc7b-76c6-390c-8fef-35e908716545 | -3.3964 | -50.2146 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af7fc6e-170c-3da3-8ec3-9d4b9e09e14c | -2.1619 | -46.636799 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37509dca-f579-354a-beae-a9521b9a3a86 | -4.1127 | -43.9282 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23eb8f61-2898-3731-b24d-7cdfae0e64fa | -2.6655 | -46.265202 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3c5e63-4a8e-357c-b415-2f9eb5dd52a3 | -2.6896 | -45.643799 | 2024-12-04 00:17:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e53c371-ed32-3c8c-8bba-7c5c3613caaf | -4.0373 | -46.133202 | 2024-12-04 00:17:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98305eb5-6630-3790-b19a-299c9f72f08c | -4.0349 | -48.3232 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830c456d-5ea9-34a2-8856-c6333a85f681 | -3.6592 | -47.106602 | 2024-12-04 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443960ce-cab2-3394-9453-b7ba45b6957b | -3.26 | -53.634998 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c09b931-a542-31b9-a7ae-138a05112c5b | -4.0777 | -46.6772 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7b92f9a-5d82-342b-aab2-a768d94f3202 | -2.5945 | -45.997101 | 2024-12-04 00:17:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25be9efc-6f3e-3c5f-b4c6-8b0b603d3a5c | -2.5772 | -46.558899 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b62ac9d-b1ba-399d-806a-199a3b401254 | -2.9695 | -45.196899 | 2024-12-04 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1668c4b-8ce6-3eeb-91a0-0cbc8554d535 | -3.5758 | -50.281898 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba6010c8-4400-3400-a09e-6d99ce2c9ada | -2.151 | -46.132401 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7ec9727-52d2-3ae4-b5d3-89bc7c6a34a2 | -3.365 | -51.0457 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f98e134-5da7-37f9-8518-f67a53886e9c | -4.0539 | -46.983299 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4053bb4-0372-3afd-bdf2-dad84abee725 | -4.7416 | -45.692902 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcc8886e-ee09-3c9d-b0df-bf395e7bcf69 | -2.6816 | -46.1091 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 981ec368-1941-3f76-a9ee-d1786b7ee7c4 | -2.6904 | -51.8451 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a03685-bcaf-388c-bc1b-90f988aaa9a2 | -3.0576 | -54.015301 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7937e2ed-4c5d-3c67-adc5-386b3bfba9cd | -3.1249 | -54.600101 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f406b551-1759-3386-b318-a244e483a190 | -3.089 | -49.480499 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7438d463-9971-3336-833b-118b52e829cf | -3.653 | -50.676899 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f396ffcc-ae35-3746-b1e7-744e846947de | -2.5674 | -46.5611 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b3f3c8-d551-3a5e-8200-c7b9a60acdb1 | -5.5679 | -45.154499 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 128c11b1-22ad-386a-b1b2-bc11f31a6b4d | -4.1189 | -43.910099 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe89c59b-b47c-3357-add6-322f31696315 | -3.3712 | -51.0737 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 457b9bae-666e-308d-bb39-f6782d2f7e93 | -3.5477 | -51.500702 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a792b243-8ca0-380f-89b4-7c1e3db1b677 | -4.0345 | -46.851501 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6009298-d7eb-34f1-8af8-1849c6f82f6f | -4.0163 | -48.793499 | 2024-12-04 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa6ae53-9b61-36de-a98e-acb958b3f172 | -3.8227 | -46.597801 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb8efdff-b552-3e23-b97d-97ba76e471b4 | -4.3724 | -43.353802 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a764f8f0-50b5-386f-a7a5-f8308a67dcd0 | -3.4438 | -54.053799 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad297471-fb47-3600-a913-9e155420ab4a | -4.323 | -45.801201 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53731c79-41b2-36c8-8fe5-00b8aec29129 | -2.624 | -45.717899 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15b503bd-89ec-3aa0-beb8-954daeb0f320 | -4.3822 | -43.351501 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b226727f-750a-3173-801d-81b931e16f0d | -2.9679 | -45.189602 | 2024-12-04 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfe5fe1c-63b3-36f7-93b9-2cff547924c3 | -2.8096 | -53.0308 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99cb3637-f183-3709-9c60-f4c6a0726742 | -3.0997 | -54.021301 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65811e5f-0998-34a2-9833-69be209ab48e | -3.1787 | -54.473701 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f262f2b5-d549-3b1e-9dc6-55a86df2edcb | -4.605 | -48.0182 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9223f8-8778-35af-9729-55881598060d | -3.8398 | -52.1287 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5520039-ab05-3f69-9f35-a059793acb9b | -3.0168 | -45.495998 | 2024-12-04 00:17:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbbf6485-bc7e-36e8-a3c3-f883b031dee2 | -2.8816 | -51.7822 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8c64d3-9daf-322c-9af6-08c34cc0838c | -4.2984 | -48.2127 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05d29fde-646f-389d-a1d1-02928213f8cd | -3.5203 | -49.892899 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c23791-69ce-37aa-8c70-059dfa23b31a | -9.3135 | -43.0462 | 2024-12-04 00:17:00 | METOP-B | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 515de82f-99bd-33fe-882c-b0ef332e4c42 | -3.3333 | -51.180599 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4df2f5-1206-3386-977c-74eca7f1780a | -1.2171 | -46.514599 | 2024-12-04 00:17:00 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 969ea182-6e30-3e23-bf50-4047a07a92ef | -3.9342 | -46.9095 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23e7e002-746f-3d33-bb52-ea089d8d997e | -3.0453 | -54.470001 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28935989-68a2-3b0c-82b4-3a7604018f08 | -3.8521 | -52.1376 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6568d64-3954-3fea-92ae-b05ea49081a1 | -2.9597 | -45.1991 | 2024-12-04 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5f447eb-e85a-3aa1-a337-1cad05479a85 | -3.1185 | -45.990002 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1a0707a-c5bb-3295-818c-c637e891c400 | -4.1881 | -48.826099 | 2024-12-04 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17722e48-d112-35bd-9750-72fb423b5a0d | -3.33 | -50.0546 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8059342-44ca-37f2-9f92-701ecc084d98 | -3.1116 | -54.586399 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62484d8a-d0cd-30c7-84f5-98ee4d2f0708 | -5.27 | -46.160702 | 2024-12-04 00:17:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72530ce2-f57e-39c6-84f1-085ee6f35580 | -10.2144 | -42.1712 | 2024-12-04 00:17:00 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 43a59060-7a25-384e-86b7-2882429029b7 | -5.6104 | -43.941299 | 2024-12-04 00:17:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06fd887d-36dc-3abc-a93c-a1c75ae6895e | -9.871 | -36.608501 | 2024-12-04 00:17:00 | METOP-B | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90be6565-4e24-3d00-a5d0-b3b7a1c46c37 | -3.6259 | -51.018398 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 422a396e-ccae-3e81-a7a6-ee5402006a31 | -3.9787 | -50.338402 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64bd9eb3-7fd2-3124-8a1a-8a58ca8a2044 | -3.0302 | -49.493401 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3e6498-ba48-3c5b-8f64-7f79eb4a8503 | -3.9547 | -52.1852 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77520e06-c734-3817-9a52-32cc2ffa20fe | -4.7158 | -45.669601 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe1b7b7-bcb4-3a78-b1a5-32f61f732825 | -2.6718 | -46.111301 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 716d7e9c-13af-3a5a-829e-e83711ab10a7 | -2.0231 | -45.522301 | 2024-12-04 00:17:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2607b4-2bf6-3647-a819-3f22adf0bb6d | -3.5398 | -50.165699 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de2cfc30-405a-3926-b1ad-ea61e7ee1279 | -3.7906 | -46.683701 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 369e681d-0a59-3e2e-b64a-ad88936c1081 | -4.2469 | -47.567699 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9052faff-aa23-333e-ad63-9c277b8b97e4 | -2.8959 | -51.8004 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a2d991-5a59-34cd-9023-2c82272f2eb3 | -2.8194 | -53.028599 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37cd81ed-1595-3158-bbac-997264490f50 | -2.1526 | -46.1394 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9012d8a7-4a0a-39c9-8ca5-115efc5a3519 | -5.1203 | -44.277 | 2024-12-04 00:17:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 758f9dcd-58ea-3772-b15b-76ff54f58689 | -2.9672 | -46.916599 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e014e61d-2de1-354f-af45-eac0df73f8d1 | -2.1994 | -45.663601 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65de4a3e-e48c-3e21-b2db-a194d8bc3fae | -3.4341 | -54.055901 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcaa2bbe-4201-3498-8947-5c70710a6bfc | -2.5937 | -46.266701 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c18b2ee-a8c4-3d68-abbd-cd55986168ac | -3.5796 | -50.299 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f7d0ec-7d42-3629-b15e-97caf43308d0 | -2.4428 | -45.691399 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6d848c-43b6-3852-9ec5-03353443d022 | -5.8204 | -46.454498 | 2024-12-04 00:17:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4981ae3d-4ed9-3456-850a-34581d84128a | -3.5537 | -45.863701 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3eec3b-0718-3d46-a893-bc232bc36915 | -2.7489 | -45.2691 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b849e861-3da7-3b2c-9560-ca5d736f0e96 | -3.512 | -51.292301 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e643191-1dde-3fd0-8014-4e1f70c245cd | -4.1837 | -45.369099 | 2024-12-04 00:17:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
