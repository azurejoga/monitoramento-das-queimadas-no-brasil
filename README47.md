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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59f02f33-11ca-33db-a4cf-b6307edfcf9c | -3.6159 | -50.19694 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d092569-96ec-347b-ae02-b1f6df44b57f | -1.39238 | -52.213 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| daa9cbbd-258a-3c09-a560-93653f3650a5 | -3.04157 | -53.27536 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67b7abcd-2a82-3226-b2a4-70851ba4dc4c | -1.28628 | -54.57047 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 503d01ae-5efb-307d-bee0-c538b34b2dbe | -2.18458 | -51.73582 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8b7c70-d04d-302d-b766-3c587a75b6f4 | -1.29517 | -54.56462 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe2fb6b3-7f40-385a-8231-63f64820a52a | -1.45896 | -53.49339 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6349b40d-d3c1-397f-9da3-3fd54cb272a2 | -2.65752 | -49.87643 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc3beaa1-c560-3e53-b3c0-fd5d9484ccbf | -3.12765 | -51.10443 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5f52033-f5f4-3612-91d9-e51d4e322bc2 | -2.97535 | -51.43445 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 096719b1-6191-39ab-864e-90bfcfa7a89b | -3.6709 | -50.22849 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b752e8d-e8b2-3e81-8080-e928652f78ae | 1.75423 | -50.9118 | 2024-11-07 05:10:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1dbed4fe-50a5-377e-a4e8-a20b713173e2 | -2.92809 | -51.04908 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 079bd079-0e90-30b6-a601-ff65b34ba5f1 | -2.8479 | -48.67836 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 485427c3-dd34-3fe5-871b-ecbc49e20dcc | -2.84976 | -51.77178 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb1a2920-8ae6-38d7-9356-410a34b2c1d1 | -3.01485 | -54.09767 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec52b20a-c825-34cf-afa1-0e921b1b15ef | -2.28617 | -53.81526 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e7d216e3-bbf4-328e-a7c1-8d7c7732ad01 | -2.57342 | -54.23557 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 122ddb94-1aa8-3214-99f6-2e0400c217fa | -3.24542 | -53.33845 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec32dbf-6a35-35a7-b455-f30c2bd9c8d0 | -1.33639 | -54.61271 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9566a19d-b0cb-337f-a885-20c16b8fc2b8 | -1.93257 | -46.4775 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8245f447-4fbd-381b-a96f-c29b622cdda3 | -1.32174 | -54.64012 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d43adcb8-46df-39bc-a61f-3e43b04a2503 | -2.17817 | -47.5586 | 2024-11-07 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0abe93f9-fa73-3d1f-8c29-26df48f541a3 | -2.76775 | -53.22929 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e5e84be-7a83-3362-af99-2898a77a8192 | -2.17462 | -46.44753 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7fa27ed-70c9-3061-9a80-06f83f24f9a5 | -1.33695 | -54.60906 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a5b53f3-a470-3f40-8d8a-fda030cb3cb0 | -2.73391 | -51.74025 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22fcf5e-f5c3-3383-98ff-6650b5cb4a66 | -3.47104 | -56.89856 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a19246a9-017d-3fd8-b56b-53f0817b2226 | -2.43155 | -53.66924 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5e79d59-f1d8-3447-8b47-e81941581d1a | -3.62156 | -51.54094 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d11104-17fc-3ecc-9791-56ee3d038025 | -3.03855 | -49.53558 | 2024-11-07 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a3d977-2d18-33ce-ac89-3c9b74e3ea3d | -3.67022 | -50.23298 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d68fded0-7e52-382d-8b21-6256d9c752a7 | -2.87838 | -51.30885 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89d4edb-c6a4-3c85-8281-72054599610b | -2.22647 | -52.487 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9bbdaa8-8c00-38f1-8e70-317970c35ff2 | -3.15256 | -50.20262 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb4fc14-1a0f-32fc-9b56-70df2295f60f | -2.91856 | -51.04889 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48716fd4-a2ee-30cb-9c2b-17968ab09dc1 | -2.88488 | -48.73517 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5984f81a-d2e8-301a-af65-aebae0925148 | -3.88423 | -52.28748 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3479112-f905-3c3d-a8c6-184c0cbb962d | -2.9358 | -54.1148 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e1848f-5df2-3db0-b3ba-54733156b5c3 | -2.06206 | -48.13876 | 2024-11-07 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66761501-d8d9-31dc-aae1-ba4c89a71294 | -2.83712 | -51.80161 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc9e9c38-88f7-39b9-9cd5-ca61fa26fa9d | -2.23269 | -48.02165 | 2024-11-07 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66b9cbf8-3f1b-3c23-9621-78a54915e873 | -3.16826 | -50.21107 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c12ded6f-5bd5-3b29-a360-66ef3ba9e3fc | -1.41128 | -54.48933 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 731e25eb-fc92-3f2a-ad06-3c4fc34a102b | -1.48141 | -52.08426 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 798e19c3-ce9c-3273-922b-69e80be8e634 | -2.72156 | -51.71341 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d7116f-dcc6-3a6f-9e59-6458dcd1a9b5 | -3.61221 | -52.5212 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd6a20ce-35f3-3ce5-9c6f-69bc83ec531c | -2.93871 | -54.11922 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48db5806-6b7d-38ae-b8d9-55e0fd182dbd | -1.19644 | -53.61872 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 072609e3-32b9-30be-8bac-6775377c8d4d | -2.8832 | -51.46588 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8788fd44-596f-34a3-8cf1-bfc2e9c50638 | -3.59142 | -50.23905 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 19413b09-0586-3adf-aee3-c5803ed11217 | -1.2604 | -54.19693 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d0bf8e-2cdc-31f3-9e1b-a1a1a37661fb | -3.53846 | -51.25385 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c1ab40-c99a-344a-bd2b-7f6fb19a475d | -2.9239 | -51.04844 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e85b09ff-2428-3fec-8ca5-f0e21e9c6775 | -2.92909 | -53.85032 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f1cc11e-f9a7-31df-b9ee-8d8cc120ab8b | -2.8127 | -51.80136 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07451c51-d721-3a5f-b24a-02a8bb29cda3 | -3.1307 | -51.11282 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ffd4001-a4fe-3a9a-8b06-4c0d032c4299 | -2.18817 | -53.58146 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f2b3abe-cd90-3ee1-bc64-09e44bf92272 | -2.72904 | -51.71813 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 530e78a5-f63c-3b42-bc87-8a629b103b25 | -2.82429 | -52.93566 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33b6df16-34f7-3db9-b928-d997400b00d7 | -1.18464 | -53.69428 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8856a034-1a61-39c3-aec3-2f51f4f3dc9d | -3.04522 | -53.27593 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc380495-c360-3018-9e4d-651a1d377d27 | -4.08877 | -51.01365 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e1bdbd23-506e-33f8-a1b8-914e2c8d5291 | -2.82058 | -52.93504 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de50601c-bc49-3e2e-a90a-65b6aa7547ad | -3.03727 | -53.27907 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc83e4d0-132f-38a4-bfb0-7d04d1110ff1 | -2.60804 | -51.30235 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a9231c6-31fc-3d0b-a757-a760546e98e8 | -2.17233 | -53.70647 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3acded-1571-3c45-accc-eb25584fe7a0 | -3.53007 | -50.35467 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ead8663c-b64b-307c-a660-7f1eeec32c42 | -1.45645 | -52.69718 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 838972d4-0ce6-3588-b5f8-2d8b7e4bb273 | -3.08469 | -50.95579 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 862bcc12-dae7-36a0-8e87-fbda882b65fb | -1.28341 | -54.13897 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8218839f-c7f6-3678-a8ac-91f17c96a7fd | -2.82022 | -52.96207 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 164dfc92-3a33-3174-b52f-a4f800c7e6d7 | -3.22838 | -50.44471 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8cc52a9-7391-354f-86c1-8af47e62bd1f | -3.62106 | -50.19308 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e97e0f16-7a28-30dc-9136-3340af6e5440 | -2.83763 | -51.79816 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05883021-55a6-3cd5-8a53-b2fc04f68789 | -2.88266 | -51.46949 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddf18c3a-6c76-358c-b9e6-6ceb7d3bb9ec | -2.04952 | -53.27494 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d053c50-a9d6-3f5a-a35b-81fb309c2d57 | -2.93953 | -51.05873 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 694b9511-b245-3fb1-b528-b6f637125024 | -3.7078 | -48.99715 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| db3a95aa-100d-3b19-b04b-f7d7cd5baf3c | -2.82165 | -52.90339 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e22eca-37de-357c-9c0a-3edc3188e576 | -4.66932 | -46.33689 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1506eef9-413f-3cb8-be29-04d40143d327 | -1.22236 | -54.53449 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e450dd7-b8e2-3b2d-9479-80bdcf169394 | -3.20571 | -50.63059 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 378a1878-3901-3b07-8099-7dfa23365284 | -1.4101 | -54.49683 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f437a9f6-c430-3a0a-9f42-bf21702914d5 | -2.95561 | -53.72277 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8762c2a7-c894-3fc8-ac5a-3d3ca6417f0c | -1.19834 | -54.07652 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20804088-8153-3daa-808e-7cee6bb22b96 | -2.8335 | -52.90068 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca3c009a-96e2-31cb-8342-9e2f5631fe64 | -3.59336 | -50.22565 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e001477-47d6-348f-88a5-97cff3082679 | -5.04707 | -46.84748 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db44e6cc-ec16-3395-80b9-d32764ea5c6b | -0.36785 | -51.42873 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab533f8c-5b35-3d69-8c73-ec2171f42c0c | -3.11699 | -51.11207 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcfad81d-d90e-33cf-b696-95cc3ea6bb93 | -2.83314 | -51.80098 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8661f510-409c-34e3-a96b-341d6f26bd2b | -2.18299 | -52.74472 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3979cdf9-3ca6-3ad2-863d-988a2995ea6f | -3.52891 | -50.33213 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 049c6ad4-9b4d-38ff-98b7-c7c928162228 | -3.01126 | -53.42688 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53f558e4-1125-3da4-ad48-8460151bd30a | -2.28052 | -53.80345 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad3f5dd3-0e27-32aa-972f-2b2aa1d99988 | -4.25903 | -50.69183 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b19feca1-c881-34aa-b765-72e3eaab9443 | -2.8524 | -48.67133 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b15745d7-8b36-317d-aa00-701de28870d1 | -3.00288 | -51.44622 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9804a6a-b74f-374a-b3f0-3cf06124fd9a | -2.66205 | -49.87711 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)
