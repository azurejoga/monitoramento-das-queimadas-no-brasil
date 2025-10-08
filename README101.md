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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67e4c721-d569-3e1d-87d7-66971ccc9f77 | -13.8536 | -51.8504 | 2025-10-08 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 56a0f5ec-c2e6-3a3a-b8ea-28304b8668ce | -10.1874 | -45.9889 | 2025-10-08 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 51b82481-ed70-3fff-a607-d6fa8f4eb9e7 | -8.691 | -44.727 | 2025-10-08 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 34ffcacf-f972-300f-8651-9f44672b3999 | -11.183 | -54.8991 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 378.6 |
| 3076fcab-eb41-3f59-b3e4-b2821ac4dc6e | -15.6393 | -52.5688 | 2025-10-08 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| bcf5b561-9255-378e-b45c-cc1c1af1fe95 | -13.2662 | -48.0409 | 2025-10-08 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1f098200-b96a-31de-a609-47bfd6c8a104 | -13.7918 | -45.809 | 2025-10-08 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e03d9dcc-3aac-3b3b-ab2c-415158a7500f | -9.0016 | -45.5148 | 2025-10-08 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2dd4884f-ec06-39bd-af43-597cdfe9b90d | -11.1644 | -54.8804 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 591.8 |
| 766c3e3b-5048-303c-a274-7a6575e68505 | -12.2525 | -47.8728 | 2025-10-08 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d9e35931-502b-3017-bfac-6a4c18e86d15 | -10.9296 | -47.1329 | 2025-10-08 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 11261581-9789-34c6-86c1-8a94e249e27a | -8.5395 | -46.2406 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5e297b56-5361-343d-bdf3-9cf2de120521 | -8.5204 | -46.265 | 2025-10-08 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 82c10e08-34c7-340c-b5cd-76f1793303cf | -12.4267 | -45.6136 | 2025-10-08 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1adbc2ec-f916-3141-a82e-70b48de2f05d | -10.7472 | -46.6409 | 2025-10-08 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 65651fcb-e523-3fae-8830-de32af5e11e4 | -12.4262 | -45.6366 | 2025-10-08 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6a85f5e2-b718-3c0c-a212-b7fd0bb16dfe | -17.5828 | -47.1762 | 2025-10-08 12:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 2288da5a-9139-3e65-b149-489902366778 | -11.1646 | -54.86 | 2025-10-08 12:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 78f6f501-069c-3fb1-9663-a7c1bb84aa49 | -15.748 | -49.0083 | 2025-10-08 12:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1ee774c6-3571-3d6b-a01b-74719e615b6e | -12.5107 | -54.7345 | 2025-10-08 12:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| abe3e490-c398-3b3a-a7c0-dbc35ab0e7c0 | -14.211 | -43.4573 | 2025-10-08 12:30:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| bcb70144-a1f9-35e3-b258-5b6e9f03febb | -11.6863 | -46.3139 | 2025-10-08 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e9367aa7-a610-381b-bcf4-bf60deb1ce63 | -12.4267 | -45.6136 | 2025-10-08 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 640f767e-38a1-3192-bb4a-e040ac8dc8b2 | -8.691 | -44.727 | 2025-10-08 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 362d6d32-e2dd-396b-8644-d6811d6fa367 | -13.2855 | -48.0381 | 2025-10-08 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4eab9fef-0e58-38a6-9227-3733c65e96cf | -13.7364 | -45.68 | 2025-10-08 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 2c814393-59fe-392b-a2d2-d8c135259ab4 | -11.1833 | -54.8787 | 2025-10-08 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 275.1 |
| a715ec11-dfd6-3ae9-9213-4dc6bfa86667 | -17.5828 | -47.1762 | 2025-10-08 12:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 89a173e0-3fc9-396a-b6d6-f378e858ddd4 | -11.1646 | -54.86 | 2025-10-08 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 2448089e-5f11-377b-bf9d-74ba8c95c263 | -13.3513 | -47.6042 | 2025-10-08 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 4a1d1b20-bd29-3d9e-9dc8-0b8ec70aa4d2 | -8.8531 | -46.7674 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cac23b40-e831-3e19-b8d2-cfd727d483ec | -12.4916 | -54.7364 | 2025-10-08 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 4d9207e1-6840-32c9-a049-fd3ceb59862c | -15.6393 | -52.5688 | 2025-10-08 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 23ef200f-1bb3-33e1-adb6-82eb2e7bff6d | -14.3889 | -46.0063 | 2025-10-08 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 846afbe9-2422-376a-aac6-97d7ac5d8ecf | -15.6198 | -52.5715 | 2025-10-08 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6c491709-1851-34c6-b380-86c715260c2d | -14.211 | -43.4573 | 2025-10-08 12:40:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| aff01cb1-bc2d-3308-9d25-531b24ddc523 | -8.4824 | -46.2912 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1e7e226e-9b0a-37f2-b9c8-e2f0a0c9c179 | -11.7047 | -46.3567 | 2025-10-08 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ab99e7af-2015-33fc-819a-3f7058f3b947 | -8.9121 | -46.5829 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1ded6da3-85e7-3983-b773-3fcbc13c0a9d | -8.9309 | -46.5809 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 25b724a7-91d1-30e2-860b-5e8b3b7b2297 | -13.8112 | -45.8057 | 2025-10-08 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 84ccee33-b34f-3707-9658-1febfb30f625 | -12.5109 | -54.714 | 2025-10-08 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 152.9 |
| ec8c3c88-36d6-37bc-bed0-1cef6cc63a7c | -8.6295 | -45.1 | 2025-10-08 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ede79b2f-bbee-3e23-a88a-d76eaea36c3b | -8.5398 | -46.2181 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b24a0425-29fe-3214-9214-9d9d2cdaf3e3 | -13.7918 | -45.809 | 2025-10-08 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4bd8c2a3-6d29-31e1-905b-6db8a450d892 | -9.3343 | -48.9364 | 2025-10-08 12:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4181bc70-316d-3cf5-9e0d-5fc51063fbbf | -12.5107 | -54.7345 | 2025-10-08 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 203.9 |
| a820c7b8-9e79-31ad-8280-6c8e6b597fd9 | -12.5297 | -54.7326 | 2025-10-08 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 06719874-ec58-37aa-a568-83dde0522862 | -10.4245 | -45.3907 | 2025-10-08 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 81570973-e533-3b43-91ba-e82f3c5b07ab | -14.7179 | -46.0867 | 2025-10-08 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 63727df2-1c2f-306c-8cd0-0fcc63a482f5 | -13.2662 | -48.0409 | 2025-10-08 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 565fd440-bc5c-3017-a726-e1d51552148c | -11.9523 | -46.4126 | 2025-10-08 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| aeae3295-e91f-3f47-928e-fae73154016b | -8.4827 | -46.2688 | 2025-10-08 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3fda0a1b-0faa-3784-a3ac-bc83d3ecd79a | -11.1455 | -54.882 | 2025-10-08 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 3e222e33-a832-3b02-b3cb-dd92b51123c9 | -13.8117 | -45.7826 | 2025-10-08 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 5467246b-6ce0-36cf-8eed-719d4a8b249e | -9.2096 | -46.9084 | 2025-10-08 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 411cd3c2-cc60-3fd8-a2d6-c01534ded0d4 | -11.6859 | -46.3366 | 2025-10-08 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1b8fe091-8326-36af-8d0a-fb15090d4d4e | -12.4919 | -54.7158 | 2025-10-08 12:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a4c114cd-7d5d-3b63-b11a-552e45111940 | -10.1874 | -45.9889 | 2025-10-08 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 552de56d-1cc9-322b-96e3-71cafd5d7ca1 | -12.4262 | -45.6366 | 2025-10-08 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8c890d47-b8d1-313c-95c1-27cb32793ac7 | -12.2525 | -47.8728 | 2025-10-08 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f09501bf-e6d8-3f87-a800-4f8750408482 | -14.7184 | -46.0636 | 2025-10-08 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 02870e06-ee51-3989-9924-113c05d4c8fc | -10.8732 | -47.0953 | 2025-10-08 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 33a9534d-3d2f-3802-90b1-68a6ec735331 | -11.183 | -54.8991 | 2025-10-08 12:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 269.0 |
| 218c8907-fddc-30f5-83fb-5fee74918b1d | -10.9296 | -47.1329 | 2025-10-08 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f8a2f94a-bf4d-3905-999b-232f93b2ac28 | -12.1576 | -51.4399 | 2025-10-08 12:50:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0cb35065-e905-351b-a9b6-fc18fdf2d1bd | -12.4267 | -45.6136 | 2025-10-08 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 577c3d65-5be7-32ef-8edd-ced940df45ff | -13.3774 | -47.2411 | 2025-10-08 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 33dc2e96-86ab-3b4f-8232-458ebdbc7b43 | -13.7368 | -45.6569 | 2025-10-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 68bbd0be-2cb0-318d-96d2-16d107d37fc0 | -8.5398 | -46.2181 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e31566f3-aaf9-32ef-8f4c-63122ff432b3 | -14.7179 | -46.0867 | 2025-10-08 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 248.7 |
| ca0b8ccc-66a4-3eeb-b3da-316cf2112f27 | -12.5297 | -54.7326 | 2025-10-08 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 9031706e-591d-3f8f-b2d3-182553842b2e | -12.2525 | -47.8728 | 2025-10-08 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9eadbbed-8ed0-3bde-a9d3-50180ac8d0b4 | -8.9121 | -46.5829 | 2025-10-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 97300c66-84b7-3cb4-b624-879cb453d720 | -14.3889 | -46.0063 | 2025-10-08 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f35bfbae-ab49-3c01-b013-0737753d6bf8 | -15.6198 | -52.5715 | 2025-10-08 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| df168254-667d-38cb-a22d-9ef395c97a85 | -17.954 | -44.4124 | 2025-10-08 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 47a8462e-fc65-313c-94df-1c2060d63c4f | -12.4262 | -45.6366 | 2025-10-08 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6d386b29-fae7-31a3-9ece-36f25b6d6305 | -13.7923 | -45.7859 | 2025-10-08 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 993a48df-1ff9-3607-a513-a2a9d5193235 | -8.8621 | -46.0724 | 2025-10-08 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f924b800-6718-39d6-8acb-0c958336eb34 | -8.691 | -44.727 | 2025-10-08 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 4fa7f922-0311-31fc-8309-1e858e054af5 | -8.6106 | -45.102 | 2025-10-08 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 055b3766-4a46-3a6f-ad3c-fae618736a08 | -10.4245 | -45.3907 | 2025-10-08 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 1a6ff113-578e-3537-87ae-fe09815f2a70 | -12.5107 | -54.7345 | 2025-10-08 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 205.7 |
| a4347096-ce32-3416-a6fb-6328e468ac46 | -13.3245 | -48.0101 | 2025-10-08 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7a2de30c-88a3-302c-81fb-2eb42023fe0c | -10.9106 | -47.1353 | 2025-10-08 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| dbbb9a47-34e5-3d86-b308-f3453304af6d | -12.0122 | -45.1929 | 2025-10-08 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 22d0298d-bf2f-3765-bc43-4564d5b42d67 | -13.7918 | -45.809 | 2025-10-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 4a0dc796-b76d-3cd9-9dc1-b37d3dd29221 | -12.4916 | -54.7364 | 2025-10-08 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 76250b50-ff8e-3317-b0d6-44eb97ea15ca | -12.5109 | -54.714 | 2025-10-08 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| e76f05d1-6b56-3cfb-bfb7-79d6a98c06f1 | -14.211 | -43.4573 | 2025-10-08 12:50:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 542a865c-e6a0-38d8-afe4-b1502c8a9679 | -12.1086 | -50.8926 | 2025-10-08 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 2acefc82-0971-355b-8647-1b03a7a9cd7a | -11.1646 | -54.86 | 2025-10-08 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 354ce337-5e60-314b-a62b-46daf14302ed | -11.7659 | -50.9107 | 2025-10-08 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bc81f7ae-689a-3cec-9ab4-888f3c9860cf | -11.7278 | -50.915 | 2025-10-08 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 402.2 |
| 3f372788-8541-34df-8a4d-e8b64f4b082b | -11.7269 | -50.979 | 2025-10-08 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7c1ac16f-bcc3-323d-88e9-c7f15349f959 | -10.1874 | -45.9889 | 2025-10-08 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fdd3e98c-df2a-3d5b-9a68-1295091fbf6f | -17.5828 | -47.1762 | 2025-10-08 12:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 94509fac-ebae-3668-90b3-5bdf519776c0 | -14.4079 | -46.026 | 2025-10-08 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5b61ce98-a538-3b38-9531-4f6f82c1ae06 | -13.7364 | -45.68 | 2025-10-08 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 351.0 |


[Clique aqui para ver as próximas entradas](README102.md)
