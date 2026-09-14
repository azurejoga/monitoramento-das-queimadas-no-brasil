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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0256f8e9-1da9-31f7-b0ae-89c2485e15d3 | -11.21563 | -46.42216 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 59d87006-335a-3c1e-b9e3-0e3f1cff6618 | -3.37382 | -61.3442 | 2026-09-14 04:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eeb8aa02-004a-32a4-8fd2-42c398870e2e | -9.43804 | -50.12965 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f0c24d94-3b7e-3685-bf71-c5e0a147d9be | -5.84757 | -52.09756 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f6228b6a-2e51-312b-9bb8-910d20261b7a | -10.23987 | -50.90583 | 2026-09-14 04:53:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d975a34-9973-322f-99f6-24c2550a9d6f | -3.69758 | -58.88226 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c53118-249e-3c78-a55f-036970b4f24f | -15.23788 | -48.06642 | 2026-09-14 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0497c181-7312-3d43-83f7-eaca5fdaadf8 | -10.68024 | -54.16615 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6e7b7201-bae6-3b2e-8fa7-1a284a860049 | -8.50498 | -54.64831 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 415b345a-1f3e-310c-bfe1-b8e3d63af897 | -15.55731 | -48.79043 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c1fb3a2-9777-38e1-9c43-dcddc2a71f0a | -4.38952 | -55.2085 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9202e340-1f4a-3787-bf6f-982427f22fc0 | -6.66381 | -43.65467 | 2026-09-14 04:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9891b965-02c0-37ea-a9aa-9dc20baba1e7 | -11.26156 | -54.13134 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af6f6846-5d03-3a0b-91be-60d9075ae727 | -11.24611 | -54.14022 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1507eed-c0d3-3cc3-bc5a-6c844c9cfcfe | -6.31839 | -59.98228 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3095fe7-927e-3488-85ab-67bd0c9d7e2f | -6.28469 | -55.27693 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3530dcf7-abc1-3b90-8019-de09ee2f3333 | -6.14987 | -57.69278 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d60d2c6-6254-3f0a-b709-60358b1aacbb | -3.59917 | -59.07271 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c425926-4d9f-31cf-987d-c7e3ac6f7369 | -6.59438 | -58.86405 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 327ab525-aca8-30a1-bd30-b0453458250b | -9.98351 | -50.27259 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28d1734f-3abf-3cf4-a007-b69134debae1 | -6.5896 | -58.86318 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72aa2621-1626-3010-8299-ef8695a5ce08 | -4.09205 | -54.43698 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e274ff6b-1647-3a12-b885-78611962ac28 | -9.42953 | -50.11692 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 581dc380-394a-3191-9035-1dca8f666437 | -7.51736 | -55.2809 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa264b49-2bae-3fbc-953c-28e51db68fba | -10.5441 | -51.3086 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb9aec51-b10b-3507-b6c1-d266eb95ebb9 | -5.79733 | -57.73084 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 094eb83d-4758-3c0c-a046-c8a7ded0bbde | -7.09138 | -41.81244 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d7f554a-c87c-3beb-8720-043b7aba6e69 | -3.8927 | -60.59492 | 2026-09-14 04:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51bda006-edd9-39ca-b7d1-32bc5753b0bb | -3.6327 | -58.62788 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3bf972-6e1b-3146-b364-1284077507ce | -10.41584 | -57.23212 | 2026-09-14 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f5689db-9728-37dd-97d3-3932847a5d57 | -16.47901 | -43.42356 | 2026-09-14 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3d42aaa-838d-3f44-9b8f-73c4a4ebced6 | -10.50364 | -51.37104 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e606e5f-716b-38fc-a75b-328b6bd1e6a7 | -10.38113 | -46.651 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef874dea-214b-3b94-8c64-6b34972620ca | -6.28943 | -59.93535 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3dce05f3-50f0-3f5a-85c9-9a8f15fcafe7 | -6.66991 | -50.91882 | 2026-09-14 04:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f1e5d82-f1af-3a24-aa81-d53537ec87a8 | -4.57238 | -54.91078 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1edd7100-76fe-39ca-b7b5-7ad1e4a47787 | -9.41187 | -50.16349 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 23628573-fdb1-31f9-a0b4-30b43a31e174 | -10.04769 | -45.4908 | 2026-09-14 04:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6958e5d2-aa03-370f-9bd4-fec1ac5022ff | -10.68491 | -54.15919 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c0012c8-1b4d-396a-8bf3-fa6bb28e5159 | -3.87391 | -58.9044 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee1d8a9d-925a-31da-b39c-4ede4c5b3388 | -11.23213 | -46.42844 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04298c5d-7947-3dc2-bf94-304370ded439 | -4.34194 | -54.77969 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2e76040-9481-3bf8-b0da-27e1e5d9a5c5 | -6.57706 | -58.85015 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c45bf7a2-a874-3807-b604-7a428f35bd63 | -3.63766 | -58.6286 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa6193b2-b090-35b0-a7ec-78ac60e7b647 | -6.07427 | -59.92352 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a2c6701-962c-3ae8-b005-b1ed46001efb | -10.52509 | -46.30991 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c9a47c-3f20-3541-bd0e-4c8f41043135 | -4.13453 | -54.01913 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f32b61a8-6538-3b80-b747-a98bf1877595 | -4.12372 | -60.68843 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a2150e2a-edff-3da7-9198-62942db8ea3e | -4.38783 | -55.20015 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef5feda8-e07d-3311-8f2d-777ecd2fa029 | -8.05564 | -54.85795 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80c35f7b-9ba6-3343-b25f-fb3b7aef1dd3 | -8.05635 | -54.85373 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83e7e1ae-8b65-37ae-89b8-4c893ae62f78 | -10.67899 | -54.17369 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 66e3c502-b275-3d9b-8dd3-2af86f853841 | -11.18227 | -42.81365 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 54b1134e-5e9c-3377-8556-d80e2ca22543 | -6.13503 | -57.69912 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497e5958-a4fd-3521-a721-06abc3f03fa7 | -5.07963 | -56.25359 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346e642d-4f8f-300e-b915-f0de6cf5d7ae | -6.64538 | -59.9648 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c72cc5ee-fa2e-3b3f-93ed-f4c15b8fe6ef | -6.6411 | -58.82062 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ffb0bf6-d770-3e3c-9d88-8b462fbd8b21 | -8.38638 | -46.29485 | 2026-09-14 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e70282e1-5518-3c06-91f2-f266692b47fb | -3.89831 | -60.59592 | 2026-09-14 04:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef7bb013-1b6f-3a94-8772-3251cadcc30d | -8.54155 | -54.70813 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d42605-695e-3937-b175-90b20f0caf8d | -4.11809 | -60.68745 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7ae09b7f-4d60-37e1-871a-afdff125e3de | -9.69749 | -54.33934 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acf8ad48-07b7-325b-9538-6ede5cbcd543 | -6.28964 | -59.95618 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e98a2d2-c294-3739-b86f-7f1e745d0700 | -6.32356 | -59.98323 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d706bb-1012-3ad2-8b39-74f949fa9ee1 | -10.69713 | -47.53006 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50f283a7-8240-344c-bab1-aeddffc54dbb | -3.80677 | -58.90468 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ab884fe-d231-324f-a8ba-a72016c079fd | -6.04774 | -52.20583 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e977d93-613b-33f1-90c8-c8073e807e63 | -7.09211 | -41.80848 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57ccf185-9bda-3763-94ce-cb830685f25b | -4.54196 | -54.92927 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c4cd362-a393-38a2-bad3-bc6f38a5cde8 | -12.16843 | -48.95951 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fdc9f23a-f3a6-39d4-a9ce-15fc83908a9c | -9.39825 | -50.16138 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01ad3ce3-77b7-3e4a-8ce6-f8c7bc72e087 | -9.165 | -49.99348 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e6d41c0-1b1f-33fa-88e8-3805917c12a8 | -4.39341 | -55.20905 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1485835a-a64a-387d-9421-f59f75fae0f2 | -11.23277 | -54.11495 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1a0860-d9cd-3e14-bd6f-99773280c15a | -7.15592 | -55.31039 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0eaf6bb-e0cd-3695-b689-3c75eb3f51ea | -8.96031 | -49.5258 | 2026-09-14 04:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7190db79-45e0-3455-b846-5dc02883a7a1 | -5.08374 | -56.25427 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60580f93-ef53-35ec-9c1c-1ccd4ce16ddb | -8.14562 | -54.8082 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 897c5087-b65e-3ad1-8349-6d169684ef10 | -3.74118 | -61.751 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dffe7b0d-494a-3c0c-bbcc-9fa5011aeffb | -3.17756 | -61.1165 | 2026-09-14 04:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98081aa4-0d47-3362-a995-a6b059cac7a7 | -11.17788 | -46.38905 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 368f4c18-51a5-360d-9ff5-754470aa01c1 | -9.71039 | -54.36947 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29974d23-5e2c-3587-80f0-f35a843b05e2 | -9.71242 | -50.84984 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fa5cfaa-c6a7-3303-9d48-52cc34ca5c1a | -7.10508 | -41.79547 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d9b7cbd9-e9de-308e-9dbc-82ce274e84dd | -3.74063 | -61.74902 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdf86196-78bb-3c22-98d1-8ca32ad42491 | -10.66966 | -54.14505 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| e4883eef-a712-3567-ac19-021717117854 | -6.32723 | -60.02302 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e491bcd-f8a5-3262-bfc6-225ff9b5c692 | -4.12623 | -60.68991 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8b755a8-7c2d-3284-b53b-eb25042ac194 | -10.46458 | -51.24871 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06222cb1-5449-3ea0-9186-16b1650188e1 | -3.71791 | -59.30221 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c36b339-4efb-356c-8ae8-e57c916ae59b | -9.45596 | -47.85333 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53d92049-1b27-360c-95f4-9c923216ddcd | -7.22653 | -47.558 | 2026-09-14 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a90fc6f9-e9f8-3a13-a512-5eff3f125c70 | -9.13636 | -51.58145 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec5a6ea-1846-3c97-870f-e803b4433190 | -15.54887 | -48.79415 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d1a0b264-70fe-33be-968e-c485eae2854e | -9.55138 | -51.36145 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04df2171-9461-3003-a0b5-514713687734 | -9.40278 | -50.17724 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 713220a1-f5ef-33e0-b68b-024eb51c7cfc | -5.13184 | -55.95832 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6708a39d-180a-3653-bf48-03e5fbad5871 | -7.0926 | -41.80481 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8246975a-85e9-3ae8-be80-057185f2489f | -6.33757 | -43.36889 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 969a79aa-d1b0-398a-be17-a6a41e0ff46f | -15.5527 | -48.79511 | 2026-09-14 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README48.md)
