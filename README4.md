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
| c5837fa3-8d5f-3e0f-885f-3c8336138479 | -5.6946 | -43.6669 | 2025-07-22 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e05ebbb9-55cd-3b2d-8d8e-448bfec85ea4 | -4.388 | -43.2896 | 2025-07-22 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4321b5c3-5532-3e03-9a20-fba817a4ea2f | -13.6975 | -45.6865 | 2025-07-22 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 4a93e561-8579-3129-a104-988bf105233b | -15.9333 | -43.5166 | 2025-07-22 01:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4037b1ff-65fe-3dad-9767-efd98b8fe98c | -11.7317 | -48.1849 | 2025-07-22 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a9c42917-26c1-3e1e-ba09-3d3c8193a4f2 | -5.6758 | -43.6683 | 2025-07-22 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5b517850-5e0e-366f-a2c0-17a20ff979ac | -8.5211 | -43.3063 | 2025-07-22 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5039de4b-87b6-31eb-8700-a6479083517d | -5.6946 | -43.6669 | 2025-07-22 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2efccb1c-a39d-3307-97d7-b21a9e0104ca | -3.1832 | -49.4642 | 2025-07-22 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 5274e7a5-3fea-3c62-b1a8-fd95d38771d4 | -11.7317 | -48.1849 | 2025-07-22 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f764419d-7e34-313e-90e2-7f80ad97e1f0 | -13.6975 | -45.6865 | 2025-07-22 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| f08806b8-dab4-32bf-b453-7300ed584d92 | -13.6582 | -45.7161 | 2025-07-22 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| e43fa62b-e730-3af6-be53-72333c975323 | -15.9333 | -43.5166 | 2025-07-22 02:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 430094f9-ccbc-304b-945f-0ca04e33123d | -3.1833 | -49.4429 | 2025-07-22 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 6cfc94fd-b327-3281-87ee-8d17714e5590 | -4.388 | -43.2896 | 2025-07-22 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5e3064fd-8396-3445-804f-3e49988dea1e | -5.6758 | -43.6683 | 2025-07-22 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3dccf3c9-6b26-3a96-8cc0-095dd5475f9d | -7.95189 | -71.45911 | 2025-07-22 02:04:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4e2858aa-da6e-309d-bf42-c4f2f38a4cdb | -13.6975 | -45.6865 | 2025-07-22 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c03a3231-77a9-3cbc-810f-227afca5cd8b | -4.388 | -43.2896 | 2025-07-22 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6a1bab3d-3897-30ff-9341-74a338f8a887 | -8.5211 | -43.3063 | 2025-07-22 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 6e5f401b-2be8-38f1-8d62-87a264ba2542 | -23.701 | -51.6772 | 2025-07-22 02:10:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| 2d7f2127-fde4-3edc-82ba-c7dab148d89e | -11.7317 | -48.1849 | 2025-07-22 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f1c264d9-db8a-3a3e-ae34-569c952a668f | -13.6582 | -45.7161 | 2025-07-22 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| a8bd2a59-2bbd-3eb7-a9a4-50f5001518f2 | -5.6946 | -43.6669 | 2025-07-22 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2da52329-5ca7-3804-adbb-b15e5ba68fa9 | -13.698 | -45.6634 | 2025-07-22 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| abadeb7e-5b27-3b7a-82b4-6446ce5dacf9 | -14.3918 | -47.7563 | 2025-07-22 02:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cba099de-056f-3809-8b69-7fcd8d5bb22a | -5.6758 | -43.6683 | 2025-07-22 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6ef2cfec-e3af-3c1a-bab8-283b7d49e199 | -15.9333 | -43.5166 | 2025-07-22 02:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 46019703-a953-381b-a54f-8125e88bdc9c | -7.4329 | -49.6598 | 2025-07-22 02:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 06953be3-736a-3d10-9be1-6c804e301ed9 | -4.388 | -43.2896 | 2025-07-22 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5900c02c-9a02-3fdc-a856-0573f1268ff6 | -15.9333 | -43.5166 | 2025-07-22 02:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| bf512398-6a98-3192-aeb5-da2a920ff55c | -5.6758 | -43.6683 | 2025-07-22 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f6f547ca-4564-354c-9831-dd5d5b1311c4 | -8.5211 | -43.3063 | 2025-07-22 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4ce697d3-40e1-3ae5-878c-bea04276155b | -11.7317 | -48.1849 | 2025-07-22 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d4495af4-f28d-3a91-998a-ac805ecfaf58 | -5.6946 | -43.6669 | 2025-07-22 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e2866062-db96-3304-83cd-6e3ca8001109 | -15.9333 | -43.5166 | 2025-07-22 02:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| af286e9e-94d2-3b8e-b80e-d2a8e84f7a93 | -8.5211 | -43.3063 | 2025-07-22 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 5c787ced-0ff5-3e7a-ad04-da125dfada28 | -3.1832 | -49.4642 | 2025-07-22 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fb444f5b-4ebc-351d-a9bc-0aa68232d996 | -3.1833 | -49.4429 | 2025-07-22 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 1cf994b7-f6d0-3dfc-a245-4f5a85e383c6 | -11.7317 | -48.1849 | 2025-07-22 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 91067b18-7f8f-30ee-b18d-e56ced6fe0d9 | -4.388 | -43.2896 | 2025-07-22 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4404da4c-8b26-3531-ae5d-df228dbed9fa | -13.6975 | -45.6865 | 2025-07-22 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 3ee4c3d9-5707-3740-ab7a-04eb0c2b36dc | -13.6582 | -45.7161 | 2025-07-22 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 58aafcd0-327a-3ef5-b635-ad079de8ad08 | -4.388 | -43.2896 | 2025-07-22 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 6ed8dde1-7166-3bfe-8e6c-900ab8de22fc | -15.9333 | -43.5166 | 2025-07-22 02:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 08825fa7-f948-31ec-96bb-f93962efd723 | -11.7317 | -48.1849 | 2025-07-22 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c8d2cdb6-365f-3401-8b7f-2c73b1449077 | -8.5211 | -43.3063 | 2025-07-22 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| eab562f9-8206-381e-b8c9-41101b45db7a | -11.7317 | -48.1849 | 2025-07-22 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 63f65a8b-24ab-39b3-bd6b-2cf34640fc47 | -4.388 | -43.2896 | 2025-07-22 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 821b1518-c657-3875-8ccf-d4b47207b39f | -11.7317 | -48.1849 | 2025-07-22 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4c4c97d1-b29c-38af-bffb-b1f8ab84ae7b | -8.5211 | -43.3063 | 2025-07-22 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 2a15f0be-684a-3bde-8f1d-62edd70a177c | -8.5211 | -43.3063 | 2025-07-22 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6becff05-2b01-3bc4-b7c5-385b01298f42 | -11.7317 | -48.1849 | 2025-07-22 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 96290610-3204-33fa-962b-867232263992 | -5.51179 | -35.58174 | 2025-07-22 03:10:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 565f47fd-b4b7-3a6d-bc87-cc172723ace3 | -5.51683 | -35.58264 | 2025-07-22 03:10:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ff8e0563-758c-3c54-b6b6-cd4b979ebe0e | -9.49286 | -40.56632 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c4fc8e49-0651-3d5b-a742-ff5db0c575d8 | -9.49869 | -40.57118 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 99ec55cb-f458-3c3f-9d1d-3594f1acb808 | -7.15935 | -40.21497 | 2025-07-22 03:13:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 30d64928-0654-373d-940e-25caf5a54398 | -9.49221 | -40.56995 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2ad813e6-d3ad-31ce-a86d-265b93c0a1a9 | -9.49935 | -40.56748 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f8f43d64-b0a3-3bda-b915-4a41d1df3ea9 | -9.48818 | -40.38251 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd8f1f5d-76ad-3145-b213-e2865db09100 | -9.49177 | -40.5718 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 99f610ab-4bf1-3764-89c9-bae646c624c0 | -9.49326 | -40.56446 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1d2d8c72-1c7d-304f-967b-8053fe6f04f3 | -9.49825 | -40.57302 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 088aa302-5d1e-3fef-954f-6992f3338483 | -9.49975 | -40.56562 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 288dcc2e-f2ac-3608-94ef-4d5ab6b6a5da | -9.49457 | -40.38388 | 2025-07-22 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3fa5ed5a-444e-3c5d-a7c6-4e23a55e442d | -9.33438 | -37.98352 | 2025-07-22 03:13:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c83f359-7c44-3369-b884-56dc94ed528e | -15.92532 | -43.52027 | 2025-07-22 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cafcab59-eb7f-33ff-9ebb-bbab53df2526 | -15.61588 | -41.33846 | 2025-07-22 03:15:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9e362e8-4806-3f25-bb6f-63ca927016db | -16.69402 | -41.01042 | 2025-07-22 03:15:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a8256607-7a86-31d6-8d9a-be7d238553c4 | -19.41178 | -44.96365 | 2025-07-22 03:15:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d686d5b-0d55-349e-9d27-7bc015b35b2e | -15.61691 | -41.33363 | 2025-07-22 03:15:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0739774a-f1d0-38d8-a820-0eaba859fbe2 | -15.93216 | -43.52187 | 2025-07-22 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c9eba9d-212e-3587-806e-50298142fa59 | -19.82921 | -41.95484 | 2025-07-22 03:15:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3314ee2d-186d-3d76-8d79-6a7a376d643b | -18.61751 | -44.26549 | 2025-07-22 03:15:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf2f4ff1-30a0-3960-9f17-0b440381675b | -18.62924 | -40.09539 | 2025-07-22 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 231be060-6a3b-3c38-a39f-804eb2765919 | -21.05581 | -44.756 | 2025-07-22 03:17:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 75ecf128-9204-3117-aeb4-92c6da59e682 | -21.05562 | -42.95413 | 2025-07-22 03:17:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 26c29f85-02d3-3168-94ef-86fed2be7cd5 | -11.7317 | -48.1849 | 2025-07-22 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e859cfc3-026f-368d-adb3-44c43e2852f0 | -8.5211 | -43.3063 | 2025-07-22 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 32576603-d72e-344b-9a8a-2ce994a64486 | -11.7317 | -48.1849 | 2025-07-22 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a957c4d0-88c6-3818-9323-05713414fc22 | -8.5211 | -43.3063 | 2025-07-22 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 63985aa3-8457-32f5-ae76-b9edc0d96983 | -3.29176 | -42.54009 | 2025-07-22 03:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d25a55-88ec-3a30-b399-6f411ca7c8fc | -3.2862 | -42.53915 | 2025-07-22 03:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c45f39e-46bd-3f4a-96b6-dfb19129877d | -3.3553 | -42.87125 | 2025-07-22 03:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72a51014-eebe-3096-8edd-89f7cb496b51 | -3.29114 | -42.54377 | 2025-07-22 03:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8a60f93-95ed-3d5a-b31e-27faaa0b7ede | -3.36096 | -42.87232 | 2025-07-22 03:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38576730-3670-3ecd-aa08-83c94cb622ec | -3.35466 | -42.87512 | 2025-07-22 03:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f38b85f-60b6-3a30-b203-f6a4b6bada0a | -6.50071 | -43.5139 | 2025-07-22 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e2440fd-42f1-33b3-85e2-dac0d3954ac2 | -7.12236 | -43.3302 | 2025-07-22 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90f1d6a8-6afd-37bb-b2cd-44f336aafcdb | -7.2529 | -44.29239 | 2025-07-22 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 307c7e16-28c0-3e0b-87df-eb94c8ca1539 | -7.17811 | -44.14887 | 2025-07-22 03:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84bbdd3f-6c91-3d78-9a12-bf914aab1243 | -7.15936 | -40.21255 | 2025-07-22 03:38:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f980d942-8da5-3ef2-8eee-b51f644d339c | -4.37931 | -43.28478 | 2025-07-22 03:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4ab32314-9876-3413-8a90-cb09f94bf76f | -10.77577 | -42.71613 | 2025-07-22 03:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| abdfc95f-1767-381e-bff3-49266ee2aa60 | -8.51214 | -43.30695 | 2025-07-22 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 74131ccd-c69a-331a-9100-d701b23795b2 | -8.09888 | -46.8288 | 2025-07-22 03:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a81be2d8-da29-3475-98b6-c387c79061af | -7.16177 | -40.21554 | 2025-07-22 03:38:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6db61053-1b8e-3f2f-8a32-5880fc93793e | -8.5835 | -44.32114 | 2025-07-22 03:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7791f159-86d9-3229-b293-3b51d1e7a178 | -7.14583 | -46.10402 | 2025-07-22 03:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README5.md)
