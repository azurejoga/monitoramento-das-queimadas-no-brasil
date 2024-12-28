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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013cf9a6-11fe-39ab-a36c-0eece657bf2e | -3.80764 | -46.72127 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4a55cbeb-30fc-3439-8697-306c905f5892 | -3.7488 | -47.20132 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| de862e64-85ae-3bad-b4d6-fc9f638100f1 | -1.34282 | -47.00076 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ef09f215-8e3d-3c19-b730-6f13d4f87035 | -3.88485 | -46.69231 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 678c0aa4-37f2-33dc-860c-2b8cade325c2 | -3.19594 | -46.13566 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 08052c87-c0ea-3b93-a829-2dc83f1bb1db | -4.12148 | -46.71928 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 37574748-aa10-3297-9cc4-58843ffb47ff | -4.03633 | -47.04773 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 8dfc2b52-fc8a-36ac-a9e1-50331fd892d2 | -3.09185 | -46.5761 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 339ab0f1-2c5d-3926-a0ac-74ba1272ad97 | -2.62908 | -46.10851 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1218519f-0cde-3164-9999-2cbc61011602 | -2.17224 | -45.40752 | 2024-12-28 00:28:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ce591ab-1d9c-3c50-a762-1e2d35ca34fd | -2.44304 | -47.48468 | 2024-12-28 00:28:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 19c933e0-c273-3735-bfe1-0eb948fb94fb | -4.08094 | -47.10426 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5d18d8db-feea-3a08-bfae-8bdf5212a396 | -3.68635 | -47.17456 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1abec44f-0ea3-30ed-b73c-da22866393a9 | -3.53044 | -42.59961 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 50bfc2a5-1c0d-30dd-a374-3a77ddb9a745 | -4.56572 | -45.99505 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3355544a-4446-3aa7-8dd9-936c559c18fe | -4.12683 | -46.67948 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 917c2552-801a-39ca-9951-a59201d83af8 | -3.91876 | -46.65609 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 79643600-e26a-3d16-a9d0-a1ceb981d6bd | -3.9127 | -46.66327 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ac75b2b-eb8b-3b35-a07d-1416d7a14383 | -2.29278 | -45.57396 | 2024-12-28 00:28:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a9c7933a-93d6-3445-b064-ed5fab9cf9f7 | -3.45298 | -42.23893 | 2024-12-28 00:28:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9ad88c5f-4dd5-30c6-8ab1-ecf853280b7e | -4.5642 | -45.98364 | 2024-12-28 00:28:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 22b20781-e5bb-3d8d-b25e-bdfc9b7ebfc6 | -3.92535 | -46.98809 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7e1b5fe0-956a-3444-9293-17e60165c061 | -3.94491 | -49.44558 | 2024-12-28 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| b7f612dd-497c-3be5-88e3-8cd8725af784 | -4.01818 | -46.7133 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5845c758-c22d-350f-9546-b7a261486597 | -3.20753 | -45.9976 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0f70da24-d363-3a21-87f6-da49d0648c5b | -2.86759 | -46.72334 | 2024-12-28 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9d2a6d34-bb0b-3afd-932a-c3754849bdcb | -2.10792 | -45.74381 | 2024-12-28 00:28:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa2958f8-5a38-3016-9136-70465bfd5a86 | -4.11025 | -42.45643 | 2024-12-28 00:28:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 08dcafbe-7747-3c92-8b83-a535cab43a54 | -3.19918 | -46.01003 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9433a568-9749-3650-b609-fc2998fe1a9e | -4.24388 | -45.4302 | 2024-12-28 00:28:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b7f6aa99-572c-3a68-bb39-200f7b9a6cfb | -2.04887 | -46.56514 | 2024-12-28 00:28:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| caa25387-129e-326b-9f70-070f54d012cf | -3.74549 | -47.3418 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a92baaaa-adea-3b80-976b-06815e5e7ccf | -3.93602 | -46.9866 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 75b709be-9269-3e4a-ada8-11e00ff4bfe6 | -2.51669 | -51.86345 | 2024-12-28 00:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| adc18892-eb56-3b9e-a16f-b2c7486e7b67 | -3.80938 | -46.73388 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5fa160ce-45bf-3c9d-a1d9-938753b58545 | -4.04708 | -47.04631 | 2024-12-28 00:28:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 3b5881b0-28de-3464-9e96-598be8f3dcea | -3.96556 | -46.68812 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c1544673-c66f-3f2f-a8c0-d653cb196f8d | -3.90575 | -46.92395 | 2024-12-28 00:28:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 71388985-6a39-3950-bb1a-df5136eb9cd0 | -3.73454 | -47.34324 | 2024-12-28 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bd94fe87-e4ef-3946-b057-71f07d360de5 | -3.19619 | -45.98795 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| bb5137e5-2832-330f-964d-a228ed4e3d73 | -4.11636 | -46.68087 | 2024-12-28 00:28:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb1da318-e508-353c-8e4a-de2cb26aff9a | -2.12029 | -45.51701 | 2024-12-28 00:28:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46e78045-32fe-3824-9771-a707be582ed6 | -3.18443 | -46.1316 | 2024-12-28 00:28:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 284322b5-9364-3db2-9e6d-7a9894118798 | -1.99416 | -45.58793 | 2024-12-28 00:28:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1f81f44-f836-30ce-b5db-b1a1e78ce24a | -3.71923 | -41.70558 | 2024-12-28 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 696a0aef-76c6-3d0d-bcb9-7023fa737fa4 | -15.2921 | -59.870201 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0d61d81-0edf-318e-8ea2-86f76807dfa6 | -15.1072 | -59.620602 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0f6407-90bc-369f-9d7a-62f95e6ffc09 | -16.118601 | -60.062698 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6eb4af-ea4f-3beb-ae56-48db50619ecc | -15.2823 | -59.872299 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a03a83d4-496a-366c-ac0e-f3820972721b | -16.110701 | -60.074402 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06b1c4a5-3dfa-3dda-9cd7-f521f9810d13 | -16.120501 | -60.0723 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5adab8f4-3dd1-3d76-803e-6f7f2f249be6 | -9.2679 | -60.311401 | 2024-12-28 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 042ead1c-fb59-3c62-b6b1-dff208b7fc02 | -15.1091 | -59.629398 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db024d85-c1e4-3907-b420-0725bddd5184 | -15.5356 | -59.4179 | 2024-12-28 01:16:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31552c3a-0954-352f-9169-db74c95d5670 | -15.1054 | -59.611801 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46eeec5a-318a-361c-9d55-9f5a6f63a425 | -16.108801 | -60.0648 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7148ef9-12b8-3c44-af33-43cc489a46bb | -15.5338 | -59.409199 | 2024-12-28 01:16:00 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59fac840-6b54-334e-9bdb-bf572d1c6d06 | -9.2697 | -60.3195 | 2024-12-28 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cff900b6-8bf4-3333-a453-6223fa606727 | -15.5004 | -60.037201 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edc7c70f-f60b-3f3c-9339-628f7bec4bac | -15.294 | -59.879299 | 2024-12-28 01:16:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83117bab-c590-3993-b156-e3f598597ba6 | -3.1348 | -54.501701 | 2024-12-28 01:18:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73e99adb-e1e2-30dd-ab0a-aeac0e8195a6 | -2.5305 | -51.850601 | 2024-12-28 01:18:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fefd864-db08-3c02-8504-e9d2843d2bbe | 3.3234 | -60.430698 | 2024-12-28 01:18:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a1ca4977-2d81-38f0-a864-05451d0aa5ed | -2.916 | -54.491299 | 2024-12-28 01:18:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1720aec-ff34-3732-b361-9f5a83c2f3a9 | -12.28251 | -64.27638 | 2024-12-28 02:04:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f0aabd0-3bdb-360e-b774-bbf26f84d9d4 | -15.09709 | -59.62888 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 70e596c2-0ff2-3ade-a03f-0eb4e5d6ed9f | -15.09064 | -59.63654 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1b957fdf-bbd3-3f80-912d-e45d0af3bbd6 | -16.10535 | -60.07187 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 2972f05f-6d60-3135-a9cb-0345bcd4fe98 | -16.0942 | -60.0738 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 51db7062-ba89-3874-a262-e920a25946ed | -15.08793 | -59.61969 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f97f804c-9c43-3a58-9050-2116e8adab51 | -15.27811 | -59.87692 | 2024-12-28 02:04:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e5a5e6d2-b8d2-3d52-9aa2-1c91fa82f839 | -9.97081 | -64.79613 | 2024-12-28 02:04:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 59452cf2-89bd-3841-9274-82e52376f289 | -6.80762 | -35.30307 | 2024-12-28 02:57:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 28e5e716-f149-3352-8189-0784f7703195 | -6.68093 | -35.13962 | 2024-12-28 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1d09ef76-3f79-3327-bd7f-0b1d16558c0f | -6.67848 | -35.14192 | 2024-12-28 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 887ef81b-b0c2-39e5-bce8-9e42ea294622 | -6.6793 | -35.13734 | 2024-12-28 02:57:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f0a28df0-ff76-3b7a-ae91-822c31dc74ad | -6.80842 | -35.29873 | 2024-12-28 02:57:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0bfe2b01-c269-3748-a710-4fde1328d1cc | -10.25401 | -36.3074 | 2024-12-28 03:00:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 872d4edc-23e2-3751-9778-7dc57be85e63 | -10.25313 | -36.31192 | 2024-12-28 03:00:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7f7dadd8-fdf0-374b-a60b-c155e7dd1b01 | -10.25916 | -36.31314 | 2024-12-28 03:00:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5365cef4-343d-3d92-a15f-0ca490456a7a | -3.7075 | -41.69949 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d68a9578-c8ba-357d-8e81-344015d69b9a | -5.46777 | -39.55418 | 2024-12-28 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a6e2619-2891-3d66-a459-f841d73ae38d | -5.21139 | -41.24452 | 2024-12-28 03:19:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55018b8c-e528-3aa4-9a47-73efe882b70d | -3.71261 | -41.69743 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 06adcbbb-d41a-36d8-bcdd-995b789f70e9 | -5.76458 | -35.56798 | 2024-12-28 03:19:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad30b975-0f0a-3213-9ed9-1f9c331167f1 | -3.71898 | -41.69859 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b609d5dd-d08d-3a53-83e4-4a1e57cbc6a8 | -5.76398 | -35.57163 | 2024-12-28 03:19:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e9eb2ad3-8d0c-3f67-b56a-2d0a8cbaeaf7 | -5.99679 | -35.27747 | 2024-12-28 03:19:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d88be7f-b9d6-3e14-ad21-e3160cebb3ea | -5.58624 | -39.53514 | 2024-12-28 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8a1369d-9438-3d11-b05f-dce0bf3aa8d7 | -3.07134 | -41.90421 | 2024-12-28 03:19:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 294b5723-fad6-313d-8722-73aec623848b | -3.7181 | -41.70388 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a4d1a300-8ad6-3d1f-b81b-ce7f483bd781 | -4.77934 | -38.55488 | 2024-12-28 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1bb408c7-55ec-34e1-8175-b54db6e650cf | -5.5418 | -35.73242 | 2024-12-28 03:19:00 | NOAA-20 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60196d3c-efe9-34a8-a6b3-56ceb92a662c | -3.7139 | -41.70046 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| bd6dcf45-9557-3c36-9280-3e9f4524341e | -3.71171 | -41.70277 | 2024-12-28 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8f4d6330-f5ec-37de-a24d-fd7aa8d7bf01 | -5.4672 | -39.55758 | 2024-12-28 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 94b62715-e4a1-3a89-a92f-26e95fd18e48 | -4.77421 | -38.55403 | 2024-12-28 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc90acb6-50a6-36b3-ace3-b1a554d0afee | -3.07227 | -41.89874 | 2024-12-28 03:19:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c10948e5-d936-36c0-9f04-5c8837d2202b | -5.46911 | -39.55595 | 2024-12-28 03:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0d4ac8e-36bd-3f70-b656-57b810635d34 | -5.00931 | -41.92776 | 2024-12-28 03:19:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README6.md)
