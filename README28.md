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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aebdd236-0d85-30e6-89ac-3e2a88a776e2 | -8.78323 | -49.63855 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c60f4e27-8cd4-3cf0-b13c-35d28ab4f0ab | -8.56195 | -49.61292 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| f5b6db73-ba7f-3a32-88c9-798f8368454a | -8.56113 | -49.62262 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 528bbfc2-65ae-3299-9548-e335eb4546de | -8.55863 | -49.60687 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 0edcfe09-f400-378b-9e03-077410cba965 | -8.55043 | -49.61477 | 2024-09-27 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a9fb3788-b7d4-3b99-8a92-7d89f7a70d89 | -9.58879 | -50.15081 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6c819fcc-2d3e-3934-8c7e-630a1a79cd17 | -9.58663 | -50.13697 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 42b91d5b-9036-3956-b2c2-c2d8f607bd22 | -9.54942 | -50.20597 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fd3965c4-ce93-3296-a833-9f2f31b5ef9e | -9.54734 | -50.19222 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 63add8aa-2cc1-3e1a-98c8-81bcd2a3ba7a | -9.61048 | -50.14732 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d5319915-8de8-3c8c-afd6-72f69e6c48d1 | -9.60177 | -50.1629 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aa24ef90-2752-3b4d-bd39-54985539be78 | -9.59964 | -50.14908 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6a54486f-407b-3c7f-aaee-66703d839244 | -9.53861 | -50.20771 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ac8a6301-3a26-3450-af11-9777980a9d26 | -10.63504 | -49.90866 | 2024-09-27 01:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 33609409-50da-3d0e-b47b-b2bbddcf12ac | -10.1533 | -50.00923 | 2024-09-27 01:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6e3cde27-beb3-3e2c-8d0d-6f33280f9c80 | -10.14244 | -50.01098 | 2024-09-27 01:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 3530d776-e059-3129-8e50-6cd0cb44533f | -10.12071 | -50.01449 | 2024-09-27 01:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 00bb6433-df5e-38ed-b180-47d80bf4d5ad | -12.19819 | -50.7913 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5f555ef2-62ff-3dcd-af52-3283c01c0d85 | -12.19703 | -50.85036 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e4ed144a-7eed-38df-912e-a67a927749f3 | -12.19643 | -50.77975 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 76d61b8d-5c27-3ee6-bc49-061ec472f543 | -12.19177 | -50.81594 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| a77fb653-a064-35e6-998e-84af8854e5f8 | -12.19001 | -50.80443 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 2eb21f6d-a625-344a-b1f7-5db58412fb65 | -12.18825 | -50.7929 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| c015185d-96f3-345d-b16a-bf6bb38ddcf7 | -12.18008 | -50.80602 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f88b3fb1-8ef5-3c24-abe7-2c58574c8790 | -12.17015 | -50.80762 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| f0d5997b-3130-35cb-a6a5-1844fe8251d0 | -12.16838 | -50.79609 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 805fc73b-53fb-30ca-a435-d498213ddfcd | -11.17079 | -49.72707 | 2024-09-27 01:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9f8048c4-3bf1-3d4e-b8fd-e256a18d1bbb | -11.16902 | -49.73393 | 2024-09-27 01:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a1a6c15a-dfbc-3ed8-a35f-89c7fd371e39 | -11.15989 | -49.72885 | 2024-09-27 01:24:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8419d599-c380-37a9-938f-f76b6da95853 | -11.02074 | -50.18744 | 2024-09-27 01:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fa8b3988-4525-31f1-8187-d36af90b1703 | -11.01018 | -50.18916 | 2024-09-27 01:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3a0ba70-a3d3-374e-880d-8f95a33d03eb | -10.9976 | -50.17775 | 2024-09-27 01:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95648aba-7883-31a5-b434-2b3a3db2f4df | -10.94909 | -50.14511 | 2024-09-27 01:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3c893574-a30b-36d2-8d53-1c704105679f | -12.47893 | -50.41882 | 2024-09-27 01:24:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2caa182c-b679-3f64-bc5e-4251b4299b4c | -12.20813 | -50.7897 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1b34b82f-bbea-3db2-a800-8f7a8aea3898 | -3.32163 | -50.30928 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| de0818f8-4ce4-33f3-812b-f278a048a828 | -2.79612 | -50.27724 | 2024-09-27 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5f816a7e-2822-3557-87bb-7dc881348f5a | -2.80824 | -50.27544 | 2024-09-27 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 116d45eb-c420-3975-9cf7-a8b05262ffdd | -2.79846 | -49.58992 | 2024-09-27 01:24:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1653a1d6-2f68-38b0-b476-5d7d6d131840 | -3.56827 | -50.58066 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e4774cd1-eccc-301e-8655-abb3ad5c1f72 | -3.56645 | -50.59081 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f71af53e-e487-327e-b6c5-e8c8e7cf31df | -3.56403 | -50.5747 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 18019cec-8ca7-33a6-818a-8cc0617dda2e | -4.5062 | -50.11473 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c9240b6a-68f9-3ad2-ab1b-5fdaa1efff8f | -4.49821 | -50.10451 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| de32e303-26c3-309b-8ff7-2e087ca736cc | -3.57266 | -50.39047 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ca20e3b6-7acd-3169-a6de-323bbf1b3b3e | -3.55835 | -50.37568 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| aa94c456-f8ac-3995-b705-2b3f56e74b51 | -5.31709 | -50.4513 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dc52ed81-3168-3b8c-ab1c-c9058a6fc88c | -5.78768 | -49.83323 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 09e0ac2a-72f0-3549-bc4f-9cf9650e668c | -6.20408 | -50.91288 | 2024-09-27 01:24:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5d17fdbf-62b0-36c0-9d34-5f0810df2cf8 | -6.1299 | -50.95884 | 2024-09-27 01:24:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7fb7cc7f-3647-3bd4-aa25-67b316dbce20 | -6.12919 | -51.13114 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 31deaf16-e950-3a0c-9ae0-c6c3a5a35f2b | -6.12722 | -51.11752 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 295f876b-ca20-3d7a-ad36-97123355cf38 | -6.12221 | -51.1263 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b0cda36e-73cb-3bf3-a441-259b1cc07227 | -6.12115 | -50.97419 | 2024-09-27 01:24:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ea39cdee-711d-3d65-85b7-e24e61eb941e | -6.11911 | -50.96067 | 2024-09-27 01:24:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aca515f5-0eec-3527-96b0-739079bed747 | -6.11843 | -51.13224 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fa4bf04a-fa12-37f0-9fb7-f18062139785 | -6.11659 | -51.11955 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0a9f1221-85cc-3534-8a3b-510a2e48fb17 | -6.11654 | -51.01672 | 2024-09-27 01:24:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9eac1c43-bdc7-32cf-a087-7b0f52aa60af | -6.10577 | -51.12033 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 802a4afb-23cf-35a0-a64a-1a2a1ad62251 | -6.09802 | -51.06725 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3729043f-e608-3453-9502-05dacb9993e6 | -5.77357 | -51.03904 | 2024-09-27 01:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 25d3a0e5-886c-361f-ae63-e7c7eb041cb3 | -6.5651 | -51.11483 | 2024-09-27 01:24:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2884e76d-93e8-31eb-86ce-6f0b87c0ea70 | -9.33326 | -50.74606 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 227377ea-cdb3-31ba-9005-d981d79dfbb6 | -9.33128 | -50.73304 | 2024-09-27 01:24:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6acf1209-0b24-3b3e-8702-76a084874a67 | -8.75999 | -50.75392 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 0875c1a1-f178-3b19-823c-040db2f67117 | -8.03018 | -50.43865 | 2024-09-27 01:24:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2923bae5-8117-31b0-8bba-77fae28d20ae | -9.04244 | -51.19316 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 32792bdd-4fde-334b-ba59-eea351502bd2 | -9.46119 | -51.46158 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4fbdcd4-4653-3b5b-a5fa-e4edb64587b2 | -9.45298 | -51.47446 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b5e4c889-1e1a-3c79-845a-288a23f76c6f | -9.45131 | -51.46323 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d11f41ef-089b-3fbe-a71f-97a7462f18b5 | -9.43995 | -51.5226 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6e9a9611-faed-3257-a621-7179133649a8 | -9.4199 | -51.45653 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c7bb43cf-3374-3c8f-a1d4-97af33edd6bc | -9.44141 | -51.46476 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f2f937b1-945c-3121-9d8e-19ccaf7319d1 | -9.4315 | -51.46624 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 72bfabf2-1886-3d53-837a-bd66e7a2795b | -9.42161 | -51.46786 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f7bc9e8e-7208-3e42-81b0-dd67c9ad2377 | -9.41818 | -51.44508 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 963f14b0-bbe6-3a7f-91d6-a2033b897aab | -9.41345 | -51.48089 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14fa1246-63a1-3688-8d25-cd86c96bbe2a | -9.41002 | -51.45821 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 526e3a73-cc71-35c9-b465-3127245bc781 | -9.40828 | -51.44677 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7a705bb3-f7b3-3eaf-9176-c0447be487b9 | -9.40653 | -51.43517 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 105d48d0-b4a6-3a81-8d7b-532716bfc4f2 | -10.72923 | -51.10577 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 361a0fb9-2fdb-34de-974b-1f4a312bb9bc | -10.72875 | -51.09996 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| aec01e06-fa06-3989-b696-163142f61f01 | -10.72753 | -51.09424 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 265a00df-2ca6-3345-a2ee-a1b500911fd2 | -10.72698 | -51.08844 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 84ca0252-ba32-35fc-89b4-3e5e713286e0 | -10.72583 | -51.08269 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a7222383-bc7c-377f-960a-765cbe18eeb3 | -10.71587 | -51.08427 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 470a710e-ff49-3c08-9120-dccce7a0bc77 | -10.62014 | -51.1296 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 92527f29-7886-3a8e-ba3f-22e51db447d3 | -10.61842 | -51.11806 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 422ab019-9976-3640-941e-e56dfa1debfc | -10.6167 | -51.10648 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 37949670-543d-3ce6-b3c8-e7469987e34d | -10.60846 | -51.11963 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c8940f6-5c8d-3772-9395-422c86ed31f0 | -10.60674 | -51.10807 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c0a1e61-7dbb-3cf3-886c-f04abaa63f13 | -10.55515 | -51.10451 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 49a99f14-1c70-36e5-a68c-0845fdfdf4f9 | -10.54519 | -51.10613 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e9bbaeeb-0f09-3032-8b71-6269c56f6b34 | -10.53594 | -51.11384 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3e76f9b2-2ef6-347c-905a-93b74d72357f | -8.62585 | -63.13749 | 2024-09-27 01:24:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 9aee7a50-f785-3463-9998-9a3feefac0f2 | -8.13141 | -61.35292 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bb71d6e9-0c1a-38f7-bd0c-fd2302e564d5 | -8.13662 | -61.29081 | 2024-09-27 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a551c705-6da3-3d74-a50f-1ba893586143 | -9.09853 | -61.35833 | 2024-09-27 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 03e54691-445f-3a1d-b172-ce0250c11f97 | -9.10634 | -61.32943 | 2024-09-27 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 332e513a-0419-3c1c-a6b0-2ab928d15a92 | -9.11145 | -61.37143 | 2024-09-27 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |


[Clique aqui para ver as próximas entradas](README29.md)
