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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5c71608-ef4d-3c24-b03d-df2fdc9443cc | -6.3145 | -43.62641 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99f6536b-d703-3502-a70e-3559b1c3c8c4 | -6.2847 | -43.58157 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c055ffd5-d6a0-3e16-8b0c-a50c098b6ceb | -6.29914 | -44.75195 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ae48da4-5fda-3815-b5d8-9c733e9756bb | -6.82167 | -44.26974 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 539e2130-e52d-3045-b599-4ff86454e920 | -6.97711 | -43.27773 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3a1edce-e010-315a-97cd-df026b7be7aa | -6.69496 | -48.39506 | 2025-09-03 03:53:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0c08eff-7521-34ac-9326-a6b52e012c5a | -6.28147 | -43.59841 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c62dc7f-32ee-3a02-a401-061d210e525a | -6.05666 | -43.42143 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e894e00f-8a99-3385-beec-d8bbf234b063 | -7.90954 | -46.47956 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0555395-ecab-3467-b455-8e41e22a106c | -8.46376 | -45.06432 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dba81892-8fa5-33c2-bd7a-7681f49fa9cc | -8.0242 | -44.05821 | 2025-09-03 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a259cc5-7af9-39c5-aa81-ba6f3eb5e535 | -7.70511 | -48.73367 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb8d8f45-ff01-3552-8d33-94ee60aea7df | -6.57256 | -47.38614 | 2025-09-03 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7926ad2-ea60-35ad-aa2d-a47064817f55 | -7.93408 | -46.55782 | 2025-09-03 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e67ee12a-b0a2-3144-a9d0-4d6cb3264067 | -6.37205 | -42.99791 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302f1545-e66d-381c-aef8-9c8f0d999cc6 | -8.4259 | -47.34408 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9e9653-1004-30b4-a077-51dd9339e4d6 | -6.23055 | -43.38173 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1aafee7-2b42-340a-9c01-68366b9bb22e | -6.85307 | -45.54513 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8139c8fa-a8e2-30f9-b5cd-f04aa2617994 | -6.45619 | -44.6793 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f3a9934-f582-3901-bbe7-3f5ca9132b1c | -6.26995 | -42.5975 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c3c91ad-65c8-3e22-b4fc-384988d5cf0e | -6.23224 | -42.42881 | 2025-09-03 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1965bf55-46a4-31e0-9334-085baf66834a | -5.89821 | -43.34789 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 758878aa-15d6-3f99-914f-1982b4f6aea6 | -5.94138 | -43.71922 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9dcf41e-6ad0-31fb-a9f2-62063b309742 | -7.79737 | -45.44754 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40077613-9693-3c1e-bc7f-3a6fa5187427 | -7.48838 | -44.82045 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 27877293-c171-309f-b91e-b01c183ed4fd | -7.4811 | -44.81062 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| abcf539c-eb00-3f18-96f6-7dd594941a9e | -6.32855 | -43.51844 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02eafbac-4e15-3c25-a2c5-f14e56494366 | -6.45232 | -41.74596 | 2025-09-03 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1bc7bbe-83f5-3223-a98b-84bdf0b3b477 | -8.36851 | -48.29967 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d84ce7c-6823-38c3-b908-a02e06d517be | -7.50277 | -45.33525 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba22565b-c384-36e1-a817-955405c33963 | -6.5778 | -47.38713 | 2025-09-03 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15f4fd07-8f2c-32cd-9d03-38864fd785bc | -6.6936 | -44.18 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77ae18f7-a733-34b5-81cf-f39f6f1a874e | -8.01555 | -44.10952 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8d1d4480-22cf-3b18-9d0e-987e89fe91f5 | -7.0044 | -43.23512 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ec35dc29-a9ab-3120-91f8-e38b0c52fcf7 | -6.75485 | -45.91267 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14230c0e-5047-392a-a285-f275241309a1 | -8.07118 | -45.36984 | 2025-09-03 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8da726cd-f2a7-363b-955c-5685a67f8969 | -6.23216 | -43.39666 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca52739-2a5d-3f84-928d-0117ad0b0e7f | -5.93861 | -46.47617 | 2025-09-03 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47ec92ad-ef8b-315c-b5ec-cf485004c2eb | -6.07887 | -46.81997 | 2025-09-03 03:53:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d9277b4-9000-32d4-ac57-2c7187931b0e | -6.97488 | -44.36289 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d6b2ea3-9c2a-317e-a420-0b521215a974 | -7.93478 | -46.53477 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6514b723-5063-3cd6-ad91-6ddac66f52c3 | -6.25301 | -42.60458 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 426f33bb-0bd4-3806-9170-68951f7b5ea2 | -7.55504 | -45.70969 | 2025-09-03 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff9bdd99-b117-3b05-84e1-47e7e08081ef | -5.89701 | -43.35501 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5921eb72-5a0c-3d30-9055-8a934f5674cc | -6.22069 | -43.39101 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01971bb2-dfbe-33bf-97de-3322102a4e63 | -5.42242 | -47.11625 | 2025-09-03 03:53:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d8e5a72-7f88-33f6-8e4d-2fec790ad0c4 | -6.02464 | -46.00932 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f54f3eb-1221-3316-8d0f-2d3229d277ac | -6.98104 | -43.10721 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a645aa92-db76-3bb0-8c22-835e54cfa7cc | -7.93588 | -46.55721 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d8fb79e6-f44e-3a20-bb13-d14467d0d8da | -7.6972 | -48.74512 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0d785a65-6338-333b-b141-180a58ab76f8 | -6.02946 | -46.0102 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab7bd4d0-3884-3f21-830a-40378eb91b13 | -7.47023 | -44.79563 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2172874d-6247-3a88-af03-491f7cb73c09 | -7.90073 | -46.44499 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a82a72ba-d0fd-36be-a458-e6970173a8f0 | -6.84092 | -45.53313 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fa19837-a4b8-3f50-afe9-95286f3187fe | -8.00859 | -44.79042 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1fd9612-702d-34a5-9284-fd62a1f47ee9 | -6.62996 | -43.96308 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a96a1e7-24b0-3458-8745-069d5d4143a7 | -6.29432 | -43.59686 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f3ba0dc-bdb2-3a57-9562-2e99c42b64d8 | -7.11406 | -44.31026 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cbb908f-0fbc-31a0-9a63-bd6c6c750e02 | -8.45063 | -47.35218 | 2025-09-03 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7481e011-f500-3fa1-80b3-39cd52c4d0e5 | -6.99577 | -43.25702 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ac9d312d-a6fd-35aa-8819-d6a763496363 | -5.89968 | -43.38826 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 239b8edb-64bf-3175-9e3f-9d8b80c77d6a | -9.1633 | -45.20305 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aa4aa20-ef4e-3643-bed1-015eb78c2016 | -7.50426 | -45.34201 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74a492de-ed7e-389a-aa27-e09260020d4d | -6.37514 | -43.00367 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ce3ced9-70cb-3a5b-b7e1-4d8155b22206 | -8.83407 | -45.77216 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b26d4ae4-e639-3415-a266-948ad52dd904 | -5.85241 | -43.00072 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6fa6f7a6-a90c-331c-b269-cabf1e202a7c | -6.19812 | -43.34769 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b780ef82-abf9-3312-9cb0-14c13e94772a | -8.87712 | -45.82456 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a4a3e62-6f41-3c02-b6e5-97d54f413482 | -6.496 | -44.09097 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac36aa74-2eb4-3b0a-a4e3-561e0fbfcfd6 | -7.92869 | -46.45535 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98426d07-8c3f-360d-98a7-6001c330e135 | -7.89886 | -46.45552 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd4ec16d-a7bb-368b-acae-b1dd49c6c6ed | -7.94475 | -46.55416 | 2025-09-03 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bf455ce-c08d-328c-b453-7442f7092fdc | -6.26219 | -43.51529 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93cc5fc7-7e26-3651-861d-35ffc89d2c7c | -7.91795 | -46.43175 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 451a7144-ac62-3648-9bcb-a2b5d15e68a5 | -7.50056 | -45.33653 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af01014c-e8d0-38e3-86ec-a9be6a58f1c4 | -5.60716 | -45.01733 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6fe5e22-91c4-3126-b186-1998e02421cb | -7.47801 | -44.83464 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 495b7bfa-fe5c-37e7-9b8b-1175beb744fb | -7.4042 | -44.01467 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267c2cbd-92c0-3148-ba88-48ad5f6a7e19 | -6.5135 | -43.5087 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1feb4bf-a1e7-36c3-8759-cf048d26fb1d | -8.38033 | -48.30531 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7680268-216d-306a-9b62-527c6a0679eb | -6.26612 | -42.59689 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e7fafb42-ac50-3d14-b903-107dc6801e8e | -6.23276 | -43.39312 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05e26a7e-d4c7-3c1e-982d-25fe86c71d7f | -5.43128 | -45.97931 | 2025-09-03 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a81db2f3-70cb-3b3b-91ca-9df44850943c | -6.62642 | -43.95871 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e41bc99-e66e-3ef1-92d5-d2b175fe3a87 | -6.75395 | -45.91774 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e157de4e-9173-328a-b8ff-75e25dd9faa4 | -5.90445 | -43.22938 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67e4df4b-be33-3b75-b6e3-9beb8a090d1f | -5.90044 | -43.22874 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eab94cfa-e882-33b7-a570-58a7abef4c9b | -8.3631 | -48.29873 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76f8caee-2d01-3671-a03d-0247fff32426 | -9.61346 | -40.6155 | 2025-09-03 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6822b521-91a2-37c9-afb9-fe498f70fa9d | -6.65166 | -45.90709 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8650893-2637-3330-905d-327f171f50fc | -6.69294 | -44.18394 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c292645-e273-3bf8-ba46-6ab80eb78142 | -6.64244 | -44.09937 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bde9bcb-6091-34f5-9255-648138b5f8a3 | -7.0032 | -43.23731 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dcb4575a-963d-346a-a85b-07b881a45ad1 | -6.94208 | -43.2927 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d29b6f6a-5178-3fb8-938f-b3c112d2853a | -6.264 | -45.05937 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 694836f1-35f8-3ab2-b2d0-1035ccf8d024 | -7.24139 | -42.54235 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07b646c6-8d52-3ee3-a7bc-d097c716c56e | -5.69279 | -45.39496 | 2025-09-03 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32bd155f-2be0-3eaf-b6e5-8e1222737971 | -6.73138 | -42.25208 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c13515b1-1c00-3772-bae8-fb8639fe3dde | -6.84199 | -44.27664 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3988dc7b-b020-364b-bd6b-fe66155d6017 | -8.05271 | -45.37025 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README30.md)
