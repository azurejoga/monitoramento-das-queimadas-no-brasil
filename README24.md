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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55f14a19-da4a-3ba8-a9ff-d3015a8f1f4b | -2.98634 | -51.46042 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64871ab5-4713-37be-aecd-8da5f57f55c8 | -2.6145 | -51.75083 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92c039c7-6ae3-381e-a8bf-0a22a3ec9e4a | -4.01843 | -48.28999 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f39ce624-4d48-3fbc-be67-6c9542b8102f | -1.34354 | -51.41504 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50dca53-4f8c-3ce1-b643-5ccbe71d8d77 | -3.27432 | -50.02725 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4e4f6a2-eb85-3031-a06e-c9f2f42508a4 | -2.99196 | -53.73047 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aeadc15e-fee7-3126-821d-a8a8c55d39f9 | -2.26656 | -46.47065 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c9c2e09-2a30-3ff1-bb56-490b31c535c4 | -4.2422 | -48.54786 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b3314d6-0cd6-3be3-aefa-4b905a897ade | -3.29834 | -50.0765 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa8ee9b0-ed9a-37f8-859c-bada390a30a6 | -2.8454 | -51.96981 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 350ca94d-4cef-3a40-a5b8-33c045fbd341 | -3.55343 | -47.37605 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| dac0ac1c-d211-37a1-91e1-1b148c3ca77f | -3.01653 | -53.44157 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b3344a4-099b-3f6d-9811-a065d9a35f26 | -3.69292 | -50.63242 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec928e95-c26d-3116-bc96-1323ca2e72d8 | -3.0362 | -53.27275 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7240b55d-5226-320c-9c46-84346dbd2ab3 | -4.8684 | -42.95638 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2246d033-fb57-3fb1-ab6d-57c3a6ed9a11 | -4.11021 | -48.50293 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8062a6e-ac06-3553-a059-40a049d7f593 | -3.79431 | -44.02435 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36dfa3de-3b73-3f80-9918-660960d240f1 | -4.78764 | -45.40479 | 2024-11-08 04:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0b73d5e-9ab4-3c2e-a3d7-93ee51a99e37 | -3.96895 | -48.12986 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a357e53-8e5e-35e6-9185-e9e33b7054f4 | -5.64576 | -44.25007 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b45ae1-6d00-33e0-8109-bfdf5a5c3d34 | 1.00394 | -60.58081 | 2024-11-08 04:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00caff5a-0d18-3d5b-ae6d-1d66aa981cad | -3.06216 | -53.91035 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22c6b24c-1f2d-3a97-af5e-4c79ac1269e3 | -5.43991 | -46.35582 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ab94ee1-30fb-3052-b1c6-9caa93238e84 | -1.45844 | -53.41585 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f9015ba5-f9b1-30ce-a780-8b0b8503f329 | -3.36234 | -53.38554 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e98be0f-55d6-3fce-894c-ce63506c583b | -4.37807 | -48.58298 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d5cb59d-22db-36e4-b80a-1074594e04aa | -1.06114 | -53.66539 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f55e7c2-3689-352d-a581-d2d8268e0507 | -3.55736 | -47.37674 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4a95de8e-5d5b-37e5-8015-f5153bf957a9 | -2.55281 | -54.00028 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40563399-7f51-3194-9fe5-0f5470842a23 | -4.78471 | -48.67497 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae240a35-6521-3716-a306-cf2c53ff1e4f | -1.10255 | -54.198 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72661d5a-3f12-30d9-92d0-6d59957db0ca | -3.27617 | -53.4161 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57ac8b3d-0a73-35c1-aa72-6728e5a4acd7 | -1.08597 | -54.11506 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4de9058-e935-38cf-bd48-daed9edefacc | -2.77896 | -52.87524 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e714583-1de8-37f2-9056-a4eb56a9f662 | -6.89858 | -46.28558 | 2024-11-08 04:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf20a58-b579-3415-8ecf-c697820c6943 | -3.0115 | -53.42971 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dea5598-3be9-3ea7-b933-fb2afe0d39a5 | -2.79907 | -52.94293 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 020b3995-5b15-3052-863c-27e4b86a0de3 | -4.28157 | -45.69349 | 2024-11-08 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eed89ab2-16e3-3eeb-91e0-bded2d131f27 | -3.84392 | -52.17922 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc8ab58f-5fe4-3c2a-a566-0ede26302be2 | -2.54472 | -54.00675 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ddaaf06-e768-3b5d-b3b9-1decb60683ae | -1.33317 | -54.59946 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4544aae9-1a5e-3c36-8158-c42b2a36db44 | -3.96501 | -46.46957 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6c83647-4c3e-33bc-8a0e-09fc9b0ac747 | -3.09728 | -51.2935 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1536c12f-5bcf-318f-b06c-12472716b3e6 | -2.77041 | -54.04528 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 885ff5d7-51ee-30d8-9e3e-20c48a6164a0 | -2.82198 | -52.96802 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7d48a9c-6cf2-31b8-a915-8ad6cb1c7e84 | -2.75218 | -53.22119 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06109e6c-96cf-3085-8e23-32dbab112a06 | -2.85501 | -51.77811 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a02612b1-6f2f-3f2e-8873-204ba4acb213 | -4.0614 | -48.31047 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 074df9ea-8a76-328e-a525-d5b9e90e2357 | -2.69247 | -51.68911 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f045d0-0e29-3fb9-a69c-9e0fda858b40 | -2.18959 | -53.63342 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41b951e7-5901-3b7f-912a-52af67f03ca9 | -2.73218 | -51.7163 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cec978df-fd65-3e76-b6e9-cbc5ab66492e | -2.81919 | -52.94241 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d7ec779-a5d8-33f5-a3ce-2536facd8110 | -1.36879 | -52.14624 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce14f7f5-427a-3b75-bebe-d9b0f9996b81 | -3.01959 | -53.86977 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ece6cdc-4143-3925-bf3a-d3375e0e772c | -1.759 | -52.34923 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6325e8a-ff4d-3c7d-abc4-724c2de5d369 | -2.12391 | -48.5634 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8703b3c1-ccda-34a7-a1d2-f929d0668fb7 | -3.02008 | -48.07867 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9a8440-5779-3895-ae9f-a93f6791bf49 | -2.61227 | -51.74346 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 109b3fb5-7464-31e0-8965-ab236e0f8984 | -4.68711 | -46.40791 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d554a467-f0ff-3ee1-8119-c126b85bf851 | -4.47098 | -48.11316 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e09ac189-eedd-3957-9f3b-74a9ee9894c1 | -4.61687 | -49.57669 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce4dd39-ed6f-3e41-a4a3-977d6140f261 | -3.15809 | -54.47894 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 89b931d3-c84f-32b2-9cea-5e84d08a2d31 | -2.63749 | -46.77063 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b5d13f-615e-3656-8c80-30d09e699dbb | 0.74499 | -59.77195 | 2024-11-08 04:53:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc78e3e6-af24-39ea-9d1f-53d45115d209 | -2.09769 | -47.8972 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89002608-84fd-3344-bf9f-e5e5a04326e8 | -2.6262 | -51.91415 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b6c52f6-8333-3ab0-8b6c-704393e0b866 | -3.97173 | -48.39755 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3044cb44-3f6f-3795-aa0c-e7f5f8fdb76b | -10.72817 | -49.52008 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd8fa06e-963f-3793-b144-24b4ee57eb3d | -1.34684 | -51.41555 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77576606-92ef-3220-8a90-ad0062a1a282 | -2.63588 | -46.78124 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5756033c-d18d-3033-9b8a-2a45d5df9acd | -2.61013 | -51.75718 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f07dc1c-018e-34ef-b97b-7a15513774be | -3.84807 | -46.44082 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34cf1265-359d-33f7-af6e-36ca709215cd | -5.73577 | -42.00597 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6cf8a998-f7b5-350d-9107-391431d2c3a1 | -5.21574 | -45.42786 | 2024-11-08 04:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7353c254-ce2b-3376-bcaf-506a63fc28a4 | 0.09557 | -49.86693 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15363599-9b24-3aac-bd13-5c8d5589b90f | -0.89714 | -51.7664 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb7338b4-e10e-3554-bab9-a55005c22761 | -4.77473 | -45.88898 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d91fff3a-2c55-3da1-92f9-a5b5244729aa | -1.11996 | -54.15646 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b02e64a-8461-396d-8628-fea2ba26ddfe | -2.07829 | -52.04577 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377e74d3-e806-3df5-a11c-cf85345e5ac4 | -1.15356 | -52.00014 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ac714af3-eb83-30ab-ad5f-bdbd883b881f | -2.80295 | -52.93993 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 384e67e5-679b-3e0e-bca2-12002bceb956 | 0.0413 | -49.5212 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b38404f1-804b-3bcc-a737-b3e89bb13ba8 | -3.0334 | -53.26869 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37cafb7-c42b-35bd-a62c-c16d3aa09e4a | -2.08212 | -52.04284 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e98b0189-0e36-30c5-b75b-ade7e7a619d8 | -1.84641 | -52.13666 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9c7a04e-bbc9-3d8e-9918-1b46144a2dc7 | -4.87525 | -45.73157 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a63403-f82a-35ce-8065-b637aca19c43 | -1.96055 | -52.90626 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 362faf2f-9b3f-3340-9e8f-99396878c4e0 | -2.28235 | -53.75695 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 192bc6c4-5a54-33a2-a9ff-057cd8dfd6ae | -0.38624 | -51.44397 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43d8b629-8073-3671-a93a-3e02dad303dc | 0.30102 | -51.13672 | 2024-11-08 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a03c4218-c409-3de5-b1d1-2d1ac93ab2c3 | -4.77358 | -48.67334 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51edb7a7-95ee-3744-b963-dad586b2c5d3 | -2.27952 | -53.75273 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db1ecf06-c581-3bd0-a38b-218c31e9239f | -6.39593 | -47.14481 | 2024-11-08 04:53:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a9bae9c-6656-34f8-b263-2858b6d6239d | -5.40162 | -45.13173 | 2024-11-08 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b4bf84e-b12b-30a0-aad0-647591035e1a | -2.69198 | -51.82252 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811dc758-f569-3ba9-91d7-2e93f6b8456d | -2.58446 | -51.92177 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc866d1a-4c0a-3ab0-8a0e-70ee2f880fdf | -2.83804 | -52.90946 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c86bef2-709e-34e3-8ea4-c7adf059dc51 | -1.45846 | -52.33411 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcc2c6b5-a53b-3af5-a3a4-83661a133bd4 | -3.8888 | -52.12989 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 318794fc-a68b-39ed-ba06-2ac9cce8780b | -4.51382 | -45.67571 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |


[Clique aqui para ver as próximas entradas](README25.md)
