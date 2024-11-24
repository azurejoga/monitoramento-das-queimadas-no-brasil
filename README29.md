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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e55793eb-0fc0-3a49-a822-6f6ab30da1c0 | -1.95501 | -49.53469 | 2024-11-24 03:57:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7be84701-09b7-353d-ad3d-2dc08195c608 | -4.27062 | -48.60772 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad82c751-7a13-395b-8fa0-446cfc7eff38 | -3.79356 | -40.99574 | 2024-11-24 03:57:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 475681d5-bbde-3fe0-b2b1-a04ca67f4cc9 | -3.34047 | -50.51121 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3582de1-f759-38d8-8d77-a4be486afbca | -7.21936 | -38.65129 | 2024-11-24 03:57:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64be9a3b-4898-3153-b107-da8350c2091b | -3.9786 | -49.93646 | 2024-11-24 03:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02609a8a-df91-3477-b4a2-4cc01b6269fb | -4.08848 | -46.83253 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a06957e-154b-3d2e-8aee-f8fec568291d | -2.27159 | -47.97982 | 2024-11-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6755abe4-4431-3336-84f0-145333fe4cbd | -3.39034 | -50.33047 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0405d82e-54ae-382a-bebe-2145ab7ac85a | -3.76946 | -44.05572 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c954ba-cfce-39da-a0e6-cba5a4763e9b | -3.84255 | -44.04767 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 266fc372-a98d-32bd-ad7b-e82c3db81fce | -5.93371 | -39.47255 | 2024-11-24 03:57:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a4e1ac0-689f-32bd-bc62-8db4c9d6b402 | -1.29175 | -51.73412 | 2024-11-24 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0f677d1a-cca4-310a-ab6e-1a24e6b694c7 | -5.10732 | -43.15501 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 28c9c512-ce5e-3dd5-a43b-abd908bc9d24 | -1.96251 | -48.39248 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a02e1fc0-9351-3492-821a-e81c30432da5 | -3.64146 | -50.22603 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced7e4f9-49ed-36a0-ae52-f7a040b017ab | -1.6061 | -46.88412 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| c56ba1ad-4169-3a26-abfd-b8a41a808388 | -3.08271 | -40.05778 | 2024-11-24 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93ae2aea-b7e1-3bee-b4c6-4029f1e8bf2d | -2.55391 | -47.2729 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 737c95ee-821d-319e-a4f1-3cc137645e7f | -3.48765 | -50.08821 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69201a0d-02d6-3d42-b95d-d6a8e3aaf57b | -2.71633 | -46.28054 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c56373a-68bc-3b9d-a347-6656659bf272 | -1.04151 | -51.74689 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c71f34ed-b813-31cb-9c8c-8468bd49f20c | -3.77028 | -44.05058 | 2024-11-24 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59482202-e7fd-35cc-9fd0-aae55c549d32 | -4.95126 | -47.80511 | 2024-11-24 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c396ac88-4504-3c7c-ac78-7e2ca0500b05 | -2.4852 | -47.09591 | 2024-11-24 03:57:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af468e3c-20e3-3063-b1d5-2334291348ed | -3.69952 | -42.31153 | 2024-11-24 03:57:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7ec661e7-a3a5-357f-9f24-4717db725687 | -4.85085 | -50.81003 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4aa58aab-12a9-3544-8b8b-7100941e341f | -4.19659 | -45.36021 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75e82872-31f4-3698-9fdd-7344aa7b906e | -2.96494 | -45.12048 | 2024-11-24 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40513017-9e89-3052-b17a-b37bac86ec18 | -5.43236 | -45.45911 | 2024-11-24 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33ec4e56-e1fd-3c4b-9d02-bb289ea8b429 | -1.9545 | -46.4375 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f5efbb3-1648-33e2-b1c8-9b1968e807c1 | -2.32778 | -46.34786 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66e4a203-f175-3fc3-abd6-4d9e429c4cbe | -3.79298 | -40.99938 | 2024-11-24 03:57:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c4b8e8e-0f1c-3c86-9109-e0e50b38fe27 | -2.73626 | -47.53888 | 2024-11-24 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83bb8cca-6d6e-39c7-8f4b-49f2be90b373 | -5.94808 | -48.04889 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98314a15-0cc1-34d5-87d3-47141df1ffdc | -3.95822 | -50.20314 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 51262190-b44e-363e-a419-27d954004530 | -0.03073 | -49.64361 | 2024-11-24 03:57:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca5cac7-79ea-32cc-bd58-ee96c0c4f7ae | -4.44912 | -46.12478 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 980f9d94-62ce-3c21-b58c-1015f8fe7a61 | -3.38508 | -50.32476 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dc77672-4804-3750-b0f4-d15b11fb2ac6 | -4.25888 | -49.82934 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dc8e3e0-41fa-3b30-b571-165cd924599b | -4.65624 | -46.05529 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a3ca743-3e90-3aba-b7d1-8e62d9b137fd | -2.07318 | -49.61416 | 2024-11-24 03:57:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e697dd46-8849-3666-9382-20ec0d515c37 | -4.23761 | -48.67178 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f90da3a4-acc6-3f8b-879c-17dc425ba698 | -7.32498 | -35.32924 | 2024-11-24 03:57:00 | NOAA-20 | ITABAIANA | PARAÍBA | Brasil | 2506905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dcdfa157-919a-309d-8f06-d5038dd732a0 | -3.52905 | -50.76403 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87c4dc7-c511-3c3e-9ffc-ebdf66a13635 | -2.6976 | -46.27753 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16c51b0e-e136-3bfa-935c-94ed1d22591a | -2.8612 | -48.43679 | 2024-11-24 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4821482d-0ee4-333e-be8d-934ef872aa76 | -2.06452 | -50.31709 | 2024-11-24 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d3307c-e7d4-3885-9efa-e3ab2652880c | -2.91541 | -45.3642 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8afac19-c1eb-3408-94e9-f6872504bf7b | -5.48533 | -46.23892 | 2024-11-24 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0501cc1c-4da9-3058-a90a-2213e065a473 | -2.24518 | -49.22026 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a28a2d3-ef18-30cf-8572-9270e0a58f20 | -2.27272 | -48.4315 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f3957de-f78b-3b24-ae7f-bc37791c1278 | -4.53729 | -42.90263 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d5a08ee-db32-3b23-89b2-f87d6f385922 | -6.84635 | -39.43447 | 2024-11-24 03:57:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 40dd9c58-408f-34b5-a040-0c9ea14772f9 | -3.70171 | -51.79965 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11d89f35-3af4-3ecc-8884-4126f99fb32a | -1.04835 | -51.74807 | 2024-11-24 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e53dad2-5e99-31ab-8079-90842b50e4ba | -4.31571 | -38.12938 | 2024-11-24 03:57:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b89e7235-7076-3c83-a4ee-420009efdc80 | -1.34436 | -46.91497 | 2024-11-24 03:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ff03eda-2b4e-3efb-9a7a-2ba31b0f186d | -2.73738 | -49.12065 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a618165-0faa-3312-b59c-4ea5a96af340 | -4.53411 | -46.43048 | 2024-11-24 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7502ef6-41ad-3a2f-a26b-c804f61f2349 | -3.95676 | -45.99754 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 587aea8e-2957-3193-80c2-99fe53ff72c0 | -3.34051 | -50.50814 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c38d47-883c-335a-99c0-09a95428dc29 | -4.93566 | -44.07243 | 2024-11-24 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a52f6293-8c32-3087-be56-fd4a84e89a24 | -1.7593 | -52.71006 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcd275f9-51e8-334e-b5ac-b890585899ac | -4.51156 | -45.72589 | 2024-11-24 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a0c1d2-26a6-305c-9b0e-b5f4ded40470 | -2.44577 | -49.092 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e1dff0-d563-37b7-8428-877875b851dc | -4.27006 | -48.61103 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c491567-a17d-3b64-a49f-e5b4fe22c6af | -1.18178 | -47.80012 | 2024-11-24 03:57:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2721f656-9faf-37a3-aee9-622d14ffbc39 | -4.24255 | -48.70763 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 11166336-aa7e-3b4e-80e0-90750fffe0a7 | -2.57886 | -51.88876 | 2024-11-24 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c081a293-38e8-3b10-8c9d-06f25774334d | -3.62491 | -45.0671 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50f8a769-60fb-3430-8382-d9ed6ce6676a | -3.57984 | -41.9505 | 2024-11-24 03:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f58bd023-f1b5-39e4-a423-d9821a70ff33 | -4.69395 | -45.84921 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8c8258c-dc63-36c6-810e-e3a783482729 | -3.95222 | -50.20228 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0ff7cf3e-3b0b-3b4d-91ad-f23d38c81577 | -2.85944 | -48.43678 | 2024-11-24 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0783b139-2bfc-31ba-b340-c6cc55c1bd5d | -5.00173 | -42.95005 | 2024-11-24 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3f69316e-43cf-34e6-8c5c-ab36b63c76e8 | -3.47257 | -50.43839 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50e408a6-cc09-35c9-9505-b7b6e9269edb | -2.73566 | -46.10404 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeecf633-2496-31d2-9e0c-e241ff8e99bc | -0.2539 | -51.63177 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91203513-314c-32e6-a4c2-5ad4b92c57d4 | -4.84469 | -50.8092 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dabec200-fcbd-370e-b96f-bda92080d0ce | -2.7986 | -46.80231 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c52d57b7-71d8-3533-b8b6-b80f508283ac | -2.01628 | -46.29504 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48aecae9-8477-397c-a6c9-3e4880271bce | -4.35673 | -45.27752 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dea1050-634b-3e6e-97ff-d3cb1d393766 | -4.95176 | -47.80215 | 2024-11-24 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57ff6be8-a1ba-3a86-880d-dda8ce920c40 | -3.85094 | -50.43438 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dd2df6f-d673-39bc-949e-a5bee683f21d | -3.07745 | -49.20179 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46c3e1ed-e0cc-3d31-99a7-3435f43f9d10 | -4.84953 | -49.35761 | 2024-11-24 03:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49b42832-89e2-378b-9dc7-a0fd2402a9d5 | -1.31808 | -49.38947 | 2024-11-24 03:57:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20bac267-9a48-3524-9952-f2c5174bb220 | -2.8755 | -45.3594 | 2024-11-24 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 345177a3-0ff3-3eb4-a01a-39ea3d8c5a28 | -3.15706 | -49.90482 | 2024-11-24 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18395b1f-b681-306f-bf79-efd6c49ad7a1 | -5.16358 | -46.20474 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45462899-82fe-38c4-8d90-9278449e1b79 | -5.95159 | -48.05834 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61080d0d-c98e-3595-90c7-7ccc1289e2a8 | -5.09926 | -43.15812 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7eb0bb2-1b73-314a-a65c-b4d9f37c4ab5 | -4.52562 | -42.90505 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9f40f03-bb71-3599-831a-9973f7413599 | -2.70471 | -46.26355 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50cc33c3-fe49-3e11-8a2b-a1151af592c3 | -4.6326 | -46.86687 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54e2e6c5-5fa0-369d-b294-ca213e1c347c | -1.96856 | -48.38981 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e109f28f-8630-3dcc-b517-69da0571346d | -3.54014 | -50.19256 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb3db7c-a6df-3961-a914-878055e6e0f5 | -2.91809 | -50.3282 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb6fe5e-c8fc-34cf-b63b-9ded95179ae8 | -2.68365 | -46.15954 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README30.md)
