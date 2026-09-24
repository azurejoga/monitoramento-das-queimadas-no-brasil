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
| 40020f26-4c3c-378a-a608-abcfda170d1a | -14.754 | -46.2184 | 2026-09-24 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9e51a181-1ac9-375e-8a2d-dd875a53ff85 | -6.7703 | -48.6792 | 2026-09-24 00:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e4e36976-b311-3f9a-82ef-e6bf0ac68013 | -10.0917 | -46.0458 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 7900e1bc-0aae-33a5-9d7e-12c20090f689 | -10.2827 | -49.9606 | 2026-09-24 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 48a3320e-c48c-32e5-8a0b-d8c1bd23e6fb | -10.111 | -46.0209 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6c83f130-e623-35c6-80b0-ce3f2dd1614d | -6.4486 | -59.9717 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 81dffb65-42f4-37c4-a543-8f8bda73cb51 | -3.4393 | -50.0685 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 708eeafb-e21d-3cbd-8536-57dd1ae8431e | -9.8677 | -48.5126 | 2026-09-24 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| def0b4e4-7e83-30df-ae5f-7acc738ba7ed | -9.2412 | -47.3708 | 2026-09-24 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 4ffcbed9-f784-3c49-8423-e8e8df6961d1 | -5.6016 | -60.1919 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 485b47d9-31de-345b-b4a2-bc4c915aeaca | -11.9586 | -50.7393 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f98b27b5-93cc-394f-a2b5-f1fe5541de04 | -4.1181 | -51.0695 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 39d0ead6-e9e6-371f-a369-2aca9ceb3038 | -9.8491 | -48.4927 | 2026-09-24 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c9a49e77-7bfd-342a-b4ba-ae310aa809a8 | -10.0921 | -46.0232 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f7549709-cb3c-319e-a37a-a8ca22eec9de | -6.4303 | -59.9532 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 9ca3ddd3-a178-35cb-98e7-4f0d0899dc1b | -12.0727 | -50.7474 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8d5331f0-8640-364f-aa54-1cb82a2d9db7 | -9.868 | -48.4907 | 2026-09-24 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 6500c7c5-39dd-3746-8a70-853887d83371 | -8.4538 | -48.6944 | 2026-09-24 00:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2608e9c8-523d-3559-97d2-a1177921b413 | -9.0267 | -61.6626 | 2026-09-24 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e190ce47-e85d-3722-83b2-80a24bc40581 | -9.2409 | -47.393 | 2026-09-24 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 18bb53de-1470-3d08-87fe-5129ae246a83 | -6.5962 | -59.9279 | 2026-09-24 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5452d71e-23ab-39da-bd63-1f1a84e9b04e | -4.118 | -51.0903 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f92c1110-7627-394b-8f07-95ecf748c00e | -11.9771 | -50.7799 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 207.7 |
| de069790-7ac6-36b4-9670-15fac319f37a | -10.1114 | -45.9982 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 24170626-f7f3-3d1f-b101-995d8c1dedde | -6.3317 | -57.7725 | 2026-09-24 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 98e1fca8-5b91-3ff0-9c7b-435684624a01 | -11.9774 | -50.7585 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 75ee70ef-9516-382a-822c-0227ca330553 | -6.3501 | -57.7717 | 2026-09-24 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 40285ac4-d52a-3c72-a127-064cdc4daaaf | -6.6146 | -59.9272 | 2026-09-24 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 142.6 |
| bb3dbf2b-1abd-34a8-b250-7a69930cc14b | -3.4578 | -50.0679 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 07d02b7a-9887-366a-8949-fe7ff05ba9f2 | -14.7344 | -46.2219 | 2026-09-24 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 69d74dda-074b-3b7d-98e4-a8306aab87f3 | -11.958 | -50.7821 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 471.0 |
| 2584511b-6ab7-3d27-a906-0e6a5175cea6 | -6.6331 | -59.9265 | 2026-09-24 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| dd02c944-7cab-3a1c-8c52-20d70e00875b | -8.0092 | -71.3073 | 2026-09-24 00:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 05978c5a-7e52-3caf-96ef-b4fd7276afd5 | -6.4487 | -59.9526 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 57c41a5b-e6ae-3e47-97fe-d996a85f90de | -10.2637 | -49.9626 | 2026-09-24 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6b0b4a24-092c-35d7-b8ce-f51bf0cbd4dd | -6.633 | -59.9457 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f502149e-258a-3655-a21a-c0722b144c2a | -8.3527 | -62.8112 | 2026-09-24 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| cabc91a9-b2a7-3082-b4be-4d65ac5f8ad3 | -3.4577 | -50.089 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 2675612d-dd98-3b66-a963-b099591cd313 | -3.4392 | -50.0896 | 2026-09-24 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f5a86622-689a-3449-89be-35da87f536c8 | -6.4302 | -59.9724 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 28acdff8-c128-3d7a-b1a0-79ca9df3074d | -5.1058 | -60.2639 | 2026-09-24 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1f259cc7-a0ad-38e4-9a57-5998bfae5e06 | -5.7754 | -45.1053 | 2026-09-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 79da1f5d-5fcb-33b5-8a66-827aaa480088 | -10.0924 | -46.0005 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 96273b1a-d902-366b-98e6-bbbfe20b605b | -10.9115 | -53.9429 | 2026-09-24 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 6951decf-a0be-3d7c-8197-4b5d3fadb171 | -11.9583 | -50.7607 | 2026-09-24 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 531.6 |
| c10acf9d-7261-30a4-83fb-ceff743cc1f2 | -6.6148 | -59.908 | 2026-09-24 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a7be3dd2-dac6-351b-81ad-f014556a275e | -7.5141 | -70.3992 | 2026-09-24 00:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a3268081-10da-375a-a276-7ee500ef4359 | -3.1454 | -54.6059 | 2026-09-24 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d8d57aca-97f1-391f-bd65-fea91934d09f | -9.8488 | -48.5146 | 2026-09-24 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1ce46927-a2d6-3b5b-854c-ecd9b794c2a6 | -1.6217 | -54.9135 | 2026-09-24 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e356943a-f494-3e3d-9ded-d488fc9ac2ab | -4.6679 | -45.9632 | 2026-09-24 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 67f12773-1856-381b-a65d-0b359db695f6 | -6.789 | -48.6779 | 2026-09-24 00:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 89.9 |
| fa2cbd63-aad2-3f76-868d-6f21b1a0c4ba | -11.247 | -51.3706 | 2026-09-24 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a3851be7-3a0c-36e5-8de9-ca8ab5b1d753 | -4.6678 | -45.9855 | 2026-09-24 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9d6a823f-0be8-3dc6-8e4a-53fc5711c31d | -5.7756 | -45.0826 | 2026-09-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0fc7594c-9574-39a9-a17b-34d716e0a497 | -8.0275 | -71.3619 | 2026-09-24 00:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cf518b0d-ecb5-3c09-8d14-eb4f9620de9f | -6.6145 | -59.9464 | 2026-09-24 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a8de3c91-d40d-3019-a880-41079d3c5ee0 | -10.1107 | -46.0435 | 2026-09-24 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 34001973-fd48-3014-b390-49a0e75c742d | -15.5686 | -42.3547 | 2026-09-24 00:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e4b3aa86-cd67-38ef-ba34-3687837acba9 | -9.0158 | -60.5138 | 2026-09-24 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2dd13bab-bff7-30a6-be62-345d8ba60412 | -9.0453 | -61.6618 | 2026-09-24 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 4dc1a7bc-44e3-3669-a4d6-12e6329b3649 | -3.1637 | -54.6054 | 2026-09-24 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 92a7f2f5-b5dd-314a-9cd6-594591a16034 | -10.2827 | -49.9606 | 2026-09-24 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7b6b87d3-8dd7-3c86-a408-58fd85c623ed | -13.2061 | -51.549 | 2026-09-24 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 518c477d-9b56-3bf9-a926-11a376b68fc4 | -9.0158 | -60.5138 | 2026-09-24 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a875cd17-1505-32ad-9483-587c10c4cc6d | -6.4303 | -59.9532 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 03baedda-366d-3325-b965-86977c516008 | -4.2951 | -49.1234 | 2026-09-24 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 17b8786d-d704-3621-b21e-bfc08a565872 | -10.1114 | -45.9982 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 23e74b2f-3a46-3278-ab44-8b63bcf2e25f | -3.6765 | -60.5459 | 2026-09-24 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| cb8e9e26-144b-365f-8d26-a5c0d4127e5b | -3.4577 | -50.089 | 2026-09-24 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b12074b3-0f6e-3382-9440-d70bc13dd86d | -4.1181 | -51.0695 | 2026-09-24 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bec8116d-c832-38ee-a4dc-5affb9148fb2 | -3.6947 | -60.5645 | 2026-09-24 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| da779d6c-e802-3a43-a035-30277aaafbb8 | -3.5654 | -43.4727 | 2026-09-24 00:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| d8844d8e-1867-3c77-a1fa-8fc2764bb872 | -6.633 | -59.9457 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 9256e546-507e-390d-a137-9c0678106472 | -7.8996 | -61.1772 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 8e142aa6-8842-3aa7-8923-5e469bdaa1be | -17.4424 | -39.9298 | 2026-09-24 00:10:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| b737f68f-132f-3549-85cd-c7926c6421ec | -6.7703 | -48.6792 | 2026-09-24 00:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4e1cc834-c5a4-3b57-9644-b771c1d6e50f | -13.2253 | -51.5466 | 2026-09-24 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 73c383a7-c69d-3908-bef5-e443c1472503 | -5.6016 | -60.1919 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a9f1ae02-2a59-3c0f-b9cc-9f216c67cd34 | -9.8488 | -48.5146 | 2026-09-24 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 54a87651-0a82-3f19-88ea-dee13d2dc216 | -3.1637 | -54.6054 | 2026-09-24 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| e64c8ddd-a7fb-339d-88e2-fde7b7cd939e | -12.4216 | -46.9551 | 2026-09-24 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a25ca3d1-1d64-3a24-9be2-6f5ea66f22b6 | -15.2511 | -43.2743 | 2026-09-24 00:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 109.2 |
| d9ef378e-f236-306f-a131-75553838597b | -6.6145 | -59.9464 | 2026-09-24 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ad577264-3da7-34ce-ab25-b0b388dd30c9 | -6.3501 | -57.7717 | 2026-09-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5d0e75d1-c107-36f3-b3fa-4995d12e1f8b | -8.3527 | -62.8112 | 2026-09-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 0b29f2a7-4379-352e-afc3-87e446a69777 | -10.9112 | -53.9635 | 2026-09-24 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d3ac2caf-eee2-314a-a295-bf5f99e7212e | -10.0914 | -46.0684 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f706819c-1c6f-34a5-b873-ed04047481bc | -3.9169 | -59.6641 | 2026-09-24 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d469b7ce-6598-3bac-baaf-477528383b42 | -6.3317 | -57.7725 | 2026-09-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a45e33a8-0019-350d-8d71-bae8bb25597a | -15.2314 | -43.2784 | 2026-09-24 00:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 102.9 |
| e4289469-d3a2-3557-a642-657454a8254a | -9.8677 | -48.5126 | 2026-09-24 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3ca70b26-cbdf-364e-b725-645d068f83e4 | -6.6146 | -59.9272 | 2026-09-24 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 1d1285de-b704-3bf5-b764-49e00302e77c | -4.118 | -51.0903 | 2026-09-24 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 50e66921-9c2c-3cd9-957e-4a35ee02adc0 | -9.868 | -48.4907 | 2026-09-24 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 9dbe6c63-4cd0-3c80-96e5-426b6327af3f | -11.9771 | -50.7799 | 2026-09-24 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 2d3a320e-d771-3f74-b633-59b5e05a5ec4 | -9.5721 | -40.3475 | 2026-09-24 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 1972d1f6-7822-3515-86bc-b70641181708 | -8.4538 | -48.6944 | 2026-09-24 00:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3a8432ed-a45f-389e-8545-f8857dc72840 | -11.9774 | -50.7585 | 2026-09-24 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 176.9 |
| bb9fdcd3-c7e2-3e06-8001-2b9436799ba5 | -6.4486 | -59.9717 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |


[Clique aqui para ver as próximas entradas](README2.md)
