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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9abbabbf-1eda-3de7-8d91-ff66b7621327 | -13.6935 | -41.3685 | 2025-08-03 00:40:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 83.9 |
| e18f85d6-b09d-3042-abe6-ba3eb7f94bb1 | -4.3196 | -48.1125 | 2025-08-03 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1b71d4eb-3af6-35c7-8372-e73823876395 | -18.8407 | -46.4417 | 2025-08-03 00:40:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 451bf0bd-4949-3d60-bb65-faf26acc196d | -6.6741 | -59.1746 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8091c308-6764-3ba7-9032-24abc002be1d | -6.6376 | -59.0988 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0b9cd834-6846-338b-8fc3-e4935ad8fac8 | -4.5497 | -44.2047 | 2025-08-03 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a5eccb1b-3b42-3c53-8946-196f4bdf8ceb | -12.6789 | -44.4851 | 2025-08-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| d731d328-e492-349c-ae4f-76163e3ec31d | -6.656 | -59.0981 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |
| aaa69a5e-0ee9-36b2-9b14-4803d5547eef | -6.6559 | -59.1174 | 2025-08-03 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| a6743b3d-2433-3565-84f9-ef787239e511 | -4.3197 | -48.0908 | 2025-08-03 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 25556a10-55ff-3874-888f-3b7e4d2ab9d7 | -13.6935 | -41.3685 | 2025-08-03 00:50:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 26c948ba-1bc0-33a6-a104-11e2328635b4 | -18.8407 | -46.4417 | 2025-08-03 00:50:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5e7b8977-0c6f-361b-b123-6cbca25697dc | -6.6559 | -59.1174 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 68cbdbd7-b4e1-3892-9d3f-95fe95a1c975 | -12.6402 | -44.4913 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| f108991c-23fc-3909-a504-efcc02484a51 | -4.5497 | -44.2047 | 2025-08-03 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 30d60b32-13a2-39f1-a5c9-51d67b210783 | -12.6398 | -44.5148 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 691ffcb3-9cb1-32b5-8a26-de23dd157b2e | -4.5684 | -44.2036 | 2025-08-03 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| c5df472b-af83-3dbc-bec9-108295efef0f | -6.6742 | -59.1553 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5f4d0735-a9c6-3968-a16a-81ee9b117607 | -6.6741 | -59.1746 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 52a098c9-a589-331f-bc3e-79e2433563eb | -4.3196 | -48.1125 | 2025-08-03 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 08886210-7fc4-3fb4-803f-9b96d9daf555 | -12.6789 | -44.4851 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ef4c4202-b0ee-32a5-80c4-bc1a1c27a4dc | -12.6209 | -44.4945 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 42ec8ebf-efd2-34a2-a178-0138dd147535 | -12.6595 | -44.4882 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 9827740d-bfd1-35d4-adc5-2f7c098c1345 | -6.6375 | -59.1181 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f05bda6c-48be-3cc3-bd95-dd30992cbc77 | -6.656 | -59.0981 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 54158e14-4429-3f72-9c17-84cef6d5e027 | -13.7131 | -41.3646 | 2025-08-03 00:50:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 5be90ca0-62c4-3b3e-bd67-529de8c631d1 | -12.6591 | -44.5117 | 2025-08-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0fb63ad5-17e8-34d1-bdf9-c805c943009b | -15.5513 | -54.2674 | 2025-08-03 00:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| bfb6dd6c-6e94-317f-8c4e-4a66857d7a3f | -6.6376 | -59.0988 | 2025-08-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3bcec065-0d6e-38de-a7ff-71b74c6964bf | -23.7228 | -51.6495 | 2025-08-03 01:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| f92afb6c-2393-3028-bbb3-cd07fee74dfe | -4.5684 | -44.2036 | 2025-08-03 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 23528470-7b9c-373b-9c0f-890c76fd5230 | -18.8407 | -46.4417 | 2025-08-03 01:00:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 4bccdea7-2854-3bfa-a84e-e0ffa9410ba4 | -6.6742 | -59.1553 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 041c0e1d-f3cd-3e73-ab73-64eb8018bf82 | -6.6559 | -59.1174 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 299818b2-c554-3171-908c-d4b2af713c93 | -12.6209 | -44.4945 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 703f9bd4-0983-3126-8765-08bc62d79510 | -22.029 | -47.5843 | 2025-08-03 01:00:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 211c19e3-3de7-3e06-8822-39455ff15b70 | -12.6591 | -44.5117 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8a4cd771-9bfb-3fdb-957a-b41a274bce12 | -13.6935 | -41.3685 | 2025-08-03 01:00:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| beb55bb3-f9da-3a3d-8510-93807d704d2d | -13.7131 | -41.3646 | 2025-08-03 01:00:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 43.6 |
| a45bc488-efea-33a0-8306-74f6572d880e | -6.656 | -59.0981 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 68705c7e-eb19-3070-bdcb-60a13f3af66e | -12.6402 | -44.4913 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 3d74889a-0af3-3823-9055-c996905d65cd | -6.6376 | -59.0988 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 64528a3b-5682-3948-bbc3-573694cd8b99 | -23.7017 | -51.6543 | 2025-08-03 01:00:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 654e6369-cf02-339e-b9d7-0e8b420af943 | -12.6789 | -44.4851 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 61038bf4-698f-3aa7-8fb6-4fd2afb5b76d | -6.6375 | -59.1181 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ecc8ed28-7a9a-3248-9811-c2233ec22287 | -12.6398 | -44.5148 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 04978bf6-87f1-33fa-a3f6-6ed48da79cdc | -6.6741 | -59.1746 | 2025-08-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b0633551-7c57-3938-a7c9-d154eb94b65e | -12.6595 | -44.4882 | 2025-08-03 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 52e8ddc8-7df7-3830-ae44-e1c35673cbb4 | -22.0297 | -47.5605 | 2025-08-03 01:00:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 404e88f4-edca-381e-96d9-2cf5a5478949 | -4.574 | -44.223999 | 2025-08-03 01:08:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad9e1fe-1791-31d0-aed9-a48ffa242fd0 | -22.0362 | -47.569199 | 2025-08-03 01:08:00 | METOP-C | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a0735d9d-11f6-3a2d-b5a5-aeb3e317e3bb | -8.045 | -43.138302 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bf56502-6b88-3a02-ae11-f9346ccfc109 | -8.0339 | -43.173901 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a235b1e7-d198-3e49-826a-e4395529ce53 | -22.292601 | -52.119301 | 2025-08-03 01:08:00 | METOP-C | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9d29979-490a-37eb-9a95-5c5f00a4af68 | -18.854601 | -46.449799 | 2025-08-03 01:08:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2e2541b-cc1a-3d08-8276-23eb8d975010 | -8.0083 | -43.115398 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca2a1696-fd15-33c5-b89f-29a4e1c80458 | -18.8515 | -46.437599 | 2025-08-03 01:08:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3a1889d-9c65-3066-8469-bf4c49f32be2 | -4.7818 | -45.340599 | 2025-08-03 01:08:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af9fb135-5533-36e1-b196-1ec3d9cd83ec | -4.5761 | -44.192001 | 2025-08-03 01:08:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccedd93e-0908-3d1a-801e-7ade3cfc43e9 | -8.037 | -43.1077 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ee04e30-367b-3497-80d5-3660c3201071 | -6.6771 | -59.172901 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbeb2f7-ca48-348b-bacf-2f1dac75353f | -2.9104 | -54.159698 | 2025-08-03 01:08:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb50974-3203-3766-8740-bda052f3d30b | -23.1388 | -49.986599 | 2025-08-03 01:08:00 | METOP-C | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ead68fd-4407-399c-9b87-670bd442921b | -7.9731 | -45.108501 | 2025-08-03 01:08:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 804f64ad-c195-3af9-aced-31ff0c19099e | -6.6232 | -59.9524 | 2025-08-03 01:08:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34798dc5-d5cb-3cd5-8f49-50d0493f788b | -21.458599 | -55.106499 | 2025-08-03 01:08:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe8d1eff-be37-3bc5-8069-43f4db76e50e | -18.8449 | -46.452499 | 2025-08-03 01:08:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a317700-4afb-3e79-9a5c-5794802141b2 | -22.291 | -52.1119 | 2025-08-03 01:08:00 | METOP-C | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 376e8920-72da-3cfa-8f20-ff821808a4b5 | -4.5644 | -44.226398 | 2025-08-03 01:08:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c634e61-72c3-3550-a6a1-e62b72ecd63a | -6.6849 | -59.1618 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dda89cc9-31c4-3b5d-9387-2902a18e8ded | -27.181299 | -53.407398 | 2025-08-03 01:08:00 | METOP-C | VICENTE DUTRA | RIO GRANDE DO SUL | Brasil | 4323101 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5bcaec57-c2d3-33d1-a076-87467549723e | -18.841801 | -46.4403 | 2025-08-03 01:08:00 | METOP-C | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 00ae4669-734f-3912-ad78-43392d9d3a29 | -6.6732 | -59.154999 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a503b341-3ef1-3995-b1ff-7061ff1df195 | -4.312 | -48.102699 | 2025-08-03 01:08:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f781c2-ffbe-3252-b2e7-b7c38138dbd6 | -24.223 | -51.861301 | 2025-08-03 01:08:00 | METOP-C | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7e81610-b29b-34c3-b2f3-ecc1a99a3c3c | -9.4027 | -45.505501 | 2025-08-03 01:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cffaa49e-14e9-390f-bfcb-015315f649a7 | -6.6254 | -59.962299 | 2025-08-03 01:08:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f04fa05d-d969-38dd-b4db-70826072db7e | -9.4638 | -57.838501 | 2025-08-03 01:08:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b43e37d-3425-322d-acc7-604e758ab938 | -6.6496 | -59.094898 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 140926fc-1f68-3634-9571-e498105f27c5 | -24.2327 | -51.858898 | 2025-08-03 01:08:00 | METOP-C | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70d6db0b-2094-3f5f-91ad-aaff7d587976 | -8.0465 | -43.105202 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6bc250ba-7a9e-3d92-bc3f-0758d1a7808c | -22.038601 | -47.5788 | 2025-08-03 01:08:00 | METOP-C | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7101a53a-1e4e-3125-abca-1ada90d26c4d | -8.0227 | -43.209202 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17640475-f01f-389d-8dff-f619c6bccfc5 | -8.0244 | -43.176399 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a59d417c-3c17-33a6-8bde-03d0f78b2423 | -8.948 | -46.751202 | 2025-08-03 01:08:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d79398e-8904-3e6e-b421-a3dbce4e2dc8 | -8.0052 | -43.181499 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9478dd02-81dc-3c26-9d7e-5b0a640fd8dd | -6.683 | -59.152901 | 2025-08-03 01:08:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dfe028e-b60e-3ed0-9758-a443bbd9c29e | -29.1826 | -50.065399 | 2025-08-03 01:08:00 | METOP-C | PRAIA GRANDE | SANTA CATARINA | Brasil | 4213807 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21edc6ea-bb2c-3794-b135-9b655a6a8e69 | -8.0274 | -43.110298 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9cbadb2b-e31a-3255-9518-8bd20cc85252 | -22.3515 | -47.541801 | 2025-08-03 01:08:00 | METOP-C | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28e22366-1c62-3ab6-a20c-5d9872be0a20 | -21.468399 | -55.104301 | 2025-08-03 01:08:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5be963-1314-35d6-b49b-9675c7f525c3 | -23.717501 | -51.663502 | 2025-08-03 01:08:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4793a955-35f7-3545-a6ec-a6f509197a0d | -7.9972 | -43.1511 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86198a88-afa4-3f7d-971d-70b2cd7d48b9 | -8.0132 | -43.2118 | 2025-08-03 01:08:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f758165f-c841-30a6-a678-1ab0ce41cd16 | -8.0259 | -43.143398 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a90706d4-7a08-3c2c-b8e1-0a9ce2fab9bf | -4.5666 | -44.194401 | 2025-08-03 01:08:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7257ea39-0534-3e5f-ac1e-2a13086ba668 | -27.1705 | -51.212002 | 2025-08-03 01:08:00 | METOP-C | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 941db58d-1223-3520-8b36-44a869367d77 | -18.516399 | -45.667801 | 2025-08-03 01:08:00 | METOP-C | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| edf1e029-feb6-3d2a-bccd-e209af6e524e | -23.7159 | -51.655998 | 2025-08-03 01:08:00 | METOP-C | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd294ff3-5a9e-3438-84b7-05a08a65577e | -8.0163 | -43.146 | 2025-08-03 01:08:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README6.md)
