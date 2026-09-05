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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb539f0b-f979-322e-bdf4-987053090b1b | 4.27629 | -60.0485 | 2026-09-05 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e4f7a9-ad3a-38f5-a4d0-b0560f49e66d | -1.17978 | -53.82396 | 2026-09-05 05:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5aa1c9b-6439-35b1-b562-3fe4d3947f83 | 2.4501 | -60.76011 | 2026-09-05 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 004cb918-3921-3391-9cb0-446538ecbdf0 | 4.35956 | -59.73463 | 2026-09-05 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d3e7144-ca90-3411-844c-d3d8dabed8f0 | 4.36036 | -59.73939 | 2026-09-05 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 438f03f1-d941-327a-8051-830a8ba2b325 | 4.39477 | -59.72677 | 2026-09-05 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf0c2db-cfb3-3245-a6a0-16b76fef8cd0 | 4.39624 | -59.73565 | 2026-09-05 05:57:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e1217fe-12ed-3b17-bf4e-6ca3281a93ad | 4.27681 | -60.04499 | 2026-09-05 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebcd864-e194-3c2f-b24b-9c0b0a074e4b | -1.17872 | -53.83078 | 2026-09-05 05:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 199e6405-56fd-32af-b9ad-919ac40d1abe | -1.18603 | -53.83043 | 2026-09-05 05:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45c70c12-b683-3b84-95cb-df9871e7f373 | 4.2756 | -60.04427 | 2026-09-05 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b015402-2c4e-3648-8fa1-3de19ac110ba | -1.18696 | -53.82452 | 2026-09-05 05:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87ae376c-cce7-386c-9375-2b014ae8cfd2 | 2.45437 | -60.7594 | 2026-09-05 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f5ccc3f-7da0-3ed2-8dd2-784504bdfe9c | -4.12827 | -56.33776 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b52ef75c-8f3b-3d9d-86e9-8a582b66c51c | -5.76835 | -59.18796 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 104329f6-9c9e-3d3f-97ec-20014e22bb2f | -6.66526 | -59.94961 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b8f861e1-8bc5-3029-bbab-9ca50ac7692a | -4.66736 | -55.64273 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cafce23d-d1f8-3670-98b7-94ed7df8aebd | -3.8039 | -55.88158 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b40550f-897d-337f-90be-4cd25c12a33a | -4.67099 | -55.64057 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c2e6215-a889-3d56-aeda-569b8968865e | -3.93355 | -59.34544 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9443161a-513d-34fe-ab63-72f0d133ddbe | -2.91096 | -60.99187 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ec5633e-05c6-301b-8125-f1c2d126b8c3 | -5.43236 | -60.18436 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95090ba0-e5c1-3c4f-979c-f20963d75fdf | -5.83639 | -60.25665 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83746a8d-253b-3863-a000-6ec9fbda4d30 | -4.91437 | -55.80271 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 78ca245a-48ba-3cdb-bf3a-694cc72a5cd5 | -5.29378 | -56.02114 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32ff6568-bf2c-33b4-a176-05546cf902d0 | -6.65873 | -59.95831 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37764ed2-ad39-3e16-b635-75c7abc209b4 | -6.68306 | -59.97425 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8324606a-6252-3f36-bb08-5f7a792cc7b1 | -3.07469 | -61.08689 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5298cb5-04ca-3d82-961d-684275ab94eb | -3.76407 | -61.75955 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f4332ef1-6003-3a26-b3d3-3c646333f280 | -5.33815 | -56.02987 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f0940996-45c7-3645-a3f9-a1a72736ddc2 | -5.33191 | -60.13535 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7979b9f2-548b-31f7-b2aa-5fe632a3579b | -3.77288 | -61.76085 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a0e39e0-2c1a-33a1-90e2-1bc4f39855cc | -3.79669 | -55.8819 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6657881-3986-3882-9d66-4ca56057a756 | -5.30037 | -56.02211 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00b6114c-372a-3018-9684-4f39f0024479 | -5.35232 | -56.03492 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c2b0fbcc-374e-3612-a801-0c14073f2a66 | -5.1767 | -56.055 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e894638-801d-3723-9114-e9e930960c67 | -5.32015 | -56.02476 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7473fda5-3cfe-3ed5-ac3f-171788e22b84 | -5.35211 | -56.026 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fac91fa8-b731-32c0-8bd8-679cc05b4b9e | -5.33831 | -56.03893 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f13c1d20-4737-3eaa-bb4d-57c5db0c4a4f | -5.29612 | -56.00428 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8fc9fd2-4c59-3886-9e28-d16599fa3d6d | -5.84096 | -60.25607 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c306e7b6-f12e-329d-b52e-874fb469413c | -4.09817 | -60.66507 | 2026-09-05 05:59:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7326ce1-dc7c-30ac-bef9-644892bfda8d | -5.3455 | -56.0252 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a76bd633-fba0-3895-a2c0-5bcce89f65d5 | -6.03279 | -60.16985 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e84b0bc9-7e46-3fd1-bcf8-fb62c9685ae1 | -5.1516 | -55.95681 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 346c4288-824d-3256-a7a9-fe08ccc6010b | -5.17592 | -56.06063 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 251731da-3801-36a4-81d6-1f634bcfa81a | -6.14658 | -59.94305 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d335b26f-a891-3d3a-9f9b-1fb73c724f6b | -6.59444 | -59.91977 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfba9bd0-13dd-3805-ae6d-2d44ac94858a | -5.33252 | -56.03235 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7201d728-449b-374f-93cd-72e4b41ae6c3 | -3.14249 | -60.64005 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f472646a-6224-346c-bbbd-f937d6d4d3e0 | -6.03321 | -60.16694 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99ca9ca6-8819-3081-b736-13a7f52ed69d | -3.77113 | -61.77087 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72334b34-e935-3421-b3c0-2c0438d8b97c | -3.77616 | -61.76726 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6739a9a9-927b-315e-98a0-3489016aacf7 | -6.58492 | -59.91184 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98ba24d2-f1b2-3963-92ba-34fa712983e0 | -6.67792 | -59.93523 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f3657ad-8178-3601-ac19-b36c6c88b033 | -3.07012 | -61.08625 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3967e2fa-f8ac-3e6e-880b-421b9485aab8 | -6.58923 | -59.91895 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cece1c83-0c6b-357d-96a0-499fe0afe6ef | -3.13703 | -60.64429 | 2026-09-05 05:59:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 683157c1-ffd4-3ea1-a867-041dd3d7c962 | -3.07883 | -61.18166 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3c599aa-55cb-3e06-804a-8bad92040bf8 | -5.34321 | -56.0421 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 77adcf36-52e9-3e71-8b54-89896fcfba33 | -4.67568 | -55.63242 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8ad8510f-5dc9-3ad7-97dc-3b684031f601 | -3.41995 | -58.30684 | 2026-09-05 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43d59df1-58a6-3352-a080-152017a69f42 | -4.67841 | -55.63623 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fb72c792-9082-392d-b177-093c11d49aa9 | -3.76651 | -61.77298 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9f413b4-0197-3c0e-aa17-4d66bf598742 | -5.32673 | -56.02577 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97f11595-5076-3753-b373-e184b48c0d9c | -3.77553 | -61.77153 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9545d76a-f1af-33a7-b865-e7d667a415a3 | -5.21388 | -60.03006 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 721403a0-068d-3fc2-b2cb-7cb203ff8e46 | -4.67491 | -55.63776 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75db4799-cfae-3428-a83e-f40d1f6f4e39 | -5.31355 | -56.02393 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf5da82-7775-3cd2-a541-219bf0e12f90 | -2.91408 | -61.00349 | 2026-09-05 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc71971d-8353-380b-bcc7-aebb2a64bc69 | -6.02769 | -60.16919 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 081b6df4-70fe-3b44-b893-507b82b21886 | -6.6618 | -59.93628 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e256c33-8445-3378-a2da-4ffec3c89151 | -3.76277 | -61.76805 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cee289c-e81d-35c9-890a-18e9d347a0cd | -3.77239 | -61.76231 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2237bc5-98f6-3e88-8ac3-f891bd902514 | -5.33412 | -56.02103 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dc24e1e-da80-3983-bfc8-40e3966d5fa0 | -5.33332 | -56.02671 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4ee5ab3-730c-3108-b80c-315ca8929b04 | -5.14499 | -55.95592 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c16a028-44d1-3a0c-931b-ca78be65c4ad | -3.76033 | -61.75461 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6799e38c-538a-36b4-9ad0-9698f94e743f | -3.03887 | -59.36566 | 2026-09-05 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e8e77b8-b3cf-3d9e-be1e-12d5d8d3ac40 | -4.67409 | -55.64339 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dca74b98-95ef-3f06-8cd6-3874c52b8f7e | -6.03236 | -60.1728 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b1d0b3d-cd7c-357e-b0ae-a6586e2681ba | -5.17026 | -56.06015 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b4c8a38-2096-39e9-84ea-24688f652a83 | -6.66048 | -59.94573 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c87ae740-6ee0-389a-98e3-ffe90b698992 | -1.77468 | -56.2478 | 2026-09-05 05:59:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8994b528-8b4f-3e35-89b4-aac8f056bbad | -5.56198 | -60.17121 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33437698-ed75-34de-8cf5-98c58c9576df | -5.31434 | -56.01829 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a428d3f6-179d-3d81-a271-45e3b100a113 | -5.3457 | -56.0342 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f63b5f6-bb22-37c0-85f3-e108b76c19d0 | -5.29455 | -56.01562 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c879fc54-bb71-37be-bb6a-004060d464a7 | -5.77056 | -59.18716 | 2026-09-05 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c9c025-cb42-31fb-a74e-91cca0c95401 | -4.68073 | -55.64465 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0165fddb-733e-3191-a1ba-4049320b9b7a | -4.67762 | -55.64193 | 2026-09-05 05:59:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6cd1480c-862c-35cd-80d2-2c2bff7207c8 | -3.79089 | -55.87964 | 2026-09-05 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d813bcdf-a2b1-3cb8-9364-6bd64b20e808 | -3.82788 | -60.76452 | 2026-09-05 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 874166d1-8afe-366f-bb71-cf5b07064947 | -3.77742 | -61.75869 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8375a33f-e00f-33e5-be48-eed444934f74 | -6.66483 | -59.95271 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 62c8f59f-f4a9-3b22-b579-561ecda396c0 | -3.77662 | -61.76578 | 2026-09-05 05:59:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a6f2183-d242-33f9-8db7-4f18cbe1271c | -6.67136 | -59.94404 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3cbc830-3314-3f48-b2df-2cfd88dfbd8c | -5.431 | -60.1213 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec3b522a-d5c4-333b-99a2-40312e58e71c | -5.33891 | -56.02418 | 2026-09-05 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f79b4f1-b8f7-3292-903a-0db5e4d86f0f | -6.65263 | -59.96396 | 2026-09-05 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
