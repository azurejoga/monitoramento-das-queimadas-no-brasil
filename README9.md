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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a84fe86d-a44c-381b-9823-d207e90f1386 | -6.92757 | -43.50557 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ae870099-00a1-3106-9418-9ded777f5a36 | -8.98968 | -36.49984 | 2024-12-17 03:27:00 | NOAA-20 | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df3297ab-ba3c-3777-a1f0-80ec2b00cdc0 | -6.96709 | -42.83612 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d84b27de-935a-3776-983a-09adeee97c6e | -7.40727 | -44.73254 | 2024-12-17 03:27:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4ee35cd-3612-3f47-bea5-942785ab28e9 | -6.97306 | -40.63664 | 2024-12-17 03:27:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2858d415-52b8-33ad-80ce-c7212acfd535 | -7.81995 | -35.23561 | 2024-12-17 03:27:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 843bc81d-d32d-3fbe-9ab2-b92609ac3b35 | -5.98179 | -41.5737 | 2024-12-17 03:27:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 67859a2a-cb1b-3f60-8023-6e1d1ce7ad6f | -6.96728 | -43.0045 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad92694a-c4d9-3a10-bf24-d429c18dbe83 | -6.0319 | -42.15889 | 2024-12-17 03:27:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 384f1c8c-4185-37f1-8ae6-40793629d7cf | -6.98482 | -43.56165 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf1ca68a-add1-363d-bac0-f536a7d0fe7c | -5.20409 | -44.56833 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64708607-7459-37cb-96f8-ce5c1abac930 | -9.27825 | -35.91024 | 2024-12-17 03:27:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d1e48e73-0c42-3138-a8d3-f58771f3ffa9 | -7.85965 | -43.09352 | 2024-12-17 03:27:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1998b16-59cf-3df2-81c4-27e79878bd4b | -8.75764 | -35.75013 | 2024-12-17 03:27:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5c88f66-8a47-37c2-bebf-b7ae49bc1cef | -8.05898 | -41.2721 | 2024-12-17 03:27:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 778c4f2c-91ba-3f28-8e36-e0c54a2c04c1 | -10.03284 | -36.17517 | 2024-12-17 03:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74356c44-6245-3de7-b702-e99f67a19d38 | -6.93114 | -43.51464 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 7c20535f-0901-34c8-ac85-be4d6d78f866 | -6.98803 | -36.24619 | 2024-12-17 03:27:00 | NOAA-20 | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4eaf4be1-e36a-30f0-a359-10de46399294 | -6.95526 | -42.83392 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c693e462-abbd-3b7d-8181-b1b332d59bc9 | -5.62315 | -44.83887 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88a560d8-7991-3428-9e03-e5bc25677e8e | -6.97301 | -42.8372 | 2024-12-17 03:27:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a968d52b-5399-3730-90df-410dbac3f03b | -6.03261 | -42.15487 | 2024-12-17 03:27:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aaeacaaa-2b44-3185-9233-f2b72d90d88d | -8.87835 | -41.10806 | 2024-12-17 03:27:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4cf70fea-469f-34f0-87c6-451137b1ff69 | -6.93204 | -43.5098 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| d696e4f3-1c99-3c6a-abad-a209c0e916f3 | -10.03212 | -36.1795 | 2024-12-17 03:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 075cb699-e05d-395d-bcf7-f3098028d657 | -7.86048 | -43.08891 | 2024-12-17 03:27:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa304d40-0a47-3f7e-adf6-1b9930e52818 | -6.91612 | -43.52668 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99f35dc6-a24b-306b-bc96-a4939c998a13 | -6.9867 | -43.56026 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90324126-3f20-3a79-8ac5-485a12bca55f | -5.20246 | -44.56574 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 36942314-5e60-3dc3-ab38-2c1a2be67692 | -7.41148 | -44.73393 | 2024-12-17 03:27:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0fccd31-04a5-3e08-b87d-b66ad67a038c | -5.35959 | -44.0543 | 2024-12-17 03:27:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc8cc2c8-1ec3-33fb-8aed-466eff9fb063 | -10.60882 | -37.00183 | 2024-12-17 03:27:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 44.5 |
| 4e7ad871-8069-3355-b29b-a47f05bd0a8e | -6.91523 | -43.53149 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed2a6e55-b5b9-3c33-bb14-1755e42a0967 | -7.98086 | -35.23206 | 2024-12-17 03:27:00 | NOAA-20 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b363b65c-a219-3bf2-99fd-85241739b412 | -12.86021 | -43.74665 | 2024-12-17 03:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6998ee0-1afc-3b34-a002-a8d4da261b14 | -6.92585 | -43.51525 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| e2d31cb6-21c8-3a9a-989e-307d3bb211b4 | -6.92409 | -43.51821 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c3898d90-62d2-366f-b7ce-41a78883996b | -14.24809 | -41.75065 | 2024-12-17 03:29:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11629054-2b59-3b3f-be1c-3832b99b06e5 | -14.24553 | -41.75134 | 2024-12-17 03:29:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a653e608-da14-3618-9c98-44bf3c20f7a6 | -15.0865 | -59.6487 | 2024-12-17 03:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3ca4e5d5-ed34-3fa4-82c4-487a27bd1089 | -5.1125 | -43.8933 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 6c8efefb-eb0b-3654-9e83-cc0b033cfe59 | -3.2968 | -53.3749 | 2024-12-17 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0f62c890-e7e7-3d40-bf57-d5d9384eb0ae | -5.0749 | -43.9189 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b8302244-ed77-37f5-9811-b45980763f0c | -5.1123 | -43.9164 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e82edcfd-19c1-3baf-a344-4b6816a47e08 | -6.9158 | -43.5185 | 2024-12-17 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a0f33eaa-b48c-351c-be3e-f7b41e2b7eed | -5.0751 | -43.8958 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 765a6fae-10b1-39be-8bee-66dc5f426b99 | -6.9349 | -43.4934 | 2024-12-17 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fad51d33-20b9-3f80-80dd-79c8a2889b72 | -6.9161 | -43.4952 | 2024-12-17 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 806c49b7-fc5e-33e8-8361-6b504c441d37 | -5.0938 | -43.8945 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 293.6 |
| a2558896-69d2-3476-a5fa-b6f7fe7528d2 | -5.0936 | -43.9176 | 2024-12-17 03:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 326.0 |
| 2769094a-6c39-376c-8494-a8266554e5d9 | -6.9346 | -43.5168 | 2024-12-17 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 51f5e021-bf31-35f3-96ee-cff58c7556bb | -23.84909 | -50.00584 | 2024-12-17 03:32:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f723b1d7-51e1-382d-8e1f-9cbed9449a31 | -20.76279 | -46.77158 | 2024-12-17 03:32:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aecab953-ffc4-38e4-b94a-1e7f20c7c4f3 | -22.54064 | -48.81614 | 2024-12-17 03:32:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dde32782-450b-3cc3-8d9a-c22467e34163 | -23.84747 | -50.01228 | 2024-12-17 03:32:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 543f6d86-cee8-3ff2-8b5f-b1f3b086a779 | -23.85237 | -50.00898 | 2024-12-17 03:32:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7511cbd4-5642-3df3-b0a7-4aa6ed61a1a8 | -5.0938 | -43.8945 | 2024-12-17 03:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 5984babe-f404-33ac-97bc-3a0f7f6f0e43 | 4.4435 | -60.9657 | 2024-12-17 03:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a3b84525-4121-31d8-b1f2-389124803c5a | -19.1043 | -52.8493 | 2024-12-17 03:40:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 144409c9-b1a8-331f-a8d7-cf23acec9b4a | -5.0936 | -43.9176 | 2024-12-17 03:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 1565f8a3-325f-3d7c-8ba1-1fe1c24a38f3 | -6.9349 | -43.4934 | 2024-12-17 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 089bc605-3efd-32a9-9b4d-a5687b4eff13 | 4.4435 | -60.9846 | 2024-12-17 03:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b655b2ab-aa67-30a9-bef3-d8fd1b73c1a5 | -6.9158 | -43.5185 | 2024-12-17 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bb40cbab-6d00-30b6-830b-e8adae57f891 | -6.9346 | -43.5168 | 2024-12-17 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3e7a4ab4-4753-3fc6-92e6-81ea4bf1cd31 | -6.9161 | -43.4952 | 2024-12-17 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 246151c3-269d-3bbc-9bd2-d4f7f898a653 | -5.1125 | -43.8933 | 2024-12-17 03:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 250e2f86-b74e-3d17-a6d1-4970e7a6ea0f | -5.1123 | -43.9164 | 2024-12-17 03:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 2932f7b2-2d14-3f76-811e-a82a1e89e7c5 | -15.0865 | -59.6487 | 2024-12-17 03:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9a6b8477-19e9-3679-8db9-3191817793a3 | -5.0749 | -43.9189 | 2024-12-17 03:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ebff49c4-512e-34b0-a222-bf3f8d9f1231 | -5.0751 | -43.8958 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 52595655-a9fd-32cb-a8e1-376d11a3e34d | -5.0936 | -43.9176 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 4e931f2a-679b-3008-a03d-e9e82bf9aa09 | -3.2968 | -53.3749 | 2024-12-17 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 63cde95c-3ea8-372f-85fd-8bd1b1f5682b | -6.9158 | -43.5185 | 2024-12-17 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c04514e4-0bd4-36b6-9bf9-315d260f310d | -5.0749 | -43.9189 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0502f65b-7ce8-3d40-8404-a805365c765a | -6.9346 | -43.5168 | 2024-12-17 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 849709af-d689-3bec-b228-71077150f9ef | -5.0938 | -43.8945 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 2e8c4226-7e2e-3fee-bf50-b03ea223da7e | -6.9349 | -43.4934 | 2024-12-17 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 10310da8-a3d4-3bfc-bf15-4fbf0c1874cd | 4.4435 | -60.9846 | 2024-12-17 03:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8d57efbe-894d-31db-ba59-9b0b712a58a4 | -5.1125 | -43.8933 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e358adb6-c459-3fc2-9a3d-5281d39fa143 | -15.0865 | -59.6487 | 2024-12-17 03:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8df1dc77-6135-3fba-a196-711175d2e2a4 | -5.1123 | -43.9164 | 2024-12-17 03:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c9978c18-d299-3d2b-b872-c84dde54ce10 | -6.214 | -46.2202 | 2024-12-17 04:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 84031b63-c642-32ff-b04c-9217f5014224 | -3.2968 | -53.3749 | 2024-12-17 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| dab5ecf2-4332-3820-9b4d-34e3f1e217a7 | -6.9346 | -43.5168 | 2024-12-17 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 36dd6980-67e0-3a3f-8cb1-58e4c51898a6 | -6.9349 | -43.4934 | 2024-12-17 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e343ef36-1ffe-3e74-8edf-500bf24f2106 | -5.0938 | -43.8945 | 2024-12-17 04:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| c228513e-3e4d-345c-87a1-f7296181d6cc | -6.9158 | -43.5185 | 2024-12-17 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 999a4267-02cd-30a4-9dd8-d1fa5297ff72 | -15.0865 | -59.6487 | 2024-12-17 04:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| eb7812c2-5658-370a-86c4-4d38336bae58 | -5.0936 | -43.9176 | 2024-12-17 04:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| ef66629b-5666-3c03-84db-2fb3acfb5838 | -5.0936 | -43.9176 | 2024-12-17 04:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| bc6a7f70-bb0b-3557-954b-e714245326c2 | -3.2969 | -53.3547 | 2024-12-17 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0e441985-7b17-3075-abb5-03e86f32401c | -3.2968 | -53.3749 | 2024-12-17 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f1b2db65-160c-3669-9b05-6291434e2436 | -6.9349 | -43.4934 | 2024-12-17 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e82b5465-208b-3516-acfe-3c5a8e2b5577 | -6.9346 | -43.5168 | 2024-12-17 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 74f627d4-a470-3652-ac8d-6d4497272d4d | -5.0938 | -43.8945 | 2024-12-17 04:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 119376c1-e347-320d-a61e-bd3968a600a3 | -19.1043 | -52.8493 | 2024-12-17 04:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 53f0a933-2e4e-3767-beb9-607abc4184d2 | -15.0865 | -59.6487 | 2024-12-17 04:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 39f772f8-4072-3427-b449-cdbc1d3d62be | -6.9158 | -43.5185 | 2024-12-17 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4715920b-fd7b-3d4d-9f0a-d5793d367490 | -19.1043 | -52.8493 | 2024-12-17 04:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 10585374-d76d-35e2-9dfe-3e3f9fb1ffc0 | -5.1123 | -43.9164 | 2024-12-17 04:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |


[Clique aqui para ver as próximas entradas](README10.md)
