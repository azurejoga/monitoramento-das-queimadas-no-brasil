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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8645c4a-b14a-3852-846b-64a9bf8f29bd | -11.30349 | -51.33982 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a794368-a32f-3d67-8f24-8979f9d402e2 | -11.30307 | -51.02075 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e127d8a-6c97-3f57-af02-7f44d99fcc49 | -11.30303 | -51.06358 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 863e563e-566c-34dc-a5c2-135d69b70477 | -11.30286 | -51.34369 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04884f50-922d-32e0-874c-999b83eb299c | -11.3024 | -51.06738 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c9d7131e-a3a0-340e-a312-6d227c41e37e | -11.30177 | -51.07119 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 954143fc-a208-3dd1-b19e-a972e33792e5 | -11.30114 | -51.07498 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e72f13c3-551d-33b0-8eba-4e6a22747620 | -11.30003 | -51.33924 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e970cb45-d91f-32fe-b390-cb3aa4712aea | -11.29897 | -51.0668 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 996dac14-1c61-376d-987b-0fc20b7192d2 | -11.29834 | -51.07061 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ad102ef-0fbe-3422-bfa6-50dbed260368 | -11.29771 | -51.07441 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beeab224-c6c6-33f9-9860-72a17247d4cb | -11.29182 | -51.34584 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb85980-7530-3e6f-8c9a-c21caf1a74ec | -11.26632 | -51.41366 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 827ecbbc-4b45-3066-ada3-ca7a4b613e7d | -11.2558 | -51.284 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7775e6ed-0978-3944-8770-8fdd4f5d51ac | -11.25539 | -51.30784 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 458ebbf6-ea00-30f7-b01a-9c38ae03f882 | -11.25524 | -51.41582 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96cde9ca-a396-36ce-8ea7-144118214cbd | -11.25299 | -51.27955 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73740db3-e3f1-3ff9-8d15-e1e9121998c2 | -11.25234 | -51.28343 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e182223-5bc8-3034-b41c-7617c6e7dc8c | -11.25176 | -51.41524 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e02865cc-e141-3c1d-afa9-e2a88a1e5868 | -11.25017 | -51.27512 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bb4885b-be31-3bc3-a761-1413a987cf54 | -11.24888 | -51.28285 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e216bae5-ca74-39f1-939f-b4fdd67a4a15 | -11.24784 | -51.27534 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8d1b8a05-c474-3ff9-88e1-daffa45dab95 | -11.24721 | -51.27921 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 259c4f8d-2c2a-3176-8599-fbd44c1d90f7 | -11.24658 | -51.28308 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80f23422-1d05-3675-a013-efe81b062fbf | -11.24542 | -51.28228 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beae9834-aee1-399a-b1b0-2f7f80f86a69 | -11.24312 | -51.28251 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf572061-a520-342d-8606-9e471833ad99 | -11.24249 | -51.28637 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e6a0ef-747b-3755-bd7f-f0081daec5b8 | -11.22927 | -51.28019 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7f13581-4899-3c2a-8f36-c71c5aa646f3 | -11.22864 | -51.28406 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11028cd0-e4b6-3646-a2ef-e7f3d90e04e4 | -11.22062 | -51.39864 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfecb66d-561a-3da7-9a07-aca9101f3b13 | -11.21495 | -51.38965 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd770a16-e9cd-3712-9981-636f66ac44ec | -11.21431 | -51.39356 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f674756-8048-3916-ad56-f328688d37cf | -11.21147 | -51.38906 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a310b0d5-0b42-3b0b-a9cb-95edd457f4a8 | -11.2099 | -51.18189 | 2024-10-08 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 415d70db-a1b5-35d9-a97d-3f80f9a9e3d3 | -11.20864 | -51.38457 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1e857ca-82dd-37be-9d84-29e4e343fec1 | -11.20644 | -51.37618 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d18412f-83bd-3392-a8d2-92050b92b18c | -11.2058 | -51.38009 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b38fc1b-d2d0-3d7e-9aa2-68135c8d8c4a | -11.20361 | -51.37169 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb8e06e3-040f-3f54-82dd-0bd3a09bea96 | -11.20297 | -51.3756 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10e49e7e-5799-3134-806c-577ca071399f | -11.20206 | -51.35941 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b548285a-0785-3b55-9bfd-dd8106e71cd2 | -11.20142 | -51.36331 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b6d5944-3b47-312e-bc36-326a69cdd281 | -11.20078 | -51.36721 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b35fb2c4-9b49-39e7-9e26-7d711c704e3b | -11.9852 | -51.91858 | 2024-10-08 04:34:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d36b9cc8-a787-38ab-a754-975d0a0ebc5d | -12.63251 | -52.43461 | 2024-10-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0766df56-0a50-3b6b-a258-2753d87e3c52 | -12.62892 | -52.43399 | 2024-10-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cd13f84-b2da-308d-b698-93d21c85c19a | -12.5909 | -52.46206 | 2024-10-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72a2ae71-9dcc-3023-a02b-6777ada2dc2f | -12.60695 | -52.22177 | 2024-10-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5409eee2-565e-3e87-b8c8-26e60a42ac16 | -5.88004 | -51.58772 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc557e7a-15b1-392d-b7f9-0744cf712fce | -5.79829 | -51.60926 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48aea4ed-035a-32b2-be46-20942a1ae841 | -5.79755 | -51.61375 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b01cb3e8-fb95-3454-88d8-708028518170 | -5.7758 | -51.45501 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b5e2bac-2713-3ae4-a8c0-2c0b121431a2 | -5.77424 | -51.45375 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10583906-78bd-3001-969a-afefaf7cba6b | -5.7728 | -51.44995 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9f0fab-3f0c-3542-a089-d8e0a009f34e | -5.77209 | -51.4544 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af50cf1-c4a5-3249-9a11-38ab555ee512 | -5.77127 | -51.44871 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f104378c-8439-3700-8cc8-f2c33c6125bd | -5.77053 | -51.45313 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04e1fb15-752c-3762-a9d5-40a4849afbac | -5.76909 | -51.44934 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48758494-857c-3b47-a22e-e247a180745b | -5.76838 | -51.45376 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f30a23-e5ac-38f6-9fc0-756a02bdba61 | -5.76756 | -51.4481 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1dc6e25-8815-3260-bbae-7a5570ab6be0 | -5.76682 | -51.45251 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f283ed45-e719-3981-b250-0f6c4116f4f3 | -5.76538 | -51.44872 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e457acf-fd88-33c7-af53-feedbc709337 | -5.76467 | -51.45313 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e08a14e-18ac-3855-ade2-7c357e12d1f4 | -5.61556 | -51.16581 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 460cf6e3-a7ff-3c77-a475-c211630f77d1 | -6.41979 | -51.7081 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c1351d2-7f5b-33c5-a505-461e7dfe00a6 | -6.41904 | -51.71258 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cc2a976-a553-304e-b27b-cc9113f7d671 | -6.41606 | -51.70745 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cb66a08-b54e-3727-9e29-3f913c57db38 | -6.41532 | -51.7119 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e54085b-8c4a-3bf2-b319-7d3358100b2c | -6.24528 | -51.72596 | 2024-10-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b78171-b7f1-363e-a2b5-941a0c0e2e78 | -10.70142 | -53.03286 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cdf384c-6b1e-346a-a93b-ff19c0920957 | -12.6753 | -53.19245 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29271337-d42e-3295-8ee2-a19eef6b4665 | -12.67436 | -53.18946 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0758f668-8e4d-3a77-9f52-0dd70cc6f6b8 | -12.67237 | -53.18721 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52fe0e87-4576-32d5-be9a-0804124e828c | -12.67157 | -53.19179 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39589e13-c0a7-33f3-9ca9-26ea5f3a39ea | -12.67063 | -53.1888 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e756b00d-5117-332a-93cc-de050201cc46 | -12.63387 | -53.11199 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 761166b4-b72e-3d90-b359-b478e7035696 | -12.63309 | -53.11652 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 441700ac-f33b-375a-9d38-785e8c6b8afa | -12.63275 | -53.50195 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a26f2a6-6e95-351a-bf3c-7747ea843551 | -12.63016 | -53.11133 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4e681ea-e581-3de8-a4e8-33f185f1bf9b | -12.62938 | -53.11588 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b31bf9db-5ae2-3e07-be70-f5ae5d68fa04 | -12.6286 | -53.12041 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e799355a-d8af-3f12-8a3a-5c4c2f5c2cb4 | -12.62782 | -53.12494 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c973796-aa74-30b2-98eb-67a03050e8a1 | -12.62488 | -53.11976 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 834f4b04-f337-3302-b6d7-260801846d30 | -12.62411 | -53.12428 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab5b3296-73fb-397f-bd26-97985bea6849 | -12.62117 | -53.11911 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9cc905-bbdb-3c8e-bc9d-76a3be95b555 | -12.60845 | -53.12623 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82abbbec-8ab9-38fe-bbba-0c84f87e7d2b | -12.60474 | -53.12557 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc77c50-0770-3bc9-bdb3-94b15e95e0b5 | -12.60395 | -53.13011 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 825e913a-5601-37d0-a597-1d81c2645f05 | -12.6018 | -53.12038 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52b9261b-8fa0-34d9-bc2a-dd209d91fd7b | -12.60102 | -53.12493 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e58f97bb-f878-3d02-8e71-118a0c126c75 | -12.60023 | -53.12947 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b48ca5d-2ea1-37c5-9f33-368fb8596b9d | -12.59945 | -53.13401 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f088e8b-2895-39e1-a3b7-c73378331559 | -12.5973 | -53.12429 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbe4e9e4-78a4-360f-b951-00c82a38b86b | -12.57844 | -53.06609 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| fbd6caab-9b7c-3285-8166-b311fb3bdbf2 | -12.57768 | -53.0706 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 6800071a-8c87-30f0-a97e-e9ee905874c0 | -12.57707 | -53.06471 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8b94f537-40c2-3d7d-ab0d-c1026310c4af | -12.57628 | -53.06921 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 39727f29-c7c1-32f3-bda6-0efc53b98cb4 | -12.57549 | -53.06095 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd327b04-d653-31e9-9e88-311387237d52 | -12.57473 | -53.06546 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| e1e23fcf-c40d-3679-951b-168e5990ef30 | -12.57397 | -53.06995 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| da0f9dff-4fb2-37c6-95a3-4f17a454171c | -12.57178 | -53.06033 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README59.md)
