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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8447e325-7cd8-3848-9493-eacac5e9943b | -2.6835 | -57.937 | 2024-10-11 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57ac3acf-64ef-3b56-8a0a-a68eb8add550 | -2.6802 | -57.93649 | 2024-10-11 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 776791f8-7605-341d-a230-2ced5a2bc3fc | -2.62309 | -57.56182 | 2024-10-11 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff66cbe4-7db9-367c-8fce-b74666643bc0 | -2.40094 | -57.17595 | 2024-10-11 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e10296bd-c9a5-3a40-80e7-3e4a497440c0 | -2.39762 | -57.17543 | 2024-10-11 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7b6a724-9d4a-388e-b48c-aba3fdd15b0f | -2.38651 | -57.15947 | 2024-10-11 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54da060d-54f2-3e20-be0b-cada6c5dd65e | -2.38319 | -57.15895 | 2024-10-11 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031c8a16-d25b-3ef0-a01a-fb3b2475762e | -2.38265 | -57.16243 | 2024-10-11 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9825ef3a-99c3-395c-8e50-8fd812839640 | -3.95698 | -57.16534 | 2024-10-11 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c61a5aea-a654-32a8-90d3-b2338345118e | -3.79679 | -58.34772 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb5c397-1043-363b-9310-8e8af72ce788 | -3.79625 | -58.35115 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b021609-514d-3385-a677-5b484178d5df | -3.77854 | -57.0001 | 2024-10-11 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d695682e-6817-3049-97c0-aa3df5aaa11c | -3.73571 | -57.12755 | 2024-10-11 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309324fa-58cd-3311-9d32-94e8fe08a90e | -3.53804 | -59.47017 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a7db4f-7276-3c8c-8a4e-97fd2e1720b6 | -3.53748 | -59.47369 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f72c41-fde2-3df8-9caa-1fa1cb3d6e4c | -3.53692 | -59.47721 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b5b539-64bb-3f42-80c3-f04b96bdc17d | -3.47901 | -59.50081 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4cbf463-6923-3823-9f76-d93f1dd46c42 | -3.47845 | -59.50434 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fff9b8e0-7429-3b18-b18c-097f731c189a | -3.47566 | -59.50029 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0499600-5f0b-375b-840a-55e9ababfe9b | -3.47511 | -59.50382 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7978a260-8099-3785-942a-6328d4ffe498 | -3.45841 | -59.58831 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 699b4e5d-20cf-30fc-ab65-97a9fc04f69d | -3.43663 | -59.57401 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59e935b1-4ee5-3012-a6cf-14661bfec8d5 | -3.43158 | -59.62782 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa31e539-8549-392e-b596-d3aabecbee86 | -3.43102 | -59.63138 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a75124f-ddc9-31fe-9080-96b9ed8c0c47 | -3.40963 | -59.7451 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8996b641-f401-3280-9ef0-2d61b30d3a74 | -3.35618 | -59.50282 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 705409dd-d1d9-3527-8938-c62c4d1772ee | -3.35284 | -59.5023 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eaf7302-f9d8-30ae-98c9-8c310860edc2 | -3.28657 | -59.79159 | 2024-10-11 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9acd5460-b047-3e4d-a900-a9cddf466410 | -3.09015 | -59.30976 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dbe61ef-b688-3b93-abef-206b4e5018cc | -3.08625 | -59.31275 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dbe0c7f-72de-3366-88c0-e7b7df526ddf | -3.05559 | -59.35785 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 949b6197-5873-32c7-ab0b-9efc1f573510 | -3.02165 | -59.39951 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fda0c1d-8f3a-3af0-8a3e-7a5d07fbdceb | -3.0177 | -59.10068 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d29ce787-f5f1-3b68-bd49-a7998553b506 | -3.01327 | -59.10712 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb02ac81-fb30-3d8f-b24f-10bca440633a | -3.00939 | -59.1101 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 982d9383-d1bc-32aa-85a0-b2a654eec44a | -2.96659 | -59.31506 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f9fb3d-13a6-31b6-8e01-35651f4513d1 | -2.62969 | -59.37854 | 2024-10-11 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb91fd08-fa6f-3886-9bfc-c6979a328916 | -2.62718 | -59.37764 | 2024-10-11 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d50ee65-f272-38c7-9966-045d79da440d | -2.58867 | -59.40433 | 2024-10-11 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 040f8e31-539b-38e2-89cb-84f735b34110 | -2.29081 | -58.87577 | 2024-10-11 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74503b57-b543-3ad0-9c2b-bb0e329326b5 | -3.64035 | -58.62902 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ceb3c88-5ce2-3978-a60f-8c072dff0128 | -3.63814 | -58.62164 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fb17c18-1056-3879-b47f-26dbbaa5dc7d | -3.6376 | -58.62507 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1e740e9-fff1-35bb-b868-3eec8fae3bc5 | -3.63705 | -58.6285 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2abc340f-277e-3cb3-a0dd-ce167a8e19b3 | -3.54241 | -58.68768 | 2024-10-11 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af622dd4-1f50-3879-8261-a396d7090518 | -3.68419 | -58.78027 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6466af8-fdf9-33f7-9cf2-73dbe19e4101 | -3.68365 | -58.78371 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e303a6b8-1964-3552-8116-e8b202316cad | -4.54953 | -59.91675 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c5ed7ae-1b4f-34b5-a784-e24144dd097c | -4.54896 | -59.92031 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5463b953-4a03-3c20-8d11-dfe055315a7d | -4.54618 | -59.91622 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eadefd2a-6393-315e-888a-086ae76a4599 | -4.41369 | -59.59421 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab0faae1-bd19-331e-bb26-7a98de029521 | -4.37944 | -59.94156 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c0432d5-695a-3dd2-9b8a-928d6167b6cb | -4.34781 | -59.77219 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ad43c3-d1f7-37e6-8ba1-014f48cf572e | -4.34446 | -59.77166 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 876252df-c42e-33aa-be02-5d46cdce8939 | -4.28889 | -60.01194 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 896fbdf7-ded4-3e9f-bc50-01c3b256e73d | -4.2693 | -59.88356 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b54962c5-c526-350f-98c9-1bb5e69d74d7 | -4.26481 | -59.89019 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df04a79a-d9e6-3fbe-87b4-b5275b0b69cb | -4.26425 | -59.89376 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c484700-3f69-313b-b2c9-7068aef6e49b | -4.26186 | -59.99627 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcdc7134-24bd-345a-8753-3438b070efa8 | -4.26129 | -59.99987 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84bb7bc5-e5a4-353d-8e34-4a29048cce85 | -4.25849 | -59.99574 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02db661d-061c-39d4-b961-e32aac95e53c | -4.25792 | -59.99934 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81b426e0-23c7-35c3-805e-049315b0bdb6 | -4.25569 | -59.99162 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d979fe7a-d4bf-38eb-bfc1-b4622c32b219 | -4.25512 | -59.99521 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 320b9030-680c-3687-8741-e1b8eac00791 | -4.23518 | -59.85991 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccd3cb75-22c3-3ab3-bdcb-e888100a7f7f | -4.23239 | -59.85582 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 095ec7ad-a1bf-3912-bc70-6ab70edf6846 | -4.23182 | -59.85939 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46696aac-f8bf-35e6-b460-80d2421e9145 | -4.20736 | -59.99143 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15bd364e-d792-3a60-b0d9-c34fed02a707 | -4.18952 | -59.95178 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed1f3a31-462a-3669-b260-0fd328babf8b | -4.18558 | -59.95484 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd36c8dd-4e79-3942-9bb0-c8ae9d9f22e3 | -4.18221 | -59.95432 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb38248-3857-3d01-8336-3bcd00cbcb2c | -4.11015 | -59.16693 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6967322-9ca4-3aeb-84f6-e9b1accc6207 | -3.98683 | -59.0192 | 2024-10-11 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 517119a5-7f41-39ad-bd61-3be0536020bf | -3.91197 | -59.10685 | 2024-10-11 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b05e49ea-074c-39c1-a882-364191484961 | -3.90287 | -59.61443 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83e48839-c779-3800-98bf-25dc0f890f42 | -3.8949 | -59.68581 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a541683e-71cb-3257-9c4a-987e9747cd6d | -3.73721 | -59.43695 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39efb2e8-da9e-3f96-a02e-e6eb3a3bea68 | -3.61603 | -59.79549 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f49e408c-86ed-31ba-86ca-d204eaafad7e | -3.60261 | -59.77137 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3768d88d-f46d-36c4-a7b8-72ca5eec0719 | -3.60205 | -59.77495 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1ae4c3-e5d5-3ab6-b852-b8814d63e771 | -3.58197 | -59.72785 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35b0aba4-68c8-3eac-9376-5d1e52ae2b5b | -3.57907 | -59.76769 | 2024-10-11 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1b48ca0-2bb8-3e10-8dc7-60d9572f45ee | -6.77048 | -60.05571 | 2024-10-11 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8595d0b9-dfb6-3440-ac71-c986662198e2 | -6.76649 | -59.78207 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a790fa0-7459-34d2-8758-c4a93430736c | -6.76317 | -59.78154 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db61550-db46-30d8-8944-ed30d40c7fd1 | -6.75817 | -59.6203 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e49b08d2-5f82-30d5-b20c-b87fa195b1d4 | -6.75654 | -59.78049 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79fce4c3-877d-3564-aa2f-965bed94c9dc | -6.7466 | -59.69327 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d54345ad-f29e-35cb-be72-ef59dacee0bf | -6.74274 | -59.67484 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 385fdbc1-a348-3075-88fe-f781fa7ef961 | -6.74162 | -59.76743 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b039020e-a1a3-398a-9a2e-5c0ea951b58e | -6.74107 | -59.77093 | 2024-10-11 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02f8c71-24ab-3e2b-87a2-242c6b0b4df8 | -6.73998 | -59.67086 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 941f3a22-8622-3c49-8bd1-214f14177c98 | -6.73997 | -59.62813 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9410d972-e07f-350d-8488-b872d2af3eaf | -6.73942 | -59.6316 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e72ec84-a998-3df7-9829-9e233e478acb | -6.73721 | -59.62414 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96f3cea6-5a25-3d26-a10a-b4f1b7f5aba2 | -6.73611 | -59.63108 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe3b6fe8-f1eb-3362-8354-5757be636422 | -6.73556 | -59.63455 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b59004a-c8b5-3bd0-b5f8-9cc4fa824e3b | -6.7328 | -59.67329 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774a41a8-ffbc-3001-81fd-f90f2b6a7051 | -6.73115 | -59.64096 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac0eca2-7c27-3dce-94d9-270b3ad5e72c | -6.73059 | -59.66582 | 2024-10-11 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README84.md)
