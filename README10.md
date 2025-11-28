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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fec6afe6-779a-34ed-bc2a-f9609358b70d | -2.97378 | -49.22023 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 423657d3-813b-3227-a048-8d9993ea520b | -5.35097 | -44.88152 | 2025-11-28 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4a9143f-f2be-385e-b295-72e6e62f24e2 | -3.86893 | -40.64437 | 2025-11-28 04:31:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39230ee7-f26e-3003-a596-60957f1fb500 | -3.23761 | -50.59705 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eca26823-dcbf-30c5-af8b-8be9de27dc41 | -4.93825 | -41.14392 | 2025-11-28 04:31:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df2273f9-c14d-33aa-9233-5f2fe4175f23 | -3.60841 | -52.61904 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 502ac5cf-603c-3b2f-bcae-eeb6e7031287 | -3.52838 | -51.63647 | 2025-11-28 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66eed902-b2f8-3bd3-9e00-8b43d00273eb | -3.76653 | -46.95693 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d9e7979-83a3-3894-8c64-17d1964f1b89 | -4.94435 | -41.19429 | 2025-11-28 04:31:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 404847d0-1bc2-3398-941b-73056dcd9d1c | -2.1613 | -50.62697 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45879391-4c6d-3da0-8ea8-a722302808eb | -1.36242 | -55.44149 | 2025-11-28 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66494ea4-090d-3626-85ab-01347f9ab895 | -3.84265 | -50.31534 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1613df4-96f5-3eb7-bf84-e6eb3c9f5e0d | -1.83742 | -55.34822 | 2025-11-28 04:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0655fef8-49ec-3306-a846-c7d7492fdb66 | -2.49124 | -49.03085 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed8aa8c0-52ce-3d65-9edf-43a95b787102 | -2.70828 | -47.41364 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f8ebe02-0def-3f35-8168-6135454da151 | -1.48082 | -54.2036 | 2025-11-28 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a522ab5-5c35-308c-869f-60e186ebc502 | -3.5125 | -43.68737 | 2025-11-28 04:31:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a9c8f69-cac0-3aab-b37b-5044bafdc32d | -4.27235 | -50.5316 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be572410-c7a7-3633-9381-56b20b08fd44 | -2.99401 | -45.42451 | 2025-11-28 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e93379d9-2527-3a13-ba07-518652a0c473 | -2.23075 | -47.50837 | 2025-11-28 04:31:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ef80ea11-4aba-3f25-84be-19e80e2ac134 | -2.8395 | -52.39782 | 2025-11-28 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfcf4b91-a571-357b-b79b-851e2b05c5f9 | -3.56248 | -52.07469 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33f402c-c33e-3903-83ff-af2a83896ca1 | -2.42442 | -45.74748 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e4f87f-55f5-3678-84d2-98a474bf021c | -3.76268 | -46.95986 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08a6abb1-970a-36ee-b741-505636f6d099 | -2.86754 | -51.7872 | 2025-11-28 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05b9702c-b0f8-3bbe-8ec2-2f5c78c16162 | -2.96161 | -48.58931 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d87d33dd-17d2-366b-be2f-55a3669e5188 | -5.43161 | -43.05124 | 2025-11-28 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faa69415-65c8-3895-96ca-301426e2defd | -7.45447 | -34.81562 | 2025-11-28 04:31:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 862c0a8b-a780-384c-bf92-a01eeeeb72d5 | -3.62738 | -53.6504 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4df68119-4968-31f3-b3be-0ddfc2ca58fe | -3.96077 | -50.19621 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad738cb-20c2-3c08-afa0-01d4fb377193 | -2.69504 | -49.55819 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ff94610-2c40-3443-93f2-9ee3b327d187 | -2.01513 | -51.9395 | 2025-11-28 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2edd81-efd5-3fe9-92b0-041ed0da705d | -3.06386 | -50.36765 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 069b0048-222e-3f0a-8ce2-9d74dbce2772 | -3.29734 | -42.4284 | 2025-11-28 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e022fc1-e9a2-3a0f-a9e1-18efa537f7e6 | -3.08824 | -40.65669 | 2025-11-28 04:31:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c0da57e4-6445-3412-ae95-8c72b3e79e92 | -5.04779 | -47.44069 | 2025-11-28 04:31:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f03aea51-2391-3e97-ae31-6e2e7728ccd6 | -3.93257 | -50.16697 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76c8c32e-7458-349b-b276-6de4551bd958 | -2.83304 | -46.72575 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3242e435-91f3-3e5d-978c-2ac28ef3adbf | -2.89869 | -54.00401 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f630424-2096-371d-ba2c-b35470282db4 | -5.76287 | -46.4323 | 2025-11-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a88717ce-a127-3649-b725-87b9a4a112dd | -2.99003 | -43.84488 | 2025-11-28 04:31:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2517eab-dc9c-351a-a01a-a67ad4bb1d25 | -5.54454 | -39.2377 | 2025-11-28 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63326145-fd41-33ee-b21f-714a2d5be99f | -4.34404 | -48.45604 | 2025-11-28 04:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1313f35e-56be-36bd-ab7e-0184b098a2bd | -3.8262 | -50.1058 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 243761c8-dc09-3d10-8f82-552d9c53e738 | -5.06721 | -43.89701 | 2025-11-28 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b91c0c8-4c1e-30fb-b1dc-1c365b3ae9ca | -3.3895 | -50.25355 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc36202d-ea94-38db-8b34-fab788f63f02 | -2.96402 | -51.02843 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 674c8b8e-018a-3927-b4a6-3eb9034a388a | -6.57488 | -47.89819 | 2025-11-28 04:31:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 982df6e8-8433-3a76-8b5d-3ca8b30caa81 | -3.22555 | -50.32173 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d5d54dd-63fd-3113-966d-fc86e7e36c95 | -3.76706 | -46.9535 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba23ebec-7fa1-3fd4-b6f1-617dd270cf8b | -3.84926 | -47.05854 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231c65e4-9b88-3d30-9da3-2bee4048a6ed | -2.50222 | -45.77021 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aef54731-22de-3746-996a-51d56b643ffd | -3.17923 | -48.61181 | 2025-11-28 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca87063a-945e-3cbd-84c9-f2fcd8065b58 | -4.57877 | -43.29925 | 2025-11-28 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ceef392-de43-32da-9df3-f5af1b974bee | -6.91972 | -38.62423 | 2025-11-28 04:31:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 048a4a2c-73b4-3336-a4df-72e5de2e4975 | -2.96408 | -51.02571 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6bbba92-0d92-37ff-8ea5-49272a1bb9dc | -2.93394 | -49.44789 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 114e242c-fd0f-3faf-b250-0a1f5abe26a9 | -2.43778 | -46.36049 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd463d48-41fb-3aed-821e-5afdeebbdf49 | -3.27874 | -53.76169 | 2025-11-28 04:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 974d222d-eb40-3be6-a3c4-cabe9f4a7319 | -3.43601 | -50.16849 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f87802-7e36-3040-981b-fef2f8f11e57 | -3.39015 | -50.24942 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64554347-92b1-3b73-a935-ccb970836260 | -3.75769 | -46.94852 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e954e53-c065-3c01-a6fc-df3da344523b | -2.65902 | -46.9695 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c014f83-8c79-3471-b398-dda35afe424e | -5.43944 | -43.05236 | 2025-11-28 04:31:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c1b2b3f-404a-3d58-b2c4-1bcaddad5ba8 | -3.53661 | -49.94358 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42610674-3115-3b24-b1e9-4884ad7b0c7b | -1.49627 | -54.7074 | 2025-11-28 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a34005c-4cb5-36ff-8707-eec1db14b29a | -3.95318 | -44.76667 | 2025-11-28 04:31:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 517389f8-15b7-303b-adc9-fbdf149b1373 | -3.22984 | -50.31813 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38ca932d-d499-3c7e-b76f-2c9f1c033752 | -3.40842 | -53.30818 | 2025-11-28 04:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fe3c924-6313-3e29-8515-6eaf60a61b8f | -6.71823 | -40.81465 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f3e9436-1c8d-3628-af01-f30295b1e7a5 | -2.84137 | -49.52516 | 2025-11-28 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fefe0aac-508c-3446-a479-e754c3a2ef34 | -2.8106 | -46.76101 | 2025-11-28 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cddf224-93d4-374b-b375-47acd75bc107 | -0.86299 | -47.66123 | 2025-11-28 04:31:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 545f4756-a450-3cf4-9d95-45c0937d9374 | -4.56881 | -50.50016 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3528d81f-0437-39c0-bb8c-b5a05562d194 | -4.97687 | -44.81927 | 2025-11-28 04:31:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37014cf1-6671-3db4-ae96-6fe9e968d8c1 | -3.43149 | -50.03473 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa245f21-16cf-377d-af68-1a7f2d12f3f1 | -5.2105 | -43.91649 | 2025-11-28 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bc7797e0-5370-3e58-a401-901d5cdf3e3c | -1.90942 | -46.28104 | 2025-11-28 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 11e69e6e-d8e4-3a72-bab8-5124ec6d48d0 | -4.94283 | -41.14238 | 2025-11-28 04:31:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d656141d-267c-37c9-921e-ac61ccbd3c2a | -2.42162 | -45.74342 | 2025-11-28 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70953615-be71-3a6f-8976-a9a4e6361a73 | -6.72618 | -40.82545 | 2025-11-28 04:31:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cf4d5500-e951-3a64-8d6f-d2bb86f81581 | -3.72342 | -43.45119 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d90e64b7-7678-374d-b1d4-2505cd5649d9 | -2.27502 | -45.83225 | 2025-11-28 04:31:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7031638a-b4ea-3c80-bb7b-c768a1819323 | -3.85249 | -47.03791 | 2025-11-28 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99bdd4c-4f27-39d9-8414-b9dab84d4f9c | -5.45151 | -50.75554 | 2025-11-28 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7265f375-9ca0-3438-a440-f31a33e3ee41 | -4.37373 | -55.71421 | 2025-11-28 04:31:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d19f8d-5250-36a4-aefe-45e82d4602e6 | -2.21364 | -51.37622 | 2025-11-28 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a16a7e24-dbf2-36eb-9917-38b92d5d3427 | -3.77411 | -50.77991 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc114419-0b85-305f-a3f0-547c354be1bf | -4.56816 | -50.50428 | 2025-11-28 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f877f6ea-4657-3f5b-8880-6be7ec63fc0d | -5.76531 | -46.43232 | 2025-11-28 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0051bb07-6af3-3178-bb2d-d5e7baab0f34 | -3.75277 | -46.95832 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47370855-2427-34b0-ab85-bce449530da5 | -3.74946 | -46.95781 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 475a969f-90e1-3fe2-aa48-3a4b3e0d1fff | -2.98989 | -49.11897 | 2025-11-28 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27dcc1fe-31ea-3d17-8164-93562511c021 | -3.92499 | -46.5292 | 2025-11-28 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be12eff4-0fbf-35cf-b7c5-f4db8c4991c2 | -2.62618 | -47.35138 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41a4c155-936f-3d31-bf66-9f66d1d6ae5a | -3.34301 | -50.26744 | 2025-11-28 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cded69df-becc-3620-987c-d89fee2ef771 | -3.75554 | -46.96228 | 2025-11-28 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0578c95c-2f08-37db-a816-4b75858a8f9a | -1.64444 | -52.03935 | 2025-11-28 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd38c394-9d0c-3213-9791-5a3d09ed730f | -3.69515 | -43.47569 | 2025-11-28 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a70898f-65f3-319c-8e1e-98f0f372b891 | -2.62395 | -47.34399 | 2025-11-28 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
