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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd63662f-5be6-33b5-9705-a37bb50b0a63 | -5.45265 | -44.00369 | 2025-09-23 04:17:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8177ecb-c710-3767-a806-628d652cdc8d | -4.84608 | -48.69736 | 2025-09-23 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ca39f58-de0b-3f1d-9db1-76f7ba828b10 | -4.00921 | -43.27 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 472ce2d5-6f9e-34ef-ba06-e31feb189777 | -5.98033 | -44.12581 | 2025-09-23 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86ff3485-121b-354b-9af0-a9b8afb38a17 | -3.39997 | -47.50191 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69798d53-1e9e-3924-96ce-67c009de1df5 | -2.79561 | -49.59834 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ad62b41-11ef-3efd-80a2-e781d8da27e1 | -7.03447 | -34.91669 | 2025-09-23 04:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 306eca0c-e138-3be9-a400-d71134400e84 | -4.48207 | -43.82674 | 2025-09-23 04:17:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef2b3f3c-edd2-39e0-994b-cb62cc32ec70 | -3.51342 | -49.44976 | 2025-09-23 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 64e39c3e-bfd2-319d-9205-87a168ce4495 | -5.75281 | -42.60952 | 2025-09-23 04:17:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ec7a9bb-caf0-3f7b-bb79-867cebed9486 | -4.08118 | -48.03723 | 2025-09-23 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b650620-dcdc-399f-9a1a-693e4ebfbfef | -3.85419 | -52.24017 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd355ca4-28b7-3180-a98a-372a821e8696 | -2.24892 | -47.88561 | 2025-09-23 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5908ca7-6806-390a-91eb-ba7bc33054b7 | -3.8229 | -52.15116 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 674f3186-a38b-3ac4-b87f-5f7b2f75505f | -6.55292 | -39.89457 | 2025-09-23 04:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1b5f347-7c07-3696-9ceb-7cd0d93eed27 | -5.94275 | -45.39495 | 2025-09-23 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1cc96b4-1205-3920-8589-58bec021b473 | -4.78333 | -42.76499 | 2025-09-23 04:17:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ce6dd01-2ca6-3d1d-aab4-c6dcc86b1799 | -4.30797 | -48.09669 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf996225-4938-3ae5-a26b-bd7875605df1 | -5.97425 | -44.1213 | 2025-09-23 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7134dd3c-efa4-3ce3-a4cf-4148109f38d2 | -5.73974 | -42.60366 | 2025-09-23 04:17:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b5077e7-4ae7-37db-81d9-48d3970b1975 | -4.15394 | -48.6059 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43eb838b-b7c0-3852-a20a-2280bc518468 | -5.14227 | -42.88608 | 2025-09-23 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b94f29c9-a56d-3730-bb63-c2190b5a826d | -3.64297 | -51.90651 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1219be66-62ee-3370-967a-6abefb5520e6 | -3.30289 | -42.39558 | 2025-09-23 04:17:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fe34483-da85-3355-98f6-c014adc98d03 | -2.37969 | -47.72343 | 2025-09-23 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e912e7a-9392-306f-b5e8-f31d3687685d | -6.12075 | -44.00912 | 2025-09-23 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55238b26-bf89-3695-a0b0-ab6b06a8a76a | -6.1024 | -44.4284 | 2025-09-23 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 099c1b64-e15d-347c-b5cd-f17260107640 | -4.01309 | -43.26703 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e8e4368-502f-32c8-a492-258632bf4c24 | -6.50343 | -41.54269 | 2025-09-23 04:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7974bf32-e88d-3553-8274-834cc5b1901f | -4.3082 | -41.85274 | 2025-09-23 04:17:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e922afff-b071-3013-9030-06d3411fca6b | -3.64383 | -48.32597 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96f6813a-2f34-3d75-801b-61709f4f1e36 | -4.14423 | -43.87978 | 2025-09-23 04:17:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf2f87c2-9d19-3566-9498-9971216336b7 | -4.59387 | -46.59156 | 2025-09-23 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c47b2ec-7ffe-375d-a6b9-1f78fb72c20f | -4.78501 | -43.54052 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa581d38-2f91-30cf-9ded-2e06abad840c | -4.41979 | -48.87321 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 139f83b4-eaff-3b7b-b162-442dff447c43 | -5.76396 | -43.96782 | 2025-09-23 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bc4aee6-5868-31c7-a808-87eaebd56e6f | -5.83968 | -42.61485 | 2025-09-23 04:17:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7012d9d2-07f6-361f-907b-da509120c940 | -4.9625 | -43.23069 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78d038cf-61ff-3825-b45f-3336d1ac6633 | -6.34162 | -44.02979 | 2025-09-23 04:17:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92024873-1364-32d4-b442-f36246815042 | -4.96468 | -48.01628 | 2025-09-23 04:17:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 634f95dd-e4e6-3d25-a7d4-40531199c34b | -4.76144 | -43.6259 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b436bf4a-b585-306c-bf45-6c1e82f33591 | -5.64584 | -42.6002 | 2025-09-23 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a141816-e7b6-3e3a-b838-fc9c6bb5b6ec | -5.13067 | -46.13629 | 2025-09-23 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d09b983b-27b1-3386-b2cd-f05d2bf193c5 | -5.64619 | -42.5975 | 2025-09-23 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0053c028-9e99-30af-ac23-5755af691809 | -4.87989 | -48.2996 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73b556aa-8447-3202-a2f6-4db28f2819aa | -5.93263 | -46.7098 | 2025-09-23 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c8e988-4cf7-3c1a-99b9-43273f68b01e | -3.93035 | -52.03307 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf3535eb-069e-3e5b-bf66-dced0ab299b5 | -2.82692 | -48.58944 | 2025-09-23 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b450217a-f06d-38ae-8d0c-4c24ce3c71d9 | -4.01254 | -43.27052 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 186cc9c8-a273-3bb0-95bc-cc1813dd2b76 | -2.67876 | -52.17911 | 2025-09-23 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a04957ba-45ee-31a5-8093-065aa2e37814 | -4.27348 | -48.19005 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d88543-4376-388f-bf24-a09d76f8f42f | -3.69199 | -49.55211 | 2025-09-23 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bed433a7-ef99-322b-8778-c3ee434e5287 | -4.79721 | -47.27635 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b30e084-dce5-3041-91bb-2bd290808fae | -5.45597 | -44.0042 | 2025-09-23 04:17:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29971ab6-d617-3a63-b520-af8a08869c6e | -4.96214 | -47.82225 | 2025-09-23 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d6ae83-c5ae-3fa5-ab59-fff97d7946a6 | -3.07782 | -49.46298 | 2025-09-23 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 428a1823-1bfa-3f96-8a02-897123cd6720 | -2.93555 | -48.58848 | 2025-09-23 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6840a8c9-60e4-3478-9f15-434cfbf5f76c | -4.07666 | -48.04127 | 2025-09-23 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68193dcb-ba4c-3717-8308-fc3e4faa0797 | -7.03397 | -34.92032 | 2025-09-23 04:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 590e7353-b43d-364d-85f1-e09ced3ff595 | -3.05411 | -46.92852 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80a2d62b-ead2-3a76-9cb5-0269cdda6d55 | -7.03548 | -34.90932 | 2025-09-23 04:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b86e27ce-ee15-3e2a-88d7-7ddcda8c65d1 | -5.10542 | -43.16562 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c277ec65-5fdf-3583-9ed2-70b40970bac5 | -5.38399 | -42.25211 | 2025-09-23 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4aeed10-4965-330c-937e-d24607d53283 | -5.65194 | -47.91253 | 2025-09-23 04:17:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e3bf121-21ee-39c7-803d-98c53a35b5e9 | -5.69901 | -46.39608 | 2025-09-23 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a108228d-13d2-32d3-8cc1-a411485cc051 | -3.51757 | -49.45045 | 2025-09-23 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bc8ebb38-2fa7-36af-9969-dc78b21dd0d7 | -4.15353 | -48.60416 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464fe2e3-bf6a-310c-b467-fddf9fbd3b56 | -3.81024 | -40.95873 | 2025-09-23 04:17:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2be34a99-14ec-36d7-93ab-7468872b1c5d | -3.62742 | -51.90905 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7ea23e8-0de1-3cb2-855d-b9ce97738a04 | -4.39631 | -44.37124 | 2025-09-23 04:17:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39e6b56e-48d9-3089-b7e9-a6dff0632180 | -7.03496 | -34.91309 | 2025-09-23 04:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5fa5451-eae6-3eb1-8add-eeb8a0a3b683 | -3.3367 | -46.54421 | 2025-09-23 04:17:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1c23215-6417-399b-8172-340ee189034b | -6.0987 | -43.15402 | 2025-09-23 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5212dbab-56f8-3b24-88ac-62a14390c517 | -5.12184 | -40.746 | 2025-09-23 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 918bb93a-e666-3156-8b73-b94d0f4763ae | -4.64858 | -43.37246 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2487f83-5874-3135-8b2d-4ceaebe97da6 | -2.7424 | -49.55453 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40d888a5-f686-3ca0-905a-683a13a51119 | -3.62648 | -51.91462 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e6aa6466-1c65-3319-b79b-c8b2d67166e4 | -4.84221 | -48.6967 | 2025-09-23 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f066f9b5-a47d-3f7c-83eb-7ef7caa7add2 | -4.49154 | -48.11311 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d436804b-364e-3bfb-8eb8-661ffa8c45e9 | -5.8706 | -43.67745 | 2025-09-23 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64054df2-124a-39d1-87b8-8dbcbdea4d61 | -5.23277 | -43.6958 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 123584e7-c253-3236-b027-406639c9a170 | -4.92894 | -43.42341 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be79d6e0-59b3-3b55-a68f-bf037e8b6ac5 | -5.23554 | -43.6998 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06bbf383-873f-35a0-93f9-4aae5acdcd74 | -2.25274 | -47.88623 | 2025-09-23 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e75ef651-3436-323c-aaee-6d46121fa104 | -4.25514 | -48.59733 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f289b74-8a22-33a1-9b0b-488b563676d4 | -3.05052 | -46.92794 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47cbdaaf-0f36-3b50-9732-815dc6913a76 | -4.40347 | -44.36883 | 2025-09-23 04:17:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c347406-4c7b-30e2-ad39-c14923541659 | -5.76441 | -42.58077 | 2025-09-23 04:17:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9630af5c-d356-33e6-bd20-f7bf14c7d7b5 | -5.61876 | -43.46532 | 2025-09-23 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fbc9933-3acf-3a86-a90d-b2ac4ab9908f | -4.13023 | -48.82155 | 2025-09-23 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e93bd5eb-4b29-3f5c-98bd-40f9e7aed3ac | -5.61029 | -45.19922 | 2025-09-23 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35bd5d0c-acce-3398-ac79-ea7a448f77e8 | -2.83834 | -48.83554 | 2025-09-23 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b16c378-7e8e-3ef8-83cb-10dd0edc16ca | -3.0189 | -49.21209 | 2025-09-23 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8cd788a-0e9c-3649-85be-d9de43910e57 | -3.63137 | -51.91555 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0ae55d6c-1853-3bef-b089-8169589a92ec | -5.76384 | -42.58453 | 2025-09-23 04:17:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d849dd56-4eef-3600-85b8-0f8e1b0ec11e | -2.25349 | -47.88155 | 2025-09-23 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 189c9a4c-77a4-3454-b578-af4c71f44104 | -3.85467 | -52.23725 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67a4820c-2217-375c-9610-76ce9ca2d8f1 | -3.51818 | -49.44671 | 2025-09-23 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 799fee7d-d863-3744-a9db-6601c1173f79 | -4.79654 | -47.28042 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 135dfa9c-d020-337e-a20d-a0c62c0a2504 | -6.35828 | -43.35868 | 2025-09-23 04:17:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
