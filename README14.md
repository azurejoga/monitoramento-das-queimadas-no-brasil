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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdd9d9d5-71b1-3eee-8533-48b7bdec6744 | -4.87849 | -45.89765 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e706aa12-5540-374a-bf83-9f65edd11bb9 | -3.07439 | -49.10772 | 2025-11-19 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efbcdc8e-d139-34e8-9e7c-94948407f946 | -4.8783 | -45.64262 | 2025-11-19 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 91495274-a2e6-3044-a5d5-acd402179a10 | -5.46088 | -50.74765 | 2025-11-19 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 282e8d40-dd31-3c5e-b8b1-bdff163d14ba | -3.562 | -49.43622 | 2025-11-19 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cf742dc-2818-376c-a643-0ef5b496bb69 | -7.17017 | -44.72448 | 2025-11-19 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14666784-01e5-3cf1-b9d6-cbbbeca04fed | -3.47901 | -49.59391 | 2025-11-19 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2608a6-6446-33fd-880f-af33c75f06ef | -11.93719 | -43.84214 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47bd6bb7-c6c3-3202-9bbb-b6ff40308e52 | -11.61953 | -43.90523 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 10b5ea8a-5525-3c53-8057-9d5caf451811 | -9.16694 | -49.63737 | 2025-11-19 04:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87e5c369-1b18-35aa-b2d9-0d188a5a63a1 | -13.90192 | -47.42311 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9fd2515-2def-3765-93dc-9bae9d875a81 | -13.9008 | -47.43026 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4c45c10-315a-3aee-b90f-7a3cbf23c92a | -13.73843 | -48.98401 | 2025-11-19 04:31:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 96b7bae7-b3b7-397a-91d6-231ac6bf61d6 | -10.06176 | -47.90712 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 511bafe4-87ec-3e6b-a148-9dc4e8b26c25 | -9.85067 | -48.90485 | 2025-11-19 04:31:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f797a5fb-2c69-3968-ba37-66023c8aa267 | -10.13691 | -44.19702 | 2025-11-19 04:31:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da7391d8-5ee6-3e41-b47e-ae20782b1bcf | -10.0307 | -53.75227 | 2025-11-19 04:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c5430d1-8a9a-342e-8ea8-05c164201f13 | -10.06234 | -47.90357 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21105a8d-416d-3268-b0d4-cf81e93cc426 | -13.88364 | -47.4091 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6380f51-1be7-3ad5-8787-5a282e941571 | -12.88465 | -50.15767 | 2025-11-19 04:31:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3714f923-9759-35bc-bb34-a553f4014cd8 | -10.27451 | -60.537 | 2025-11-19 04:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 149445e7-e6e5-3005-829f-1669f19bd8f3 | -10.68582 | -48.88409 | 2025-11-19 04:31:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129cd031-3191-364f-9f0e-f72e8fdf3d1f | -13.93175 | -47.51176 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 229d213e-63f2-3d47-93dc-9fd133d96403 | -13.9058 | -47.42009 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa8f27bd-afa5-3cf3-ae05-1e0d7d65f5c0 | -12.8128 | -49.34545 | 2025-11-19 04:31:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1968aa93-7443-3e22-bf38-4c70f446522c | -9.39286 | -48.45143 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 830b4ca6-d04d-378f-8e74-c48f9db8845d | -10.07064 | -47.91584 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae4a3c6a-19a9-3107-9a19-06b8f1b5ed95 | -15.28564 | -53.15842 | 2025-11-19 04:31:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b27daef1-5b4e-32f9-af24-3d5d0fd70f91 | -16.05326 | -50.429 | 2025-11-19 04:31:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b1c2742-bf57-3299-938f-35d18894011f | -12.88116 | -50.15705 | 2025-11-19 04:31:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 82a7f95c-836e-35c3-93f1-aab152c2c7f3 | -9.39566 | -48.45564 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c7f5cde-bfed-36f9-84e4-2bd71d4958f3 | -15.06755 | -43.40623 | 2025-11-19 04:31:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dfd61803-def3-3de6-8dbf-66eff49fa799 | -13.88253 | -47.41624 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6913684f-8e79-3376-a025-94a450c15bf8 | -10.19435 | -44.89778 | 2025-11-19 04:31:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e042812-2009-3f61-ae2d-4e27c8a7a721 | -10.35066 | -48.90136 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7aa18254-a37e-3a5d-9ac6-1512eb0a3ccf | -11.01309 | -49.04015 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7ba51d7-378f-3458-acbf-8a547731c163 | -10.35005 | -48.90507 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d71aa451-1f64-382b-86fe-2c133a6637b4 | -13.93562 | -47.50879 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 147bc45b-d4c5-3318-88d5-bda574c49743 | -10.29994 | -53.77697 | 2025-11-19 04:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fae56ec-e829-3175-bc85-c95ade538574 | -13.88694 | -47.43165 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf8c665e-0185-36f1-a8cd-60c27386984f | -13.88028 | -47.47432 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e75b24-e87b-3cd0-98ba-d6d4e54b5034 | -13.88971 | -47.43577 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 475d088f-3a20-3a7c-b973-8c82fee5d926 | -10.0559 | -54.34532 | 2025-11-19 04:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed2f4b8c-1992-31fc-9b0c-47e2ea9e4e59 | -11.67002 | -47.96975 | 2025-11-19 04:31:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8616b727-6cc7-3ab3-bdfc-afe77818e28f | -9.35747 | -50.74157 | 2025-11-19 04:31:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fa6cd4b-f66c-301c-b00f-f4eef9f03097 | -10.78602 | -47.97728 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3acea4e-55c4-3375-ac40-38a141159976 | -13.20217 | -48.32002 | 2025-11-19 04:31:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 064a12e4-df20-3e14-bf26-86e29356ba19 | -13.90469 | -47.42723 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bff8b1c7-abfd-3f4b-b4f7-57881a4381c3 | -10.02843 | -53.74996 | 2025-11-19 04:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c96ba7b-d03b-38d4-bc0c-5ff9067fca85 | -9.38624 | -48.42783 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a135797-ed89-3f10-9d76-6dcc52e609ae | -9.39964 | -48.45254 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 818b502d-993a-3302-bc89-11723e985067 | -14.92951 | -47.77248 | 2025-11-19 04:31:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a590326-23c1-3957-b68b-7eb7dde8e9cd | -9.37726 | -48.41887 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f51b174-0ea6-346a-823d-ee5fc8cbeeab | -9.39625 | -48.45198 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c2f997d-e5e8-3e91-81e4-445c78f5d893 | -9.37167 | -48.41048 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e544aa0-5831-382c-8105-bc6726809711 | -13.89027 | -47.4322 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90193fc6-8ec0-35c9-bb17-612013188e71 | -14.40063 | -48.27405 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6fdfb0da-da1b-39c9-b0f1-4bddd44d720a | -9.38447 | -48.4388 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 086786e5-ad59-3431-9162-aab2602c356d | -10.92417 | -48.66685 | 2025-11-19 04:31:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f31c78b1-ec9b-30d4-8fbd-e11dd8454587 | -13.07045 | -42.13425 | 2025-11-19 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a1e10d7-a0e0-37eb-880a-2693ffe68dca | -10.71998 | -47.73512 | 2025-11-19 04:31:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 182fea60-28b8-36d5-b726-9adde4c40561 | -9.38108 | -48.43824 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45e28342-1402-3360-8f02-323c9b836158 | -12.23384 | -48.73742 | 2025-11-19 04:31:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75e68637-b28e-365c-92ac-7e9bd26c2315 | -11.86317 | -46.96348 | 2025-11-19 04:31:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25e529b8-0d42-3d86-989d-39a2e1a8a88d | -11.13555 | -44.95301 | 2025-11-19 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ca4cd9-57ef-3a88-897e-aad48b532ae3 | -14.93007 | -47.76891 | 2025-11-19 04:31:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f3b1ade-093b-3468-829c-db7d946975a9 | -10.34953 | -44.01945 | 2025-11-19 04:31:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0098f002-dc65-3bf8-8918-8a7ab8540047 | -10.10038 | -49.58604 | 2025-11-19 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57cd0821-a384-3751-b296-b642ea1fad8d | -10.7771 | -48.83809 | 2025-11-19 04:31:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2bd135-3dc2-3aea-9117-d89950025211 | -9.38506 | -48.43514 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35516934-9492-361e-84a1-39402f08ab59 | -9.38226 | -48.43093 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1b4857d-00eb-3a4d-bf2d-11156840047b | -12.59999 | -48.87638 | 2025-11-19 04:31:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37884fa6-7fdc-345e-bf99-45fa35179039 | -10.03183 | -49.2094 | 2025-11-19 04:31:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00695631-a375-3e87-b916-72f9c16d6e4a | -10.55047 | -44.12 | 2025-11-19 04:31:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a17d97de-4a05-38cf-a31c-bbcee8a8f15f | -11.61046 | -47.62002 | 2025-11-19 04:31:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aad86593-fd96-3b53-af2c-bc75096d0dbd | -10.76972 | -48.03643 | 2025-11-19 04:31:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2b62d4-bcd1-3d41-be77-bda16f8e9ee3 | -13.07023 | -42.13643 | 2025-11-19 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3daabd5e-50b1-3765-9b87-a73596cd3492 | -13.88249 | -47.482 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24d95448-82ef-3a7b-9913-421dc5c9f229 | -10.94528 | -48.70765 | 2025-11-19 04:31:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b18b574-bbbd-39c4-9099-410c234e81d7 | -12.45439 | -54.44817 | 2025-11-19 04:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9b773d5-0b1c-3713-8a39-d390351327b3 | -13.90139 | -47.40467 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4adf9421-2bad-3576-bcb4-8d9b5ee85d92 | -11.61584 | -43.90468 | 2025-11-19 04:31:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6265fc9-37e9-35d3-a169-8411d4ae224c | -13.88308 | -47.41267 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a542ac8f-01af-3817-b9dc-d83f9f9283ed | -10.35126 | -48.89766 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bd285ef-14c1-30f7-97e4-a3c452a2ac88 | -11.66889 | -47.97682 | 2025-11-19 04:31:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 094ee8e0-e076-3b37-89d0-a3b9ad16d3bd | -10.36785 | -49.89111 | 2025-11-19 04:31:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6e29174-a37e-3d7a-a9a4-816c81f99288 | -10.6625 | -49.37094 | 2025-11-19 04:31:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8093f1a4-b456-3dbb-8d69-55155143ac6e | -13.88084 | -47.47076 | 2025-11-19 04:31:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18080223-9c61-372a-bc2a-8813e317b0cf | -14.40007 | -48.27761 | 2025-11-19 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4fea722d-8bb9-3cec-a6a9-8dc11028e8c0 | -11.51402 | -44.99953 | 2025-11-19 04:31:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab74d1fb-3502-3b13-ade3-d34bd1e2cfda | -9.35745 | -50.74371 | 2025-11-19 04:31:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c5d45ed-70f4-32db-b3d4-d5ebcaf98b84 | -9.36769 | -48.41357 | 2025-11-19 04:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74473e7f-2c51-302c-a7aa-6f7159a04dd8 | -10.3492 | -48.93159 | 2025-11-19 04:31:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9212e0e8-d554-3c95-adfe-28c9126cc935 | -10.54643 | -44.82665 | 2025-11-19 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ececd05b-728c-3c5e-929c-75fb004a91f6 | -10.50338 | -44.03228 | 2025-11-19 04:31:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88f25311-3380-318e-9133-a3559cc0d2d0 | -13.0657 | -42.13765 | 2025-11-19 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0e28ca9-e55d-375f-8056-f376770317f5 | -10.03528 | -49.20999 | 2025-11-19 04:31:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 603f05c0-9032-32c3-a227-8df58d4ea833 | -11.21959 | -49.71941 | 2025-11-19 04:31:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b1cb895-8069-3f0b-aa52-0b1e55979c67 | -10.09913 | -47.88781 | 2025-11-19 04:31:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc64b715-6788-3d04-b085-dd5520fb34da | -10.38228 | -47.53569 | 2025-11-19 04:31:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
