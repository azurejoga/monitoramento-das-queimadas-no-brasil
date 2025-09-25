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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3e10269-688a-3cad-8608-32317b2079ae | -7.3755 | -44.4478 | 2025-09-25 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 56187a4d-357e-3d85-8433-5a1b4c7322dc | -11.4225 | -44.9794 | 2025-09-25 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 06095d1c-194f-3a78-a4ff-8f37ad9425cb | -5.7767 | -42.8902 | 2025-09-25 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 07423574-3163-3669-bdc0-c4854f8596ae | -9.771 | -45.9484 | 2025-09-25 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f7430c6f-3e85-398c-8bcd-f5c61c0d5298 | -15.822 | -59.5017 | 2025-09-25 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| a73f51a5-da2c-3a62-ba4e-1afe7ae02c77 | -8.6817 | -44.0121 | 2025-09-25 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f7c04d0d-5f11-300a-9140-2b0ef6160864 | -11.6622 | -44.4107 | 2025-09-25 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| e668d799-c626-3ee7-ac90-27023d6111ee | -8.7894 | -43.0631 | 2025-09-25 14:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 886ac360-e185-3ad0-92a6-9a6b82435e60 | -8.4987 | -44.9998 | 2025-09-25 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 22dd3883-fc14-3c61-a398-f214b37aabb9 | -4.7812 | -43.2188 | 2025-09-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f06d766f-c6c5-3488-b5be-230a49a86a02 | -15.8223 | -59.4817 | 2025-09-25 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c8b5cfa0-ea72-3692-a2e2-53efe2354d42 | -17.9506 | -55.8731 | 2025-09-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| a40665c6-3bd1-3bbf-a596-6ae9461b73af | -21.0131 | -50.0217 | 2025-09-25 14:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| 1956db34-ae15-3efe-a590-9bcb919ce246 | -8.6628 | -44.0142 | 2025-09-25 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| b4992719-9b50-3627-afb8-2e3052991153 | -17.9312 | -55.8548 | 2025-09-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 12957176-852e-3944-8de7-92ee99564a46 | -3.2116 | -43.3726 | 2025-09-25 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 1c89f695-8baa-3ad8-8422-5714de15b420 | -17.951 | -55.8522 | 2025-09-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| e8faa750-b276-31b8-b65d-e919a204078f | -15.8029 | -59.4835 | 2025-09-25 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 20e4e2ad-d419-3bac-ae15-3d6670edb032 | -11.6622 | -44.4107 | 2025-09-25 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 273.6 |
| 93d34a9c-1976-3c57-bfde-659139f025c6 | -8.8415 | -46.2095 | 2025-09-25 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 6bbbd6cf-46da-38a5-bad9-2789263403cb | -20.5441 | -57.1434 | 2025-09-25 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 16e8793b-8394-387b-b954-723a869e4c86 | -20.7135 | -57.8112 | 2025-09-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 91e1c510-8a83-3c3c-ace6-35ae37c3ce64 | -6.4129 | -43.0958 | 2025-09-25 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 93c8646f-f439-3dca-a401-549d1baa3b73 | -7.6141 | -46.6188 | 2025-09-25 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 8538d687-81c8-3547-8c7f-ce6a00b9bdf7 | -17.9506 | -55.8731 | 2025-09-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| ad1d8919-7d52-3941-8bd9-b9964ee90f1a | -5.3428 | -43.204 | 2025-09-25 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 82d1ff2f-7b52-3dbe-9e1f-aa5bdf6d52f6 | -15.2626 | -59.4339 | 2025-09-25 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 351d615c-cdca-355f-a24b-124363e46537 | -17.9308 | -55.8758 | 2025-09-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.0 |
| 2a6c64cb-18bc-3555-b060-96e70aebb2ec | -9.7851 | -46.2851 | 2025-09-25 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6076429e-c0b7-30e5-905e-888542a8d8e9 | -10.313 | -45.2219 | 2025-09-25 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 55a09292-1504-3954-be22-db86094a09a0 | -11.4674 | -43.5248 | 2025-09-25 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| c3e68389-208a-3123-8cf7-8b311bea5b6e | -20.5445 | -57.1224 | 2025-09-25 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9d731979-1494-3b6b-875e-d5fd6965c1ab | -8.1324 | -44.1417 | 2025-09-25 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 953d318e-b5b1-32f5-ad14-e8586c3af25e | -4.7974 | -43.5435 | 2025-09-25 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0f00612b-d543-33e7-8ed0-31a9361a965f | -5.7767 | -42.8902 | 2025-09-25 14:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 81b7027d-f67b-3671-ba13-f6fbcdc0d00b | -17.9312 | -55.8548 | 2025-09-25 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 30f8addf-5e10-301d-9cfd-724a504b9347 | -11.4866 | -43.5219 | 2025-09-25 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e2cdf901-94a0-3370-9407-e05f753fa471 | -8.7384 | -45.4299 | 2025-09-25 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d3db4294-c39a-33a5-8387-694399dd234e | -5.1972 | -42.6984 | 2025-09-25 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 2e136266-0b6a-3898-93ea-e146326b9a7b | -10.9381 | -44.2598 | 2025-09-25 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| dfd8f5e8-8123-3383-b110-5664c5a81e93 | -9.771 | -45.9484 | 2025-09-25 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |


