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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87b93e14-1f5b-3d89-ab2c-7dea449e34fc | -11.47517 | -57.11108 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7027e9ec-d199-3229-a92e-772dfd0ecbdf | -10.78368 | -46.93314 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 544b504d-32e1-3566-b130-c694fdd17171 | -12.1315 | -47.21711 | 2026-05-30 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18477534-a934-3bd8-8995-9095eaf90f0f | -10.63125 | -48.32342 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e8b88298-cf8b-3521-a457-883c411b05f3 | -11.59973 | -47.44416 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9525e45-2e58-3878-9337-cc68d3948bce | -10.80039 | -46.95755 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 524882e1-0e7d-3087-b96e-ac8c10af3be0 | -10.62675 | -48.33001 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c7d8af6-a804-35c3-95d6-28ecef4c231b | -11.47504 | -57.1045 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7d9baad-32b3-32ce-848e-b1f30eabe15b | -15.80655 | -58.68048 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 66baf951-035e-3d25-b51a-84b9951c3eb0 | -11.76227 | -47.07438 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 723f6dcb-755a-36c6-94c7-6678fd63ca8f | -10.82206 | -46.9284 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3aa131e-42f3-3a71-8f99-c8f382e85d04 | -10.77037 | -46.97448 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b1f32db-aafe-3c19-9958-c94b7b194a3e | -11.47586 | -57.10756 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8748bea-753d-35d6-9a00-47b422874544 | -11.80508 | -57.00902 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d71e383-0b14-3cb9-bc5b-ba84b401573b | -15.80577 | -58.68419 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b63aa06d-a6ff-3396-8502-de43e9342596 | -10.80204 | -46.94698 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e7882c6-8492-3f03-b484-947db6f207c8 | -10.78145 | -46.92554 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c59aa5c3-4b8e-3a19-85bc-121e360639db | -10.04047 | -52.10065 | 2026-05-30 04:38:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ff5783d-7d12-3b46-b6ca-00efb41fd2d6 | -10.80758 | -46.9116 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca8889e3-44d1-344b-be39-d1feb4087d48 | -16.16965 | -58.47084 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 84c36172-b8ae-381b-9377-a52a6841726f | -11.90946 | -43.83179 | 2026-05-30 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ef1cbf-6dca-3b95-9ef8-a008a3877ce7 | -10.84851 | -48.34088 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90747c0-d080-3d37-a03a-986967d6e5c5 | -10.80403 | -48.2969 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2014d654-04ac-3387-b621-927692b27c79 | -12.44552 | -44.74888 | 2026-05-30 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 180c1938-c01c-3c5b-a684-592cdea83eff | -10.81758 | -46.89144 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455956db-5788-3c87-9435-9195315fb293 | -14.13262 | -58.93172 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 742ea20e-10e2-3283-9c80-2ec4ff5ae55c | -11.62727 | -56.8676 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9e0157b-35a7-3896-b373-eee8dc531e11 | -10.38919 | -49.44405 | 2026-05-30 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1479d92a-11c5-3b5b-9798-ea8c609adc15 | -10.80593 | -46.94398 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78bea689-2b24-324d-832e-0e0459c3115e | -18.11854 | -42.43903 | 2026-05-30 04:38:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26ff2254-533b-3a23-ac70-e8d67afec825 | -11.59084 | -47.45722 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06c3b33e-53db-3a5f-b6a3-899e79ea9f97 | -11.92636 | -43.92825 | 2026-05-30 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d08d2eea-a9b0-3e51-a94c-cdb50cbb6fcf | -10.84375 | -46.94278 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d0fed0de-196c-33aa-bf24-72a6572cb151 | -11.58529 | -47.44907 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45081d9f-004d-3de4-aa77-571f5385506c | -10.80067 | -48.29638 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4343a57-ca89-33b5-86e0-fb61a31ec955 | -10.63068 | -48.32699 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc236d33-3e49-396b-9dfd-a980b926b9ee | -10.78313 | -46.93667 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b294bca-66a8-3e20-aac6-d9edf5d4822f | -11.58807 | -47.45314 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4edb40a9-1e5f-3d36-af55-0d5344746f51 | -10.79261 | -46.96354 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b7fb896-2b92-3eee-9c6f-1eafda530d76 | -11.99819 | -47.76947 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44f66a38-c1fc-3e39-99d2-904b2bc453bb | -10.63812 | -49.72897 | 2026-05-30 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a3e044-db77-3914-a295-1d7d6702a1e7 | -10.8443 | -46.91748 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f546418f-27c1-3ad7-8706-3b42a6d7e2c0 | -12.00621 | -45.35968 | 2026-05-30 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b63c7b24-e8b1-319b-b392-f26dfc959896 | -11.16796 | -46.79085 | 2026-05-30 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b5c4bd4-9f93-3d8e-ac9e-d140eecbf908 | -11.62791 | -56.86423 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1425735d-afc8-38d1-84fb-f20a2599acad | -10.84153 | -46.93518 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d8fc899a-1095-3d2b-afbf-dbd66d3bd7d2 | -11.63136 | -56.86708 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9393d51-3862-3ea7-bcf3-2a3dc98ed0d6 | -10.84319 | -46.92455 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90fc8fa6-4632-315a-9472-6f6050d1bfe2 | -11.47437 | -57.10802 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d0436bc-a556-392d-9458-6ce2030a6595 | -10.73123 | -49.02371 | 2026-05-30 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7ab7039-2a24-3b07-a036-b96ddc204fda | -11.59696 | -47.44009 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de17d3bb-740e-3c68-97b0-91735d38e4cc | -16.16852 | -58.47124 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d713b9bf-257d-35fa-846a-820c6e9ac649 | -14.13086 | -58.94016 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a642e765-95b5-3014-8b72-ed29d3f8b11c | -11.63266 | -56.86043 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e41a76d-af18-3549-b955-17f3ad9ff480 | -16.17317 | -58.47604 | 2026-05-30 04:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ed5a66f3-e04b-3b29-a2cb-9a34b19c9e23 | -11.58418 | -47.45613 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bea4fc95-626b-3ba5-9876-72608e779835 | -15.782 | -58.66385 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4b21e60a-97a5-3c43-b049-00301f045531 | -10.97141 | -49.4339 | 2026-05-30 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 470b2473-be75-3f0a-baf3-afef0a5249ed | -10.81479 | -46.88738 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd66334c-aaa0-3d63-9a30-2e7b5e14598d | -14.13225 | -58.93579 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1447f9e9-7176-3a63-8350-7ebd5a853af5 | -10.8379 | -46.921 | 2026-05-30 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a2032441-0caa-3d07-83f6-e5f3369aff5c | -10.8375 | -46.9434 | 2026-05-30 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 631ff157-0687-30f6-8234-35998e3bb4c4 | -10.8566 | -46.941 | 2026-05-30 04:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 47111537-19ed-3f98-9aa4-16f3d3060f0f | -21.81103 | -49.13437 | 2026-05-30 04:40:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 93b71bb5-bc0f-3df4-a33d-57071d82f3d3 | -21.29848 | -48.58429 | 2026-05-30 04:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| bffe414f-a53e-385e-b6b1-62a8ee26fdd1 | -18.46169 | -54.70903 | 2026-05-30 04:40:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2b434534-4b22-3ad8-b997-10bcaed79aef | -20.18825 | -49.56293 | 2026-05-30 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 515c6156-df21-38e6-b3bb-b19c388b59a3 | -22.86727 | -42.37651 | 2026-05-30 04:40:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4244ea9a-c6a0-36ad-b81c-c2826923415f | -18.69351 | -47.30667 | 2026-05-30 04:40:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45b84b7b-a108-334c-9547-33f6cecd71d2 | -20.62562 | -51.70297 | 2026-05-30 04:40:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de3da872-90af-3b47-bd4c-55172683a77f | -21.25433 | -49.35696 | 2026-05-30 04:40:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d8c94319-a5e8-3aaa-8615-696420b39a3e | -21.30187 | -48.58488 | 2026-05-30 04:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6020fcbe-1c92-3211-964f-5bed6c66ab34 | -21.25098 | -49.35637 | 2026-05-30 04:40:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb736350-dcea-34ce-b4a5-d509c928b8d4 | -19.68436 | -54.35272 | 2026-05-30 04:40:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8141cf15-ee24-3dc9-af5d-885924e83e51 | -18.23788 | -54.59436 | 2026-05-30 04:40:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7948dd0-a812-3cfe-ba12-2b58f74a762e | -21.80767 | -49.13379 | 2026-05-30 04:40:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2b5ab3a-d304-359c-8f24-28b6a998297a | -21.81161 | -49.13058 | 2026-05-30 04:40:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7cd563e7-5a3e-3bfe-a023-09990020dfa6 | -18.241 | -54.59407 | 2026-05-30 04:40:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43adb47c-ad74-33a1-93e9-755225aa0d85 | -20.62837 | -51.70756 | 2026-05-30 04:40:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22a54840-464c-3676-a48e-c9668f2009ec | -20.42739 | -47.52597 | 2026-05-30 04:40:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49e0bc56-96ad-328d-aebc-c8da26b1897b | -18.46099 | -54.71273 | 2026-05-30 04:40:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb2bdc5-5cb7-36e5-8efc-49a9e52cd5c9 | -21.21427 | -48.54294 | 2026-05-30 04:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5059c33a-9af4-3727-8215-e7ae95b25ac3 | -22.87073 | -42.37739 | 2026-05-30 04:40:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 064cf3d9-a757-3ad1-9268-a97f4d66f6bc | -10.8566 | -46.941 | 2026-05-30 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8ad57cd8-5711-3fbf-b8fd-95f87cd4bc56 | -10.8375 | -46.9434 | 2026-05-30 04:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 24c5bdb5-ccc8-3dfc-87aa-a30a8f89afaf | -6.28569 | -48.53374 | 2026-05-30 04:53:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28f3efd9-bfc3-30e9-9c22-2066a7d3ef8e | -7.33775 | -49.85944 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bd0aa92-ca10-301c-a5bd-90c97c1e3cb0 | -8.02467 | -46.58101 | 2026-05-30 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dd5caff-df47-37ac-9c25-4e945b4f97a1 | -6.25442 | -48.56217 | 2026-05-30 04:53:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d06bac89-6d1d-3602-8e90-7db408ddf870 | -6.75372 | -45.00968 | 2026-05-30 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18e5d99a-13cc-3904-bb04-9719a6d55682 | -6.28443 | -45.46443 | 2026-05-30 04:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33f2555e-0e93-3fba-86ba-48d1a6ad55a2 | -5.92267 | -43.47835 | 2026-05-30 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3afabe20-bbe7-3c65-8b50-88f0bea89dc4 | -7.33543 | -49.85069 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 284fe5e1-9db3-347c-9198-325c01118b00 | -8.01965 | -46.58466 | 2026-05-30 04:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88cb2802-1755-3f33-bb04-f299a0ffda49 | -7.61434 | -49.46719 | 2026-05-30 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d32dc8a-37ca-309d-89d1-250b0a7dad36 | -7.33481 | -49.85479 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a360cf5-92f2-3af5-9b23-87927ffcfe38 | -5.94873 | -43.48513 | 2026-05-30 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fb552c5-b0a6-350d-b4ab-c32aa19bac8f | -6.75853 | -45.01043 | 2026-05-30 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 331df9c1-4792-3ff7-821c-756d670d71a6 | -6.25467 | -48.55956 | 2026-05-30 04:53:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb676b75-88ed-3341-abae-4251a7d95f2b | -7.33418 | -49.85888 | 2026-05-30 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
