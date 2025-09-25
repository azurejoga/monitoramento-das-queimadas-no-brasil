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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed9529cd-497d-3595-af8a-232e535205c7 | -15.2819 | -59.4321 | 2025-09-25 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2552085f-771e-34fe-8b2d-9108d28ee73d | -20.5441 | -57.1434 | 2025-09-25 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2393746a-3ca6-3eac-a9bb-ae4f00f81729 | -11.6457 | -45.3388 | 2025-09-25 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 75e43a20-7600-324a-9ed5-be93051b59a1 | -4.8161 | -43.5423 | 2025-09-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 65f0e63c-8bcf-3588-9798-5106ed42c6f7 | -12.116 | -44.7606 | 2025-09-25 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 0dd7046b-12d1-3717-af58-a5217f26383b | -11.6622 | -44.4107 | 2025-09-25 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 66101ac3-1ef8-319f-afc9-a9aeec30aa9d | -8.6631 | -43.991 | 2025-09-25 14:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 17955861-0ff2-345e-9753-f269dcb8e70d | -11.6626 | -44.3873 | 2025-09-25 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| e707fe71-dfad-3e87-b951-faf6807970f9 | -17.9308 | -55.8758 | 2025-09-25 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.2 |
| ca8b8123-8a53-3211-bef0-9f679ed2236d | -4.7974 | -43.5435 | 2025-09-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f1b7070f-3502-3d38-8c5d-0289d9a78811 | -11.701 | -44.3815 | 2025-09-25 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| cd3eab20-63e1-322b-9878-6088aa90d560 | -6.4131 | -43.0724 | 2025-09-25 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c8f4a490-c615-3f65-afd8-1fb19b034dac | -6.4317 | -43.0942 | 2025-09-25 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 277f8d77-8ddf-3ab0-b875-9bb2324cd675 | -8.4987 | -44.9998 | 2025-09-25 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| be0746ec-af46-3a85-8834-5b0d685917ac | -11.6622 | -44.4107 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 340.2 |
| cecb0ced-0a13-3493-bd6a-d15abb05c513 | -17.9308 | -55.8758 | 2025-09-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.4 |
| 60aa1adb-4bb6-3d84-975a-b1511f093ec1 | -15.8029 | -59.4835 | 2025-09-25 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5e677f89-5651-38e7-b2fb-9750c519cd51 | -11.6626 | -44.3873 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 9a05c4c2-35e2-3887-9b80-aa544d93ecb0 | -6.4317 | -43.0942 | 2025-09-25 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9933ec06-4935-3794-9dd7-e0f21af24351 | -11.6262 | -45.3646 | 2025-09-25 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f0424005-fea9-3da6-977c-91c82849db79 | -11.6254 | -44.3229 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 107c1ebc-4dbf-3c36-bc32-c5596f39691d | -7.7692 | -46.1806 | 2025-09-25 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6614c543-5838-3cf7-8f84-7972dbfad1a4 | -11.6818 | -44.3844 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 556ebfb2-721b-3466-8a21-9a47f8c75e1f | -11.7006 | -44.4049 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| eb4170aa-b5db-3491-aab4-d18a34886355 | -11.701 | -44.3815 | 2025-09-25 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 761dde96-28cf-330c-983f-c6289262f923 | -10.313 | -45.2219 | 2025-09-25 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 06642a6c-d9f9-3879-94dd-313984c8eab5 | -8.8415 | -46.2095 | 2025-09-25 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1edac891-7393-327b-8292-c5ce0374abcb | -20.5441 | -57.1434 | 2025-09-25 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bf0342ae-7e10-335b-a8c9-e3b07dddd639 | -11.4229 | -44.9563 | 2025-09-25 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 70516613-17fb-3d2e-91a0-cb4185dafae7 | -10.3321 | -45.2195 | 2025-09-25 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1fbe066d-fc49-38e5-a801-d19a88438949 | -9.7851 | -46.2851 | 2025-09-25 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 06b9db34-d8ac-3fa6-8bcd-59bae4aae9f1 | -8.1324 | -44.1417 | 2025-09-25 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0e72f88b-228d-32b7-8e0a-94583e03bfec | -10.3935 | -46.167 | 2025-09-25 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 572970a4-52d1-3f6a-80f6-592b57e159ef | -7.7555 | -44.1342 | 2025-09-25 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6d3b4bb9-05dc-3748-a433-d785d2257b55 | -17.9312 | -55.8548 | 2025-09-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 476436cb-588f-3cae-a762-df0250fa3482 | -6.8336 | -44.175 | 2025-09-25 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e137fe6c-bed7-329c-a62e-083f7d18de8d | -11.4225 | -44.9794 | 2025-09-25 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| feaec8d1-088a-39d0-adbc-2729c677a5b3 | -6.4129 | -43.0958 | 2025-09-25 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 29132bd2-1afb-3e9c-ac59-3ffb40869e34 | -11.4037 | -44.959 | 2025-09-25 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| da8889f2-3540-334b-ab4c-bb6cb944480f | -11.6457 | -45.3388 | 2025-09-25 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c24774df-111f-3b7b-ac27-981a7e9a715f | -8.6631 | -43.991 | 2025-09-25 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 924b54b2-f1a4-3f5f-8293-5885002db04d | -7.3567 | -44.4496 | 2025-09-25 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 09925b8f-0b73-3e71-857a-b4f847399c27 | -3.2116 | -43.3726 | 2025-09-25 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ee9acfe9-c92b-3bbc-b2b1-dc979cce208d | -15.2819 | -59.4321 | 2025-09-25 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| edf34669-47d3-3b50-bdaf-ec86f7e29e43 | -8.7898 | -43.0394 | 2025-09-25 14:10:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 1029a751-9e2c-35c1-9daf-83530597a1e7 | -17.9506 | -55.8731 | 2025-09-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| af47c117-9435-3de5-b84c-a6b75328e7fa | -7.788 | -46.1789 | 2025-09-25 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e67ea484-82c0-3dca-9512-2a99205e48c2 | -17.951 | -55.8522 | 2025-09-25 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 1d0af888-1cf1-3f5d-989a-c209704c8030 | -10.294 | -45.2243 | 2025-09-25 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| bf4651d1-f15d-38f6-8ae5-a4a6e5603494 | -8.4987 | -44.9998 | 2025-09-25 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| cc77dc5f-1f24-392f-9634-034584de335a | -8.6631 | -43.991 | 2025-09-25 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0749cc85-f763-3144-9cce-d1f6a1599e4a | -11.6818 | -44.3844 | 2025-09-25 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| cf953098-1578-3f9d-8e41-77aaa4c2b500 | -11.6622 | -44.4107 | 2025-09-25 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 288.4 |
| a6a408f1-5122-33be-be27-21bdaa3a5051 | -4.4611 | -40.9566 | 2025-09-25 14:20:00 | GOES-19 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 118.6 |
| 85e93aba-4b4b-36f9-a261-8c5e1ac63c66 | -10.9569 | -44.2805 | 2025-09-25 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 83d3c3e8-7890-399e-81b3-2291402ddfca | -20.7131 | -57.8321 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 10444ff3-7e4c-3616-a701-43197f614042 | -10.9377 | -44.2832 | 2025-09-25 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3595ca55-83e7-3cf8-8a31-7e4353ff777e | -17.951 | -55.8522 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| fb08a33b-76c1-305c-9cc5-ae713577baaa | -10.313 | -45.2219 | 2025-09-25 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 409.0 |
| 65a8081a-44f6-3509-98e5-065fa0c86dcc | -6.4129 | -43.0958 | 2025-09-25 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 583fbece-1d79-3c19-981c-c2c0e654cdb1 | -3.1929 | -43.3734 | 2025-09-25 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c64861da-f1ba-3e99-b379-a4640fb0d83c | -6.6975 | -44.6232 | 2025-09-25 14:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b7c20c7f-7f5b-3634-a51d-e77c8b0637ad | -20.7135 | -57.8112 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 3391c62f-8df4-32a8-bbf8-f8bff9f5bdd5 | -8.1324 | -44.1417 | 2025-09-25 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4090644b-60f7-31c1-a597-8a274efb648c | -21.0131 | -50.0217 | 2025-09-25 14:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 191d9821-31e4-3569-8311-301f15b67321 | -17.9308 | -55.8758 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.6 |
| 82011bbc-7ae1-33f1-b85c-46938e913eff | -8.8415 | -46.2095 | 2025-09-25 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 409e3639-bc39-30e4-92f7-6f85a2f82ef1 | -15.8029 | -59.4835 | 2025-09-25 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 1c3dfdb8-1c18-39ed-b9c9-5adce1a3478d | -3.1764 | -42.9547 | 2025-09-25 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| dffa07fe-468e-30f8-aa6a-69e8b89a9a78 | -3.7815 | -41.6957 | 2025-09-25 14:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 4213ab46-fb96-380e-90ee-c988a64ffa53 | -7.3755 | -44.4478 | 2025-09-25 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| af1f5b47-a3f0-3b4f-877e-cc31fbef8912 | -4.7974 | -43.5435 | 2025-09-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8b76330e-3ac7-3823-93f6-2951e38159aa | -11.6457 | -45.3388 | 2025-09-25 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 7cbf4aeb-a7ac-3794-af2c-b057dcf3e7c4 | -5.7767 | -42.8902 | 2025-09-25 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 0368adbb-2963-39bf-bc7a-0800646cac07 | -7.6141 | -46.6188 | 2025-09-25 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1dfd899a-12c2-34e3-822e-8d482a1b34e2 | -17.9312 | -55.8548 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 34071f17-9405-3d7b-98a8-2a848bf94dd1 | -11.4037 | -44.959 | 2025-09-25 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7639c2d2-37bc-30a6-a6a7-58a4ad0d728f | -15.2819 | -59.4321 | 2025-09-25 14:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 2c8732af-be1c-38f1-8679-15e6d1c307a2 | -7.3567 | -44.4496 | 2025-09-25 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3c63c721-2cda-3aa4-b919-0ef8416153fe | -11.6626 | -44.3873 | 2025-09-25 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 14c7da42-9fca-3703-bde8-a07df226646d | -4.7623 | -43.2434 | 2025-09-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 66890bed-9cbc-3ceb-b01e-154d78ab2a64 | -17.9506 | -55.8731 | 2025-09-25 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| abe6ebd5-5bc8-3aa2-ba69-1819fd4b24ec | -11.4229 | -44.9563 | 2025-09-25 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d3ead109-5873-37eb-8e2a-db74e501e918 | -8.4987 | -44.9998 | 2025-09-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 0a9cca03-42bd-39be-89ef-bdd12cafb107 | -10.9381 | -44.2598 | 2025-09-25 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 7caa2dc4-6320-397b-81fd-42e86b35e618 | -11.4229 | -44.9563 | 2025-09-25 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1cfc5aaf-7db5-30dc-90be-cc41232f9872 | -11.6818 | -44.3844 | 2025-09-25 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 3b728c88-45e1-3e1d-8d24-1765b56e1a44 | -9.2488 | -48.2491 | 2025-09-25 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 64d227bd-c484-3a4b-a027-d078a0d2e6b9 | -11.4037 | -44.959 | 2025-09-25 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 93504fb6-f666-3371-a317-9eabdc292dd9 | -8.1324 | -44.1417 | 2025-09-25 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8a4ccad5-37c0-3459-bae9-4b43954a0a4d | -7.6141 | -46.6188 | 2025-09-25 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 705a4e83-1a88-3042-8cf1-d26b7aca9705 | -17.951 | -55.8522 | 2025-09-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 9209e3c8-e732-33c5-a65f-f53a39fe4843 | -20.5441 | -57.1434 | 2025-09-25 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f7b1bf50-03f6-3994-befc-5f6da0e675b1 | -8.8417 | -46.187 | 2025-09-25 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8d842519-8601-3fbf-a307-f73b3ce366e5 | -8.8415 | -46.2095 | 2025-09-25 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 4f735467-45b2-325a-a40a-9bb9d5e99baa | -10.9573 | -44.2571 | 2025-09-25 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 750414e2-9449-31b5-86e5-e6cbb2721f87 | -15.2626 | -59.4339 | 2025-09-25 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| ab05bb6d-71d5-3fd3-8a64-b5fe65fedb94 | -15.8029 | -59.4835 | 2025-09-25 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 938b9662-a4a4-3462-b4a0-dd7c8f903bb5 | -17.9308 | -55.8758 | 2025-09-25 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.9 |
| dac1b60c-6163-3dfe-9792-ccfb840929e4 | -9.7851 | -46.2851 | 2025-09-25 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README42.md)
