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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b1455b-a358-397a-b109-7520ad76a0b7 | -3.56976 | -55.4198 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8aef16dc-a15a-325b-8f18-93c313544e0c | -3.10395 | -53.7476 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf8c1080-2e5d-3472-abe1-868866703d9f | -3.05214 | -54.22593 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ab02b002-0d5e-3fe7-8b0a-09b7e3a7d3bf | -3.56161 | -53.28337 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec3d24bc-9c6a-3483-8d22-1ced72e498f9 | -2.90059 | -54.14062 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1a47728-9842-3a8a-a3de-f892733c5a40 | -3.10278 | -53.75489 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1861ff44-85d9-3f2c-a84a-61c8ef5f2eb4 | -3.4622 | -54.59047 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2e4d1820-7fc0-34a2-a9d9-adf360c3e5f7 | -2.92445 | -53.94924 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f24b9ce-0976-3fd4-a09d-05ccf6336a2e | -3.70555 | -50.65839 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d75f9bc-1ea1-39f7-abaa-42b31facc9f6 | -2.78137 | -54.09556 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 77a56b7a-ca0c-3fc5-8aab-b53d30a098d4 | -6.20836 | -53.26654 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51bceb96-01f1-3e09-96da-e0eba7ca95f8 | -2.21955 | -53.70823 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dd8b62d-5826-35ba-898e-1524fa2ecb0c | -2.9012 | -54.13686 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e9457b6-c584-3110-a4ba-f00b4bbee147 | -2.58492 | -48.43704 | 2026-10-05 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 501b0c6a-895d-36b5-997f-ce982a62f01f | -2.94375 | -54.13594 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24371db5-ad9c-3082-890e-d584a8ccd95a | -6.25508 | -52.84488 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a41526-2e03-3a0a-a57c-703277b370a8 | -3.44385 | -51.84523 | 2026-10-05 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4a8442-fee9-392a-a285-418b920fdc13 | -2.89167 | -54.10836 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43b032ef-7573-39b2-861e-ceef9fd87366 | -6.06338 | -53.47251 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4ff0726-bfcc-3688-ba66-1245282e52e8 | -6.19475 | -52.81816 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b9d0223-1046-3c38-ab19-94f43da13d6d | -3.07285 | -49.54345 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d6cae14-6243-3221-962b-95289ab49c03 | -2.21897 | -53.7119 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5050dc5a-94af-311c-9889-a33d0693ebb0 | -3.1023 | -53.73614 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c27d1453-59aa-386e-89aa-cf44f2d075c7 | -3.50386 | -54.62095 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e753cc-0d78-3b67-932a-cd1adbcdc3cb | -3.807 | -50.85759 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5eb9288e-0e12-340e-a7ae-567b025e0b6f | -1.47222 | -54.5284 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 396d95c2-eb6d-3ebc-ba16-552de1f98af9 | -1.51849 | -54.82825 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47adae58-7eaf-3662-a172-17421847f37c | -4.25408 | -55.04485 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d22671fe-60d7-3f3c-9fa2-e5aced99b581 | -3.15988 | -53.07585 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb890d34-d429-3526-82cf-972c24958670 | -2.88518 | -54.12659 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0ca0da2-5b37-38f5-a9de-5b3fd4e899d7 | -3.40325 | -51.67289 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99c75702-868f-3cd7-bf04-6e815da5f6d5 | -3.04073 | -54.20864 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fdba567-3635-3b9e-b247-7c1c72c08dd9 | -2.67826 | -49.03331 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| daec2cde-c23d-3407-b85e-6971cc4d6422 | -2.95022 | -59.16475 | 2026-10-05 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 430e5b73-39f5-399d-a33e-c67f8fad9fcd | -3.28114 | -50.01159 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e0e7cc6-c8e7-3e75-b4c0-e709e50b14f5 | -4.10874 | -49.07324 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e938be0-a68d-3730-a978-6adec72529a0 | -2.59307 | -51.85612 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f80366-901e-38e9-ab5a-d1d02ff17341 | -3.60253 | -54.05104 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f13dfb-7da1-3943-bfbb-d43a75145b4e | -1.88046 | -56.28045 | 2026-10-05 04:57:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dad9b72f-7c88-3c54-91dd-288366ed3cb5 | -3.04643 | -54.21729 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| debb4d51-3f66-31c2-869f-9e85aca549ca | -8.66143 | -54.5646 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e639a27-e9e2-39f7-a593-f6cb3af5da4b | -2.88396 | -54.13412 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60dbc6de-929d-38df-8f81-dc0d5ab0f479 | -2.9286 | -54.16438 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b53d93c-f7ae-388a-a861-b1365294ca24 | -2.78583 | -54.11168 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2d811a8-ac6c-3ba8-a90b-3f38ea090ae3 | -3.31117 | -53.85495 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e0d3cb-fec2-394b-8c07-765c737798b4 | -8.65588 | -54.55631 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4e1044e-771a-313f-93f8-bb8aa2e35527 | -8.52787 | -54.59089 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ded744e-68e3-3a89-87b4-528d0783cbf7 | -4.46216 | -54.96675 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f52ebf-d1e5-3611-9e58-820710dbd92a | -3.06459 | -54.16996 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8921d57a-9d92-3a4d-ae28-82b163ce3331 | -3.00756 | -57.75446 | 2026-10-05 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6c8575d-3eb4-3d1b-831a-bdefd674cd6e | -5.98648 | -53.63583 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 072feb63-fbbd-39e3-8a08-c69b1b21c587 | -5.89584 | -52.04352 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f693c6e-1acb-36fb-b5b6-97d7f42cc4a6 | -2.81849 | -54.12843 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 022a22b8-1a14-3e5a-a0cd-272e3f39db5c | -8.66479 | -54.56516 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a5b3af19-c048-380c-bd5c-10594b40a3aa | -7.17934 | -42.00249 | 2026-10-05 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d24b860-91df-334a-87d4-a95bc7d89190 | -6.89962 | -43.68326 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16c07dde-0efb-326d-9da4-ab23c4ad6ee2 | -2.98677 | -54.04296 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f92c27d8-8318-37b1-b667-3f97fec688f3 | -3.11035 | -53.70758 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8813b9f6-b04d-3713-be23-4e2650cc3e22 | -3.11597 | -53.71592 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08fbccac-9697-3a48-bf2d-f28971ecb0a6 | -3.07897 | -54.16845 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| b24bd668-a757-3fdd-9ac1-1cd9a8488b02 | -4.11725 | -49.07352 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f88651f0-cd2f-3ec4-b929-243cef78e844 | -2.46979 | -48.04179 | 2026-10-05 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1885030f-5f4f-352e-bcb2-f60386f2ee6f | -7.43426 | -63.56027 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a84b8cd-63a7-3532-9ffe-2bb5547e90ca | -2.27445 | -48.74596 | 2026-10-05 04:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2c86adc-aff8-3d7f-b813-0c286587a2fb | -4.44812 | -50.83867 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45329862-9a2d-3d34-b668-47b034b6e853 | -2.95488 | -59.16548 | 2026-10-05 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8801643-d91c-3013-88aa-82fbae3de56f | -4.25401 | -50.77914 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| caadd57d-6992-31e3-b572-83011c5a7178 | -7.44583 | -63.56074 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64eb8403-f271-38fe-acff-34323a076827 | -3.59573 | -54.31402 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c85db8-2878-3794-9144-56e44ccc2d67 | -3.04342 | -54.23618 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86c3e91-02cb-392f-8b38-df3b993c0414 | -6.20744 | -52.82371 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf5a57e-40d2-3600-8389-5990c755b1fb | -3.91809 | -49.71559 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a13ba32-e653-3140-b008-e591fea70cca | -5.99825 | -53.51913 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0a1f3ef-1549-3cb7-9d8b-598224189e8b | -5.99492 | -53.51862 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43913e25-7dda-39e2-a256-55ea1a9f2042 | -4.11104 | -49.08215 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc3bc4c7-88a2-36b2-a3e8-f90a10c27630 | -2.58611 | -51.85461 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27ef1eb4-e8b7-334b-a273-c5f223a0ab9d | -2.98819 | -54.10068 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b4ae34b6-0e6f-333f-b47d-ecbe88d9705c | -1.6158 | -55.10938 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8953c09a-d93c-3294-bc1b-c7ac5defbaf3 | -3.42043 | -54.55239 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c34204-57f0-35f4-8a20-3324c326e99e | -5.85075 | -53.46342 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d1be72-7177-326f-8b83-c1ed449f90c4 | -2.93462 | -54.12677 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b09255b-07a8-34ad-97fa-47cbdc15c466 | -2.80591 | -54.1187 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c99801-d927-39b4-b8e7-3fc579877af2 | -6.2584 | -52.86665 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4892c908-6afe-3a48-b543-33594ba6c70d | -2.90363 | -54.1218 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47109ef0-dd48-3cf8-bc6e-40ad5e860640 | -2.2258 | -53.71296 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65b6969d-8486-38fa-b041-ebbbf46fe27c | -2.97218 | -54.09045 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8db519-07f0-3f8b-99d5-c557ee3b7719 | -6.00036 | -53.63449 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6fa1d4b-ad04-34b3-9fd3-b3b3f9977afc | -2.98736 | -54.03924 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9200bac-8db6-3559-ab4a-36381310a498 | -6.20963 | -52.80989 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a388d0ab-2ddd-3295-b3db-1ee681b5eee9 | -3.46737 | -50.09711 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0506598a-b325-3693-9008-f09ab547fc2f | -3.61487 | -54.60599 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d3ede8f-7d98-3697-9700-ccb65f3f55fc | -5.68522 | -53.50135 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c298f14d-cfba-3912-828a-d0d796de1510 | -3.10055 | -53.74707 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 970b26b4-0c19-3ada-b7ea-5ac6ad5ddd0e | -1.46935 | -54.77889 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f34e2979-93e4-31f1-9b54-933fb0070bb2 | -2.82211 | -54.10586 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cdd31fa-e0ad-386f-9b73-61a16040bae3 | -2.84033 | -54.21341 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19ce89af-ba58-3bf5-bd8b-a0432963b09a | -2.93359 | -54.1112 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab8fcdbb-2c01-3193-b621-65f31074e536 | -3.11927 | -53.73883 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11143eae-857a-307c-961e-7fce5692044c | -3.11374 | -53.70811 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 866f9ee6-ce78-3bb9-b7bc-7dbf2d10da62 | -7.50446 | -54.99667 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README45.md)
