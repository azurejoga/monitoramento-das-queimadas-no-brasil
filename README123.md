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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06604b17-4894-326f-8f27-ad66703d69e7 | -10.57587 | -48.69951 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5049d2b2-9fd6-36d5-a082-ec65ec0ee8e5 | -14.75244 | -54.63996 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfe354c2-01b6-3db4-bc37-14b74265fc09 | -13.1799 | -50.92669 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1483c8e5-47f9-3a7c-ae59-c312a6bbf02e | -10.30361 | -50.28119 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39e264ee-39bb-33b5-8bf5-94fc9fac5ec4 | -14.46077 | -48.40122 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dba23e37-7e8b-3655-a7a3-e7cc5b6fa296 | -14.16479 | -49.20786 | 2025-10-04 05:06:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 386d4fb4-c591-31a7-a164-dc7b4ba3ae6c | -11.64233 | -46.8659 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82ee41f6-90b5-39e4-9840-bb83b1ad3efe | -13.51601 | -47.27797 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6a416f4b-50bf-388f-9d3a-f54c4da27f27 | -9.63644 | -55.13101 | 2025-10-04 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 04b9e78b-5bac-3b76-82b4-5f001cdcc789 | -16.01405 | -50.85358 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15cfe33b-71d5-34d2-ab9a-9716722eb007 | -11.1359 | -47.8548 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d07f1eb-e993-305b-8474-ac17080d5ca2 | -13.33068 | -50.9406 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95bf40b9-3bd3-329b-96b1-36f514d55415 | -14.88722 | -48.27688 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 987c42ef-2243-35be-9393-0e1d17dce66d | -9.63443 | -63.24395 | 2025-10-04 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d5741e-54ca-398e-97ec-5790e6157a69 | -13.30328 | -48.13562 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3505de2-122c-3183-9d36-02378fa524f2 | -11.56321 | -47.67757 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e3b8a8f2-d38c-3788-9c34-b894e86a2bf0 | -11.91508 | -46.40007 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8e2f39b-c049-3085-be1e-ec9dde0ebcf5 | -13.98303 | -48.19896 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 046d30ce-345f-3415-8b31-659e850a68ab | -12.70948 | -48.56993 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93574c16-2ac5-312b-9255-f2d06a669e75 | -14.24079 | -46.10213 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1a43138-026c-3978-81af-a9793191d399 | -15.72746 | -46.28328 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cdb7d00-4a53-3c05-acd0-1d76db669aab | -15.22456 | -56.82092 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 569e6d80-9300-37e8-a03b-1535cddeef7c | -13.97845 | -48.19158 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 522b7e4e-152f-3ab5-8ec8-40aa60390b34 | -14.67222 | -48.29105 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 174b9594-999e-3abb-8520-9d398e10d360 | -14.90089 | -48.27776 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93adcc03-509e-3c77-bcea-d9686a3c922a | -11.79404 | -46.82353 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6c9dfda-563e-3736-b0e4-ea93396d9b63 | -13.57199 | -47.58268 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 181e41d1-10ec-3f2c-9ebb-2cacd9ccaf95 | -12.36615 | -54.17042 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83f4f860-a753-3e3e-a7b1-7799919be144 | -10.88087 | -49.10165 | 2025-10-04 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 043f5e27-cb17-392e-b516-c3e07c648627 | -14.88176 | -48.27681 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43133552-f1d2-3dca-b660-9e3dba63d33e | -13.17893 | -50.93359 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8869c924-c5e1-3864-8afb-c00802e3e09e | -14.96838 | -47.26406 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d9b9049-8671-3b77-95fe-b3a10faee951 | -11.56279 | -47.68108 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44c5991c-c592-3f69-9779-8ebdb1d1500b | -11.45423 | -45.14612 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3919c071-591c-3006-9bc5-ee47201693a5 | -11.54394 | -47.67393 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6b18159-a81e-3aa3-874e-beae5383aecc | -13.51035 | -47.27731 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2489654b-2074-3e3d-bcf6-0f8ee51a9116 | -10.61146 | -49.14692 | 2025-10-04 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da65a0e2-ca58-36f2-8e4e-ed0ae5d0efe1 | -13.93388 | -48.17355 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d76e379-aefa-3462-9cdd-16430c8cf240 | -14.8485 | -48.28085 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f460e21-f7d8-394c-9575-bb7f9323710b | -10.33968 | -50.31305 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 077e323c-dc16-3cfe-881c-be7752e3fdd8 | -11.96292 | -51.47277 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 805bed3d-bfeb-3ad0-a0ad-f8a2277c801f | -13.1354 | -47.80542 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 664cd827-cd45-325c-8a3e-bfbd199ef24b | -13.74627 | -48.09459 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e14c74b9-1f61-3d18-9414-b54feaff1590 | -11.69594 | -47.50601 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e711f72-33e0-38bc-bbdf-60891f3ab6a1 | -13.93425 | -48.17045 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 01fa5f24-f583-3300-89dd-5ddf619fc637 | -9.98901 | -57.81996 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46633494-dde3-3a52-921c-94ae89ccf7c5 | -11.7961 | -47.91947 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43f56fcf-d8f6-37dc-aab4-b33b6bc744df | -13.5188 | -47.2756 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be224387-5cc5-34e7-a65b-f13836581d5e | -13.10681 | -47.90514 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 180b8064-ba18-3c29-9143-1a9c09094514 | -13.24344 | -47.83947 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcc5bf68-f961-3a0a-a309-d607b8b965ca | -14.65372 | -48.30945 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ef93abc6-b248-33ed-a700-543ab8a6fe01 | -15.34351 | -47.81905 | 2025-10-04 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7abdb85-fa0e-3c6b-9a28-81fa97e1f236 | -14.89107 | -48.2906 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 009b03b2-4260-30c2-ab65-809256e7dfcc | -11.28172 | -47.80062 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5c47bc0-5def-37fe-ae3d-ce44c3057005 | -12.81244 | -46.85308 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b46c4e79-7ba8-300f-889b-bbf0a0c37420 | -13.98801 | -48.20287 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ae80387-7302-393d-84f5-a428a80c9d16 | -13.46814 | -47.26721 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cdf59644-648e-3324-a654-546f72b2e839 | -13.3283 | -48.10834 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47a34d36-317b-3fd4-b025-2b1748bb1140 | -13.26096 | -47.21864 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d9ce864-e6f0-3798-8577-5fdf25383569 | -16.01767 | -50.93948 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef66345f-3550-34f2-9c44-6e2d146ebe6b | -13.76451 | -48.0553 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70ce320c-4cb1-365b-9e54-59ae1754b40f | -10.52453 | -50.84364 | 2025-10-04 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c13baf3-6973-3a39-9c73-97698ecfacd2 | -11.91925 | -46.4093 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 5c066bf3-fbce-3cc8-b2dd-0d0758296083 | -14.28444 | -45.87211 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3364d382-5da4-399e-bb73-6e9f425a384b | -11.91337 | -46.35627 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a23ba277-9133-3546-b827-7fff5aaf8ed2 | -16.367 | -49.40638 | 2025-10-04 05:06:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 602cf46c-7d94-3a08-8ae2-fd296e1f4b99 | -13.32239 | -48.09631 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 45c10745-0a5e-35eb-b4f7-66637f450a1c | -15.7918 | -46.25927 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e65eb109-7a33-3e4f-8553-2ab370368983 | -15.21291 | -56.83015 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95c0943b-6f0e-37bd-93e9-75b166cec51b | -10.64126 | -49.14257 | 2025-10-04 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b68acf6-fce8-319f-aa52-e4c36219addb | -13.98267 | -48.202 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 658a0a9e-f0be-303a-ae31-8e84286fd554 | -14.24125 | -46.09792 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a138fc10-1c67-3d4f-a305-7e452d1588b4 | -15.53561 | -46.81277 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d27262ab-9586-360c-a9d8-784b291488a7 | -11.12909 | -55.46346 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 480f2373-68bb-3c09-b658-615c97ae15c3 | -13.12278 | -47.81853 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79fd1f68-eab1-3750-bd1e-e259302ae0e9 | -11.05338 | -47.78705 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f04849ea-c43f-3a73-81aa-b61f218999fa | -15.52767 | -46.83088 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc7f7083-857c-362c-96cc-63a69c6d5473 | -15.37797 | -47.96074 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5a05089-1176-3a56-a476-65281729de8f | -15.66497 | -48.14701 | 2025-10-04 05:06:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 530931dc-a27c-316a-a191-ca295cdd01c2 | -9.85819 | -60.26977 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a78912-66f3-3ba7-8e25-77aa99f6d651 | -14.70768 | -48.1976 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9b16b03-d9c5-32e9-ace1-ed228a7ef5c8 | -14.46682 | -48.3954 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80f8ff77-3ff0-33a6-a28e-a219b74bb037 | -13.33584 | -48.07389 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61d740d5-5e5c-3f85-aedb-7c48ea36308e | -11.55241 | -47.6767 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0152d0ed-5364-3a73-aec3-4b289922e46f | -11.10122 | -49.84852 | 2025-10-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e985317-29ef-37af-bfb6-8bfed1b2b8f4 | -12.8765 | -47.28973 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2cb9676-434a-315b-8cff-eaaa4e6c37fb | -15.35078 | -46.2589 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69ed0e24-0da5-38be-918c-e156864c9f80 | -13.11005 | -47.92355 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65f06bd2-aad8-3d7e-9797-b609300de7a8 | -14.94833 | -46.86193 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f133fdf-c449-35d1-b260-74cb28f021af | -13.30157 | -47.59372 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 72d87fa0-63e3-3d69-aa22-36da242079e3 | -14.93654 | -46.86031 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eee2b586-6be2-3f17-bddb-f163ac44dc40 | -15.23832 | -49.30163 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59dcc09e-31a0-37fd-9d3a-6e15b0a55e53 | -13.33425 | -48.08762 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da6969f4-7206-3f40-8598-ec8f3fb478df | -11.8891 | -44.99689 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 194782fb-549b-306c-8a00-03ac4ae06705 | -11.46383 | -54.35469 | 2025-10-04 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd9bbd46-b2a6-3d21-b441-c7eef15eb360 | -15.60338 | -52.48901 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d79f8175-71b2-3ac2-8021-0721dc53d8ef | -13.1805 | -50.88643 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 499c28af-1398-333b-a4bf-49796af4db2d | -13.181 | -50.88466 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca7be618-8d16-3d1e-9728-332a88ac0c3a | -15.30806 | -46.30947 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab7383b1-fb6b-37ef-b039-0454c69b85e6 | -9.71199 | -67.46599 | 2025-10-04 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README124.md)
