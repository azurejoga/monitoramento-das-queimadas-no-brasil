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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6ba4c78-9954-31b6-a58a-2cae28ce5329 | -7.90616 | -44.92961 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7f3dca4-42d9-34f8-9804-bb2935822039 | -11.00483 | -45.92731 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f7d9caf-d19a-37ed-a266-457f458da39a | -6.62605 | -51.01013 | 2025-09-05 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee266ef7-c83d-3e5b-b85c-72639b8b2fa0 | -7.72139 | -61.52401 | 2025-09-05 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9d725d-b65c-31a6-8792-dac7c05b22b8 | -12.98092 | -54.77848 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6aae2da-e9dd-3fbd-a68e-39eaf18b286d | -10.30078 | -54.14175 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 909ded54-2ced-3376-a4b0-293af18a2d88 | -6.27548 | -53.44143 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0287d8c-a6eb-3b06-9910-c9794bb692e7 | -12.97707 | -54.80363 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9e4f85b-9dff-3b27-a56c-3957c3c8bb29 | -8.0651 | -52.37318 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13a223ba-e09d-3fd5-adad-438052c32ef5 | -9.50798 | -57.82161 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15eb0249-7f74-318a-a8f4-3ed9371370b2 | -6.26109 | -53.44635 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7296d601-5f0d-334f-9472-3f25313a353b | -8.52077 | -51.32758 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a71c496f-f042-348d-805e-66b3d139ddb2 | -13.6593 | -47.92437 | 2025-09-05 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf5c05de-d6a8-3e32-90a0-d8a25d1b93f3 | -9.9678 | -51.64162 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be10f7cf-f936-3850-ab05-79e70c9eefaf | -12.97593 | -54.78874 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14e11259-ab5f-370a-8b8f-060e8745c0d3 | -9.71102 | -51.08307 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0325af65-992c-3461-b16f-7c4c1bbbf576 | -11.39977 | -43.59962 | 2025-09-05 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3406fdf5-a316-37bf-9956-f9d9534be469 | -5.92375 | -57.71773 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcf1a136-1d0f-3c3f-bff6-e83cbecf276c | -12.95906 | -54.79367 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5d1e69ef-10fa-3a0c-8bb5-f30164488f75 | -6.8292 | -52.80673 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ebbdf7-a0da-36f9-b2a8-859a2a5e2b82 | -11.20189 | -55.02559 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f34e5927-b110-3f9c-87a9-32b9e1ce7280 | -11.2661 | -48.33857 | 2025-09-05 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 039f6056-0c04-38a4-9f2d-ac5972d9867a | -10.96877 | -45.9749 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17449cb6-9684-3d6a-a91d-39847d65db6d | -12.2434 | -50.14025 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b74d7370-e088-3fcd-8aa9-cd5201265363 | -8.97921 | -44.45363 | 2025-09-05 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 370c2e6c-9ca5-347e-98d2-16745f8f4a5d | -12.98818 | -54.79805 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e28e3d5-4bd3-33fd-a8c4-c2d030765598 | -7.90582 | -44.93343 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74f28f15-b425-3cc5-8b88-ec9d00b58589 | -10.16709 | -46.25763 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0da6058d-c1c6-3320-9bc3-c65cddeb6550 | -12.52073 | -48.07701 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b5e0353-64b3-3574-8b85-f84fc2cf21ee | -7.70046 | -50.30447 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79dcf03b-227d-36c8-b364-b53c58e79ad8 | -10.76372 | -48.29025 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43669ba0-9a42-3555-a3ca-66ea56e50e60 | -11.17371 | -50.02318 | 2025-09-05 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 347a5b36-7b39-3977-87f7-2cc47648532f | -13.66061 | -47.91386 | 2025-09-05 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b5a6613-c5d5-3801-bca8-8e0f9ede9aed | -9.96852 | -51.63547 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cccd5613-4bb4-3c69-bcb8-a292e1af9819 | -5.91861 | -57.72595 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b3d4ce-9319-3833-a9c5-b705f730dd3a | -8.88701 | -52.05055 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f5c2d3-ab9d-34ae-a26a-577e50d20403 | -11.67843 | -52.16765 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1be500c1-fcd8-3b79-bd3a-7a36af29b4e8 | -7.7165 | -45.16707 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 290a7564-c99b-3559-8d3c-4fb589ce67f1 | -10.67945 | -51.62321 | 2025-09-05 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8b655e9-2220-3b34-bb45-5f490c87ff89 | -9.93082 | -60.10833 | 2025-09-05 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77ecf043-9492-3129-ac08-1913b278c6e3 | -5.8595 | -57.77162 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ba800e-999f-318e-aff2-5f16f9e85691 | -10.76137 | -45.27432 | 2025-09-05 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a00e0de2-ffc3-304a-b0b7-f740cd6314cc | -8.06922 | -52.34602 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ef517d9-146b-3837-ae48-a28cc1dc3347 | -13.10111 | -57.11117 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2393aada-0dcb-3703-adc1-4d60365839f4 | -6.15728 | -53.41591 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1f8a8f4-b517-36b7-b087-5f5f29f3d4df | -12.98533 | -48.05911 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3d5ffe3-1334-3c65-b0b4-4b02db60e846 | -11.59838 | -52.15298 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a85a83-dab8-363b-b815-ecf0b5a13db0 | -10.97278 | -45.98591 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3386a3a-efcd-30d4-ba08-a7f0fb0bb2da | -12.49442 | -53.85312 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5933767-8cfa-3b7e-bb4a-5df5d4790a52 | -12.48613 | -48.07642 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec3b261a-91f6-3a95-808e-201028d2abac | -5.85581 | -57.77091 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b9cdbd8-b9b9-30c2-af5e-c95bc8ea6f00 | -7.77364 | -50.95549 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e0d9b25-9ad0-39f8-a189-3d59d8c54f34 | -8.00984 | -45.44796 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8697438a-c987-3c5a-80f3-3fc3077718c7 | -10.79201 | -56.29906 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425f1822-64f0-3bea-b729-ed381a17d772 | -8.06635 | -52.34152 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 573f8945-3b59-35cc-a5bb-965b862651d2 | -11.58648 | -52.10764 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca0b0ad1-cd0f-3f16-945d-002dd6072187 | -12.29087 | -50.00743 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b28f9c3-8ce7-33c9-8451-ae4fa5dd38d2 | -12.9732 | -48.07785 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c954c134-3293-368b-b736-f83f90497db9 | -7.72141 | -50.32171 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e2d98dc-39e4-3f01-82d3-893ec694bf4d | -7.6921 | -50.30814 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91fd4ca5-7e87-36fe-b65b-3304b37e5b8e | -12.49024 | -48.08204 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c163fc19-2eaf-3d60-9704-c9200b645814 | -10.51578 | -57.77658 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137b57e1-85bf-30cf-8c87-27d15c94fb8f | -12.71951 | -45.09037 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 358b18ff-9ea7-3697-be4b-c59a705fa368 | -10.9784 | -46.00753 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe98ea8e-7453-3ef2-82d3-a7405eee0184 | -11.64867 | -52.21956 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56647837-f9a2-3927-b3fd-74ed1ab4fa28 | -10.05905 | -58.38739 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ae70447-3805-3355-b452-ee16585bfaa0 | -8.05707 | -52.37943 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73a1221c-a612-38b2-9b5a-051c501faa90 | -12.97758 | -54.77795 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69adc4bf-c734-38f8-bc29-ee9a4ff1497a | -11.63659 | -52.22646 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f83d411-2b04-3564-bc2b-b3f9de1c42c4 | -7.68748 | -50.2953 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 704e87fe-750c-3e22-a630-3c43ac8c4412 | -6.2727 | -53.4374 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd0f637d-4be8-3609-abb3-426c88bbe0f0 | -12.32209 | -47.0516 | 2025-09-05 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a274245-d469-3fb7-b192-0571601484d0 | -10.08519 | -45.26315 | 2025-09-05 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a8a442e-6449-339e-b164-192f560a8137 | -9.93546 | -60.10551 | 2025-09-05 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94548eed-00f4-38d0-9dc7-8b4d11732f1b | -12.89702 | -48.02555 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 053e07ad-cda6-3924-9c93-6fc1f885f04d | -12.63421 | -56.98846 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 676313d5-a856-380c-b399-16cf7b8bb29f | -9.37684 | -50.38864 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee57ae59-e706-3b17-8a47-a44c25e66f58 | -12.98151 | -54.79698 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c82102-5596-3329-be26-42367737d98b | -6.83599 | -52.85218 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b554835d-9bc2-3120-bf12-53d4e409aca3 | -8.00449 | -45.44727 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2574dc8c-d3a4-3aa0-a3d2-18991be42d28 | -9.7986 | -48.31413 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78ec3e15-db92-3c43-9355-88e0a2c38d1f | -10.98508 | -45.99768 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8962469e-4096-3e63-aee7-51949754dea0 | -12.8314 | -44.45559 | 2025-09-05 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2f9cf7b-6c98-3e97-abb5-3f5678ed5b74 | -12.95962 | -54.79008 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5c7e0314-31ec-314a-b47f-4f117c057246 | -12.50645 | -48.0751 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dcedae5-14f6-369b-a7c7-61578854f393 | -5.85878 | -57.7761 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d86d71-3a58-3b92-9189-81a13a7cb6e1 | -12.49158 | -53.84883 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbe9079-5901-393e-9828-2f1c5e03651d | -8.09241 | -45.34405 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44d50c9c-e770-3791-abe4-f63e7b4bdd5f | -12.48873 | -53.84455 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ead651a-8ca9-37ee-afec-69f5bb6002e4 | -12.98155 | -54.81905 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2f43987-e24e-3a70-877c-ba0276583da1 | -11.64598 | -54.52762 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7460c9ac-9aa7-3ad3-bc87-3018fbb815a9 | -8.52745 | -51.33289 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c521ebb-e2c3-3672-9498-78d894d196ef | -9.42301 | -46.78446 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b9671b3-1c74-3254-97e6-ff86ba0ab719 | -5.8602 | -57.76725 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5684965-1278-317b-bcaf-09c3390414a5 | -11.20077 | -55.01101 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3346351-8f75-3305-8148-4d6b1cff3e35 | -12.96815 | -54.79486 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d060fc5b-c0fc-3b76-b283-8242aa6bd5e4 | -12.63758 | -56.98902 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba17aa3-05d4-3122-9a7e-8233c3abf505 | -11.62517 | -52.20311 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2c562b9-996e-39b3-8729-3a1c466bb689 | -11.98986 | -46.74932 | 2025-09-05 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc2c1f50-99e5-3df9-b83e-9170438607ad | -8.09648 | -45.35461 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)
