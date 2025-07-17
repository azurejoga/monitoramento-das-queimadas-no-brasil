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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbfbb17b-e97e-3380-8779-c4d789eb8d42 | -3.37313 | -47.49457 | 2025-07-17 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 1215a0ac-5bb0-31ea-991f-20dacd0db553 | -9.48786 | -40.39158 | 2025-07-17 05:18:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 339e02c7-0c82-3705-885e-9472b62ca4be | -6.71298 | -44.32385 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 85732107-4a6a-351b-8a7d-018ef1989450 | -9.37822 | -40.6184 | 2025-07-17 05:18:00 | AQUA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 065da2b7-a292-3d17-b31c-21d3e1ada655 | -3.37874 | -47.49034 | 2025-07-17 05:18:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 532eb99d-49ff-3830-8d3c-3861dfdaee9b | -5.52492 | -43.87983 | 2025-07-17 05:18:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7bf92da9-fceb-3e8f-a528-32189abb9f73 | -6.72457 | -44.32572 | 2025-07-17 05:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3ab01f70-c0a6-359f-8ea8-27ce7dc3ee7d | -8.09799 | -43.14696 | 2025-07-17 05:18:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| dd177cf2-3550-3779-b1fd-e963e2795755 | -25.11537 | -49.18406 | 2025-07-17 05:18:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90d92c75-a7c5-3949-891a-d5b3baa6da62 | -25.12168 | -49.18476 | 2025-07-17 05:18:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4796952b-97ab-36aa-a78a-ceffd5c83ea8 | -25.11742 | -49.18443 | 2025-07-17 05:18:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b014fb90-68a8-34fa-bcc2-4d657ddcf0c2 | -6.7194 | -44.3231 | 2025-07-17 05:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 672c7c48-04e3-3125-9a5a-135b88447d55 | -5.6567 | -43.7161 | 2025-07-17 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 5decd68f-55d6-379a-90db-eb38c72e6d91 | -3.3958 | -47.4785 | 2025-07-17 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6f5f7235-3281-38a4-9af3-f848a420d3d9 | -17.3628 | -44.1399 | 2025-07-17 05:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7da432a5-3ef9-32e5-9959-2441b5466257 | -5.6754 | -43.7147 | 2025-07-17 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| aa1ecd52-bb6a-394f-abf3-9c40a9c7e410 | -17.35968 | -44.13478 | 2025-07-17 05:21:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 82fa8b46-1921-38a0-b42a-0a7eef404577 | -17.35791 | -44.14563 | 2025-07-17 05:21:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3bc289a7-bfc2-3a3e-91f9-2e135b4e7488 | -17.15576 | -46.10828 | 2025-07-17 05:21:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b23679a0-d494-3038-a9f8-34e388cbb0b4 | -20.0033 | -49.05032 | 2025-07-17 05:21:00 | AQUA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a856c2b8-fde6-331d-a285-8806cdb61339 | -19.96305 | -48.99031 | 2025-07-17 05:21:00 | AQUA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 126.1 |
| f01f6d39-160b-3b40-b11b-3f397c36dd1f | -17.15611 | -46.11499 | 2025-07-17 05:21:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2cc1e7b4-5df3-3391-9304-4c6bf4859b7e | -19.96423 | -48.97583 | 2025-07-17 05:21:00 | AQUA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0199f2bf-2894-3415-90e1-e4f494d1a255 | -19.9601 | -48.99708 | 2025-07-17 05:21:00 | AQUA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d51b72aa-7613-3238-8e7f-f9dbda32ad19 | -20.99328 | -49.75925 | 2025-07-17 05:23:00 | AQUA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 287b1969-cd2a-3f1a-b17c-b1f12d1e1a90 | -23.25325 | -45.56789 | 2025-07-17 05:23:00 | AQUA_M-M | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ad10a708-5e5c-3adf-b476-5174db913cc7 | -23.25141 | -45.57896 | 2025-07-17 05:23:00 | AQUA_M-M | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 4ff9fd95-bc74-3058-a724-5dc2df9a9ea7 | -5.6754 | -43.7147 | 2025-07-17 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9c6cd9aa-7ebd-341b-a97b-614072792baa | -5.6567 | -43.7161 | 2025-07-17 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 713cadb7-d9a9-3462-81cf-c4bda30a38b4 | -17.3628 | -44.1399 | 2025-07-17 05:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4d2fbffa-0a05-3063-8ee6-d24f7921d3c5 | -6.7194 | -44.3231 | 2025-07-17 05:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1f5200b4-9cb5-3b9f-838c-101cad256044 | -5.6565 | -43.7393 | 2025-07-17 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b3d87075-af58-38b6-97d1-82f634e9dece | -3.3772 | -47.4792 | 2025-07-17 05:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6f5bf925-8e5e-3ffd-9b7b-1fa75cc7a9b3 | -6.26818 | -57.39811 | 2025-07-17 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6c78b7-b40b-3c1d-98e0-acb8732a9b56 | -2.58728 | -51.9227 | 2025-07-17 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cfc642-68da-3295-9af6-db1c03b2989a | -4.36757 | -55.77053 | 2025-07-17 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2c3badb-0faa-38b2-8570-ea6c20151317 | -2.58659 | -51.92724 | 2025-07-17 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c5bcef8-e9e2-3eb0-8ee1-293a5f76ebc8 | -7.50958 | -55.01051 | 2025-07-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 077e3ec0-e822-3b6b-a40c-dec5c95e33ea | -12.50103 | -57.78522 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36865b5e-598b-3981-a1ed-6f82c485d587 | -11.8708 | -55.4484 | 2025-07-17 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 562a2d30-2c05-378f-baf8-7f8b58394674 | -8.42789 | -64.03287 | 2025-07-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8929a28d-bc39-35d2-bf8a-71ce8786c52e | -10.05626 | -64.99619 | 2025-07-17 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24c48d08-0b44-3547-846b-3be0c04a1212 | -10.67941 | -56.54714 | 2025-07-17 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d08e9c0-537b-3b8e-a9fd-11a7f02d1f55 | -10.6744 | -56.54641 | 2025-07-17 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f051a2d6-a0b9-367c-9df4-72289a3097a5 | -10.05194 | -59.10454 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9f46f38-ddf4-39b4-8c81-c3a87646e843 | -11.87629 | -55.44911 | 2025-07-17 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1f7388fe-20b0-38b5-9c27-38597f2871f9 | -12.50368 | -57.78973 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 907951f6-a6cc-3547-a812-b30dbc9b189a | -9.02073 | -61.22392 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 668c8385-3aa1-370a-947f-5306c317e920 | -12.50034 | -57.77878 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d952e311-c09f-32fb-bbc5-f9e55de3d584 | -10.05611 | -59.10516 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8132deec-b23f-330b-872e-6370d9b101c8 | -7.89726 | -55.42181 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40d9f0fb-a3cc-39c0-9db9-9e50ae78a45c | -9.01712 | -61.22337 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f2b7838-b9a2-3ec3-b3e4-a3704889aa73 | -10.05755 | -59.10455 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2910ddb5-041d-3c64-b8e9-2a8569e30118 | -9.02435 | -61.22447 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc495eec-6ca4-350b-a072-bad91022b57b | -10.24341 | -59.27431 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4831cb35-3495-33a7-974f-02de8af73814 | -9.0858 | -59.47008 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fabcc35-7db9-30d3-a031-7bc1732876fc | -7.89207 | -55.42101 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5835f5c-a24f-3b52-9b5c-d801736055f3 | -12.50508 | -57.77933 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 012a144c-83fb-3374-b7ee-25fd8ef7cceb | -9.71236 | -61.29277 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53bce69b-6a0f-34bf-80e3-943ff4b30eb2 | -10.05703 | -59.10836 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1006fd1e-6c62-3a4a-9fbd-6ecb7e4cf660 | -7.49019 | -63.81673 | 2025-07-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b11d2fa2-7b8c-3b02-a72f-0bf679a789fd | -9.08179 | -59.46947 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c302bdec-c334-36e4-b139-2d06cc625de6 | -12.50169 | -57.78001 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e1c346b-bd7c-3e8d-81c7-8cd10a197498 | -8.42458 | -64.03234 | 2025-07-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c31a7c45-02df-30c6-9b6f-b8186581ddda | -12.49965 | -57.78396 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 15d3c83b-647c-3ca0-b6e4-3a7a5f49c32b | -10.67979 | -56.5442 | 2025-07-17 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0f131e0-f928-321b-bdf7-28e19b7d62cf | -9.46264 | -63.14648 | 2025-07-17 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ea751a5-33f5-3973-ac56-d0616ef04920 | -9.9012 | -67.01283 | 2025-07-17 05:36:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 683ab527-18ea-30b0-b659-35fe46d22923 | -12.50437 | -57.7846 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1c6cf1e-dd10-3867-b273-715010d6db13 | -7.88315 | -55.36823 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98915c99-1a76-3ab6-919c-7dd5a7c2d312 | -7.88728 | -55.37093 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2485f34b-add9-3868-a569-16597906b39f | -9.17707 | -59.78224 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e7033c8-0a6b-3541-aaff-44377972e78b | -9.13274 | -63.91244 | 2025-07-17 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9286a7e5-75b7-309a-9238-5dd33e16c978 | -7.48688 | -63.8162 | 2025-07-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 736e8d4b-e5f5-3259-8440-45d65fa76c62 | -9.02632 | -59.54372 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34b43d20-570d-3dd9-98e8-980b85fedb6d | -12.49695 | -57.77942 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 077799a0-1697-3a18-9f93-73fa1c125d77 | -10.05249 | -59.1007 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2666660-366f-3c45-bb50-93c3b9d1e6be | -7.88252 | -55.36696 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e107703-5f50-3ebc-b191-ead28eff7cdf | -11.87585 | -55.45272 | 2025-07-17 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9b7dde2-862a-3906-bef6-c2b6277fde9a | -7.88207 | -55.37017 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd170485-9612-30df-8456-538e8e3ecad9 | -10.11019 | -58.21811 | 2025-07-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89ae83ad-bf80-38a4-a933-60f5a281f8bc | -10.67478 | -56.54351 | 2025-07-17 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b284bef-13de-3afd-bada-08fc022e728a | -9.92714 | -63.11668 | 2025-07-17 05:36:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13ec135b-d0ef-31a4-a57a-bb1f5cdde4b3 | -7.50273 | -55.01178 | 2025-07-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55eb5622-e849-31b3-b8b6-8d8f5d8ac21a | -7.50385 | -55.01273 | 2025-07-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c82b7602-1844-3bd9-a169-155486d785b0 | -9.71299 | -61.2885 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f44440c-e0eb-3d3a-9da3-2c87f16dda4a | -9.71663 | -61.28904 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1794bf31-a939-3ae6-b7f3-ea56a9c961cf | -11.87036 | -55.45201 | 2025-07-17 05:36:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35c66da5-3f6f-37e5-8f51-0532f8e715d2 | -9.46208 | -63.15009 | 2025-07-17 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c743083-f7e1-3c9a-b775-8eadd189658b | -7.50911 | -55.01381 | 2025-07-17 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182ea460-d758-3726-a368-d7728c60cd14 | -10.05666 | -59.10133 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8981fc3d-d4b5-32d2-b3f8-a9475aa756ab | -9.02497 | -61.22024 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b0ba0b-aa33-3018-b17f-892313d962e3 | -7.90005 | -61.52245 | 2025-07-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b012b563-c48f-3ea6-863f-e90ec47c752a | -7.89165 | -55.42413 | 2025-07-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce9cf53c-3a67-31b0-a760-56e4f0024c45 | -9.0165 | -61.22759 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09876778-80d9-3e17-a2ad-663ed82e44e8 | -10.05556 | -59.10897 | 2025-07-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2cd3d76-f80d-3898-837f-1597de0bcfbe | -9.94911 | -65.09354 | 2025-07-17 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6b32b0f-85d7-39be-a6a2-dff6f965b0cf | -9.16294 | -59.71276 | 2025-07-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21edb321-b0e3-3275-a6de-9181313b11bf | -12.50576 | -57.78587 | 2025-07-17 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ebe84be7-4902-310e-bbf6-3e8bb70ed7c5 | -9.10182 | -64.15421 | 2025-07-17 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
