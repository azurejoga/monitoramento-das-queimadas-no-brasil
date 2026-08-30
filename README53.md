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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d223bd-3975-3796-80ce-12af21eea51e | -6.84239 | -59.46273 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4e645a1-5f7d-36cf-929c-f93cd52becd1 | -9.19692 | -59.36708 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a4418c-f150-357c-a81f-ed69625fa5ef | -6.77207 | -55.67147 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07bfee29-6d32-3d06-a105-e0490bf710fe | -7.59049 | -61.35086 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ed870db-ea53-3d43-9445-26b00addcb67 | -8.22486 | -61.42465 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f010dcc9-eb50-3313-9401-7e84a52e7876 | -6.90999 | -59.48759 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d75bad54-79c1-3db6-9139-5205eab60f5b | -6.7764 | -55.66771 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e63110e-0aa5-314a-b5c5-268c1a510419 | -5.88248 | -57.78352 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be9c0469-d6a2-3f60-afd7-91142f7959bd | -6.17985 | -57.77061 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5331255-157b-3b54-b4c8-9765d6b65768 | -5.87408 | -57.77126 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b01e2e80-4ec5-3199-b01d-2995db01cc3b | -9.89507 | -60.2753 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3e3f4aa3-f7a6-37e0-b1dd-d6e21192a94c | -7.55421 | -61.31441 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b894f418-e001-3016-a498-7f2aa047f7e0 | -10.75341 | -54.06018 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6637f0aa-c9cb-349a-93bc-57db985b0832 | -7.24601 | -60.63213 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e6438fa-d327-3fe5-931a-c7af1dc6fea5 | -6.48537 | -55.88803 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12dd3c05-12af-3c4c-8983-3f22d9872bb8 | -11.29123 | -54.03557 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e52d62f-ec80-3d8a-aa27-8a88390c9446 | -8.555 | -54.71665 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18c9bb7d-e8a1-3567-b468-11ec7f0aa284 | -6.76944 | -60.01474 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ecd668-4464-3822-a8bf-9720e2ed876c | -8.56666 | -55.29427 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f36e0d4-1b45-377b-8c67-4b0e06afbe13 | -8.94469 | -62.3763 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e73e61f4-b304-38b6-b5d1-abf6565be168 | -11.79989 | -51.03638 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 034feeba-5926-3ae4-aa33-357173a822e4 | -9.1516 | -59.50623 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5435fdf5-9c13-3261-a405-b8984847f6eb | -8.91929 | -66.95374 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f81a856a-693a-3a55-bb2b-62cabd503131 | -7.39992 | -60.58665 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d33489df-7bdd-3119-a7ff-26301b513f9f | -7.30378 | -60.61556 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb045f36-f785-3430-8dc5-69f0b6460234 | -5.97831 | -57.68903 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 338fceb6-1270-3a39-a7c9-255b0a2473fe | -8.9524 | -62.37347 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bbfe3bb-7219-3356-94b0-69c819e74cc0 | -7.30771 | -60.61251 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b9039c2-ec25-346a-8953-82dfed224817 | -7.69602 | -61.1542 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2d5e3cb-f349-347d-ae1f-fa036bd75018 | -7.55899 | -61.41511 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4421df4-4c05-3114-9958-60b136c365b8 | -6.93879 | -58.95353 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54eea9d-d1ab-3fb1-9b1c-57a79919ebaf | -8.62875 | -66.53999 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ce53cb7-1ef0-322e-b835-26b91c6b6160 | -9.17507 | -59.61686 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0088d402-a696-3fed-a65f-30b49369669a | -7.51189 | -55.28139 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5505cb20-4b8f-3df9-bc45-504d96679cc6 | -7.29313 | -60.61755 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f09a5bc8-5a03-35ab-aa92-70f874915bbd | -8.49934 | -55.29879 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cf9a5f1-7f2d-35d8-b2f6-2f45edf6ee05 | -11.04236 | -57.22669 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae67f8ad-5182-335e-8636-403f94f95cc2 | -10.94412 | -51.41619 | 2026-08-30 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80f68347-bb93-360b-96e7-1859eb50cb3d | -8.18211 | -54.9357 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bc9254e-494a-369b-993f-30baf2e26039 | -5.97159 | -57.68799 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f3f0d55-7521-35db-81cd-635d3721fbb3 | -7.30941 | -60.60176 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92a6121e-e41b-3b17-a57e-65d0bfbf8592 | -9.06855 | -60.49059 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adfb8d12-6d32-3b4f-8d60-5509fb5a8423 | -10.00941 | -46.3971 | 2026-08-30 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7be13821-f284-3a76-83bb-d3073f54b621 | -6.78651 | -55.67172 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 934f2b4c-a5d2-3faa-9aff-f4c496cf90fc | -7.05452 | -55.6816 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d46828fb-9045-315b-a993-c956bae99e26 | -9.14104 | -61.1017 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1903815-9b52-3ab9-b35d-1d31129d03a2 | -6.7223 | -60.01089 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b4b6c39-2764-399b-8380-d69e6ca4be52 | -6.88893 | -59.44891 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454b62a9-e63f-3048-8bf3-4aa971fed13c | -8.6537 | -62.8434 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 042a3abc-b4ed-37fa-8e5b-776efce2d884 | -6.77511 | -55.67627 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dca0585f-6940-3b3b-81fa-c68885ed30ec | -6.87509 | -56.5735 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8579ff1c-e24b-3cd2-bdd7-078450786d99 | -9.41523 | -56.98264 | 2026-08-30 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a28f7b1-c014-37c9-9580-a9d16439e79b | -7.30662 | -60.59764 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e81fb3b2-014f-3ab4-8056-80bd4df3b8bc | -5.96824 | -57.68746 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b27c376b-b067-3939-8cca-8efa758435f4 | -9.15492 | -59.50678 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4fc95cc-b34a-3827-b782-6f70a227add8 | -10.83998 | -50.49355 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d9575be-d04f-3e5f-a547-95af1d8660b2 | -6.93872 | -55.70633 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 526b179e-24b2-3e2c-a5e2-27499be3b10d | -8.9155 | -66.94801 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 507068bf-4a60-3b97-9fde-59800e0e0a19 | -5.4899 | -57.14509 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4a0fc979-ba28-36f7-b8b0-41244ccf9a22 | -6.52863 | -51.43639 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8505d6d7-6038-37c2-8ec3-c30ca91faae0 | -11.7937 | -51.04248 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c969555c-24eb-30ac-acb7-2b57ec373952 | -7.33013 | -60.60136 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8499bb1a-18df-3878-9b96-26e6277c4367 | -6.62971 | -53.17849 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56a0bb86-b893-3a75-a9e8-f1932b0ca3ae | -10.76853 | -54.04559 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef96ab5b-e2dc-3f9d-a43c-afcc3ff2bcd1 | -6.77234 | -55.64468 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6b3b58a-cffe-3351-9413-0bf11e74d548 | -8.60966 | -54.77874 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 104ea898-f9bb-3bb8-af64-04b3276be6f2 | -9.93761 | -60.52277 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53f45417-ad4e-396f-8702-0076d5fa7665 | -6.54638 | -55.10984 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b3b4298-2c0c-385e-b763-325cce953676 | -11.24203 | -54.00698 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8ca36316-855f-357a-984b-8693901d7bd2 | -5.81116 | -57.6524 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5b036cb-fcfb-3637-8086-2ce9c75ddf87 | -6.75326 | -58.72548 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad949a76-ac33-3243-b9e4-20781aa96681 | -9.39754 | -51.6516 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b038a61-8a63-341f-9be3-05ad22be5939 | -6.85678 | -58.97977 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 380243b2-29ef-34b7-bf54-764ce691489f | -8.95906 | -62.39918 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b9ded5c-5f21-3685-9e3e-7d5558ec75c4 | -11.24725 | -53.98853 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84dce22-b401-30f9-9856-8d93d2332b94 | -11.16391 | -51.29127 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cc1a061f-3e43-34ab-b3b6-b562e9054698 | -6.18257 | -57.75278 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f69e7e9b-e4f1-3c0d-b4c5-b5acca4e07c5 | -11.16478 | -51.29201 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 142c615a-961a-3393-bb95-c1c4051c2ccc | -11.82129 | -51.03927 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ca75bde-661a-3d0f-ba7e-b5b6309cb913 | -11.19438 | -55.10804 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13d32b0d-37de-3504-b59e-8fca59d8497c | -6.86422 | -59.47689 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a90aece9-de11-3ab5-bac9-c5741058813f | -7.39714 | -60.58252 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b3730ad-3c97-34c0-bc70-c9d835498d4a | -9.16316 | -59.49739 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1b1611-54a6-324f-af0f-9945326f0033 | -8.7393 | -69.56995 | 2026-08-30 05:18:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df76b1b0-5273-3680-b033-8f96e6297221 | -10.94123 | -51.41524 | 2026-08-30 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68eacec8-46bf-3577-a059-36cbc902361b | -5.48484 | -57.15557 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d2a722f-bd97-38a3-a87e-56154995f112 | -5.4789 | -57.14389 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9f5c8d87-1df5-3676-ba2e-a45232023c0c | -8.61421 | -54.6902 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d3bc83a-fea6-3092-9f47-056b849f586d | -5.48173 | -57.14806 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 053ea30a-2a87-3384-827b-942a34ad600d | -7.25945 | -60.63431 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04ab1b80-4257-3965-ab1e-c55e7ead5628 | -9.87391 | -60.30011 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53cf9888-b5b4-3cdf-a4f5-03479a021a54 | -9.40126 | -51.65238 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a57931ac-8733-308f-8e15-3ecda1073a84 | -8.9571 | -62.41116 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3785ad2d-370e-34e6-b6d6-654e322c5310 | -6.15427 | -57.80318 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10f08194-99c3-38a5-8445-5c21b4bc0737 | -7.23649 | -60.62695 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dcd7e48-df67-3487-8817-6dc35f624b87 | -6.72446 | -59.43377 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01cc121-8c1d-3cf7-b507-2ff8a11408c6 | -9.88785 | -64.98615 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fda5a72a-b5db-3346-a536-2cbfb6ec69b8 | -11.19035 | -55.10746 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef599c44-b82d-36d8-a6b9-c92556252a6f | -6.86157 | -59.42678 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b44348f-9a54-3d23-962d-39913a4c8403 | -9.70913 | -60.7424 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README54.md)
