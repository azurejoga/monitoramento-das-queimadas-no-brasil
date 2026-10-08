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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b97f5ef8-57c2-35fb-bc18-90078f5e31b1 | -5.85664 | -53.46574 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 841c190c-40f5-33ce-9435-68a79518b2d1 | -3.08157 | -53.95446 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0625998f-6a1a-3c7b-9d27-518e001223bd | -3.83708 | -55.98065 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e74d7725-4516-3a6a-99ac-eca989e06287 | -7.22484 | -55.1609 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad314872-25d2-3e6f-92d2-482ca45b9b1a | -6.88957 | -43.70199 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39a98f19-bf02-36fa-9288-134e9c5f9840 | -3.61793 | -55.50428 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66b19d44-0cb5-3fef-9d1a-fd61710e3f4a | -6.11306 | -51.73483 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f339a2ad-f37c-32d5-9d17-e7f34732c3e7 | -3.73844 | -51.21083 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c865885-1690-3076-8988-a2e264651377 | -5.62569 | -48.80773 | 2026-10-08 04:46:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab073c2-2772-34ec-ad88-680b429666a1 | -8.22038 | -46.32866 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50623ae4-6d88-3a7f-8b16-1503a707c8c7 | -4.24711 | -50.74487 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16f7182d-dfd6-3c9b-8f74-6e68d3b71e45 | -5.97292 | -55.35902 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67c0b36f-1f99-3e05-bf20-0da543ee59a1 | -4.35488 | -43.79226 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 92ca3136-9f8c-3a9d-982a-a50a01532eaa | -3.03119 | -54.10794 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f3748cd4-986b-3c79-b12b-d1ea6e2e23a4 | -10.88417 | -49.14632 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d2853efd-a0f1-3938-a9a9-7b7470ec44ff | -8.60223 | -53.12623 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e209dd32-1e5c-3b95-9564-35190a7a3384 | -4.06957 | -59.84179 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4aef128-451e-33c5-8195-232ffdba9bcb | -3.54132 | -50.09599 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8388c59-13fb-38f3-8171-5fdd51900645 | -3.28312 | -54.054 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b5fde2-74b9-3373-aab4-e2699769cef8 | -3.11636 | -53.78584 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00ac8275-b40c-3683-8a65-6d1cbfffdb33 | -8.21876 | -46.34007 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1557ce3b-440e-3e01-b49d-d55b7f69200f | -7.20264 | -46.52133 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2ff2a5-1f13-3b87-9343-b278a770e587 | -3.29735 | -61.0126 | 2026-10-08 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 575037e6-b60f-3db5-8b9d-4421d9bc7747 | -5.73805 | -45.16077 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cecdb272-cb45-3f9f-b1e8-bca5310ccf4a | -3.02058 | -54.07935 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b09de3e0-33e2-3f0a-b16d-172c1f8df1ca | -2.50101 | -58.07298 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b0613a-7d4f-3584-ad00-7385481d0c6d | -3.27437 | -54.06151 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 150901d1-7dbe-34b1-aa64-8b22ede765e3 | -3.28468 | -54.0676 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2881f686-825c-33c7-9dc3-ecbdc3e682a7 | -3.62591 | -55.50547 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5882612-70d8-31f3-8ff6-cf2c7e969c50 | -5.37866 | -44.17264 | 2026-10-08 04:46:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d2194860-d2f9-3301-b14a-34318134f6d8 | -8.76812 | -61.38412 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fae0476-37a7-33e5-b07f-cf04449462a7 | -3.26789 | -54.05755 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a4e67f1-4869-3962-be63-2e2904e8402a | -6.46542 | -55.48207 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f267f61d-9529-35bc-bc46-6145ced88bb7 | -4.54117 | -55.61694 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5d3c093-2bd3-3a3c-98c2-efb7ba11d09b | -3.0162 | -54.08315 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c62d7798-2ec6-3294-bac1-7b7f22f54df0 | -3.6752 | -54.2811 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32a290e5-7845-3673-8740-a4010786762f | -2.93324 | -54.1512 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ac58eb-eab4-38b6-94f0-5c08e80284b0 | -8.58164 | -53.10437 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bf1e7e5-94c2-3124-8fe3-10d68629510b | -5.96759 | -55.36769 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f34fa92-7396-38ed-862b-6dd81da1f347 | -3.02451 | -54.17443 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a94848fb-ce49-3241-ae2e-a07ecac16bd2 | -3.66699 | -60.62738 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1918f055-a4b9-3aa8-9a4a-eba3e6ff9a82 | -5.87539 | -53.49603 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af7aeeb5-29d6-3a72-9b40-4768a9a75866 | -3.86367 | -50.4105 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bf0e5697-434d-343f-a9cc-3e33a30291e2 | -5.26453 | -45.40336 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6060e0f-adc5-3125-a879-91bbab616321 | -3.15034 | -54.08925 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e1b053a-8f6b-37e0-9f68-a8df1f441f92 | -3.92876 | -50.33961 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 76d61a86-14e9-3200-984f-cc6be814b416 | -3.00708 | -53.90471 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8da16aed-4f1b-3615-94d1-2919a70b2b36 | -3.50571 | -51.69468 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aceb9d74-9279-3146-9412-4f731a171037 | -2.50751 | -56.15845 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b59a5e99-2154-32d5-8488-1af134cd1b75 | -5.75306 | -42.05093 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf8f6172-bcaa-3f57-978c-6301faeab72e | -2.75256 | -54.0402 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48356cf7-0858-302c-9935-573c0b0af3aa | -9.93509 | -57.51248 | 2026-10-08 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80f705ef-5d98-3388-b7a5-060875295369 | -3.54376 | -54.6722 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 57714429-8beb-3118-9d18-9ff8c76c9549 | -7.21295 | -55.1638 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bce7b8c9-bc8f-31da-ae95-5ae8d249733e | -2.7802 | -54.08039 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d7b7834-fd2f-3f50-887f-129068a26127 | -3.2835 | -54.00554 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ccfa61f-8545-3e3a-bd1f-3af929a75517 | -5.69622 | -53.47673 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fa5b3bb-085d-3243-8e92-3134ab77325a | -3.36611 | -58.19288 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd4e992b-a930-3b91-ac78-06fc907fe1ae | -6.9301 | -43.65908 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 2fa25f3f-13c1-3068-bf17-c52d6f66496f | -5.74095 | -53.46423 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d1864c1-33d6-3fec-8b67-a7d6bae747a3 | -4.50963 | -54.99275 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04d43d20-ee52-335a-8d65-02bfa136aae2 | -3.58837 | -54.66044 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 03f6f65d-825d-3012-9bac-b7748c5efcb3 | -3.93883 | -51.01614 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9820f699-6588-3cc7-9d30-4fd0add7fe16 | -3.58137 | -55.6019 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ad8b6dc-31e0-37c6-82ef-5f7fcd3db7f7 | -5.91285 | -53.88776 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c84b13c6-12e0-367e-a21c-05b64b885d0a | -3.07861 | -53.94962 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6ada77c3-9a10-3b08-b56f-affb02213897 | -7.1913 | -52.62517 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58441834-ca0c-35ee-ba66-1532a3d0b520 | -3.20681 | -53.87702 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be262270-dbab-3067-8977-1301f3730909 | -9.83723 | -47.471 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88cd7079-af46-3025-bf7e-bc1ea3e84205 | -2.57167 | -56.16448 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 536fc20f-df0a-300b-a3b8-d7923090077a | -2.76415 | -54.10953 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcfb70c8-8d74-3ee5-9bb8-d51a76213e54 | -3.17048 | -54.74421 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9add416-c29f-3703-be7c-0fdc7435863c | -7.64143 | -44.37743 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 666ea20b-8f2b-338b-98ad-fb008766274e | -3.1743 | -54.74482 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf29ed8a-8e96-3290-9acb-9da5b8d5ef7e | -7.86421 | -44.22159 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50d37027-a26f-3403-8692-b931170ac841 | -9.8364 | -44.78843 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69a4dae4-d474-3642-80b8-f56bb4e3a688 | -3.09097 | -53.94275 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66872a85-3756-3410-ab6a-6f36cc61e99e | -2.94064 | -54.0642 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba0801fb-e11d-3d13-b62b-7d20a4307335 | -2.49201 | -56.14774 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b115519-884d-35fb-bc2d-f713761a5348 | -4.11172 | -55.16834 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9902ecad-dfdc-3712-bc4c-fedd769027f9 | -3.65946 | -50.95095 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0801c37b-30a1-3a94-871b-968dab7ce13e | -2.91605 | -59.31519 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a48687-907e-3ee2-a3ff-c029e3a2f476 | -8.59873 | -44.87299 | 2026-10-08 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 045a3718-e17c-3c55-abf3-d0e41af8c231 | -2.7742 | -54.07045 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6ee9d73-1c74-307b-8676-16855cba11d6 | -3.51876 | -54.65869 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 245f7514-a432-30e6-a89f-7f0cf18c552a | -3.18234 | -58.63772 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345a796d-310c-3ee7-b0b4-afd9380e1496 | -11.62632 | -43.70513 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c505196-14f1-3dd1-95af-826dfcb2a178 | -3.16435 | -54.7408 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea6ee261-05ef-380c-8e5f-213cd7f0c4c7 | -5.24213 | -50.90845 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2510ea82-36a4-35cc-ab44-39fb4d7537aa | -2.99546 | -54.07099 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 45c597f9-63aa-3e79-ae3a-d75e107cce4e | -3.22685 | -54.35236 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c5ce74b-0b3c-34c5-b439-349db2de2a06 | -3.07353 | -54.26223 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 528964df-934f-3b4e-914d-676864e492d7 | -3.22511 | -53.38247 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c533f34-4bbc-38e8-89f0-073ee383ee47 | -11.63187 | -43.70247 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8bc6663-1eee-3e54-9a3f-5188c0e80637 | -3.28592 | -54.03679 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb55f22c-6430-3d90-baf4-c397695557ad | -3.59242 | -54.56218 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba416e1-7722-3caa-a5ae-c246447f75d1 | -3.6534 | -50.94649 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 007799fa-bd41-32a6-bdb5-3a36031a6009 | -3.28976 | -54.05949 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e01b224-cac4-3e20-97d6-e6fbd2475014 | -3.02358 | -54.08429 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 72606b46-2ed1-3a7a-be9b-296ebde6e3fc | -3.62192 | -55.50487 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README119.md)
