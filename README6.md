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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9670d18-f368-303e-b437-1ecfc03b4b1a | -6.77715 | -55.4881 | 2025-05-07 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14ca92da-40ae-3158-9d8d-c9f668ecd8cc | -7.91836 | -61.54667 | 2025-05-07 05:16:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 359f63fa-4413-3b39-8c06-53c36ad1351b | -6.71273 | -47.5921 | 2025-05-07 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f09dac24-a05f-3f63-a940-f274595624bd | -6.71313 | -47.59193 | 2025-05-07 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e820279a-d87d-3422-9c36-885977d35c6f | -5.41246 | -49.08203 | 2025-05-07 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dcf9574-dbee-3c27-a439-b31c9ed941c8 | -5.16235 | -45.10569 | 2025-05-07 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 961b0d62-df03-3dd1-9bc2-65b0f9a613f9 | -8.23956 | -49.73709 | 2025-05-07 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2f478dd-a734-314a-9944-f0d84def120d | -7.56332 | -45.83841 | 2025-05-07 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d7d8fc4-df02-35ee-b3b7-444749186ffe | -9.27149 | -47.90427 | 2025-05-07 05:16:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a722b3c9-e8e2-3301-ab9f-f3abc114da52 | -5.16144 | -45.11244 | 2025-05-07 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 582e337d-3733-3254-8526-431f6b63674a | -8.23907 | -49.74072 | 2025-05-07 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 792146e0-0708-37bc-8260-e1a3aceeb9b8 | -11.7753 | -48.7105 | 2025-05-07 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34043eaf-11a9-3038-b423-71cdc3755ac5 | -11.78234 | -48.70245 | 2025-05-07 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ff0a0d8-09d8-3897-932f-1813664bde50 | -11.62678 | -54.94015 | 2025-05-07 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130da39b-b3dc-336f-b691-f22928d78a4f | -13.5001 | -52.95611 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f49e40c0-f4d4-31b4-9b97-d95eecb40180 | -11.39329 | -52.939 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dc35f8e6-2dca-3305-a704-c39a47922517 | -11.39265 | -52.94388 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e557ad5c-03f2-35a2-a482-f22944c09344 | -13.13363 | -53.24987 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e85904d1-f461-3bf4-bbc5-2ba642d02c54 | -13.04939 | -53.71413 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a0a562-8ffe-3ab1-9a1f-53f6e83eb388 | -13.04759 | -53.72784 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ea1aecf-bad2-3579-bf27-c8b9f06ea5fb | -11.39791 | -52.93962 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b32cc494-b8df-33a4-ae53-9b2e171ae579 | -10.23588 | -59.23935 | 2025-05-07 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4afa105c-2a34-36ee-af1b-d915d794702d | -12.49871 | -55.73886 | 2025-05-07 05:18:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a351e373-e0ff-345c-b711-014dc8e39aa1 | -13.5042 | -52.96203 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d3681aa-c4de-31a8-8d5f-692ac901095c | -11.27788 | -52.47243 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 986a676c-6580-3f34-b462-84a18a363679 | -9.93256 | -65.01954 | 2025-05-07 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0072b543-d896-32d6-baac-a5b65676bce6 | -13.50381 | -52.95581 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0fc4ff6-0dd6-31d2-a3e3-414f1c5ead83 | -9.93598 | -65.02393 | 2025-05-07 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb317c1a-1b20-310f-b6ca-ef37efb4b453 | -12.33503 | -55.16129 | 2025-05-07 05:18:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfdee8e-7e45-3768-af10-59b726a1a16b | -12.65044 | -54.08535 | 2025-05-07 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff9368a-2411-3b3f-a25a-bbc39619f8d1 | -13.05328 | -53.71925 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 013dbbf3-a67c-32bd-90b7-8719704f5092 | -11.39202 | -52.94873 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7aef0089-1fc5-320c-a8f2-060bf51ccead | -11.77566 | -48.70647 | 2025-05-07 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 214bc748-0c2d-3c97-bae2-a39aa1ca48f3 | -11.26294 | -52.4756 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f928aff8-3495-3d69-9976-7946e86b8b92 | -13.04311 | -53.72727 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d66663df-8ee3-3016-a0d3-97ffbd01c382 | -12.55726 | -57.75689 | 2025-05-07 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd72238-97e6-33f0-91f8-783bdb671c4b | -12.33552 | -55.15773 | 2025-05-07 05:18:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b9419f-4002-33d2-8593-7bb34681c23e | -15.22417 | -51.55601 | 2025-05-07 05:18:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d438ca5-2df7-3bd7-b343-d4b3474c4cd6 | -12.1734 | -54.23544 | 2025-05-07 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c8f6edc1-8eeb-3eb2-bc15-6a0869e05dc1 | -14.68864 | -53.39035 | 2025-05-07 05:18:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39ec761f-7804-3279-991d-381177e8a08f | -12.55668 | -57.76086 | 2025-05-07 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d66058bf-98e2-3cb2-8c63-f70800bbaabd | -9.92877 | -65.01823 | 2025-05-07 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8067808f-f6c5-38ac-a0c8-40d88c3034b6 | -13.04819 | -53.72328 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84c1bcf6-1df0-38a0-9cd6-be0de92d0a68 | -9.16267 | -61.9538 | 2025-05-07 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4409464-c6fe-3403-b11e-dd9f31ff73ff | -11.25754 | -52.47993 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 331bc6b2-3dd7-3f26-bb50-95263f59168d | -13.37353 | -54.2524 | 2025-05-07 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d97af687-c012-3268-bb5a-5b70185978fb | -12.01262 | -62.83817 | 2025-05-07 05:18:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88075e49-bc30-38e7-a627-6128a4f0ae61 | -11.80388 | -57.3677 | 2025-05-07 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13b9b9fa-da40-3293-b690-0da48e66b678 | -11.39663 | -52.94936 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dbecc98c-9f04-33db-b9d0-5a058752bcaa | -12.08712 | -54.58503 | 2025-05-07 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1475190e-6caf-3b9f-b41a-a3f6d329dd55 | -13.05 | -53.70952 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda57c33-e63e-3378-95e9-4eadb85f54cb | -12.651 | -54.08111 | 2025-05-07 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3d86f2a-3a71-3c5f-9a68-aba87434aefe | -11.38868 | -52.93836 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1df3968a-328b-3048-a958-3dac50f44247 | -11.80448 | -57.36366 | 2025-05-07 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b4c2450-8d0b-3f00-9123-a2ea684781d4 | -9.9363 | -65.02334 | 2025-05-07 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc7efcdf-c8e4-3e3d-b032-d757993f9cea | -13.04879 | -53.7187 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 548f6f25-0195-3c32-8930-f4186d8df6a4 | -13.05207 | -53.72839 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31671edd-f203-335f-ba79-1f19fd1eca47 | -11.49208 | -60.98748 | 2025-05-07 05:18:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d84a4475-3c92-3f61-8ac6-3db77f8870f7 | -12.55318 | -57.76032 | 2025-05-07 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b3346472-d33c-3199-8540-5091999676d0 | -13.50485 | -52.95676 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f63b28a-8cfd-3535-be3c-8ca82ee855f1 | -13.50312 | -52.96106 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f755b5ea-98cb-3b4c-8bb5-aff0682fc684 | -13.05268 | -53.72382 | 2025-05-07 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9359273-cc88-3978-99b0-518215b7d113 | -11.39726 | -52.94453 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5f5a2110-22f9-37f2-b7d6-0abe85a3c1df | -11.77587 | -48.70573 | 2025-05-07 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a63e65c6-9a63-3828-93ca-7946742de366 | -12.17712 | -54.2402 | 2025-05-07 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90909d63-828f-31c3-9c49-2817ffc737d7 | -9.08429 | -63.69963 | 2025-05-07 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5eb5bb6-63b0-36ce-8380-e5d1f2f400b9 | -12.64944 | -54.05935 | 2025-05-07 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61395306-3c16-3289-b8b4-8d58547f38ff | -15.07893 | -48.94492 | 2025-05-07 05:18:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa4c35a2-798d-35bd-8489-6034f4a9836b | -12.36966 | -52.485 | 2025-05-07 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6bafb78-8325-3757-be36-df812669242e | -11.27312 | -52.47183 | 2025-05-07 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61202986-0f35-34c5-952f-fef409d15649 | -13.49839 | -52.96037 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 534042d6-cc18-37cc-ba29-dfe24a7ed813 | -14.688 | -53.39554 | 2025-05-07 05:18:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0cc1bb5-efda-341a-bcb4-ceb73e81104a | -13.48741 | -60.3737 | 2025-05-07 05:18:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97471445-cc89-3d1e-83c3-7e0fc3c07241 | -12.17285 | -54.23959 | 2025-05-07 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b29e91cb-4f65-343e-bcef-5d3892ed6dcd | -13.49946 | -52.96131 | 2025-05-07 05:18:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5e46e79-3281-38c5-9dac-0ae00cc8d749 | -11.79964 | -47.37869 | 2025-05-07 05:18:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e108da47-5ede-3628-8308-1e4cbaa22c20 | -11.3963 | -52.9477 | 2025-05-07 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 035f8b8b-7cd8-3a82-b09f-0c3f7035af3e | -16.65617 | -55.7473 | 2025-05-07 05:21:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3a23d4d7-e0b7-3a93-8340-c2283fd471ef | -18.2669 | -52.99955 | 2025-05-07 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32121f71-0535-3a3e-91bf-c4d4a3795293 | -18.42286 | -54.70575 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 870e510f-d2ce-35b8-9f9a-f226ea2387bb | -18.41987 | -54.70764 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5b8a462-b08e-3d85-93a6-60adc7b607d6 | -18.41933 | -54.71241 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a276353-a501-3764-8f5e-2022716c38a1 | -20.72366 | -54.40731 | 2025-05-07 05:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7658ec-6c5a-33e9-a2e0-d69f3424b1ca | -19.05929 | -54.37015 | 2025-05-07 05:21:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cceeb051-3de2-3af2-9938-d6ad83aa377d | -20.56594 | -54.06612 | 2025-05-07 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b4a7774-8649-32dc-bad7-d88408fa3b0b | -20.56532 | -54.07196 | 2025-05-07 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d55034c-db6d-30ff-8030-ca76b969f7c1 | -16.65255 | -55.74287 | 2025-05-07 05:21:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 32aacb17-f459-3d0d-a628-361ca2cc7760 | -18.41878 | -54.71721 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a89790fe-da04-3bf1-ae29-50dc044f6662 | -18.4172 | -54.71455 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56df72ad-6c8e-34bf-b634-26b7647fc5a7 | -20.71889 | -54.4068 | 2025-05-07 05:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35d34f0-cb70-3fcc-adc8-6d9ead3c0702 | -20.27563 | -54.63945 | 2025-05-07 05:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 493151eb-10b2-310e-8643-66ade4dd30af | -20.72296 | -54.40662 | 2025-05-07 05:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56773cf9-435c-39b4-84a7-0aa6bbc38e44 | -18.42383 | -54.71318 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55da4f3a-6e1d-31f0-aa6e-496cdb953d29 | -17.62731 | -50.91741 | 2025-05-07 05:21:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a7d720a-224c-3c1b-a4b3-8976d7d13dd1 | -17.14996 | -54.00496 | 2025-05-07 05:21:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7e428aa-857e-39c4-8fa7-8092fbfd8439 | -18.42437 | -54.7084 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 400987f6-c200-3fb3-ac55-70f998baf4e3 | -20.27676 | -54.62917 | 2025-05-07 05:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e302978-7cf4-35dd-a359-16a52c83687c | -16.65205 | -55.7467 | 2025-05-07 05:21:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 57e7c958-d04c-3b46-a8e0-4b5581ed4df0 | -18.4217 | -54.71527 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9013b2fc-ebd7-3cc4-9eb6-d8a2a827321c | -18.41778 | -54.70978 | 2025-05-07 05:21:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
