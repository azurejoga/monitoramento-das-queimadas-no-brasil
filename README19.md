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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e9682f5-8e74-3a2e-abd0-efe41ac60839 | -5.64879 | -46.97652 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 843433bb-26da-3b43-bf50-d8404b0b4ea8 | -5.64719 | -46.97496 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bdc81900-f212-37d8-82c3-16bce2986e1f | -5.64629 | -46.98009 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed3aa27c-d261-3801-a9ba-08f6b5ff46ba | -5.64244 | -46.97534 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a21cc8d9-b29a-3c04-a17f-2a352545484f | -5.63992 | -46.979 | 2024-10-24 03:40:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3814c078-4ca6-3b83-b148-53469ea7a4bd | -5.62207 | -44.83212 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a4aa6062-435a-32ab-a167-1079c87e7b98 | -5.62143 | -44.83577 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eb768574-17fa-33b6-a2db-9c9f69744dc0 | -5.61651 | -44.83115 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c6c80999-d6b9-3b4d-b519-fab2ceb29542 | -5.61586 | -44.83482 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d7faf49a-e96c-31db-bffe-0ca3b5ec991f | -5.60729 | -44.88332 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eaa7287a-97a0-3a2d-9adf-4a415ee4a4a3 | -5.60239 | -44.87854 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2aea399c-e061-394a-a184-4595fa5e658c | -5.60172 | -44.88229 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 752b6ee0-00cb-3900-8d1c-09c6f38e1b9e | -5.59619 | -44.88103 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff4abae-70d8-361c-979e-4fe9454609eb | -5.58468 | -44.89148 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bcb5e69-1a6e-398c-884e-cde06becec30 | -5.58304 | -44.89025 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63b447a8-1b09-389e-8148-7766365c2355 | -5.58235 | -44.89412 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| da1d3369-be47-33a1-9e31-445be75664e9 | -5.58044 | -44.8826 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 99197d6f-b9a1-3b91-83a7-074a3b1addc8 | -5.57978 | -44.88646 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0480bee4-b636-34f7-bcc4-9fe3347a1178 | -5.57912 | -44.89037 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 74e5f819-090e-3618-b3d6-d4f7fae8886c | -5.57887 | -44.8814 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d14e45b-d857-38ac-a727-0883f8db2416 | -5.57844 | -44.8943 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f27a5b4-1357-3284-a1e4-ba51e07d9ab2 | -5.57818 | -44.88525 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fa681bbf-e690-3b18-9c52-82724f8206a9 | -5.57749 | -44.88913 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 77a6dd84-02c0-3992-a954-051ea74cb72b | -5.57679 | -44.89304 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f053323d-ae71-3d12-8b5f-e0efe2bff29c | -5.57355 | -44.88925 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06995eaf-0dc4-3ad6-a667-7ee1aa2eba0c | -5.57289 | -44.89314 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bcf8a19b-a5d2-37ea-9050-cd5c77ea6159 | -5.57192 | -44.88805 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52a266e6-d89d-374e-b8f2-539a375f04b1 | -5.44636 | -47.68692 | 2024-10-24 03:40:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84c190fb-8331-3dc1-9d1b-b00199e8537f | -5.44069 | -47.68027 | 2024-10-24 03:40:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ff8615b9-fa09-3c7e-8fec-4da00d0378ad | -5.43964 | -47.68607 | 2024-10-24 03:40:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 72b0389b-0d58-3be5-9f1e-7601e16bfe5c | -5.42791 | -46.56455 | 2024-10-24 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6110ff11-8f0f-331e-b31d-5ace648c48a3 | -5.42704 | -46.56939 | 2024-10-24 03:40:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c966a71-5b38-3a03-b3a8-55cbdc8fef7d | -5.42429 | -44.79749 | 2024-10-24 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d285e43d-29cb-328a-8921-cf38f13e2cbc | -5.30234 | -47.00652 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52c0d431-44e5-39f1-befe-e4d30246711d | -5.30152 | -47.0036 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 86cf9926-9335-3d63-bcde-5e2ec46e5b76 | -5.30136 | -47.01185 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffdc37e3-0c5f-382d-bef1-bcb85207a2d9 | -5.30059 | -47.00892 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ec89da70-2375-3317-aa8e-4a97cd2cd50f | -5.29585 | -47.00585 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aedfb625-6c47-3b37-a2d8-b99acdadc80a | -5.29489 | -47.01109 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00c4d448-3e44-3759-be0f-c2ad7c03c506 | -5.29411 | -47.00814 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1674661a-fa8d-3340-8c41-647a5e0fd709 | -5.2939 | -47.01645 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3f64d40-bde2-3318-b20e-6d5297aede2c | -5.29319 | -47.01342 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1352ca3-399a-3dad-9d46-bade86c32bca | -5.29223 | -47.01885 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96e89dc4-13ae-34e3-a288-9e7a2b775614 | -5.28845 | -47.0101 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b218b01c-cb7d-3c7a-828a-50bc41018fd3 | -5.28747 | -47.01547 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a0d3d97-cb62-3867-9319-538d2f239184 | -5.25599 | -44.00078 | 2024-10-24 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d2bd772-643c-3d16-a6d0-b1944850e94b | -5.22733 | -47.95793 | 2024-10-24 03:40:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 20206fa1-3623-38e1-b14b-47112f9b629d | -5.22702 | -46.16876 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85f3baa0-3711-3b8d-bc44-ebed41f57747 | -5.2269 | -46.17242 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 558328a6-0d6f-3afa-bd78-7a5eae2225c3 | -5.22618 | -46.17358 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25fc5a18-6460-30a2-a1ed-a5344345a0dc | -5.22598 | -47.95729 | 2024-10-24 03:40:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f242271a-686f-3d79-a208-16dd3bf3a5c5 | -5.22485 | -47.9636 | 2024-10-24 03:40:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 831e19df-7f20-3e86-8314-50ba3582b023 | -5.22092 | -46.1677 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e3213b4-14ca-376a-b2d6-4560c3933cf8 | -5.2201 | -46.17241 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2afc38f3-e03b-3abc-8dae-d7be57239c6c | -5.21255 | -45.9318 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f26ebe2a-2000-3005-987e-5047b8050f5e | -5.21173 | -45.9364 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26dfaca2-44cc-36a7-a294-ddd15e46c026 | -5.16865 | -44.00836 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d74b3906-fdc5-3028-b32a-faeb3ad707a6 | -5.16338 | -44.00726 | 2024-10-24 03:40:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa51747-c7b5-3e1e-8443-d177fdc58f11 | -4.96401 | -45.51586 | 2024-10-24 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1921ca9d-f945-39bf-aad6-302540942b9c | -4.96328 | -45.52002 | 2024-10-24 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2dae74d5-6689-37df-895c-41577168407e | -4.8745 | -48.21323 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8d1caae-ea44-3f59-9d2b-b680fcbead23 | -4.87414 | -48.21828 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ff8ad9a-1719-3e7f-9856-c5f3e278cd8a | -4.8732 | -48.22034 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b12e44f-ba21-3da4-997b-38f2c17a68c2 | -4.86723 | -48.21695 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b2f902b-0815-3d22-89f1-eef302e287a7 | -4.85036 | -45.03857 | 2024-10-24 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fca59fe-cb88-3e6c-a9f7-f35c7e8eb041 | -4.84573 | -45.8591 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac416475-41ce-3b5e-98d8-f4cc888817b5 | -4.84464 | -45.03764 | 2024-10-24 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d94f2894-3ac4-38c8-a676-318e97b9e90c | -4.84395 | -45.0416 | 2024-10-24 03:40:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c566f22d-0c69-3a76-b11c-ce0d78d2a598 | -4.80052 | -45.69474 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 719afc18-4f89-3def-8c9d-7a05ed4ef177 | -4.79973 | -45.6992 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d91aa4b-e42c-3303-9188-6f5ae7cb197a | -4.79809 | -45.69224 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1453b1f2-9f12-3359-bd61-3054a9880a76 | -4.79732 | -45.69678 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b702c4aa-21e1-39de-b1e4-949d8485fc79 | -4.79654 | -45.70134 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5940124b-4527-329b-9ee2-e7f6f07c163c | -4.79458 | -45.69358 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19b19603-b555-3299-a8c3-93d3f0f0858e | -4.79376 | -45.69818 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69128475-3681-3a1d-be02-3ecb7f5b2dcb | -4.79216 | -45.69105 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42c2f084-d808-36ef-9e73-03e9db0d5ecb | -4.79138 | -45.69564 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51b8c398-640f-3478-9f69-dbc4cc9c3cca | -4.78944 | -45.68797 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33fe37b6-f71b-35b7-97e6-932139e1b6d1 | -4.78864 | -45.69248 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 815517b3-0d68-38b1-932a-c943e76b94dc | -4.78782 | -45.69707 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c422ad4a-f2f8-348e-8a5d-210c067cf444 | -4.7862 | -45.69003 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47ce6f4c-82c9-32b9-b66a-ca725803ba92 | -4.78543 | -45.69456 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c7dedad-d8d4-3b73-9433-3bbcc4aefd55 | -4.78267 | -45.69156 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82147350-366a-3d84-8c46-363722de6b09 | -4.77041 | -46.4052 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 879f50b5-348b-3b53-baea-954830517ec6 | -4.76954 | -46.41024 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9770674-fba2-3116-9847-1ed867c96a9b | -4.76796 | -46.40802 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d378d03a-a949-3398-bcd3-e6b6a9d540a0 | -4.76746 | -45.76353 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 577ca110-8532-3e09-be31-9444e2f6660d | -4.7642 | -45.76032 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7337ab4-013c-3de5-95b5-658c834cc8d9 | -4.76416 | -46.40425 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9edf4aa-932d-3938-837a-999b722b5abf | -4.76342 | -45.76472 | 2024-10-24 03:40:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e44158a-54cc-36c6-be4f-e1b4beb0a998 | -4.76328 | -46.40932 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5039eeca-b7f3-3b24-94d5-ff7f77ee05f7 | -4.76171 | -46.4071 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ab704441-62b1-3b32-8e68-e7da6158ec82 | -4.76148 | -45.76245 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f85d0f33-5e89-368a-bd70-43ca8e46a535 | -4.76079 | -46.41216 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7a6f4cee-aeca-3201-a032-60534fb501b4 | -4.75704 | -46.40829 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2908bbbf-6fc4-3b40-9038-d282a0c6f49b | -4.75497 | -46.64585 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e431d6f4-2e91-382a-9510-c4f2e4271388 | -4.75411 | -46.65088 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db9b149b-bcc3-3f88-9f02-d20607da3e6b | -4.75092 | -46.6478 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 44caea26-8f79-36fa-82fa-d4d8dcac66b5 | -4.74923 | -46.62075 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31e65ba0-9cb6-3a7d-986c-712d379a8e6d | -4.74835 | -46.62571 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README20.md)
