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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dff2f2aa-b5f0-313e-a284-e64e46c5e983 | -2.3233 | -46.8786 | 2024-11-29 04:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 26afd56b-9770-3c89-beca-53b11a227899 | -1.6081 | -52.2912 | 2024-11-29 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 305dbcda-1070-3dda-93d9-f2471a366be9 | -2.9844 | -53.2819 | 2024-11-29 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 188945bc-c2be-3e80-a5aa-216e07afe6b8 | -2.3419 | -46.8562 | 2024-11-29 04:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| acefd12a-ea4d-3936-8ab3-2d895eb8d752 | -2.6684 | -48.7767 | 2024-11-29 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 85a4382b-3968-3640-8465-afc4f2c31666 | -1.5897 | -52.2915 | 2024-11-29 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8d798a10-6735-3ad7-9769-1444dee17eb4 | -1.092 | -53.3954 | 2024-11-29 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 11e03413-9cf3-3c75-ade1-25f18934e1ce | -17.5805 | -42.7483 | 2024-11-29 04:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8e218d5d-b394-310b-81a1-2cf3bff9bd03 | -2.6498 | -48.7986 | 2024-11-29 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 0279c643-4076-3dab-a9df-948d08d1ca1e | -2.3419 | -46.8781 | 2024-11-29 04:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 8800b829-a0dc-39cb-8420-6adcd75fb822 | -1.6997 | -52.433 | 2024-11-29 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 628b97f1-b0cf-3572-a0a4-5786ce017e61 | 1.8399 | -55.8218 | 2024-11-29 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aaed4a48-57c1-398d-ad02-e40cebc4f57f | -2.9844 | -53.3022 | 2024-11-29 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 9a13fa65-7970-3ddd-b8ed-939c4fa40c9c | -2.67 | -48.79 | 2024-11-29 04:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0bc9364-1905-3f6d-9bba-e5c37e9ddc4c | -1.71711 | -52.49773 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a39e5e0-a457-38ce-a082-865db7d673ee | -3.95209 | -52.20606 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 634eeb5d-6f5a-3a38-9320-fa09fa631815 | -0.98911 | -51.72715 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38a2f093-570f-3804-a162-57a9b300803d | -2.86355 | -45.53815 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1392f147-2e8b-3a3b-9f0f-19d1abb008bc | -3.98037 | -46.7322 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7184760b-b9d8-3685-bf15-2ae9e7d7f617 | -3.54187 | -50.18745 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd186564-827c-3741-9bc3-7c4e96d0dc71 | -4.07185 | -50.03454 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e5aa5a2-a58d-3feb-beb3-40c123142e43 | -2.88459 | -51.58672 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ccb578-8dd9-3e90-b302-7fe9040623d4 | -4.06931 | -46.82402 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db14084e-5ed0-30c5-a7c5-39fb19499da7 | -1.53615 | -52.67163 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b960a4b1-b4f2-3bc8-9d84-096bc9181bdf | -2.26442 | -46.44191 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c2db46c-12d7-3b84-9134-3da4ff75af61 | -3.26116 | -49.898 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86ea219c-877c-3f5a-b7fd-60afd6373bed | -3.91363 | -53.67559 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0827ba87-235a-36f3-82b5-ca4cbd1e7d82 | -4.06505 | -46.82323 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c249370-4829-3a98-9a18-091cfefdb272 | -3.89782 | -49.81913 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 324449a9-19c5-3b35-b0d1-806a221c7b86 | -2.65447 | -48.7974 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4d379413-2456-3e2e-b426-1ac6560705f5 | -1.96181 | -46.44143 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fb452591-27be-3ea1-8d61-13b378934efe | -5.50488 | -46.25415 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16909ed3-afce-37f7-8310-284583b864da | -5.12211 | -45.15276 | 2024-11-29 04:04:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdc4882a-52d4-35ef-ba6b-120efee93c26 | -5.72223 | -44.00227 | 2024-11-29 04:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ab70084-14dd-3c01-b986-7f1b99f1de2f | -3.46748 | -50.53204 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| acac079b-06b0-3eb3-8ed5-3913f805e1ea | -4.84019 | -41.2572 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66623ec8-9cb3-3ee6-bd6e-49e685376dc5 | -4.74339 | -45.78327 | 2024-11-29 04:04:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6000e3-9cd0-3ce3-b0ae-e0c2af50a52d | -4.67249 | -42.38311 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 37a3bcae-1f2f-3286-8084-375cab8777ef | -3.82545 | -46.53893 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2aba21c-d7aa-315a-be0f-971d99bb0fd0 | -6.54487 | -40.49806 | 2024-11-29 04:04:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a97f63b5-41bb-3b79-adc4-a543ae16e346 | -2.06688 | -46.37869 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e41a06b4-d627-3222-b873-8bbc0b0048ef | -3.10026 | -53.8157 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c099be-c3d0-3265-9172-5f08ac11ba78 | -2.83761 | -48.09316 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a63f34aa-488c-3c39-83a2-6464e1d8ce93 | -2.84177 | -46.80541 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f43bdec-e0ca-3c14-b458-0437e3bee69e | -3.24691 | -46.15604 | 2024-11-29 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1408dc-1325-3bef-9979-1ba80f72fd4d | -4.41248 | -42.13836 | 2024-11-29 04:04:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ddd93e61-8be5-3037-be7f-1e1ba4cdf2bc | -1.33056 | -51.93637 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba43a346-426e-3eed-a1d7-129d70f2feca | -4.09276 | -48.48935 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6b3c138-38b1-3543-8c20-f7ce27ee286e | -1.30388 | -51.95953 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e8accb0-ce05-3aa8-a88f-384ad53acc91 | -2.87624 | -46.84112 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 222d139c-6f8e-3086-a675-4c55f218db8f | -4.16986 | -44.26981 | 2024-11-29 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37c73813-53ac-3fa9-b7f5-2d77381de783 | -3.52728 | -50.48232 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feabaec1-3b8b-3d48-850b-7a03d02063b1 | -1.67658 | -52.50184 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 620199fe-5425-3eeb-b109-2e3f7c22e583 | -1.20655 | -53.75604 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 076aa556-1971-3a77-a8aa-cd0221f005cb | 0.97952 | -50.12687 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77eea9e8-2b8b-3830-bd6c-bb158e7a785f | -1.59773 | -52.29448 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c63262e4-9f58-30e9-b956-2b60f996c161 | -2.95092 | -45.72111 | 2024-11-29 04:04:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d17a0e93-66bd-3c19-9e66-34ff0297fcef | -2.26377 | -46.44592 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82872ba5-1658-32dc-866e-24707131da14 | -3.93819 | -46.69661 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0a30a0-db39-3010-b9b5-d5a6193b780c | -3.47303 | -50.53297 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8835822-ebd3-350e-a6ce-985c6ca1adee | -5.89506 | -35.41022 | 2024-11-29 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fae4e3ef-38d6-34aa-b0d5-1224021a87c4 | -2.82184 | -46.84524 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a97943-2d52-3d8a-bedc-3219cf06dc46 | -5.55579 | -44.38463 | 2024-11-29 04:04:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1baa2da-dca2-3c32-9b1f-f7670f90bc91 | -3.46409 | -43.53701 | 2024-11-29 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7667185-7d2c-357a-b249-6e43bd0b1d07 | -3.8593 | -50.15143 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d65990b6-fa53-39e4-aaf5-ee5acbc2e4b3 | -1.19174 | -53.87564 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 595bae7d-ec7e-3cf4-9da7-0347d613c725 | -1.2103 | -53.76575 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b4130dd3-efc0-3ac9-bf57-3b489b1c94af | -3.91777 | -53.67585 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 164819bb-b617-35ea-9696-c71ff50f8efc | -3.11031 | -54.48518 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0360772a-d58f-3b9d-9a0e-67a1eb7c2b81 | -3.25013 | -50.62375 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23c7875-8721-3234-94c1-8a50c5ea6c0c | -2.6554 | -48.79167 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 145f7a87-e7f8-3fda-8325-d3925f9ebda7 | -2.33917 | -46.87431 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c50b9a74-be5a-3b3e-a1c7-5afaf06535e8 | -4.01348 | -45.96144 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41d57300-35cf-3bfc-a825-b4fe6cdbd6bf | 0.97953 | -50.12871 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7af6630-c838-30e2-85eb-fd90b01e6a1f | -5.93976 | -40.02827 | 2024-11-29 04:04:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29d74e97-f7da-391c-ae59-5f35a8caa42d | -3.86075 | -50.15662 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c34f98d0-f04e-38dd-af42-b321ae902426 | -3.42248 | -43.20947 | 2024-11-29 04:04:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d5fc15a-02d0-3c5e-9f20-a25213f89f49 | -2.65041 | -48.79076 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8407ddd2-bba4-3c15-9ee7-dae0046ffa79 | -3.58716 | -51.14788 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43ec8da3-31e3-308c-be9f-4a7ca5e06d4d | -3.70041 | -47.12563 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69547b56-04d5-346c-98fb-210f1d2b55ba | -4.03316 | -42.30171 | 2024-11-29 04:04:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2afd2ec6-2d74-3cd4-9c3b-92a8d07fe5e5 | -3.2709 | -50.62538 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7f25258-069d-3fcb-ba6c-bf9b6a68c7ee | -4.00008 | -49.97425 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 834aa957-f9fa-3c28-a452-2bdaf0839620 | -4.15053 | -43.81691 | 2024-11-29 04:04:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| deac91d0-84bd-3392-825a-034c665f40d3 | -2.97824 | -53.28061 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 49fa65cd-eebc-30d4-916b-5f7635ec5d58 | -3.01269 | -47.80197 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f16bfdb-03ee-3f63-9d6d-9c676b5d12e7 | -4.7875 | -46.1237 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eba3199-f6dd-31d4-8889-a4bf1f70ff34 | -4.40305 | -47.26853 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2c4529e9-bd76-353c-ba57-26e3747b6cfc | -1.78262 | -52.74667 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9a9bc29-5b7b-3fb0-97e5-d778692b686c | -3.38408 | -50.12165 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d89297c3-5aed-3ae0-83b4-1995975f73fc | -4.84073 | -41.25375 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 70d33aa5-b5c0-3716-ada8-8131af611882 | -2.57742 | -51.92691 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b5cc3dd-36d7-3d04-8f19-ac96f5cceecb | -2.93918 | -48.34176 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f66b5001-79d9-3c98-bf8a-c23c356c1f0c | -2.67712 | -46.27348 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d630e01-db18-33e2-bd03-a3a502d68d40 | -5.91898 | -45.54739 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9504758-85b4-3c0b-b9c3-8f177bf4d00c | -3.82112 | -44.04074 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c5ace3b-4c97-3c50-adf4-dc8ab36f7f83 | -1.59686 | -52.29971 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 7fa856d4-318c-39a9-a77e-e6d2590251aa | -4.09331 | -53.98272 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7b91f09-7ad7-37a8-a6b5-9c6d0f62c834 | -3.37313 | -50.82708 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1db2ff2-52df-3ef6-819b-10c21b5dd96e | -3.56784 | -53.02527 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README23.md)
