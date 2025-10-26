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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ecfe905-5d33-3f9d-bccc-2a8bb52e2118 | -9.21974 | -51.52182 | 2025-10-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e1a0c58-4b2f-3cf0-81ac-65117a82fae6 | -10.89845 | -48.02623 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 710d4706-27db-3270-a658-cfa0cd65452e | -9.26069 | -45.5961 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5aa84029-8cc6-3570-950a-a9b6531bef24 | -11.32664 | -53.93203 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6f21bac-89d3-333b-a613-493d044e0ed5 | -13.88974 | -48.46176 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a80b7b5-15dd-3d44-b43f-c174d7128efd | -8.33394 | -49.31098 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf2549c-e0a0-3df7-9662-e5584b41f5c5 | -13.33145 | -47.91937 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e79286af-3e27-306b-8ed6-a0cb5a8ddcd0 | -10.97418 | -52.02805 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6cf35dd-2f20-3cd7-9b40-bb3921c898ca | -7.61429 | -46.6735 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f4d3431-6ec2-356b-8566-9f9c8319a6ca | -13.3152 | -46.77739 | 2025-10-26 04:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 519e2b74-f0ba-3e09-828b-676a98716903 | -13.87716 | -48.39328 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f40712ec-7b71-3591-8b32-c9b27c77c830 | -10.95025 | -47.57747 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4658b2b4-256b-39fe-a28f-2d9f8f68e99f | -9.26495 | -46.41636 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 010d593f-e6a7-3452-b6c8-88d2939f1987 | -7.77889 | -45.38326 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6708bc42-ca9c-3fe2-8e0d-0b2ff63fde30 | -12.16851 | -47.00332 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0de0dc7f-32e2-3251-bce0-a23c2d1db5b0 | -7.48925 | -46.97028 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15924ae3-58ed-3db8-84dd-9b38f967b37c | -11.32719 | -53.92853 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6ce6444-0348-397a-a4ae-5299da4dcee1 | -8.72341 | -48.00689 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79cf8050-1e38-3bcd-9333-4ab5169009a4 | -13.00291 | -43.81247 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffb6a6b9-c935-3fcf-9028-3ebf48c5807c | -9.68898 | -56.48731 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 427dfe21-a1bc-3d25-ab3c-985bc57c7e29 | -10.22645 | -49.86768 | 2025-10-26 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc34dcdc-63e4-3380-8ad9-c975a438a714 | -9.44798 | -56.65047 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcb3dbf8-baaf-3819-9c70-f511e082e172 | -12.42136 | -57.80569 | 2025-10-26 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c34e9c2-09d5-3b54-a084-45be7ad26507 | -10.79481 | -56.03846 | 2025-10-26 04:51:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4b499a-f3b7-3444-b8d8-c4765ab09e4a | -12.89162 | -54.73209 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68fa836c-cdcf-3005-aa1b-569945180b77 | -8.32958 | -49.31489 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fabf00f0-a76c-3e0e-9d51-35f69d032a33 | -10.89989 | -48.02801 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cb4aa08-8e0e-330d-855d-b44d4c2a504b | -14.51237 | -43.00409 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8e97a48b-3351-3896-a028-7ad7c4c6cb85 | -6.77424 | -55.4846 | 2025-10-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62472ae6-851a-3665-86f7-b85d69074abe | -11.02754 | -47.86676 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1445363d-74ff-347c-a976-8cbaa9fa5663 | -10.84321 | -48.8184 | 2025-10-26 04:51:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dab702d8-38a5-3077-bccb-971f0188a73a | -8.12409 | -47.03629 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9c549e1-67dd-327c-a2c4-ec52f153d2fd | -8.13285 | -47.03201 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97f15be4-b5fe-35c4-9cec-f0d39721bf00 | -12.41763 | -57.80505 | 2025-10-26 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c3446b-d1ee-357e-886f-f21f702a7248 | -10.4889 | -55.61586 | 2025-10-26 04:51:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0a9b0c1-13ef-355f-af28-5254bd6c9fcb | -10.99104 | -44.86446 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 211e67a5-0793-3cef-b9d4-cc1d61abc660 | -9.27087 | -45.5928 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9345556a-cd73-3bc5-82cf-d0eaa527742d | -9.31519 | -43.09698 | 2025-10-26 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9eed6fa0-956a-3748-bc78-f8aa2545ebce | -14.51119 | -43.004 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 2d75a392-fca7-3740-96b6-d5d8c9c6e002 | -10.59529 | -63.46693 | 2025-10-26 04:51:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67c76e61-af1f-3eab-ad07-5466e895b731 | -11.26821 | -54.81547 | 2025-10-26 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26b1294d-f5b9-3d37-b607-e9d15d891369 | -9.60331 | -50.78919 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91d07e87-abb6-37ec-817d-2a328a01b631 | -9.31567 | -43.09316 | 2025-10-26 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 133ef836-292b-376e-a5e8-dd811bf08f4d | -10.89525 | -48.03091 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb279225-b571-3c97-ba97-3ac43ab18cd8 | -10.88882 | -47.95628 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26a035af-c79f-3571-8d72-5a24da0d7fa9 | -13.87927 | -48.47662 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 703a7b67-143a-3325-ae62-25ef797b3216 | -10.90399 | -48.02882 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9028e156-92b4-39df-952c-a99793538090 | -10.59584 | -49.17585 | 2025-10-26 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11207717-5f03-3447-a7b6-b40c34956710 | -12.13631 | -47.00333 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4e3c02b-59fb-3203-af11-c0c67ea50b54 | -11.45685 | -46.08901 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a14b3c2d-2b12-33f9-bc18-ff73d82b93fa | -9.72657 | -54.61815 | 2025-10-26 04:51:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb74801-2baa-30e4-bed6-83970dad3fc6 | -13.23256 | -47.74886 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f798816-8b2c-3e5b-8f65-fd59139b9cfe | -11.95925 | -55.26022 | 2025-10-26 04:51:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccbefb2b-6694-3c7e-93db-c9b3b075751b | -14.1721 | -47.30672 | 2025-10-26 04:51:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 952d0078-1577-3f15-8b8b-aae44333d56d | -11.84792 | -49.86321 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcc966f8-fa8a-3a26-906b-903ef1c0c4e9 | -10.338 | -48.12074 | 2025-10-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c722e007-d840-3d5b-9760-6884b286ff07 | -9.73125 | -55.01898 | 2025-10-26 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 832fd1fd-118e-3869-8fd2-6cf20a4039f4 | -12.86085 | -48.65424 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e6c05e3-1302-38ec-aa49-aeba1c419983 | -7.80062 | -45.41195 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff2ba685-bc3a-3d2c-b4ff-b4de6704131a | -10.90669 | -48.02776 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70aa7cf4-2e25-3861-bbf4-2e4ccfd15edb | -7.69696 | -42.1853 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 819c7ebb-ddab-3901-bccf-cd15ef2b1bd9 | -13.53669 | -49.55311 | 2025-10-26 04:51:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3fd0bb59-9165-30a6-b7c0-3afaab03983e | -9.43642 | -46.33284 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe7db839-ea4b-3a2c-82d7-dbb98349cd26 | -13.53489 | -49.5371 | 2025-10-26 04:51:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05111518-4dd0-3998-9875-a8620b718c9e | -9.05076 | -46.98548 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5354676c-1225-30ea-8159-c34a95a09be6 | -9.18357 | -57.68875 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 255896be-77bd-313f-9f98-e175be1b486d | -11.06196 | -48.3222 | 2025-10-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c00bc4d3-e305-37c8-a1d0-b38c07b7c688 | -10.75486 | -49.78534 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 006b6f7c-6333-3222-af8f-0ba7bad85273 | -7.88211 | -45.71196 | 2025-10-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b6307ea-1367-308e-98a2-d52803e8e954 | -9.68312 | -47.4371 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92149166-5e07-3c86-aa48-70ed6bd97289 | -12.2412 | -47.02309 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| adfaef12-8033-338d-892a-5259e8bd1e86 | -8.23917 | -49.76982 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6723bac4-1f3d-3479-8384-1ff332e95a84 | -10.83729 | -50.59746 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2de2d8b2-64bc-3bc7-b660-acd99c85c1e0 | -8.33748 | -48.17789 | 2025-10-26 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ba7bffa-3422-3a72-847b-356a9f533506 | -10.48608 | -55.61148 | 2025-10-26 04:51:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57356d8f-672d-3481-9bf6-8f3fe8e21919 | -7.79569 | -43.16087 | 2025-10-26 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6701b8b1-e9f0-3491-9b21-ba402c1b77aa | -7.84804 | -46.42442 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99055588-9c1e-36d3-b0af-64ce4b750a03 | -12.29759 | -47.48896 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fbf6de5-d1ee-36e0-b424-b9aff4169c79 | -8.20728 | -46.93587 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33453e79-2f3d-31f8-aac7-e5765dc595f1 | -8.61034 | -54.65377 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de377c1-6bda-3400-942c-4e13a0a48962 | -7.69598 | -42.18414 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e6203e36-462a-3ad6-b840-8258c78201aa | -11.56341 | -54.52311 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02ebc156-4c19-3272-bc9c-9e1f344ef3f6 | -13.41059 | -43.55443 | 2025-10-26 04:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffd66c26-e560-3a3d-a72f-841f2a6b63f3 | -10.19146 | -44.90625 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0bb77fc-27a0-3937-9ce2-3893d28a5f3c | -12.0443 | -54.23688 | 2025-10-26 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 509e63b5-f162-32ed-b05d-fd5086b70a90 | -7.99839 | -47.92297 | 2025-10-26 04:51:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6274ac13-17a1-36ea-901e-9e5b7c8a1993 | -11.84856 | -49.85864 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f1aa780-ac64-38e5-a9ef-345a2a172740 | -8.7783 | -48.37455 | 2025-10-26 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c305cc78-ac56-3f4d-87bc-f6bc65569a7d | -10.88757 | -48.0255 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fc2d922-b137-3a0e-886c-ebea0be2449a | -9.16104 | -51.30589 | 2025-10-26 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e4567d5-cf70-35ad-a598-305f323a8a15 | -11.55733 | -54.51848 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cccee39-cb0b-3f1d-ac26-3268826b1527 | -12.31071 | -47.45703 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d64f9d2b-7c1d-3ef2-978c-f1810190ec88 | -13.26632 | -54.38742 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8ce34bd-8098-3b18-8f57-54e277e5d600 | -9.44576 | -56.64121 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d7f5f7b6-63fd-3500-89cf-f5b4297cbabe | -12.30632 | -47.45647 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8224715-ef0a-3b67-aebb-c0b3002556d6 | -9.44212 | -56.64061 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b2b839f-09ab-3487-a467-a98bc2d686ef | -10.2147 | -52.66486 | 2025-10-26 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f38cfd5-1e49-380d-b355-718c48d3eb27 | -13.53418 | -49.54235 | 2025-10-26 04:51:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 434b6e33-9f1a-3255-adc6-0256dfb32240 | -10.98871 | -44.86449 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2dd62b1-9140-360b-82d3-da6b1cb23cf7 | -9.26542 | -45.59702 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README43.md)
