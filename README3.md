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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8dc02d3-bddd-31bd-8ae3-959b1f4be6f0 | -2.54179 | -47.47468 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e2ef1ec-1c16-3207-837b-28bd4d0e0ad1 | 3.06643 | -60.46584 | 2026-01-04 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7a9efa9-ecfe-3fc6-8ea0-1f3ba95c5514 | -1.01075 | -48.88776 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e6302bc-9328-3b9b-8579-b8209314369f | -1.99632 | -47.98352 | 2026-01-04 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86eaf395-b918-32d1-b2bf-98141a9befc9 | -1.33539 | -55.42979 | 2026-01-04 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8b97b2f-0ace-3780-945e-c94044db8580 | -2.44958 | -47.10243 | 2026-01-04 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc9b4864-3cf7-3ad4-a88c-2126dd09f16b | -1.66765 | -53.92273 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d377bb4-361c-33df-a297-8bc0b8cb0d24 | -1.01406 | -48.88828 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed83fdfc-965d-3d96-8925-3e73d98c96b2 | -1.6096 | -55.16144 | 2026-01-04 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82ea67ec-0b5f-3dc6-9fc6-f8790e2e2459 | -1.33614 | -55.42516 | 2026-01-04 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0bfec21-c783-3fa4-9e38-e2510da0fe2b | -2.44902 | -47.10603 | 2026-01-04 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac59a5a1-a255-3fb3-842f-86a7abd19f53 | -2.0007 | -50.52145 | 2026-01-04 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbfe0d25-9887-3a85-b71b-5e244e27914a | -2.7144 | -45.56968 | 2026-01-04 04:38:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24b638c2-d691-35e9-816d-8227d0019ea0 | -1.19477 | -54.10441 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f32e3531-b168-3c40-9b2e-4ae157892add | -1.23771 | -53.38167 | 2026-01-04 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ec59ada-e4bd-366d-9aa8-f6f56cd5d48f | -2.93889 | -52.31638 | 2026-01-04 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d18883-1864-35e6-9858-21b7d209e406 | -0.17001 | -51.50045 | 2026-01-04 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da3296d-6a2b-3c54-8a9b-0a647a736d5b | -1.8087 | -54.06391 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df13086-946d-38b9-8e94-79b3bcc72a99 | -1.21587 | -53.77986 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b2f469-f153-3c1a-ab87-0926297b9f02 | -1.96443 | -54.06109 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bd9176c-7206-3a40-9aec-2ad8b9cee517 | -0.7362 | -52.41962 | 2026-01-04 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57a77da7-ada8-3fa6-a44a-9d3ae7ac2eaa | -2.08994 | -53.48438 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1a767cd-33c1-3c6f-926b-2b5dbd587a1a | -1.11871 | -53.44591 | 2026-01-04 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72f6d35c-e912-346d-8e46-d502068eab7b | 2.55155 | -60.5676 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2659d2f1-8cda-394a-9bfe-38f88626a26e | 2.55839 | -60.56663 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daabd393-2182-3188-9b1f-1620f315b927 | -1.21176 | -53.77916 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd067f0-62f4-3ce4-9232-51bcfa52945b | -1.92573 | -46.45157 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db8218fe-9ec3-3b90-9796-4bf3a3e0b1ff | -0.4947 | -51.67726 | 2026-01-04 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ebca43c-3ab6-300c-9f41-65540a531be1 | -0.49536 | -51.67299 | 2026-01-04 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f90d34c-249b-3fe9-a92b-570008705593 | -1.14549 | -54.16994 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c50e955-6eaf-3fea-b2a2-a8c78a660755 | -3.49474 | -47.16869 | 2026-01-04 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d019590e-e6e7-3f07-b3c1-dff8130818a2 | -2.11499 | -53.48122 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d2d6067-1470-32d3-9783-3f2d2c2a3b85 | 0.62126 | -60.28444 | 2026-01-04 04:38:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fca42eac-bc5a-32ce-b841-29f00bde95f2 | -1.19539 | -54.10048 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798985cc-69ca-3b5f-b0a9-89c00f52e025 | 2.555 | -60.36132 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 688a2f47-3062-339c-8978-21480c95cfa9 | -1.6177 | -45.70408 | 2026-01-04 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b7ea686-6387-366a-9b26-2fc01f6a22b6 | -1.96985 | -53.36169 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 473e35a7-c569-3df0-b721-e8dde8a43686 | -0.17365 | -51.50101 | 2026-01-04 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e1cc17f-76fb-3b66-9cbe-197951e3562b | -2.05684 | -47.92207 | 2026-01-04 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba51f3f4-cefe-3d85-9f75-a74e9e1be82f | -1.92229 | -46.45104 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b9592f2-6ff0-3a79-9de3-fa5ebae4def1 | 2.55055 | -60.36047 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c61840f3-0a6d-327a-b1dd-2e10bf927085 | -2.92261 | -52.23125 | 2026-01-04 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88302c66-b8eb-3767-8c6c-83ba31dc01fa | -0.92146 | -48.65533 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a87e1ba-9f1d-3ce2-9270-916ab97ad407 | -1.52684 | -54.52537 | 2026-01-04 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1ff463-7508-30dd-bcde-2aeeae170c81 | -0.92531 | -48.65241 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11fb75b1-e344-36a3-a6c3-23bb6dde4e1e | -2.42331 | -51.83097 | 2026-01-04 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429329c1-2113-3414-9352-2e538b45c9d6 | -2.42692 | -51.83153 | 2026-01-04 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19383253-dec9-3375-bf46-d5e36459679f | -2.85514 | -48.56265 | 2026-01-04 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59c9863b-8d77-3158-a252-3ecc35f0b928 | -2.86347 | -52.80755 | 2026-01-04 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce645269-8972-3d05-a0f4-2a5db9344655 | -3.41724 | -50.15632 | 2026-01-04 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d8ad7b8-dc88-31df-9051-84650bd04f09 | -1.10252 | -54.11165 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72b8b171-7d86-3f79-9751-9ee79d378ad9 | -2.4462 | -47.10191 | 2026-01-04 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 657eec68-445f-38af-adc2-f7774a8a77ab | -2.07262 | -54.25854 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33a307af-f103-3476-b335-6187c630becf | -2.45143 | -47.79139 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a75b78c-fda5-3467-b03f-b09781d0403c | -1.0952 | -53.17038 | 2026-01-04 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ef9430f-b1b0-3913-a3d9-441460b71e50 | -0.922 | -48.6519 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9be7b4fe-ade6-392f-a014-dd28c4e74575 | -3.3439 | -47.37132 | 2026-01-04 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8578f919-59d3-380a-a45c-fadbdd581c8e | -3.9636 | -42.16636 | 2026-01-04 04:38:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 44e2ff28-30ed-3d7a-8613-d8517651bf45 | -2.16227 | -53.7074 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc50283a-27f8-3d2d-9a74-75add407ae11 | -2.8546 | -48.56608 | 2026-01-04 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a06aab3-a09b-399a-a129-37a59abe3ed2 | -1.66935 | -53.92321 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98639367-ccd7-34e6-bea6-120378aa5052 | -0.32458 | -48.5333 | 2026-01-04 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abfa811d-ed10-3c39-836d-065264e0b708 | -3.8935 | -42.5205 | 2026-01-04 04:38:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21b73147-3b95-3456-8285-57c57cd499bb | -2.91105 | -49.37433 | 2026-01-04 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 934cb92c-d6ed-326b-b077-e4e0c91d2f41 | -2.45197 | -47.78791 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01b4cbde-acaf-300d-9426-924b5d5e2dad | -2.38314 | -47.66287 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bd8eb14-cc66-38fc-a37f-0b3f58481ecf | -2.23055 | -53.72127 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c66210-ed67-3e10-9709-8f4b709b0ab8 | -2.92272 | -52.23042 | 2026-01-04 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beb03a5b-c48a-3677-bae0-88275dedf67c | -0.08846 | -51.27954 | 2026-01-04 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 76faca87-2f58-3120-811c-9abca8aacb71 | -1.96912 | -53.35852 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d6ed053-3267-3158-b281-528563f11270 | -0.99919 | -47.1569 | 2026-01-04 04:38:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acd0eccb-d2d8-3416-b656-7ae1b5090557 | -2.76562 | -45.08809 | 2026-01-04 04:38:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd6b3c5-bb90-33e4-b3a6-5fb7efb62c68 | -2.44919 | -47.78391 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2e3683f-0d9c-3536-afed-b28937271818 | -2.91436 | -49.37484 | 2026-01-04 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89979027-252c-32fe-aed6-5a8454d6bd8d | 2.54821 | -60.362 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b0fe7a54-4f35-3a09-9f68-4497f32bf451 | 2.55733 | -60.35971 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c00e310c-8960-3a39-ba9b-d22c70dd845d | -2.11555 | -53.47777 | 2026-01-04 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16db84bc-c1bd-38cb-adbb-04011bf34492 | -2.54513 | -47.4752 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f811719-4a03-399b-83d2-295ba116dc9d | -1.34074 | -55.42593 | 2026-01-04 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12fb10d8-9674-3023-a5b4-b6a93d706b34 | -2.38855 | -47.60626 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 434341a2-fe0d-31cf-a719-782a39f8f2cf | -1.96501 | -54.05742 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f8ad0d-2f98-3d52-8bcf-5d725b9e0b24 | -2.76192 | -45.08752 | 2026-01-04 04:38:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 562185ae-1d47-3e0b-a480-0f47c626d1f2 | -3.06665 | -54.02774 | 2026-01-04 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5240869d-c6c0-3a7d-a42e-ace787b9141b | -6.231 | -55.62826 | 2026-01-04 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77fd2d0a-6c7f-3b29-9716-39b24ef6afe2 | -4.26119 | -48.83653 | 2026-01-04 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eac7b486-b323-35d6-bf82-e6a327d41dd5 | -4.75703 | -46.65506 | 2026-01-04 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cebc6d95-ae46-3376-8168-5460e478a9cf | -4.34629 | -48.59553 | 2026-01-04 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56232395-f771-3ea1-90c0-3a7461109ce3 | -3.24694 | -52.69001 | 2026-01-04 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c96bae14-fed1-358a-8182-74fcd2eb68dc | -3.06662 | -54.02763 | 2026-01-04 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62c7781a-3cf3-37ce-b4e1-bd43c12ad0c2 | -4.75907 | -46.71124 | 2026-01-04 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af1a0ae8-8dfd-30b9-ba70-0c44b03b11c1 | -4.58204 | -43.81339 | 2026-01-04 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960fc0da-1e77-3a20-b61f-d834d95ad129 | -4.75847 | -46.71509 | 2026-01-04 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcbd591d-2869-304a-84f0-70a0892661f6 | -3.86638 | -48.90121 | 2026-01-04 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae70aa0-09ad-3780-9183-6b87a6ed6307 | -4.74134 | -44.44803 | 2026-01-04 04:40:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abe93b4f-c590-3635-aa4a-db0e2a30e51b | -4.58259 | -43.80965 | 2026-01-04 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba93402f-1494-3fcf-ba66-64dbb23a81c2 | -5.56252 | -45.45136 | 2026-01-04 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 145603f3-33c4-3864-84b8-2f7852347e25 | -3.33187 | -53.24648 | 2026-01-04 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 988beb24-024c-3c6d-a1a0-c4866f62ca02 | -4.3496 | -48.59604 | 2026-01-04 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45086180-6307-3d36-9b4d-ce280bc61866 | -4.12613 | -46.44701 | 2026-01-04 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be99cb64-ef9a-3a8d-aaaa-7229e58db864 | -6.23533 | -55.62891 | 2026-01-04 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README4.md)
