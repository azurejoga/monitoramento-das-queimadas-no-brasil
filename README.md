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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 654d6796-c842-3dc1-9178-9c0eb0cef368 | -4.1112 | -45.7018 | 2025-12-16 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b65c486c-2d7e-3437-9149-350034896c99 | -1.6777 | -45.8091 | 2025-12-16 00:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b1647c6b-c16d-3b93-8721-54a47ce187f5 | -5.1174 | -43.2898 | 2025-12-16 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c137cde1-947d-3d0d-9055-7f7234de0c3e | -1.6637 | -52.065 | 2025-12-16 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 42850481-3cfd-3efd-87c9-bfaef424e424 | -12.3074 | -57.3608 | 2025-12-16 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 34067f8f-be33-36d1-9b8b-c63cbbee16b8 | -2.0846 | -46.1782 | 2025-12-16 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7bd09f0e-bf4c-3861-b3f8-703c99ea54d3 | -1.6591 | -45.8095 | 2025-12-16 00:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8e1d2cf5-3cf2-3a5d-9e66-5788b4386455 | -2.0301 | -45.8236 | 2025-12-16 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 96aaf19d-5fce-371a-812e-e72b957bb590 | -3.6542 | -44.252 | 2025-12-16 00:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| dd2aa825-0330-3d16-a438-374fdf27a57b | -1.22 | -53.717 | 2025-12-16 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 51d9f53b-03dd-3b92-ba3e-e8321ce1f44d | -2.0847 | -46.1561 | 2025-12-16 00:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4637429d-b874-3081-816e-50c4b70ff56c | -2.0301 | -45.8013 | 2025-12-16 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| ddafc960-1f03-30b4-8b2c-564a7ee887db | -4.6564 | -42.4048 | 2025-12-16 00:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 00153b0d-2352-3126-a475-42ff6463042b | -1.22 | -53.7372 | 2025-12-16 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 844e121a-8884-3dbf-b29c-679f462a8e20 | -3.6356 | -44.2529 | 2025-12-16 00:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 02ec49e6-87a0-3e90-96f2-74d7facf18f5 | -16.0616 | -58.9778 | 2025-12-16 00:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| e53d122e-a79a-32b6-ba44-971c48076da4 | -16.2383 | -58.8395 | 2025-12-16 00:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 80469c35-945c-3611-b714-4ad3054ed998 | -24.36491 | -49.43057 | 2025-12-16 00:07:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 532b1c24-e606-3407-9703-8ffd5c0098cd | -15.13741 | -41.83659 | 2025-12-16 00:09:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| c93c90a4-0eaf-318d-926c-dbabe7ff9a75 | -13.43088 | -41.32381 | 2025-12-16 00:09:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 5afeb3cd-22bb-3654-9fdf-9fbee0cb286f | -19.50706 | -39.81273 | 2025-12-16 00:09:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4599a369-f90e-364e-92fb-84cc4916fa54 | -15.46372 | -39.15048 | 2025-12-16 00:09:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 79133fdb-7dcf-324b-b2c3-dc2aa6114c97 | -12.82239 | -43.81903 | 2025-12-16 00:09:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 58b103a3-1014-3744-8454-143f53e84047 | -4.1298 | -45.7009 | 2025-12-16 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6bfbe1da-cc25-3b90-97f6-025fcd7fd96d | -4.1113 | -45.6794 | 2025-12-16 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 79caa8dc-cdc9-3686-af59-9952dc6bd5d8 | -1.6637 | -52.065 | 2025-12-16 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 92695592-7e4f-324f-abbc-7f2b33d61d6b | -16.0616 | -58.9778 | 2025-12-16 00:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| a0b1a6b9-238a-3c0a-966a-83625f9516cf | -4.1112 | -45.7018 | 2025-12-16 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 62cbee06-f69b-3134-be28-59f35c1140e0 | -4.6564 | -42.4048 | 2025-12-16 00:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| f4f43619-1396-3b83-99dd-8edadb558979 | -2.0301 | -45.8236 | 2025-12-16 00:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4d1cf939-8126-3d4e-89f6-294bfc58d862 | -2.0301 | -45.8013 | 2025-12-16 00:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 80b4f615-b56a-36fc-baeb-30858ec3855a | -4.1111 | -45.7242 | 2025-12-16 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 52e09f40-e89f-31d2-85b4-178875a24df6 | -3.6542 | -44.252 | 2025-12-16 00:10:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 766ca031-4dc8-3497-9387-e8069571de5e | -12.3074 | -57.3608 | 2025-12-16 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 07aba08e-1249-31bb-96b3-48ab1fa95bc4 | -4.66003 | -42.3915 | 2025-12-16 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9514498f-9c25-3581-937e-41e49a4870ca | -10.77521 | -44.46347 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1cabed4-d29f-386c-890a-6bbb883c05d7 | -5.75903 | -40.50581 | 2025-12-16 00:11:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 4e4ce496-7670-37fe-ad08-c6df68f26aa1 | -12.04263 | -44.23797 | 2025-12-16 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5ef5188-68e3-3f84-b439-9ee2325d7d89 | -11.7556 | -44.03215 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b951f44c-77da-36d5-ae96-b6d3cc031245 | -5.19395 | -44.29857 | 2025-12-16 00:11:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 27b9e001-a98e-3915-9adb-0a7473441839 | -9.61391 | -36.04155 | 2025-12-16 00:11:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| 2d2da603-2b02-3940-94c2-a6b70e686b91 | -8.72744 | -50.249 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6c7380af-b818-3345-9586-d3b08d210c08 | -5.27631 | -43.63889 | 2025-12-16 00:11:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b65a6598-b6ca-3d34-a087-1dac91e00705 | -11.04983 | -45.39608 | 2025-12-16 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ec91634-0618-3dad-a704-770441feb3ec | -9.5596 | -44.93416 | 2025-12-16 00:11:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 379ad6a4-9ec0-3164-acf1-bd210acbcd34 | -7.49696 | -47.03051 | 2025-12-16 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d7acbfc6-931b-3a09-8f11-6307547e864a | -7.61129 | -47.0569 | 2025-12-16 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7a5af31d-f2cd-3395-82d6-4d50c7006db4 | -9.12075 | -44.4305 | 2025-12-16 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 12e6af6e-eba2-3ebb-aa6c-d5d901c8f838 | -9.1664 | -40.51318 | 2025-12-16 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5fec359a-3754-3b51-8f60-a22e335dee24 | -5.50281 | -45.12817 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a9f35489-3c0f-3855-814f-7a62997a8b44 | -9.83486 | -44.73072 | 2025-12-16 00:11:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10a895f1-103c-30d6-a875-3d6f4a0daf1d | -5.94894 | -42.53651 | 2025-12-16 00:11:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| efaa33b9-2300-33d6-a771-a3b08df9877f | -10.48141 | -44.61275 | 2025-12-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a218fe1f-d620-316c-b777-c23f473cbbdc | -5.48428 | -45.38459 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8309853e-2d79-304c-a2b7-992cb7c5d974 | -8.41114 | -44.03957 | 2025-12-16 00:11:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f62dc0e6-e21f-325d-bbf2-4168e565cb45 | -9.16861 | -40.52732 | 2025-12-16 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 34.3 |
| c4c18c13-6ea4-32d7-ae8b-89f6bae7f6d5 | -4.65887 | -42.39768 | 2025-12-16 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 417d8cd1-b738-30fc-bcd4-7caf76d24581 | -11.88606 | -43.71395 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 993a3c9f-1266-3ef4-9c7a-c1449b6d5684 | -4.53117 | -40.77161 | 2025-12-16 00:11:00 | TERRA_M-M | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c8f9bfcc-2852-3a26-bc7e-0362fdf93865 | -11.85124 | -43.73475 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f873dcb3-a2ac-3a40-9ef4-f6787765c0ae | -8.6671 | -44.22294 | 2025-12-16 00:11:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c6532f48-561f-31a8-b0e6-df3ffb4fa7f6 | -8.98773 | -45.9397 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6111cab7-af8f-3aca-b31c-f6aad6e34f3f | -9.16485 | -40.51995 | 2025-12-16 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 4010154f-af46-3863-8319-a0862a7b5d74 | -5.49167 | -45.43768 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 785373a6-48f6-3341-9b11-b0f6862a0009 | -11.89495 | -43.71262 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a212cf89-225f-3d6f-b4df-6882d92fd95e | -7.61851 | -47.05014 | 2025-12-16 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1fe8444f-99a7-378a-966d-31f888fee6a8 | -10.76647 | -44.93542 | 2025-12-16 00:11:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b0a7975-bb92-360e-9519-c407049da8c0 | -5.47914 | -45.4124 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a861d6af-b118-396c-a01f-bc0105d05f9e | -11.93571 | -44.0025 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7b504bcd-40fe-3a04-b14c-076a53da09c0 | -5.49312 | -45.38331 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9425d963-e51c-38e8-bb95-53df3880df08 | -10.80791 | -44.50431 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e16b41a5-857f-34b1-8de5-6bf417415d73 | -8.4188 | -44.02903 | 2025-12-16 00:11:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4ec64df7-7b37-340d-af01-ac3df66c2039 | -4.65149 | -42.40512 | 2025-12-16 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e737a697-a984-3b45-81a5-01879130a65c | -9.79687 | -43.93175 | 2025-12-16 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3fd6c9c8-781c-3e0f-ab29-3866ef053601 | -9.56083 | -44.94306 | 2025-12-16 00:11:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 535e48fb-a7c3-3d10-a6cc-2a6d045e56c1 | -8.98649 | -45.93063 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 482d6e72-016c-3df3-b3f0-30230bcb5556 | -5.47791 | -45.40354 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23c66217-904e-37cf-b47f-619e1b75f50f | -10.9998 | -44.81967 | 2025-12-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c069174c-a817-34e3-91f3-3bf3d920e21e | -12.16971 | -44.35957 | 2025-12-16 00:11:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28e95534-0ccd-32a4-b7cd-281497131090 | -4.66173 | -42.40361 | 2025-12-16 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 906c7071-193c-34d6-a67d-9cb84786a126 | -5.71742 | -46.20892 | 2025-12-16 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ac3c5b2-c051-3339-97e3-a531c2f53930 | -11.93445 | -43.99348 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9d41cf9-fb00-3209-958a-3613fe388030 | -11.89367 | -43.70352 | 2025-12-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dbe1915f-a62e-3261-998b-2324587808c3 | -5.57918 | -43.75986 | 2025-12-16 00:11:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77a557dd-4ffe-3d68-9984-c971aa3ced82 | -11.88478 | -43.70484 | 2025-12-16 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 50d6c70a-5793-3b8c-a607-81660de64004 | -10.60428 | -44.83432 | 2025-12-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9562ad90-25cd-3e98-8195-786c4cf93619 | -4.66065 | -42.40975 | 2025-12-16 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 94ab15bf-5b14-314c-bba1-100469e53cf3 | -8.42011 | -44.03823 | 2025-12-16 00:11:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 71fe1478-5042-3e30-b170-5a7b1db1a4c6 | -11.14887 | -43.32694 | 2025-12-16 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| afc1cb9d-549c-35df-afff-685ab86eba48 | -8.42777 | -44.02766 | 2025-12-16 00:11:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bf282fc5-76ea-3dce-bb9f-f79e0259f6f6 | -9.16696 | -40.53412 | 2025-12-16 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| ed9e294e-af32-3b36-a3cd-d39b29b58637 | -10.36536 | -39.12703 | 2025-12-16 00:11:00 | TERRA_M-M | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b20232e0-b9a1-393f-af82-82d641e86572 | -7.14585 | -40.09624 | 2025-12-16 00:11:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 31.8 |
| a6a3a344-95ab-3d17-9d67-3674b0443076 | -3.64767 | -44.25623 | 2025-12-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 758b8523-eea0-3ec0-b01d-a8e867cc6225 | -3.64629 | -44.2465 | 2025-12-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 97664996-10bf-3c0d-961f-72d0f76085b8 | -2.47646 | -47.02604 | 2025-12-16 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaad8a97-621b-3c16-9c91-bbf6c8112888 | -2.90332 | -45.38468 | 2025-12-16 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7f2ed285-11f7-33c2-ad49-afe58986d25e | -3.40817 | -49.21185 | 2025-12-16 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 195e3e90-e52e-3132-a019-81040a2be6e5 | -2.61817 | -45.65947 | 2025-12-16 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d407fc3e-f8e6-329a-bb98-fb030062b794 | -2.92624 | -48.22557 | 2025-12-16 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |


[Clique aqui para ver as próximas entradas](README2.md)
