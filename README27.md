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
| e3d7db19-51d2-3da9-83af-98223a4dc9cd | -14.8901 | -48.079 | 2025-10-25 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| c0df1c1e-6b14-3ed9-86e1-9708c6208961 | -2.8149 | -49.1354 | 2025-10-25 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| afb7863e-0af3-3524-897b-49c2a016c097 | -14.8701 | -48.1047 | 2025-10-25 04:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7f49806b-3b2f-3f2a-80fd-449194c2a50e | -2.7964 | -49.136 | 2025-10-25 04:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 5d0721ed-08d6-31b1-a810-bb1da0757e75 | -22.3098 | -52.2708 | 2025-10-25 04:10:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| 0b90c93b-cb02-36ab-af3b-6c6f1e2fec1a | -18.1714 | -51.7466 | 2025-10-25 04:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e20fd9f8-5423-33ff-b5ee-3bc0722440ec | -4.8399 | -50.9345 | 2025-10-25 04:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c280f0cd-2046-36cd-92d7-4cb7ccecfb2f | -14.8706 | -48.0822 | 2025-10-25 04:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a95448c4-dcb1-3b8f-b9aa-dca5f658ff73 | -6.50852 | -42.303 | 2025-10-25 04:17:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 27149827-6af0-3df7-b274-fbb0da9eeb13 | -3.82967 | -50.19591 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 18d2988f-a3c6-332f-8184-5c0997c567b9 | -4.8531 | -46.73241 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02b08fe2-1227-3380-b7a0-d2232e1f5c8f | -6.33433 | -41.71781 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65ef80fa-5502-31c7-b625-787e0220dc6a | -5.43498 | -45.86055 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75b119c9-6bff-3f63-a96c-8c1a8c845566 | -4.8601 | -46.73347 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02b6f6ad-40ea-3c22-85e8-873e71dbf445 | -5.8866 | -43.20078 | 2025-10-25 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9dad9fba-a801-3900-aff3-4b5ac6f8f5e1 | -3.47438 | -49.97503 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9563c021-8225-32fa-9625-acc660436a54 | -5.12257 | -50.61842 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5b601ce-cb7d-3d53-baa8-39b6d23bbc33 | -3.1452 | -50.16185 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2904eb46-18a1-3b89-839b-9ac454b6570f | -4.29053 | -48.26734 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16645894-a7e3-3e5e-b04c-cda9baba9f2d | -6.42872 | -42.02284 | 2025-10-25 04:17:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40eb5a6c-cf22-357f-bf4f-18d2cbb7e39e | -2.80902 | -49.14189 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 28c7a604-c3df-358f-9727-cf6e0fe8fe43 | -5.45025 | -45.40935 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af92e29e-eb89-3ea0-9b2f-ea2f60d47f4f | -4.70225 | -46.44016 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2905ff1b-5a0a-3104-a914-23a932819428 | -4.10068 | -48.02374 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c930231-43cb-317d-96a1-4343d9b9cdec | -3.11843 | -49.10784 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 36ff5947-6b24-368c-b2b0-0e00eca04fba | -3.86479 | -51.89683 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 298cb657-3868-3e02-8945-703aaf921fc7 | -4.55397 | -46.6823 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9dab5a26-256f-3343-95bb-05abba52935f | -4.2085 | -48.60641 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e4cb53a-f2c2-3577-ab49-19b2e5712dd3 | -5.93642 | -43.36466 | 2025-10-25 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbc2caf5-35ba-3005-8dbe-8e627348e480 | -2.85881 | -48.67788 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eb29f39-e76e-3b61-a6f6-ffdffb70924f | -6.09731 | -43.70267 | 2025-10-25 04:17:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 554bfa39-48ee-36ff-90fa-de8caffe5a6b | -6.43282 | -42.01949 | 2025-10-25 04:17:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3073b41d-bf27-3ec4-bbcb-ce138f59a8a6 | -3.94287 | -48.08786 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbaf1fd2-b46e-3cf4-837c-c81571ef945f | -2.86562 | -50.7166 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1bcb9ba-f53f-3ad7-9d21-ecf1d10b635f | -6.10063 | -43.70321 | 2025-10-25 04:17:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f80af33-7b28-392a-94b2-f301a4063bda | -3.47946 | -50.0784 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff61dd98-7851-363e-a974-b4bce5dc0ae5 | -4.24527 | -48.55163 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f12cf3eb-1d62-3300-85c7-7499428eb2d4 | -3.47877 | -50.08258 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36663820-8071-3629-8e84-b935bc845c7a | -4.24165 | -48.55304 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 797d4ce6-45eb-3c82-a6b2-86ffce288860 | -2.26458 | -47.84788 | 2025-10-25 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7cbd2fcf-8b80-372d-a5f2-9eaf9e3b19e0 | -5.13353 | -41.20005 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 117aadb7-b607-3bff-9aee-0f0e8da161da | -2.89632 | -49.16679 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1b231b5-a646-3bf0-880a-b16ef7896042 | -4.33105 | -47.8923 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce3d5ae-ddcf-3578-9ce9-eed1d219a86a | -5.54468 | -46.52881 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 746eef11-c317-3e0a-b050-b9b31e3c029f | -2.80782 | -49.14937 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3134b227-d24a-362d-bf9d-65d73674440d | -3.58108 | -44.8765 | 2025-10-25 04:17:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a2aa9de0-a305-3189-8136-101615b87012 | -3.72132 | -52.44454 | 2025-10-25 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e334e601-15dc-39d8-96e1-6735e3bc501c | -6.36152 | -44.27048 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db6b244a-316e-37e8-a61c-3fc58be2d80c | -4.09936 | -48.95231 | 2025-10-25 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45826b3d-f55d-3ef9-aea9-344413a16059 | -6.41002 | -43.76557 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90e4a673-1cc1-363a-b2bd-01b4ce568ed4 | -3.14043 | -50.62058 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7321b741-d2bd-3f6d-91c8-76100b7004fc | -5.69199 | -46.28713 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098c9112-020e-39ec-be51-37c5d120c46b | -3.1356 | -48.6252 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0814cffc-4b7b-380a-b3ca-4d79ae05bbb9 | -5.54449 | -46.52466 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11787527-7251-333a-8ef0-0cf395683278 | -4.22786 | -48.6117 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e03e1361-5b2c-3889-be02-2f26a1f6b97b | -6.35767 | -44.27342 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 439b37e3-31f8-3a83-a06a-de6ab10ecc82 | -3.78036 | -52.03093 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81d1a52d-f872-38dc-827a-25cfb31f3415 | -4.82777 | -50.93383 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84398310-06d6-369f-8a81-b25fecf5c405 | -5.0202 | -47.15638 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81282637-1a8c-3205-b618-8f3b4938c4d1 | -4.26924 | -50.51164 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39b0bfc5-e5b2-3b99-ab1b-29063735c03c | 1.43522 | -50.89368 | 2025-10-25 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f8fe1d1-bb33-3a03-8fae-6ebae70223f3 | -3.91752 | -47.69134 | 2025-10-25 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9090f077-e09d-3e0b-ab5c-2e5c854147b2 | -4.22478 | -48.60616 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65d9d09-908a-3f16-aefa-bc84e7f214b0 | -5.51334 | -46.41578 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f4d0dd0-ce85-3455-85b1-12fb33ef910f | -4.48573 | -46.47794 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa17c6cc-6cc8-3acf-9297-f3794f0ad7ae | -3.15134 | -50.46029 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696ee1bf-53a5-3a0e-b0ae-ca6f18bbf10a | -5.47029 | -40.87817 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45b889ec-0eee-3957-8dd6-164b19e91bfc | -5.54923 | -41.34267 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27731cc4-6a5c-309d-914b-a26bd98727ad | -2.17447 | -46.56062 | 2025-10-25 04:17:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2532d636-0bbe-3584-a0cb-1e57d7b304f5 | -3.69801 | -49.00565 | 2025-10-25 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66113594-31e8-34d3-9d1e-fbb752d721a5 | -5.59717 | -45.19189 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 262be26f-2696-3164-9ec9-0b90484d98af | -6.12649 | -41.72969 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be01b1fd-88a4-3ec8-bd65-8d74963bb25d | -5.64493 | -45.97189 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04c4b781-9204-355f-a68b-20ab59285778 | -2.80549 | -49.13744 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 6c4c8db1-076b-3bf7-a53f-72e2835cf002 | -6.10346 | -45.84836 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e53622f-7dfd-350d-bfdd-041741abbce3 | -6.30703 | -40.93486 | 2025-10-25 04:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 979ef49a-2eae-3807-90b2-7821707cac42 | -5.01733 | -47.15165 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 428a381c-11b1-3db6-83c8-0fd2de770625 | -2.86102 | -50.71585 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9625492e-d724-3cb1-af9a-85fcd7b6338f | -3.2646 | -50.14958 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4203e35a-8488-3f2a-9f6b-df9156d9caa8 | -2.80369 | -49.14868 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2929a98a-c2c6-37e6-9076-14b19ef1772f | -6.04649 | -41.77897 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a409013-ac6e-313e-a97b-59f1ff175335 | -6.55045 | -43.23374 | 2025-10-25 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 44ef618b-3884-368f-b4d8-a1998f3d7d79 | -4.25149 | -38.69859 | 2025-10-25 04:17:00 | NOAA-20 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 586de5e6-3ac0-37db-ad8b-302849b8180e | -6.32026 | -41.85838 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c1da852-bbf4-314b-82a1-22822be22063 | -5.37541 | -40.71325 | 2025-10-25 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae5e1363-580b-3998-9ccd-c075687b1f66 | -5.45359 | -45.40989 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53c8ef24-4892-39b3-9c62-53e1f91a1334 | -4.70571 | -46.4407 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3133f865-cdf3-359c-be96-f44973065c27 | -2.72619 | -49.16771 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf40225e-fb4f-319a-b6d9-7fcfd925802b | -6.31733 | -41.85389 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aeaabc43-477f-35d0-812c-213e26941241 | -5.03681 | -41.19459 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07f62882-c007-3990-a395-4690a0d47ccc | -4.25726 | -44.57717 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3f5d5b6-61fa-320c-b24e-eb2b1f2e0efc | -6.31966 | -41.86234 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 66e28e84-5d94-3a67-b1ef-952f9bdfe2cb | -6.35821 | -44.26996 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f175c1f1-7783-33df-bece-9acafeb11e36 | -3.46306 | -41.31314 | 2025-10-25 04:17:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66142e44-e564-38d8-98f7-a6ecc841fdec | -4.8566 | -46.73294 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f4c2d3b-dec8-3b11-9f32-04a93164780e | -5.46176 | -46.47284 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53c09f84-15d2-3625-a814-10102abffc69 | -2.66953 | -49.12399 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33090667-f2c3-3e6e-85eb-07266979f337 | -2.72499 | -49.16262 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3c7e7e8-380f-3a7c-b8ac-060b340a1c06 | -6.33788 | -41.71837 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 132e193b-76ce-375b-b67d-bc2363e6c23b | -5.54239 | -41.38745 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
