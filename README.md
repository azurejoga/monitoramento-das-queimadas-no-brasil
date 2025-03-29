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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8965a8f6-b00d-3d48-99a2-c4f4c1750f45 | 2.5625 | -60.318 | 2025-03-29 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bc803d57-6093-3b13-a0d9-dc710d367b45 | 2.2333 | -60.7018 | 2025-03-29 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bbde7b0f-ebd5-35f3-b677-3e4d7c661c70 | 2.0138 | -61.0826 | 2025-03-29 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b8aa2dbb-f3f6-301f-ae55-bab2c00edf61 | 2.0138 | -61.1015 | 2025-03-29 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ac9e12b3-3735-34a5-b153-ddc6b7b288a9 | 1.9956 | -61.0828 | 2025-03-29 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c9465ba9-e35b-3d49-a0b7-b2c146fcfde3 | -20.5862 | -56.0392 | 2025-03-29 00:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 34636ab6-20eb-32e6-a419-dbb37a136d42 | -8.14006 | -43.14712 | 2025-03-29 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| defdc7b8-db24-307b-8a9b-b25f001efd83 | -8.12849 | -43.14859 | 2025-03-29 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 8e615d5b-1b3b-307b-82b4-c28d7faeb572 | -9.93294 | -37.19962 | 2025-03-29 00:03:00 | TERRA_M-M | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c0263f86-3991-3e45-811c-0e20883780ee | -9.09268 | -37.31343 | 2025-03-29 00:03:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4d17e174-e83e-30d5-80aa-b82e1fbfd58e | -10.63083 | -39.83947 | 2025-03-29 00:03:00 | TERRA_M-M | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2a11709e-ce9d-3e9c-beae-46528068bd56 | -12.26685 | -39.41172 | 2025-03-29 00:03:00 | TERRA_M-M | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5efc72b9-45d3-343c-8201-22e18b5daefd | -11.47012 | -37.92378 | 2025-03-29 00:03:00 | TERRA_M-M | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 332df64a-1458-3b1b-a1b5-6b629591e5e9 | -9.42493 | -37.0566 | 2025-03-29 00:03:00 | TERRA_M-M | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a29000f7-eec5-36e9-a3eb-bc39e9b22abc | -9.42366 | -37.04759 | 2025-03-29 00:03:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 14359a52-924e-3d5b-822b-769e668240dd | -20.5862 | -56.0392 | 2025-03-29 00:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 4a71c8bd-74e3-3d95-8101-e936e8f3c5cc | 1.9956 | -61.0828 | 2025-03-29 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6b8b2c36-5148-3f7d-8e8d-ce7abd61fc3b | -18.0482 | -52.8719 | 2025-03-29 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1f3cb567-7652-364b-94ce-550f98aecd98 | -18.0279 | -52.8966 | 2025-03-29 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0dce0f9d-5505-3609-832e-b56d734c3703 | 2.0138 | -61.0826 | 2025-03-29 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 9cd2f0d1-ccd5-3658-9640-d61d3912bfd1 | -18.0283 | -52.875 | 2025-03-29 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3c505353-10d9-35ad-8f50-76cb643f7027 | 2.0138 | -61.1015 | 2025-03-29 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e219ee5e-9033-3ac6-bd0e-b0fb6e29a881 | 2.0138 | -61.0826 | 2025-03-29 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 390350b3-e4e2-3cb8-af8c-a7ec05d6a301 | -18.0283 | -52.875 | 2025-03-29 00:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| be1eeb55-3609-3033-9034-b9f0c0cde384 | 1.9956 | -61.0828 | 2025-03-29 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5915449a-efa4-3b3f-b411-8df37c9fbf8a | -18.0279 | -52.8966 | 2025-03-29 00:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| dd1e7433-a77f-3726-9fcd-67eeaf938c69 | 2.0138 | -61.1015 | 2025-03-29 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 839fb928-5eec-38ad-86f9-085d153fa604 | -18.0482 | -52.8719 | 2025-03-29 00:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 58c41fc2-b6a3-3237-bef5-dc9630e6bae6 | -20.5862 | -56.0392 | 2025-03-29 00:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 469fdc7e-9e5d-3c67-85c4-a63072df4429 | -20.5862 | -56.0392 | 2025-03-29 00:30:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b2ae749e-8cdc-364e-a5b3-f9d1d6a980a0 | 1.9956 | -61.0828 | 2025-03-29 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b4b285e0-f65f-3747-91d2-8ec528a5701b | 2.0138 | -61.0826 | 2025-03-29 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4756a9bd-e28e-36a9-8937-13d22118ebda | 2.0138 | -61.1015 | 2025-03-29 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fdc93873-8f74-3526-98cb-1a966758a913 | -18.0283 | -52.875 | 2025-03-29 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a91a7400-ddd0-34fd-ab65-18a0bbd4331a | -20.5862 | -56.0392 | 2025-03-29 00:40:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c9fc5878-884a-38f3-86b8-633d9466e612 | -18.0283 | -52.875 | 2025-03-29 00:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ab68dbd9-2fbd-3d26-b8d7-c5843b569f28 | -18.0279 | -52.8966 | 2025-03-29 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b29db436-26ee-3003-8757-53ab7ad0e7b0 | -18.0283 | -52.875 | 2025-03-29 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fe51b5fd-7809-37d0-86d7-c7fc933d1834 | -20.5862 | -56.0392 | 2025-03-29 00:50:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2a905a2c-54b1-3245-91cc-27c081e7fa28 | -20.5862 | -56.0392 | 2025-03-29 01:00:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| db818be5-0a1c-32cc-9646-4a6e344ea44f | -18.0283 | -52.875 | 2025-03-29 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 35378b5f-d498-3dbe-bad7-f755e205bcdb | -18.0279 | -52.8966 | 2025-03-29 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ca638ffe-9369-3be3-9da9-51a3c09cf97d | -20.5862 | -56.0392 | 2025-03-29 01:20:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5dee3977-2f1b-3a69-87f6-47ac69002bc4 | -20.5862 | -56.0392 | 2025-03-29 01:30:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ce9088e4-e0f1-34ed-b448-77f1213aa0d5 | -20.58628 | -56.0401 | 2025-03-29 01:39:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 48625dcc-1384-3461-893c-53cf0a1ec76f | -21.46049 | -57.16418 | 2025-03-29 01:39:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b74efba7-0b5c-30d6-8ff5-c99a3ae7b191 | -21.46367 | -57.15731 | 2025-03-29 01:39:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a9831876-870c-3183-ade8-ccd5c717db29 | -20.57598 | -56.04213 | 2025-03-29 01:39:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 48.7 |
| fc34e877-3664-33ad-bc63-7535ed6a2dc8 | -21.45881 | -57.15318 | 2025-03-29 01:39:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53a07b0b-ecee-3af6-9232-c2c5d2777a19 | -18.02094 | -52.8731 | 2025-03-29 01:39:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 60b72d5e-e211-3164-b29b-d3f52b448e2a | -18.02529 | -52.89712 | 2025-03-29 01:39:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 49015010-30ec-360b-8103-e07ad7830d55 | -18.53484 | -56.18517 | 2025-03-29 01:39:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 30a9032e-950d-3066-9d0c-aae1bde5e063 | -20.5862 | -56.0392 | 2025-03-29 01:40:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| df4b8262-4588-38d6-b62d-10b9450fc640 | -9.92974 | -59.90604 | 2025-03-29 01:41:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7e05f6c-6331-3cd1-a665-fff0aed22138 | -9.26203 | -60.31679 | 2025-03-29 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e260b196-20c1-3c45-baf3-3444aa7d50cf | 0.82582 | -60.58199 | 2025-03-29 01:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 70f4cf0f-a54c-3f85-aa33-6908f1726abf | 2.24095 | -60.71165 | 2025-03-29 01:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9e017e7c-dab3-33e2-b437-18242cc2a1c9 | 2.24458 | -60.71805 | 2025-03-29 01:45:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4910fb28-a79a-38c5-8738-d665c8fc9417 | 1.58126 | -60.67071 | 2025-03-29 01:45:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 13b9eb61-56b3-3c6d-9dc9-0afc8e685f70 | 0.82403 | -60.59489 | 2025-03-29 01:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a9079fa3-1b29-398a-b4d5-22286a35624d | 2.57334 | -60.31884 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2658fb69-2b84-30f6-8682-064f90f2d223 | 2.57083 | -60.32657 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a7ca7c3f-87e0-3887-a8d4-a34e55a5755f | 3.04366 | -60.80927 | 2025-03-29 01:47:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 86eb855e-865b-39cc-a120-0ea51a91be5e | 3.35854 | -59.94869 | 2025-03-29 01:47:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 31141c2a-3e14-35d3-9941-b939484a3daf | 2.57283 | -60.31234 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 28e28e90-9be3-38c6-92c8-d2d5827a843a | 2.73239 | -60.4046 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 886bf736-57aa-3bb0-870b-89424ecef898 | 2.73437 | -60.3904 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 31d37223-a8e7-3be1-a8da-915058d41850 | 3.35832 | -60.01917 | 2025-03-29 01:47:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 08a916c3-0569-33fb-952a-cb0a1691ac31 | 3.36663 | -59.95642 | 2025-03-29 01:47:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae28b110-a37f-301d-b186-2f75084c8a06 | 2.73513 | -60.39707 | 2025-03-29 01:47:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 25.7 |
| c08d858b-2a66-361d-94e2-f81ede37dfd2 | 3.35625 | -60.03476 | 2025-03-29 01:47:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0c1bc2ae-238b-3169-a743-45a87a1344ba | -20.5862 | -56.0392 | 2025-03-29 01:50:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2adb219e-3313-38a1-af1b-b5e9e1d36412 | -20.5862 | -56.0392 | 2025-03-29 02:10:00 | GOES-16 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 743683d2-c8e1-3f83-9c85-887746461bf3 | 2.0138 | -61.0826 | 2025-03-29 02:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9a46ca3f-9c00-3c23-81a3-ef69029319cf | -7.00727 | -34.97857 | 2025-03-29 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 85e21632-79b2-33d5-92a4-6850782c7ac2 | -7.00832 | -34.97301 | 2025-03-29 02:51:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d1519e07-daa1-3b33-923f-a31e68c80cdf | -8.38944 | -35.0255 | 2025-03-29 03:13:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ca0f7734-5a0a-3e42-8963-0404f55a610a | -8.38864 | -35.02473 | 2025-03-29 03:13:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 42a999e2-1e96-3cf4-9e3e-4984ccc13923 | -8.1336 | -43.14906 | 2025-03-29 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cd3b224c-eaf2-3c17-ada6-0fcbbb3e7bbc | -8.12647 | -43.14755 | 2025-03-29 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8572caef-fbb5-3b17-9621-3d8c67a66101 | -13.95759 | -38.95556 | 2025-03-29 03:15:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44170277-60d8-3c1c-9e71-a14aab1da4c1 | -13.95655 | -38.95703 | 2025-03-29 03:15:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a8a93e8c-46a9-3401-955f-00af62fb6fc7 | -13.95703 | -38.95855 | 2025-03-29 03:15:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3ecabbe8-1a86-319e-a8bb-3addbe2b12e7 | -11.65197 | -43.07652 | 2025-03-29 03:15:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 722c119d-4b1a-3b5d-a923-9dbf2e95a6e6 | -8.13495 | -43.14214 | 2025-03-29 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d7906a2c-4479-3b04-be54-7659a86f3264 | -11.47216 | -37.92451 | 2025-03-29 03:15:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d320289e-0343-3790-863c-558ef6d07d62 | -22.77801 | -43.04424 | 2025-03-29 03:19:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2ed7e704-67fa-304d-acb0-c0e570725c0f | -6.00164 | -44.61644 | 2025-03-29 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55bc2525-8f28-38c2-92ad-54b70604c33e | -10.63084 | -39.83836 | 2025-03-29 04:08:00 | NOAA-21 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 892b455c-66a9-3552-8b33-d37694957568 | -11.822 | -38.47762 | 2025-03-29 04:08:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42a4d5a5-5350-34cd-a434-703e85ba4018 | -8.14032 | -43.1442 | 2025-03-29 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0b26efab-248c-3abe-88cd-239e5a359d06 | -10.19863 | -36.18853 | 2025-03-29 04:08:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 74392d66-a3bc-39e7-a24c-011fa261e86e | -5.79159 | -43.61972 | 2025-03-29 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ded4b69-0873-37e9-bf99-826d6334df32 | -5.79505 | -43.62028 | 2025-03-29 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e103d011-ca62-3846-842e-f9380647aaca | -7.8524 | -39.7523 | 2025-03-29 04:08:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1f94b3a-c686-3a4a-a7f3-792645c2e27a | -11.18919 | -40.51159 | 2025-03-29 04:08:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e77ba3a-3481-3a08-a2a4-d1ab74fe3f3d | -12.86323 | -38.36628 | 2025-03-29 04:08:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 651bb9f2-060a-38e9-af7f-8c022d9ffff4 | -9.93309 | -37.19426 | 2025-03-29 04:08:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a1aafdc-45af-3795-a1bb-1232771b574b | -5.99803 | -44.61586 | 2025-03-29 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76ad3247-88eb-3d3c-8b5f-5bd93c218fa1 | -8.13361 | -43.14313 | 2025-03-29 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README2.md)
