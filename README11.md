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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ff8aadb-debc-3e18-970c-47a22b00225c | -13.06546 | -53.35539 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b84d7ad-8754-3cb6-b57c-d33e23ca42c6 | -13.07058 | -53.35638 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa3dc994-da29-3d0f-9a2e-3639afcb5e0b | -13.06675 | -53.36026 | 2026-06-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 649af15a-fbaf-36e6-ae09-294c7b35fad0 | -13.87068 | -47.1428 | 2026-06-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57c45e0f-ed86-3282-ad80-4d409d2d0dab | -14.31917 | -42.40709 | 2026-06-25 04:17:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1fb18040-8870-3ff9-b395-12a3b6f10d03 | -10.35751 | -50.10848 | 2026-06-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 875842ea-032c-390b-b35e-7429354f898d | -11.88482 | -51.7612 | 2026-06-25 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| d68fd6f0-aaa4-3d3a-a472-f146177715d1 | -10.36922 | -47.34435 | 2026-06-25 04:17:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69e9bd5c-2831-331e-bff6-1647d945f3a4 | -10.77432 | -54.10855 | 2026-06-25 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eec7e744-3ded-3747-93f7-472bac32451c | -10.59541 | -47.1088 | 2026-06-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1713c5d6-aa3b-3740-9551-349ec34ca287 | -14.26929 | -52.04542 | 2026-06-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19358549-cd8b-3e29-b5ce-10c0e683b97e | -12.43298 | -43.77594 | 2026-06-25 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 711e46ca-131d-3392-bddf-6b0cb72cf9c5 | -12.84301 | -44.35781 | 2026-06-25 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cecfc491-b099-347e-be53-8998333def3d | -19.53183 | -42.59131 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7143afdb-290f-32fc-a0b1-90855896f10f | -19.52456 | -42.5904 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 0bf2cdaa-3663-3e80-8df8-f9b436898457 | -18.5248 | -47.24327 | 2026-06-25 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdf349f8-fcbb-36b7-9c87-8152f65b2488 | -18.52144 | -47.24267 | 2026-06-25 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa8ca567-25e7-3280-9dcf-5b10ebbab259 | -19.52819 | -42.5909 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7748c321-23cd-3302-b88e-d000b0d2cc86 | -19.52699 | -42.59965 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1273e8f8-7a10-39c0-94f7-4361b79470f0 | -19.53121 | -42.59584 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 702c0ddd-c686-3014-8802-f9679c8bc440 | -19.52756 | -42.59545 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d919794-f656-396c-aaa9-516cc4eb6166 | -19.52393 | -42.59499 | 2026-06-25 04:19:00 | NOAA-21 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b0b3e4bb-5f16-3daf-a289-eb28aa163967 | -18.46065 | -47.25501 | 2026-06-25 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87c0f583-bfdd-3656-9ea2-cea4511a13d4 | -7.7498 | -44.6184 | 2026-06-25 04:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a285bd89-6173-3a8e-a754-58cad51c383f | -12.7373 | -44.4521 | 2026-06-25 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| aa974990-6af0-3399-816a-6260ed71ebf5 | -11.8868 | -51.7452 | 2026-06-25 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 06a78446-78f4-3c05-97f8-a2235a4bc77a | -11.8865 | -51.7663 | 2026-06-25 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 8794400d-d50e-3701-bd41-9024918f3f62 | -11.8678 | -51.7473 | 2026-06-25 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 701aa349-e286-30db-ae14-951d5ba76f09 | -11.8868 | -51.7452 | 2026-06-25 04:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 123bbacf-8285-3986-a21a-e8f1c27b4f8e | -11.8678 | -51.7473 | 2026-06-25 04:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fb7a0eb6-1746-39d7-b028-f2ee25625435 | -11.8675 | -51.7684 | 2026-06-25 04:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b7f6c81f-4c43-3ffb-be2c-49ac3eb3accf | -11.8865 | -51.7663 | 2026-06-25 04:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 14ac120a-2da0-327f-bffe-f7c0b634fd4d | -7.7498 | -44.6184 | 2026-06-25 04:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b5e8ce45-89ba-3276-8105-f9269150c05e | -12.7373 | -44.4521 | 2026-06-25 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3229ec7d-68be-3efd-946b-327ed12f1d82 | -11.8675 | -51.7684 | 2026-06-25 04:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 35c99786-3b28-3edb-b8a7-40d7c20b81ec | -12.7373 | -44.4521 | 2026-06-25 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 98dfa42f-29d0-3e53-8605-6adb462ea4e3 | -11.8678 | -51.7473 | 2026-06-25 04:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 6ff7ff6f-b176-33e9-9cf8-caa9df8a2346 | -11.8868 | -51.7452 | 2026-06-25 04:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 0b1599a1-ac6c-38ce-a4e7-a10bf6b98b59 | -11.8865 | -51.7663 | 2026-06-25 04:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 119e89b0-802e-326a-860e-1362e405b7c0 | -7.7498 | -44.6184 | 2026-06-25 04:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3b0fbc9d-3d85-3782-8821-0b153cd25dc3 | -5.7868 | -45.04472 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d90bd985-a099-3aaa-8f71-0e53bbfa330f | -5.78709 | -45.04295 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fddd92b0-1b2a-3eb6-9c0b-67423b04edc2 | -5.78752 | -45.0398 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd1c1e55-4e47-3cf3-8d57-a2da7072991a | -5.82093 | -43.59475 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c1698ab-ee6d-3cc6-965d-653ef54f9736 | -4.66167 | -43.22186 | 2026-06-25 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bce1d38-6f02-3fb6-9bd7-646135602fbd | -5.8081 | -45.06304 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8b3ad0e-7606-358a-91fb-635131b728e5 | -5.80883 | -45.05808 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f5d0a7a-2c01-379f-83ac-b74c73b15a88 | -5.81031 | -45.04808 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63b99a3d-1b14-3a6c-aa3a-844271ebb89d | -3.56237 | -43.20359 | 2026-06-25 04:46:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c5e06db-bf59-3064-a466-f9b6cdbd6c52 | -5.82151 | -43.59079 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42d289fa-5238-36e8-9648-12abd80399b6 | -5.80737 | -45.06796 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29d1ccd8-39ea-3be7-b402-aabecee28710 | -5.04534 | -43.26508 | 2026-06-25 04:46:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e258eb74-7ffc-3c98-bb7c-6cf8edbe4209 | -5.755 | -43.19211 | 2026-06-25 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76bd2a47-ae07-36b6-931e-2f868ba29508 | -5.8172 | -43.59014 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 46c4a09d-2b8d-399d-b2b9-67d200cbb18a | -5.90248 | -43.85932 | 2026-06-25 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44548bd4-a673-3216-afe3-4acadeb746ce | -5.82209 | -43.5868 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7eb85685-bbe8-3680-a88d-2754b80f91d1 | -5.79783 | -43.63284 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 410c84b8-5975-37f9-a4be-89485fac3f2d | -5.81778 | -43.58614 | 2026-06-25 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9dfe9c3-1984-304d-b7be-c44aa84fbeca | -5.754 | -43.18961 | 2026-06-25 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be6b912f-edc4-38bc-831f-7a8094fb2120 | -4.6626 | -43.22036 | 2026-06-25 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40fbda31-74e4-3372-94ae-7e05be73919a | -5.80957 | -45.0531 | 2026-06-25 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1a0a4db-b548-3dad-b707-e270104cb154 | -5.81413 | -43.79019 | 2026-06-25 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6f29b8e-7783-35dd-8b28-a271722640d9 | -4.66665 | -43.21836 | 2026-06-25 04:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9529217a-dc41-3452-bba0-7f384d30c7bc | -5.90305 | -43.85541 | 2026-06-25 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64d70aa2-46fe-3f1d-92ea-5d8a9ee8c2af | -5.75059 | -43.19139 | 2026-06-25 04:46:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e79d1b5-5117-354a-b9e2-9178f218a97d | -9.45931 | -49.83368 | 2026-06-25 04:49:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c20722be-7442-3de7-8314-6b755647d1fd | -11.09941 | -49.45459 | 2026-06-25 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a51e5c91-adfc-3d03-8daa-f10f7a908fda | -6.97631 | -42.89221 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c4659b6e-7ea2-345d-842a-fddbb502bec7 | -11.3632 | -55.81899 | 2026-06-25 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4ca45f-81dd-3eb4-9d35-2c0143f7e698 | -12.84413 | -44.35693 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b75e36e-de87-3fc1-9e70-534b4aa9500f | -6.98057 | -42.89148 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d7928a57-5f4b-3427-b76c-280d83e4deeb | -10.73628 | -47.26157 | 2026-06-25 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e73b1d0-5e37-3298-a159-fb1d987dd26c | -8.67984 | -47.86377 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ebcccfbf-ae37-3c5c-b41a-ac7320bad99c | -11.90398 | -56.8679 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1352a76b-ec4e-30d5-bba8-1b265f0d48a1 | -6.97598 | -42.89077 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6ba0c145-bb3d-3d5d-a3bc-587c3e2213c5 | -7.75107 | -44.62619 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efbc2b73-c58c-3017-94be-1c9567a28e36 | -7.74025 | -44.17408 | 2026-06-25 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a88c8eee-7ce8-3b70-9694-840249f35bd1 | -10.80254 | -48.56454 | 2026-06-25 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c3f6d7a-bd1c-3837-b765-a39070c3eded | -9.19234 | -45.32141 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6dc897f-9bdd-304e-b9ff-e95e14264e91 | -12.83507 | -44.35563 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be434101-9fb3-3003-b1aa-95bef6ba1be7 | -6.98161 | -42.88815 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b365977c-78bc-311f-8596-0e11b3cb7126 | -10.12521 | -52.11319 | 2026-06-25 04:49:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ece071b7-2315-31e0-9a95-936caa1c97bb | -8.57565 | -46.90743 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 338a5719-eac9-34f1-9791-2cef8b106f5a | -9.20883 | -45.32722 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30233720-67bc-30e7-9137-8880b350264e | -9.36745 | -50.54426 | 2026-06-25 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82d37722-a872-3fae-b0b7-2fb5a16da48b | -11.53959 | -52.77761 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7fa0c11-7a7a-3af3-8f79-1d4dcd2fb902 | -8.32323 | -47.12832 | 2026-06-25 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f54faaa-8b12-37e4-9cce-55a97d5833a0 | -12.74782 | -44.46016 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 27354f50-4ff3-3724-bf89-ac8eb8c6102c | -11.90473 | -56.8638 | 2026-06-25 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aa53702-460a-318d-a7ab-3720d1103960 | -11.57495 | -54.71326 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3131b7a5-542c-3be0-9619-e6b38417fb50 | -11.8768 | -51.75763 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ffe95962-f3c9-3e2e-a4c9-ebb57a7edebf | -9.97741 | -47.73522 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d279c0d7-952b-3d56-9180-fd26914b5644 | -9.57722 | -49.12323 | 2026-06-25 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 548fa8da-ae08-3a42-b907-6cab98638f3b | -7.75162 | -44.62247 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7fe54c9-64f6-3ed2-9443-75f0ef55a95e | -11.6376 | -52.86032 | 2026-06-25 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d88821bb-1237-3de2-9e93-57c2424e3ea7 | -7.75686 | -44.61551 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f191fbd-2716-3cbd-b24e-68e11462d20a | -12.13944 | -48.26062 | 2026-06-25 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38b6faca-d2ce-34fb-b5ab-fc1a50899b6b | -7.00127 | -42.77759 | 2026-06-25 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c360f9df-5bba-3a52-93da-afcd83f3e706 | -7.76099 | -44.61619 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92fbbf7b-5771-329b-9160-c8d3ed4782d0 | -6.98584 | -42.88739 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |


[Clique aqui para ver as próximas entradas](README12.md)
