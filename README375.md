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

## Dados Diários - Página 375

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fbbf1b7-e319-3311-9545-408a63153d2a | -2.90576 | -59.20531 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a6ff0492-f211-39d7-b581-29bdb2c25a8c | -3.30226 | -54.01655 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5b5b537b-d96a-3028-8a52-79a3b0f6844a | -6.73946 | -55.11915 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 20482bb7-f265-3d75-80b3-43cd5ff10fdc | -4.05338 | -38.93511 | 2026-10-08 16:39:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b4deb248-0ff8-31e6-83e1-372114f83d34 | -6.45173 | -55.04316 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 45f3f6cb-d13a-3430-ae7a-41700c0add1e | -1.31915 | -56.41063 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25a47cb5-b1f8-392b-bd79-8d5a6b8d74fb | -2.86912 | -54.16275 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ff3ed728-6389-34b3-91f5-e6e851de73e2 | -3.80091 | -40.45654 | 2026-10-08 16:39:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e071622c-e50e-301e-b7b2-4d1776ee30b2 | -2.05673 | -54.29696 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e6ced4d0-ab4a-3842-a658-1fa7d8ab993c | -2.50167 | -56.06406 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 54cf369a-978a-34a5-92f3-2d6f2216bc55 | -3.00142 | -57.7407 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b667cf4b-0a20-3f1c-abe8-4c8f1057d446 | -3.03643 | -54.2343 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3fbd06a0-909a-328d-8f47-6ca44974e28f | -5.01874 | -42.44427 | 2026-10-08 16:39:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 6a7b96bc-9eb4-3428-be4d-5a2078843d9a | -3.77728 | -59.25146 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d62daa70-0e1d-32f6-96c7-9b863823a79d | -4.34221 | -43.16167 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 09b94c11-39cb-3260-a265-5ce75b6817a2 | -3.55098 | -54.68666 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f619ea2c-9172-3158-b064-cfceffc467ab | -3.7095 | -57.09192 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1be2891b-8ba4-36ec-8aa1-55249294c7ec | -3.30704 | -53.70704 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 223.4 |
| 8861182c-efb2-3625-bf7b-f0477539d527 | -3.59778 | -44.35414 | 2026-10-08 16:39:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3eb33a61-6b56-3b83-b790-34d657fcfbdc | -3.51245 | -59.33135 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 6c4ecdb9-2c3d-36f9-8595-4f29bccae1b9 | -3.01165 | -54.07105 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 3450fecc-8825-3e3c-9a85-d3e01c8990e6 | -3.09093 | -58.01713 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b94ce698-389a-309a-8c8c-e9289a90299d | -3.73845 | -57.1263 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1f9c9ec9-ef18-3c56-919f-f8fcdf40133d | -3.17187 | -58.62334 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d1305757-cfb7-36d1-a438-ccec7b79fc5b | -4.09533 | -44.12923 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0d25a305-e858-3cc4-b1c9-96087b9ec995 | -3.92128 | -55.85831 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ad39a74-db85-3df3-8a80-6d4ba0fe7498 | -5.63462 | -45.79628 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0ca9022c-f2cb-36b7-8832-3f74b7e02125 | -5.90791 | -53.88986 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 357a3ad1-3813-34b3-b4c6-980a44965d52 | -0.61168 | -56.81095 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 45c140a9-d010-3ce4-878e-506edf162d6e | -2.07647 | -46.56548 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11b9b41b-48b6-3f40-b6a2-d335627fe3dc | -6.15051 | -47.93228 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 56f91205-1242-3f4d-ad2f-67b823ce8cd2 | -3.87971 | -42.8378 | 2026-10-08 16:39:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aed7d586-cfdc-36e9-93f2-9599731702f7 | -4.0878 | -44.12654 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 953f6ae2-a19c-3bf9-8750-30f8a1f9c168 | -3.77316 | -52.62865 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 11f72a90-cbd5-32b1-9ad5-df23357e2789 | -5.79518 | -43.7515 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dea4a543-2522-392c-9bda-f951704a5777 | -2.26627 | -55.85088 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 24ddf93c-b4d3-3831-ba30-3d5aaba3bbf6 | -1.21217 | -55.68819 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e708dbd-a1f8-3276-be3e-065a6a3ee44d | -1.19907 | -54.20524 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2793ac33-376e-35da-95ae-055c06a8c7ad | -5.86284 | -53.45972 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 7947560c-cdae-38ae-aafb-76533d046dc6 | -6.73902 | -55.11586 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7d637a41-fae7-3dc8-975e-7a231fe21254 | -3.02659 | -54.06628 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 34549502-fd8b-32a1-a152-bb48eb2db462 | -2.99127 | -43.2816 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c5777eea-4006-36be-974e-cfa14dacd46a | -5.21731 | -44.63239 | 2026-10-08 16:39:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c7fc786-b4eb-3c49-8064-e07146a0e4c4 | -3.00418 | -51.12051 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b2318230-0d60-3d09-b278-89f7f428f09b | -4.41693 | -55.74963 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cdf62877-4436-3425-b1fe-a5750f39a0cb | -3.00219 | -54.07246 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b8d69d1a-8fad-3069-a30f-f586e172ef08 | -5.69337 | -53.47419 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0e8268e7-aa1c-3bac-a0b5-d450e1da15ec | -2.56788 | -56.17368 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 4406d893-db28-32c1-85ef-95aacbd0e6b7 | -1.52904 | -54.82348 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 4355f7c3-e5c9-3d53-be5d-99a78e603cc4 | -5.06159 | -46.17728 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b265a975-203d-3fd4-85ac-d2f4161718e6 | -3.50309 | -59.26619 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 41be5891-5ebb-3569-afff-2066f63e795e | -3.01251 | -43.34509 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 53dcdc03-f349-3b20-92c8-f8ee404b2646 | -4.37787 | -43.36456 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bd76da0d-d31a-3792-a00e-f2953edbafe4 | -5.25715 | -55.91632 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0d21b63a-9f8b-38c1-bf84-50bfadff2a86 | -7.21129 | -55.16223 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 076fd248-f984-3ebb-9a06-7ff6c5c36ad9 | -4.37553 | -55.31893 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 314baa4a-7b82-3009-b7eb-0fc881f99f24 | -6.13983 | -51.75924 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2a9c3b82-f256-3eb2-aa4e-3141b6e58869 | -3.34848 | -42.49057 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3bcc1130-b358-35f1-a4fc-3e584992ad63 | -1.40376 | -53.22999 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 78ae93c2-9b32-344c-8bb0-96e312c9552c | -3.97422 | -51.86906 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 380310fd-5b6b-3ed3-b83d-a97e3adb2b55 | -5.34662 | -45.7323 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 66c14093-c574-320f-903a-3693389030a2 | -6.32588 | -46.54743 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4b5151a-e71b-3720-ae7a-496618937be0 | -5.93144 | -53.80899 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cc472184-a8c6-38c1-a850-2388bdcb972e | -5.67264 | -46.35572 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 581bf8f1-aa49-3d8b-beef-d3c0eff946ae | -1.45434 | -55.25013 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1184ca5-c18e-35c6-b761-389d9c47d6ee | -3.71129 | -59.63965 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 040e16e9-d6b2-3c3b-b4d9-e7dccc8fba35 | -4.96328 | -56.26994 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6bc5e111-37b6-3bd2-bfd7-985824179b7d | -3.59727 | -58.99805 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e05f3e26-f369-3e61-bf98-34d72ba70b98 | -3.96541 | -51.86654 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fb89f263-005d-31f0-a887-016eb5a2ffd3 | -6.44806 | -52.70037 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| bc700891-6548-31de-90fe-6aadd4b910a2 | -3.06137 | -57.3147 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| a45eae27-7945-3bb7-8fcb-b5c83c68ecdf | -3.00494 | -54.76355 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e138dad1-df7e-38dc-8d12-11d2ada5f56a | -7.23454 | -55.13013 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 949be863-16bd-3f2d-8cbf-7a163655f76d | -3.40115 | -57.99995 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 67657bf1-1f7a-35d6-aefa-86b14a643255 | -5.39738 | -45.90851 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a5904343-2574-3f83-ba8c-162be8f8fde7 | -6.14437 | -52.64434 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c2ac8892-2499-3401-86c9-c4d5fdbfdaf0 | -2.27721 | -48.75425 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 92fc2f53-b920-34c9-be17-0a5877dc147c | -3.01213 | -53.90068 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 942b09c7-feff-3924-a417-091188d0a28d | -4.58276 | -40.65578 | 2026-10-08 16:39:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| feee3491-709f-3cd4-8e86-c5e85704f1b5 | -2.50746 | -56.1403 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 36f33cb1-7ae4-33ca-a2c4-8faa3fb07a83 | -5.37991 | -44.1924 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 570fc341-39cf-3b70-bfa9-8f11a9e7ef16 | -5.60662 | -45.59146 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f4922ce-9191-33d4-a97e-b0bbe3faacdc | -2.94633 | -54.15324 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 060b51b3-1e6b-3d4c-ab41-6c953a1f6c57 | -4.78281 | -43.34095 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 2b43e867-662a-3262-84a0-6d3c3d2bb41d | -5.959 | -51.79171 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fc6ed48d-8857-360c-8ef8-698549e4ba70 | -3.1656 | -58.63593 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1dc78262-726a-38f7-986b-6f047022f095 | -4.32661 | -41.23429 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 34d72d32-c1ad-36c3-9300-cb93dcfc220d | -3.01212 | -43.34403 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3d6054a-7daa-3cc3-b7e2-8cb3de35142e | -5.09884 | -46.22024 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d0e58d03-4a4d-394c-97f5-e1ca60dde697 | -4.58973 | -56.08503 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44dc2bf9-2fd2-34fd-a664-d559e8a3ebbe | -1.83026 | -54.99455 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 13460f05-2beb-32db-bbb4-dba54fc37f83 | -3.23977 | -44.37402 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f27d4f0-6871-300d-827b-93d01c8cd97b | -6.46839 | -55.0071 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a9c02425-c710-3d68-8660-26c401730dbd | -5.70144 | -53.46322 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| c87a5b3a-58b4-3784-84d5-1798ee3da6c3 | -4.85907 | -42.99815 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 64c71045-802c-3816-93f5-76f224a77adc | -6.2078 | -46.64075 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1036cbfe-496a-3bae-8534-19aea771c9ab | -1.7476 | -57.18147 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc913c49-9182-3e19-a86a-a761853e6927 | -0.40313 | -51.71537 | 2026-10-08 16:39:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a06ee939-dddc-3352-9b00-871dba72d596 | -3.09443 | -53.93893 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| e98f1c8e-3dc7-3c48-ad22-7b92d4d2ab29 | -6.37382 | -55.13322 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README376.md)
