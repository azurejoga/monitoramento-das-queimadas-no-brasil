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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b528a19-8f27-3aa0-a11d-4c7a3dc0ac17 | -1.68199 | -52.78885 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595d6413-98f4-33ac-ae51-153f15e9c685 | -3.06447 | -54.05942 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 960e040c-ca40-36f2-8a41-1d3d35d75bbe | -1.66254 | -52.75496 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f93f264e-718c-3c62-a91c-6193454ff9db | -1.45021 | -55.21094 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c6fcd83-0c18-3a98-a9aa-221aa55e4128 | -1.74392 | -52.61081 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd2cf38-a915-3247-8ede-251727e9d82c | -3.27262 | -50.32958 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4c2404-1ac1-36f2-a42e-881b9035ebd8 | 1.08816 | -59.64397 | 2024-12-04 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58f57f22-0afe-3924-b3a3-aaba2eb2513a | -4.38143 | -43.37618 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7c6fe98-05bb-3b7d-b1d0-3a6c22bfa14d | -2.97005 | -53.7422 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4afd4f25-4196-32b4-beda-4ce19baf3486 | -2.27679 | -53.6144 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac40585d-0626-3c1b-b330-8515bc9c0a4d | -1.41693 | -54.5278 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8a3f643-7bb5-37fa-b8e8-5522c9fd026d | -3.12236 | -51.26594 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39bd23f2-2744-3f64-b9d1-513942b7bc5b | -2.68912 | -54.24329 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4ca8310-4257-3839-af89-54110a5f0dbb | -1.82131 | -54.50954 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e00ce96-d348-35e9-b403-57755151dd06 | -2.86158 | -54.09727 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0c9a0e1-adef-3348-b3fb-4d79068fde80 | -2.80564 | -55.30736 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b027bb32-a48b-32fa-846a-607a0424f466 | -3.11713 | -53.10196 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3617b39b-74d6-3835-97bd-756f55c7dc80 | -2.59456 | -46.27941 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f3f310-5a4e-3bfc-acce-0c0dc6fa7bb9 | -1.68592 | -52.51238 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41145add-bb15-3e06-8ff6-6acf30d2b807 | -1.48478 | -53.80949 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7937f5a-8ece-3da6-bd99-e6254a4c9b89 | -1.78563 | -52.29073 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9207e0f4-78c8-350b-9097-a532925b84af | -2.86632 | -54.00037 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00a71d1-5632-3d15-bb40-4e9a82a1d5cc | -3.4344 | -52.63923 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5c3295f-fd75-3ce6-b06c-fdd4a208958d | -1.47186 | -54.48336 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3801ed1-c318-382a-a2cb-568b62beca0a | -3.30039 | -53.67016 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14047c56-8b54-31f2-9f99-773eb93695af | -3.69885 | -51.08525 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47d03e8f-871f-3f4f-97e5-4c55ea584220 | -2.69504 | -51.87045 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f71acfcd-347e-3843-8527-467f523bb678 | -3.25687 | -53.83025 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd34941a-91d6-3136-90fb-8957f7df89b7 | -1.9614 | -53.3187 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fc4c8e2-7743-3d27-8163-96b042261989 | -1.74475 | -52.78994 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36dd2710-eae7-38df-8e7f-7d7f479c33cf | 1.12997 | -60.51718 | 2024-12-04 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5669bda-7e83-32c4-ae02-9c096dca9c54 | -3.02057 | -54.03849 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e214521b-c788-31b2-8224-dc8bd3d35bf2 | -3.61847 | -52.5007 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8668dbbb-b1f8-34f8-9872-5b471ab625df | -3.09011 | -54.04884 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5b48f10-a2f6-3edd-9185-6bc75312b050 | 1.04499 | -59.52791 | 2024-12-04 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67fe9f38-8353-30e0-a548-a080782b58c2 | -1.618 | -53.89473 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d527e56d-8f0d-3b87-9543-e5266ad56982 | -2.84378 | -54.10176 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c2ed74-916e-352f-ad1c-c25f745267d5 | -3.93911 | -46.63348 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757d2758-45bd-375b-96cc-78cde7cf5541 | -2.90092 | -51.57683 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21203a47-8332-37de-976c-6c25a10bb96c | -3.26512 | -53.6207 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 38bd0db3-beb7-3667-86db-cafa53e707ae | -2.09925 | -46.58262 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eadcb478-311f-35d1-b484-3060ff782825 | -4.06302 | -46.81327 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c837e5-ed41-352c-903a-64743f34e942 | -2.10143 | -46.58292 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ca448b1-3ccc-3fac-8261-f32e4aa76942 | -1.13435 | -53.78812 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9588f8f2-788b-31e5-8ae8-f18153256a2f | -2.34057 | -53.92647 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047caf8a-c8a3-3d02-8744-614e88aedeb0 | -2.74193 | -54.1007 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c87c9b9-7c8b-357e-b329-535c3ed8828e | -3.12143 | -54.61297 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3cc5615c-4b9b-3194-a3a8-4f93043f8863 | -1.62134 | -53.89525 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a405faf-21cd-31d4-97cd-00180f6f9d88 | -3.25611 | -53.65654 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f9e1e060-42eb-312e-bb7d-9fe74b7549d3 | -2.87698 | -54.02014 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cc01425-cb79-380c-b378-e7e0a8f39516 | -2.83709 | -54.10073 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78251c3b-df3a-313e-83a6-095e1eb15366 | -2.86268 | -54.09023 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 943984aa-f555-3cc3-988f-0fda2e9c7634 | -1.99476 | -53.28278 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f939d3c7-9674-3a29-a82e-b551da4afa3c | -3.80212 | -50.9776 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 190dd464-4d9b-3014-b176-2bb2c00e14e9 | -2.86602 | -54.09074 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51a5fc21-ae6c-37b5-8248-47e5d5db43eb | -2.70753 | -54.12414 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af654876-ecbb-342c-a0cf-ff9139d35736 | -2.34689 | -54.38973 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8912939-5742-3b47-9f1c-801ad2cc627b | -2.22928 | -53.69877 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 415ac19e-c285-3b37-aeb8-b05b14fd9fa6 | -2.21276 | -53.78366 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 428e0cdf-58e0-3086-8d8e-24f97fec133c | -2.45322 | -53.81352 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e24aca86-aaa0-3189-a057-6204e232acc8 | -1.74622 | -52.61901 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 7e331e41-569e-3ef9-a0f7-dd55b33753f5 | -3.7168 | -51.79792 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d097e21-36b6-36cf-a188-ed33618666de | -2.88757 | -54.01815 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a8e2a99-979c-31c6-930f-b8544984c2ca | -3.43739 | -54.11303 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2ba7e5a-2388-392b-9f41-44d6494c0d86 | -3.26684 | -53.65446 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8919b2b4-f60b-3dc9-a3d3-99890f2621e6 | -2.80064 | -53.06265 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c8eb0a7-38aa-3660-90f5-075fc98636e0 | -3.26063 | -53.6498 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61ffd90d-505f-351e-b776-2b9133d457bf | -2.70077 | -52.91259 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5f606a7-8108-371f-b931-5566ea5be53d | -3.31815 | -50.43641 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 103f9a6f-8231-34ce-853f-2edcfd426175 | -3.72603 | -52.05985 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0881cc11-fdd7-37e8-a66e-25211a88b9e4 | -2.76981 | -54.11937 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59a06e2b-a249-3bd3-8b9b-509c827c40d3 | -1.31479 | -54.57531 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79094c6b-42cf-3b42-a247-b02bb3682324 | -2.83687 | -54.03566 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e47121-2fa2-344f-b2ce-72dc9e925b94 | -2.80394 | -55.29655 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509057b2-6036-3697-8081-aa210095ef64 | -1.34613 | -55.1807 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b46e5157-3261-343e-8cee-6bfe01108644 | -2.98615 | -53.88406 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8f240eb-c0e4-3955-b0a4-711aa1f75d6d | -3.29792 | -53.67773 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92750f6d-bc51-3af1-a93b-0f84573d710c | -2.46903 | -53.62189 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f299f20-08b2-3863-8962-c57e47cef3a8 | -3.51049 | -53.83183 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad5546a9-b214-356c-83e1-1741b6e470a3 | -3.25782 | -53.66794 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9556d2c6-7f63-33b9-a4ba-0898b7e00910 | -3.31652 | -52.14805 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 428f45ad-bae2-3579-b233-a3e3de6435f2 | -2.43981 | -54.01066 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 080f9d2a-81c3-33fb-b79a-d4d8c89aca92 | -3.06837 | -54.05639 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d9d32d4-3422-34be-9076-dd591b0ccf0f | -1.75335 | -52.80284 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b16bad1-428d-3f31-be2d-d10da52d768b | -4.38174 | -43.37532 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5994da5-64ac-38e7-ade0-4bd8dc7a504a | -1.49929 | -51.93389 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d01ebdf5-c447-3678-96e0-a25461ce1cda | -3.07221 | -54.03155 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ae03bf1-2a1f-30b4-b793-763e282f6368 | -1.70949 | -52.4526 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ce59e8c-bde3-38d4-82a4-063a6dc5e9b6 | -3.51506 | -51.30832 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79e4f218-fbee-37e3-9089-fafac4f7456a | -3.68292 | -50.25619 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bcd545f-587a-30f5-9434-7f9b2a1b4710 | -3.25439 | -53.62275 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48721c13-0103-3eff-9c2b-71964fe9243c | -2.81181 | -54.04267 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df199d81-58dc-35f6-8bb5-a8972c996a13 | -2.5801 | -54.33319 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 045976d7-e965-375b-a486-ac85ebeba1a2 | -2.77877 | -55.32782 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6be297db-5e1c-3c00-92c6-ac78b5539a13 | -1.91801 | -47.05159 | 2024-12-04 05:03:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8924aa40-0faa-3a25-9724-04c557456999 | -2.4473 | -53.69583 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9764c1f7-fba8-3d76-9cff-b9127a73a2ea | -3.27715 | -50.32672 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa804e28-ad05-3f71-af6e-a73ec535d2fc | -1.58127 | -52.25288 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a68eb8f3-338b-3b2e-aa12-35f768a03c08 | -1.9032 | -52.85201 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13d6f59b-e28b-346e-839c-54b34b945cfd | -2.952 | -53.88235 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README46.md)
