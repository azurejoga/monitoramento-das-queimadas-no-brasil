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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5efb907-32d5-3b8e-a679-d7ebbd1ba805 | -3.6215 | -60.566 | 2026-09-02 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 1bcc8e24-d53a-3f3e-97bf-5ae7d573597c | -12.1453 | -44.2195 | 2026-09-02 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7e77f3ad-3c9b-30dc-a816-4617fb87aa78 | -7.2006 | -60.6706 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 1547a967-b728-339c-ab79-0c36913f2d3f | -12.1312 | -47.1309 | 2026-09-02 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 3342c944-ef27-304c-989d-69bbb752037a | -1.4752 | -54.8157 | 2026-09-02 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1fcc3fc6-d9e8-3ba0-a52e-99a7d692128e | -12.3814 | -48.1655 | 2026-09-02 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 10df5eec-b92f-32ca-8492-6f29fb142d42 | -7.3487 | -60.5883 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| dbe269a9-2c37-3c0c-9c18-ab076425441f | -10.3193 | -50.0425 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9567d22f-a07f-3d77-a47f-4aee2cd3a262 | -11.0244 | -49.6872 | 2026-09-02 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e9cd78bb-0b8e-329d-9c20-1b7f2d5f856b | -9.0244 | -65.4367 | 2026-09-02 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cd1b16c0-52ed-3844-bcf3-13fdc6474be7 | -10.3382 | -50.0405 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0be091c5-6949-3601-a2ba-ecf2c2b8cb44 | -3.0347 | -61.4846 | 2026-09-02 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 08525cfc-76a3-3188-b113-5677c820b52c | -11.1126 | -51.5114 | 2026-09-02 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 866a59dd-cc99-3d2b-b7e7-bfaf6cef689a | -7.0427 | -59.2366 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2a7cc189-d9d6-3446-8fb9-7ac4bfa49d75 | -6.3722 | -51.7693 | 2026-09-02 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 07410cd6-7f89-3db3-ab9d-f61204960ac6 | -13.9855 | -58.672 | 2026-09-02 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 101d63af-ced3-3a2c-9efe-effb25a7f61a | -11.5479 | -45.4676 | 2026-09-02 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 6380fc2d-a436-3cfb-87a3-01f37532202a | -13.5724 | -59.7362 | 2026-09-02 15:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 96a5a591-d0d9-33a1-b12f-045497e377c1 | -11.8386 | -51.1365 | 2026-09-02 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1d9d8875-03be-30bd-bd77-21348e4570fe | -4.9788 | -55.8417 | 2026-09-02 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6cda81dc-82c7-314d-a72e-06edd20c64b1 | -9.043 | -65.4175 | 2026-09-02 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 89d8bd21-65bd-33d8-87a1-423db9905a94 | -3.8446 | -59.3977 | 2026-09-02 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5f364fe0-a321-302e-b99f-31745ccd842d | -3.6216 | -60.547 | 2026-09-02 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 921d04e8-10d1-3982-a165-a52a58b00b2e | -7.2005 | -60.6897 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| f9bc3afc-e131-3c9f-bf0b-76ffacfbdeed | -3.2361 | -61.2359 | 2026-09-02 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2e3023be-6b87-35ee-862c-c115eded0d45 | -6.6542 | -59.426 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| af06739b-b3ad-3b4a-b656-0df6b6e3a2a0 | -9.4538 | -45.6228 | 2026-09-02 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f315ea2f-42e5-3c46-8794-023d0957bf37 | -12.1457 | -44.196 | 2026-09-02 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 610.1 |
| 1a5b3389-7a0e-3068-aaa7-c1f300f87f9d | -13.6236 | -51.8158 | 2026-09-02 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 73e80dfa-dbed-3ed6-8f3f-c80c499fbc63 | -14.6145 | -53.59 | 2026-09-02 15:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ac76a50c-956b-32c6-a960-a7da7e31c3ee | -10.3388 | -49.9977 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ac95aaa8-fab0-3f7d-8be2-9f20c3ad96aa | -8.3717 | -62.716 | 2026-09-02 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f2e445f3-2ebf-3bcc-93b4-83b863c1464a | -6.7123 | -58.9412 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 761696dd-3bed-30ea-909d-791f083ffcfa | -6.6883 | -59.9436 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b68f3af0-7e76-3bbe-96ae-c8ff7d2da65b | -7.6602 | -45.8539 | 2026-09-02 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 2211f5a0-a8b1-3b74-9f26-986a2556105e | -12.0933 | -47.1138 | 2026-09-02 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 5037b056-346d-3c04-9e69-ddb7626fb50c | -13.9853 | -58.6919 | 2026-09-02 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 51015d6a-31f5-3b3d-84e0-ad7066f0cfdc | -10.4145 | -49.9898 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 520.8 |
| b6f5eef2-9e19-3500-b20c-8576158b1826 | -8.4046 | -44.9869 | 2026-09-02 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 15a959b2-4d9d-3097-9081-185576184b73 | -7.0242 | -59.2374 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 07d8d597-af9c-3a42-acab-aa6a13bec11a | -3.3452 | -42.8067 | 2026-09-02 15:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 264.6 |
| d2222514-83f8-3f6f-b8a8-89c3a228466f | -9.0058 | -65.4373 | 2026-09-02 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 16bd7e3c-7c98-3104-83d0-a3be7f7b6a9d | -3.8263 | -59.3982 | 2026-09-02 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9c8de0ca-566f-3b3a-9da6-d33a9d67e084 | -7.2933 | -60.5905 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ed4417c1-0caf-352e-8daf-20591905d56c | -15.3852 | -53.7652 | 2026-09-02 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 34b3dfe8-bfd4-3ffd-9d97-41222c092eb7 | -6.7451 | -59.6533 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 680563f1-ae9c-3f70-9b3b-36211bf43cad | -12.1128 | -47.0886 | 2026-09-02 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 36dfbb19-b5d3-31ad-927b-a3a460dac9c8 | -13.5531 | -59.7574 | 2026-09-02 15:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2583125f-238b-3e93-85e4-68098d419a5d | -15.3841 | -53.8282 | 2026-09-02 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4b4b31ef-ea32-3e49-83f2-e3afdf9627f2 | -6.8756 | -59.4171 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d4d9bd8c-a148-3d6f-8cb7-e6512336afdb | -2.9447 | -60.9002 | 2026-09-02 15:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 63838a35-bb7e-36f5-aa2d-3c7f061fe47b | -3.4595 | -59.6548 | 2026-09-02 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 849e3731-8d4d-33ce-a684-62bc0e284a17 | -7.9907 | -46.5177 | 2026-09-02 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| b0c7ea93-a4a4-3b44-8e06-450e27db3c14 | -3.7533 | -59.3231 | 2026-09-02 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 60fa4505-33a9-3e9e-b589-ff41bf497f0c | -6.7463 | -59.4416 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| af01b85b-aa6e-35ac-93b5-92fd723c1ea0 | -12.1704 | -47.0806 | 2026-09-02 15:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| da48680e-c170-3319-89a9-9cfa135d4b86 | -6.8203 | -59.4001 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7e9fed33-af83-3b88-9a63-df3ff6a507c1 | -1.959 | -44.7682 | 2026-09-02 15:10:00 | GOES-19 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cd3bb8c8-0c98-346e-b877-8a12a807c283 | -11.5483 | -45.4446 | 2026-09-02 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 09ce3ef7-84f3-3eb5-9513-af1eea60a039 | -11.0376 | -51.4559 | 2026-09-02 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c4c780fd-fe5e-3233-b8d2-00af543595da | -11.3615 | -45.1955 | 2026-09-02 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 4d7397bc-73f3-3776-84e5-7becbccce430 | -6.93 | -45.7157 | 2026-09-02 15:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c816ff32-1342-3286-85a1-0d1b2f8a3554 | -5.5832 | -60.2116 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c9923a6b-77b9-3437-b441-3fd279f5d066 | -3.3688 | -59.4079 | 2026-09-02 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1f14baf4-53bf-33d9-815b-b7b2d898fe3b | -7.688 | -67.1262 | 2026-09-02 15:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fbebe2f0-4891-314b-896c-64a6b7424f0f | -11.0247 | -49.6656 | 2026-09-02 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| aa322b72-9af9-3f63-baf8-f81c5f72d6d0 | -12.3622 | -48.1681 | 2026-09-02 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 771f955e-4e69-35cd-9084-7028f8653f96 | -7.2536 | -61.1074 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7e072097-1338-3204-89fb-4a682386e87c | -8.7628 | -46.4642 | 2026-09-02 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| aea460ac-1c79-34b6-94ea-c1ea8bbdea91 | -12.3626 | -48.1459 | 2026-09-02 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 825230e5-c4af-3def-ba93-677eff4bf4d3 | -13.9664 | -58.6736 | 2026-09-02 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e56fcb3b-3d63-3e8c-9405-c8592fdb0031 | -7.0613 | -59.2165 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5d7b6a03-8e7e-369d-b714-59a8e343a92a | -1.5116 | -54.9546 | 2026-09-02 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 140d1b8c-8569-35c7-917f-584aa37248cd | -7.0057 | -59.2575 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f879b3dd-2951-3f8e-ba6f-d635e4284617 | -11.0434 | -49.6851 | 2026-09-02 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5f0b2be9-b950-360f-befc-c515b09e95e9 | -3.2179 | -61.1985 | 2026-09-02 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 511d8437-3444-391d-8a94-ddf364d42f7e | -13.5533 | -59.7377 | 2026-09-02 15:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a4bb2533-16e0-3455-aa7d-93761a117c7f | -10.3385 | -50.0191 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 077143e0-eaac-3a13-bfd1-051ddb470bbf | -12.3818 | -48.1433 | 2026-09-02 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e684c5b9-94ad-3e56-b7d6-f7a58d70b153 | -7.571 | -60.4643 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f81ec1c7-ddd7-3666-bf93-7b0bc421c29f | -10.5788 | -47.7306 | 2026-09-02 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 769d2101-49d0-31a9-ae81-109b606bd6cf | -10.7242 | -50.8534 | 2026-09-02 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f614f538-2b0b-332f-8c06-887f59c6a44f | -11.0936 | -51.5134 | 2026-09-02 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e00fda44-eae8-36f2-a78f-6f607a4c2cd3 | -3.2178 | -61.2362 | 2026-09-02 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ed7535c4-cf1b-3db6-833c-73ac3fd7c85b | -5.961 | -52.2056 | 2026-09-02 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f62cfd35-b75f-38f5-a47f-03c2197c5e9b | -11.0437 | -49.6635 | 2026-09-02 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f3a527f6-5662-300c-8c7d-ad098d9e7257 | -5.5649 | -60.193 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 90fed86c-dd5c-31af-b704-65d369b07680 | -7.0428 | -59.2173 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8098574c-6a0f-36cd-899a-4aff9f716743 | -3.3688 | -59.3887 | 2026-09-02 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 9ac5fae2-62f2-3181-ad38-09992de9ed81 | -7.0057 | -59.2575 | 2026-09-02 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c7f7ea1d-b4a9-3b74-a077-68da21327194 | -9.862 | -64.9771 | 2026-09-02 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5d108d13-1505-30d1-9c6c-9a4af3da48de | -10.3193 | -50.0425 | 2026-09-02 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0b839002-11fe-3a22-b089-faf3c5c7b8de | -12.01 | -60.5345 | 2026-09-02 15:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b3368e4f-68fc-3807-92e6-af051eeb7acd | -11.1723 | -51.294 | 2026-09-02 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| be050c22-cee6-3858-99e7-d60dce98bfbb | -9.6941 | -65.077 | 2026-09-02 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 05a7a5a3-c15a-3c57-aaec-b3f7fa9881a1 | -10.1138 | -45.8394 | 2026-09-02 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ffbe1823-eed9-3518-8af1-3cf1cef38a68 | -11.1129 | -51.4903 | 2026-09-02 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1ceadd31-1d72-345e-93a5-69e554065359 | -3.3688 | -59.3887 | 2026-09-02 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 71a1a43f-c248-3aa8-af33-b8f4fe59e880 | -9.8806 | -64.9764 | 2026-09-02 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6c6e350d-6c4f-36c5-aba9-6529edf4f44d | -13.9664 | -58.6736 | 2026-09-02 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 145.2 |


[Clique aqui para ver as próximas entradas](README84.md)
