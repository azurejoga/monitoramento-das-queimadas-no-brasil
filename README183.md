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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3332d7-903a-3b82-8de2-b05555b610ca | -2.98854 | -61.43163 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ba36b61-17ae-3c81-a616-1a4b70d0407b | -2.98907 | -61.42815 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aedacc2-0c1d-394f-b967-5b886053e37b | -2.99044 | -61.42891 | 2024-10-03 06:05:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75c7681e-e00a-38c9-b0e9-252eadd29496 | -1.50126 | -61.59047 | 2024-10-03 06:05:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e11b977f-f40e-308f-bc24-1b0199e1eb7b | -1.50652 | -61.59131 | 2024-10-03 06:05:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85657939-993b-3f6b-8a0e-e4328b6873d3 | 0.89575 | -59.69471 | 2024-10-03 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31340a1f-51f0-3b2d-a44a-ea4aa2e4d181 | 0.89001 | -59.69566 | 2024-10-03 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17652d93-0ae4-3147-b681-05d41049cc02 | -3.4 | -42.27 | 2024-10-03 06:05:08 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b228082a-1bfe-31e9-8389-fcea2846aae0 | -3.43 | -42.27 | 2024-10-03 06:05:08 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20c7a146-a06b-3a0a-a4ae-0ef3ad90fc73 | -8.9976 | -67.4094 | 2024-10-03 06:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0aba8ed8-43f3-3d4f-9df2-54c1d65b0eda | -9.0515 | -67.871 | 2024-10-03 06:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ab7aedc7-af95-3b0e-8816-61507bf7f568 | -11.6931 | -64.9974 | 2024-10-03 06:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a5b7841a-af43-3ef1-910b-d863d88f4ec6 | -7.95723 | -70.15253 | 2024-10-03 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce29f82-5ce5-3f89-a358-532b1bf191a4 | -9.43722 | -68.94448 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e0bf83b-d10d-383b-95e5-282f98ac5e27 | -9.44022 | -68.94931 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| baa5e52d-f609-3c8f-ba62-18bf4ab364d1 | -9.45242 | -68.94234 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f6d54cc-6ea1-3e79-8893-676c5e8c3209 | -9.45245 | -68.94559 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14e6b962-c130-3654-aad1-9e142b80d165 | -9.5028 | -68.95757 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d943f133-c9a9-3012-b663-1925d0fc6849 | -9.50343 | -68.95328 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01469990-c525-38b9-9004-39662fa16d22 | -7.45134 | -70.00065 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84849e4a-9a3c-3de6-86a8-44a7e4684f17 | -7.45475 | -70.00118 | 2024-10-03 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5762d252-942d-30c2-a34e-e109f8a7e956 | -9.34557 | -65.75808 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d9ba9ca-8e51-305a-bdea-9afdbe775854 | -9.36626 | -65.79916 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f2b312a-07a5-3bee-bb86-5c9c87500f20 | -9.36684 | -65.79479 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c90cb0f-12e7-3f7c-ba58-d6b5daca13e2 | -9.36877 | -65.5269 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab69f1de-2282-37d0-b2d5-82caa0fe6849 | -9.37647 | -65.47153 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd9b0da9-056c-3e6b-af29-768b8c3a52de | -9.37652 | -65.53737 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfd800cd-a17c-3671-ad57-30078d9fa279 | -9.37711 | -65.46693 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5188b645-26b0-321a-83ee-0950d3d62a5b | -9.37716 | -65.53278 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09eb20a5-04a4-3203-8526-813bb317ea67 | -9.381 | -65.50529 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 547020d1-6c67-31b5-a2b1-c88c0903f294 | -9.38165 | -65.46758 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9db5ce72-b741-329c-a358-3627ce2939f8 | -9.38167 | -65.53347 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59ae9701-e77a-3b54-90d9-7abc29690d0e | -9.59643 | -65.67008 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7448b6f-7450-3655-ab5b-1f68520e751d | -9.59864 | -65.673 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52dcaaa8-cab0-3343-ac50-a522d505d91b | -9.59925 | -65.66845 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f6dff4f-0649-3b18-b36e-7c94f92244fa | -9.6489 | -65.74005 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bc59217-a676-3309-93d5-6a243456a87f | -9.70778 | -65.76376 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e0aaa04-5c94-32dd-ac1d-7d24b129acc2 | -9.70837 | -65.75934 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a479203-d73e-34a8-9efa-13c13cf7545a | -9.70897 | -65.75494 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 626b13e6-df40-3118-97b2-13f20e3a308f | -9.75067 | -65.51331 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8fd6a91-8ea0-344b-b792-a5e70275c51f | -9.7858 | -65.85686 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 145d247a-6b0c-39f0-b374-1dc342fb4e5d | -9.54805 | -64.33142 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5066d707-7be4-30cd-9637-5ff15751c8ac | -9.55012 | -64.33199 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6b46443-7d8f-3053-b1ed-4f03ebf17d8d | -9.55297 | -64.33213 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53963d12-586d-32f7-8248-7abc5292f469 | -9.5917 | -64.43398 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6705f81e-abc5-394f-ac6a-a011526532df | -9.59659 | -64.43467 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98197ed2-ad3d-3ee4-a02f-02152aa54e9e | -9.67473 | -64.72622 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 645a7a75-aba4-3edd-abd5-d8df74c07367 | -9.67952 | -64.72691 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc5dec94-9174-3439-a746-d1dee58b73cd | -9.68022 | -64.72176 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c95971e-9e0e-3b31-a5df-b24921cf6d57 | -9.8108 | -64.95447 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 378919a5-1483-3232-9215-94c74b5897dd | -9.81553 | -64.95522 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 247139e0-5e60-3971-8040-0fe7a8886e3c | -9.82025 | -64.95596 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c88ccbea-f090-3c49-9c3c-ba09ae087155 | -9.82429 | -64.70194 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 934ee99b-97c4-334f-8a23-091a85a4d562 | -9.82493 | -64.7013 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aa7b49a-2647-3f09-aa1a-692013a37441 | -9.85083 | -64.87127 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47b0ce08-4769-33ee-baec-3bd2148e8ae7 | -9.85152 | -64.86611 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f423f297-1596-3b65-8b2b-3757a0e43768 | -9.8556 | -64.87192 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23600878-89cd-3b41-a4a2-fc7c5cc0a044 | -9.85629 | -64.86677 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb12f2c0-ccd0-34c3-a913-e115b5df0bb4 | -9.86075 | -64.97746 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07068c12-49fa-3deb-9a01-2a02671507d6 | -9.86144 | -64.97231 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e8bd705-4188-3b57-9f8a-c5ac219fffd8 | -9.93238 | -64.77209 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f704c47f-d427-30fd-b9e2-b3611c8685d0 | -9.93257 | -64.7714 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7c880fa-9a00-3ac0-9a19-0290fa6e3cc6 | -9.93308 | -64.76675 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53920498-da89-3ba4-9b5d-2930df7183f8 | -9.9333 | -64.76608 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da47233-6760-34af-b26a-c670c0820849 | -9.93719 | -64.77271 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1eee4c4-fef3-3f97-8ef5-8baadc858899 | -9.93737 | -64.77203 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523a2cf8-a70e-3fa1-b600-a2f1a66bc636 | -9.93782 | -64.91624 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9023e1ac-8f58-398b-a0a5-a3e648f61c85 | -9.9385 | -64.91108 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6d3b27f-1fac-3cc2-884c-181da6ce73c4 | -9.93919 | -64.90591 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c09c6ee8-65c4-3bab-b771-1ad7d764266d | -9.94258 | -64.91689 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a31e27b-fe8b-3113-8b9d-eed71de002bb | -9.94326 | -64.91177 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90d49388-d894-3895-ab44-a8088fd225a0 | -9.94394 | -64.9066 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8da7c248-a52e-3158-a09a-16d3b5a0d709 | -9.94801 | -64.91243 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9594d39d-9025-380c-b815-15d40680e14c | -9.9487 | -64.90728 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4afbba0-caf7-3e24-86a2-327d041ac8d1 | -9.96048 | -64.78149 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a21c6f92-1eab-3c5b-9bf5-ad60add87d7e | -9.96118 | -64.77618 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cb04a45-0212-3f7e-acae-5010567a39e8 | -9.96528 | -64.78218 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 516edf02-3f04-3874-a445-06f6c98605e2 | -9.96598 | -64.77685 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32f4ecfc-5953-33a0-b0a2-0783f7c7ea42 | -9.96669 | -64.77149 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50e51311-6fb0-37f5-a94f-9dd492649e0a | -9.9715 | -64.77216 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a95d5479-781c-366c-a848-eea1e4989cb2 | -9.9722 | -64.76688 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246eb232-61c5-3324-87cf-b33a63fbd07d | -9.98659 | -64.76903 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c7ba217-4f14-3c18-8788-37599947bcf0 | -9.14465 | -65.55511 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb9945cf-e296-3d3c-a601-7e557cf166ea | -9.14528 | -65.55054 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 166ebd80-5920-3869-9646-3170d8b1f1b2 | -9.17499 | -65.55172 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb2b35b9-e7fe-3314-8797-3d182d6e961a | -9.17674 | -65.55516 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b83baba6-490c-3bf2-836c-c4360fb7ae33 | -9.17826 | -65.5615 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6855f2-cd5e-3417-81a8-ee37964830a3 | -9.17887 | -65.55695 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd990d87-6ea5-33ff-95b2-a47bb4948be3 | -9.18059 | -65.56036 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d96889e1-cf82-3161-863a-c6ddfac4444b | -9.24129 | -65.60297 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 738ce26a-e240-3a67-ad91-a553b4864a09 | -9.24577 | -65.60364 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d920305a-b833-3079-8df6-e786dc0f6ee4 | -9.29536 | -65.34744 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d02555a3-cbd3-35d6-9ad1-b09d59c8daaa | -9.29601 | -65.3428 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f4bda71-81e4-37a3-85fa-55ef4a708bfc | -9.29666 | -65.33815 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29b59335-2f5f-3e95-9b94-1f0477823b8e | -9.30184 | -65.3677 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c92403a-a5ee-383c-a862-75ed2d06cde1 | -9.3025 | -65.36296 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14ee470c-219b-32b5-9b80-62a9f8c849ef | -9.30269 | -65.36574 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8236d5ac-c4a3-384b-88cc-17ffb802d70f | -9.30316 | -65.35832 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31e273ef-e7a6-36e3-9ec9-a1ca366f490e | -9.30331 | -65.36102 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1db8e771-30c5-3989-868e-a2cf1157a4ee | -9.30392 | -65.35641 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README184.md)
