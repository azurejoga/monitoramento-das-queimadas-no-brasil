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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c1b91d3-b580-36b7-a616-98b1240c83ef | -7.86446 | -35.02392 | 2024-12-07 04:08:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ee795d51-5d15-3321-be31-a0bf0c4f29ef | -5.98208 | -46.07546 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69112346-377c-3756-ad62-a199945ea020 | -5.77355 | -46.55075 | 2024-12-07 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc999c24-e639-32ce-8a5a-bd6808d14d09 | -6.20585 | -46.06227 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f813179-adf3-3c83-829e-04562b52a8c5 | -6.93382 | -42.84151 | 2024-12-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3500c3e-d26c-366c-9738-f9aa2271488e | -4.41939 | -45.66099 | 2024-12-07 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dbed0c9-9c49-3b37-af26-1939cd71a36e | -6.30017 | -44.87627 | 2024-12-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9c3be37-40fa-3301-a7a5-8b006fec417d | -6.45573 | -45.75123 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22cff3bb-4648-3af9-8249-7aa3d7725b3c | -5.77166 | -46.55031 | 2024-12-07 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 29703615-c936-35da-a13f-78354356cc85 | -5.11678 | -44.00819 | 2024-12-07 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e5b36d-cc44-34b7-a13b-553730946812 | -6.93048 | -42.84099 | 2024-12-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ae13a67-75f2-3ba6-a828-ca90f7173adb | -4.32143 | -45.88864 | 2024-12-07 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eb31578f-7a3c-34f9-b7c2-fa95efb1f3d7 | -6.00811 | -46.40574 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ae335a2-a6d4-33d3-93fa-ebc3770dbcc3 | -6.4482 | -45.74997 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d48029ab-4e57-307e-af53-5cf187b21193 | -6.49109 | -44.68648 | 2024-12-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fc2db9-f133-30a4-adc8-ab4a0e938144 | -6.20199 | -46.06164 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97aac71d-b71a-3021-a05e-0d90a955605c | -4.88082 | -47.22979 | 2024-12-07 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13a7dd73-9587-3e1f-abbb-5c3c731581be | -5.58109 | -45.21117 | 2024-12-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 854c9754-49af-3f4c-8c3b-368759c554ce | -5.51114 | -45.49101 | 2024-12-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15501621-16f5-310b-a5ae-ef84017b5692 | -6.95276 | -42.76522 | 2024-12-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fe6a9fb-4337-31a5-b662-01a151e74efd | -6.84061 | -44.38587 | 2024-12-07 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b06210d-d33f-3db9-b01f-e856a7c03afd | -6.29096 | -43.85143 | 2024-12-07 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b40b114e-3499-3c25-b100-b093b278e1c0 | -6.45509 | -45.75315 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56154992-9188-3422-ad9b-13951426a826 | -4.39098 | -47.76622 | 2024-12-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0bf726e-1bda-3a06-8f50-df34fb8e0c63 | -4.17666 | -47.53304 | 2024-12-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b41e450c-d522-3058-aac4-0fa4677373e4 | -7.65039 | -35.31573 | 2024-12-07 04:08:00 | NOAA-21 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 33cbd382-a7d7-36ff-901a-2ddc52b13f6d | -6.44829 | -45.7473 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebd9388e-bbc6-3ea3-9034-b2282bd9dd9c | -4.42804 | -45.82737 | 2024-12-07 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 268d2cb6-f28e-3e58-ac79-3c5486c5084e | -5.97328 | -43.35768 | 2024-12-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4723a20a-226d-322a-913c-cb79547e018c | -5.77296 | -46.5542 | 2024-12-07 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5083ea6e-b461-31c1-a680-d5a4d3cfbadc | -6.35446 | -46.08466 | 2024-12-07 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a34da9ea-70d6-3a2b-a9c6-115c7f81d20a | -5.11328 | -44.00763 | 2024-12-07 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450f8c6a-fcb6-336d-9186-fd295e6be0a4 | -7.90822 | -35.24384 | 2024-12-07 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6c5a976e-322a-3b64-8924-76c1ba9085ad | -5.11614 | -44.0121 | 2024-12-07 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89da442d-8141-3a33-82cc-dbbb58aa6381 | -5.98126 | -46.08037 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7dd6ec3-6bcd-3d23-8516-6883a906fef4 | -5.11264 | -44.01154 | 2024-12-07 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78eee63-74a0-3418-ae53-26c039434770 | -4.14211 | -46.58778 | 2024-12-07 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eea78e1-7767-359e-a6bd-5c8c5acf7e3a | -4.38646 | -47.7714 | 2024-12-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3d96b4-d988-3019-91b8-99c0d7e67fb4 | -7.91344 | -35.23976 | 2024-12-07 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ca99c465-2617-3109-b192-cb348e1041af | -5.7711 | -46.55376 | 2024-12-07 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 99f5fecd-12d4-34f9-b719-3c89c866c286 | -6.4565 | -45.74664 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1c2fe08-80cd-3bf6-8545-eb4bca299b45 | -6.06091 | -43.62062 | 2024-12-07 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7354f89-607e-3abf-92f5-f67277301fea | -6.01067 | -45.92722 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d25db1ae-4fc3-3151-a06c-2f05c7abb665 | -6.48819 | -44.68177 | 2024-12-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bdb2471-1244-31be-bf86-7c443802c813 | -6.93105 | -42.83746 | 2024-12-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35179210-d530-3ac8-8b57-8d188987f1d2 | -4.60748 | -46.08538 | 2024-12-07 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b98f36-f2df-3eb5-84fb-57b423ca6657 | -7.91277 | -35.24451 | 2024-12-07 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 0ff1e3f3-edfb-30a6-b9a8-c208036f55a8 | -6.45583 | -45.74855 | 2024-12-07 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 020ce801-0fe5-3e7a-bb53-392332487759 | -6.41003 | -46.19014 | 2024-12-07 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 693d9db0-5ef6-3384-9193-b1d9fc5e70ea | -4.42323 | -45.6617 | 2024-12-07 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71d548b9-c910-3f4d-b4cc-e71b895c7d4c | -4.14493 | -46.58907 | 2024-12-07 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0aabbab-be36-37a3-88a6-e239b79aa36c | -4.42405 | -45.65672 | 2024-12-07 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b040945f-8137-3ec3-aa7d-6c6bdc3ea9de | -2.84173 | -40.30017 | 2024-12-07 04:08:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a20483c-6d5d-367a-b750-d65d06d3f5fe | -5.50737 | -45.49043 | 2024-12-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3dd82b6-d54a-3241-a771-790a199a70b3 | -4.14318 | -47.73917 | 2024-12-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 896d9f31-37ce-3b98-aa33-c96851ee54bc | -5.75311 | -44.33543 | 2024-12-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 251825a9-f8ba-3150-ae54-f224218e8fba | -4.39024 | -47.77061 | 2024-12-07 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc65ea78-2999-3472-b64d-7e7aa385496c | -4.14082 | -46.58837 | 2024-12-07 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379d71ab-0bbf-396b-aa6d-dac89159b1cc | -3.55034 | -47.38583 | 2024-12-07 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43c84ed2-9d95-3cb5-88bb-8163b8f236f6 | -6.8441 | -44.38646 | 2024-12-07 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0746d704-a774-3cc0-b177-39c2cbb1a799 | -5.50845 | -45.48845 | 2024-12-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 690966e2-6339-3b6e-a0d2-4eccf87f6641 | -5.58181 | -45.20678 | 2024-12-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c043d064-8460-3e89-ac4c-90ee83a0c532 | -4.8802 | -47.2336 | 2024-12-07 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8650fdf9-4d01-3efc-9ce7-5890934f6753 | -10.75994 | -54.78234 | 2024-12-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7154f57c-c40f-33ba-b001-43ed0aec8e3a | -11.20052 | -53.81953 | 2024-12-07 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64d20659-7173-326c-94e9-22e941a2289d | -11.30924 | -42.1321 | 2024-12-07 04:10:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da8d01be-f660-32a7-ba44-f7472d93c6ed | -14.38295 | -46.03748 | 2024-12-07 04:10:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68ef400c-f5c1-357a-b439-b358400b2b42 | -11.87135 | -47.71307 | 2024-12-07 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2632416-176a-3dac-9ff4-88a49c53ace1 | -12.86083 | -51.93969 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2dca9a3e-616c-3f53-9b90-68ae41dd651e | -11.73453 | -54.30918 | 2024-12-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61896f41-35bd-32e5-a5e8-36f412088830 | -11.05625 | -45.37646 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92471673-f107-369d-bf1f-54685b436ac1 | -10.54359 | -44.68385 | 2024-12-07 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a109d36-312e-3df6-b868-da79b64bd5d8 | -10.97853 | -44.73097 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79f3689d-232e-37ca-a497-05599084a9c6 | -7.17402 | -44.99313 | 2024-12-07 04:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7fbb0073-1e96-3cfd-aab5-17148ff7851d | -12.91978 | -49.68297 | 2024-12-07 04:10:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fec0018-7325-30a0-b3e1-95f32d175995 | -10.5303 | -49.05474 | 2024-12-07 04:10:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3852ea30-b148-334e-8b23-99b9c80a075f | -12.46079 | -46.93996 | 2024-12-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970e9dfc-5ff5-3de8-8412-f534c2073105 | -12.49921 | -46.35182 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9c36e51-b17a-355b-aa5c-a55e86891cc8 | -10.53466 | -49.05556 | 2024-12-07 04:10:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4734c55b-188b-3b4f-8d9b-6b28b4856cec | -14.38362 | -46.0335 | 2024-12-07 04:10:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32d52d5c-6b2c-3771-986d-1c668e9d3a59 | -12.93002 | -48.63485 | 2024-12-07 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f632b19-14b1-3c43-a97d-77cb6c713c7f | -7.08718 | -45.20607 | 2024-12-07 04:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72e69cf8-459e-374b-878a-c231b841fe64 | -11.05845 | -45.38502 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc9e0b92-cd29-3a99-868a-8cffb225733c | -12.2025 | -47.15945 | 2024-12-07 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590289a0-73fa-362b-8d40-1f814ba6cc4e | -11.41411 | -51.27265 | 2024-12-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71bab5bb-1253-384a-9e42-8621767a60f2 | -10.03832 | -50.57425 | 2024-12-07 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f52055d-c101-3f20-8d9f-200703b3b648 | -11.94221 | -43.93446 | 2024-12-07 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69202b69-cf5f-3e36-8c21-5476fcd10f77 | -12.85067 | -51.93769 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85923f29-ba89-3a0e-9b50-3bc71cc32d23 | -12.48259 | -46.27505 | 2024-12-07 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92bed222-de2c-38e6-9a2a-58e005a5d854 | -10.98227 | -44.4682 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd30559c-8560-335a-ab67-4d59e310bf70 | -10.66108 | -44.4989 | 2024-12-07 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 350fbd8c-5205-3b42-9f00-0a36e721d9d9 | -11.06674 | -45.3783 | 2024-12-07 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db758711-fd88-363e-9235-5ae3fac130f4 | -9.18902 | -44.34971 | 2024-12-07 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2351083-6ef1-3539-9666-5cb8170e77ed | -9.90805 | -48.57978 | 2024-12-07 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3f4aeaf-688f-3919-83b4-81efde53767d | -10.67716 | -45.11758 | 2024-12-07 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab242681-f7ed-3b5c-925a-9810f6a8a93c | -12.41146 | -49.6847 | 2024-12-07 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9deca046-84d8-3fce-988a-83f563e470b7 | -12.46368 | -46.93445 | 2024-12-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd840945-1f76-37dc-a021-8df804c41aa1 | -11.16627 | -43.57039 | 2024-12-07 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c683650a-aa66-3760-b425-1cfbe35db094 | -12.8501 | -51.94075 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c0334c6-f3e1-34c4-93bb-727983c474c8 | -12.85962 | -51.93588 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
