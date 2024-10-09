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

## Dados Diários - Página 211

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69fd4bb1-a281-3acf-b71a-f5be183de9a5 | -6.79584 | -59.3469 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9907f38e-94c0-3ee5-b7c6-8fafabade9e7 | -6.79538 | -59.35022 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74bb28c6-98a8-3309-b12e-f44bda0c1de0 | -6.79493 | -59.35355 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95f02982-19b2-331e-acf0-13b41ff2af0b | -6.77592 | -60.04519 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71b1c9d9-16ee-3646-803a-a687525704f1 | -6.77512 | -60.05112 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 2ed6ce35-58d0-329d-a2f1-8d1d7f2cb334 | -6.77471 | -60.05408 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 0031dce1-8a37-3461-adcb-ad9c9cbcb892 | -6.77431 | -60.057 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 44a822b9-2f65-331a-9700-a844e9d07fe2 | -6.76599 | -60.05465 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0ce17a45-9646-3fef-92b6-689bd2215b29 | -6.76557 | -60.05753 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8021fe5-e49f-3780-8422-c34c7c870a5b | -6.76516 | -60.06044 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f7a8fe3-31be-3880-8ffd-8293ee006903 | -6.76492 | -60.04958 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e9bf611d-798e-3ef5-b734-f85e0584a3a1 | -6.7609 | -60.05384 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d7d5ed84-41e4-32a1-9454-12b66441578a | -6.76048 | -60.05676 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f54bbfa-1fdc-3b0d-8215-6abc7c00b515 | -6.73505 | -59.63393 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae0f1b5-56be-30a6-aefd-253f926828fd | -6.67779 | -59.46635 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd8e7e1-5d77-3f93-9628-0dd92bafb8bb | -6.66092 | -59.77987 | 2024-10-09 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85369c29-bd7a-3cee-9bc8-e6170059f0b5 | -6.65573 | -59.77912 | 2024-10-09 05:55:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38a35810-b5c7-3231-bb77-111d1c9b15b9 | -6.54777 | -60.00499 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e468a340-9ae6-3f8d-9af8-0145ca28dc8d | -6.54686 | -59.9982 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e0ed65c-3c08-3620-8170-a323a5d7aebd | -6.54311 | -60.00117 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdfd1a89-8951-3680-b8db-94ff36bf05a6 | -7.30001 | -59.73613 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| febaf3ac-b77d-3d9c-94bb-238a903a2f72 | -7.29914 | -59.7425 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d1ac56a-a526-3594-b203-0865f86f1a33 | -7.25084 | -59.62667 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70f2b11-edcb-39c8-a0d3-fcd260c660c4 | -7.24967 | -59.63173 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82709e7e-5152-3070-a43e-2e85cc4d045d | -7.24479 | -59.62786 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31ae867e-5c15-3873-ab55-c43191e68a86 | -7.24466 | -59.63229 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f55dd1b6-2dbe-38dd-8e6e-7cb30ff9dcff | -7.24437 | -59.63101 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9c833a7-d131-3cc7-9ba5-ebf3e21e3958 | -7.19269 | -59.77446 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a44ed403-d560-3197-8585-f4176f65453d | -7.16555 | -59.3541 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cb4577f-5037-3f03-97b4-d823054fa420 | -7.15925 | -59.35998 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b6384ed-6ad9-386f-bf7e-ce58a6331453 | -7.13403 | -59.30383 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c27635e-690d-3243-afa2-d75606e9d010 | -7.0406 | -59.40286 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50674acc-d1d6-37b5-9cd2-dfb0cb2d7b6b | -7.03405 | -59.44999 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af40dbe3-ecca-30d1-af4e-b8beb30b77b5 | -7.03339 | -59.41554 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2885ee4e-694e-3ca0-ac3f-45e4bbbd27a7 | -7.02712 | -59.42145 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0febe9b1-ed5e-32fa-bbe3-78fc627a4398 | -7.02665 | -59.42482 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07f31c93-2b61-3107-8e1d-6118388d44c9 | -7.02317 | -59.41054 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ada4f3a-8bf7-375d-addd-a3baa6c2501b | -7.02131 | -59.42408 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d287334-b037-39d5-a196-02221029f3d6 | -6.80564 | -59.355 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c643289-f3ea-336b-b551-f03949a840d4 | -6.80029 | -59.35426 | 2024-10-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e09cbc6a-9536-36aa-9cca-fc45fed4bbf7 | -6.77552 | -60.04817 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9e4b44ac-aa61-386f-9496-15b5daeac08d | -6.77391 | -60.05995 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b24ea8b1-4916-35fa-aded-2ccf1704856b | -6.77041 | -60.04745 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 56a693b1-ddaa-39f3-9f45-061b595faacf | -6.77001 | -60.05042 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dd4b0498-31d9-37cd-b573-93b0f9bf8b1b | -6.7696 | -60.05338 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bf8b2605-1a77-3f2a-8517-d6a94f297990 | -6.76921 | -60.05631 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4e54663c-44c2-397b-b76f-0cb45e840d12 | -6.76881 | -60.05921 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 37a3491f-49d1-3118-af71-47a1b29aae75 | -6.76683 | -60.04874 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a2f4de1-fce6-3e92-98d0-5a3c366fb638 | -6.76641 | -60.05171 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f82289a-a740-3749-8f65-9a228661cac7 | -6.76451 | -60.05256 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 043831fb-5530-35ce-9936-3b368b1572c2 | -6.76412 | -60.05548 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 542e8361-f456-335e-917c-b1bb41e82f52 | -6.76372 | -60.05839 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 76bf925d-ee40-3241-948d-c8d3fe2ceb71 | -6.76132 | -60.05087 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f73f477c-2201-39ef-9d51-9f3e6abd1793 | -6.54862 | -59.999 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5aacd546-a23e-3b4e-b948-d89e559f050d | -6.54819 | -60.002 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e2cb10f-de7f-309c-9e10-76a7cde4b061 | -6.54645 | -60.00123 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31c50b33-cb8b-3850-925c-8b2169e83727 | -6.54605 | -60.00424 | 2024-10-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0dc701e-fe72-36bb-b195-3bdf5e83956d | -9.33846 | -60.3189 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ccea596-a02f-361f-86b1-f265734aa0ee | -9.33409 | -60.31176 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03f1aafd-c2ad-3746-9dc1-2ec0771e023e | -9.33367 | -60.31496 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9173a505-c9a4-31dd-b769-e70c19d49739 | -9.32889 | -60.31102 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08118101-1761-3157-af07-fce601d1d2af | -9.24299 | -60.42939 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7d08d5-27ca-36d8-bff7-fa548bb3c201 | -9.24258 | -60.43248 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d5ba94-729c-36f0-b4fe-894d3d21ff1f | -9.2393 | -60.45714 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb2bea7a-7535-3dfd-b8b2-99043bfbed0d | -9.15158 | -60.42947 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84c721ca-4f65-393f-97cc-161272951a99 | -9.15116 | -60.43257 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86f688ba-b472-3ca2-a126-0ba085aff80b | -9.08928 | -61.12856 | 2024-10-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d34c7c0-b146-3990-80ea-c001be4707d0 | -10.42926 | -60.9935 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 327a2eb6-46b4-3435-9c03-1141aad12a73 | -10.42886 | -60.99656 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90e81d50-c8c7-3f14-9cc7-5f1564ba0db2 | -10.4285 | -60.99941 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 694f7c1c-a028-377c-8ae2-6b7ff2a24ea0 | -10.42426 | -60.9924 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0a14d66-523b-3d4a-9ca4-649ed082fa58 | -10.42387 | -60.99549 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 533ea20a-1b44-3a55-a9df-07130b09b778 | -10.42349 | -60.9984 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 933cfa98-b596-3152-a98a-7619d74f3096 | -10.41888 | -60.99435 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ed21d81-4212-362b-a65a-53f2c49770da | -10.39521 | -61.25654 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d33429f5-89e4-319b-af84-8c835088b368 | -10.39438 | -61.26294 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01d6307d-3658-3404-a811-58ded6d5d616 | -10.3933 | -61.23233 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8eba5e5d-dcc2-3621-97e3-bb08bea8caaf | -10.39254 | -61.2382 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 12fb344f-da08-355d-8e61-52ea4df57bdc | -10.39179 | -61.24397 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b5e5a538-d080-3bd8-863e-d2e0a538e241 | -10.39104 | -61.24977 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 00a2201c-d93e-3f83-a221-73bd001bbe25 | -10.39026 | -61.25582 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 392139b9-3837-32a0-b141-89056c94156a | -10.38939 | -61.2626 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98be7db1-3d9d-3988-b5e5-8ccc5d795060 | -10.38909 | -61.22581 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5f99038-1d06-397e-866f-ac9b25be2fbc | -10.38833 | -61.23167 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 417a1be5-aa7b-3b43-9c01-4e473b2c618a | -10.38757 | -61.23757 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3bce9308-5ee9-3372-8946-13794797882b | -10.38682 | -61.24342 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c69eff2-16c7-3a78-9ed0-6c9a33a185fe | -10.38607 | -61.24921 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fea883be-b59e-3542-870f-ded0f8674917 | -10.38532 | -61.25507 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| be5286eb-c8ab-35b5-ae52-f1bcb044026b | -10.38448 | -61.26153 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f14ef4ec-ee6b-3f54-9658-a480010866ea | -10.38413 | -61.2251 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fccc2b44-b26a-3d03-b554-80ca1e8d64e8 | -10.38338 | -61.23096 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 553ff849-2fff-3597-bce0-cf6b10918d5b | -10.38261 | -61.23693 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1686c14e-3fd7-3aa9-a186-e169ed8ad4e0 | -10.38182 | -61.24306 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e84dc3b8-4482-3398-b315-9c739a6ea2c5 | -10.37587 | -61.17109 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d671b2bf-d0a2-3d0e-a0c3-e99ffd9cd4ad | -10.3753 | -61.1705 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2c94923-4be9-3b04-b80e-444bd56e4c60 | -10.07096 | -61.12096 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6178012-2419-30dc-a234-a2ffd2c75357 | -10.06595 | -61.1206 | 2024-10-09 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0a5f2cd-5710-3e12-b6b1-3e5327f04acd | -9.98038 | -59.87222 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3071968c-24d4-3f67-805b-01cca153e185 | -9.97994 | -59.87564 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f42a59db-4960-3ac5-8490-7ab6a0c05582 | -9.92794 | -59.93826 | 2024-10-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README212.md)
