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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7ede3fe-064c-33e6-8151-be4a19afae56 | -11.13952 | -53.94319 | 2025-06-05 05:59:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e75249c4-306d-3f87-8af5-bc8ad71792b7 | -10.67349 | -44.37923 | 2025-06-05 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2f92d336-2956-303b-b08d-de0bcf36d655 | -18.94946 | -52.49422 | 2025-06-05 05:59:00 | AQUA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ec09f95-b409-3b3e-918d-8bbb1557437a | -10.67368 | -44.37217 | 2025-06-05 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 65ea8554-f4ed-30e8-902c-012462b76b7b | -10.65196 | -49.42722 | 2025-06-05 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c42f79b0-218a-3687-823b-f7c7424ea282 | -18.84192 | -53.61506 | 2025-06-05 05:59:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e6224bec-17a0-3aeb-9e75-95c1d377241e | -10.8162 | -56.95835 | 2025-06-05 05:59:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b4492b4d-f1e3-34f8-8c11-84642f932cb3 | -13.52374 | -56.5536 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 11a97b72-1e47-3f42-bd1f-51df98934eef | -11.49564 | -48.37849 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 07f594d6-d909-3a3c-bfc8-e29b07194448 | -11.54741 | -56.43522 | 2025-06-05 05:59:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7940e89f-d03a-3e0a-bda2-5aff2feb3293 | -10.49697 | -53.65093 | 2025-06-05 05:59:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f20decfa-f4e1-31d5-a03c-74e387eb6616 | -10.81981 | -56.94684 | 2025-06-05 05:59:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c3c0dbc4-593e-3990-8be2-e6bc11597985 | -13.52108 | -56.56928 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 211.1 |
| fb10d101-b644-3bee-9655-58ba1a1d0583 | -18.84044 | -53.62461 | 2025-06-05 05:59:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e8a74b65-6f2d-38a2-afd9-bdc82a21374a | -18.83151 | -53.62314 | 2025-06-05 05:59:00 | AQUA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 30659991-d716-3d9b-bdd4-0bfe62d7ce2a | -13.5123 | -56.55165 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4b801995-0f5b-3b7d-af75-35d89ba6b1eb | -11.50147 | -48.37417 | 2025-06-05 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4d3d1927-04cc-345c-bbe4-ee31d878c1b3 | -10.6506 | -49.43655 | 2025-06-05 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c8ec1112-86eb-3c4d-ad74-0d8e1f4ec165 | -18.8479 | -53.6251 | 2025-06-05 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6ac73a1d-11c3-32bf-9a5c-ef633041c235 | -13.4961 | -56.5709 | 2025-06-05 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 5f40a0bd-2519-3961-9071-671baafbf48c | -13.5155 | -56.5488 | 2025-06-05 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ee01acfd-f28e-359e-8e48-366711408d59 | -13.5152 | -56.569 | 2025-06-05 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 454851d9-b73c-3f5c-a796-91ce0c438803 | -13.5344 | -56.5672 | 2025-06-05 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 66c5e53b-f247-3037-998e-f4634d03d554 | -13.5346 | -56.5469 | 2025-06-05 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b9d5581b-f977-31d9-aa5e-4bf2612caa67 | -18.8279 | -53.6283 | 2025-06-05 06:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 58ce90f8-af87-3cd0-a587-df4e2a95987f | -13.5344 | -56.5672 | 2025-06-05 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| b872139f-8262-3bfc-89f6-048fb4e8aa0d | -13.5155 | -56.5488 | 2025-06-05 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 24c93834-1d0c-35aa-a123-9a36000483ef | -13.515 | -56.5893 | 2025-06-05 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a934e26f-67c2-33b1-8ccc-fcaaf9b1d3fc | -13.5346 | -56.5469 | 2025-06-05 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 16d76e92-0ef2-3f42-a754-0985bc0d0a0e | -18.8479 | -53.6251 | 2025-06-05 06:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a19d6816-1ae4-3d08-a899-2227165a1c2c | -13.5152 | -56.569 | 2025-06-05 06:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 293.2 |
| cabebad4-e48e-326b-9378-aa7c6b7b132e | -9.24425 | -63.29251 | 2025-06-05 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03787696-a690-34b2-a465-fd2d2c3fda6c | -9.25066 | -63.28893 | 2025-06-05 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7f59137-4d56-3238-8fba-b13854f93fb1 | -9.2458 | -63.2895 | 2025-06-05 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a641e5ee-71dc-32af-bd63-e8aef36d388e | -9.24524 | -63.29375 | 2025-06-05 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0767a6a6-8975-35a8-a531-0ec082d9bd9d | -12.0149 | -63.78942 | 2025-06-05 06:16:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afec38b1-8606-3f7e-a06f-c51ca4c0d4e5 | -18.8279 | -53.6283 | 2025-06-05 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 81218e0c-4b02-3052-80ab-557f0329e1eb | -13.5341 | -56.5874 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9a2ec78b-f00f-3930-8d36-05900e51b4a4 | -13.5346 | -56.5469 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0854d16b-2fc6-3725-89ee-a587177cc958 | -13.5344 | -56.5672 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 833c0a8c-b4cd-3ac0-87ca-cfd150e37fe9 | -18.8479 | -53.6251 | 2025-06-05 06:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| cc63bb19-6169-3a3a-ae41-ffea24ff1ef8 | -13.515 | -56.5893 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1ffdb58e-71c3-3e2e-b5b4-d3a2a3a6a8cc | -13.5152 | -56.569 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 216.2 |
| f3f504cb-f738-3000-be99-df3f886ab128 | -13.5155 | -56.5488 | 2025-06-05 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 068acc90-7499-3d04-80eb-fe7d08a3d75f | -18.8479 | -53.6251 | 2025-06-05 06:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.4 |
| ed2b9105-d63a-3336-81b5-53b4233e2d55 | -13.5152 | -56.569 | 2025-06-05 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 261.9 |
| b8ab574b-bdc3-3d1e-b7ea-d5c2b16c23cb | -13.5344 | -56.5672 | 2025-06-05 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 6899a442-e08f-3463-9d7d-4169b0254bd8 | -13.5346 | -56.5469 | 2025-06-05 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| fb6dedb6-7a61-3852-bc81-d897f6fda5e6 | -13.5155 | -56.5488 | 2025-06-05 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e82b9eba-054e-3491-a076-568d3e924eb9 | -13.5346 | -56.5469 | 2025-06-05 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 455603e9-3238-3b92-91a6-8495aa820b0c | -13.5155 | -56.5488 | 2025-06-05 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| dc3df4a1-d8db-3f63-834f-95f0cd8f992c | -13.5152 | -56.569 | 2025-06-05 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 203.9 |
| e9f6b462-074d-3615-8c67-86f83f3b575a | -18.8479 | -53.6251 | 2025-06-05 06:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 587d54b8-bc0c-3232-89c2-9d359b5aaac3 | -13.515 | -56.5893 | 2025-06-05 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 389473fc-b35a-332c-8e33-57120408c9bc | -13.5344 | -56.5672 | 2025-06-05 06:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 81e013ef-024f-3657-9cb2-4af45ea76a01 | -13.5346 | -56.5469 | 2025-06-05 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9eac94ba-4ac4-3040-8da1-74b2669a546e | -13.5152 | -56.569 | 2025-06-05 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 2890f2fd-c3eb-3a99-b484-eb492e39e5e3 | -13.4961 | -56.5709 | 2025-06-05 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 77fd2068-9833-3a16-a34a-368e7bbe9a38 | -13.5344 | -56.5672 | 2025-06-05 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| f64a4350-50a5-3f8f-82a0-61da34977d89 | -18.8479 | -53.6251 | 2025-06-05 06:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 4179759a-7735-3dae-b7be-b6034f2b27f9 | -13.5155 | -56.5488 | 2025-06-05 06:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1601be11-951c-39b9-8630-7e719d17bea6 | -18.8479 | -53.6251 | 2025-06-05 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 0da2a04c-0499-314b-a440-bcd91059e0df | -13.5152 | -56.569 | 2025-06-05 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| c87f959f-458d-3b92-82b2-d288926902cb | -13.5344 | -56.5672 | 2025-06-05 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 6478f262-2e3c-3e61-b919-c9dc2136f225 | -13.5155 | -56.5488 | 2025-06-05 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 477fdf62-a40c-3d45-bac1-59747dfd3200 | -13.5346 | -56.5469 | 2025-06-05 07:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 76fc6d40-29e8-3786-9a07-a13c6d3230e7 | -13.515 | -56.5893 | 2025-06-05 07:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 3ea84f90-2669-3ee9-a49c-3c55a1566c17 | -13.5344 | -56.5672 | 2025-06-05 07:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ea24831e-0486-3756-87d5-1f846467afe9 | -13.5346 | -56.5469 | 2025-06-05 07:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 090ad808-e166-38e6-af82-a94318cda0d2 | -13.5152 | -56.569 | 2025-06-05 07:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 215.0 |
| e45d1bfa-9fff-352e-a4d2-d691f4df1a5d | -18.8479 | -53.6251 | 2025-06-05 07:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 604a5884-0ca8-33b9-b525-83ac3c19155c | -13.5155 | -56.5488 | 2025-06-05 07:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 99a1e863-0337-35fa-9d8e-d9f0417b8f42 | -13.5155 | -56.5488 | 2025-06-05 07:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 43988a28-1cd4-3089-bd01-25b221578475 | -13.5152 | -56.569 | 2025-06-05 07:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 258.4 |
| a2774606-7e95-3e1a-8049-eda153e66a46 | -13.5344 | -56.5672 | 2025-06-05 07:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8fcb7690-39eb-3991-9e64-b329a25cc420 | -13.515 | -56.5893 | 2025-06-05 07:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0d6eb4e8-4df0-3407-80f9-43f10b6354fc | -18.8479 | -53.6251 | 2025-06-05 07:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 229b77b0-d5f6-3209-8925-66116750f27f | -13.5155 | -56.5488 | 2025-06-05 07:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f110453f-18aa-303d-8576-950e807bad2f | -13.5346 | -56.5469 | 2025-06-05 07:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5ccc5433-3ee5-3918-9834-12f45138eaa2 | -13.5344 | -56.5672 | 2025-06-05 07:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cbf7704a-5b22-34e1-b3dd-9c7b7403f551 | -13.5152 | -56.569 | 2025-06-05 07:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 201.8 |
| dd5085ff-af0d-3b48-9614-d7f59af9715c | -13.5344 | -56.5672 | 2025-06-05 07:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| bd01896d-802b-3455-81fd-e0e3ded6d2cb | -13.5155 | -56.5488 | 2025-06-05 07:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| deffdb7f-33dc-31bd-94ab-7260c1d3c8ff | -13.5152 | -56.569 | 2025-06-05 07:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 240.7 |
| c6e3c897-68d9-3ce0-9347-aa236eb5670a | -13.5155 | -56.5488 | 2025-06-05 07:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d97981fe-1c29-377d-9c88-957a95968695 | -13.5346 | -56.5469 | 2025-06-05 07:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 96c38eeb-1c59-35a3-8d8c-c4c2286821e7 | -13.5152 | -56.569 | 2025-06-05 07:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 16b1cf66-9679-32cb-9731-f7d544548714 | -13.5344 | -56.5672 | 2025-06-05 07:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 67328b21-0716-3291-afe9-1cf3ca2ab0e8 | -13.515 | -56.5893 | 2025-06-05 08:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2648fdb7-a0ae-3eb6-b7f5-0003a2c4395b | -13.5344 | -56.5672 | 2025-06-05 08:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6657b1c2-48a5-3513-ba6e-66f6350a8f7b | -13.5346 | -56.5469 | 2025-06-05 08:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 35.7 |
| f63e1d96-9dd9-3719-83d7-9c4517c0d287 | -13.5155 | -56.5488 | 2025-06-05 08:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d3a889bd-2447-30d0-8936-1edec04ffb5a | -13.5152 | -56.569 | 2025-06-05 08:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| fd676d71-307c-3fd8-a273-61292a020a0a | -13.515 | -56.5893 | 2025-06-05 08:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| a8d1cbe5-7165-3f1c-b06d-b8ee591c1acc | -13.5344 | -56.5672 | 2025-06-05 08:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c0f3f77e-8ba5-3b30-816f-c23955236d9b | -13.5155 | -56.5488 | 2025-06-05 08:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1cef771b-551d-3622-85f4-078dcdaf37c0 | -13.5152 | -56.569 | 2025-06-05 08:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 9a87500c-d37b-33e8-9118-2a2c8987cd4d | -13.5346 | -56.5469 | 2025-06-05 08:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| c880dc5e-6ec0-398b-a738-fb56e5d40db0 | -13.5344 | -56.5672 | 2025-06-05 08:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 97e19be6-8b8d-3be2-9eba-31a1ee91a13d | -13.5155 | -56.5488 | 2025-06-05 08:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |


[Clique aqui para ver as próximas entradas](README21.md)
