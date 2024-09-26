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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b05dc0f-fa2a-3d4f-beda-4862f7178da5 | -20.81 | -51.33 | 2024-09-26 16:03:27 | MSG-03 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c91c7f9f-8f73-347f-b009-de4608cf5dc7 | -20.77 | -51.25 | 2024-09-26 16:03:27 | MSG-03 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c31657c-cff5-31be-90e7-81cd5f9fe832 | -20.58 | -51.25 | 2024-09-26 16:03:27 | MSG-03 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ee34ba8-b1b1-3698-9838-0c88a80e3516 | -20.59 | -51.31 | 2024-09-26 16:03:27 | MSG-03 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 651b8118-0d45-3969-87e4-e46346eaf96a | -20.59 | -51.37 | 2024-09-26 16:03:27 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a67f86f-ae31-329a-bb0d-860651ae34e8 | -20.59 | -51.43 | 2024-09-26 16:03:27 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3198c514-aef2-3f05-a42a-f55bed93fb6e | -20.56 | -51.41 | 2024-09-26 16:03:27 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cad40387-75f3-3734-afc9-e23a2c6af6f8 | -17.04 | -56.23 | 2024-09-26 16:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2de11d11-e2ab-37e8-a5b4-7a7067f343d2 | -17.03 | -56.15 | 2024-09-26 16:03:48 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fc6aaf0-8195-31e1-b43a-1a3624c031d4 | -16.56 | -56.01 | 2024-09-26 16:03:51 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c92e5ad-5ca2-3b35-b8a0-3fa61f728f5c | -14.55 | -45.73 | 2024-09-26 16:04:01 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6292ba-7c3c-3ba7-8d21-7f0301fe72a0 | -10.8 | -45.94 | 2024-09-26 16:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0544693d-1d83-3510-a6c3-937938da3489 | -10.8 | -45.99 | 2024-09-26 16:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afa9281d-9056-3551-a5da-d0c06b3693f9 | -10.04 | -53.42 | 2024-09-26 16:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 056b379e-a6aa-3aa4-9fa8-a6731e8cbeba | -10.04 | -53.48 | 2024-09-26 16:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f45b2e7-f116-3931-88c0-1cd6f6ebd454 | -3.502 | -64.82 | 2024-09-26 16:05:27 | GOES-16 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 831a1c4b-d8fc-3634-b1ef-aca953d1d513 | -12.4974 | -50.4177 | 2024-09-26 16:06:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b7588c8f-5ad9-3547-a947-8340432823c3 | -23.56 | -47.31 | 2024-09-26 17:03:10 | MSG-03 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 568460d5-60aa-3834-84dd-248b1a495f21 | -23.59 | -47.38 | 2024-09-26 17:03:10 | MSG-03 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 758ab6b5-6765-37d4-a3fe-d85658378a84 | -23.56 | -47.36 | 2024-09-26 17:03:10 | MSG-03 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e11ae4cf-3d9a-3378-97b1-b6b4874c1a9b | -22.73 | -47.05 | 2024-09-26 17:03:13 | MSG-03 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2ff9c73-dca9-3c6b-8bd6-4f2230345be5 | -21.55 | -50.78 | 2024-09-26 17:03:21 | MSG-03 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e40e8f23-0582-388f-a930-fa3df0b03327 | -21.28 | -49.25 | 2024-09-26 17:03:23 | MSG-03 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 968294fd-b6cf-34b7-8324-30587ec8e384 | -21.3 | -50.98 | 2024-09-26 17:03:23 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ddec2e8-ba11-3f51-a865-9dc15ef34b51 | -21.31 | -51.04 | 2024-09-26 17:03:23 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2fc3fe8f-21df-30d3-9567-722860d9ab6a | -21.27 | -51.02 | 2024-09-26 17:03:23 | MSG-03 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3522a456-6375-3a02-b8c1-cff01b0ff3f5 | -20.63 | -51.45 | 2024-09-26 17:03:26 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2bdfc17-7a33-36ee-a44b-0e49e35b03f9 | -20.63 | -51.51 | 2024-09-26 17:03:26 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd147f00-b9d6-3e07-a55b-c1ed69c2da12 | -20.59 | -51.43 | 2024-09-26 17:03:26 | MSG-03 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 576ecf57-9f74-3342-b93b-04060e119545 | -16.87 | -47.76 | 2024-09-26 17:03:47 | MSG-03 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25c66f28-7e5a-3a96-8fd0-f1d0ab5cf9f6 | -13.23 | -45.65 | 2024-09-26 17:04:08 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32f41a94-d156-39d0-b36b-c932fb415422 | -12.8 | -54.06 | 2024-09-26 17:04:14 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c196bc4-1bb9-32ca-b63b-69bfc00708c3 | -11.24 | -51.17 | 2024-09-26 17:04:21 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9361d45d-d33b-3107-8048-03ccda6ac671 | -11.21 | -51.16 | 2024-09-26 17:04:21 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1b560d-7b33-3720-9c4b-1897f4707ddf | -10.22 | -46.19 | 2024-09-26 17:04:27 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a4d7751-790f-3ac9-9a44-4dd1e814a0f5 | -10.04 | -53.42 | 2024-09-26 17:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8f3c332-f03d-3a25-a970-70098d7f9693 | -10.04 | -53.48 | 2024-09-26 17:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58e68e7f-9075-30f0-88b2-dbd834b78e92 | -7.98 | -41.02 | 2024-09-26 17:04:40 | MSG-03 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 02e72078-9fe1-36eb-b3b5-bbadf1f36dcd | -7.95 | -41.02 | 2024-09-26 17:04:40 | MSG-03 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bee245eb-12e0-3908-966a-3c6097b1a9c8 | -6.4783 | -61.4201 | 2024-09-26 17:25:43 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c982855d-9dcd-301f-ae2d-33a272f1fe20 | -3.3925 | -64.9139 | 2024-09-26 17:45:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 7dcc6cf9-2fe5-37bc-9659-e567dd91d5dc | -3.4107 | -64.9321 | 2024-09-26 17:45:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 99984d92-769d-3054-9c6d-b714dcc9cef5 | -6.8193 | -59.5734 | 2024-09-26 17:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 332f59e2-6b6a-3ddc-a124-a34571a9e074 | -12.2248 | -50.7722 | 2024-09-26 17:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |


