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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66db9412-57c8-370d-875f-94a13b7cbac5 | -7.39981 | -44.76167 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e4cdfbd-f099-38bc-848e-3f9df046c154 | -4.90562 | -43.46678 | 2026-10-10 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ebfed71-59a3-3858-9a43-75f3fbc0908f | -5.59617 | -47.26852 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f454d3-bc03-3d9b-b0e9-f8a8b821702b | -6.22865 | -43.84944 | 2026-10-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75330f5a-68c2-314c-ba4d-1c3ad7320fba | -7.31955 | -41.78989 | 2026-10-10 04:08:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0b5edf7-8c59-370e-85f5-635b4a2d91af | -3.18453 | -50.59282 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c365cc00-71ca-3c40-b00d-64ecf59a24fd | -5.79822 | -53.80226 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5acbd73f-12ba-3d7b-9427-497d633e3063 | -6.41764 | -44.07418 | 2026-10-10 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70544139-336c-3db8-a965-dd772aa5809f | -3.25062 | -54.02142 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 813cfbba-b5e6-3190-869c-474fd756a4ca | -3.30351 | -53.99843 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8034d113-bca2-3e54-98f4-6feb05cce7bb | -4.09321 | -53.99237 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9912de4-601c-3037-b247-971bcae2ba08 | -6.07657 | -44.00901 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b65da594-2196-3bce-80b6-845a5d3bd324 | -4.10145 | -54.02441 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dfe661d8-c907-3890-b007-222280991d79 | -8.7761 | -49.60593 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8397a6de-81a5-3daf-95ee-93cacb1df140 | -10.27947 | -43.94976 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b42caf7-a2f6-304a-a926-9366d59760b4 | -4.83658 | -43.34904 | 2026-10-10 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0ec8957-8662-35bb-8dfd-465d06aba206 | -2.73166 | -54.14037 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9240896a-4fdd-3af5-a8fc-fa737c83161f | -2.52446 | -46.80168 | 2026-10-10 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 077570fc-fbb8-3499-b827-ac20dfb333e0 | -8.22979 | -46.37337 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 557f16fa-de00-3717-b82f-bfae7da409c2 | -4.09994 | -53.99326 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dbd54d7f-3d4b-3b55-9df1-4d10b515fe83 | -3.21405 | -50.5499 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8eefd90-c3ee-3ced-a5fc-ef873a9a05ec | -8.09195 | -45.63284 | 2026-10-10 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae011801-8b23-3c7d-8ffe-5212b8fbecae | -4.43123 | -43.11589 | 2026-10-10 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5caafce5-426e-3985-a08a-bc4958c73bf1 | -6.82353 | -39.55914 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| caadc0a8-fdf1-3e77-8009-b372b6149258 | -3.25799 | -50.42887 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c077700-0d8c-36a0-a63e-c52aa7c265c1 | -6.0658 | -44.66031 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1de4f48c-d62b-36c0-a63a-38a67799d541 | -9.20677 | -45.7947 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 139f249d-cb6b-3a4f-b8ae-5d98e56b3e7f | -9.94118 | -44.87978 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04f27256-ca2f-3270-b324-20d84f0a967e | -8.35668 | -48.14334 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 521df46f-c320-3c9d-b955-02576cab54bc | -9.32409 | -46.47783 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f99914f7-2047-3daf-8ddf-518ae8024af4 | -1.63152 | -54.41495 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 477964b4-2499-3eb3-b9d7-4519f49779f0 | -7.03813 | -47.66368 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6ca0f1ea-8bc4-3600-9e21-0604c121dd43 | -8.37595 | -44.1961 | 2026-10-10 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3892e2ca-97f0-3542-91d4-0e2fa4e7dcb7 | -7.57009 | -45.65695 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 806b20ab-c5c5-38bd-ac52-bbc813a02caa | -8.34385 | -45.00719 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb4f9bff-1056-3b5e-be11-b5339d1480c9 | -5.70834 | -41.64793 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3adb3e2e-0a08-3476-8a80-7cf64b69f0a9 | -5.51829 | -50.02607 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dec9cf1d-0723-37c4-a954-d199d0f7dfa0 | -3.3524 | -50.40899 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3e90b5e-2d73-3434-9000-c82a584f4765 | -6.08976 | -44.26241 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a10e1b2-63ce-3578-8101-5b278c99c530 | -5.88664 | -43.41466 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b5aada5-3057-33d6-85f7-d9723a6f0664 | -2.20745 | -50.82726 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54ae5ec3-40c9-3086-9b2b-498b97cfcb94 | -6.41134 | -43.73964 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 240382f6-82ec-3b7d-a181-0910df615f89 | -1.62651 | -54.42484 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a469357c-58b1-3928-9460-340a87f98929 | -6.43215 | -55.27224 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 834d215a-948f-35a4-a338-fe01485170c7 | -3.25243 | -50.3959 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f181df21-51e3-3ccc-9092-56eb96df5175 | -6.07957 | -43.99033 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 152bb2c0-140a-33d0-9f7f-db1ab8657e72 | -6.10666 | -43.0084 | 2026-10-10 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 742319cc-7d23-3421-b786-386d17aa392d | -9.93489 | -44.87476 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a359905d-e539-3415-8d39-3dfa62faf273 | -9.61483 | -45.98454 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dc7a51d-6925-39cf-af07-89ce8f36307f | -6.4517 | -55.28292 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1921fe7a-719b-3c3e-ba49-431fb3b5b687 | -5.87674 | -50.10049 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e205626f-85ee-32d1-87af-7b6d883f335d | -5.56046 | -43.96516 | 2026-10-10 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3842d08-faf2-32b3-88d9-9e8c9cb07ae4 | -8.97788 | -45.95084 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bbc0b84-9c56-3aa9-8a31-1a68b6699ccf | -4.22223 | -53.82602 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cc36cc49-d13d-381f-940e-84ac7805adfe | -6.46106 | -55.50146 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8c6d12e-47ae-3504-9dcd-741f1e094017 | -6.41476 | -43.7402 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7006bbf4-d807-3841-ac46-fef854648849 | -4.68339 | -47.4367 | 2026-10-10 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a281acba-7ecd-305a-9944-4c6e73b6ebce | -7.48323 | -42.85028 | 2026-10-10 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbc83bf2-3320-3bc2-8523-26a0248dd1de | -7.39814 | -47.77156 | 2026-10-10 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39f8eafd-7a1b-3069-85cf-118930f29d94 | -2.21716 | -53.69486 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3eecdd9d-647b-31a9-a20b-373c7a235ae5 | -6.50214 | -44.36217 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57b0b97e-a1b0-3327-8b83-9489a7331dcf | -10.28516 | -43.93587 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3df0761-4996-3643-876e-734c77a02ac7 | -3.27466 | -50.39592 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cca0ca79-f9b5-3597-96ea-89a8bdcb951b | -7.5349 | -45.31926 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 90709910-f3c1-3741-a497-167a0c75a143 | -3.2201 | -50.54722 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95cfe21b-0546-3be4-9895-e3ec423b2732 | -7.93071 | -54.72673 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06a04036-5291-3336-9081-d10432020f01 | -6.77801 | -48.66386 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 12.7 |
| bfad9100-33c9-3f39-8acf-1b9e3f458512 | -3.22023 | -50.55278 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fc99c6c-3592-3d42-bdea-6953cdcd0236 | -8.96406 | -47.44759 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b431d22f-a886-3b7d-9519-eda1530d8715 | -5.51317 | -43.04312 | 2026-10-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7953bc8-9e6e-307d-9f81-0f973906cf9a | -9.75681 | -44.78319 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da82fc79-b334-36db-9bee-3d8962c7c5d4 | -3.01397 | -51.01253 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 204cef24-8825-3d14-8314-2b1a44ddc053 | -7.2421 | -55.2143 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2892eb02-a096-3338-a2a8-63a0b193d770 | -3.10962 | -53.78661 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cbcac0db-b576-3814-9f12-0756e1a89f78 | -8.22828 | -46.38259 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b086277f-a814-33f4-b336-84d40d7b2fea | -6.47061 | -55.07127 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 85694e0e-1d9d-3de3-a67b-030533b39366 | -5.29883 | -37.33001 | 2026-10-10 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 65f07d07-9bd6-3767-90a3-0c2a7b863a92 | -4.43176 | -47.54019 | 2026-10-10 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e2d5f4d2-12c6-3bf6-b13a-5fc9185dc2f7 | -6.65504 | -55.33796 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a43faec3-e8eb-346b-baad-68c3b575e825 | -3.25858 | -50.42535 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 44959e28-dcad-3835-91ad-57b4aebfd76e | -5.87703 | -43.40937 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4da280e0-99ed-34bc-a3eb-a5e6d31f7d4a | -7.03065 | -47.6826 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8189456-e807-3ab7-9f10-efc4f8e26788 | -8.24114 | -46.42387 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e21cb078-4cc3-35c8-ae6a-1c4ef8a31b11 | -6.20773 | -46.64297 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a5f77ff-9db7-30fa-92db-953d076313e0 | -5.23177 | -50.68228 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b29b4b3-02d9-3bb7-888f-9eb2b1b3145e | -8.2396 | -46.42614 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 369f1717-fc64-397e-831b-6f0b14730023 | -7.21458 | -34.90645 | 2026-10-10 04:08:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2fff6da8-e93c-3c37-9fdb-0bc30d7ebf4f | -3.56771 | -54.67888 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ff906bd-28a5-3bb2-ae06-f15c5278fdb3 | -4.40753 | -49.78051 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38b38578-a5cb-362e-aaf6-cac094b4b8a4 | -8.25023 | -46.43303 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e3510b9-5684-3552-b758-9629c15bbf54 | -8.21258 | -49.70232 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ffea9e-7161-38ed-9be7-59f3fe9890e1 | -1.62931 | -54.42863 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b3203e64-236e-35b3-ac60-fb8bfa239837 | -7.10703 | -52.65239 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43d96bf4-7f39-3d5c-9fd6-841f1264a4e4 | -3.21463 | -50.54635 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccbf6143-9abb-3ef1-99e6-cb7ae50e67d1 | -6.1959 | -45.43066 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c520891d-a559-3700-98b8-d45bfea18bfb | -6.58631 | -41.56065 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6d16880-a778-372e-a2a2-2e856a985226 | -7.52833 | -45.31382 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d45183a3-00ca-30da-a883-0dbe5eb0d14f | -8.23577 | -46.42549 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 909546d4-820d-3e5c-be66-9bd6b4bd682c | -6.88314 | -45.91241 | 2026-10-10 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9658d4a-4a62-3b3f-8d93-bc401edec141 | -3.34929 | -50.41503 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README41.md)
