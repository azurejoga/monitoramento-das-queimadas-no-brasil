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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72f7922f-0008-3dca-8ce3-bdae4c82969b | -14.12124 | -42.14003 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 636d7773-ff02-3ac9-aadb-3dbe9c6c45cd | -10.46102 | -47.95101 | 2025-08-10 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a71b8e0-60e9-3ccb-b67f-07cdf8c7ff8a | -12.60332 | -47.12744 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 320bd02d-ee3e-36ae-a25c-46717292480a | -12.55483 | -47.08255 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebc1a9b2-6b0d-3d3d-90b2-f886cec2d7a9 | -8.92562 | -60.73417 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f0720ee0-9d85-3ed2-b265-af413a5aac3a | -13.06015 | -56.8527 | 2025-08-10 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6596b90-da06-3823-b8ed-7f31926cdbb5 | -9.87586 | -49.95255 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76e474dc-99b8-3fea-8564-8dec952df31a | -7.06205 | -59.18644 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57c81f63-2cf9-3128-9911-857b86525ce8 | -14.46964 | -47.84298 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9fa8fcb-ddca-3c3c-bc5e-449617c92cf1 | -8.92905 | -60.74498 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025d83af-ca68-30e4-a44f-6ea663e87bc1 | -9.52682 | -45.4018 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edb3143c-8ac6-39c6-8e65-62066b472b6a | -13.63671 | -48.98401 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ddf69e6-85ab-3b87-890e-0f117bfeda4c | -8.90573 | -60.54541 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d24a6283-14ac-3d42-988b-66b811b8ace1 | -10.44149 | -50.97791 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c71edefd-824e-355a-ac36-aa023295024b | -7.07959 | -59.20116 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c307a19d-97af-397b-98ec-44d4d0ce1d8b | -13.10996 | -46.89431 | 2025-08-10 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8c8af05-d67d-3ce1-baba-31ec530e64c2 | -11.09732 | -59.91016 | 2025-08-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 802a5b9a-f60c-3faa-b7db-fc0e15cedc2e | -7.07569 | -59.19469 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db097104-033c-3d20-96f3-02c089fbbf2d | -9.51977 | -45.42485 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb47154-b261-3674-92a4-b048bd61f711 | -13.63297 | -48.98351 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b3044d-2153-3328-92bc-04168a63fe5e | -11.73061 | -45.00906 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d583b412-1483-3975-9cce-57e2498a9c61 | -12.57717 | -41.28898 | 2025-08-10 04:46:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cc7c060-ec7e-3157-9a90-ff9130ff0b15 | -9.64037 | -48.34618 | 2025-08-10 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93a3e81a-d3ac-3951-9808-e55d625a6d7a | -9.49438 | -46.29137 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faf0a1af-f1ab-3c00-a55e-232a106e7a84 | -11.09792 | -50.45697 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b2b411c-7ffb-33c3-a21d-eb4d49b71da1 | -9.5189 | -45.42715 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98668f61-27ea-38a3-a5a3-a38e375626e1 | -11.1076 | -50.48506 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b01e9f77-66b9-3376-b939-1568c6758077 | -14.2942 | -51.96542 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a053290-aba4-3db7-ab19-6adaf38e9294 | -9.87243 | -49.95201 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34561d2a-aab7-392a-bca7-94c2e69114db | -8.92844 | -60.74825 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d38757-931e-37d7-97a4-01043f39c3f4 | -7.05819 | -59.20845 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd67189e-20ee-3c42-8c37-4b98508008b5 | -14.29365 | -51.96903 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c63ebc0-d9c2-3100-82b0-2748712b9a56 | -7.07066 | -59.16593 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5b66579-66a9-3b83-afa6-457b27b6e8b1 | -7.06014 | -59.19733 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2ac2f77-ac30-3041-9bd2-3ae3aab2faa3 | -11.08328 | -50.50783 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b22730f-1161-398a-a8f7-248168780d81 | -7.06784 | -59.18204 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec801ffb-acac-3510-ba62-adf48f4b4fe0 | -9.49493 | -46.28756 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14e6b2ae-edc2-339c-833a-0f9c0343d144 | -9.86798 | -44.70551 | 2025-08-10 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8873a362-b769-3d50-9dc7-04d4d5bc12c1 | -11.74745 | -45.02665 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ca12008-83df-3368-82ef-32c0423488f7 | -8.06421 | -49.71206 | 2025-08-10 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b86e70d6-7b00-3564-a4ce-6e1cb71235ae | -8.92784 | -60.75151 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04295a0d-7c3d-3a00-9562-90f7f0d6b895 | -8.92502 | -60.73744 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 009df2ad-4743-33a2-b445-8a18e97d26d0 | -9.37316 | -61.53565 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a7f01eb5-9051-37ac-b0e2-e7e4e979a33a | -12.6494 | -44.51436 | 2025-08-10 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb471991-049b-3414-9986-cc9f773d10aa | -7.07664 | -59.18921 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b100f703-0a86-3b65-b604-acb770d8d8cf | -7.05525 | -59.19649 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e1548950-1862-393b-81a4-1538c6953578 | -8.56115 | -54.68449 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6f306e7-5c8f-32cc-949e-05fc07e0bf1a | -13.63462 | -48.99851 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 192344fb-a5a3-3e8a-9a75-a2076924fbc8 | -7.07083 | -59.1937 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8b61b82-b261-362c-a49b-59ea4873a564 | -8.56748 | -54.66865 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4a1266-a05f-362a-b9e0-63e7b1e7630e | -15.15653 | -48.12843 | 2025-08-10 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4eee4b6-651d-3fde-a1e2-237f73c3e6df | -7.08341 | -59.17923 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0dc7f60c-d657-3cf0-9016-5ee8c631f01c | -11.73214 | -45.01786 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4f3f604-b822-3fd8-b1f9-861e60ebee5c | -9.87186 | -49.95577 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aadd6ba-b11a-33ea-bd42-d35adc3faa4c | -7.06987 | -59.19919 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3070626-ca89-3323-865c-6e8ff9d0306f | -12.60796 | -47.12428 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88bc3e4d-6b07-3810-a386-78ec6e0645ad | -11.11956 | -54.65142 | 2025-08-10 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 790dcddc-5542-3126-91b3-7f80883b36ee | -8.92441 | -60.74073 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba126e5e-5ed4-3de1-90bd-a2c210f2babf | -9.37383 | -61.53203 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b55d97d5-fdb2-3ca2-acf7-26c848bda72e | -8.90631 | -60.5422 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beeae911-19f0-3a98-a19f-808b9e7434cb | -8.07345 | -49.90127 | 2025-08-10 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dee2095-9a3e-35cb-98c0-1d291ec98b80 | -9.55863 | -62.72254 | 2025-08-10 04:46:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec809291-a7ad-30df-b0e2-6b77996a7796 | -7.05427 | -59.20208 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 081afbf0-ef4f-353d-a9e2-a056f6eacfd0 | -7.05916 | -59.20289 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45ae5210-9366-3eaf-9565-e095e87085e5 | -14.59366 | -47.16191 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a82a194-69f6-3232-a16c-dd14f240ff13 | -12.64283 | -44.51229 | 2025-08-10 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81660c22-b2d0-3498-9da7-6863b8cbe450 | -12.16981 | -50.21803 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4aa0592-9b4f-311b-9898-5ff269ad7a94 | -11.76561 | -47.48383 | 2025-08-10 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| affb2a67-dcbb-3965-9d03-32def40406ed | -11.08668 | -50.50836 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 970ebd1d-31e7-3f7a-8d9c-ca029eb7a231 | -14.29698 | -51.96957 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11b9d7eb-d1d4-3b20-964a-822c4526c8a5 | -11.43983 | -42.31974 | 2025-08-10 04:46:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15efa687-a395-350c-a9ae-bd78d0065b90 | -11.10207 | -59.91119 | 2025-08-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7332049c-3e37-39d2-994e-2d777f16f12f | -12.57912 | -47.15069 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 043abd96-42fe-3062-93e7-61c84e3c4feb | -8.96005 | -46.74176 | 2025-08-10 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19399c4e-f238-3a29-a0b8-bf419dee898d | -7.0728 | -59.21124 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 851f5ae7-a164-3b3c-bdf3-d74f215bec3f | -8.88032 | -44.79033 | 2025-08-10 04:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edfd043d-d8c6-3a5d-89c9-f8c542f50130 | -13.77975 | -48.879 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ddc214c-6f82-30fd-9e15-12dc6c996c95 | -8.90516 | -60.54858 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29450ce1-b2f7-35a7-a544-b4062fef1440 | -14.48883 | -47.86047 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d58d90-9ba7-302e-aed2-1d481a6e3b5e | -11.09736 | -50.46068 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf78217-1676-3bd7-84c9-fd09794e0d46 | -15.92136 | -47.95715 | 2025-08-10 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e24b5012-a2bf-39b8-baa1-b674cf856fcd | -14.44741 | -47.85508 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e4783c7-ac95-39df-87d2-01661c125909 | -13.5993 | -46.93661 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9647dfc9-9f4a-33ee-978e-93f2a8730ca7 | -14.12036 | -42.13908 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b4cd5060-0785-341e-bca9-d96fa24523ce | -11.72929 | -45.01936 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95b222a3-c9b6-3773-9497-6aeaa0f7823f | -14.29976 | -51.97374 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c34a1750-5166-3fd4-aaa9-a766eb039a10 | -13.06177 | -56.84325 | 2025-08-10 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fa3cf27-932c-3e0f-87cc-95aecfc84261 | -8.91666 | -60.54411 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9133b228-99a1-331d-9028-14d7f5c950a5 | -14.46558 | -47.84988 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79e01dff-32cc-3dbc-b638-b88e3ae4705c | -14.4893 | -47.85694 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76cfc230-e3f6-369b-9464-b02316ae204a | -12.57964 | -47.14696 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ee5b60-3c17-36ad-bee2-b9da40d70320 | -9.49799 | -46.29576 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7fd6eb5-f87a-3044-9682-e8204e69d691 | -11.44211 | -42.31718 | 2025-08-10 04:46:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb8634e2-3f97-3c30-b234-6edcd349ade6 | -9.49328 | -46.299 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c51bdb6c-e48c-370b-8ce2-8c1ad99d4521 | -14.48661 | -47.84627 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c6b0ef2-6982-3e56-baa1-fec8cc0adb44 | -11.38106 | -50.55238 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f54aa8b-7811-3934-834a-8709e996fb7b | -7.06697 | -59.21583 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 573e4894-bd7c-37aa-a0c8-3b2809301552 | -14.10631 | -45.3947 | 2025-08-10 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 254a218f-0c85-3102-afe9-30d0e68b8872 | -12.69152 | -48.20098 | 2025-08-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de17c309-78e8-3d30-a8bf-7f05468fb308 | -12.68604 | -48.19766 | 2025-08-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
