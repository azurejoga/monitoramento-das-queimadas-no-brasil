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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3daff24c-d1bd-3ac1-93bb-bc512c9b3b51 | -17.8427 | -57.5636 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 1a50bf65-8e55-3af8-9582-614aff7613a3 | -17.843 | -57.5431 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 1612a0ea-70ae-369e-813c-f615306c5d07 | -17.8628 | -57.5407 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 64e4aac3-7bd8-360c-9798-f5f6e1ef3e22 | -17.8631 | -57.5201 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 46240dbf-fef8-38a9-b6ed-6c2153832999 | -17.8828 | -57.5177 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| f6ea18ac-fc6b-35f0-ba00-2c2eaccae3bd | -17.9217 | -57.554 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| fbf56504-c0e8-34e6-86ba-91fe5c52ecca | -17.922 | -57.5334 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 1daba175-8bc9-39c0-b0ee-91bb150e3678 | -17.9411 | -57.5722 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| d9b59f18-7e45-3ad2-80e5-b8d88f826eb7 | -17.9415 | -57.5516 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.9 |
| 56defb1f-db87-32ae-9675-22f034ce8f42 | -17.9418 | -57.531 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 984c152b-d293-3606-add8-8fb67b63af86 | -18.024 | -57.3357 | 2024-10-26 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| efe7180e-dc4a-34bf-b9eb-4d56627aae67 | -18.0851 | -57.2249 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| bf193f71-69d9-36f8-9ac5-c94a9277a966 | -18.0431 | -57.3745 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| f0491002-9183-37b5-954c-33ae5f4b8fe8 | -18.0629 | -57.3721 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| fe226cbf-3d27-32db-b307-09487a1d756b | -18.065 | -57.2481 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 105eff01-1fc0-3027-8642-4e7f0f1c8b47 | -18.0653 | -57.2274 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| b5848623-1d6e-3713-8eb9-caaddf89b950 | -18.0827 | -57.3696 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 850196ab-001d-3aea-8335-5740617aeeb8 | -18.0847 | -57.2456 | 2024-10-26 02:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 7eb50000-2534-3a60-8e4c-9a1d5cc537bb | -18.2649 | -55.9975 | 2024-10-26 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 1ffbb124-1184-3d10-9bfb-b6bcaed4d7a8 | -2.1929 | -53.7234 | 2024-10-26 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 75b8af79-f860-33d0-99bd-5a45c5230658 | -3.013 | -50.481 | 2024-10-26 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| afde5cb7-fd05-3d53-add8-f1f7bc2ad064 | -3.0129 | -50.502 | 2024-10-26 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 83e00a10-f864-3d1e-be3e-8b382e407482 | -2.9945 | -50.4816 | 2024-10-26 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| d04efd71-24bf-357f-9ce2-299ea90a4d47 | -2.9944 | -50.5025 | 2024-10-26 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 88029c62-289f-3fa4-96ac-5d602ba472f1 | -2.9501 | -52.5708 | 2024-10-26 02:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d9d1ca43-5ab7-378f-8bc2-a8dc1ae22742 | -2.9317 | -52.5713 | 2024-10-26 02:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4c96b6db-65c5-3100-9faa-0005b8f9d950 | -3.1116 | -53.7234 | 2024-10-26 02:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f0d2efbe-c3e7-33a9-aeae-6911413c31b5 | -3.4917 | -43.3136 | 2024-10-26 02:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9ba9cdff-d0d7-3bf4-ac3c-f62ca878d531 | -3.4915 | -43.3368 | 2024-10-26 02:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 37cd7ca9-7a70-3164-ac5d-4a0fa51e815b | -3.473 | -43.3144 | 2024-10-26 02:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7caa08bc-45fa-3933-81b7-17fbaa51bbba | -3.4729 | -43.3377 | 2024-10-26 02:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| b86f1c19-faf4-309c-89b7-1bd9af11b649 | -3.6084 | -45.8147 | 2024-10-26 02:25:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| eca73f82-08a4-3c00-9b8e-9d55d935169c | -4.58 | -48.0132 | 2024-10-26 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 209.6 |
| e283d428-aecf-3695-973e-33c040650bff | -4.5799 | -48.0349 | 2024-10-26 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 4220fccc-36cb-32d2-9d77-3a224ba27b49 | -4.5614 | -48.0141 | 2024-10-26 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2733321a-1419-3e2e-8ef5-756a5da60f81 | -4.5613 | -48.0358 | 2024-10-26 02:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 84d78548-1af7-395e-83b8-818a2ae5dd83 | -6.0931 | -47.225 | 2024-10-26 02:25:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6c820c9a-da52-3f83-ba23-c5d078f13e49 | -7.6474 | -63.4584 | 2024-10-26 02:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1c3b3339-dc42-3626-9e31-146a87099ddc | -16.9012 | -57.5108 | 2024-10-26 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 39a209c6-ecec-35a2-a58a-9d4596fb86d5 | -17.0499 | -53.452 | 2024-10-26 02:26:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 37f96185-db4d-37b3-871d-b0adc05b0b4b | -16.9207 | -57.5086 | 2024-10-26 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 9266dc71-50a8-3bd4-8e69-e9f38de3660b | -17.254 | -57.4903 | 2024-10-26 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 895b668c-c649-3c45-8cfe-43eefa527523 | -17.2537 | -57.5108 | 2024-10-26 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| aa675e7f-c454-3d70-82db-f60cf94a4abb | -17.8069 | -57.3419 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| a342cea3-b101-3fc5-b3e0-a1c0840ebd5a | -17.8066 | -57.3625 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| d3a69baf-7a49-357a-9d4a-9983be7ca6c5 | -17.7875 | -57.3237 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 56bf7b55-5472-330b-aeec-a7ca709cc81e | -17.7872 | -57.3443 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| f09b5309-ad5c-37ac-9464-5d12b241c0fd | -17.7868 | -57.3649 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| ce9e6445-7525-3c25-b821-facb70f07272 | -17.7674 | -57.3467 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 0b5f07b2-dc21-308a-b2bf-0a7c7e656f18 | -17.7647 | -57.5115 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 64b312f5-25bf-3425-a6d2-ddcf72f3bb72 | -17.7644 | -57.532 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 4a9c90a8-7843-397d-b5df-40320786f513 | -17.745 | -57.5138 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 630d6837-7b0a-39f6-8606-fb254a077b7a | -17.7446 | -57.5344 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 086a9b78-1fdc-309f-99cf-54c9c484e88a | -17.7443 | -57.555 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| e658be74-2a82-3792-bbc7-11c3022463db | -17.6865 | -57.4798 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| bb1b241a-5ced-35b0-b138-7c7dcc5166a6 | -17.6667 | -57.4822 | 2024-10-26 02:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 99e08521-97a4-3f5c-9ae9-91394ac3c7d5 | -17.9612 | -57.5492 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 1d14bfa0-e084-3554-bf78-90ba2fa6b0cf | -17.9418 | -57.531 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 66ed4c99-420a-3ad1-883b-7661e50aeae5 | -17.9415 | -57.5516 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.2 |
| acf35f93-9bdf-362d-8ec1-d260ff072627 | -17.9411 | -57.5722 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 1919062f-8bff-3f25-b6a3-edde7682c372 | -17.922 | -57.5334 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 594451f6-267e-3273-ab90-51ebcc74afd0 | -17.9217 | -57.554 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| a3108020-404f-3206-a514-95c12b99fa58 | -17.8828 | -57.5177 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| f7e5dc5b-8240-3e4d-a148-a1ff24df981e | -17.8631 | -57.5201 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| eb29d0db-2058-35cf-a2af-8273c33d03b1 | -17.8628 | -57.5407 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| ebf3b396-135a-3cc8-a9d8-9f2eeac000dc | -17.843 | -57.5431 | 2024-10-26 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| afdb0ccf-24f5-3767-a613-8d6627913236 | -18.1028 | -57.3465 | 2024-10-26 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 289b1f0a-0151-3381-b5a9-2d861d879b17 | -18.1025 | -57.3671 | 2024-10-26 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 933ed602-fa3d-3628-b9b8-a8981247625a | -18.083 | -57.3489 | 2024-10-26 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 4175b8f8-a413-31a9-ac18-7001b030fa16 | -18.0827 | -57.3696 | 2024-10-26 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| df50a8ee-2d2b-3722-ac6b-7e0ff96c8cde | -18.0629 | -57.3721 | 2024-10-26 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| bf7fc57e-df5b-3554-8bb8-520869ae7539 | -2.1929 | -53.7234 | 2024-10-26 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9062cbb1-ebf7-3da0-865a-4a29d6b1142b | -2.9317 | -52.5713 | 2024-10-26 02:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e0728cb3-6cd6-36bf-bbee-d9405f248ac5 | -2.9501 | -52.5708 | 2024-10-26 02:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 42baa974-6144-3878-8832-9056c89f3644 | -2.9944 | -50.5025 | 2024-10-26 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b33142dc-defd-3aff-a998-75ec9e6f70e5 | -2.9945 | -50.4816 | 2024-10-26 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 3e9bebb0-d9a4-33a2-af62-9afc102c2266 | -3.0129 | -50.502 | 2024-10-26 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8432cd1d-1d40-3279-acb7-fb326561127b | -3.013 | -50.481 | 2024-10-26 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 366627b1-6d2c-30c1-87c0-3e8ddb7f5f16 | -3.4729 | -43.3377 | 2024-10-26 02:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| ed9352ee-55e5-3b9d-a364-13170de444dc | -3.473 | -43.3144 | 2024-10-26 02:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 34ea848d-8d25-37b5-90d4-c09cf26724d6 | -3.4915 | -43.3368 | 2024-10-26 02:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0ffae8ea-ac31-38bb-8b3e-e886b5916723 | -3.4917 | -43.3136 | 2024-10-26 02:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fe1ce415-73a1-3680-bf38-f88f1818ed2d | -3.4211 | -54.5787 | 2024-10-26 02:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6f4a3b8c-8102-38cf-bcfe-a497c9b51070 | -3.6084 | -45.8147 | 2024-10-26 02:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d6ea3c2e-2f91-3d1d-a4df-eb2203d7f193 | -4.5613 | -48.0358 | 2024-10-26 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1cf78abf-f140-3d96-baee-d013f092bc2b | -4.5614 | -48.0141 | 2024-10-26 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ed17cb1f-7218-339d-96c6-44bb8850bc97 | -4.5799 | -48.0349 | 2024-10-26 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 244.0 |
| 84ad93a6-bc8b-361b-bd04-2b6966445988 | -4.58 | -48.0132 | 2024-10-26 02:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 176.2 |
| ac254a0a-32ce-3bf4-b4bb-2b67cf652bba | -7.629 | -63.459 | 2024-10-26 02:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 34a4e560-a7a7-31dc-a682-aeaa45346590 | -7.6474 | -63.4584 | 2024-10-26 02:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c4c9ac6d-9154-30ac-8c10-1139eb7de6b5 | -7.6475 | -63.4396 | 2024-10-26 02:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8dba3182-c337-3e72-861e-ad9879244045 | -17.0499 | -53.452 | 2024-10-26 02:36:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 9486dba8-892e-3ab0-bdfd-8088bcfb91ef | -17.2537 | -57.5108 | 2024-10-26 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 134e3c5d-4fac-3d9d-8139-1741c473b99a | -17.254 | -57.4903 | 2024-10-26 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| cf829497-b13f-368b-a28e-86dac1dd29d6 | -17.6865 | -57.4798 | 2024-10-26 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| afbe7e4c-d3c1-306d-9f74-71bc3948be28 | -17.7446 | -57.5344 | 2024-10-26 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| dbe83732-df19-3a7a-8f05-5fa66beb7684 | -17.745 | -57.5138 | 2024-10-26 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| ef1f56bb-2206-37ba-92d1-fe30f8a9a279 | -17.7644 | -57.532 | 2024-10-26 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 251a6030-90da-3512-93bf-107d0c9a2c04 | -17.7647 | -57.5115 | 2024-10-26 02:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 8ff1e042-ede8-3b3c-84fc-fcbad701be9c | -17.843 | -57.5431 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |


[Clique aqui para ver as próximas entradas](README23.md)
