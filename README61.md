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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5976954a-4177-3acf-9ff3-da42803ab4cc | -9.70103 | -61.2843 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40c689ec-a26a-3548-b549-48d8709335fd | -8.67056 | -62.42595 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8991ab22-8878-3d23-a086-222cc468588f | -8.54989 | -51.30033 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f43cf621-7961-38cd-8f4f-87282d287821 | -11.6009 | -51.94778 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f70e01d8-3b58-3ff0-ab22-98a3d098b349 | -9.45421 | -60.56868 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9652a950-535c-3f76-a67f-827667bdfdca | -14.03507 | -44.55445 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aacffdbe-7276-3cc7-8f33-ffcded30fd55 | -11.31681 | -43.69122 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 110ae600-e67b-3ab1-a46c-e5ac959661fc | -11.81244 | -46.44948 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5dd90781-0edc-3f0b-93c5-74e0f5d28a90 | -12.93907 | -56.97932 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25739651-a1d0-3ae5-aa96-3f9f362a2ffc | -11.82941 | -46.4309 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aa8707dd-1785-3c24-9347-710fd9cdac39 | -7.95497 | -46.38931 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58d80739-f409-38b5-b124-de07ef009174 | -11.90368 | -46.4263 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 436eefba-771c-38a8-a691-67b4e54c45b9 | -11.07724 | -52.05614 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f2ffff-207b-3223-b2ab-30f3244aeb90 | -9.071 | -65.44308 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ad63d28-a6cf-3684-adf4-3db8356344d1 | -13.46581 | -46.98097 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b7abf59-5514-3d5a-918b-1035d87bf754 | -11.07896 | -44.63193 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d10f9422-4a6d-32f0-8722-3015825d42c3 | -14.49441 | -52.99155 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5ae2fc7-318b-32ad-9c5a-b707bae6b09a | -9.69858 | -48.29496 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1fd1ba3-2d5e-33de-87f6-d00f6709de30 | -11.06083 | -52.04971 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 289d4d92-4797-3400-b427-42fcd697aee7 | -11.0067 | -46.84506 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38f8a981-17e5-3cdb-b096-b5b1433eb4e0 | -9.44122 | -60.56105 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09bc3192-23d7-38eb-89dc-c0d1dc966ff4 | -8.69364 | -62.41996 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c4a4c7d-ba65-3d1d-93f2-2d2025b487a1 | -13.30669 | -46.88327 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 468f49b0-4754-3b6f-9f3e-69ad5af60485 | -7.95111 | -46.38436 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec2915c1-29a1-3972-af0e-24a18cf978c2 | -15.07089 | -48.62336 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b17d3038-ef61-319d-872b-843ff5271ea8 | -11.06826 | -44.64041 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc00f30b-e858-3285-819e-a4a85d660537 | -12.43752 | -63.92524 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9e84880e-8131-3597-ac87-3114f010e3a9 | -8.96623 | -50.01088 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e70c338-4084-34cb-91c8-ccfce2fe1da2 | -11.31589 | -43.69889 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7981b956-d551-3d0f-a420-14e7828d9e1a | -11.07698 | -44.61477 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b9396f8-9e98-37b5-a630-31d8fd569e6f | -11.89138 | -46.73064 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b4b1586-45bb-3c40-9051-ec0c604c1766 | -13.68966 | -46.88848 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92049a8f-e3ea-3436-9dff-a22f18640108 | -10.31772 | -59.19281 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97cb351a-a71a-3950-b650-f6d82bfc5078 | -7.70619 | -50.27661 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38248310-e701-3b86-b2ee-00a1f5b106b6 | -11.9173 | -46.70088 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65bc280c-7ce3-338a-a54f-e988c581eae3 | -11.00738 | -46.95078 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9273b747-ca57-327c-a4ee-77d7724447c1 | -9.45308 | -60.54816 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5f0b59b-1a3e-3e77-b64d-fbd0779ef042 | -11.29991 | -43.66413 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cd888d9-2fdd-36eb-8361-2a6f7fdbb65b | -12.83635 | -48.08226 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b125ed0-54b8-3c91-90fa-016f82248cdd | -11.82535 | -46.5101 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8b284f-54e1-392e-8693-c26548937eb2 | -9.68286 | -47.04525 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0e0e34b-66d4-3b19-85b8-a31baf0a7e51 | -9.45223 | -60.55294 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb952dd2-4e22-34cc-aefb-f31307eeccc0 | -11.06365 | -52.054 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 216eadfa-f40a-30a6-90c2-521d2524b8dc | -11.81384 | -46.43911 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d92e1b6c-0c49-32ac-ad5d-2754aeb51dc0 | -8.65089 | -62.44308 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3404d6-1b6c-3ae1-b574-764c94f635ba | -13.48151 | -46.9695 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f3093580-261e-33f6-ae18-d09c05a17ed6 | -11.89946 | -46.38522 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae7606ad-687c-34fd-82de-df771579b80d | -7.95046 | -46.38881 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa04d133-70de-3cf1-8b25-77506f33fb70 | -10.70805 | -49.00827 | 2025-08-31 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbab29cc-cd53-33b7-bceb-482c6b783f66 | -11.86447 | -46.50438 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acb6b006-4e9b-34b7-a2c1-30652ee950f6 | -11.68956 | -51.68516 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f435813d-cf5f-3255-bfa6-b13c5862edd2 | -11.02162 | -46.87783 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b61518c-8e24-3ed1-a159-1ea283af3e6a | -9.10923 | -65.76405 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd159369-0ed1-3c09-8ea5-53ceed8dcf39 | -9.44005 | -60.54083 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d41a931-470a-33c8-9126-71b4f555617e | -12.93063 | -56.98625 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26cdb488-1368-3e13-9efb-b16b01ef27b5 | -13.66956 | -46.93251 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 521b35fd-597c-3a32-8511-2fab18fece59 | -14.32559 | -51.86296 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7208ec90-5580-31d3-b9f1-50b927f14f7a | -11.21685 | -45.01859 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd50c8f7-06b0-33d4-bb21-72c94c395714 | -8.90215 | -62.10703 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81d437f7-aac5-30a3-98f5-0a3361d48e84 | -12.22446 | -64.22803 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7050bae8-f3ed-3ea3-b528-41dca1cd5c1a | -7.97252 | -46.41245 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2bd0788-703c-321b-b293-f52bf796c41e | -10.9603 | -50.86155 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f434f567-302d-3b21-bab7-b3e7de409872 | -13.01606 | -56.90811 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d09d12-76a4-3b49-9a28-8e59d1f6f535 | -13.57518 | -46.92328 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff5292d0-1944-3eb6-92fb-d3d679b224f5 | -10.60564 | -44.32586 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 699e40ba-9bfe-3ae6-99b5-cf74155d7503 | -8.64948 | -61.94883 | 2025-08-31 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98e9c775-2bdb-348a-981d-d7b83c40eb3c | -9.25399 | -47.06701 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a456f066-64c7-37c8-9efc-c0d5cddbad62 | -8.74334 | -62.38781 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1f4a713-b7ae-3c4c-99d0-6d5185a1cd58 | -14.44048 | -53.39302 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3663414a-740d-310b-b275-4bf34d5ddb1b | -11.36361 | -43.5907 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 922e07d0-b72e-3d35-bb0a-34620ab926f1 | -13.09606 | -57.12305 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da937fd3-7c8a-3e26-89b9-ef4da7a23b46 | -11.8179 | -46.44473 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cbaa9e42-50a0-35b8-923f-3a1036203253 | -9.448 | -62.34082 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068d0911-ea2f-32d8-9573-1319aed2a9df | -11.91698 | -46.40406 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a511fa93-d05a-3d56-92e9-b80c7df66e10 | -13.34488 | -46.97644 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a5626ac-8abb-3eda-8848-2211e4d58c14 | -11.21561 | -55.06351 | 2025-08-31 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2e282c3-b91c-3be3-94d0-74fef62b79d7 | -9.93689 | -51.61444 | 2025-08-31 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed9f842a-3cf4-3b4c-8030-f2a6da2e4930 | -9.66927 | -63.17019 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1096ee72-3389-3701-8d26-745786043d14 | -13.50941 | -46.9744 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9a5307a-2048-3a5d-a65f-db0469be039a | -12.79988 | -48.09344 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7433a609-d8c1-3192-8e88-2dc6486cb7c8 | -7.0966 | -63.1417 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0e4f7e0-2a6e-32e5-849b-4bae0cdf6f06 | -8.64156 | -62.82989 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7759436-d948-3366-9211-7a859d66997b | -14.53603 | -51.97895 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c083ffbc-ad34-3a5f-8fee-7edc3f2c73b0 | -9.43633 | -62.34552 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6db3a528-8e19-3711-8b3e-c2a666a55e73 | -14.62608 | -48.06051 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03ff7420-77a9-3a25-9a04-22a32364c881 | -11.81016 | -46.44102 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6a9f29ea-6968-3237-8fb9-acce09a79fa9 | -11.68611 | -51.68461 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b81d47c-4471-3fca-a2ce-fc025713ed41 | -12.93417 | -56.98686 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d8d3aa4-a8bc-30d2-9f14-104de6f4d37e | -7.71286 | -50.28062 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6d872b2-6a66-3734-b654-eab3c9fa4106 | -8.85669 | -45.73055 | 2025-08-31 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d1c11d5-cf8e-3fa4-abed-742291673dba | -7.45844 | -49.59924 | 2025-08-31 04:51:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01ccd7cf-513a-3988-a37f-d593464ee5c9 | -15.67294 | -43.22618 | 2025-08-31 04:51:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1197d2c4-f7d6-3d32-801c-241dcc9531fb | -9.44497 | -60.56684 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ecc3214-3bba-386c-8bcd-1fa9ffcb5722 | -11.0077 | -46.84282 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 510eaa24-8582-3465-a8bf-fcf1b3804da4 | -11.07936 | -44.62866 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15dbdf6d-03fb-376b-9fb7-6aec68e1d884 | -7.71931 | -50.30992 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0eaa737-5671-3894-ba2a-fdad65706ebb | -11.55823 | -47.61847 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe961bfc-c325-39ba-8945-27781f0e18aa | -11.8919 | -46.36914 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| beefcb21-5d1f-3264-beea-057967a27f20 | -13.46693 | -46.97205 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c1ded50-bcd4-30f1-8b00-2fb6dbd58dbf | -11.35261 | -43.63345 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README62.md)
