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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7207a4a9-e40f-3c97-8493-09917d7eea02 | -14.11172 | -54.52145 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 62414ad5-b8c2-35dd-ab3f-65264ab30d84 | -12.55098 | -57.21789 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bf3b8860-63b8-3d3e-9914-86f40c9ab295 | -16.47818 | -50.02777 | 2026-08-16 12:17:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5ea29122-252f-3c7e-bb9e-bb19aa8c4963 | -15.15692 | -48.66695 | 2026-08-16 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 037cacf4-de0b-323e-b1a9-347874944b7a | -16.47243 | -50.04003 | 2026-08-16 12:17:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 939e7134-a8c0-3af5-afc5-554f10ee758e | -12.00714 | -46.44138 | 2026-08-16 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| d09ef64b-e455-32de-b0ad-2e1b7d42ae4c | -12.14156 | -50.12137 | 2026-08-16 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 851b9c6d-2ff4-3895-8651-4f45c6cc3dad | -14.37879 | -51.90182 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ea61fddf-64a5-3fde-acea-3e7e0ab5cf18 | -15.14235 | -50.06492 | 2026-08-16 12:17:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 28ca1b73-ce14-39f5-8cfe-76f037246ff5 | -11.8844 | -50.61235 | 2026-08-16 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f625c746-983e-3378-84a3-59a8739e5588 | -12.54169 | -57.21648 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e3e78899-5f99-3418-9fc0-4a4ff9e71c8a | -15.21154 | -52.71584 | 2026-08-16 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e6005ac0-ab11-3909-9e28-cc63152c1a94 | -13.79812 | -53.78482 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 700ff7b7-d2da-3f1f-b1be-aca9bbb1fc90 | -13.70783 | -51.88396 | 2026-08-16 12:17:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 870e7f12-ec0c-3a4a-96ca-fa81b89d3145 | -11.9064 | -45.95868 | 2026-08-16 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f2dd1c40-d29f-3730-8b52-63d716f4752a | -14.29169 | -51.94699 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9bfcb03c-f161-3ea6-b3b3-9b35f13ccffa | -14.38199 | -51.87684 | 2026-08-16 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5272e281-9e9c-3a18-a25d-d99d411b77c4 | -15.10032 | -48.72264 | 2026-08-16 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 86fbb892-f4a5-34f5-8293-53c8b426e9fc | -16.47459 | -50.02171 | 2026-08-16 12:17:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c919fef7-3fb2-3523-a34a-e6703c0be208 | -14.88145 | -46.66668 | 2026-08-16 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| ca9b1a01-1fba-3c97-b5d5-6d0ea361c76d | -14.11301 | -54.51217 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 49822e1a-97e6-37ce-8027-eb660e6f6d37 | -14.89524 | -46.6445 | 2026-08-16 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7d9f35ca-1555-3861-b813-d8b315a278c8 | -15.07254 | -47.01252 | 2026-08-16 12:17:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3169734b-a971-3c57-8e6f-3ed3cf908e40 | -12.70975 | -48.47507 | 2026-08-16 12:17:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 897f66ec-defd-34a5-89b8-ff2e5586d82d | -12.70738 | -48.49486 | 2026-08-16 12:17:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 216.7 |
| 5487bd46-d019-301c-84e9-eea9b9b81fda | -15.21301 | -52.70464 | 2026-08-16 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fe5bfc0-73f9-3159-840c-7344f90a19bb | -12.68369 | -48.47088 | 2026-08-16 12:17:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bf4abd08-0a03-3a56-b265-86bf404ab6c1 | -14.03234 | -53.61957 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8c56e3d4-8dfe-31b4-9463-55151f4f0ee6 | -14.07694 | -53.70623 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8623aa9f-1ac2-3cfe-9947-44b523004ecc | -11.84338 | -51.78934 | 2026-08-16 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6cafbc62-288a-3069-b924-9493785d99cd | -16.4659 | -50.02654 | 2026-08-16 12:17:00 | TERRA_M-T | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 70584145-f958-3697-be4c-a60ca83187d9 | -14.10277 | -54.52015 | 2026-08-16 12:17:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 07f52771-24d7-310a-8aec-50b351679fe6 | -15.68949 | -53.81727 | 2026-08-16 12:17:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a0ad752-7c68-3b52-a7ce-c75ff49d5a88 | -12.55906 | -47.85756 | 2026-08-16 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 66d70c26-0c6f-3e0c-8b0f-bfa7afb727b6 | -11.81339 | -51.78555 | 2026-08-16 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| dceccc66-f817-38d1-82e7-59c03944f331 | -14.88447 | -46.6375 | 2026-08-16 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3b8a2da8-a9b5-3840-9222-6b793c0c4756 | -15.02977 | -52.70173 | 2026-08-16 12:17:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 20b3831d-c84b-345e-85d3-5e5ca4634b89 | -11.89349 | -50.6277 | 2026-08-16 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a5e942af-58e9-3faf-b000-f4a00f3c50ca | -12.70733 | -48.48098 | 2026-08-16 12:17:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 1ec19a92-6d83-3f2e-a0f3-497fbedde1a9 | -23.75884 | -52.85364 | 2026-08-16 12:19:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 909b891b-686f-328b-83fc-8fdf13ab2499 | -6.6664 | -44.005 | 2026-08-16 12:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 3cc2b597-a425-3d84-8bc4-703dce1c1466 | -12.0282 | -46.4471 | 2026-08-16 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7cd38a45-438f-30a0-aa45-f56e33b81fc0 | -12.0091 | -46.4498 | 2026-08-16 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 0d7227c9-ee78-3fac-9231-47a465450d99 | -6.6666 | -43.9818 | 2026-08-16 12:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| bb9ac0aa-2967-351a-9d73-ad9c8fa481f5 | -12.7017 | -48.4753 | 2026-08-16 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| ca69c448-f4eb-319f-926b-bc5ed9315a9f | -6.6852 | -44.0033 | 2026-08-16 12:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 416.5 |
| 2b8a2ed8-3d8c-35fa-8969-59055bab1267 | -11.0609 | -47.2503 | 2026-08-16 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8d827f34-b0f1-359f-b08b-0599718d2f97 | -12.0095 | -46.4271 | 2026-08-16 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 1eb27ee9-4626-3877-9884-8d403c21b4c1 | -12.7013 | -48.4974 | 2026-08-16 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 264.6 |
| ecd95c7f-9f5f-3ecd-8ee7-02502e380cd4 | -6.6854 | -43.9802 | 2026-08-16 12:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 497.7 |
| 364cfb7c-e62e-35be-952b-a73f516136d4 | -12.6825 | -48.4779 | 2026-08-16 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 044b9aae-0c60-3ffc-a559-2717c0a1e831 | -12.7013 | -48.4974 | 2026-08-16 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 4fbd2359-2565-32ff-abf5-9371c6d44208 | -8.9601 | -60.5165 | 2026-08-16 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5873885e-eba9-3fda-a6e7-d91baa332457 | -12.0095 | -46.4271 | 2026-08-16 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 194559ad-f4e5-3b88-8c6f-8253bdc14bcc | -12.0282 | -46.4471 | 2026-08-16 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 53725702-ff01-3251-b8e1-511b9037bcfe | -6.6852 | -44.0033 | 2026-08-16 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 397.4 |
| 37d555fc-054a-3fa6-b2ad-c7ed6ffd2618 | -6.6854 | -43.9802 | 2026-08-16 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 427.9 |
| e9825243-219a-3a16-a0f5-818ac02d3580 | -12.7017 | -48.4753 | 2026-08-16 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 17f1d4eb-7201-334b-bc44-1972951d16c4 | -11.0609 | -47.2503 | 2026-08-16 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 46173288-bac6-34df-a2c4-77ca06247a2a | -6.6664 | -44.005 | 2026-08-16 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 91ef9053-d21c-3b9d-af7b-1e96724fb4a9 | -6.6666 | -43.9818 | 2026-08-16 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 90c156cf-1c61-3f35-ae92-1db90e1b449d | -12.0091 | -46.4498 | 2026-08-16 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 4ec07207-6088-3787-906d-2392e3863c5e | -12.0087 | -46.4725 | 2026-08-16 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a17fbbdc-8c83-33ec-a022-8083fe3facf6 | -12.6825 | -48.4779 | 2026-08-16 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 7d440ded-27f0-3310-84a8-0462498c458c | -15.0682 | -47.0098 | 2026-08-16 12:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b5a47485-034b-3871-8dd4-73953b4b90b6 | -14.3923 | -51.8867 | 2026-08-16 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 61df2040-fbe2-33e3-8c62-e021fab19f5e | -12.7013 | -48.4974 | 2026-08-16 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 7020f96c-4dcf-372c-8f3b-75c5a966145c | -11.8291 | -51.7937 | 2026-08-16 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 2f3b3e33-e097-3ec0-b76b-55177f15f96c | -6.6852 | -44.0033 | 2026-08-16 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 589.4 |
| afb48029-e157-3877-82a6-5689bedb61a2 | -12.0095 | -46.4271 | 2026-08-16 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 171ff8b7-649e-3d6e-8721-113dac19d74e | -8.9787 | -60.5156 | 2026-08-16 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ce491408-6768-3c89-9c04-842b718bd89e | -11.0609 | -47.2503 | 2026-08-16 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3c391d11-ed30-339e-9097-99bb49834d80 | -12.0091 | -46.4498 | 2026-08-16 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 51d01887-dccb-3fd8-b3a2-5e11d75f2e83 | -11.0796 | -47.2702 | 2026-08-16 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 32b8124f-baf0-3cd7-bcfc-e589dc227509 | -6.6666 | -43.9818 | 2026-08-16 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6ce805e0-eb01-397d-bcb1-5049b30fa031 | -10.9746 | -50.5291 | 2026-08-16 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5f7f60f7-69a1-366a-b9d5-1b1528f6d53c | -6.6854 | -43.9802 | 2026-08-16 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 804.4 |
| 5f73dfa8-5d22-3178-9cbb-1fd88546a952 | -12.7017 | -48.4753 | 2026-08-16 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 33974890-3ad6-36db-a4a9-7e96c90cb811 | -11.08 | -47.2479 | 2026-08-16 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5f3668b3-d217-30f5-9845-20aefae4fffd | -14.3919 | -51.9081 | 2026-08-16 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 5011f483-1d4a-3562-a3b3-02d8fa854d89 | -6.6664 | -44.005 | 2026-08-16 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| a94f5763-e69f-38fd-804e-30c8946bd31a | -8.9601 | -60.5165 | 2026-08-16 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 13ca89df-65e5-38c4-85d8-e1595d057e6e | -12.0282 | -46.4471 | 2026-08-16 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 1996bbb2-5a1b-38e7-b492-47ee87e87817 | -6.6854 | -43.9802 | 2026-08-16 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1044.1 |
| 5bb48bc1-a27f-33ca-a1c8-aed391bdb65f | -11.0796 | -47.2702 | 2026-08-16 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ad7e5ad0-be27-3dfd-92f3-3664af9b37c8 | -11.08 | -47.2479 | 2026-08-16 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aded6bb3-c9c3-3d15-b542-b5ad0d005362 | -12.0091 | -46.4498 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 3185a383-70c5-3f07-a5a4-e8566bf34f80 | -14.0737 | -53.6971 | 2026-08-16 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3c98ff48-df85-3d7e-8da7-f6633af8f24e | -14.3919 | -51.9081 | 2026-08-16 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b21c5102-b6be-3453-9c71-74feba6eecc5 | -12.0095 | -46.4271 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 54630769-c7ef-35d3-ac1d-60ab41dd0e3a | -14.3923 | -51.8867 | 2026-08-16 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 659cf215-26aa-3eca-9310-4f3b23cbb216 | -12.0087 | -46.4725 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ab7c6541-5ede-356c-8ea1-961638698dba | -11.8291 | -51.7937 | 2026-08-16 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 62078b67-46c5-3d50-98c4-eea4a95a501b | -8.96 | -60.5358 | 2026-08-16 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| bb56765e-a246-3707-8c01-d3a53facbd2b | -6.6852 | -44.0033 | 2026-08-16 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 864.9 |
| 297771f5-182b-36fe-896a-1957689a7f95 | -12.0286 | -46.4244 | 2026-08-16 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c343f0a4-efd8-3d61-ad2e-6729a04fa424 | -8.9787 | -60.5156 | 2026-08-16 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9d971676-2b9c-3a52-8fb0-44a3e992a18e | -15.2095 | -52.7127 | 2026-08-16 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3154a194-5ccc-3a2a-aa99-7628ef85a367 | -6.6664 | -44.005 | 2026-08-16 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 9e085611-23e5-3a1f-bf45-74829558903c | -6.6666 | -43.9818 | 2026-08-16 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |


[Clique aqui para ver as próximas entradas](README61.md)
