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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a4bc4ec-52de-336c-b473-f8f70e1ad061 | -1.54809 | -48.60798 | 2024-11-08 04:53:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 952450dc-3f36-3af2-9318-a8289f1b73f5 | -4.24354 | -48.53912 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3f88ed0-610d-3fa3-a000-aa55ba7361d0 | -3.09332 | -53.71216 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65884517-38ec-3fa3-a8f4-0245424d7dc8 | -3.96189 | -48.15911 | 2024-11-08 04:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8f78c536-6016-3065-835e-a4bef96ae367 | -5.7463 | -42.00243 | 2024-11-08 04:55:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c0662d25-937a-3d22-bcd4-bbec929e30ae | -4.50855 | -45.67223 | 2024-11-08 04:55:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 696203b1-9bbf-37ca-9b72-6b591a4770ff | -4.69035 | -46.39717 | 2024-11-08 04:55:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d5716d46-4b53-341e-98cd-0f101c5447e9 | -3.55527 | -47.37594 | 2024-11-08 04:55:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 3835546c-c57e-34f2-98be-6b90ba7e3af6 | -3.72182 | -41.6913 | 2024-11-08 04:55:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3134d9f0-a9fa-3fbe-9475-0f5f78af4ef4 | -9.10286 | -43.031 | 2024-11-08 04:55:00 | AQUA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4bd576f8-d435-33da-985a-184bbf0c83b5 | -3.81322 | -43.59128 | 2024-11-08 04:55:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f491e5d8-c7fc-3cc4-9572-56063ae845f9 | -4.52871 | -45.68327 | 2024-11-08 04:55:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f6a359ea-5ee2-39b6-8272-27b261c651ea | -5.9856 | -45.37111 | 2024-11-08 04:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 93e4db5e-6718-3cc3-811a-c13b9909cb1b | -3.55121 | -47.38035 | 2024-11-08 04:55:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 2a1eac41-c257-3cd7-897d-203bffa18939 | -5.98869 | -45.35182 | 2024-11-08 04:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2be1ac2f-a99e-3cf0-bfc6-c539b288372f | -4.51891 | -45.6586 | 2024-11-08 04:55:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| e5646e14-b43f-32c0-9175-5536c6d36105 | -7.40436 | -35.23462 | 2024-11-08 04:55:00 | AQUA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 7a481b68-4241-3f87-861c-518fe24955d0 | -7.49305 | -43.55554 | 2024-11-08 04:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9a5b2632-d7e4-33dc-81e3-d07716808510 | -3.55644 | -47.34883 | 2024-11-08 04:55:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 45c7a961-13f1-38c2-927f-ed4bb61a0a57 | -3.56023 | -47.34457 | 2024-11-08 04:55:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 6f2c0556-703d-3097-b090-ef36a3de7611 | -5.64813 | -44.24339 | 2024-11-08 04:55:00 | AQUA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ce627b6e-c060-3540-bfb2-8eaa150c6d02 | -4.87033 | -42.95096 | 2024-11-08 04:55:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3a809158-d2a1-33b2-b60e-c26388129dcf | -4.51536 | -45.68057 | 2024-11-08 04:55:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 8d79cb10-0d5e-3f80-8d68-da2586094a08 | -7.40254 | -35.24767 | 2024-11-08 04:55:00 | AQUA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 49cd8a12-9469-3eb3-a847-c7d2f1d234e3 | -3.97835 | -48.16171 | 2024-11-08 04:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e4a02f1a-35bc-3607-81df-baef9e04209a | -3.96921 | -48.16537 | 2024-11-08 04:55:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ed151cfe-f718-3777-85ea-2cece27e9b6a | -7.69188 | -61.06192 | 2024-11-08 04:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201dab10-1bed-345e-b50c-baa0a92d4329 | -10.75902 | -44.0313 | 2024-11-08 04:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f96dc70-2590-3255-a876-b168d07acc85 | -6.9128 | -59.06179 | 2024-11-08 04:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2694f35-79d6-3d81-8813-e308a2aee5fb | -6.91211 | -59.06593 | 2024-11-08 04:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a71d4ed-f19a-3c7a-9cb6-9c97fb06aed3 | -7.29263 | -57.55016 | 2024-11-08 04:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e7e9558-247f-31dc-8f6d-97d66101bdd9 | -6.91715 | -59.0625 | 2024-11-08 04:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50eaeb81-7b35-351c-a02c-045311c3a846 | -2.8016 | -52.9414 | 2024-11-08 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| b8e0a933-dc3b-38b4-bbc9-daa5b4c25213 | -4.5209 | -45.6804 | 2024-11-08 05:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 117.0 |
| b4b24fae-a92c-3cae-98d2-e8259f4f6650 | -3.967 | -48.15 | 2024-11-08 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d1eca24b-1ab7-3e87-b2e4-f417dee92c7f | -3.5632 | -47.3629 | 2024-11-08 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 684f6115-dec6-3ac2-a9fe-7ec67c9242c7 | -2.82 | -52.9613 | 2024-11-08 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5945b3fd-aad9-3bbc-b7b9-473a9c0982ae | -2.82 | -52.9409 | 2024-11-08 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0d56d242-57e3-3ba5-9425-b151c08eee14 | -4.6835 | -46.4074 | 2024-11-08 05:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 017114f6-b31b-3eb0-9f18-0a30ec04846f | -3.9669 | -48.1716 | 2024-11-08 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a666d342-e81c-3ce8-bc00-8aca99de37a6 | -2.8016 | -52.9617 | 2024-11-08 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3b210150-9cd2-3c03-ac56-d5636bf8c218 | -3.5631 | -47.3847 | 2024-11-08 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 9554cf0b-8b30-350b-870b-b95d7f82d0c8 | -4.5022 | -45.6815 | 2024-11-08 05:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 44a3fae6-7269-374c-990c-bf592ca070b1 | -3.5446 | -47.3855 | 2024-11-08 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9660dc6a-ec9c-31b5-9b56-5d8b8303c001 | -4.8767 | -42.9554 | 2024-11-08 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 4cc3f584-6029-30c6-9b12-547936c57682 | -7.4799 | -43.5579 | 2024-11-08 05:10:00 | GOES-16 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| eb8a640b-ca61-3170-8e3c-a9375ca18172 | -2.8016 | -52.9617 | 2024-11-08 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e20fc02c-a357-304a-ab2e-2ff7efab3da5 | -3.967 | -48.15 | 2024-11-08 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 846477ea-805a-3e7b-bdda-345a7228f168 | -3.5446 | -47.3855 | 2024-11-08 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 581b8f1b-d9b3-337c-8949-b2c765c50ae8 | -3.5631 | -47.3847 | 2024-11-08 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ef5e0e36-0060-39f0-9e01-d5b0421e7171 | -4.6835 | -46.4074 | 2024-11-08 05:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 4ad0fe54-5a23-3504-b85a-7382dd286a5f | -7.4988 | -43.556 | 2024-11-08 05:10:00 | GOES-16 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 40decfba-0e0e-3ed9-9bd2-a1568517bca1 | -3.5447 | -47.3636 | 2024-11-08 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e2b084ab-b8a3-36e3-85ac-46879845019d | -1.1467 | -53.6573 | 2024-11-08 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0a252831-21d9-35d5-99ed-b85bf3f4f64b | -2.82 | -52.9613 | 2024-11-08 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 821277c3-e7c8-3473-bbf3-3f5a367ec2f9 | -3.9669 | -48.1716 | 2024-11-08 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 350f3821-343b-34ab-8094-0014acaee5de | -2.8016 | -52.9414 | 2024-11-08 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a46adaf5-34f4-3bfb-82b7-c337007ff768 | -4.5209 | -45.6804 | 2024-11-08 05:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 134.3 |
| b2d01bd8-802e-3895-82e0-3e8ccfab030c | -3.068 | -50.5631 | 2024-11-08 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| ac8ce9a0-bae0-3070-9d45-236b35acb35b | -2.82 | -52.9409 | 2024-11-08 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 885523bb-9912-316e-8c8f-077af8d706b5 | -2.8016 | -52.9414 | 2024-11-08 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 53c38fb5-130a-3e98-87b1-bc9a7fb26ca1 | -3.5631 | -47.3847 | 2024-11-08 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bd16c6c5-3ee2-30a9-b1a6-90a5c98dc86b | -4.5207 | -45.7029 | 2024-11-08 05:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 836f294d-f8b9-36a6-b035-d1bcec9db70d | -3.5446 | -47.3855 | 2024-11-08 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 5632bbcb-d518-3941-8ba0-5f65f13ebd14 | -3.9669 | -48.1716 | 2024-11-08 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 41b0e31a-1e7e-366d-865c-36d43d38e2ac | -2.82 | -52.9409 | 2024-11-08 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0e43afbc-97c5-3f48-9092-989dfe8c59c3 | -3.068 | -50.5631 | 2024-11-08 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 81b47f91-718b-35e2-af6b-f7202bed7c78 | -4.6835 | -46.4074 | 2024-11-08 05:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 23b1e3e3-ed42-3f09-8d10-89ce94b6d125 | -4.5209 | -45.6804 | 2024-11-08 05:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| bcb10668-08f8-31d4-a93a-bb7e52a2a8f0 | -2.82 | -52.9613 | 2024-11-08 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d276364c-2c91-3470-b4da-14636ae40034 | -2.8016 | -52.9617 | 2024-11-08 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| baca8b33-dbfa-30d9-a93a-2db08c1a9a65 | -1.1467 | -53.6573 | 2024-11-08 05:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9526c82c-6416-342f-bff9-9c6b193f5171 | -2.82 | -52.9409 | 2024-11-08 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3e3ca09a-1e3e-3c2d-8f2b-96e7a38dff31 | -3.5446 | -47.3855 | 2024-11-08 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| c1438ea1-b63c-3237-b070-76191729901f | -3.9669 | -48.1716 | 2024-11-08 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| c8b23516-dd18-3840-b4dd-4b27973c4807 | -2.8016 | -52.9617 | 2024-11-08 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fc344444-f03e-3337-bd6e-8488ed25125b | -2.8016 | -52.9414 | 2024-11-08 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| e40634c9-f852-3c30-b109-47718370e0bd | -3.5631 | -47.3847 | 2024-11-08 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ef2dd0cb-c90a-3b72-bf73-48fb375c0b94 | -2.82 | -52.9613 | 2024-11-08 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 651cc604-752e-3bf5-9c08-15f2fe3b5292 | -4.6835 | -46.4074 | 2024-11-08 05:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| cd269e99-eb5b-3cef-bee5-fa1f8bc42271 | -4.5209 | -45.6804 | 2024-11-08 05:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 509f2ea3-be3b-3b71-bc13-66ce19577a64 | -1.1546 | -52.00843 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba9c5722-b907-3ea5-b246-80e1ecf20e1d | -1.45611 | -53.41681 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78be029e-5d44-3e3e-a6fb-67f1576b1872 | -0.64182 | -52.38714 | 2024-11-08 05:37:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef75c42c-0365-3acf-a1b9-f04dbfc22cb9 | -1.1472 | -53.65725 | 2024-11-08 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f4632e7c-911b-3719-9f77-3e8da7b7e3b1 | -1.17149 | -54.15818 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f58891-d71b-3110-b78a-f2f5329ef934 | -1.52758 | -54.29149 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 491dfa8f-7e0e-3b1c-b929-28a39ab74299 | -1.22994 | -55.80735 | 2024-11-08 05:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f22b695-7083-30ab-a4d2-841356fc0eb7 | 1.57968 | -63.30339 | 2024-11-08 05:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 838eb14f-862d-346a-859f-9485de7a6ec2 | 2.51452 | -50.94004 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab8bac77-2f01-39d2-ae56-e4e10ebd7ce6 | -1.32662 | -54.18347 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4aea07a-fffc-3666-8cab-3772ea77c04f | -1.10414 | -54.1985 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c99f3a52-b713-3c5b-9223-b483a32e9e86 | -0.64463 | -52.39161 | 2024-11-08 05:37:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6812ecf8-a31c-3dbb-a525-5e443c8f0cb5 | -1.14786 | -53.65295 | 2024-11-08 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9a9b6c7d-3782-3ef0-86fb-9fe22e4c382f | -1.24373 | -53.38609 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8f29682-cfe1-3a01-80d7-ad04f0ffc3c3 | 1.52415 | -56.07025 | 2024-11-08 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21a2d837-5cf6-38d8-9aca-bd22be72c82f | 2.52105 | -50.93884 | 2024-11-08 05:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5af7e85f-60d4-3076-be36-8936259ad532 | -1.34256 | -54.62374 | 2024-11-08 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa6dcd83-46b5-3798-82a5-81dba19869f8 | -1.25527 | -53.35159 | 2024-11-08 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2862102-f3a9-36a0-9576-804df72b5a4d | -1.14737 | -52.01149 | 2024-11-08 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README36.md)
