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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 120d8dfe-896f-3fbc-816b-168a08f074a2 | -6.17198 | -44.30116 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8004cd5a-1876-378b-8566-a2834566ea13 | -2.95139 | -49.34119 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 118ae52e-f7ab-33d1-9bf0-06b63f20b938 | -5.02243 | -49.99747 | 2025-10-15 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83d74494-c80d-360c-842b-e516ca93ff96 | -7.94741 | -44.13284 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60138a83-4612-3f81-a75d-96355f336273 | -6.34244 | -42.65624 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| adb3adb9-3996-344e-a3e8-093212a4a70e | -5.42315 | -44.2257 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f54b5e4a-28a1-3dfe-a541-679a958bfbf8 | -6.24315 | -41.55472 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83bf6cfc-625d-35cf-a98e-4ee483b054c3 | -6.19578 | -43.28251 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3309f1d0-5e25-398f-b723-9b78cb592847 | -5.52409 | -42.72322 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80871899-e5b2-35a3-9497-4487fe1ce4ea | -6.43627 | -41.88004 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b099d75-c384-39df-ae3b-503da3495330 | -6.44997 | -43.81885 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67b5a916-cf48-35a6-9970-13964c10a81d | -5.87612 | -42.78547 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c20a9ba-ec61-3e68-a6ff-8ca4e5e59061 | -5.83111 | -42.32667 | 2025-10-15 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 28632abf-2afa-3f9e-9453-af732595345d | -5.31141 | -42.91498 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68786d27-b617-3a44-a0de-ef7042f2a39e | -6.07029 | -44.30257 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6520063-1790-3e4f-8f0b-efe5fe6deaa3 | -3.99981 | -45.43405 | 2025-10-15 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bb9451f-ac72-3f1f-97da-57739f895902 | -8.28251 | -43.43805 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fc42bf3-9f60-3f26-a34a-4075bbd5fe85 | -5.57137 | -43.02081 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b360d733-fdbf-39a7-8148-7e455dabe657 | -5.39323 | -44.03731 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 182c62f5-3f92-3f6a-becc-b81337803386 | -3.78279 | -49.43284 | 2025-10-15 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e050d3f-f86e-3020-91dd-76c408302b53 | -6.05227 | -41.90097 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0cf277d6-df3b-33bd-b391-bb82611250a5 | -5.34613 | -43.74587 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 66714479-3c95-3e50-adfb-b9627669330d | -6.48969 | -44.11311 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 108ac5ee-8057-30aa-b65e-e565eb782799 | -4.42441 | -41.6035 | 2025-10-15 04:06:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| afea0e3a-21d2-3c8b-9bd3-f53d09b5bcdf | -5.8405 | -43.96022 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1256c80e-b2fa-3fd4-97b0-c0e7132a0050 | -6.19425 | -41.75638 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1775ecc0-375f-3941-91f6-cf8217559afa | -6.22256 | -42.49811 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e7c792c4-3583-33e3-910f-c3337254889e | -8.09973 | -39.99399 | 2025-10-15 04:06:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1676b75a-1966-315b-bb41-3a9d61a83415 | -5.57287 | -41.10852 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ec79b9c7-2002-3ee2-ace1-33e21759fe31 | -5.615 | -42.72646 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6fb7602d-a4b9-3562-a2e7-94257c9e3700 | -5.63209 | -42.68461 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0aff328e-d15e-3073-b9a2-5b0c857db34f | -4.27237 | -44.36611 | 2025-10-15 04:06:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5c906e6-71e6-311b-bc28-0336881afa1a | -6.45994 | -41.85886 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e675fea1-15c2-3d2b-8d8c-f72fe136c4f1 | -6.05126 | -43.39491 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd9a6ea-e362-3c22-abfc-187632166b68 | -5.40259 | -41.15578 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ecb6e7d-62fb-3642-a827-3f6c6d120222 | -10.16373 | -36.16997 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6eadeb4-5493-35d8-b43b-ac58c87997b3 | -6.59337 | -43.92103 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2163a08-63fd-35a5-a4d1-1be17b179305 | -4.63418 | -42.52332 | 2025-10-15 04:06:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b21eed8f-68bb-36c1-bcb0-f801a75db922 | -5.45509 | -44.65016 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30682453-a65d-30d6-884c-1e8c0e41d6ce | -7.94548 | -44.14452 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bc86e3c-9d96-33ed-b26c-9ffd43f73f5f | -6.45938 | -41.88372 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e915516-937d-3b05-80c7-68c2f1ead089 | -4.19859 | -44.70498 | 2025-10-15 04:06:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2adfc8d8-01bb-341b-b676-bf5844c0418f | -8.27471 | -43.42175 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b67d922-b777-3efe-838e-82107035a56b | -4.28786 | -48.58458 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad4227e9-12b6-3984-861a-ebdffd29d2d8 | -4.14042 | -41.65887 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 62c2a3bf-9c89-3e89-8aa9-ec37ccbb8b46 | -6.2604 | -38.16671 | 2025-10-15 04:06:00 | NOAA-20 | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6adcc9b9-0193-3269-a757-4817efe9e7b7 | -7.07989 | -45.20621 | 2025-10-15 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da5a8740-5966-34b1-9d57-3057a1ebbdc1 | -3.16678 | -48.61144 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d80c6bf-2154-32f8-8ee4-6827899def3d | -2.95189 | -49.33807 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 875425a5-125a-3bdd-838a-be8917a97fe4 | -5.00789 | -44.49525 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a5b0ca9-f9f0-3e90-b57d-e134e66e143d | -5.24271 | -44.89116 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e4376d0-e35f-3d41-8aea-9d97707c66b9 | -8.13733 | -44.47537 | 2025-10-15 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d35fe6d-277f-3143-9b7b-09cd19451ca4 | -7.23589 | -41.20537 | 2025-10-15 04:06:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69babda6-b7ef-382c-8d46-7f6e97680982 | -4.14485 | -41.65247 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17d30a27-cb16-368b-842e-ee4aa462b81d | -5.90256 | -44.72792 | 2025-10-15 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 559b3442-1cc6-3bd3-9ee2-5272884720e6 | -6.37382 | -41.50103 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c32963eb-1f9e-337c-81ea-f0be85353798 | -6.17631 | -42.61551 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36850b0b-0b00-3c80-a46d-3519d47ff61f | -7.16056 | -42.49525 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8025574c-0c5d-3b24-aab4-3d0b3257dd2b | -5.03174 | -44.7362 | 2025-10-15 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8ba0352-8f36-3001-a288-64911434dfe3 | -4.78627 | -46.01196 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0386c68-6fbd-338f-9604-aab2c2414de8 | -6.77239 | -42.81644 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6004c51-8e98-3a71-8392-4f834d408b05 | -5.29689 | -42.52401 | 2025-10-15 04:06:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f497fb56-136c-3fd5-ab55-5bf3954c7fe3 | -7.48341 | -42.13297 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc4d2555-71cc-3d4e-9ae7-143e1f1f4432 | -4.31898 | -44.53753 | 2025-10-15 04:06:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e47f583-e548-373c-bb74-b0c6a50eb9ec | -4.88552 | -42.76907 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f85275e6-d790-3d52-8fc0-f2583a2f9d9e | -5.72651 | -43.83615 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b519d1c6-2c0f-3e92-ad33-dc8aea8a62df | -6.33872 | -44.01553 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df2ef2c3-fd6d-3510-89cf-6e287226836c | -4.66103 | -43.12019 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1e40e729-d40c-3404-a043-7174e7fcc979 | -5.19124 | -43.80784 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f40ada3a-4aa1-3020-a519-435fa1249bd3 | -6.05338 | -41.89401 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 90adbbff-d14a-39a3-a281-78f02f78e575 | -5.32882 | -42.56237 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2dd10cb-23ad-30b9-81ca-810e144cd140 | -5.18907 | -46.17647 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df98aa0a-0094-3681-acdd-de8c0da3b9b0 | -4.31454 | -44.54136 | 2025-10-15 04:06:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a05474d-15a0-3a92-bca0-c9a6547776bc | -6.05891 | -41.90201 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 366a7950-5ca2-3c2e-9d3e-0481815943d2 | -6.33517 | -44.01503 | 2025-10-15 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef9d4b94-6d2a-35b0-8a45-8863b6853382 | -5.2324 | -45.07235 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0098b0e-0824-35b3-8604-333f12f48920 | -8.28168 | -43.40038 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9bc6a09-7552-3a0c-8c5e-6ebecf15b57c | -5.70859 | -37.94102 | 2025-10-15 04:06:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54258d2e-4bf1-3f8e-a713-8a982076b250 | -4.90699 | -43.46105 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b5e98521-9dec-31c8-b44f-5d71afe45131 | -7.48557 | -42.65213 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d16b30c-e982-344f-9f78-d616ee2425ef | -8.25718 | -43.35191 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 103fc858-3bd1-39ef-befa-e4b6c74a05bc | -7.25933 | -44.91094 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42464c7e-2564-36b2-b24c-5d545be7327b | -7.75359 | -42.44194 | 2025-10-15 04:06:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88a1a4b1-5783-35ae-86df-4f98c27c6325 | -5.56753 | -41.31651 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| be18aad9-f73a-3357-9849-2ff41842f843 | -8.24761 | -43.34662 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 81906c13-2a6b-3b4e-8011-56560e243c09 | -5.53775 | -43.46272 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c04bef10-96a5-3d35-a807-877ddd458672 | -5.59231 | -42.84649 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb01d821-f8a1-38eb-b70a-1baf950e61f6 | -8.21373 | -44.0318 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb5c383a-b767-3eb9-9338-b39e637411fb | -5.87495 | -42.79274 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0ca1783-ff36-3358-8ba4-12b25566b736 | -5.19834 | -46.14501 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddfab033-a7ac-3e30-b204-89967d451b8a | -8.26278 | -43.36034 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6c903ff-851e-314d-bbe9-d682917771be | -5.56529 | -42.99316 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d207368a-bd36-3361-85c6-6e20067b3c46 | -7.94327 | -44.13615 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9197df9-63ca-3e71-824b-2cfb3831a332 | -4.82872 | -41.47504 | 2025-10-15 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4691fc18-bd52-354a-a335-45f945cd6d32 | -5.85948 | -42.82384 | 2025-10-15 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f56d6f8-1ad3-334f-92d6-5b1007ffbca9 | -5.18396 | -42.92161 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fa3da62-6020-34b1-99f9-8fc262efb800 | -5.56708 | -42.98207 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe09a306-4620-30ec-8d00-32a72e45f213 | -9.13518 | -46.87325 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f421f8-6224-378d-b4fd-2ba282263a61 | -8.46044 | -44.18964 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4c13c252-078f-3c2d-902b-7cdda7bc747a | -5.873 | -43.8714 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
