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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae84dc93-9eec-3ceb-8f65-e3ef2bd69d1c | -2.96887 | -40.22654 | 2024-12-20 04:10:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c17761f3-697e-3415-98c8-727119503bd2 | -4.27535 | -48.09405 | 2024-12-20 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bddfc6a-eb55-3454-b9c9-b560ec6f506c | -4.92802 | -41.32753 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b1cee0ca-6a2e-3081-bc71-da5fb2c3ad42 | -3.20392 | -45.51175 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90412996-6778-3198-a461-f42444ad5b72 | -2.55459 | -46.93413 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a3b9c3c-7b74-35ab-991a-415e4cbe687c | -3.21117 | -45.51292 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16e9c52e-d145-34ce-8659-6ebe59aaab39 | -4.17897 | -42.70791 | 2024-12-20 04:10:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62a07e76-6bdb-3570-8077-21e3b34ff21b | -4.44963 | -43.8965 | 2024-12-20 04:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6fb34b3-f3a2-3fd9-a865-f8ba9c05bfa1 | -5.55916 | -43.11016 | 2024-12-20 04:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 473551fc-9670-3093-a8fd-ec5b7800ca43 | -4.45391 | -42.53609 | 2024-12-20 04:10:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 556efc91-9009-3b72-9143-692bf2af41be | -4.9123 | -41.31781 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6909b6f5-4d21-34a5-a8b2-e2936f1af73f | -4.10728 | -49.41406 | 2024-12-20 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b7d7e7-8a98-3b7c-b081-ff3ddf25ad82 | -1.79081 | -47.17564 | 2024-12-20 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0200b1cb-e112-300c-a65d-9b143178be85 | -3.86185 | -46.60264 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 191d7ec9-731c-38d6-950b-646e261b2d22 | -4.48679 | -44.32536 | 2024-12-20 04:10:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a0a1104-ce5c-3a5d-bb51-90b973d700e7 | -4.00171 | -46.55416 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6421340-d545-39f3-a992-6d5a0834eb18 | -3.08656 | -46.56589 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4769845d-afe2-3523-9815-48bc6c7f610d | -3.80647 | -46.71197 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05f958b1-052f-3654-93f7-ea0a85902fc8 | -2.652 | -47.18413 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f911a2b2-97a0-340b-905d-981feb790d01 | -4.28134 | -43.04995 | 2024-12-20 04:10:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70cd4c2f-9e1a-39b0-847f-96f3235a400c | -4.92746 | -41.3311 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 63458756-95cc-338a-97cc-5fee8353026b | -1.26249 | -54.15285 | 2024-12-20 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35526a97-315c-32b4-85d3-39d886c0cfca | -4.27657 | -46.67423 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f9e2efb-36f2-3286-a868-f117ee49cee9 | -3.77219 | -43.2406 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca5ff2b8-fb50-32e7-9e2e-906c7c02adfd | -5.98458 | -41.60638 | 2024-12-20 04:10:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d1ab6c03-e5f0-358f-9420-0bf5fce822d7 | -2.84242 | -40.29506 | 2024-12-20 04:10:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7d84e3c-882c-3945-afe7-86e7e5d8f77d | -2.46855 | -47.08609 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21add113-ddd1-3dde-b625-8a8375a8e98f | -3.17718 | -50.5722 | 2024-12-20 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5835a613-494e-328b-b866-22367bcf3afa | -2.42771 | -45.68432 | 2024-12-20 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9a14ae7-a900-320c-87c3-ca6d62eed796 | -4.45336 | -42.53953 | 2024-12-20 04:10:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1bebc47-50e1-37e8-a45f-ad5aac1f520c | -4.92691 | -41.33468 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c0b51cd-0013-37a1-a3ba-3c977a022324 | -4.00247 | -46.5495 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72e1f1f9-2ad1-36c5-bb3d-8ea37baf96ec | -5.09133 | -44.71167 | 2024-12-20 04:10:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0dabf9-d99d-303d-b4ca-07e64777dc05 | -4.11349 | -43.54945 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 877bb59e-e31f-36e9-b413-649b037f2e06 | -2.57896 | -51.92701 | 2024-12-20 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c43f90-7056-36e6-afe9-274e5c011dc3 | -2.69607 | -46.14258 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1158651d-21bc-3a7c-bd8a-37bad3836839 | -5.32788 | -43.73357 | 2024-12-20 04:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a773c48f-a105-3fe1-a84f-c9721e60db70 | -1.26174 | -54.15742 | 2024-12-20 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ca6a165-3906-35d9-9af8-e477fb73114b | -2.84185 | -40.29875 | 2024-12-20 04:10:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8a1aceb2-d91c-3058-9ad1-4e8694592be4 | -4.12965 | -43.55558 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c5b56f1-72e7-32c3-a66c-0455fc62521a | -4.33912 | -39.23598 | 2024-12-20 04:10:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea03b4ec-131e-3a91-b007-9e9bb0a822b5 | -3.22682 | -46.79776 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db38922d-563d-3382-ad57-d9d00ad09178 | -4.00552 | -46.55477 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d5355d-1b5e-31a7-98bc-08a7369fb5d1 | -4.09339 | -46.63441 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da814458-289c-3b64-a10c-4497bbe21b8c | -2.5054 | -48.05852 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 991a270c-a477-3a6e-b2d7-462495a659f9 | -3.32236 | -43.55256 | 2024-12-20 04:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 143367f1-36a1-30f7-a38d-ff03d62a2186 | -2.7626 | -45.55562 | 2024-12-20 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 082e4678-ab03-3107-b8c3-9bb1167ea309 | -4.54116 | -43.29688 | 2024-12-20 04:10:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25cb7d7c-41d6-33fa-84e0-c2304a884b9d | -3.0827 | -46.56531 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69a47d9e-02ba-33b2-b175-5e833211fba2 | -4.11187 | -49.41485 | 2024-12-20 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb6c6817-bfc3-3bcf-9fcb-b739ef35f6ba | -5.07563 | -41.68789 | 2024-12-20 04:10:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7f427402-4213-3a0a-8241-f71819e46592 | -4.11627 | -43.55349 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 029117bf-7f91-3898-8aca-400dfcfe448e | -4.43551 | -43.63945 | 2024-12-20 04:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6aa1a6e0-7030-36c5-b116-35ede5baf3cb | -3.23151 | -46.7935 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| abbe2a80-af6b-384f-b900-8e0ce62130c9 | -3.00764 | -46.71228 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63baa0ef-7f11-362f-ab0c-4dd7d8423ea0 | -4.93027 | -41.33519 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62e90bf2-0831-3279-b0e8-946f742e1e06 | -2.70508 | -46.1346 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d178565-fd9d-3623-b939-3037f7d47e2a | -4.59225 | -47.99035 | 2024-12-20 04:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21d3548d-7aff-317b-9f35-c84e705cad84 | -1.79121 | -47.17647 | 2024-12-20 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31e19883-f2bf-3455-8b33-5911e5445c73 | -5.38994 | -40.67144 | 2024-12-20 04:10:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fea4d082-abb0-315e-81b9-5b28dcd6ecfe | -4.42118 | -42.89474 | 2024-12-20 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cd408cf-7d52-309d-9699-d107566c7064 | -4.11293 | -43.55296 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6477adb8-33c1-3590-899d-ed438f475c9b | -4.24399 | -43.20052 | 2024-12-20 04:10:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18a1456d-427d-3580-bed2-e52cd1dda03b | -2.85763 | -45.49966 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4350834f-98b4-30fc-a29c-ed0b754c8565 | -4.93563 | -45.09614 | 2024-12-20 04:10:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1d3a852-7a84-3bd0-ac6a-fd31f817b436 | -2.55856 | -46.93482 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 696988e6-4361-363b-9950-675f8fb17147 | -3.2401 | -46.78986 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 546eba8e-7006-3fa7-be54-c36aab7000b0 | -3.22995 | -46.80327 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 867272a2-8d24-3748-a91e-e003d97b53bf | -2.76921 | -47.38947 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65e49eea-e1e7-318d-90f8-15b5be98ce2f | -2.65335 | -47.18109 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836ebef8-aadf-3a07-b3ef-7c398a82361c | -2.674 | -46.11086 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277b2f73-31bc-33cc-a394-00f71ce164b1 | -4.24796 | -41.92367 | 2024-12-20 04:10:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7255bf8f-75cb-3e50-bfe3-6b998a32d120 | -2.67835 | -46.91366 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed06d5b-eec0-3e61-9cf4-c13b499b566c | -4.91566 | -41.31832 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f42172e-7627-38f9-9aa3-f8f670fc1b32 | -2.69985 | -46.14318 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb1d0f4f-32f7-308d-80e3-be4a747b2c70 | -4.85717 | -41.34967 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17c4e134-15cf-31dd-a6ce-f48f4517d040 | -2.76513 | -47.38881 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 814ea18f-73ed-37e0-9278-b79e649d0a98 | -5.05789 | -45.773 | 2024-12-20 04:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c753976-d9d6-3783-a5e9-f34ee21b882c | -3.00453 | -46.70676 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79a52e99-b295-3465-a9f4-e2392b449eac | -1.28165 | -53.18577 | 2024-12-20 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2346e05-b317-3d06-9248-01c10d9aa948 | -4.12018 | -43.5505 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aceac2eb-b37e-358c-b92e-f18463404c0b | -4.30288 | -43.76809 | 2024-12-20 04:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cbd62e9-3567-3598-a7a3-10af2deb063a | -4.11571 | -43.557 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5235d915-6cfe-321c-b46d-0a1cd9591df3 | -3.08391 | -46.5676 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f14f7b00-dd70-3403-9799-58ad692788b2 | -4.27276 | -46.6736 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7c05249-6e1b-3b25-9c50-40fbd345dc5c | -3.2362 | -46.78922 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6083430c-e67f-36cf-a8cb-a720fb2271db | -3.99791 | -46.55353 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffdb8439-358d-35cc-ada8-cf8238e1911f | -1.7949 | -47.17626 | 2024-12-20 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1000d4f-b792-364b-a0b0-05d0543eba59 | -5.09169 | -45.83756 | 2024-12-20 04:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3aca92-c449-37a7-92b3-adc1c368c404 | -2.46239 | -51.84391 | 2024-12-20 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b0287e-fd8b-3f1d-80ea-e50c62cdcc23 | -4.92972 | -41.33875 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09129787-b58f-3896-aa9e-80eba34b81c0 | -3.23854 | -46.79966 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62e5b5ed-2381-303f-8cd6-1d45356088da | -4.13309 | -46.15553 | 2024-12-20 04:10:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a394c5a-623e-35f6-80e8-51fab0e9d983 | -1.28088 | -53.19047 | 2024-12-20 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f61a7b4-0308-3777-8c5a-789b4a3a5598 | -3.23385 | -46.80391 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 02c0a428-dbd2-360f-a00c-a990d69eb3ce | -3.22604 | -46.80267 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0762a752-94d9-3d55-a927-8d27c13f4070 | -3.22761 | -46.79286 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| af87ecd3-72e2-3355-aad4-5eed0e0e4fd7 | -2.50819 | -48.05831 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f85d265-6845-3c55-bdb7-916b9cc21dd0 | -4.92635 | -41.33826 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95999561-89ff-33bd-8cec-ac2ec6effef0 | -3.22292 | -46.79713 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README7.md)
