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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47aacca4-579d-33d2-8615-95fcc9fd29fe | -9.92433 | -47.72955 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d3b4cc1-4294-3997-91f0-978ba3f83369 | -9.73333 | -48.28777 | 2024-10-14 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04d75859-fda0-3129-857b-f6ad13d4d6e7 | -9.72981 | -48.28707 | 2024-10-14 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b26d03bf-73a4-3bb3-960e-188ffdaa3d8a | -9.64306 | -47.68828 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90cbe165-a558-33fb-8d5f-4be2caec077d | -9.56836 | -47.6962 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7c09e3e-0820-3c09-9f1b-8995fe31f290 | -9.5649 | -47.69562 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18a461fa-dd0f-3e6a-be35-41db6ddfd9a4 | -9.53879 | -47.61658 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e810c5d6-d9f9-3049-a39c-9e834617457b | -9.53816 | -47.62039 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 584a9fa1-1588-3f3f-b66c-99ff5d6e4cea | -9.53694 | -47.80193 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1d682a2-4539-3585-99c0-022139240f88 | -9.53558 | -48.01433 | 2024-10-14 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9127110f-8eee-30b3-8c47-ea46cf63e8b9 | -9.53534 | -47.61601 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97ba8241-0ba6-3d70-a32a-8d60073c47a8 | -9.53472 | -47.61981 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eddf9ac4-9fa0-3f4d-b7ca-e011218385d2 | -9.53455 | -48.01497 | 2024-10-14 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40bf7b13-a03b-3fbe-829b-8d64bfb94779 | -9.53127 | -47.61923 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03ebb9ec-f4b6-3181-8acc-6c544205661a | -9.52776 | -47.83633 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f48da39a-a8d1-3c7d-93e5-6d205bf55f60 | -9.52427 | -47.83579 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20943150-6be6-32cd-9e5f-6b34dbe420d6 | -9.50303 | -48.67208 | 2024-10-14 04:21:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b5d5ed4-d9cf-3a1b-b171-869aaaae8cb0 | -9.50275 | -47.83634 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc70426c-e7a5-3b80-bf8a-3f62ccf2893e | -9.50211 | -47.84023 | 2024-10-14 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcdeca80-6e0b-3f4b-b244-a8d3941fbc03 | -10.05307 | -48.06491 | 2024-10-14 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 97161be3-b430-323a-b938-e2f6127bd349 | -10.47441 | -47.87015 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74b4cbbc-9197-3e3d-9b61-12bfaffdcad2 | -10.47097 | -47.8695 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 433fe91f-3ab5-39fd-a0aa-7b95220cf326 | -10.46816 | -47.86503 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c80fbb52-2bcc-36a9-a117-f1d176167392 | -10.46753 | -47.86888 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 813ed984-ba89-3825-8176-4be6bc4b6df8 | -10.46689 | -47.87275 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c9ce170-e59e-3474-8240-6ae5af1a8c47 | -10.46408 | -47.86828 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 683853d7-db9a-3ae8-9c5b-1393e7ff33b8 | -10.46344 | -47.87214 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c1772b-5a6b-37e1-8e4e-a669903f82f4 | -10.46062 | -47.86772 | 2024-10-14 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2056f0bb-42cf-338d-910f-2c92dd4819b1 | -10.80042 | -49.07272 | 2024-10-14 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08bd5253-23c4-38a0-957f-e1223a50795e | -12.63236 | -49.17824 | 2024-10-14 04:21:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0c3ac12-517a-3473-9b5b-4d356a3c5a8f | -7.96518 | -49.06103 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 06300809-1abc-3824-a1b5-7a0d7273b257 | -7.9644 | -49.0656 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 68ff4f94-018f-35b7-a43b-3ac20372cb0c | -7.96218 | -49.05581 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8373f9f0-3d72-3ee6-8dbe-a40d4cc7f6cd | -7.96141 | -49.06042 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 664f4991-4bad-3bd8-8a67-f3e68e5a97d4 | -7.96063 | -49.06499 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d427ebe-08cf-3db8-9034-f514c4f62a86 | -7.95986 | -49.06957 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 52269017-fede-33ef-af30-79f9718ba914 | -7.95763 | -49.0598 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3657047e-4aea-3a52-87df-b0952af8511b | -7.95686 | -49.06439 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47397c61-e895-3931-a9af-1e51b00790a6 | -7.95608 | -49.06899 | 2024-10-14 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf000ab8-ef52-3858-94f4-4e9602a388f9 | -7.8734 | -49.79242 | 2024-10-14 04:21:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7bbe23f-a7c6-3213-a9b7-d327e1376eea | -7.7305 | -49.89692 | 2024-10-14 04:21:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18903182-06fa-353f-b367-fb526251119a | -8.06416 | -49.3992 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f87163a3-c7a5-3ebc-8344-a00fb6a88eda | -8.02884 | -49.63453 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c806ab0-aa54-3382-a294-a0a2c115d5ca | -8.028 | -49.63952 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff6843ba-43e6-3e8e-8a6a-180cf49d3be6 | -8.02494 | -49.63391 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84599578-42a3-3508-a162-799e1ed5ec1c | -8.0241 | -49.63887 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bfde4aa-ecb8-3996-9605-7a70ce66d5bf | -7.95168 | -49.39768 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbb79c2a-e140-3105-9285-0a7d3f897299 | -9.16151 | -49.82911 | 2024-10-14 04:21:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8441300b-b795-3ccc-aaff-a5ae09e18599 | -8.89197 | -50.13172 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5eb2a2f-6892-3394-8372-5c75b666b1c8 | -8.88801 | -50.13101 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3a38ca-988e-326c-8ae9-0dd21d7e88b1 | -8.73847 | -49.921 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06dc5915-7f27-3c4b-89ba-1c040ed4ed38 | -8.65708 | -49.926 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a2182e6-82d1-3efd-82f9-0860424e3946 | -8.65314 | -49.92533 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bee13723-522c-3a11-b65c-89b527c2aa9d | -8.63911 | -48.69568 | 2024-10-14 04:21:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0f9a166-0d61-3ac1-a8b0-26d3c605eadf | -8.35748 | -49.36343 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07d1142b-1883-3356-9a0b-4f196e2b1212 | -8.33587 | -49.96904 | 2024-10-14 04:21:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfc75633-79d7-3b83-b7b4-5168cb72dbd5 | -8.26062 | -49.50237 | 2024-10-14 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80f56f16-6b0d-3993-9244-65379adaab4f | -8.18278 | -49.94128 | 2024-10-14 04:21:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dda4a46-e661-33b1-bcfd-a19931d7cb60 | -9.9089 | -49.14337 | 2024-10-14 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71970852-4751-3074-b42c-3cc04eaaf2b2 | -9.77711 | -50.09798 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8806a5ae-65d2-353b-a6ff-50b0530df41e | -9.75455 | -50.13551 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b818b47-3717-3bd6-bd4d-b49539088c25 | -9.73888 | -50.13282 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ff911ba-c952-3e44-b7dc-3282926a11b9 | -9.64113 | -48.94905 | 2024-10-14 04:21:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21fadb99-b1b9-3c88-be5b-2ed40aa4b4c6 | -9.62426 | -48.98209 | 2024-10-14 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e432175-4361-34fc-bb62-906285a8aac9 | -9.62352 | -48.98652 | 2024-10-14 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66f99192-8dd4-3594-bde8-8eacacff7081 | -9.62059 | -48.98148 | 2024-10-14 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a48cd2a7-f5ea-3ac0-8286-8512698c2265 | -10.539 | -49.93954 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0acdeb46-6554-39fa-8a76-414380b1f2fd | -10.52734 | -49.78325 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0533d436-015d-3f96-ab27-97ccc7515e19 | -10.52655 | -49.78796 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f9dcbf25-2e17-381a-bfca-e180a1d1e794 | -10.52576 | -49.79268 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b871f79f-5b37-311c-9bd1-1081e737dc95 | -10.52497 | -49.79739 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 36bb8ff0-5aea-3a35-b3f4-5bf30fd23076 | -10.52355 | -49.7826 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0320150-be50-39de-8ed8-286237b7ba8c | -10.52276 | -49.7873 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d1cb8ddd-65d1-3804-804d-12324feb4e22 | -10.52197 | -49.79202 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e65ee41f-0dbf-3e38-a992-7748eebead14 | -10.52117 | -49.79674 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12681590-6abc-398a-a901-c63241c70920 | -10.51976 | -49.78194 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83d43ea2-488d-3822-acd4-8c80e958e409 | -10.51897 | -49.78665 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 055ae990-f3ac-3d02-8a58-9a9cd17991c0 | -10.51817 | -49.79137 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d59f8a5-6f52-38c1-a569-b3eefd51f5fa | -10.51738 | -49.79608 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e415fddf-337b-311a-9127-965772834381 | -10.51597 | -49.78128 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e895510-f552-336d-8f8c-5c23580de3f5 | -10.51517 | -49.78599 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10053077-c531-3b10-a352-01cee450347e | -10.51438 | -49.79071 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c878a4e0-79dc-3b86-beb5-ece80e3f5bd9 | -10.48316 | -49.9521 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1036289-fe02-3f67-9537-aedb2ee8fa10 | -10.47851 | -49.95626 | 2024-10-14 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31cd79f7-acc5-3059-85bb-dc945db6f5a7 | -10.47213 | -50.55921 | 2024-10-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20a1b455-fc99-3fd5-a86d-9b73a23b8d49 | -12.10228 | -50.76801 | 2024-10-14 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e3ed247-38ed-3061-afef-e76b27343479 | -11.55349 | -50.72184 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf7860fc-7373-3da7-ba5e-0ea36cd23c8b | -11.54954 | -50.72113 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 990a176e-4196-3cc7-9ffb-9eabeca159b4 | -11.54865 | -50.72631 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 25b3684f-9bbe-3ca4-904c-de6b99b03c94 | -11.54559 | -50.72042 | 2024-10-14 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 616fbb6c-9cb3-31d1-84c3-83cba12467b0 | -13.62818 | -50.62747 | 2024-10-14 04:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0ba3783-0085-37b3-9f2d-10f6d2dd8ec6 | -7.78847 | -50.2202 | 2024-10-14 04:21:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f23d621-4a2e-3b40-a6cf-1793a046f666 | -7.78786 | -50.22382 | 2024-10-14 04:21:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99ee016-79e0-3d8e-8c70-a4e6f9e15991 | -7.76418 | -50.56221 | 2024-10-14 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11fc1af1-549f-320f-bb9a-c4a8878feabe | -7.76353 | -50.56605 | 2024-10-14 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfcbebaf-9a19-3ab2-8a3b-98fc30640802 | -9.16869 | -51.49357 | 2024-10-14 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0517f794-579e-3466-86dd-8a7fb7f540d3 | -8.90724 | -50.62633 | 2024-10-14 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3302cdc-6cfe-387c-8c7a-15b26a7b154f | -9.49054 | -50.97866 | 2024-10-14 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0cc526c-7aed-342b-b239-cc00674a84bb | -10.82326 | -51.1427 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ddfcff2-4a27-3b08-a2ea-651b8c728a6e | -10.82045 | -51.13451 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
