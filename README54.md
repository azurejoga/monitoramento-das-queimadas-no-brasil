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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ea3e97e-761e-37d6-b25c-78cf0495163e | -4.28892 | -46.90931 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6141b461-7140-3110-93d9-fb146a59bd5d | -2.61836 | -46.18747 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d975f34-be22-3dcc-920a-5c65fd6bf9a5 | -2.60013 | -47.55711 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97f9e2ea-97dd-3847-ba06-13ded3b567b4 | -2.25535 | -48.38444 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 905dae3e-8c7b-3e31-bb6e-89526295f048 | -3.61876 | -50.15348 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f98e9134-9fd4-352d-a01b-6702d72c0927 | -4.46879 | -44.23323 | 2024-11-17 04:29:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32d40d80-71d0-3c78-bfdd-1dd3730cfe2f | -2.64771 | -46.19557 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0263d6-056f-35e9-9297-d0b9a23a7d25 | -3.97434 | -50.93084 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2444fd6-755a-37d6-8a5e-30243881c4c5 | -3.80101 | -46.51023 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c4753b-8595-367c-8917-77870dac9cb0 | -3.09343 | -45.97414 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c596325-5a5f-31ca-98b1-11bf8b56cd5b | -2.23411 | -53.61458 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f276bfb-315f-3423-b942-6a1f80fe7c84 | -3.69574 | -51.07753 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 949bcd74-0c52-3a95-b2a6-b3b29b8a5bae | -2.22253 | -47.21499 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6737829-1259-38cc-ad9f-17b0e267eb5a | -2.21484 | -47.22084 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| eb3b2ca4-0ab9-3a44-a9f9-215ea58b2152 | -6.92338 | -47.82825 | 2024-11-17 04:29:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8eff651-8bbd-352a-981a-e6e142308686 | -2.67524 | -46.193 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ef3bfa-4483-31c7-925c-b6b5e6038294 | -2.61504 | -46.18696 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23554db9-6f99-32ee-a0d4-fa3ebc9a5773 | -2.21815 | -47.22135 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6965f580-1104-32d7-a139-4099d0f8a713 | -4.33302 | -48.61359 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1747085d-97ed-3740-9816-49143c52264d | -2.19871 | -49.54106 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 276514bd-d8da-3788-ab85-ac7f3e0bcaaa | -2.62556 | -48.55212 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9179ded5-5170-3eaa-8c7f-6173c7e6751e | -3.56887 | -50.25854 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5183e5f2-2936-3b2d-b416-b542fa071ade | -2.11179 | -48.89365 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52185d07-176f-3238-bcf7-e3061f28cb38 | -2.4157 | -48.78875 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99edcb5c-8844-3c05-947b-cf7eb2de616a | -3.94575 | -46.71362 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d0ba074-e955-309a-9076-46b0ba94c0f0 | -3.78274 | -46.03712 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c2c99e8-a08e-3d14-94b5-e46ac4f7d005 | -1.1375 | -51.6883 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37ccc258-e8f6-30e0-96f5-71095ff8cbb0 | -1.32558 | -51.87188 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 61e1b481-9394-3a78-93de-75a7450d5052 | -2.16285 | -48.32611 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3132de55-c22f-336d-9f7d-5101966a2ff4 | -2.50445 | -47.23866 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c1b56ca-dec2-305d-8b36-f65ced99ba69 | -2.38875 | -47.94806 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 597927fa-85fc-3eb6-8daf-e7d6e8196b8d | -2.60398 | -47.55417 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1914d3db-9870-391b-88d5-4b619495fb57 | -7.37623 | -40.97459 | 2024-11-17 04:29:00 | NOAA-20 | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ad69c976-93af-3409-989d-aa75a7b342d1 | -3.12512 | -45.90317 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 690ca6da-17f7-3c2d-b106-459136d9db85 | -3.95593 | -49.9698 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e194d04-0656-3458-809e-1525924ce81c | -2.35654 | -46.79678 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7dfac0-bff4-330e-ab3c-0a2ef6864784 | -2.463 | -45.61626 | 2024-11-17 04:29:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fec8342-26f1-3d61-95a7-aefef89c9a6b | -5.99794 | -42.63082 | 2024-11-17 04:29:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e91012da-afb6-3360-b054-48e3109bea9b | -4.54098 | -45.25656 | 2024-11-17 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 364e6d95-c17d-3a5f-b32a-29696540de34 | -1.28147 | -48.09445 | 2024-11-17 04:29:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3825d1-fdd3-31c0-a108-e2b7ea68ff31 | -5.0337 | -44.86276 | 2024-11-17 04:29:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 747676ff-7cb6-3c62-b425-4143cd29767e | -2.66188 | -46.16956 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f412605-f535-302d-86ad-7df96257c30d | -4.10428 | -46.87311 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 789c03b8-41ea-3fdf-b784-b9a94ff030fb | -3.15711 | -46.60841 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48db0cff-616e-310e-a728-ae1d0f0283c8 | -2.08332 | -50.48622 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49d65ba1-3cca-395d-9bd3-aa64c568e9c7 | -3.03929 | -47.9819 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e39f63c6-d832-312f-901b-61641877da88 | -3.34828 | -46.42931 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7256fd8c-12eb-3870-a4b5-daf65a6bda4c | -3.56236 | -50.25329 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 18445831-dfea-3adb-9662-b701f3daef07 | -1.3267 | -51.8646 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 28ab3346-db46-3e8f-b1a6-4d36fef21ef3 | -1.63981 | -50.5232 | 2024-11-17 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8417a7b-54fc-3518-8f7d-43ff0ab8e4b9 | -2.24797 | -46.88142 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad7dfad3-c137-3174-8926-e088c84e801f | -2.65768 | -48.5461 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05ba4bcd-a31b-378e-a36d-4918ffc3ff32 | -2.30563 | -48.46979 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b49341c3-3650-35cd-b948-aa578ba3024d | -1.08929 | -52.33699 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7b37b02-038b-37ce-9239-cd262d075992 | -4.48053 | -48.10816 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e75d8f05-8920-3dfd-865b-89e7bca6946f | -2.84586 | -46.66544 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca7cf477-ee47-3f1e-9e24-d1e7db773507 | -2.82825 | -46.66975 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd34af80-dee2-3eba-8950-9afe04c5d1fd | -5.40335 | -42.77196 | 2024-11-17 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 116aa478-4f80-3f00-9077-df5c0fd680f6 | -5.26846 | -47.18266 | 2024-11-17 04:29:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecd0d14f-61fc-35ea-82f4-bcdd87084704 | -6.98673 | -39.66195 | 2024-11-17 04:29:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e1e21d0-e9cd-3685-ad3c-21d9f8e5bd0b | -2.94143 | -48.32314 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a8b310-6da9-31d5-9946-623b3fe27471 | -1.20497 | -51.76477 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 959d62c7-5851-3329-b2a4-d452cb252f9c | -0.93688 | -51.72214 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 281b2066-9a5f-3edb-a50b-634830a0a895 | -3.69279 | -50.11843 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab258f38-5e5d-373c-947b-b2df4eeac98a | -1.01804 | -48.06787 | 2024-11-17 04:29:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 080d7f4f-a64a-3219-8ddc-7f553dd320b8 | -5.17828 | -46.16677 | 2024-11-17 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd23ac19-2511-3f1c-a8f1-51b64107522c | -2.66697 | -46.20241 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b9a9cb-ab81-38a5-b6c5-afe8d633b6fd | -0.92999 | -51.76505 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93b01e51-dd13-325d-b780-b92937ca0dc9 | -3.79052 | -50.14166 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14a86842-1919-37ea-aea5-22d32cce3fc7 | -3.53076 | -50.51739 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02b9f4f7-01b6-3c95-ab3b-a00eeb8bfdd2 | -1.10638 | -51.93779 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b382e22-c907-3edb-9e74-0a1f6efd8528 | -2.8044 | -45.9732 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc1e9b7-81af-3758-80e5-bf62a5a43cd1 | -2.66134 | -46.17304 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cfaf9a0-d643-30ab-aaed-7d2b222df209 | -2.10737 | -50.80367 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 996d4ea8-d099-3dfd-8a6e-4e46c891e332 | -2.96342 | -54.31147 | 2024-11-17 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55545eee-edd3-3c89-b998-b4be89af12c6 | -2.11341 | -46.37488 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06c11058-7280-3f5d-af4b-43c4b8d7c11a | -4.54954 | -46.41481 | 2024-11-17 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4442321-0d7f-3b6c-9c34-9e40a6ba9f85 | -3.84374 | -46.62704 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a059010-de40-353a-878e-b9a70a407d22 | -0.31702 | -51.50565 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab6cdc92-8357-3f4c-afaa-bc5b06bda064 | -3.07516 | -45.46364 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04af604b-9880-3e37-8b8a-f57efdaf4ea7 | -2.71201 | -46.06658 | 2024-11-17 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac568dc2-f27a-3537-91ab-b9b80957f7c6 | -2.94478 | -48.32366 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08fef805-b51f-370b-bdd7-0c34f1a25500 | -3.90166 | -47.08097 | 2024-11-17 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| de8a3735-372c-3dd7-a5fd-200145057a8f | -2.39854 | -48.45118 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 687173cb-e5ef-34aa-8535-e0e9ab9a7c8b | -2.16035 | -46.39978 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b9cf78b-cdb1-338f-a713-674facc4fd56 | -1.12724 | -48.3581 | 2024-11-17 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bedee134-f574-36e1-a2b0-88ee19b535c5 | -2.80234 | -46.66221 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3885953-f884-39c7-a646-c0001e32ba6e | -3.52535 | -50.26517 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be2d125d-5002-320f-ac8f-2bcf98e36195 | -3.79254 | -46.67234 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2239d9ef-ee24-3e1a-b150-8d94328626b1 | -1.68671 | -48.18252 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04448749-f9f9-3281-8176-838c194ea28b | -2.35309 | -47.46504 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6496b2f8-311c-3852-8266-850b543fbaad | -4.32017 | -48.60794 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0307c926-6178-376c-843e-f1b6a5c2d4dd | -2.47302 | -46.3566 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa4394c3-a211-3fed-ab08-57c56cfd3fb9 | -3.04247 | -45.75984 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14bcedf4-3bc5-3f05-b4f2-74f2883727eb | -2.67246 | -46.18902 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4b3903c-b01a-3bb3-bce9-32e9c3673cfe | -2.17964 | -48.75211 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a803e06-6a5e-3f20-b09f-951a86314917 | -2.82879 | -46.66631 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d9ec4dae-129f-367b-adf6-341e139a2972 | -4.1032 | -46.88 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac30a3e-c782-354c-8388-fc3cf36edec9 | -3.78109 | -46.04775 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a83f4813-9664-389b-a8b3-923f0020230a | -2.13456 | -48.12085 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README55.md)
