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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c646aa6-cf06-34c0-8f86-765077e10850 | -16.68636 | -55.88175 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4364d3ff-d73a-3f96-bcc9-bd0a0467ec04 | -16.68633 | -55.92622 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 776ce17a-e34c-3ff1-9d28-e0b011eca7d2 | -16.68412 | -55.91844 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e8d7d1c4-7be2-398c-8bd4-ef9cbdabfa56 | -16.67636 | -55.94678 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 77dc02fd-2e7a-35ae-8ed2-4d151bad2981 | -16.6758 | -55.95039 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7ef9a1ed-93b5-3f45-b47d-26e895d2f4a9 | -16.67359 | -55.94262 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 45ea6c68-7b84-3d54-86ef-e59000c52741 | -16.67169 | -55.91262 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f3816ad9-c6f5-30a7-a164-a81aa33fa6bd | -16.67113 | -55.91624 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3008c14f-b9cc-37f7-9130-3d55573e8a9c | -16.66837 | -55.91208 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 82035eea-86b5-349f-ad07-ed67f17fe647 | -16.66781 | -55.91568 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dba62ef2-bcce-377d-951c-96fbe2b5eff2 | -16.66504 | -55.91153 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ce174df8-1d2a-34a7-8625-005d20e6c9b5 | -16.66449 | -55.91513 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e541fd50-53f2-3622-bf84-2b1e590d6fc4 | -16.66173 | -55.91097 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a78bd768-883a-3d1a-bd53-998885782bae | -16.66117 | -55.91458 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5a17b46b-2f27-323f-85c1-c05e8994a4e3 | -16.65785 | -55.91404 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| af8c2fad-1866-3596-9224-703050cf7320 | -16.65729 | -55.91764 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 24eae1e0-14bd-347e-8e14-a699d06bea2f | -16.65397 | -55.9171 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 988c5b1e-f7d6-358e-b2db-e73836af7b80 | -16.65177 | -55.90932 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 238b6834-09f7-3202-9401-177f4e9869f6 | -16.64845 | -55.90877 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| db526048-2909-31fe-ac02-f9566e13fa20 | -16.64013 | -55.9185 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b702bda9-ed26-3df5-a360-fb0181e03243 | -16.63737 | -55.91434 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 91d94c14-57b2-36b8-b8f5-481605cc80f2 | -16.63681 | -55.91795 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e3bce9ab-25ae-3802-88c9-5381f2ed22cc | -16.63405 | -55.91379 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca7a8fdc-1484-3124-8b3e-997f940c1eb2 | -16.63349 | -55.9174 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5b0387b9-b0dd-3f6e-8861-c6c98bf108fe | -16.63017 | -55.91685 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1243d6b7-57da-33c8-9557-9a4bb244bffe | -16.62741 | -55.91269 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d52c87ab-9717-3c9e-abb5-1b28b2a8ec6d | -16.62685 | -55.9163 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| edf3ed74-2e1a-3b76-9c51-57aed11d6726 | -16.62409 | -55.91214 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 78a9cc61-e7b3-3ce4-a92f-38fec1c61a5e | -16.62353 | -55.91574 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 752e2f87-52af-332d-8e9e-25e7b1c3148a | -10.57034 | -56.55985 | 2024-10-04 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9a9dfd7c-6f32-30f6-b70a-a55994a4ac04 | -10.56697 | -56.5593 | 2024-10-04 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bd29fcf2-08ca-398d-a00d-0b9cc3d217a9 | -11.92792 | -56.95113 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26f305ca-0b3e-3670-ae32-15e7a9818e59 | -11.92733 | -56.95481 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c4ec6c8-dc16-32a3-8d1f-c0718c20d453 | -11.92455 | -56.95055 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65627a6b-0420-300d-bed4-f5f74c8a1bb2 | -11.92395 | -56.95423 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f77bc95f-294f-38f3-9715-ef776db1d5e2 | -11.92336 | -56.95791 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fea49fd-373c-388f-9651-8839459c05e2 | -11.92276 | -56.96159 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92dc996-061a-3196-8da1-51c391ec8aae | -11.92117 | -56.94998 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45543afa-3890-3368-84bb-6b42e5c83d2e | -11.92057 | -56.95366 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa99f034-b103-3f88-8510-71ca1ec00db7 | -11.91838 | -56.94572 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2f628c-222a-3f9e-afd9-b4059b203dfe | -11.91779 | -56.9494 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb5df40f-3b70-3695-8f75-9fb629a9cc2e | -11.91719 | -56.95308 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fa81032-9082-315c-818b-0b1126ab38ae | -11.915 | -56.94514 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71ab26a4-2137-3d21-8aef-4a02b35641fd | -11.91441 | -56.94882 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec84276a-ac56-3f7a-918b-4acd164eddcc | -11.91381 | -56.9525 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a1d69ca-4ed8-340f-9b6f-4631bd4ea636 | -11.91322 | -56.95618 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b438c9-10b4-3b4b-8247-36ef7a80fdca | -11.91262 | -56.95987 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26d0b65-a8c5-3d49-83ce-fad80b8a53d1 | -11.91103 | -56.94825 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 897f5c9a-9000-3311-b7f1-789a62c457ff | -11.91043 | -56.95192 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d0a12fd-745e-3c0d-8845-beabaf6526db | -11.90984 | -56.9556 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21cef9fa-0798-3144-9350-11b639ba23ae | -11.90705 | -56.95135 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5f31bd4-41e3-3d55-b371-6bf1961c24a8 | -11.90646 | -56.95502 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64fb797f-547f-36ce-8eeb-9dad59dae7be | -11.90367 | -56.95077 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5216beec-8fc6-365e-8f9c-623a6d987f52 | -11.90308 | -56.95445 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af003441-6c77-3ecf-9f06-5b111344c291 | -11.90089 | -56.94653 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee67054d-1ab6-3859-9149-a9e5815b6eea | -11.90029 | -56.95021 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759a7742-7c14-3c60-b2e1-5d7fc9fa0dd1 | -11.8997 | -56.95388 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b48d9646-a747-30af-8005-169c5dbb063e | -11.8991 | -56.95756 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c604994-8cdf-3f70-959e-189424d78ff2 | -11.89691 | -56.94963 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7876c2de-4678-306d-bcf9-7995e44c886d | -11.89632 | -56.95331 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ede64f0-ce46-3a6c-995b-50a27aee8a03 | -11.49138 | -56.7888 | 2024-10-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f535084-3ac8-3af6-82e8-6b52075c5ec5 | -11.49078 | -56.79245 | 2024-10-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c656b548-7bb7-31d2-ae83-9d863cceb222 | -11.48741 | -56.79189 | 2024-10-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0d855d3-ae71-34bb-a8b0-7006a3424ac7 | -11.88966 | -56.2144 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e4d11a-2236-39e1-a7a9-81018ee71460 | -11.88862 | -56.19963 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d22ad709-de73-3cd0-9e95-24996f9ec135 | -11.88805 | -56.20319 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 568aa223-1f53-3fc0-9671-8b509dae127e | -11.88748 | -56.20674 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbb53ce8-1023-3933-923b-b2d273056ae7 | -11.82239 | -56.58965 | 2024-10-04 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3a4fa97f-f65f-300d-892c-5505ee55bcd3 | -11.488 | -56.78822 | 2024-10-04 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90702dfb-a55a-3621-abdb-ba53d9d41c34 | -13.06841 | -57.25395 | 2024-10-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6c91df-caa1-3cea-b25a-7345863450db | -13.06503 | -57.25338 | 2024-10-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2f4effb-20f9-3cc2-8776-7d64d4fceeb1 | -13.06442 | -57.25709 | 2024-10-04 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb6a2e73-29fc-3fbf-804e-a5a88ced7478 | -12.61061 | -56.48648 | 2024-10-04 04:57:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c07d1125-fa20-3553-a9a2-c63b227e473e | -12.61003 | -56.49007 | 2024-10-04 04:57:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97c0c58b-b773-3eac-b8b5-070cf69e285e | -14.98551 | -56.44513 | 2024-10-04 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c986c67c-fee2-3dfa-8fdf-fd5deb0aa6ce | -14.98163 | -56.44814 | 2024-10-04 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 418f1739-cdd8-3ad1-a1ae-ac48fc1b6a2c | -14.98106 | -56.45171 | 2024-10-04 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18c6cd20-d1d0-39a4-a130-2f53ad2efa3a | -14.98825 | -56.44925 | 2024-10-04 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8c703d1-e4c1-3973-8bfa-21ee0ca7898b | -14.98494 | -56.4487 | 2024-10-04 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 080bc950-581c-30c5-b771-04cf1f0c46a1 | -16.44875 | -57.57544 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 79feeca9-8276-33dc-a023-be6ad2cfc6e5 | -16.5223 | -57.26934 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 17e92979-aca8-3e7f-a05e-2fdd91f55701 | -16.49882 | -57.28765 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3c134cc4-1b44-3fec-8073-adf01fc0950e | -16.49374 | -57.29797 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 74871f8b-09ed-339f-ae12-eea9cc2636f2 | -16.49041 | -57.2974 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bf843981-b7ca-3ae9-af63-412dee5f0ee1 | -16.48375 | -57.29625 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fac410c4-238b-3e5e-bde4-a146fb971087 | -16.47709 | -57.29509 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 9d5280a0-90fd-33c7-b640-f8c1aa6f855d | -16.4765 | -57.29873 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 33994759-3d06-3324-97bb-aa01d77eb8fa | -16.46651 | -57.29699 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3e81e400-350c-3dc7-9426-175811b26979 | -16.46377 | -57.29278 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5fe0605b-f69c-3b8f-9532-35af4020de86 | -16.46318 | -57.29641 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f2eb04b3-db5a-3175-b114-c3a94263e8cf | -16.46044 | -57.2922 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7c260133-1695-3ae5-9823-e7c03417b972 | -16.45985 | -57.29583 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 97c97eb3-271a-3cc0-b080-15ff30262f03 | -16.45868 | -57.30309 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3d47e97c-2d77-3f94-af4c-7e0563af999d | -16.45809 | -57.30673 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e2f237d-4880-3146-8b6a-d350fa109243 | -16.45417 | -57.30979 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e62764cc-3606-3d77-9837-0870741646e8 | -16.45386 | -57.29478 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4b9c71bb-73b9-30e3-99e4-4db50af2857f | -16.45328 | -57.29842 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b4475aa-b3fd-3cf0-93be-81ef020d5ec9 | -16.4527 | -57.30205 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2472f245-e2fb-328a-b401-62fe363efa52 | -16.44604 | -57.3009 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f8826730-d2a1-3b9f-917d-4b93d1c4d451 | -16.30521 | -56.71352 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README162.md)
