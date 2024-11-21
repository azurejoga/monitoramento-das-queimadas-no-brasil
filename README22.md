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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f339b33e-ec83-388c-b74d-32d9ede1ef95 | -5.23711 | -42.64037 | 2024-11-21 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a1ecf8-9aff-36bb-a1db-a1fbfbd11e27 | -3.12445 | -45.44712 | 2024-11-21 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9e816ba-c92a-3d39-980a-68b5f7347728 | -2.78918 | -52.55052 | 2024-11-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ce830dac-806a-398e-aea3-0a9ceeefe716 | -5.50597 | -46.39487 | 2024-11-21 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd8116d4-778b-32fe-b810-9ec67d41ce2f | -3.2014 | -54.3243 | 2024-11-21 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 09fbc7e1-0bb4-31d6-82bb-1987adc30311 | -2.0259 | -54.5289 | 2024-11-21 04:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 22e512fd-ea6d-3429-add5-5d6f95d9b0b7 | -6.1182 | -42.5086 | 2024-11-21 04:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 0cdb9df0-72d6-3eda-a228-39ec6c898d9a | -3.2951 | -53.8395 | 2024-11-21 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3b0fae61-13c4-340d-b90c-a315e688c9b4 | -3.2767 | -53.84 | 2024-11-21 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 88e6bb26-165a-3012-82e5-4f51287b75d8 | -3.295 | -53.8597 | 2024-11-21 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f12fd83e-c0e4-3ba2-92b6-5479537ed91d | -3.2768 | -53.8199 | 2024-11-21 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 58a42104-caad-3876-9f3c-dfa01e9380a3 | -4.2575 | -46.1188 | 2024-11-21 04:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 41b86c8b-cfcd-3557-9ed3-2920d9b9f815 | -4.2388 | -46.1197 | 2024-11-21 04:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 151dc155-03e6-339f-9b15-f16a14d4dd50 | -8.25811 | -34.97991 | 2024-11-21 04:10:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bedbff19-f446-3610-acf7-30007e545dcf | -8.16706 | -43.82035 | 2024-11-21 04:10:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b18e0d3e-daa0-360a-9406-46cb2f481470 | -7.38906 | -42.77999 | 2024-11-21 04:10:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3de4d4e7-0f6f-3700-baae-bafb0c558dfc | -6.66633 | -47.10565 | 2024-11-21 04:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94255c7d-7111-3413-a573-c6ef40fbf3c1 | -10.12365 | -36.45651 | 2024-11-21 04:10:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cfcad0d5-c199-30b8-b088-8482e5a9b59a | -6.82564 | -46.7721 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a91322c6-283b-3aed-8815-9dcb250b5110 | -7.00674 | -46.35003 | 2024-11-21 04:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd356f72-a95d-3932-a23b-245d912367ec | -6.82751 | -46.77281 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17443686-5963-3b58-8cfb-50f5b93056d9 | -10.3886 | -44.46955 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcb83299-06fc-37c9-a39f-df4358077bb8 | -10.39541 | -44.47063 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57a6c16-5381-3795-a058-645bee3df394 | -10.3914 | -44.4738 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bca1833-700d-3d16-907f-7d1682097c26 | -10.39942 | -44.46748 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bab95dbd-fa57-3c39-8b8c-9493a46d48c6 | -10.70355 | -48.8122 | 2024-11-21 04:10:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14d315be-4046-3c22-86b0-eef43e5d7944 | -10.39601 | -44.46693 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccb74b77-a540-3c18-91a9-084e5cb428e5 | -8.74336 | -37.26263 | 2024-11-21 04:10:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7a0fc96-a898-3e25-abb8-dd907f623d3b | -7.01397 | -45.62067 | 2024-11-21 04:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ad170a21-564b-369a-9849-dc698a1b2935 | -6.82108 | -46.77493 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 39286695-c30d-381d-97e6-0b09cac70658 | -10.392 | -44.47009 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b670f24-b28e-3291-a5f9-b47bc90bb28f | -6.57547 | -47.86892 | 2024-11-21 04:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a8d9cd7-3d16-37ad-9821-f9c878d58967 | -12.8047 | -51.4934 | 2024-11-21 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 000f9702-c379-3b29-bf55-aa0d1749730c | -9.13006 | -43.10896 | 2024-11-21 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2f0c714d-981b-3636-b077-142c5dbc1fab | -6.82232 | -46.77916 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13c0768a-74e3-3866-b7b0-1b14c0c1dadf | -12.68676 | -52.40329 | 2024-11-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844538f3-657c-3bef-9f15-f743cb4b12c2 | -6.53546 | -44.43077 | 2024-11-21 04:10:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50647a20-8188-350a-b66a-63079ce98ef6 | -9.40677 | -43.31622 | 2024-11-21 04:10:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 73131ce7-784f-3c97-92ea-dd1d25b75db8 | -9.48731 | -46.12586 | 2024-11-21 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c47d5c5a-2801-31cb-b1e2-1eeec1340fc7 | -11.4608 | -48.01121 | 2024-11-21 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a1d6e4-df21-3369-8d10-8ea8049cfcd9 | -10.39321 | -44.46268 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13942a34-7876-32f6-bcd1-54a4783edf10 | -11.46142 | -48.00762 | 2024-11-21 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1020ad2f-7d33-3cde-b6f8-bb7228f0f425 | -11.87534 | -38.34676 | 2024-11-21 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b47373d5-6ad3-3203-be32-a6444e66ffef | -6.63756 | -47.34935 | 2024-11-21 04:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42c3f555-ed5f-375c-8fe3-21dce46cfb3b | -8.22181 | -41.01097 | 2024-11-21 04:10:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8ee76798-9acd-3b9b-a173-f21edbe01f76 | -6.63821 | -47.34552 | 2024-11-21 04:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68a5c248-2ccb-3311-b4af-8e096a2fe2b2 | -9.96477 | -36.07966 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| abe3fa4f-e818-3842-aae8-4624da78eb97 | -6.31593 | -49.67933 | 2024-11-21 04:10:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42957c5a-9c4c-3bd2-a33a-59f21f662c69 | -6.95336 | -47.84647 | 2024-11-21 04:10:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6c180b7-269a-382d-bb39-ee48e9887839 | -13.53439 | -42.97533 | 2024-11-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca894604-3605-3301-8603-9d9bb7e09ab4 | -9.35286 | -43.0983 | 2024-11-21 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48c1bd57-bdd3-3cf1-a103-0c0ab2a5d253 | -6.82691 | -46.77631 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3d990b5-8918-3cc7-b9fb-f2e44f3c28a4 | -7.39294 | -42.77701 | 2024-11-21 04:10:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f3c2fc7c-f3e4-37f6-baa6-b7aca5d5894e | -9.05797 | -40.53726 | 2024-11-21 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8a9f1c5-4cd1-3896-b7a9-ea26f3bfedfa | -8.52619 | -40.73459 | 2024-11-21 04:10:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 076bec5d-10d9-387f-b46c-3614d24480b7 | -10.69998 | -48.80735 | 2024-11-21 04:10:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c204ec64-09a6-3071-a45f-21fd4657ffdb | -9.19639 | -43.03335 | 2024-11-21 04:10:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec797d9f-a7eb-3705-8e97-4f0ca4c68733 | -6.31868 | -49.677 | 2024-11-21 04:10:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c496b612-5e71-31db-a369-22137fa5073a | -8.21204 | -40.94016 | 2024-11-21 04:10:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| db614eb4-b6f9-3afc-bb95-3d870a449a20 | -6.86693 | -44.75979 | 2024-11-21 04:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 624a9072-accc-3914-8c45-e032668e6b28 | -10.69927 | -48.81144 | 2024-11-21 04:10:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0cdcaaf-a560-399c-8850-dbdd343b7e3a | -9.96097 | -36.0745 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 064aba19-fc7a-383d-9a84-5ae5f83c9202 | -8.22516 | -41.01147 | 2024-11-21 04:10:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 913b6f4e-6a7b-3f1f-8bf2-d9d440010704 | -9.96158 | -36.07004 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 666999d5-472b-3c02-bb17-bdc6058ee59b | -7.47315 | -47.18125 | 2024-11-21 04:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3196848c-fb5d-3e31-9b20-da3ae2f881ac | -9.9692 | -36.08027 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| ff84023e-0568-3f36-bd25-18e73bf8f0c3 | -6.57387 | -46.75737 | 2024-11-21 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e9bff04-2222-37e7-9543-26f1641185be | -6.82507 | -46.77561 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a3a09199-3396-39a4-8e41-d740c0f9530d | -8.21485 | -40.94424 | 2024-11-21 04:10:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3aab73e4-14d4-349a-85c7-b3a9d6c00968 | -8.14742 | -43.7909 | 2024-11-21 04:10:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 85d8dc0e-a1f8-328b-9d0f-0e744511e68a | -8.8691 | -35.71691 | 2024-11-21 04:10:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 022b492c-88dd-3e53-a4c5-50b5ee40169f | -9.96538 | -36.07523 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 09557de6-f485-353b-b5ee-cb8844a32677 | -11.20601 | -37.41117 | 2024-11-21 04:10:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7cab985-8608-3679-9156-717dc3823682 | -7.43553 | -39.7681 | 2024-11-21 04:10:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60f94647-b89d-3e1a-a240-0f6debe82c09 | -6.11293 | -47.09741 | 2024-11-21 04:10:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58fff2ff-bed4-31be-99a0-171f153c3d87 | -10.38799 | -44.47326 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76d5464f-5ad3-3b12-b408-999537f51421 | -12.69201 | -52.40432 | 2024-11-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47116d6f-d585-334e-baf9-ba5ae22bd4df | -9.4101 | -43.31676 | 2024-11-21 04:10:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3fd07477-62fb-36a2-8ccc-1f8770bdc866 | -6.82292 | -46.77563 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db7200f2-b35e-3d4e-8cf7-ca72834bc3fe | -10.12423 | -36.45234 | 2024-11-21 04:10:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 860946ae-96f7-300c-af8e-bcdbb0a60fb1 | -10.3892 | -44.46584 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf9bd17-227e-3284-a48f-8a5e04821d9a | -9.9698 | -36.0759 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 3b802c68-1ba7-3d9d-b222-e937473a7389 | -6.99211 | -46.3177 | 2024-11-21 04:10:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8dbe58d-4ceb-3217-be0e-5691487f4c8a | -7.10047 | -46.71067 | 2024-11-21 04:10:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c560c7-1e49-3459-8fd3-016cbb31b9d8 | -6.86759 | -44.75572 | 2024-11-21 04:10:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5bf9778-f6ae-39ba-adcb-0d0e3c152a44 | -9.40733 | -43.31268 | 2024-11-21 04:10:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74584890-978c-3acf-a70f-a59a6d47f760 | -8.79714 | -40.75679 | 2024-11-21 04:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3cc9604-ce6e-3531-912e-8f632915a37f | -7.40512 | -42.76459 | 2024-11-21 04:10:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5ea14d7a-9358-37fc-ae39-cd695f2c7081 | -6.81992 | -46.782 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a94e293c-a9b2-3cc9-bb4a-9299c2f1e560 | -10.39661 | -44.46324 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fa98893-21e4-3f0b-91f5-676d263bda2f | -10.66109 | -48.1084 | 2024-11-21 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b27d5fd-b19c-3883-a174-e95eaa5ea5d0 | -7.00761 | -46.35252 | 2024-11-21 04:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b51a8b90-0944-3a82-86fd-6f22d2ed31f7 | -9.966 | -36.07077 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 60f8e3f8-b1b5-337d-ba23-0e425b8e848c | -13.21565 | -48.32764 | 2024-11-21 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 179f8443-ae3e-3cfb-80b2-79f1ac4abd72 | -8.33724 | -43.90029 | 2024-11-21 04:10:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d123426-395f-36c6-9932-db8f1c8d6083 | -9.97311 | -36.07932 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b55c3716-db4a-3a59-8224-5dc43c94793b | -7.49963 | -42.87655 | 2024-11-21 04:10:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a0a442d2-37ad-304f-b9f8-11d6010b00ee | -6.82352 | -46.77212 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ac28066b-db11-3c8d-b8e1-f375c13acbae | -8.66302 | -36.97575 | 2024-11-21 04:10:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bff60ffe-46b0-38f9-a8a8-25d461d6fcdf | -10.45751 | -40.38157 | 2024-11-21 04:10:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README23.md)
