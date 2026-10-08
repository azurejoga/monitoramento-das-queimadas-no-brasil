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

## Dados Diários - Página 209

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33596196-b53f-341b-8e90-198df4b3a38c | -7.88421 | -54.99693 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4a14b910-1f0e-3aa3-b34e-09937938cf6a | -3.30178 | -54.66504 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9752a21b-f199-3625-ad06-3dcea9225315 | -3.18441 | -58.64495 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 78fa13c0-37ab-3de3-a7b2-ae93738d00f3 | -9.73666 | -46.93331 | 2026-10-08 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3e01280e-ddd1-3ee8-9a44-fdf80cfc30d3 | -1.71428 | -55.43954 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ae1f91e4-cab6-3489-b5bd-a8a928ee55c7 | -6.05113 | -53.4803 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4c36bc41-2604-30a8-9185-e402dd37e15d | -9.9589 | -43.5516 | 2026-10-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| f575c1d0-0609-3e10-ab44-f7ff3d1a57bf | -8.6291 | -67.0296 | 2026-10-08 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5ef0f4bf-1e96-3336-b111-d847b5e15971 | -11.6186 | -43.6433 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 377.8 |
| 11b9484d-1363-3471-8fa7-ae2b78a2e52e | -10.4527 | -47.2801 | 2026-10-08 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c474e53a-05e5-3d2b-a611-27770c7458cf | -11.8485 | -48.0373 | 2026-10-08 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 26246b92-097b-32e4-afe2-0e50e95df65e | -11.6369 | -43.6876 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| fae43447-732f-3fe6-bccd-23f9771eef04 | -11.6177 | -43.6906 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d9bf603d-20b7-3fc4-8750-9ddd34d641c9 | -9.3736 | -45.9489 | 2026-10-08 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c2451410-d5e5-3414-9e57-64d1644cd905 | -9.9014 | -44.8147 | 2026-10-08 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| cb3db034-0da6-3347-bfa2-04da98fa1d7b | -11.6378 | -43.6403 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ace2744d-574c-3e3f-9490-8d08c23e97c2 | -11.6365 | -43.7113 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 2851b7fe-c71d-3e77-9013-3816c614da2f | -8.6107 | -67.0116 | 2026-10-08 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5bcbbe50-1900-33c5-9f7a-fa08d775e20d | -11.3176 | -46.6798 | 2026-10-08 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 851db093-d8c0-3fcc-9298-8b39464178b7 | -9.9398 | -43.5542 | 2026-10-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 437.5 |
| 7d662712-4c0c-31cd-b9f7-397cc3405a01 | -10.4337 | -47.2824 | 2026-10-08 12:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9d34ac86-bee0-36e9-aa64-92b369efdd5b | -11.619 | -43.6196 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 83ca8ef8-ef1e-3252-b0ea-0aa3eb5e7251 | -11.3367 | -46.6773 | 2026-10-08 12:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e5653a6c-82ea-3327-a440-063fa9c2cea2 | -11.6181 | -43.6669 | 2026-10-08 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 54a8e2d8-8f94-3dcf-8ad9-4f1c396d4646 | -8.6107 | -67.0301 | 2026-10-08 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| bd758d9a-5de8-3805-9a07-0b65b90ad69a | -12.29052 | -57.57341 | 2026-10-08 12:21:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 44c8773e-aaf7-30ea-9d4c-f655f18f7581 | -13.92726 | -51.34696 | 2026-10-08 12:21:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e5893ee2-6ad4-3c73-8cde-6407f4c6cf7f | -12.14457 | -57.2382 | 2026-10-08 12:21:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a2c9fc7c-906e-3427-9498-ed70b0bf0b66 | -13.17281 | -54.32969 | 2026-10-08 12:21:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 92cbec0a-b1cb-396b-898e-5117071adc81 | -12.46403 | -58.49427 | 2026-10-08 12:21:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e60afa4b-70fa-3faf-ad05-cd83cf596041 | -14.36964 | -55.02068 | 2026-10-08 12:21:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9b610bea-faef-3633-9199-d757edd3f537 | -14.67234 | -51.45446 | 2026-10-08 12:21:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 146eb2da-249d-3971-bf4d-f9fe8bca86c1 | -12.13699 | -54.67525 | 2026-10-08 12:21:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3d7d8727-5d49-32c1-ad6a-b371e0598c62 | -13.16419 | -54.31593 | 2026-10-08 12:21:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| be8dc110-e5dd-39ce-a90e-455ae9d3f1a2 | -19.13901 | -50.80855 | 2026-10-08 12:21:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 30.4 |
| d6a08ee2-85bc-3419-bbd7-9d5e4d16aae1 | -13.17439 | -54.31734 | 2026-10-08 12:21:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| fcd21f86-5028-3433-90b5-76fc6ad708cd | -12.88297 | -58.27641 | 2026-10-08 12:21:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2ba6e5c3-6306-3a48-abb0-bf6a33b5e721 | -13.22179 | -54.5027 | 2026-10-08 12:21:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2fa040e7-4cab-3886-a216-6366aebf9e2d | -10.62234 | -60.48845 | 2026-10-08 12:21:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 74cba8c9-ff81-3997-be26-4f33a59993e1 | -14.66998 | -51.46072 | 2026-10-08 12:21:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| c0fe97a1-fec6-32cd-abb1-6d92858bacff | -13.91657 | -51.33907 | 2026-10-08 12:21:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 26c21a66-e586-3c79-8270-d44e4a048a73 | -11.75597 | -61.05443 | 2026-10-08 12:21:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d5f38c6c-7e4f-348c-8b06-b61d045a1247 | -16.35121 | -55.32386 | 2026-10-08 12:21:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 20938fea-28d9-392f-8a08-22d7f4a4ade5 | -25.81598 | -53.43428 | 2026-10-08 12:23:00 | TERRA_M-T | SANTA IZABEL DO OESTE | PARANÁ | Brasil | 4123808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| a1ded6f4-7658-3a83-b651-f5d5b0e81abf | -19.97057 | -57.18382 | 2026-10-08 12:23:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f231e9f0-1df5-3de5-b092-ee1c621ffea7 | -25.02494 | -54.11421 | 2026-10-08 12:23:00 | TERRA_M-T | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 72d3d8d1-35b2-3b45-895c-4e0fecf02e8c | -25.57859 | -54.57214 | 2026-10-08 12:23:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 67300213-1b44-37cb-bc51-66bac57504fa | -11.6177 | -43.6906 | 2026-10-08 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| dd9bfd93-c98b-34d9-ab6e-6eaff266cd7f | -9.3736 | -45.9489 | 2026-10-08 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| ff03e3ce-f6c7-34b1-af20-dc89756392dd | -8.6107 | -67.0301 | 2026-10-08 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 9758f00a-1d66-3618-bf3a-c5743a87cc99 | -9.9398 | -43.5542 | 2026-10-08 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| ad84a137-e056-3d4d-8d0b-4044bf81d776 | -11.3103 | -44.8337 | 2026-10-08 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ccc8bd93-f989-3a35-b483-3f08620755a6 | -11.6186 | -43.6433 | 2026-10-08 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.3 |
| 91674b31-aa4f-3d3e-a506-1d19b5e3f077 | -8.6107 | -67.0116 | 2026-10-08 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 215e5d22-b276-356f-a69b-d0800f18a763 | -11.3937 | -46.6922 | 2026-10-08 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 998ffb81-77bd-30f9-955e-705c7008155d | -7.2185 | -55.1016 | 2026-10-08 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| bf123541-a721-3fb8-a836-408545bef957 | -11.6181 | -43.6669 | 2026-10-08 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 15fa4072-a28b-3c9f-b78a-3446d72a3698 | -11.2482 | -46.2604 | 2026-10-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 45f3ba44-8a82-3fcd-a513-2a4891f6273f | -10.4337 | -47.2824 | 2026-10-08 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| b2a4c59c-430c-3248-8921-8400a0da8ea0 | -11.6365 | -43.7113 | 2026-10-08 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 5901c1e7-d385-36ea-8092-ec28dddc2c84 | -11.2337 | -44.8446 | 2026-10-08 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| b5106f95-1654-3773-b3ae-a63c9a146918 | -11.2486 | -46.2377 | 2026-10-08 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 52701dfb-4c51-3826-8091-c99aaf14cb61 | -9.9014 | -44.8147 | 2026-10-08 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9d90f363-3704-397d-aa09-5792a52590ae | -8.6291 | -67.0296 | 2026-10-08 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6687557e-fc79-3580-95b8-9a4b669a0316 | -10.4527 | -47.2801 | 2026-10-08 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 2902328c-61fa-3051-b85b-040365d96d7e | -11.0953 | -44.0037 | 2026-10-08 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 97ec142b-0427-3164-9617-f6574ed3c37b | -9.1543 | -49.8142 | 2026-10-08 12:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9a93ea85-9bb8-3f7b-9af2-31cb875830fd | -11.6369 | -43.6876 | 2026-10-08 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 464a93cd-75e5-34d8-8174-b22acba5063c | -9.3739 | -45.9263 | 2026-10-08 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 877a9404-c100-38c8-98d5-ed9787594db2 | -8.6107 | -67.0301 | 2026-10-08 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| b7182519-6768-39ad-8546-079f445526da | -8.6291 | -67.0296 | 2026-10-08 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| af492327-d00b-3f44-bd4d-f8c000ff04f6 | -9.1543 | -49.8142 | 2026-10-08 12:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7db69a26-c4d3-341e-a4ae-2b0272f29bbf | -10.4527 | -47.2801 | 2026-10-08 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 603b7fb0-367f-347e-8c1d-6d3012e059f3 | -9.3736 | -45.9489 | 2026-10-08 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| bdeff6f0-1823-3ad4-814c-a11e9d7d39e7 | -9.9014 | -44.8147 | 2026-10-08 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| abc33439-0aaa-34a3-a18a-f1d861364a63 | -9.9398 | -43.5542 | 2026-10-08 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 526995a5-e45f-359e-bca1-64750bcae98a | -11.3367 | -46.6773 | 2026-10-08 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d6d91e99-788c-3bbf-b86d-40f1fa7029a7 | -9.8253 | -47.4629 | 2026-10-08 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8200c669-45be-30ee-929d-d451e53a64b8 | -11.3103 | -44.8337 | 2026-10-08 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| b57858bc-67c3-316c-8079-34f0172d5c64 | -14.6701 | -51.4643 | 2026-10-08 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 20b25d5b-0f27-349b-aa95-59f1ea9c3fe6 | -10.4337 | -47.2824 | 2026-10-08 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 179.6 |
| e7bc3b03-fd85-3fe9-908e-990c300dbc72 | -9.9018 | -44.7917 | 2026-10-08 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| fe20294a-a068-365e-b760-3b543edcd245 | -8.6107 | -67.0116 | 2026-10-08 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7fbba62b-ea9e-3efe-82a6-dd39adaf7047 | -8.6291 | -67.0296 | 2026-10-08 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| cea5bdcb-1990-3731-a830-54ac33e4e56e | -13.1833 | -54.3158 | 2026-10-08 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8a6907b9-69e2-315d-ad2b-ae46bf365f9d | -8.6838 | -45.2765 | 2026-10-08 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7e89dfc7-7b4e-3645-bcd9-503167acaa2b | -9.9018 | -44.7917 | 2026-10-08 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f452d0f6-4a94-3ff0-81c4-71575093a4aa | -8.6107 | -67.0301 | 2026-10-08 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.4 |
| eaf0432c-3a1c-362f-9aad-37815353b4d3 | -11.3367 | -46.6773 | 2026-10-08 12:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 220bf669-b0f9-38b3-932b-f6644a124d56 | -8.6107 | -67.0116 | 2026-10-08 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d65d5650-9f6f-321e-9d72-50431f23d236 | -9.9398 | -43.5542 | 2026-10-08 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f24eac88-c6b7-38d9-8619-9a3572b9777f | -9.9014 | -44.8147 | 2026-10-08 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c9445762-df0d-3fdb-8891-89c8cc12c1b3 | -11.3103 | -44.8337 | 2026-10-08 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| fd8ab5a4-232a-311d-93f5-133d0cff9e21 | -11.6181 | -43.6669 | 2026-10-08 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| aa5b6238-1f4f-34ff-813f-d1a9db54b345 | -11.6177 | -43.6906 | 2026-10-08 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| dadd728a-77ec-3033-ae69-f19c14573beb | -7.2185 | -55.1016 | 2026-10-08 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 379334d3-2073-3b0c-afc3-ed3b413c5527 | -10.4337 | -47.2824 | 2026-10-08 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 6eb5e0e7-6f00-3a47-826e-ac3a16596a28 | -11.6369 | -43.6876 | 2026-10-08 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 4cea04cf-57bf-381c-b986-b3195aac7114 | -10.4527 | -47.2801 | 2026-10-08 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 5d599602-7dd7-3346-8600-87fcff4fc606 | -13.1641 | -54.3178 | 2026-10-08 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |


[Clique aqui para ver as próximas entradas](README210.md)
