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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb8d607c-1f5a-3396-887a-9683d785fc8d | -9.22905 | -67.8246 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9299f668-8afe-35b1-af45-139cbf1fdda1 | -9.22773 | -67.81472 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 02d357b9-afcf-392f-ab43-238ad7a7960e | -9.22376 | -67.78513 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1c1c439d-f8fa-3968-9880-2d73ca208462 | -9.21448 | -67.78642 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed76f210-5209-36d6-807c-f06a6ef1336a | -9.1958 | -67.85952 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 01931236-04a1-35ce-bf5a-05081cd6740c | -9.19449 | -67.84959 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e53d53e6-5949-3861-9bd8-50060fc9b47b | -9.18871 | -67.85666 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c6b8baa7-440c-33a5-845f-ea7eeba1fdeb | -9.18736 | -67.84675 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08737ba7-42a3-3e1c-b7f3-3f6343bf4de2 | -9.0607 | -67.87026 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df0ee5d0-cacb-3aa2-81cd-3c780141d0bf | -9.05936 | -67.86037 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2b3c6bbf-550b-347d-8119-d03701765ac5 | -9.0514 | -67.87156 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8eb95f17-3b13-3804-9a10-3c3381bbf902 | -9.0514 | -67.80121 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aedd2707-1455-3380-938e-e72bb18c437f | -9.05007 | -67.86166 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| eb7471a2-624c-359f-98f5-2567fd7f1639 | -9.04213 | -67.80249 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d96c5b36-6cd9-3035-8c69-ccbe53d09011 | -9.03676 | -67.90392 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| effc213b-5f79-39fb-85f0-8a6528eb5a90 | -9.01705 | -67.75605 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4bed925d-179d-3426-8982-0cf9c2f1c904 | -9.01575 | -67.74628 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| be521dc0-0915-3dca-adec-14e95b6e9263 | -9.01444 | -67.7365 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5610098e-9cbd-3904-9347-b5f3c790b2f1 | -8.99892 | -67.81473 | 2024-10-03 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed6d8b69-8a23-3fd5-8969-5557e27fcc84 | -9.74895 | -68.42547 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e5c27f15-f67f-3cbc-8237-96573c68aa66 | -9.74069 | -68.43755 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 92a51a4c-3485-3063-809a-7788f5fbc50e | -9.73929 | -68.42677 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 48e97a3d-94fe-3d93-b71a-280891070b52 | -9.73102 | -68.43887 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f9c71c43-93cc-3386-9da2-3c7672d3b6c8 | -9.68652 | -68.81645 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61d1d6db-2b3f-33c8-8954-fd37cf09e68a | -9.64293 | -68.64036 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d15a7986-a0de-3ed1-9c0b-fa4049bf50c4 | -9.63316 | -68.64175 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d157a118-fb39-338e-9fce-5d5febf25e40 | -9.6317 | -68.63068 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 50e0c473-4170-3974-bcb0-4cfb8db36ec3 | -9.58834 | -68.6031 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae454813-b489-38d1-ba15-354d4ce12f0e | -9.58691 | -68.59219 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8e6a95cc-4bb1-3753-a160-d896de1155f8 | -9.55445 | -68.26971 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 17eaca87-f21f-3833-80ed-b69068c76634 | -9.55307 | -68.25923 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c94a3ba8-7023-387f-9d40-135ec8d12140 | -9.51483 | -68.44269 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7649141f-d0da-370a-90f1-8dd5117603a9 | -9.5066 | -68.45464 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c0956806-7690-3aff-83ea-0dd25de9b6e3 | -9.50518 | -68.44395 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cd0e23db-78cf-3ae1-8c2e-376ecf321b3c | -9.50264 | -68.49902 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f5c683be-d99e-34d0-9741-6753cb8ecdd8 | -9.50121 | -68.48824 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 44b23fa1-0ee4-30aa-a161-e57af8076a96 | -9.4974 | -68.05618 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ade89727-79a0-3f5d-998c-7a57375883ce | -9.49296 | -68.50031 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3de2f447-4555-307b-8912-0758cce4ad62 | -9.49154 | -68.48952 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 77b3d694-277d-3f15-a0d7-f3acda6a7ee8 | -9.49035 | -68.55572 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 15.8 |
| fec40729-5d03-3e4e-a9c5-273a9fda5bb8 | -9.48892 | -68.54482 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e92cfdbf-d858-3d49-8927-2afc1fd63bb5 | -9.46589 | -68.5432 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f7d8a98c-16a1-3fe8-b54b-fbefacaea7bd | -9.46531 | -68.51494 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 19.3 |
| fcda8750-162b-33c1-ab59-29654e7ab89e | -9.46297 | -68.52157 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 79990c9c-6bb6-3909-b89e-e5f72e72d2f0 | -9.46151 | -68.5108 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a023f129-343d-3ad2-b471-911f36cde262 | -9.44795 | -68.55666 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8089132c-b596-3187-95bf-cf2729b9ae90 | -9.43288 | -68.592 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dae9c757-a243-3526-8610-efb1c5ce14c3 | -9.40363 | -68.15448 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 30.3 |
| e62fd2ff-9505-3717-a9b3-f631dda7c05a | -9.39855 | -68.26058 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b28d936a-22ec-3aa4-8a58-b0fdbce0cceb | -9.396 | -68.31424 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b1f7d0c0-7f41-3d6d-9a36-22e95eefd180 | -9.3946 | -68.30375 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 24.4 |
| d1104681-0d16-348a-a644-f46a01a94f5c | -9.38922 | -68.33652 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e84dd60d-d72f-3a5f-9339-98bb6fbc2d36 | -9.38783 | -68.32602 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7bea9bee-405f-33e5-95e2-b06fb5f125f4 | -9.37964 | -68.33779 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1d547a63-efbc-35a9-b1df-9541b0630ca7 | -9.37826 | -68.3273 | 2024-10-03 02:09:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 46a468ea-8809-3974-9ae3-3fbbf19a9369 | -9.36814 | -68.79734 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 64f95714-f349-3340-baf6-3603841dd913 | -9.3583 | -68.7987 | 2024-10-03 02:09:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 65e2ed52-80d9-37ef-b27e-489aad5d9dc6 | -10.00187 | -68.72648 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a89ac658-17c8-33d2-8821-011fc49f1792 | -9.89488 | -67.58315 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 921e5e63-bf4f-3fb4-8cd6-1ae6f298cc62 | -9.63331 | -67.47935 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4ba45cc5-4fa5-3aac-a533-1249d2c6852c | -9.63201 | -67.46966 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 43fb3af3-7d2d-3a6c-955c-58df84fd5844 | -9.62283 | -67.47097 | 2024-10-03 02:09:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 81e555bf-2dfd-3fcd-954f-950267debdca | -10.53043 | -67.85705 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c43d1afc-0f4f-38b6-b18b-fc079757b5cc | -10.52906 | -67.84675 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2025505-c2e2-3e63-8225-4209412f79fe | -10.5075 | -67.90206 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b018d4ab-d3ff-397d-99ce-3220b5cf2235 | -10.50615 | -67.89177 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3ec32d94-90b1-35ad-b4dd-08245ab1e10a | -10.43832 | -67.9286 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb8d64d4-e6b9-3664-a9a0-516985d5879b | -10.3434 | -67.97904 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 92310694-0d55-32f4-b098-3d20e0015cb5 | -10.34203 | -67.96867 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ec76237-9eb1-3023-a5b2-c1b811acb9f7 | -10.33391 | -67.98036 | 2024-10-03 02:09:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b2e6c06f-3209-321c-9eee-1182000a6f4a | -10.31898 | -68.01408 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9bd6f048-1cd5-3df2-a586-485448eae325 | -10.31764 | -68.00374 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2ca92af0-3533-348b-a55c-ec10f0f3fb68 | -10.31364 | -68.01059 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 12ab75a3-fa52-3144-95c5-e937aa7c6e72 | -10.31224 | -68.00024 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 271a5c2c-8a40-3c69-9b96-8cb20032a5f0 | -10.26615 | -68.01713 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3199eb7-9d81-3db5-ba12-54c2ecd3f0e3 | -10.17549 | -68.17388 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 81adce53-c70c-3a93-8103-3e1e8fc1f573 | -10.16592 | -68.17521 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 00621be1-6890-3f53-b57d-6fb20bf39597 | -10.16487 | -68.34451 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b96256d0-d1ec-3f42-afa4-71bef7536922 | -10.15631 | -68.0275 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d07abcc-44cf-319c-bdc4-825d02a5b02d | -10.13045 | -68.01628 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 277268c1-a4a7-3e57-b994-46e69095626a | -10.11739 | -67.73203 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7e1a6342-85f8-3fd4-9d82-e82b9999aa58 | -10.10805 | -67.73334 | 2024-10-03 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 20.3 |
| fc967ecd-9bf5-3b35-9324-db2382c14dde | -10.10673 | -67.72333 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 91734bf1-6d66-3d9a-ba10-380ca1f39dbe | -10.06802 | -67.83755 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d0ee3fe8-8093-354a-81f6-085297e96ddb | -10.06667 | -67.82744 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04dd91a6-4151-38d7-a13e-33295cac0dcc | -10.06547 | -68.03585 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cd5b6dbf-7550-308e-be9e-c47b8b71d571 | -10.04121 | -67.85157 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98ade597-c74b-300b-b584-8e0cedbcd352 | -10.03981 | -68.46672 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f12315e0-7eeb-34df-997f-07859e40e722 | -10.50648 | -68.67931 | 2024-10-03 02:09:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4ad93e30-f76b-3708-842d-cab0fafcf7ee | -10.50501 | -68.66785 | 2024-10-03 02:09:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ed4a60fc-6ade-37ff-9867-50e2fa5b21cd | -10.31614 | -68.70556 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0625041-a93e-3848-ba49-1ce541c28bf6 | -10.31586 | -68.71142 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0efe13da-d92e-315e-91de-774df7c87225 | -10.27375 | -68.77523 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8ee14cb2-3d20-36c3-8800-a5a2d02a927d | -10.27226 | -68.76379 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7b6f9efd-ce2b-3cff-852c-e6db21857eae | -10.25238 | -68.76649 | 2024-10-03 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e76052b6-585f-351d-8832-3c96734719cc | -10.97724 | -68.45824 | 2024-10-03 02:09:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7a2370c6-32d8-3dc9-8a2d-b590663f64cd | -6.88263 | -59.05437 | 2024-10-03 02:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 3d6cdff8-b278-315a-821e-0f2b0384993a | -6.87909 | -59.03139 | 2024-10-03 02:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 23b161f0-6c2c-33b2-9b79-2e619138641d | -6.87522 | -59.04982 | 2024-10-03 02:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1a1fca91-4a56-3eb2-b61c-2f6aa0fb3a25 | -9.16424 | -59.38523 | 2024-10-03 02:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |


[Clique aqui para ver as próximas entradas](README51.md)
