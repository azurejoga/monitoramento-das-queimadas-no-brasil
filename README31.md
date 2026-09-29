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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc187043-cff4-3b15-9dae-b7ed17025926 | -15.8396 | -49.17147 | 2026-09-29 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e402556-b8d7-337a-b8a6-9f18df5d9215 | -14.48835 | -43.25986 | 2026-09-29 04:17:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7da24deb-a2ca-325f-a9db-c1ebab6d985d | -11.65448 | -43.51678 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8137292d-a593-3961-8406-33dd661612ba | -11.61094 | -46.78925 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a694ff98-66ac-3038-a1b9-0b7070f2317f | -10.79417 | -48.74931 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c433613-66ff-30cb-9f78-b5ec337d273b | -11.18427 | -45.13772 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a53cd094-8135-3f85-97bc-97576e101707 | -12.01047 | -50.94757 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f2c5429-77a9-3c7f-8da5-1fb64a96eb28 | -11.07085 | -48.90217 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bf37316-1f12-3927-b4fa-7a490a1338de | -11.41357 | -43.42459 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2818c8f9-ac41-319a-af67-2165a7757ec2 | -10.92846 | -47.59103 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e4c7a86-9c1d-3c36-918e-1b5fad7f049a | -14.86213 | -47.99126 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38c11dae-8b55-3137-a708-7b9e36213ed9 | -10.28295 | -44.63824 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87ace8b9-b268-3f83-8649-4ebdbe8cedc4 | -13.86773 | -44.00093 | 2026-09-29 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5576a297-74fb-3448-b5bd-74001a9071be | -10.29653 | -48.17152 | 2026-09-29 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45bcc451-8111-32cb-b243-4c068c85d38a | -12.396 | -50.2221 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a73307db-8d26-3780-aae3-60ce8ed4b62a | -13.20687 | -48.56292 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bf4d638-c01c-3216-bee1-fb450d9242b0 | -11.71427 | -43.45707 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de82ddc6-2e30-3777-acc2-75f4facd08cc | -11.50465 | -47.40541 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a537724d-6947-3f49-9460-908b72dc6cfe | -16.42256 | -43.29775 | 2026-09-29 04:17:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dbe9329-2619-3392-8578-299fd0c6f6dd | -10.81594 | -48.7378 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02560646-9828-359f-ac61-06c086b54f45 | -11.20058 | -44.79784 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 332896ae-1353-3ccd-8144-f761db7a1429 | -12.73437 | -47.26677 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 46618ef7-638b-3adc-9f11-5e65d262276c | -13.73746 | -43.66887 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1f63c6f-5f33-3e37-a7b3-c71140d1b9da | -12.77017 | -50.6708 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 410929d2-b97b-341d-a3ea-6eff0c66237c | -12.94299 | -46.66471 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c5fa07d0-fdc3-37a5-8332-ffafa05ea520 | -8.74351 | -47.87725 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11cc6bb6-31d7-3907-9eda-87f357184bac | -11.86472 | -47.07985 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15d56065-e8f2-3850-810d-c6f536ded3bf | -14.80086 | -45.95862 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e885928f-d78b-31f7-8402-b3b48cb34cfd | -12.77725 | -44.153 | 2026-09-29 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84811962-828a-37ee-9871-85cae641d3a9 | -11.37421 | -54.04643 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7485bb84-65a8-3ee4-8e36-49e8d6b0f091 | -11.38504 | -54.04835 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07a224e1-b7a7-3a9f-883d-3f035bf86039 | -8.85762 | -49.87963 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9a260561-80f6-373f-b6ea-7a6e45b55898 | -16.34927 | -42.57413 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30be68b7-e68c-3f9b-9bbf-811a0d66dcf8 | -11.84573 | -47.07752 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f44dd24-315b-37e2-bdac-bc8f67ff2701 | -15.00396 | -47.86604 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6a2e840-6376-3fd0-a09d-036492a05755 | -13.33331 | -46.8147 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f8e0d70-518f-3c02-87de-479e2a93f117 | -13.52457 | -46.9132 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 872cc4b1-71f3-3f72-86c1-d561adeec788 | -14.08289 | -46.31574 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29810592-386d-302e-bfa3-09a92ee924fe | -11.30936 | -43.55003 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5a89e60-2bcb-3732-bf54-8e0ee66750a4 | -11.14243 | -50.07771 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 362d39a8-cd50-3350-8713-f45989a659ae | -15.23965 | -43.27115 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 119edef5-093a-3e24-80c6-c44ec1fcfc25 | -12.21052 | -38.98408 | 2026-09-29 04:17:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2fc637cc-40a0-36d5-a7ed-9ac78fc34cb1 | -11.50531 | -47.40145 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4209ad1-2627-36f1-9446-6efdd730ec9f | -11.89938 | -50.62276 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bfda405-32fd-30c5-9339-0e1a05dbd1c3 | -12.7186 | -46.98285 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 359d9b05-28b5-3bfd-9821-b01957b26c05 | -11.42975 | -43.4527 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b47191e-c89f-397e-bfb4-51b63c8dd166 | -15.00677 | -47.87065 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 913caefb-14a5-30fb-9faa-249ec59d560f | -12.00196 | -50.99485 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38de2385-ae09-3781-90d6-106aa0e6bc06 | -9.13967 | -49.98136 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd898e8f-3921-3b70-a269-949f566fda40 | -12.01687 | -50.96202 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3192e9b2-d794-33df-aa68-f09170dca90e | -12.01482 | -50.94837 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5fca9f1-879c-3abd-acc2-98104e1a6baa | -12.057 | -50.93845 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dc571cc0-163c-3235-9c67-a684365099d7 | -11.16945 | -50.04662 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27ffb5b2-b9cc-3108-bf84-86f2aaba1bb6 | -11.41024 | -43.42407 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 995135e6-32c5-39e0-a25a-7f6d739d73c6 | -11.39643 | -43.44749 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e5628c-f7bc-32be-9ce1-402c4fdf68ac | -15.16861 | -46.17178 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 656a1f4d-2ed9-32e9-b36d-1986d2a9fd0b | -10.70834 | -47.82664 | 2026-09-29 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7238626a-8f20-3098-bb1e-131ca32055c3 | -12.04291 | -46.49255 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b3ac9be-dac5-3aca-b3c6-6f39a36e99a8 | -13.36993 | -44.01045 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 658e642a-914e-33b1-a28d-1151b31492eb | -13.06691 | -47.44894 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bef302a9-3f2e-3828-9b8a-d1d79294458f | -11.44585 | -43.45888 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10cb15be-c580-3486-8410-4169599600d6 | -10.51822 | -45.3641 | 2026-09-29 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d7522b8-aa34-33c6-8592-a93e6b01969a | -11.45256 | -43.48183 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14efeece-5dab-32cf-b177-bfe87245950c | -12.02558 | -50.96362 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27fbf2f0-6c0b-3c51-8b5f-6c1bab714904 | -9.08784 | -49.88116 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56c35e8e-7187-3aed-8da8-10de84ddf8f8 | -11.42756 | -43.46696 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b1890381-631f-3d8a-99dd-e233761c8dd5 | -11.42865 | -43.45983 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84ba99ca-8e0c-3ced-8053-ad2c0b29e03b | -11.17983 | -45.14425 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f95988b-bfe1-331f-9e5b-5a672e3486ea | -12.63792 | -47.25562 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18ee0bf6-d062-3382-bf33-c1bec42d21b9 | -10.2622 | -46.65914 | 2026-09-29 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10e05eef-258e-30a0-b433-7737178db1d4 | -14.75091 | -43.95836 | 2026-09-29 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b03c3647-c18c-3802-a726-63a82cbbb7d9 | -10.27249 | -44.64014 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66962cbe-1a69-38f6-b3a5-72942f30fdd1 | -9.77817 | -44.81867 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6e619cb-a95f-3951-b5ad-6672168955c0 | -15.0951 | -53.87257 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15f6325b-aeeb-3390-966f-4bd890783836 | -12.06274 | -46.49977 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 76c9e20a-be42-3fc1-ae6f-f8d3e1e23874 | -12.69658 | -47.26963 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77078a4a-b0ed-3ada-8245-e7fec2a484d7 | -11.41812 | -43.46183 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 311549da-658b-3629-acbe-5a6f707ebbed | -11.28392 | -43.56055 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 091c97b9-0c7d-3c55-abea-6afcef051432 | -10.59198 | -46.20877 | 2026-09-29 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 612ee87b-6cec-3db7-99a2-1e3bbe62d596 | -15.38261 | -47.92257 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1c15b10-f503-3c7a-a50c-be7aaa8028c9 | -11.95715 | -50.93935 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7d541d6-4e4e-3785-af4e-35e64d27fe73 | -8.89288 | -46.19635 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 392bf70b-36de-36ad-8fc8-32e7efcd726a | -11.42587 | -43.45574 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdb23eb5-ab68-38ee-973e-82c7d5a9d18a | -11.86007 | -50.47328 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 93a77bac-2888-378c-b0ab-fa0f4d283fba | -13.41125 | -43.89579 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25c502b4-d04e-3b4d-8a35-08d9bcca717a | -11.36404 | -47.44664 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79964b81-010a-3cbc-984b-db5359e88c79 | -11.44257 | -43.48026 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2647c5d-d7d6-3e89-a7fc-aabdd295324c | -11.85103 | -47.11096 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c750a67f-ecfe-3613-8715-4cd83dc25514 | -11.93069 | -50.88598 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb035cd0-e9cb-368d-bb87-1cd817804c3f | -12.01892 | -50.97571 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7a7e792-b8a4-324f-b2f7-80f38d06feb4 | -12.01661 | -50.98863 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de74e5dc-8ef0-3329-96fa-0a31ef035a71 | -13.71367 | -48.83099 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98878305-4be4-3837-84f3-77d07d2efade | -12.02352 | -50.94997 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c04d6746-c808-324d-b9d7-20e89aeefe75 | -9.78812 | -44.82026 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0831eb46-02a9-31cb-953e-d4df3a31ab2c | -11.14312 | -50.07383 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 257fdeaa-c9c4-3d1a-822c-4b8f4f7c151a | -12.73307 | -47.27458 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a1a965f3-81eb-3d70-8911-e40448a5a4fa | -12.01917 | -50.94917 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b4025e0-2811-3846-afc0-1ea882c7bbd1 | -12.0519 | -50.94192 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a50d9d8-f161-397b-9eef-672509cc20d0 | -11.18371 | -45.14125 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d62fdccf-7ddf-3765-8b9a-5136dddb14a4 | -19.00655 | -47.87295 | 2026-09-29 04:17:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README32.md)
