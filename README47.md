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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 555b26ec-b0a2-36e4-aa23-2e613d645b7b | -15.53417 | -45.21689 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| db8654d0-ad19-3451-87d3-b498a0d48880 | -10.90709 | -46.52589 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ac136e7-3883-3d2a-842f-9de66324ee25 | -9.77062 | -47.7515 | 2025-10-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faac4ec9-0401-338b-b06d-5fbc6ecffe5e | -13.36362 | -48.14044 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1efe5aad-8836-3e0d-b22e-f0dee619db39 | -17.38877 | -47.15794 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fee823c-4e9e-3eed-95aa-6ddede3231e8 | -11.27082 | -47.21115 | 2025-10-01 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e58ae2c-9caf-3f61-9518-4142e65c8004 | -10.66836 | -48.54845 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5c7089e-2daa-3f91-bdf9-a9b7e04475b6 | -14.56126 | -48.2347 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d087f7dc-32e4-3842-83c3-9d0257786d67 | -13.06099 | -47.06639 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f3c23d-0762-3800-9e12-ded334178709 | -12.00139 | -46.64383 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f8a8848-ef14-31ac-8bdf-ee1a217fe271 | -13.93585 | -48.10194 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70143155-3891-31f3-ad60-9df71fe281cd | -17.40694 | -47.14998 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a274d35e-4731-3166-89be-d8570d019fc3 | -11.69843 | -45.36184 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9377864b-41a6-3439-95a3-2a865a0eea36 | -10.43749 | -50.86517 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7412cb54-cea6-3fde-80cc-ab833b685ab4 | -10.80877 | -45.35257 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 804d6fc0-ed5a-3772-bfe7-905285370a6c | -17.39207 | -47.1585 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b341a5-feff-3dd3-9a55-e99d83582c57 | -12.15094 | -47.76991 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1539e9d-023c-31e2-85bd-2a552bdbf2ee | -10.12881 | -45.67527 | 2025-10-01 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d486876-1f74-3fb6-9404-78bb1c823873 | -14.34926 | -45.90268 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 873cd671-0b02-3793-9fb8-4d7fce523a53 | -11.99437 | -46.58116 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4414a2bb-9933-360d-ad55-240e9aa82835 | -12.67077 | -46.86705 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b86ea65a-d280-34a5-851f-a6281c46578e | -14.35756 | -45.91498 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026d9152-666d-371a-ab50-abb1f66a6b1f | -16.02387 | -50.9053 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cd8b08c-6774-3009-8c2a-ffa4a2ed81a1 | -14.63029 | -46.98162 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0d7f07b-dff9-39dd-943b-5ecf3f0d336b | -15.28658 | -47.83787 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b9ded76-1c24-3eeb-8bd7-c901e1f44c50 | -12.95967 | -48.43435 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3aa9e4a-f895-31a3-a177-0eaf42277917 | -13.33071 | -47.84451 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72867fb6-7963-3564-9aed-39c15863ebd5 | -12.70554 | -46.88348 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a5f33d6-7447-3362-8a48-b1e2bb2a7308 | -15.21811 | -48.17518 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 164f9444-81a6-3b5a-8feb-bdc66ce51782 | -14.68886 | -45.27564 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63fb2933-5909-3b3f-8d93-b7524cb876de | -16.76216 | -51.34249 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55b359ec-585e-3cad-85e3-03cbe5de2111 | -16.20957 | -48.28049 | 2025-10-01 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa79d00b-4b04-3730-b5a4-387ef47c487c | -11.82089 | -44.98566 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ccda46d-9a29-35ae-83bb-667e6a52d97d | -13.24693 | -47.30988 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4e9dde2-0745-3cfb-845e-ad02f89a0d6b | -10.48385 | -55.62337 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4fe60c6-ff79-309b-b619-e29945a5e5fb | -15.47466 | -45.87717 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f18c8fb-9083-3bd6-934c-0a1683256503 | -10.95718 | -44.32022 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82d2415b-64c8-3274-bb6b-b0c3ba737f3b | -14.52569 | -48.3666 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 889db504-3608-3673-b278-b50f2b9ca4ac | -15.17038 | -49.10121 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1978cbb3-6598-3446-b509-d86db8e0c246 | -11.46705 | -45.01005 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02abcd14-ef64-3789-a9da-95f5e6ecafd9 | -14.71651 | -48.14237 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8a4850a-a90e-317c-ab82-0b1932a4641d | -13.33464 | -48.14701 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c859b2-c7e6-3a12-80ef-e945ba1e7313 | -13.41676 | -48.19945 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73ae8d25-ef80-354c-8073-3355ebe23b0a | -13.13168 | -47.43104 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ec7baf1-4550-32ed-95e8-e2b2a1256167 | -9.42773 | -54.71536 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff80993-4606-3ff7-b2e1-91386e6e1aa2 | -13.30406 | -50.66769 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56265de7-7b61-3680-be26-03f1d8499c42 | -13.02937 | -48.6779 | 2025-10-01 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 018f3c2e-0e32-303f-9854-08a12ebfbd23 | -13.36454 | -48.15602 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3731e8-6d68-3bf0-b06c-31009e63301d | -11.45612 | -43.51492 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13ee4d14-13f3-35b5-95f3-0de495a6578e | -13.33865 | -48.14383 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12066fae-d569-3501-9d73-a639994bf2be | -14.00658 | -45.0041 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 853d9b2a-f2a0-34b2-b076-234e9626a4e3 | -11.43592 | -44.94712 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1777e09b-6b96-3be0-be2b-d3a5306d7b38 | -15.31082 | -46.41312 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2023185e-0f3b-38a0-93f9-513a4cf2bca4 | -15.2447 | -46.96705 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b1d6f7-e2be-332d-8456-c1f5c03b8777 | -14.01806 | -53.8887 | 2025-10-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9e2cf41-a92b-30e0-8c53-d684a89dc68c | -11.68621 | -46.84946 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52cb1e5d-271f-3154-a962-8b69331b69f6 | -15.48352 | -45.8637 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25c13c9f-082e-345a-a506-f66f0c97e47d | -14.58389 | -46.36332 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6825a49e-1626-385c-9812-a6ee19fdbf9d | -13.59177 | -48.03683 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 525a6704-d164-37a0-8b0e-164c188890e5 | -11.7536 | -46.83194 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfad4119-76b9-3ad6-ac42-b7152599c6b1 | -12.04089 | -47.90493 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e165fe97-ddf2-3a1d-a426-d83475e5f457 | -13.53763 | -47.25864 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2c143a0-ba5b-3daa-9dde-e603e23a81dd | -11.75634 | -46.83609 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef0e65ff-6b35-3ba5-95dc-6f6c6c19abf3 | -14.49635 | -48.43868 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 42817aed-a0ce-333a-be16-f5f889512cc3 | -12.24833 | -47.79797 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abfc3898-0630-3fa3-85be-4ca30967a44c | -14.79671 | -45.79874 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f62b6e87-88c0-3ece-ac9e-45208ce4e7f0 | -16.00263 | -50.87294 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee2b6131-5b48-3987-a91d-fa2d31b76c4b | -14.70487 | -48.129 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39777367-a251-331e-abd1-9b16b2e883fa | -17.41129 | -47.16547 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86e1c258-fbc7-322f-9025-a1d0586ada76 | -13.21021 | -47.32586 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96934622-8e20-3c90-9cf5-3374c8c80b19 | -12.87399 | -46.91469 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af76b62e-0629-349f-925b-f86773627519 | -14.68673 | -48.24023 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98cc9d29-bda5-3564-863d-bcdac9eba219 | -15.84478 | -46.25847 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7ed3e65-24ec-3140-b3bb-222b6f577a16 | -14.3581 | -45.91143 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0a606a1-72a7-3d29-a106-4145d039d7fe | -13.82481 | -47.50574 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7d75a84-8662-3320-adb6-29bcac157364 | -14.05683 | -45.02649 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56e3be50-f039-3933-a2c4-a37994059a7a | -13.96256 | -44.90625 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ccdd4fa2-0327-3b7a-ba04-95003742424a | -13.67449 | -48.06969 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cdd30a5-2368-36e4-82ae-f462341f33ed | -15.28925 | -46.20105 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33256725-b70c-38a9-bd42-33b3eb2d867e | -14.72379 | -48.14005 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6e64d78-6ae8-3a59-a489-4767c18f5a28 | -11.81424 | -44.98463 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4861abb-c67c-377f-a4cc-4bf18e5a3259 | -14.98821 | -50.7717 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89be1662-df7a-3140-98e8-00b4712b3c3a | -18.33311 | -41.80254 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a61b3e6f-fa08-34b4-aa57-f551d70a0aff | -15.46691 | -45.88332 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b23f4c4-9b4a-3427-9514-b32982bde588 | -13.56247 | -47.27377 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a39e21f-8854-36ee-9fe0-e18282996965 | -11.8431 | -44.99644 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50062263-a7aa-3585-8a70-c8efbedbe2e6 | -14.52897 | -53.11939 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9af085ee-cce5-31c8-8285-4d2ec50b7ef1 | -10.79447 | -45.35747 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a254c86a-fa2f-3960-8ea3-86227bd474fe | -14.8508 | -48.33666 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2e45f45-3f00-3991-953a-1ab5b449f9aa | -12.85705 | -47.02151 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30eae4e1-57ca-30ea-badf-152fe572935e | -14.50654 | -48.44036 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ed00876-5dd6-301c-8570-336a6e0f6ba5 | -11.84032 | -44.99233 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e54abf-09e8-33b2-bbf1-29b0685fe372 | -16.83011 | -45.3694 | 2025-10-01 04:21:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30020f99-c74e-357b-8eae-454ba287928a | -16.36588 | -49.12688 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acfd7eac-3288-3d0d-8932-98a0b9eea88d | -14.75806 | -45.76273 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d0b5797-85d6-3515-b174-bf990c8340b1 | -12.48771 | -46.84029 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0982d717-e30a-3d75-b213-b786410b653f | -12.95129 | -46.42469 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5970f7b1-db7c-3b8c-8681-737839fa72cf | -11.3808 | -45.06223 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46f50a7b-0f6e-3d99-baae-fc0bcddca583 | -15.14601 | -48.39494 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| caed394d-4847-3974-83d7-03b405967ac9 | -12.78525 | -46.87473 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README48.md)
