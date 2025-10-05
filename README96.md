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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4a8f24a-525c-3c30-a04d-a39d91234e3f | -13.23074 | -47.81955 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 404cd1e8-e43a-3bf8-b713-25e6eab8af2f | -9.5489 | -45.60946 | 2025-10-05 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80b20eb9-e961-3d56-bcc3-3d2cf5974f0c | -7.24508 | -44.88091 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe5c8de-ab00-33fe-b75c-2a8744bfbd84 | -12.38422 | -51.09269 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cacff37-6d73-30d1-876c-68ffbfb33589 | -8.57269 | -46.32901 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ccaef71a-3bab-3f7c-8d78-721a000aa6ff | -13.34444 | -47.59393 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df8e6609-f384-3cea-b8a6-d8142859f45b | -10.36078 | -43.73433 | 2025-10-05 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b1e6e99-1924-3a3c-8a86-c3e9de2a363e | -7.48058 | -43.02977 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4fa910a4-23f0-39f5-9564-ba973b1a0c50 | -13.51958 | -47.24104 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed2e2a3f-067c-32a1-9a49-1e53d25a9a84 | -12.90826 | -47.31226 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3be32074-70cc-3c1d-b363-b50f89ff9387 | -7.43934 | -46.52967 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e00b6467-f747-3a62-ba4e-fd71751c8c57 | -9.85264 | -52.22066 | 2025-10-05 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6560ed84-19b4-3ce3-920a-cad5d2a6b619 | -13.33143 | -47.78374 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b35012d-f596-38c8-8c4c-820516f671f2 | -8.85742 | -46.78547 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c4498d-0e4e-3307-9db9-ec2d94f9a5d5 | -13.2648 | -47.19479 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a71a16cd-4929-3e18-9e56-6068debc1650 | -12.93699 | -51.00968 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24faffb5-2b5b-3f8e-8137-29a2729c5c89 | -11.71443 | -45.34925 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3da73822-7084-370c-ae87-25890d84cdec | -7.01319 | -42.30068 | 2025-10-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fc9c0d20-5e7c-374e-afea-74c26368caa8 | -12.39373 | -51.0979 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f5ce5ab-1a37-3ec6-96ec-9059894ed72e | -12.42202 | -45.15191 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0fbe996-971c-3bdf-8ad6-b7ec7834e501 | -10.05013 | -49.20021 | 2025-10-05 04:46:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f932fba9-d118-32c2-8f08-5dfdc0a8dc8f | -13.45869 | -47.26461 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42a72b07-e014-3bcf-be16-597c1ce8f689 | -13.13945 | -47.96006 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5335b08-6d1c-31fb-bf59-9e696d2a4535 | -9.15157 | -59.53103 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40b6d2ad-26e7-3e4a-ae8a-1d78969db0b9 | -13.11861 | -44.07657 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d007749d-faf0-3f4a-9365-bdef5d418776 | -13.31565 | -47.78091 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea708bc-4738-3906-9abb-616b1d53b088 | -11.10754 | -47.87363 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32e0b208-47f9-371b-8f25-1eac7c6fd8d5 | -9.15263 | -50.06112 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63f41054-127b-3e19-9f82-9dfc98bddea3 | -7.46121 | -47.18554 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 860b3fa8-cffe-3978-8182-8c1cfb185881 | -8.58642 | -46.32008 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 740a859a-22a5-30b2-9814-75a44f0aef30 | -7.43528 | -46.96659 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46db1caf-30a1-3ad4-8fe0-52d1a9112f69 | -7.75402 | -42.60612 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 667872f7-822a-3272-a896-fbe6f014447c | -10.57157 | -48.68475 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e89584e-1b32-3d56-a1b5-20ba931ed658 | -8.89665 | -46.68179 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9da8bbcb-2639-3519-82b4-0db030f7b132 | -8.89679 | -46.04256 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 809a10c4-9086-3fbf-92bd-e7a6c03b7a76 | -13.43581 | -47.27931 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bf8c4cb-edf6-3b88-be0d-1fbfe160b822 | -10.45535 | -51.27777 | 2025-10-05 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55eebca8-8e29-3688-8e50-62bd4c77a1d1 | -6.39754 | -47.33334 | 2025-10-05 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5357922-b324-3393-91d7-9f50a5d1a9ca | -13.71689 | -47.34931 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fa601ae-6555-331b-b849-88e96a06f3c5 | -13.23683 | -48.48213 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 551035f5-bc65-3554-8462-54b35dff0974 | -9.41702 | -49.21913 | 2025-10-05 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10465ef6-0983-3f4a-846f-1ecc5aa476f6 | -10.8325 | -47.98487 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25cb9e85-a914-3e8b-9186-72e5e4e029e9 | -10.74389 | -46.61768 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e41b3d8-9f4b-3160-ad45-68d67359d34c | -12.87564 | -47.27776 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd6d2675-5a1f-37ad-b15b-8fd0297fcec8 | -7.17234 | -45.0759 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2940211-9c73-3864-9953-ac255cdf5cc8 | -10.83455 | -57.17278 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dc5bbca-ed98-3f2c-88f3-648f09e737bb | -7.45782 | -47.18317 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9561cbbd-610a-3f18-9b5e-5f0f3403cc18 | -9.91436 | -50.19492 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a88b4530-cbc9-3499-b632-7f4306ab7e9e | -12.97932 | -51.03835 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02252590-d002-32ac-85d9-53ac1270fca0 | -9.21744 | -62.47055 | 2025-10-05 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60a3a879-0f13-3f4a-a568-0c1dd226f2dd | -11.72179 | -51.46683 | 2025-10-05 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d88999ed-2ab0-34dc-b854-68dfc6310a45 | -13.43626 | -47.77777 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf47a36e-7497-3a6a-afe5-d0eb21fba1c9 | -13.10197 | -47.82706 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e73c864-d9e1-3402-bbbb-f7cd70a063cc | -13.32009 | -47.78554 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d75bbd39-52af-36e0-b6b8-d6a5a02ad7b7 | -10.41509 | -51.66942 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b590a3fb-3714-3aae-95a0-f9a598ee2a66 | -10.00806 | -48.29008 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6103ed1-1a38-34da-ad65-1c8f8d8f4fbc | -12.70398 | -45.85455 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 981f6d54-b18d-3332-a321-6f73ff5dba7a | -8.61853 | -54.96614 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcdc3413-a0b4-3665-bcaf-f5c96f1be119 | -12.87971 | -47.27832 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bb47251-6bf4-3e7e-b6b6-bf194c1b224a | -12.57879 | -48.15909 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dba7a262-c472-3c90-8973-9830c12a0753 | -8.85895 | -46.09962 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40b07d30-ad0c-36e8-9346-98d00cc0da2b | -8.95502 | -48.74943 | 2025-10-05 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022451ce-e6f1-35c3-9a22-5224edfec458 | -13.34896 | -47.57898 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bab2db73-994f-389e-ac71-4bc25a9e5141 | -13.28223 | -47.58831 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 710aba84-8ac3-3c98-abf7-26bd9b68becd | -8.57931 | -46.31149 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7b61d3f1-e9ce-3d0e-923d-49fd6f7f9d22 | -12.81903 | -46.85951 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe24ebdd-00a9-3556-b85a-67840a5351bc | -8.58849 | -46.30535 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 38439d86-0ce2-304d-83e8-60ef95e81e8a | -12.61118 | -48.12391 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 033156df-bec2-35b5-85ed-6da8168b775e | -8.55843 | -46.312 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de0d2ac0-551c-366b-aea8-8502b25e8d9a | -8.90115 | -46.67889 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9386ea63-6f0a-3868-9ffe-f24b37c0d066 | -9.20704 | -46.92069 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a0afc0e-567e-3935-8b61-9683d6d5d647 | -11.45975 | -51.51233 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff2e2042-8cda-3242-8305-2445b7a71b05 | -11.45866 | -51.51939 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93cb2604-71ea-350a-82ec-2195a6ef9585 | -9.91097 | -50.1944 | 2025-10-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61870f8f-a014-3be7-8ec3-38b833a82ef2 | -10.46251 | -57.51006 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b737f93f-d032-3ae7-b165-9287e5741a74 | -10.84317 | -47.1909 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beea18cf-d35f-3370-a4a5-13f96329afbc | -11.09697 | -49.85983 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b52bb6ec-1919-3fe8-9f37-9f74d69f8a89 | -9.98592 | -48.26654 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 330f0a47-160c-36fe-ad7d-7ec4dc04e8c0 | -13.10232 | -47.94012 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d537b874-1c8c-3cfa-9a5a-b7397ccb6056 | -13.25094 | -47.20429 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b61f6d80-ffd4-3975-8270-b2052c29502c | -7.31511 | -45.5568 | 2025-10-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afc447e2-755c-3850-aacc-9b653f9f3de4 | -10.19267 | -45.53284 | 2025-10-05 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9327c20-04ad-326c-8848-a82816b2bf90 | -11.00043 | -46.50991 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8202e00c-8cc5-3fa3-a23f-e71bfb546f2e | -11.83247 | -45.09074 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1100545-32ec-3000-9856-5b9357053a11 | -13.30586 | -47.56485 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55d1e5e7-ad24-3b39-80ff-4c1aff016866 | -8.95863 | -44.61032 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c4bfdc-7c04-3fa7-bff8-d51b97719b50 | -13.27893 | -47.61266 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38e31494-45a4-3438-b71c-115cd8b49ca8 | -11.63819 | -45.07588 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49378812-1e17-3d44-a800-c9083c43ee8c | -8.57981 | -46.33749 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0753084b-4d27-3936-b535-5d6db714e37b | -8.55635 | -46.26695 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8acdf11b-3c69-365b-913c-7d1bbe78a76e | -7.36655 | -49.60408 | 2025-10-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf8cee4-836f-3016-a76c-0792caf8cab2 | -11.80838 | -46.8524 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a62c85c6-ea3d-3957-8992-472517c940d9 | -11.81611 | -46.85724 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3d5cd15b-56a4-34f2-9d17-55044258f561 | -7.12232 | -44.17097 | 2025-10-05 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbfd2992-ff25-3516-a320-769f3f1b3514 | -11.11812 | -47.20702 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd0a04d8-eb16-30e3-9691-cf315aad4af0 | -11.95079 | -51.48104 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f32e6da-6c32-3bb9-a9dd-e128745f327c | -11.38962 | -50.83484 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce28ba6-0059-389d-be5f-ca869439a069 | -10.36454 | -48.28202 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0bb087e7-bf45-327a-a1cc-a351a41028b0 | -11.11069 | -47.8789 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e448d915-9d6d-3f0f-96aa-0ba74fd539a5 | -7.80064 | -44.5471 | 2025-10-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README97.md)
