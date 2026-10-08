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

## Dados Diários - Página 359

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee4b509f-72a7-340b-a0cb-ce8a9463f307 | -7.21062 | -55.19795 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 44bed5e9-1a82-30ac-91d3-8ae46e500281 | -4.08194 | -44.11176 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 33357dc1-51e5-3bd0-8649-a9caf5a2c739 | -3.69734 | -58.82416 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 43642573-8057-3468-826c-2bfa9c6f9c5a | -3.65419 | -58.88911 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb839791-83d2-349f-a22b-f45d3cfae3d8 | -5.70001 | -53.4533 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c80b1b24-bb2c-3d14-b801-96319d162a2a | -4.33389 | -42.74866 | 2026-10-08 16:39:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5bdd8668-67cc-318d-98dd-1d8adef2ce52 | -3.151 | -53.72459 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 749c57c1-8680-3096-92ef-4a00a445274e | -4.63385 | -43.49573 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dd1ad488-5d2f-3ccd-9ca7-6acd8f41bbb0 | -3.26954 | -54.05734 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9e6ed258-99fa-347b-bb2c-ecea248e02c8 | -6.21112 | -52.84213 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8fc67b66-8ecb-3bfa-8c28-65e8cc5e1ec2 | -5.71906 | -45.35229 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b9d5829-394b-32b6-aea4-0cf58c49e113 | -2.56735 | -56.17019 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 305d79d0-7c2b-3917-856b-b341e3c6adf9 | -3.37524 | -44.70663 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b244dcd-90da-3c07-81ce-a7df990ba403 | -4.20733 | -41.759 | 2026-10-08 16:39:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 016555a9-c8e1-36bf-800b-7a55153e917e | -3.89877 | -44.12382 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 50d17a5a-9e2b-3e0a-8afd-50556797f1dd | -2.75044 | -54.12032 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 7066b3fc-7333-348c-bdef-8cd05be3cb62 | -3.74139 | -58.85235 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 81c92783-18b0-3264-9b59-1590c254f8cb | -6.73401 | -59.43455 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 83c5ec54-2ff1-328d-819e-6e78c739407b | -7.22165 | -55.15702 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b7132c42-99a5-3902-b4e6-550237bab26e | -3.85693 | -52.03509 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 727a6754-2c34-3179-87e1-a46e2fd4f779 | -2.29806 | -45.71037 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 010b1d79-c7ea-3cff-b585-10191c3cd4fc | -5.50972 | -42.85269 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 9c7a732e-f524-39b6-8d5f-e5415d5ede1b | -3.09383 | -53.95248 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| f2b768d5-066e-39cc-9a08-cef6e9e6b2fa | -2.8738 | -54.88395 | 2026-10-08 16:39:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33f40e94-5565-3268-83ec-81b0380f9471 | -4.56201 | -54.21051 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9535e60d-4a55-3ae4-8d8a-903784ff8df1 | -3.43167 | -54.06028 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 68931cc4-80c9-3f37-a4ec-f57893a75a4b | -1.72376 | -55.44757 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5c6c452a-74c9-3feb-b4d6-5952512bd69c | -3.10589 | -54.27481 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06f0d808-31b6-3e90-a702-2ad51d12b85c | -6.41153 | -51.94113 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb1cdc9f-0343-3909-b7e4-489a35f2861e | -1.63053 | -55.1293 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7c4fc534-df09-3fd2-ac79-30f0cca85420 | -5.36206 | -42.8408 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| 0f7a19d5-766a-322c-a195-e8c80857a9f1 | -6.1055 | -47.04375 | 2026-10-08 16:39:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3fe854d1-a503-3a5a-accf-b35ea50784ff | -2.08693 | -46.56743 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 6e9e2045-cdec-327e-a165-019861c81d56 | -6.85509 | -59.38873 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dfe8330b-9d3b-3eac-b35e-7fed7518bbf9 | -5.41856 | -45.86994 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26bc4ab5-106d-3eda-bdac-0fc7824378f7 | -6.13784 | -51.9213 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f98275a2-88b2-391a-aaf6-7f65443d5a39 | -5.50474 | -42.84479 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| bf395056-9c04-3134-83f6-ab4d91c69f32 | -3.51553 | -59.21051 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4c3922c-d4b6-37d1-b083-255439a2dd88 | -2.0852 | -46.57826 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 156fbe6f-bb1b-3e5b-bb52-dcb94fa2932a | -1.833 | -55.04589 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1fecb1db-d9d9-3a19-bcba-b546566795f1 | -6.28804 | -46.43233 | 2026-10-08 16:39:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9d8c7c31-3be0-3c12-9073-9582894c60f6 | -5.48806 | -43.96352 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2d0f93c7-c74f-3268-9a06-e8e51c56cf1e | -2.45534 | -56.78353 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49c79295-67ab-39b6-8331-fe8cf8fc3001 | -3.97009 | -51.86964 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d226003e-9d04-3efb-b6e3-2229700c5f1f | 0.53249 | -50.76841 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 95f13c16-7b0d-3858-b652-223ce6a51d3e | -3.84975 | -55.91174 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a76c107-c3d0-3cf9-94f1-0cacf12ca90e | -6.72339 | -55.12196 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fedae6a9-4d8b-3b4b-85d4-4014f7cccd01 | -2.10588 | -56.62039 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ebf7937-66c2-39e5-8829-1eb23c110639 | -5.35684 | -43.07293 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9cfa828f-2ad7-3980-bb52-542af6f4cb59 | -1.5442 | -52.75343 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 22c2c3f8-070a-32a7-b4b3-23f1a25baded | -2.49088 | -54.54715 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ff0a13c-e697-30ec-b465-40b718937b06 | -2.8656 | -54.20467 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 45fc9669-5d7e-3b6a-9c1a-4b00f560517a | -4.5769 | -38.94938 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8dc29013-4174-3793-b1aa-3cb3411b35a8 | -3.89359 | -41.60191 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 8e87a0ab-5ac5-3f8a-9244-d8764b740afc | -2.05276 | -54.3027 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 17bdf437-6c7f-3468-a89c-7b2a3ee072e3 | -7.51321 | -55.57626 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 59dabdb1-7b9c-33e5-ab52-d4f2a9eee95d | -1.41184 | -55.41122 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 556091f8-fc19-3215-bdec-cedd28728f63 | -6.15736 | -47.93129 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 70d6cb04-75cf-3909-92ce-5a6426c85a54 | -3.4008 | -59.92693 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0adba8b6-1577-3e77-abfb-920908432337 | -3.63691 | -59.31859 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f53100e-8cc8-3d93-988a-a1366971148a | -4.07318 | -51.03642 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f36d2429-51d9-3e61-9f41-5ad3bc309a64 | -3.5672 | -54.48529 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c793b72b-2178-3ded-917e-453eeb278f8f | -5.93003 | -51.83125 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| d3ec90f5-6b37-3210-9a4c-872799336015 | -6.10833 | -53.50472 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4caa468b-8e79-3bb5-8362-f65874ce2ba9 | -0.71564 | -57.43067 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 996a5b71-eacc-322f-8515-a839c3e1aeba | -5.91407 | -52.57458 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2377e2cf-5262-3b5c-bb90-fe7b993a3065 | -3.04208 | -54.27153 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bb94a056-e0d3-3602-aa92-232e4a11dedf | -3.20088 | -41.14473 | 2026-10-08 16:39:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 427e33f2-5e49-30c0-8bb4-cbc4b92a0caa | -3.00694 | -54.06404 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 6861b11b-3e40-3129-8b28-6ffdb800faf5 | -3.97259 | -59.33316 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 169f2591-7567-3947-a068-bb4e3125dd77 | -4.37598 | -55.32221 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2701c611-5ea7-3766-b872-5ff854eee072 | -2.25882 | -56.74492 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d9b2bd3b-250c-3a7b-a886-f8b6459c489b | -3.77013 | -44.36199 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a1453a9a-a871-3ee1-af84-9d94dbc6c3b8 | -1.28603 | -55.41946 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1876f130-67e7-34e6-9903-cafad4d1b4fc | -3.09527 | -53.96252 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 951a94c4-b053-3981-836a-bcc691c75149 | -6.27024 | -52.27531 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f954c179-3294-3abe-9f88-acb4624f470a | -4.75288 | -42.59354 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 39e50989-4d86-305e-832b-7a32ee26ee12 | -5.39632 | -45.90161 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fb8230b1-3dd4-35d9-a982-62e4604f2d49 | -7.20381 | -55.18867 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0b80686d-777a-3acb-8956-7e71f6d3c356 | -0.61081 | -49.42508 | 2026-10-08 16:39:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a2d3bafb-bb21-3542-a87f-35c743071a25 | -2.77465 | -56.98599 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff6af600-904a-3b9f-b487-cc92d82cb362 | -6.09183 | -55.73236 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bbff1919-6429-3e98-b3b7-5cd10ed9470d | -1.21399 | -55.64754 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f414685f-db87-32c8-81c9-f68acc662ed1 | -3.18775 | -58.6426 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7dab2c4b-87b9-3ce6-bacb-b50861bddf91 | -5.33182 | -40.90007 | 2026-10-08 16:39:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c1792a73-0dfe-3574-8dc8-1561b5d97105 | -2.37626 | -56.8566 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee383981-bc65-3f19-9ed1-31ffa9597162 | -3.8517 | -44.1193 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ff0a11aa-7c19-3228-9be8-512bc21f6a0a | -3.01458 | -54.12235 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 44cbdfca-92fe-3a9f-a2ec-57a4e3a8103e | -2.50387 | -56.60707 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 042bba0c-74af-36c7-bbf4-d873d923036a | -4.16103 | -43.20103 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ea8073f-08f0-307c-99d4-2e010fd6aa19 | -6.17138 | -46.02176 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf7da6c5-b5a9-3df2-98a0-884779907d66 | -3.00405 | -54.04392 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 63c9dbb5-0341-37e0-a9ad-b40179221102 | -2.02888 | -55.62933 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0b261e77-7906-3ac0-b66a-106f5bc1e7ba | -0.72682 | -57.43413 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19ffa49d-4a9c-346c-90ec-08ebca46899f | -3.23988 | -58.49452 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 929bdbd1-7278-3ab1-8334-081691cfa043 | -5.95096 | -46.37947 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 581061e8-b85d-3682-9339-8ff50fcf7476 | -3.26833 | -54.01611 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a6ace460-b948-3908-9b48-d3235f510b50 | -3.26582 | -41.84632 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9022fc88-6c34-38e3-9333-b76bb26baada | -1.76834 | -54.98668 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 95c3901c-628d-3c67-8d9f-8f81d66d6f3e | -2.50968 | -47.38109 | 2026-10-08 16:39:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |


[Clique aqui para ver as próximas entradas](README360.md)
