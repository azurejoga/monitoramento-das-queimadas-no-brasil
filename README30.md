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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86d86a8d-f6f5-33c3-a481-ca9a19561835 | -7.34005 | -42.49044 | 2024-11-07 04:18:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2455c547-2921-3dc9-81b5-70ca437b0ee8 | -4.38575 | -50.83689 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99640963-fb2a-3fa0-93bc-4465b3ea5d9b | -3.02516 | -53.27213 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36cf8d12-ff21-3693-ab74-e420b29a0262 | -8.30723 | -43.61308 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f04b26b3-24bb-3143-8140-4252648a0b74 | -3.19116 | -53.40084 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c11748e-ea9a-3792-b65e-f909ac634ab9 | -6.07811 | -44.72072 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64386c6d-0c05-3bd6-bcd6-37475e219f98 | -2.73999 | -51.90128 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 287a0d98-fb4b-30f5-ae19-784dc9ffd891 | -7.45184 | -43.52679 | 2024-11-07 04:18:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3991dda4-b9e8-3810-afd6-c6c28f106490 | -7.53782 | -42.84809 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c362736-721d-3a8d-917d-5fcf33b94ff5 | -2.83112 | -52.91029 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5149fa0d-02d7-39c8-9b44-5cbcb5e3775f | -4.75893 | -45.68861 | 2024-11-07 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acbe3485-73f5-3de9-8b79-f5356915855e | -1.55205 | -52.27058 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb591d2d-bfed-3585-9266-1bbbaf916be4 | -3.41742 | -50.38799 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dc6211a-6a38-33f4-89cc-e340adf36b61 | -5.50393 | -43.78733 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59e76573-7084-3aa5-98cd-1f455f96a187 | -5.93424 | -43.77196 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fae175f5-0b55-36c3-bff8-a44651c9164a | -6.46405 | -46.95925 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2e07ab3-0255-33dc-91b9-bc32e8b5686c | -2.43234 | -53.67289 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e4e6d00-bbf8-3a94-b453-0550ae0be69f | -6.13855 | -43.96478 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79b38532-ebe2-3c80-a8b7-7ce03512664e | -8.93678 | -42.59518 | 2024-11-07 04:18:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fca59a32-8edf-30d4-ae61-c8f5e30aa1d8 | -2.84908 | -48.67874 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e5221092-1f31-330b-a855-23345ff1a9ff | -3.09313 | -53.71541 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5977f8d1-c6f9-3e47-9ca4-33c7bb2f5c22 | -3.00914 | -53.43851 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c27f000-a223-310c-a82e-5e67ebd8b36f | -4.3419 | -46.77765 | 2024-11-07 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f9ff1b1-4452-3695-ae9e-ff94a594e6bc | -5.59339 | -45.20712 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f25c8e36-9e3e-311b-b710-32355bd1b229 | -3.09794 | -50.24557 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee1031ad-1e84-3686-8767-a7a1b4051c16 | -3.11227 | -51.29342 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c80a705b-86f9-3274-8160-f2cb828532fb | -2.23472 | -48.02476 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba08234b-07c7-3304-9c6b-8a7b8a9073ca | -1.4404 | -52.82852 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49e573c0-ce68-3f4b-aa85-f3e1c9617614 | -2.72043 | -54.15162 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d892e530-13fd-3b85-a974-a0cc78750f6b | -4.71222 | -49.6086 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8144c96d-4841-3dd9-aba8-163d4f17836c | -3.64301 | -51.79622 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758f9f83-bf8c-33c9-9624-5c8ffc8f160b | -6.04654 | -46.60799 | 2024-11-07 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc66bdca-b2e3-3827-9b96-6f324ea6d564 | -2.38579 | -47.83079 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50cca9ca-d6dd-3bcd-9b9f-349536569000 | -6.49795 | -44.68409 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca5199c-9005-3f99-b348-b43746a8e4a5 | -8.08744 | -44.42662 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff22fa62-b1ef-3554-aa73-def2ed97653b | -3.61413 | -54.22351 | 2024-11-07 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ee8775-9207-36c7-a132-053251414311 | -1.22504 | -54.54636 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77431980-be0f-338c-91b6-f0441d0bd5af | -3.45107 | -50.37585 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4c0efe94-f0c8-338c-8489-d1fd4abba946 | -5.39215 | -46.68695 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24a639ba-8b0c-3b35-a04b-b2c52f643089 | -2.82581 | -52.90958 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea07c742-6db5-3d9f-a975-fd47351b3eb8 | -1.22989 | -54.54379 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 896bea61-59b3-35cc-9935-3955428dbf3b | -5.61403 | -45.93319 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af67d5e-b869-32d9-bac6-d823398b1c09 | -7.9023 | -46.69361 | 2024-11-07 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9add2ecd-dd26-35cf-beab-b496bd2f5421 | -3.14686 | -44.40993 | 2024-11-07 04:18:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 168d6043-98c6-37a6-a114-ecab2d6f86eb | -6.48474 | -44.68202 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e6ce287-3196-3261-b012-05cb9e2756ae | -1.32751 | -54.64178 | 2024-11-07 04:18:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bd91b51e-b280-31e1-a28d-1c71f252386f | -4.81814 | -43.69817 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2cd2f4f-44aa-3873-a684-6372bce4e50b | -7.40979 | -44.80713 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4e47581-3bd1-3e7c-bb3c-b6b239296a9d | -3.25251 | -53.4096 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262be12d-9eb3-38ed-a83a-2a153dd1a45f | -7.2595 | -42.62379 | 2024-11-07 04:18:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f55e1db4-bc44-34a0-b05b-bc0c83754b7b | -5.61821 | -43.94773 | 2024-11-07 04:18:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1de1a125-424a-3768-bc30-3a6ce6ff664f | -2.7972 | -48.28105 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1630707-cb42-3721-a1c4-29742b26b431 | -2.94663 | -48.59671 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8d3c91c-e65b-3293-8571-a956e313ba93 | -3.53202 | -50.29304 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157d3178-2cae-3a3f-944a-adb3d0d76772 | -6.08526 | -44.71831 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34780cc5-87a4-3363-bf07-d80935f8f318 | -4.23882 | -48.53287 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7e1f7cf-c732-3e71-916d-8fd5d04ae5e2 | -4.37922 | -47.24044 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfd5f4bf-081b-3687-b065-dca5d27091e9 | -2.88182 | -51.47259 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31f5b865-8590-3544-a7d5-a2f21132ab2a | -2.62055 | -51.29582 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 64ed1d59-a3b0-3759-b0a2-59095149be39 | -5.83939 | -46.23955 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93488344-c303-3fa0-9915-8ff9e58cbf20 | -3.32786 | -50.07788 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae815da2-d11c-3f0a-af04-d4d634e1d225 | -1.14381 | -53.74183 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c428abbb-8610-3f1d-b09e-c920669185fd | -3.77842 | -47.73172 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac1cacf1-8bb2-351f-8693-9a335e553c47 | -1.4 | -54.10757 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc4b2eba-48a7-3b8f-b873-bc3f9845b48c | -3.48115 | -50.38523 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67104bdb-dbd9-382c-865f-b9f489564c36 | -2.83641 | -52.91118 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 784bf809-ffef-3312-a658-197dbf55b903 | -5.44217 | -47.68396 | 2024-11-07 04:18:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a8504e1-7af9-328c-be9f-1a68ebbc7ef9 | -1.21856 | -54.53718 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89cfebec-707a-374c-8a62-05f1d259d223 | -3.04281 | -53.27824 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ae9237-c5e4-3b29-9ea2-31762b426349 | -5.6488 | -49.39836 | 2024-11-07 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9fd2f43-724b-3034-9add-cd4adad81e37 | -2.80476 | -51.49205 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c26c5d1-4064-3823-aacd-dbf861933e22 | -5.45384 | -45.52961 | 2024-11-07 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e287cbff-7111-3575-8346-282aa603c692 | -1.52243 | -52.22445 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3b69dec-0647-3027-be13-b3e3f53c0dbb | -2.8319 | -48.46214 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88658d9c-22c9-31a1-a1c3-9a6c792dc141 | -2.70573 | -46.67805 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e42b0e2-1b76-3a91-843b-7bccd2a28c1a | -3.27503 | -50.34962 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7bd6365-8dde-3c79-8eb8-dff24d7974c6 | -3.61534 | -50.19783 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b463dd10-a8e5-3554-8b36-f43f12319394 | -2.43475 | -53.6689 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a7784c8-0ad5-3777-80f1-8c1290dc4479 | -3.66439 | -50.26041 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e769e1a6-d27d-3ceb-a0eb-d39c18380e72 | -2.96233 | -48.72407 | 2024-11-07 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7d5d4e7-89e1-3b4e-ab67-65ccbaf8e3b8 | -6.0748 | -44.7202 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0caa9077-383e-3eb3-82ea-e3237f95d3c9 | -3.54202 | -47.38579 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8dc29c7-d3fd-32ce-a236-2b5ff7123eb6 | -5.97936 | -45.55877 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ee84f57-e9f9-393a-be96-f117136a9a3c | -5.04356 | -46.84951 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5820ecec-1ce6-3789-aabb-b21ba40e700e | -7.06389 | -43.10403 | 2024-11-07 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f9adabc-1b4b-3355-8f18-ce93d4f5c5fe | -2.64116 | -45.77243 | 2024-11-07 04:18:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59f8b3ca-f7c8-3a58-9fe1-b173c3309f91 | -2.82048 | -52.90895 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d774720b-3fcc-3c54-81c4-484dfc4788b7 | -6.12589 | -43.98063 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 098b6ffb-19e9-383d-b1a9-3b42a82dcf76 | -3.24588 | -50.02408 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2576b671-ef3a-35d2-9334-b33815926b22 | -1.16334 | -53.73044 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb0965e7-d3b8-39c9-b565-12df99b4e27f | -3.00921 | -53.2343 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4268f83-e0da-368e-99aa-a054e9132ae5 | -2.40038 | -53.63316 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcd8325e-ddc6-31d4-9581-a7040cd230df | -4.51239 | -42.86583 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e24b9a6-83b8-319d-aadc-ef631a5d8145 | -4.80739 | -50.82257 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 022e1466-5572-3256-a7d3-68c1f752ed81 | -5.93702 | -43.77598 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f4355b0-7b98-300e-9d64-c022b5fa132a | -6.11094 | -43.96761 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe6165f8-05d5-3b97-8e22-26bb66b864e4 | -6.27609 | -44.73363 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc64ba3c-5d5b-35d5-b026-3945bfbaad31 | -5.7914 | -35.38839 | 2024-11-07 04:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa6edf64-e867-3b4e-8439-ff8c48fb1a04 | -2.60884 | -51.76394 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22f7f706-57c7-3e10-92ac-d488201727ed | -4.76793 | -48.67679 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README31.md)
