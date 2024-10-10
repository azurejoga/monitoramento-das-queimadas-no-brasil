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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b0ea763-24f5-3052-bc61-d2220f7854dd | -7.65305 | -42.54547 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f788bb1c-bb52-3c00-a9d8-b5c241baf720 | -7.65225 | -42.40271 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3e65bbd3-1a0c-3b00-9458-78e4bb5cfb4a | -7.64853 | -42.40212 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48327f02-d008-30ce-b7b8-ab43af80917d | -7.64481 | -42.40152 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 91df513d-c98d-3059-81cd-53e40eb32623 | -7.64408 | -42.40599 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2c403363-6374-3a56-9a7c-3d79f096d350 | -7.64035 | -42.40541 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3cb42db4-0ca1-393d-bdf8-6b73d1d80886 | -7.63663 | -42.40483 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a43bebf3-3816-35b2-9c4a-1cf0bc54c79e | -7.63591 | -42.4092 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61b12a90-4436-3cda-8c65-7e119aaa44dc | -7.63291 | -42.40423 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 699c852b-e614-3444-8e11-672c1290c7ab | -7.62846 | -42.40803 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 81e789ee-a9c0-32bb-ad12-a9eacbc4d1de | -7.62027 | -42.41135 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 20494660-9ec2-3047-b484-ff83a01f3434 | -7.61654 | -42.4108 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 671f3226-ae48-3d49-9c6b-4db009b1a6be | -7.61581 | -42.41524 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 308857a4-40ff-34a1-b2ac-b82b73831aac | -7.61508 | -42.41967 | 2024-10-10 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 763a749b-10b2-37f4-8a2b-3757d69a7d41 | -7.29176 | -42.23816 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 89ce2460-9753-332f-bd6e-3bdf59e1fc5a | -7.22948 | -42.30278 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 72805b27-c09e-3c73-9c64-4775ca8b9807 | -7.22577 | -42.30218 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e1f9d57d-5ff9-3e67-9103-4ac0e802758b | -7.22351 | -42.29259 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da360213-4a3b-3e2c-9a73-337ea9c2c9bc | -7.22279 | -42.29704 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7fbff677-bdcb-3dbf-96a5-b43e21d6b207 | -7.22205 | -42.30157 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e248053a-30df-3de3-a9e9-9259e3dc9635 | -7.16303 | -42.61504 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a357faf-f779-3d62-b1ec-95cdb36d10fc | -7.16226 | -42.61971 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eefba351-4f5a-3e83-b547-d9a423f4ef2f | -7.16149 | -42.62442 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c197053-1278-3f17-90e1-1f3ad933a6e9 | -7.16 | -42.60977 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 30e0bb05-0b15-3c73-aff7-149299b90898 | -7.1577 | -42.62378 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38d5df32-7ce6-3a46-a2a5-511ef2e456db | -6.69814 | -43.18559 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 63c7456d-d7c9-33c1-9cbf-c070c2145ca8 | -6.94171 | -43.43406 | 2024-10-10 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd12cb54-c4dc-3616-a4da-d97c2cf791f8 | -6.9093 | -43.54373 | 2024-10-10 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e575ac-4bc4-38ea-90bf-1c9dae9f77f7 | -6.72327 | -43.55973 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 412b038d-3cc5-3696-8164-e1743a1413e2 | -6.71923 | -43.55903 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f224692-5354-3027-b765-ae18cd8f547c | -6.68993 | -43.45553 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef066b2-1901-368c-9ab5-30d50a7f09a5 | -6.65403 | -43.52189 | 2024-10-10 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b30f73df-2a69-3321-bd07-cfbcf6cecf40 | -6.62205 | -43.16016 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b440c3b9-d190-3f5d-b419-0e4224650d35 | -6.6181 | -43.15951 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3e5422e-9b57-34ed-8a4b-0973071b3220 | -6.52674 | -43.22626 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f22c1937-8ae0-3064-9c28-e318a54f9fba | -6.52618 | -43.22968 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 584d37c7-25fe-3d20-92c0-8106f8a01978 | -6.49088 | -43.34444 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99036ac9-89a6-3b29-81df-c0bd59df4c18 | -6.48392 | -43.36163 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbdc7a88-5697-3f03-b16a-8be8757cec9d | -6.47268 | -43.3303 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a6b77cd-4cec-3af8-8fee-966319aa80d3 | -6.47209 | -43.33383 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 442267c0-6c59-3674-930e-3a1be39a098d | -6.46808 | -43.33321 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3045296-4f38-37cb-9310-4334a5ec6e6b | -6.43819 | -43.33978 | 2024-10-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0781e924-5519-305d-a6a5-0b985f9acc17 | -7.12649 | -42.64751 | 2024-10-10 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 466acdcd-ab79-3d4b-87f6-c8f99d0b9629 | -7.12571 | -42.65222 | 2024-10-10 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ef2ce7c-ca2b-34bd-a62c-3ad425905324 | -7.11753 | -42.60774 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c896b3ae-41fb-3953-bac3-e0f8bd41a38a | -7.11373 | -42.60716 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5c69828-41d1-3db4-971c-1d8383509e7a | -7.11296 | -42.61179 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07feab15-8b81-3800-820f-1fed0855d41a | -7.10601 | -42.27534 | 2024-10-10 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| edac76b4-73a2-3299-ba22-9bd6f0d8886e | -7.10528 | -42.27978 | 2024-10-10 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef4ce584-00ad-335b-8764-d6eb0bea84c2 | -7.09167 | -42.62255 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 82423fb3-d181-38fc-b630-86c2b946635c | -7.09089 | -42.62719 | 2024-10-10 03:55:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e19cbb31-e065-3e62-bca3-a699cf2b54d2 | -6.67044 | -42.09053 | 2024-10-10 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dced0f40-113b-313d-9d81-c04eff46be8c | -6.66607 | -42.094 | 2024-10-10 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6a520f84-577d-3ed7-943f-85410c529aee | -6.63729 | -42.19873 | 2024-10-10 03:55:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2dce4fe8-7759-3f05-ac7d-78e1f8ffe5d3 | -6.63655 | -42.20322 | 2024-10-10 03:55:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01f8e683-b55e-3e08-9432-476cebf446fe | -9.30345 | -43.34591 | 2024-10-10 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0f97e7a1-44d3-328e-8830-308c24585282 | -9.30264 | -43.35073 | 2024-10-10 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5d6b0f9f-5419-3bb5-bd32-8c076c5d604c | -8.15091 | -42.96112 | 2024-10-10 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 460213ee-01a9-3c2e-b8b9-1cd68e03816e | -8.15012 | -42.96582 | 2024-10-10 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 889b9073-5ba0-33f5-9ecd-00a0b58cdde7 | -8.1471 | -42.96049 | 2024-10-10 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| e1ba17e1-c6c7-31f2-8398-41418938902c | -8.14631 | -42.9652 | 2024-10-10 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 41a56f9f-54e1-3097-a876-e11eb1fe572b | -8.13899 | -43.79522 | 2024-10-10 03:55:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2325b703-3074-34a5-9ed8-9410b4eb8d62 | -8.06419 | -43.83958 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 306b7d0b-8851-375f-94ad-22f10cff2c89 | -8.0198 | -43.83223 | 2024-10-10 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c716bf50-ef02-3119-8f12-2f3a79bf3df0 | -10.82944 | -43.79326 | 2024-10-10 03:55:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15a26006-b90d-3efe-bc23-33e561fadf34 | -9.94637 | -44.07095 | 2024-10-10 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df5388d7-0b99-3563-86dd-c7660de85673 | -9.9424 | -44.07026 | 2024-10-10 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e5a44eb-5f17-368b-bfdb-85ccd9bb8c1a | -9.93903 | -44.06604 | 2024-10-10 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8993e417-69a2-3fb3-8b29-4dc1c27bbc89 | -9.91798 | -44.06948 | 2024-10-10 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71d40d3a-9267-3cd2-a920-e674228b626b | -9.51082 | -44.07137 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ea50ad0-876f-357e-b13f-0b6e3c82115d | -9.42781 | -44.13796 | 2024-10-10 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33e3aa1a-bb75-3e3e-958b-0a472cc1856a | -12.29539 | -43.73524 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 74578ec9-4dfd-314f-8dac-44f391d2f7ef | -12.29456 | -43.74008 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6c24b588-50d9-326c-9916-b2e773397000 | -12.29163 | -43.73459 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5f81a2ff-1975-3e97-a188-8b5e2fca5496 | -12.29083 | -43.73928 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a1e7a507-cca7-3c03-b5ec-f777e238daf4 | -12.28921 | -43.74871 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75b2353f-1167-3b8c-8f60-88679043b5ae | -12.28786 | -43.73399 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 323448e5-92cd-31c4-a059-c66662d70340 | -12.28708 | -43.73856 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a87ee16a-ee5a-36d1-bbaa-fdbf79f1afd0 | -12.28627 | -43.74325 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 771cfc9f-01d8-37f2-831a-fa2ce897358e | -12.28329 | -43.73807 | 2024-10-10 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| af377b82-efd6-3070-a777-296b5df8cef5 | -12.28251 | -43.74262 | 2024-10-10 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7928eb27-ecf1-3616-ba35-d6970dfddf7b | -12.28173 | -43.74717 | 2024-10-10 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 55733ab5-c06e-30de-ae99-456a30798e7e | -12.27796 | -43.74657 | 2024-10-10 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ec442a2-ecc2-3831-9dd2-0e8955ad3bd5 | -11.89532 | -43.88722 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2ce99de7-363e-3b71-877f-bdafdcbb4a95 | -11.89151 | -43.88655 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ec203173-5a7c-3df7-ac7e-1a178e17f56e | -11.87426 | -43.83182 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dbdd63b-87f0-3501-a326-2275c18697f4 | -11.84302 | -43.83127 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ce9997a-dae8-38ab-89a1-483d6706921f | -11.84003 | -43.82583 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71991b33-e7c3-33f0-a14d-005b65fcfab7 | -11.83921 | -43.8306 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bde1eb0-fd57-37f6-adb6-ad7e2ea7c5cb | -11.53023 | -44.02823 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 47a3efc9-f416-364b-ba27-6f100fac6c9b | -11.5281 | -44.02509 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 90db4b41-e566-3934-b4b2-7d7b3ab30ca9 | -11.52723 | -44.03002 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d971e667-3e01-381a-9ffb-b6f2cbbb0762 | -11.5272 | -44.02261 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7efa7b44-ebe2-3f6e-a360-1838ef1e2775 | -11.52636 | -44.02755 | 2024-10-10 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4504cd04-d0ad-336d-9473-b8f79ca107f2 | -11.7962 | -44.49774 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5163812e-1284-3015-b9b5-acd36e80c662 | -11.79224 | -44.49704 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef05ee59-569e-3ec2-91c5-7ff7d0727dc3 | -11.7875 | -44.50069 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9021c274-82f9-3983-8a4f-6ab4d02094a7 | -11.78689 | -44.50415 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 268e7d7c-4a91-310b-99fb-4dc603b96502 | -11.76966 | -44.55511 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 457683be-26a6-36a4-b200-2a7a3541fc0a | -11.76506 | -44.5579 | 2024-10-10 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README44.md)
