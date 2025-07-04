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
| 57c6348e-7e29-3090-9dbc-529d8659242c | -9.85483 | -44.71395 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b38eabcf-1742-3ea1-93ff-d7e567f87b2d | -12.42693 | -50.02642 | 2025-07-04 12:29:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 333.4 |
| 7e0f9efb-aa96-3281-8412-d41c2697217c | -10.56574 | -49.12989 | 2025-07-04 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e77fd826-4793-31a4-adb7-33424a9c3330 | -12.66614 | -45.28089 | 2025-07-04 12:29:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0d3df147-9103-3051-8f72-29f571b7536b | -7.7019 | -50.57385 | 2025-07-04 12:29:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f453a462-1b22-3cbb-b638-6797f1e3b6b9 | -8.84528 | -49.84144 | 2025-07-04 12:29:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d082aa79-17d7-383a-b238-6a9f9750419e | -14.54243 | -47.03246 | 2025-07-04 12:29:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77cc0562-d890-3b19-87e1-d991bc07c8bc | -7.09823 | -49.16758 | 2025-07-04 12:29:00 | TERRA_M-T | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 88984386-2f50-33cd-aeae-c8a853e9ea88 | -14.24245 | -47.03114 | 2025-07-04 12:29:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c0afefd1-b74b-3fa8-894a-56609f0df70c | -7.85788 | -45.12156 | 2025-07-04 12:29:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 926bdf0e-2c62-3bba-aaef-5addcf811777 | -11.86622 | -44.86431 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e3e540fb-f694-380a-8ac7-4e65ff8b026e | -10.64222 | -49.42324 | 2025-07-04 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 595cdbfb-689b-3081-812b-872f9b9b88fe | -10.37895 | -47.0027 | 2025-07-04 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 88a20f48-5766-347e-9eea-e5106c8b405f | -15.29858 | -47.99123 | 2025-07-04 12:29:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7aed21a2-a50d-3f6f-9b83-9ffb77b18706 | -10.25535 | -48.14456 | 2025-07-04 12:29:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0bb61878-d691-3246-bb10-19237f902ebe | -10.59064 | -49.45545 | 2025-07-04 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb842ea7-23a3-3794-8542-17f9b1d487de | -14.64446 | -44.17845 | 2025-07-04 12:29:00 | TERRA_M-T | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b4ab158d-3341-3a05-81ac-eba66082f1c6 | -7.6163 | -45.7448 | 2025-07-04 12:29:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7acba35d-1ca8-34d6-be79-3a1e9678589c | -13.69372 | -47.74355 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba4664e0-5b34-36b5-a7ce-0337b5856b2d | -11.57168 | -44.84673 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 1bd9f9de-4d30-3e57-875a-c8d5c9b869ac | -11.45527 | -45.11335 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| aaf09cec-4e03-3413-b32d-2cbc11eac43d | -9.0806 | -44.32163 | 2025-07-04 12:29:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| afb17a5a-cd85-3e70-9469-37deb7f45f53 | -9.08332 | -48.33213 | 2025-07-04 12:29:00 | TERRA_M-T | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1aa2a984-0f09-320b-a556-29e54322340f | -11.56113 | -44.84539 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 64be44e0-60fe-3f29-b5ed-c5566fcadb44 | -13.57147 | -45.24303 | 2025-07-04 12:29:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f99c461f-f725-3bd8-bf40-054ab113d470 | -7.84748 | -44.21182 | 2025-07-04 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 42bfe43c-ef9f-31d3-9b9e-a8006c07bce7 | -11.10495 | -47.01545 | 2025-07-04 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b13aff17-09a0-333d-a6b3-baed8bd7475f | -12.42558 | -50.03563 | 2025-07-04 12:29:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 428.1 |
| 23f312f5-9ddc-3de6-bb02-2dea0720cb4a | -13.38848 | -49.12422 | 2025-07-04 12:29:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f12e5e62-abcc-3661-b5f1-55e7c41f718a | -7.91645 | -44.54152 | 2025-07-04 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f16dbb15-24e0-3381-b53f-76ebcbfb975c | -9.2363 | -47.00098 | 2025-07-04 12:29:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 15b7c9da-425c-3ee9-a9a7-4d73ed68dfed | -7.85941 | -45.11044 | 2025-07-04 12:29:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 58e04f4b-ffbc-3895-9abd-34207689f536 | -11.5734 | -44.8336 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 272.7 |
| e0d7e829-e658-37d1-b768-3e6d8a0c0734 | -12.41665 | -50.03429 | 2025-07-04 12:29:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 31fe4a9a-5f19-3918-8f07-d4c622fbf050 | -15.29993 | -47.98139 | 2025-07-04 12:29:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdfcf5d3-44e1-386f-a95c-3060a0a61381 | -11.49221 | -43.22489 | 2025-07-04 12:29:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 917cdb8a-e8bb-316a-9859-c66fe44d8d81 | -11.11277 | -47.02644 | 2025-07-04 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 46dd4853-b552-3a2c-8eb7-631462d933d1 | -8.45123 | -49.63389 | 2025-07-04 12:29:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d9698576-5dbd-3118-baa8-b2d22d09cd3d | -10.82008 | -54.03072 | 2025-07-04 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 028efbd3-5fd0-3b07-a6fe-96ee3c71f1ae | -11.53941 | -47.86162 | 2025-07-04 12:29:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 822d7b2b-8f19-31d9-8465-7e6e8b698f38 | -11.54834 | -47.8629 | 2025-07-04 12:29:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 01d7d69c-abd6-3445-b229-02685bef7a6f | -7.71143 | -50.57521 | 2025-07-04 12:29:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cb9f4b14-0c0c-30df-887b-9c06e90b921a | -10.38029 | -46.99316 | 2025-07-04 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 9dce7e9d-96a8-398b-909e-541eea9189a2 | -12.41801 | -50.02507 | 2025-07-04 12:29:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b3aed8f6-dc8f-3d1e-8c95-0a9d063927d4 | -8.86584 | -47.2728 | 2025-07-04 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6a44cc38-322d-3af1-9e14-36d185e5b22e | -9.85652 | -44.70137 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 9c964713-dbba-317a-9a0f-930d52164f5b | -11.56284 | -44.83223 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2facc8b2-bbec-3822-b623-358c8c7ba352 | -13.44431 | -47.81343 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ff2346b2-3753-36c2-89fb-62b482a7260a | -7.70033 | -50.58426 | 2025-07-04 12:29:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 60e4c8e2-bf73-3f05-a2f3-807554a32977 | -7.66702 | -46.95109 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eaadaaa6-7200-3273-a1b5-1a900495de50 | -11.53811 | -47.87081 | 2025-07-04 12:29:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a1415b0f-cc6a-34fd-ac60-db68da49c1be | -12.65575 | -45.27952 | 2025-07-04 12:29:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d7ad3c37-966e-35f9-8d24-a83f195778cc | -7.61406 | -44.50745 | 2025-07-04 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9e605e38-1078-3bef-b74b-94e3b9d4c7d3 | -11.92865 | -45.38774 | 2025-07-04 12:29:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a5d99142-363d-3eea-852d-2343bb4690a3 | -11.91847 | -45.38631 | 2025-07-04 12:29:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d4875cc3-d9b7-3684-a4ca-245c88fabfe0 | -9.22031 | -48.59946 | 2025-07-04 12:29:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4db9fc83-40b9-33c6-b20e-e174926597fa | -11.11141 | -47.03619 | 2025-07-04 12:29:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| dab0bdbd-b8bd-3201-8f10-a4676e673818 | -11.44495 | -45.11201 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 85a0cd33-60ee-338e-a9f0-00e6eedb8f53 | -7.66831 | -46.94196 | 2025-07-04 12:29:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6861c093-9f91-323f-ba25-698a679f787a | -16.93694 | -46.09906 | 2025-07-04 12:29:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 90ed07df-82ee-3146-82c6-563634fd03ad | -14.54342 | -41.99133 | 2025-07-04 12:29:00 | TERRA_M-T | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 771291ef-2ca7-3474-aa37-4d2abbade23d | -11.54704 | -47.87209 | 2025-07-04 12:29:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8b4d789a-007c-3f36-8651-68dcc8e62b81 | -9.79617 | -48.25711 | 2025-07-04 12:29:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 41e4fa27-a424-323a-a34c-1c5c9de4bcf6 | -8.45262 | -49.62457 | 2025-07-04 12:29:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57a4ee4f-8a4a-3ff1-98c0-101289efdb4b | -7.63667 | -44.33661 | 2025-07-04 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b850a718-9245-3d14-a6f7-26906c264b79 | -7.09688 | -49.17682 | 2025-07-04 12:29:00 | TERRA_M-T | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7a0838dd-19a2-345c-a016-1b5d306ec4a8 | -8.73623 | -50.25847 | 2025-07-04 12:29:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 522cdd2e-0f41-399d-b9bb-af0b648cb93d | -9.22159 | -48.59058 | 2025-07-04 12:29:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 43a2b36b-538d-3b72-a5a5-38b8d9f46ead | -11.67084 | -44.62156 | 2025-07-04 12:29:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a123df4e-f1e1-3388-b5c6-e5ca77676652 | -12.66775 | -45.26817 | 2025-07-04 12:29:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8fcb32f9-66f6-3ffb-8465-3ceb17ae7b6f | -15.2744 | -42.53582 | 2025-07-04 12:29:00 | TERRA_M-T | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0605c7c2-245c-3fd4-974e-90178e76e92a | -11.56123 | -43.30898 | 2025-07-04 12:29:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1f761104-ce7e-3e4b-996f-4b1d8d84d5fd | -6.005 | -44.5418 | 2025-07-04 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e438d534-7788-31cf-98c0-13cf9cd1bf4b | -12.427 | -50.0387 | 2025-07-04 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 458.1 |
| 7cddc0f1-9506-30b0-b6ed-2a85799e9eb0 | -6.0052 | -44.5189 | 2025-07-04 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f63ba478-726b-3589-aea3-43831dbc2d39 | -12.4274 | -50.0171 | 2025-07-04 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 300.6 |
| d69eea85-d92f-3133-96ec-c0166743206a | -19.16437 | -49.13855 | 2025-07-04 12:32:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9db9f556-c275-397f-8c1b-da376382dcb8 | -20.26786 | -50.73002 | 2025-07-04 12:32:00 | TERRA_M-T | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| c0195a50-282f-311f-bd7b-50e82be13b2f | -19.91304 | -47.47037 | 2025-07-04 12:32:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3fa88641-6450-3ec1-aed9-0cc6c686415c | -18.68921 | -51.80307 | 2025-07-04 12:32:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 470cf22c-2341-3bec-92ad-5f40693ddfce | -18.81612 | -49.59651 | 2025-07-04 12:32:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 6f25b57f-18a1-3ade-943d-ee193cb189d8 | -19.75117 | -53.99802 | 2025-07-04 12:32:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57a3e800-a107-3423-9780-0468000b5afb | -18.45093 | -54.66693 | 2025-07-04 12:32:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7017a7d6-b57f-364c-a299-7923f441595d | -30.5603 | -52.69057 | 2025-07-04 12:34:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 22.2 |
| 241cc9ba-15c4-3e7f-9b39-f5cbb9d7bae2 | -30.9227 | -52.26226 | 2025-07-04 12:34:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 11.1 |
| 65dfde8d-6ef0-3b8e-ae31-dd18fc59dfaf | -30.55887 | -52.70087 | 2025-07-04 12:34:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 41.7 |
| 6d711395-8da9-3428-85c1-be994f786a28 | -30.92129 | -52.27274 | 2025-07-04 12:34:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 27.6 |
| 2e3e2a21-fe03-3e0b-ae7b-8b0f83ed53c9 | -12.6636 | -45.2776 | 2025-07-04 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e504e75d-9beb-329b-a98c-d7b05363af74 | -12.427 | -50.0387 | 2025-07-04 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 433.7 |
| f900dc02-ad6f-38a0-ac30-727d782216f9 | -6.0052 | -44.5189 | 2025-07-04 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6f60c849-9e85-313a-8ed5-fa72d8f31f7c | -12.4274 | -50.0171 | 2025-07-04 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 279.8 |
| e4f56f62-4424-3b90-a78e-ded9906ac158 | -6.005 | -44.5418 | 2025-07-04 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| da4a98d3-4929-3385-a297-a07bd22c9635 | -12.4274 | -50.0171 | 2025-07-04 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 277.9 |
| fea31d83-7f71-37e4-91a9-07a89bb5df29 | -12.6636 | -45.2776 | 2025-07-04 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 67db88db-1548-3cd6-bdc9-5d9458806481 | -12.427 | -50.0387 | 2025-07-04 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 534.4 |
| 657e56a2-7c65-3317-a4b4-b62a3fbe9a5d | -6.0239 | -44.5174 | 2025-07-04 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 63246e68-2110-30ef-af95-35c9be53e2db | -6.0052 | -44.5189 | 2025-07-04 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b1304b0c-00b3-338f-ba70-c1e100d640f2 | -6.0237 | -44.5403 | 2025-07-04 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 3a7da43b-dc37-3de3-96de-12f14e68af49 | -6.0052 | -44.5189 | 2025-07-04 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f3dfb5cd-e879-336c-b11b-9e330966a5d8 | -12.4274 | -50.0171 | 2025-07-04 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 329.9 |


[Clique aqui para ver as próximas entradas](README24.md)
