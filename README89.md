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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58dfa1e1-f054-3aa0-89f9-ea5917e92cfc | -5.87387 | -53.49474 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab5cb57b-eb51-34b9-9098-8da0b87d4326 | -0.41781 | -52.06408 | 2026-10-07 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca960f0e-954b-34d0-9582-89d61e4641e7 | -3.80051 | -51.98798 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 088fc1be-fb29-3a62-bf30-c99b61748c68 | -4.77031 | -55.67777 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e18001e-b7d8-37fa-828c-70abc4374d05 | -3.04999 | -53.94316 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f2590b-87f5-390b-aa65-8981d055b186 | -2.77012 | -54.10199 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 928568ac-18e2-30fd-a50d-e252ac82fe54 | -3.12185 | -53.70206 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3ea4198-7a85-3ee2-9b85-bf663962ce54 | -2.92852 | -54.13405 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e22c8b94-10b5-3822-bfef-c894b689e9a4 | -1.40469 | -54.61206 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fab08826-fcb5-33c7-b1c8-d52a8f3750ca | -3.00284 | -54.18115 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92781660-0fa7-3136-81c8-e2975e43c406 | -2.50269 | -48.13877 | 2026-10-07 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f68419c-7e1b-386f-ab30-297f1ead7e34 | -2.87963 | -54.11935 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff8733a4-e63c-3655-971e-e742ce4bb14a | -3.54203 | -59.48434 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f2b14fc-1742-334d-89ff-6f4f542a4764 | -3.09552 | -54.285 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e5259d21-06f9-3ec3-ae82-b8a8a3e2e788 | -3.12828 | -53.76165 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74986726-d431-318e-ae61-5fc06e56f779 | -2.98851 | -54.05307 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d701e09b-bae2-31f5-bc85-cd12da19a272 | -3.99222 | -56.25821 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3ab759f-95c1-3596-b41b-9d560a497ad4 | -3.9994 | -56.25574 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec1a5d88-150c-39e3-8171-d438cd1f146c | -3.50503 | -54.60535 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d7f6a4-eda8-3ab3-b94c-7bb7e8259cb1 | -5.2472 | -47.93711 | 2026-10-07 05:04:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd28a355-da9e-30bc-81ea-3ae414f8c1d5 | -4.4657 | -54.97136 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb861a1-4a21-3c51-b4ef-35e6e0392535 | -6.19048 | -53.44119 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5ac1a7d-3b99-3202-a964-d85cbfec742b | -3.70273 | -54.21008 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 950ea28f-81a9-344e-b250-74a73ed2c398 | -3.08547 | -54.26198 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a15c8760-89bc-3cc1-8657-fd05b55db9a2 | -3.29838 | -54.03232 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2c39c93d-8de5-380e-a4c1-2cee8ff15832 | -1.12842 | -53.11054 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54ea9e50-b34e-3787-ae48-847ca62fe86a | -2.65901 | -54.31372 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcb57e7e-0ace-35be-94cc-9fc319ba00a4 | -3.76903 | -59.40285 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 829d1da1-f5cf-3df0-bd83-2ac3d0cab992 | -3.05229 | -54.2139 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa25905c-5782-36ce-904b-57c44d79689c | -3.01154 | -54.12506 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8659a301-4a75-3e01-acab-85c3b6fdc4fe | -2.97027 | -54.08271 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 415d3189-428f-3b6f-9dda-3e3d607b7f92 | -3.38484 | -58.19564 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18d0c405-1fe4-3785-92d7-c804c4b74989 | -2.78856 | -57.65386 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22a0c2a1-2e31-340a-9fec-246b6c47db5c | -4.75374 | -55.65411 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 78c7699a-78a9-316d-ab87-f7381f02f6c7 | -3.07281 | -54.14525 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c86f7a-3268-3534-92e9-7672d33e323f | -2.97658 | -54.13041 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1dcc492-7823-373a-8ce9-ba1e0c347eb6 | -3.1694 | -50.4352 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0acf0892-fe31-3de9-8cd9-7d06fbf5aa27 | -3.06659 | -54.25189 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 400e0dce-6bfe-398e-9de6-4f9aed716921 | -6.40948 | -52.71251 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6557bbbf-adca-3524-8bec-412c95a17d98 | -2.77882 | -51.36789 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0f726b1-8aaf-31ae-ae53-14262e4f0dc0 | -3.969 | -55.81915 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08002ab-5a30-3ddc-af2a-5691b32ddcaf | -2.89931 | -56.66826 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 664aa5f6-7499-36c6-a668-5b6bbe0a3b63 | -1.24389 | -55.70594 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05c70a14-477f-37f2-8237-7e752eeec22c | -3.20749 | -53.87263 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 981f3265-f25a-3ee9-af72-2882e1ef683b | -2.95892 | -54.15645 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2db650bd-8a28-363f-8f1f-545a30f9d67a | -3.06569 | -54.16932 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4244bb4d-7a62-33a4-befc-0c400e0820c9 | -2.98941 | -54.77207 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc1254e5-a6a6-384d-8dd8-70898b338db3 | -3.28334 | -54.0409 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc6dc4f5-876d-39f7-8e95-071d4c2eea35 | -2.3057 | -57.08746 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee878090-8ff1-3e56-ac4e-1ab97ae823f2 | -3.18786 | -50.55203 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 318ec4f8-420b-3d0f-85eb-9c993970f783 | -3.10114 | -53.76864 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab355ee2-2a30-3a6b-aacb-ed5c95bdf0b4 | -2.89894 | -54.08277 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f2dfdbd-4244-3cc2-9399-eabb2e229468 | -3.56225 | -54.47882 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdf74f56-84d2-346e-8854-f7607ea39d1f | -3.44337 | -56.93363 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f8eb2e9-0df9-33c5-b143-0cbee8cf7fce | -2.83457 | -54.12627 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f36fbb8c-787e-3b34-b8bc-2a5a3e775333 | -3.66393 | -60.62738 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 462638c3-5efc-3ed2-9707-87266b4ed70f | -3.99995 | -56.25227 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb2d4cf4-5b7e-34dc-8b3e-c4e6e71b82cf | -8.44252 | -46.40583 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 85add743-a055-3ac5-90fa-2f449daf80d6 | -2.13994 | -54.45572 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aebcc775-9971-3bd2-8047-998384ede0e5 | -3.45526 | -56.90216 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 019cba4f-6f1a-3829-972c-438257487273 | -2.95573 | -54.13461 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 641b3409-5372-36c3-9e8d-efb76528e73d | -2.83998 | -54.06963 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 020eb68e-3cab-3ee3-862c-af103b5de5c1 | -3.62124 | -55.27875 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c5aad104-323c-35f2-bd09-a4ff4af5351a | -4.76202 | -55.66594 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c996eef-1e07-3833-93b6-898e5e0a61f1 | -4.08301 | -55.37625 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 994bf892-d72e-3185-9846-71bf27081c05 | -3.06614 | -54.14423 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39b171e6-ccea-317d-bd9a-19914b072e63 | -4.7565 | -55.65805 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca7462e4-cb2d-30b7-9d44-bcf66577a887 | -3.302 | -51.11515 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b97d65-781a-3253-903a-5fc0d60d78f5 | -3.07998 | -54.27545 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87018e90-f89b-3d47-8ad7-567f00123795 | -3.26215 | -54.26447 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3845e6e1-eac4-3d83-9266-675c4e943855 | -3.00806 | -54.76086 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 984e70a1-f22a-3669-8480-5098d8b2de75 | -3.10169 | -53.76507 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cff57356-1b3f-340b-b340-0b622f95968a | -3.09265 | -53.71228 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f131260c-d3b0-3bfd-9be3-e02efb6e3f27 | -3.08887 | -54.28398 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ff29a4ee-3532-369f-9725-6a02eced1926 | -2.91622 | -54.10341 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22315825-3bf7-376e-abeb-e5b495d484fc | -3.68545 | -55.95807 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac1d862-7c03-3c63-acb2-79217dfa4f73 | -3.51011 | -54.63807 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5a73dda-1a05-3f8e-988f-dab935207a48 | -3.26563 | -50.40788 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f24c145-caa2-3d1f-b154-c12f26498526 | -3.29055 | -54.01663 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b66c4e64-ac3a-3cde-94b4-8a450164f9f1 | -3.54659 | -59.48028 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ddd85ff-4b8b-3b57-a4ba-7862ced30d41 | -4.15459 | -55.15528 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 215ab4b3-55f2-3b2d-bbce-c8e4976551e3 | -2.93579 | -53.9331 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60036915-1550-31cf-bdf7-138ab4a60c09 | -3.05444 | -53.93659 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6f924e-50c7-332c-975d-34595ad23e13 | -7.187 | -52.62138 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9fa4bfa-715d-3120-96b1-cf0ccbbe8228 | -5.89906 | -52.04147 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 834e8098-a204-3374-bc6e-83afa454a4c7 | -4.05927 | -56.32936 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7887453f-5c1f-3c10-8bad-5b744db38058 | -2.92628 | -54.12652 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcf1721c-25b0-3c1a-9d8e-47890200f78b | -3.47674 | -59.45704 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46030e14-7b2c-3a7f-b42d-f2261f19bfb3 | -3.1571 | -54.08615 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a67ffb67-be93-3adf-b0d9-022bffad87f9 | -3.66978 | -59.63314 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fa7073d-24c0-3dad-b1e2-80a045df1322 | -3.00656 | -57.74271 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b99ab1-5607-3ae8-a171-c6ee2a37207f | -3.28618 | -54.06665 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2261dea-d65e-3859-9968-6f56e5e9cc2c | -6.12637 | -53.05199 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95779709-fc13-36b7-b5f6-5721efa37b7d | -3.2778 | -54.05453 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7251863c-2199-39fc-a1f7-df0a5e256582 | -1.36311 | -56.91707 | 2026-10-07 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a3d17bf-641c-3927-9152-363bfcb24b00 | -3.28 | -54.04039 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dbf24143-4b51-3b11-a80e-81d8e7e5d604 | -2.8067 | -54.08609 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be0e17ed-b4e0-39d8-a2ea-03664b90352d | -3.28834 | -54.03079 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fe235b52-a494-396a-8ce1-c6522268950d | -6.21219 | -52.83822 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a5c94e5-842b-3cc7-902d-503a56f3def5 | -3.86075 | -55.98867 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README90.md)
