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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e868143-7f0a-3184-8c61-e98138cb928f | -5.1451 | -48.89639 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 109ee4e4-f7c2-31d1-ac3c-0f2047308552 | -5.14445 | -48.9006 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 945aabc0-8941-3eee-8047-a83fa0302d43 | -5.1438 | -48.90482 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b0163dc-b87e-3318-ab41-04b28376492e | -5.14016 | -48.9043 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9553167c-f4d1-3f27-8132-481cb8d52b43 | -5.13951 | -48.9085 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dce21893-1751-3778-b7d4-783e505def43 | -5.10421 | -48.92051 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2e5ab76-7450-3943-9621-ed78b251e357 | -5.09907 | -48.88096 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5d0b30f-1bb7-3d4d-a854-6f900d905167 | -5.09543 | -48.88041 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffd5105b-1827-3035-bf7b-c8e4c3daaffc | -5.09479 | -48.88462 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7919fc4b-6d8d-3a50-9a01-f4c0497124c3 | -5.09179 | -48.87984 | 2024-09-29 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e03f163-b141-3869-9c46-614bf2ce81f0 | -5.22202 | -48.195 | 2024-09-29 04:49:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10cfff6f-284b-36d4-baa3-7ed3952dee21 | -5.21893 | -48.18982 | 2024-09-29 04:49:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62e576a6-cbe4-3819-a9a5-4116b46a7ae3 | -6.00918 | -49.33862 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0e30576-fa1f-334d-99be-5a4c2f5d920d | -6.00855 | -49.34276 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9c92468-cffc-3130-8bd2-ac6050298745 | -6.00496 | -49.34224 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f11bbbb6-ce25-34df-bf99-614ad78fc0d9 | -5.96163 | -49.18031 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e527e7f-b979-37f1-b635-b4988edb3e19 | -5.96099 | -49.18449 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f121d349-a36b-3bfe-aad1-e31f236b9837 | -5.95801 | -49.17977 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73598ec-902c-3b75-8a71-3162a5dd7327 | -5.95737 | -49.18395 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 359771bf-b22e-32b1-913f-d06524299075 | -5.95439 | -49.17923 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a929f46b-99fb-3836-bb7a-f80f45d0b3b7 | -5.95376 | -49.18341 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2f587c5-2f67-376b-835a-500aad2ba4ac | -5.95014 | -49.18286 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74036b3e-1921-39ce-a260-1bf36dbb14d0 | -5.94652 | -49.18231 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab3bcd92-08fa-3f5b-9405-738b367e36fb | -5.93357 | -49.62214 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74aa4064-6ade-3b3e-b327-3b191b5fb359 | -5.9325 | -49.20152 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376506fa-5731-3b03-9fcc-ff42fcafbdcf | -5.93064 | -49.61754 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e559be-75bb-3564-bd01-4d895c5b3106 | -5.93004 | -49.62153 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a217846-7486-3922-a11f-36c984cf0268 | -5.92952 | -49.19682 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b7de58-e347-345f-8fb8-4c9bfcfc1426 | -5.92889 | -49.20098 | 2024-09-29 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e423d490-abab-32a3-89d3-8fd81d34fcd0 | -7.5898 | -49.19125 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75334412-add5-3d08-90b3-95837f3dac43 | -7.5861 | -49.1908 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60a1cb25-3c93-3e1a-991a-a4f9e5cf4d95 | -7.58242 | -49.19021 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a13ac337-a931-3c0b-9b36-0800f7dd6b09 | -7.57505 | -49.18905 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a5702d4-30fb-39c4-9bd4-7c601f9ce00e | -7.56743 | -49.41446 | 2024-09-29 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70ee9758-4b39-3cb6-8768-42213be13f11 | -7.56684 | -49.41671 | 2024-09-29 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e5e4d30-064d-3a86-99fe-5e4b8fe5f500 | -7.5668 | -49.41875 | 2024-09-29 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1742f76-5ed2-3eda-b184-c68b0bc54d13 | -7.56379 | -49.41387 | 2024-09-29 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38dde813-60d7-30f4-8c2a-0701435c7eb5 | -7.56321 | -49.41611 | 2024-09-29 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e658b40-7d9b-3e6e-8720-c956dce10905 | -6.45761 | -49.69318 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96514023-2f16-3e47-a98d-dc73bdd19dfd | -6.42826 | -49.72204 | 2024-09-29 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140dbe80-1c12-3ae2-981b-76135ab538c1 | -7.74488 | -50.00124 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4d982a-03b0-365d-b9cd-19b02633b948 | -7.74197 | -49.99652 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2dbcc33-dcf0-3d05-bc9e-d023e68fbf8a | -7.74136 | -50.00058 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91fd4ffc-c37b-3d8d-9aaf-a7e5fe90b6bd | -8.89732 | -49.63784 | 2024-09-29 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e276a361-523a-3417-8dac-cd3494c22233 | -8.70816 | -49.60391 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c5c623-0c79-37cb-be62-eb71b8248d74 | -8.62112 | -49.48734 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17531a87-2c8e-3b7e-ab36-d76a48363498 | -8.6181 | -49.48244 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32156fb3-6e1b-3126-b252-6d4b3404b437 | -8.61745 | -49.48679 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7c15cd7-2f55-3ef6-b579-15b91e298efd | -8.46565 | -49.60218 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6e1cf2a-8b1c-3ba4-aa09-fd00cb32b25d | -8.2434 | -49.38705 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d6dd02f-cc9d-31c1-948c-42ed08a12c7f | -8.23971 | -49.38654 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f704407-0d4a-3c56-a03a-9ad514461df5 | -8.23843 | -49.39533 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e6e0659-f140-325e-b396-5cd8eaee8ddc | -8.23779 | -49.3997 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05d44c48-66c4-3266-9e41-4409b45d24c3 | -8.2354 | -49.39037 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e0b6299-5e64-3b6a-b662-5cbd3470b3a4 | -8.23476 | -49.39479 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6e31cb4-e11c-3eeb-bfaa-72e3038832d6 | -8.23412 | -49.39917 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a246ff76-5d96-3540-9511-58c97ff90af7 | -8.23172 | -49.38984 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38e8c649-9407-39fd-b00a-7dceb74501d9 | -8.23108 | -49.39425 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf95d47e-15fc-3ccd-989e-47ed02995a2e | -8.23044 | -49.39862 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d83030f-716f-38ce-a328-a3e2904ca458 | -8.22804 | -49.38931 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb2a00f3-9c18-318d-b771-7268c337075b | -8.2274 | -49.39369 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd6dce97-4107-3204-87d1-173023ad9773 | -8.22485 | -49.39071 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| febcf4f7-d4db-3441-97a0-a2f0b5016001 | -8.22436 | -49.38881 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c9b610f-819b-3b4b-a09c-025bd1851a7d | -8.2242 | -49.39503 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06d8bd5f-b058-39fa-b106-b0deeda35cf0 | -9.37817 | -50.02301 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 977b735d-7af3-39b3-99c3-793720e49da0 | -8.22373 | -49.39312 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd139204-5c94-38ef-8693-307078bffe97 | -8.09636 | -49.52272 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c29c005-b558-320f-917d-e0e221ce41fd | -8.09571 | -49.52698 | 2024-09-29 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bc92245-1329-3906-9930-d37574f9333f | -8.02071 | -49.89965 | 2024-09-29 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0bb4c70-367e-38f8-93e8-38ddf8525bdb | -8.99638 | -49.82578 | 2024-09-29 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3883abd-ceb1-3cdf-9fda-d25ef187e1b9 | -8.99575 | -49.83002 | 2024-09-29 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f24feb8-9215-35a0-bd90-9bf0e40d3ac1 | -8.87055 | -49.74315 | 2024-09-29 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 611228c0-0000-30ad-9b08-55181e40cb08 | -9.9435 | -50.16034 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fd0cfc-5960-3af0-a433-cb79ec5fb21c | -9.9399 | -50.1598 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2f89562-0344-35a5-998c-a150acddfefe | -9.74322 | -50.43407 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7371e4d6-f8de-33e5-b4a8-4c0cfa03af8c | -9.74026 | -50.42953 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c94a32-048f-3f25-aed8-4e31226191c0 | -9.73966 | -50.43357 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727de8b3-ac16-39fa-afa3-a956bb9af66c | -9.73671 | -50.42902 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 719e8ca3-d63b-3654-bf59-749172e83037 | -9.67666 | -50.10156 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d8c7ff-dd08-347b-ba01-84d711d1abf5 | -9.62389 | -50.10003 | 2024-09-29 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fef0c15-d2ed-320c-a204-5c17664cd48c | -9.57668 | -50.19476 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41179fd6-6130-3cf4-bcef-ba86ff2401f0 | -9.57607 | -50.19888 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2102b97-1087-38f8-8593-40563f4b83c8 | -9.57545 | -50.203 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28379ca3-4aa4-38cc-b648-d71571b233bc | -9.5731 | -50.19422 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2e86942-60b9-3e71-8dd5-80185051e0ee | -9.57248 | -50.19833 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c31f5374-1413-3903-91c1-523c4213e103 | -9.57187 | -50.20246 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8d2d4fc-c8f9-368b-a128-ad742074712d | -9.57126 | -50.20657 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c98d5050-a36c-39b0-af98-fc0cc28d2e1c | -9.56952 | -50.19368 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdfd59c8-983a-3fbc-9700-64cd3606d699 | -9.5689 | -50.1978 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b314b5b9-4c45-36b5-abdd-c9eca04d78f3 | -9.56829 | -50.20192 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81271cb5-b432-3e5e-b032-8451ec79bbb6 | -9.56768 | -50.20603 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1b2e1d63-f99d-388c-a807-7bd4e3006a83 | -9.56655 | -50.18901 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 681d4cca-98cb-326e-bad5-0ac7b16184bd | -9.56593 | -50.19314 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c54caea3-4d4e-3a9c-af37-5ed6982c1c37 | -9.56532 | -50.19726 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0132f465-3ea5-3407-82ff-ecb30c9f3620 | -9.56471 | -50.20138 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e4eea0-2283-3d9d-821a-692a081546c9 | -9.56358 | -50.18435 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2c6f036-6edd-3ab8-b983-cec93a170599 | -9.56296 | -50.18847 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa93b8bb-c839-38e9-ae53-5a98168c54db | -9.56113 | -50.20084 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7e4262e-eb55-3edf-ade0-4ab54e0477e1 | -9.55999 | -50.1838 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81afe2b3-ad88-33f2-ac05-a06ce2d8346b | -9.55816 | -50.19618 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README46.md)
