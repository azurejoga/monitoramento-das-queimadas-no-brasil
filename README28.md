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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c336d21-2ab8-3228-8132-28d74a7d8330 | -6.15656 | -46.10498 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b700bae9-0488-3226-a481-5e18da021806 | -4.23565 | -46.34321 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61ae73d-f121-3f49-813d-003f85b2fcfc | -3.25936 | -49.57042 | 2025-11-18 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed131c2a-1c03-3034-825d-2c04caf3eee7 | -5.48253 | -44.69005 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5b9fb9f-f8e3-3eda-86d6-1723e47101ab | -7.85789 | -46.86517 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3eb716-cfe1-3fb2-a945-eceec9e2b9aa | -4.84033 | -49.39237 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02435ab4-3c48-31fe-9c9e-b2ae578aa5fc | -5.17295 | -44.34042 | 2025-11-18 04:21:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aae529f8-3d8f-3582-8602-5c6b0d75f272 | -5.09652 | -41.47173 | 2025-11-18 04:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3bd5c97-3ad3-3994-8d1f-7fa1c67190be | -7.04129 | -43.96482 | 2025-11-18 04:21:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3643c85-0da9-3dc8-b614-6bff7938fd79 | -3.79909 | -50.12534 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82567a28-c7de-3f69-b50e-5bdc965e9d19 | -4.23599 | -44.58803 | 2025-11-18 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccbc8a55-db51-3398-9d64-72dc4d379557 | -4.23653 | -44.58458 | 2025-11-18 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c29fd3-49f8-3372-b858-0a33c9948b90 | -9.74573 | -43.94789 | 2025-11-18 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80767974-d251-36c4-a518-58863778132d | -5.46202 | -40.97695 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28512d35-a443-3cc5-9f5f-4bdfa3ca6e77 | -4.97001 | -41.85174 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0f45caf-577f-3936-8448-1367cf856419 | -3.79039 | -51.10438 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0658ddd-81a5-34c5-bae2-9f9ae7db0b6a | -4.23159 | -46.34645 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6afa22eb-fc33-368c-bfd1-c6c0e597abb2 | -6.67621 | -40.89405 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 85e92a15-91b9-354d-bce4-5d38277b67ba | -10.76608 | -44.18226 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54b87c23-3435-313f-8c97-6bb1387a1c4c | -3.79843 | -50.12945 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c77d933-a901-370f-a088-30d045b77c24 | -7.16924 | -40.65288 | 2025-11-18 04:21:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cb8f71d9-cefe-3c14-9d52-4de0b2e5787e | -6.67183 | -43.76018 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52937e78-7ee4-31ab-892b-5bc9a3048d43 | -10.87446 | -49.54444 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dca4546-cd52-31ff-ae98-7069771efa1f | -7.1051 | -48.71669 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 776fb87f-6999-3496-847c-aeb2c00ffd3b | -6.67611 | -40.7932 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4d190e4-c6ab-3962-bffa-b2fbe3e9994b | -4.65027 | -46.53954 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a0a0765-a285-33ae-90b8-e181a568c9a0 | -6.30668 | -43.78965 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1178fe03-5dc1-3a74-9414-3db2ab5058f7 | -6.86456 | -47.20825 | 2025-11-18 04:21:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64ab9f12-c867-34e9-be6c-63fbb75253e8 | -6.34796 | -41.74525 | 2025-11-18 04:21:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 83db0f75-d4f4-3f84-83b8-db679726de53 | -7.43284 | -45.20196 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bfd7559-135d-3b96-a35c-3d4da6292209 | -6.55528 | -44.46425 | 2025-11-18 04:21:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27f9df77-942e-357b-803d-194438e9f036 | -3.28301 | -51.4288 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 730a76d7-f6a2-36fa-9428-a77c8536c682 | -3.23496 | -50.50753 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 901c6041-e373-38d0-9b61-bd900d0d7ebe | -5.20201 | -43.30526 | 2025-11-18 04:21:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2d1ce11-8d7b-369a-ba40-785db7c96d2b | -4.50837 | -45.97992 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3443f45-a2ec-3206-a200-0f3688229895 | -10.6854 | -44.27028 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce6a5321-d8e0-3d69-bf24-3bce4756105b | -5.40311 | -44.06651 | 2025-11-18 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6a3fe13-3112-3973-944d-dc2a1a75fc89 | -5.73969 | -46.29402 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa74be9a-efd2-3d34-9213-0f50ae3a59bb | -5.07894 | -49.83947 | 2025-11-18 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c90b109-25fd-3f94-976b-6626393d9367 | -6.67052 | -42.0306 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6246e2c9-5418-3e12-87c9-7cbc3ec6ac07 | -9.21718 | -40.51522 | 2025-11-18 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85bb4fef-0cd0-3d8d-a6d8-4c9e662f0dd3 | -8.30115 | -42.25891 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f9b0773-2226-3f34-9914-b8d7c43371d9 | -6.64472 | -43.60475 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fc977aa-fbf5-32f0-a100-28a58bbaec8a | -11.01914 | -45.23807 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db90ae33-149a-3aeb-84ad-e1dbd154a1c2 | -10.79533 | -47.64329 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33801393-dbdb-3c7e-9647-a315a43b9945 | -7.86131 | -46.86572 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 253626ec-cd45-346b-9d56-0f2e0022b8d5 | -5.18838 | -46.07504 | 2025-11-18 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37b58b3-9ac6-3589-b82c-8705bca0cb5f | -7.9482 | -46.82634 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ae1c8c-0b4a-33bf-bcd1-cf389512e084 | -11.43193 | -43.31834 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf4c2908-59cb-31c3-b0b8-db3526729b2f | -5.74027 | -46.29034 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4edd234-1ceb-39cf-99a8-18e8e87ab82c | -10.72331 | -49.06855 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69fd59dd-7a50-3072-88b4-ccdd8c017f16 | -4.13894 | -46.3553 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87a065a1-3eef-335a-96c3-16c5abe51efb | -10.93413 | -43.80955 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56383849-0271-3fc7-a664-703cce79e587 | -5.21807 | -49.58362 | 2025-11-18 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1c1cd40-495e-3883-8568-b0530e9ff38e | -6.84341 | -46.29528 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b11f89f-8a92-374a-b15a-87db6b8c4b7e | -10.86743 | -44.08269 | 2025-11-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4c25a4c-08a7-3f34-9011-0159da5534b7 | -11.08911 | -44.80876 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca8480c3-9355-3bc8-b020-d1bcfebc13d7 | -5.3916 | -46.23174 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a424e665-bc24-3f7e-87ae-b19e8760130b | -6.05349 | -41.55824 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| efbea21e-605d-3731-8dac-5c59e4dff07b | -4.51374 | -46.03357 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a6e4f6d9-ba32-38ee-923a-edf82811e08a | -4.3356 | -44.34584 | 2025-11-18 04:21:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158ae05a-e0fd-3e98-bb2e-3242402b588c | -7.6121 | -42.57539 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09d14e52-97ac-3de0-bd8b-03da22ea1546 | -4.73292 | -46.37723 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76c8809d-ba82-3b1d-8f30-1e0bd8d27765 | -6.94096 | -39.62711 | 2025-11-18 04:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7863485c-56b9-3567-bf27-edf2ac17ddaa | -10.38658 | -47.49935 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95c1bf7d-ad3c-3350-a963-3889ad878e81 | -9.88279 | -44.18972 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 319abd67-7485-3c43-824f-82663c351e07 | -4.68775 | -46.93671 | 2025-11-18 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea708bcb-7802-3835-b9f4-b99cc11ada2a | -3.28107 | -52.42218 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c54814e-ef82-3d3e-bb51-bcf6543a9cc3 | -8.54005 | -46.05376 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed0afd2a-b19c-348c-a79a-f213264ae573 | -6.68072 | -43.76875 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c023d0-b1d6-319e-8dbd-f258cf172a05 | -9.40193 | -48.45409 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7ee0abfd-8797-3aab-8bc6-ddd6ccd0b94c | -7.30372 | -45.76112 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbfdd3dd-3e24-3df7-a120-28fb31cc544d | -4.67707 | -45.80119 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 421a425f-56a8-327d-9c7a-2a7b69a09620 | -7.94915 | -46.82244 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7b2a8b8-d4cf-3bc3-999e-b1b0a262486e | -7.42252 | -42.76015 | 2025-11-18 04:21:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe991610-52fe-3d7f-ba70-2053f006cdde | -3.48702 | -52.35707 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62d417e0-6bb2-3987-a03a-39623a0e5e5e | -4.42157 | -45.90669 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f20e93d-ba04-30ca-b96c-0482440abeb4 | -10.52172 | -43.96227 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8955d6e9-10ce-3c81-90e1-8485a56cb760 | -5.47237 | -41.40579 | 2025-11-18 04:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5adc634e-91b1-3f33-b5bd-f2f7d1c827ff | -6.64634 | -43.59418 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74131d80-ad40-3275-9188-512de70a18ae | -3.0847 | -51.26374 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 812502aa-db0d-36e9-a582-320c81dfbb1c | -6.29071 | -43.80492 | 2025-11-18 04:21:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 44f8e85c-0a6c-39b7-8f57-7e29f131c6fd | -6.41726 | -47.43926 | 2025-11-18 04:21:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1edb494d-909b-3027-a896-aff0f98319c9 | -7.69499 | -46.85069 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86c6213a-fb6a-368f-918e-eb3694e4ee15 | -11.44802 | -44.9494 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 102bc919-9bbe-39d1-b797-01c108db8695 | -7.35481 | -46.21095 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa069ce-b18f-3903-a27c-24de08c4b872 | -4.42496 | -45.90725 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd1dac3a-219c-358e-86dd-dccc84366a75 | -10.51889 | -43.95809 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaffe13d-3f0f-38aa-b21f-25beccd4e722 | -4.48815 | -46.59336 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fde6111d-7142-3d6e-afba-80d68079b5ac | -6.21426 | -46.88077 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 618fa105-74ec-350a-b274-bae9072f2838 | -4.1757 | -44.23576 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2f2cfa99-7f70-387c-9166-7b50c110be00 | -3.51241 | -50.27935 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2efb93a-1dbe-30dd-aa28-70c079724f98 | -6.40484 | -42.3278 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bfbe70b8-cff0-3353-aabf-d5d9bbb5d6a0 | -3.77935 | -47.61069 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| affd24a5-11af-3c2c-ae21-5fbbf75bb5aa | -6.44561 | -45.74369 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc480c82-5682-3434-86a7-e6696d8f5104 | -8.09674 | -46.0588 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ee6e0fe-2c28-3f4e-afc8-d6d92e46ab6b | -3.1558 | -51.48581 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39d01806-d4d5-3ad6-8142-d81c88b72963 | -6.93747 | -49.67048 | 2025-11-18 04:21:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 426acf15-f24b-3cc2-ba40-68d75121512c | -8.38097 | -48.70538 | 2025-11-18 04:21:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 478802da-1d4e-385d-8a9d-d132f83b2cb6 | -7.56989 | -46.29295 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
