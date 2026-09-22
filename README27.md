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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee80ee37-0719-3a2c-bf6a-74f4a1d466d3 | -6.467 | -59.9902 | 2026-09-22 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f31db559-eed3-3d21-bc93-8b764fcd8e55 | -3.2396 | -53.9417 | 2026-09-22 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8b9eb763-9cb8-3291-a532-6578cf3ba186 | -7.5889 | -57.6757 | 2026-09-22 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 24ab88e6-fed7-3718-80f8-aa66550e9d18 | -11.3255 | -54.0487 | 2026-09-22 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9cde9f02-d8b0-38d3-b343-ca822d5ce967 | -3.2395 | -53.9618 | 2026-09-22 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f727c335-6c01-3c06-aca0-5da0d3d2fb9a | -10.6094 | -53.9902 | 2026-09-22 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 4f176cbf-14f4-36fb-99e6-cde7429cd95b | -5.7569 | -45.084 | 2026-09-22 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| bc4ea8a2-9307-3d28-ae2b-0460b9438aa5 | -9.5594 | -66.0359 | 2026-09-22 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e92869fd-2ba3-3004-82d7-92be29a6c2c3 | -18.7472 | -46.93 | 2026-09-22 03:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 73424243-0db2-3ab2-9dbd-841644e05428 | -5.7567 | -45.1067 | 2026-09-22 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8fb8e413-47d6-3e4e-a089-893d948e2a1b | -10.5906 | -53.9918 | 2026-09-22 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4183e18c-b9e1-3cc2-b404-0497d92a53b3 | -10.6097 | -53.9697 | 2026-09-22 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4f75c710-f488-31d1-979c-a5246e67945a | -3.2211 | -53.9623 | 2026-09-22 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6aafff04-3823-3304-bfc5-c5b2b5591873 | -3.3453 | -42.78551 | 2026-09-22 03:40:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86f1c7a9-5db2-3f24-b7b1-780c3da5115c | -3.68568 | -42.96427 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f1703d9-a31e-394e-80c6-018319ed92e3 | -5.00797 | -38.02743 | 2026-09-22 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7f9e42ea-130a-3895-9014-5eb9f9928c71 | -3.68924 | -42.96062 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1f94e162-c3ca-3a92-a77e-b741a78039e6 | -3.69363 | -42.95547 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b35b2663-19b3-34ca-aadf-108b34463c50 | -3.69194 | -42.96538 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61253dcb-4763-379c-a340-915f61c0b5d2 | -3.83546 | -40.10975 | 2026-09-22 03:40:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 774409e5-d2e7-3d64-82c7-85c583093890 | -5.01311 | -38.02388 | 2026-09-22 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 048e1ba7-2b79-3579-ae11-7f90283d708a | -4.21934 | -40.62268 | 2026-09-22 03:40:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33aaff5c-cdd8-3e0f-a38a-fbacf26eb8bc | -3.68652 | -42.95933 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dae00f48-0df4-33b3-b8aa-f37095be8f4c | -5.00869 | -38.02313 | 2026-09-22 03:40:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53f7459a-47fa-3eb2-b3ca-245ba20dfee6 | -3.34614 | -42.78063 | 2026-09-22 03:40:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381946e1-c235-3092-bdeb-66fc05a623d1 | -3.69279 | -42.96043 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f1450e3c-86cd-3d85-8269-3f92545a3559 | -3.69011 | -42.95573 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 305d8aaa-47ee-32e2-8f8a-f008351701f2 | -3.83494 | -40.11283 | 2026-09-22 03:40:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4e186b00-20e2-3760-bab1-2fea34febae6 | -3.68836 | -42.96558 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0de1e6c0-1707-336e-abab-2190d530c80b | -3.82974 | -40.11197 | 2026-09-22 03:40:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7d34419-4459-3183-ba4d-b091fa5d4969 | -3.69098 | -42.95082 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a05b10a6-3f84-3be4-af00-34e6d5a96ebf | -3.68736 | -42.95443 | 2026-09-22 03:40:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 836b4dfb-46de-3847-931a-57d64b6dd630 | -4.25532 | -38.04272 | 2026-09-22 03:40:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4b3cf4c6-9285-3f6c-8816-5b29c554f90d | -4.21991 | -40.6194 | 2026-09-22 03:40:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4dbb8cc7-9aa7-3b52-9513-9c2696454c06 | -5.42139 | -36.75836 | 2026-09-22 03:42:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 612dc3b6-1add-34ac-8760-b0167141aa6e | -7.13142 | -42.0692 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a41d9d02-5c14-3279-99b2-c8352b4ba6dd | -6.57642 | -44.16361 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40886e5d-e26e-3881-a897-26dc96f541c8 | -9.60964 | -43.94111 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8051dee-d40c-33ac-9c35-0e59714d6904 | -6.49764 | -37.00849 | 2026-09-22 03:42:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00ca843f-064a-366f-b816-c55cdf96da81 | -6.57943 | -44.14759 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7540b6ec-aec4-3c3d-ad01-cd9c0c980c0c | -5.74907 | -45.08763 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d594e9fe-8b39-3189-b5cb-15e8de84c26c | -6.89971 | -41.69429 | 2026-09-22 03:42:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a6043ae-a724-3b9b-9317-1a21196ff47f | -5.75717 | -45.08248 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4521979d-f207-3d0b-878c-59fd3f78eb38 | -9.29235 | -44.37853 | 2026-09-22 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd84d5d0-61b5-3f5b-a9a3-a965313a9c3e | -5.76203 | -45.09614 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2b9a5c55-655a-3cf7-ad10-7880379c9347 | -8.48678 | -44.75252 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f4278a4-3ff2-395e-97f0-15e8de2d00d0 | -9.28234 | -46.18874 | 2026-09-22 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b25b0769-0cb9-3c80-a503-279e7221aa58 | -5.83471 | -43.84674 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 079c0782-af8e-31b4-89fc-03959562c3b1 | -8.79666 | -44.27791 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27fb509e-f462-3618-aa9d-203601cfd14d | -7.13634 | -42.07404 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eafa3810-0faa-3d3b-9cad-0ecc5fbd0c6c | -4.57892 | -42.9383 | 2026-09-22 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64b4f482-671d-3c2e-b801-2fb6b40bf963 | -8.30626 | -40.60201 | 2026-09-22 03:42:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d2c739ea-4028-3445-ba4e-ddb9e70d63e3 | -9.60486 | -43.92882 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70613127-af19-3d0b-a421-8cf97d14f133 | -6.59967 | -39.14218 | 2026-09-22 03:42:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb1bd5bc-bfc9-3bd7-9bf7-5d8147cca989 | -5.75469 | -45.09563 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| c66e5856-fd45-307a-a28b-1b32f915a03f | -10.02043 | -45.21025 | 2026-09-22 03:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 051e52fa-d4aa-35fa-899b-b48036bf93f1 | -6.59502 | -39.1414 | 2026-09-22 03:42:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7239bd13-5d07-3bcd-bc79-a5d6fe7210d0 | -5.79665 | -43.86827 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20e55434-d2a4-3d51-8d53-498017153aea | -4.95204 | -45.15424 | 2026-09-22 03:42:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7a99e13-0575-3d47-aa2f-0025dd77586d | -9.62644 | -43.94727 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 303f7176-bd68-33aa-8e66-3022fafae459 | -6.49706 | -37.01198 | 2026-09-22 03:42:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4330bdb9-e057-336d-9d7a-517ee1ab5e4c | -9.62212 | -43.93692 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46ae0824-962b-3721-98e6-49ef34ec8759 | -6.50168 | -37.00915 | 2026-09-22 03:42:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46a61b3f-4d0a-37c3-9f94-a3cb2108801f | -7.83219 | -45.25797 | 2026-09-22 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0fff42e-4232-3e28-b87c-843498e355ec | -4.95907 | -45.15535 | 2026-09-22 03:42:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8d8b938-fc1c-3334-a244-1a7d75c0b6dc | -10.01515 | -45.20282 | 2026-09-22 03:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c158c832-a2b5-3884-bb51-fa537934296c | -8.78763 | -44.29139 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1d65c0b-4589-3e51-bfa4-e51ea0f5f373 | -7.26253 | -39.18091 | 2026-09-22 03:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f924c88-4435-37de-8b04-00041173f5a8 | -5.76413 | -45.08332 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9711ccd-4bf9-3d8f-8f48-0915dade3b6d | -7.55458 | -42.66143 | 2026-09-22 03:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| daf5f856-53d4-36ea-a93c-08fec5e3c9a3 | -5.97865 | -44.72866 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f45807f-b6f8-3ebd-86fd-bc3d38164ecb | -6.71556 | -43.98385 | 2026-09-22 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 840e6bd7-c863-389c-ab66-0541906153bb | -8.48807 | -44.74156 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d95f8394-bf41-30e6-bbe5-67ffcc83c748 | -8.31895 | -44.75452 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb3948e1-2e9e-366b-83f5-326798a93c0c | -5.74825 | -45.09359 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0d531a50-3b08-38de-af42-91288585fdc0 | -5.75027 | -45.08131 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b03223a0-80ee-37b1-9f93-77f8c847401e | -7.83073 | -45.25399 | 2026-09-22 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f82f6cbd-1486-396d-9edc-2c83ee629437 | -8.78695 | -44.27637 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7ab4291-066c-3692-8db1-6860a6ef994a | -5.75506 | -45.09529 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 60d1cf76-8f15-3e91-962b-c1802087fa1c | -5.98537 | -44.72989 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b292c5f-5f79-38aa-9418-a8ef7a51b1ba | -9.61834 | -43.92874 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed76f624-86d6-3020-8358-967c0780841f | -5.32094 | -43.41586 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3218da7d-891b-39bb-95df-3eeefb495875 | -7.44638 | -44.74485 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d042e39f-e953-31c3-a855-49547d148157 | -6.71647 | -43.97885 | 2026-09-22 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c784b79-00c1-30a2-8c97-703b2e51f29f | -8.78952 | -44.28139 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 20fc2727-5d64-3bf4-a68f-51172b781653 | -7.82961 | -45.25989 | 2026-09-22 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 805f8672-2b67-3429-86f2-93117c2432c6 | -9.62296 | -43.9325 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c4b7c47b-ac03-3f7b-b6a0-b851b1761f91 | -8.48885 | -44.7416 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1c18e30-3d98-3ac5-b544-8da04d6192a5 | -8.79217 | -44.28284 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a1abc34-83dd-3e6e-b658-12846f875284 | -7.26314 | -39.18367 | 2026-09-22 03:42:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40dbadd9-b1e9-38a6-862a-4a63b7932334 | -6.57643 | -44.16164 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ed59482e-29cf-306d-9bfa-a952181248c9 | -10.48513 | -36.89787 | 2026-09-22 03:42:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b95c7de8-20df-3763-8cc3-455a886f8ece | -9.61007 | -43.93439 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d17e08a4-1cf9-3470-8a21-b0d05d0849ac | -8.78456 | -44.30767 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a80b623-1778-3cf5-8007-d6df6e2b7ff5 | -8.30672 | -40.59958 | 2026-09-22 03:42:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e135a276-ef9a-3d87-83b7-cc158afc9667 | -6.57933 | -44.14561 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8eba27c-863b-3e42-b301-d9af0da345f4 | -9.61781 | -43.9266 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5c521f3-5d10-32a0-83e5-8e01029461f0 | -5.78773 | -43.76994 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80df1fed-95f6-36eb-b84b-029ad54eaaad | -8.48781 | -44.74707 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4b82637-bbe9-3e0b-a8de-a4114665e359 | -5.33787 | -43.30444 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
