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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7e22bc-aef0-3725-a494-eaeeca118b25 | -12.32286 | -50.56757 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 04710c92-41d6-30c8-b1b5-60c7027970b4 | -9.88263 | -45.85115 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2a796de0-c57d-3373-8fd8-c50b4765be09 | -11.48509 | -45.07476 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cc550184-fde3-39d9-bfc7-c0271974a2e3 | -11.82728 | -47.22761 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0949b4f5-8093-32fd-b9fc-7e4af56b4778 | -10.08632 | -46.97495 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3d0cf43c-be24-37e8-88eb-b00d39005b42 | -11.32899 | -48.37402 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b7aabe5a-f7ca-3de2-87c7-be761a7b04bc | -11.23892 | -45.05845 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f6edfdf5-1121-3645-a163-16f14cb94654 | -10.3338 | -49.98444 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f909fbee-9822-3c63-affc-a44ca5eae299 | -11.16238 | -45.05873 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 87c9a073-a1d7-3101-8ed1-590c53e54ae8 | -11.2268 | -45.05039 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 365cba4b-c1d9-3b0b-8205-a8ef2eac7f55 | -4.85036 | -45.39815 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 96d2dff9-56e4-3c99-8253-60db63f65d73 | -11.0766 | -47.11557 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3eab27d5-35be-3352-a9ec-0d1dc913a4d7 | -11.32958 | -48.37884 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 98734608-9adb-355d-92a8-630f6cc40fcc | -10.90036 | -46.62814 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39809e7d-efdc-31c0-b0e2-ddb948fab9e3 | -4.15101 | -43.09814 | 2026-08-28 16:07:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f0185540-d424-3509-a2f5-328eba94a2e4 | -11.70149 | -47.61505 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a0db1c03-6363-3cb0-8545-44732cdc02f4 | -10.91765 | -46.62641 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b1ea4b7a-1a34-3c7c-8425-1ad2bd82ead9 | -10.79569 | -39.37371 | 2026-08-28 16:07:00 | NOAA-20 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5c1548f2-ddd0-3534-b987-0b4114b38fdf | -11.84886 | -47.21901 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dc779d4d-fcde-3c96-b42a-a55e0f6e6084 | -2.23512 | -47.71467 | 2026-08-28 16:07:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 383cbaf0-d90b-3a1d-9f64-a9e8a96eaa6c | -11.7633 | -47.62981 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1b49cf30-ac3c-3373-9a11-1d7c5ea1769e | -12.31864 | -50.59657 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dddd0ca7-570b-3fc9-8c49-5226043340fe | -1.61741 | -48.10613 | 2026-08-28 16:07:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 46bf4b0d-c417-3b3f-9980-257a9f48f153 | -11.35671 | -48.39571 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e823fe07-d6e7-3319-bc18-5f10975fa164 | -10.95186 | -50.29145 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6550a23b-b660-3ccb-af4c-684f558e93b4 | -11.4858 | -45.08046 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c8be9fb0-323e-3fec-bb3e-53ecaf7cb9b4 | -0.2896 | -48.92384 | 2026-08-28 16:07:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97862702-9c03-34ec-936f-afd1aec1dae8 | -0.52737 | -51.80933 | 2026-08-28 16:07:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53dede99-debc-32cb-91c0-460619fb53ff | -2.99674 | -48.95378 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ec3c5742-afd5-3814-95f5-52b90f5ac1e1 | -9.82963 | -45.90291 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 090a88b1-11e9-3dc4-b832-eb14ab31c063 | -12.03958 | -47.17737 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80b1de52-56fe-3b68-82b6-5fa62897b4cb | -11.25099 | -45.03386 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 24ac945b-6ce7-33ed-9141-464156c5e08f | -9.98601 | -36.38117 | 2026-08-28 16:07:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ebe2f64b-138c-3e05-acb9-09ba94dbbcde | -12.33145 | -50.58089 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6c466314-4a68-3cd3-8b43-7983d11d5b13 | -9.04009 | -41.60692 | 2026-08-28 16:07:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7fe9ca50-fb9a-32a3-bf8a-a613346c8dc2 | -11.24661 | -45.04776 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5c891709-aa91-35d1-8d78-7b60c9082fd5 | -12.21906 | -50.54589 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c03d17cf-7b55-39cb-a84e-848439204f0c | -12.08098 | -47.18057 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8517fe03-fc46-398f-8ce9-14bf24c1c30b | -10.2166 | -38.52386 | 2026-08-28 16:07:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3b129ef5-837b-3b5e-8fe8-11b88256b94e | -9.83003 | -45.90599 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0615a43-fe6f-346c-bfaa-db45a13b356a | -11.23824 | -45.05287 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 70020a07-7c2e-336d-9ba8-9ff6a20a6aef | -9.89287 | -46.34589 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 963fba5a-dd4c-3d6e-93d0-f23089fc3c56 | -1.84035 | -44.68398 | 2026-08-28 16:07:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7c16b62a-0b50-3c2d-9460-941d747fe040 | -11.02097 | -45.07579 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ba40c45c-0ba9-3e24-aa5e-be342b0248dc | -2.28453 | -50.54428 | 2026-08-28 16:07:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cc4c3972-19a6-3e3b-afc8-8f10097e7ebe | -9.7355 | -45.96175 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5071f7bd-04e9-3ffc-9aa7-cbfd356419cc | -12.32202 | -50.59306 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| f528c127-2a13-3c84-9696-89b37b6e43de | -9.86091 | -45.84447 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a15912cc-1dc3-3544-a111-dee1db0e33b3 | -11.2488 | -45.0644 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 4123e9c7-add7-3732-b350-fbb96391b8cd | -1.57865 | -47.73898 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 52fcfdfa-e4e3-3866-8e06-fdc2714aa054 | -2.73046 | -47.05469 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4683d35-0638-3fed-a767-068f050f7d93 | -12.31489 | -50.59381 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7588b227-3509-33d6-a516-d23a0242bdcd | -3.02676 | -43.62089 | 2026-08-28 16:07:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16751629-baae-371f-a1ff-0a07e2c2251c | -11.25155 | -45.04699 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 926ef9d7-d819-3c3b-bbc8-31628ad3a50a | -9.69118 | -46.56296 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7cdfc8cc-4530-319d-8510-6f20d89185f7 | -12.22347 | -50.54683 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3387b62d-7713-38d0-a3a8-03e59e24cb87 | -12.20562 | -50.55441 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f0ae1452-240a-3b01-bd1d-b951087e04fb | -9.88642 | -46.33779 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8b64f5a-feb3-33b8-a5d7-7b85770ca6f5 | -10.54601 | -50.47993 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac46c4f2-f75f-3a8f-ab05-f94f5ad6a114 | -11.82776 | -47.23175 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 533077d6-2645-347c-ac7a-91ad8c220859 | -11.79887 | -47.6748 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 40b58274-7b29-3d78-9a83-9ae427db4051 | -1.96552 | -48.37337 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8b318f7c-2d29-3e3e-8ac4-3556a437943c | -9.86013 | -45.83836 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e367ee20-5f90-3666-b7ef-f234b3dbe0f0 | -12.32761 | -50.57823 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 235.9 |
| e974e27c-fb64-34bb-9a5d-89caa47d86d5 | -12.05734 | -47.18592 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe053ad4-37b7-38e1-b21c-98fd7b927ac1 | -9.88856 | -45.85668 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 50dd0f3c-7125-3d47-a5c5-3624e93cb8f8 | -11.46729 | -46.94627 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6e42f8d9-f445-3255-a502-ebdfd0735acd | -11.84367 | -47.2173 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ee7c8e10-f270-32f1-8137-bc75b8fd4f6c | -10.92228 | -46.62514 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7b7c4f51-a9c7-3158-bb2e-af33970ecd0b | -10.6375 | -45.22535 | 2026-08-28 16:07:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d02e130c-a080-3826-91e3-600c1abb6237 | -9.85748 | -45.83701 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ab353c2-6154-3d18-a762-476a0288fd55 | -9.88185 | -45.845 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| f43fbb24-4de5-3d23-8708-0d39fcee302b | -12.31646 | -50.5754 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2c8e410c-0cf0-3798-91be-48ad3a6f38a8 | -3.05948 | -48.7465 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f3550c91-c78a-3fe3-8268-138aa2da7764 | -2.72501 | -47.05254 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d79abe2a-ce82-32ec-8e16-6bdd1421d138 | -10.01793 | -45.62885 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ffca267-93cd-330e-92e5-5747a4d9a402 | -10.08778 | -46.98632 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 87945ce1-ec3b-39db-bf1d-31437504bcae | -12.33071 | -50.57384 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 0e790360-6e1e-3a2a-b8d4-42e1c6db9483 | -2.82765 | -44.37623 | 2026-08-28 16:07:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0021ccc4-4ec2-363c-84ab-8232adff67f8 | -1.5805 | -47.75135 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| df66e159-34cd-3c6f-ad53-06c79ea0b248 | -9.87156 | -45.84623 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7235c17-345b-3dec-95d8-24562d9a7da4 | -9.86129 | -45.84753 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d53e3603-fda3-32f6-b332-42fcb270e6ff | -11.83306 | -47.2269 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b5fec432-ef1e-374c-be4a-c94980b80c1f | -4.08439 | -40.12515 | 2026-08-28 16:07:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 71d6a307-08ad-3970-bb82-fc393c1940ad | -11.84463 | -47.22552 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b77fa9f0-364c-32ca-8ca6-1755b95a8b23 | -1.78419 | -45.77469 | 2026-08-28 16:07:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 29.3 |
| fc3ae5f0-3c20-34be-bece-294f8cd171a6 | -5.44062 | -47.53553 | 2026-08-28 16:07:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b6cf9e23-fb5d-359e-aa77-3525d4e4d641 | -9.79262 | -43.55946 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| c2818609-90d6-366d-a50a-0f4b3e2d15e9 | -9.66678 | -45.71489 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 471df6d0-2ae6-397d-994b-10b6c81927a7 | -11.81996 | -47.22236 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 996d1305-2ebe-3a11-b28a-133e6f015ae1 | -10.92321 | -46.63241 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 679d422c-43ac-3046-bdac-9e0a9d829c93 | -10.9286 | -46.62484 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a81d7f87-564c-3521-b651-1052781dd418 | -11.80187 | -47.67163 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| aa2bd221-94f5-3a33-b344-2cc2c06bbfad | -10.33381 | -45.35505 | 2026-08-28 16:07:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| db959c21-1115-3c19-8b9f-1c9870548195 | -11.16227 | -45.58204 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 7972324f-7937-3253-965b-b32bad4d9fd6 | -11.59229 | -45.39691 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 737c69f9-5e96-3ce4-9fff-9369a16c3f4e | -9.79205 | -43.5552 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 64a68ddf-e022-3a98-bb90-5f7e74ad69c6 | -3.93242 | -44.90744 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b029fe23-2f52-3985-927c-d915ff4f718e | -11.83831 | -47.2286 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8dbf83f8-1c44-38e5-9697-83b6ae314ecf | -4.84964 | -45.39917 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |


[Clique aqui para ver as próximas entradas](README96.md)
