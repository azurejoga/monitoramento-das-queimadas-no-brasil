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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d07ebfe-3996-3ff3-b668-c4fd75e34a77 | -11.0863 | -45.6688 | 2026-10-07 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 4de0ad14-f592-3493-b927-3571b3cd54f4 | -9.1174 | -65.359 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| e48aab85-c4a9-3d39-9228-be27a6b3e1d1 | -3.9842 | -56.2295 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 546bf87a-a9c7-3723-ad97-9683cbbac775 | -3.6197 | -55.5089 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 226.8 |
| f0f0e206-6989-386e-af86-eb51d1c80028 | -12.1742 | -44.7284 | 2026-10-07 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 408.5 |
| d3be37cb-c0b3-3eb9-bdeb-5d3cafd45856 | -6.1973 | -52.85 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1c311838-7233-3cae-9e87-012396f07909 | -3.2451 | -57.8693 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9a50bee2-c38c-37d2-9f3e-c7bea418336c | -3.2576 | -54.0418 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.2 |
| e3e7a1c4-68ba-3011-84ca-f2466eff0186 | -3.295 | -53.8597 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 436cc335-d60a-35d4-99c8-5c7f07e990dd | -6.3284 | -55.3077 | 2026-10-07 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6da7d9f0-9971-3169-8f35-f9e4643e7439 | -1.5118 | -54.8153 | 2026-10-07 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2e70b258-acf2-3e86-8f4d-65c56829a658 | 1.5283 | -56.0227 | 2026-10-07 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1f839821-f1ca-3d02-92ed-2d61a454d9bb | -2.788 | -57.6455 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9c5dae1a-8195-34a9-8b9b-ed40505f8afa | -12.1746 | -44.7051 | 2026-10-07 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| bcd31654-d706-37f7-b545-eb084fc485b4 | -3.8383 | -55.9774 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 227.8 |
| 534629df-6bfa-3eb0-b88d-ef61563a27d2 | -3.4943 | -54.6367 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bf3bb0cd-182a-314b-ab26-7290a6f836d9 | -9.6757 | -65.0401 | 2026-10-07 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5179cd85-56e4-3915-b9a0-4a5b89355b4e | -7.3846 | -55.2124 | 2026-10-07 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c0d106b4-45e8-37ac-933a-7fc577226c6e | -1.2455 | -49.062 | 2026-10-07 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4911bb35-238d-3a09-a662-123815d5a528 | -3.4312 | -56.9307 | 2026-10-07 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5a8dc8d7-8734-349f-ba90-b5e637208aff | -8.6291 | -67.0482 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2e1be391-08aa-36ea-bb41-dae9f7b35b5d | -11.2337 | -44.8446 | 2026-10-07 15:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 609ee23e-d9c1-3597-af19-96fdcf2389b1 | -6.7066 | -45.5765 | 2026-10-07 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8f24333f-9758-3a57-8c46-f2cb5b2bea22 | -11.1556 | -46.0916 | 2026-10-07 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 53b21db6-da8a-398f-af6d-267bb810931d | -1.8803 | -53.9701 | 2026-10-07 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 31905f2e-647c-30f0-b3ed-2383bacea6d7 | -11.0867 | -45.6459 | 2026-10-07 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a27cbc42-650e-34ac-b1eb-aa489a32c8c8 | -3.8567 | -55.9769 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 198.6 |
| d4225620-a916-3464-84cb-2c76af0cee86 | -1.2922 | -54.5585 | 2026-10-07 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 75273fe4-5e30-3b7c-ba0f-5944dd858e6f | -2.998 | -54.7492 | 2026-10-07 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c33ddc3a-4943-30c6-8e9c-900cc56cd4f4 | -3.476 | -54.6372 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2521eaf5-dddb-352d-95fd-f96bbca9bc77 | -2.7879 | -57.6649 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 7169dbdb-115c-3e11-b240-a0df2be3fb21 | -2.7696 | -57.6653 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 36a5cac0-4323-3571-b591-dd866d89a5c0 | -8.5367 | -67.032 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7e6c5250-3e81-3f05-8319-29f7649a9d98 | 3.5263 | -51.2778 | 2026-10-07 15:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 91460cb7-69a9-3339-bee5-c491d2627248 | -12.2136 | -44.6758 | 2026-10-07 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 922b6ccb-b4d4-35a1-8564-09a075463f16 | -6.3468 | -55.3267 | 2026-10-07 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d60d6a5a-cec3-3810-89b9-b5c2af6c4ca3 | -5.8204 | -53.8457 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e5735880-6bec-300a-bb6c-131fdfa173e9 | -9.0046 | -65.6988 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7e1a4f95-db61-331e-99c2-d0bd6c185782 | -8.2621 | -54.717 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 37fae1d0-c636-3233-a9fa-77cb690d8e28 | -3.0074 | -57.7578 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| cba41b1b-0ee8-34aa-ad8a-8c36f2da5c4a | -9.0859 | -61.1437 | 2026-10-07 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f169bc57-9e2c-3eab-82bc-6b468bf831e3 | -1.4569 | -54.796 | 2026-10-07 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 7f4be166-2934-31b9-8015-e85966ed0027 | -12.1939 | -44.7021 | 2026-10-07 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| c0e916a0-545b-32a0-ab13-f483dea772f5 | -3.0191 | -53.9071 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 11d0f305-be87-31cd-91b7-2e798a61452a | -7.2 | -55.1026 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 532.0 |
| f04164ba-6e92-3431-bcc9-889f483efc09 | -3.0074 | -57.7384 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 26772147-4939-378a-9e21-6707eec962e0 | -1.4301 | -49.0382 | 2026-10-07 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 4364625f-d31b-3b2d-b494-d78f8f27adf1 | -2.7697 | -57.6459 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 699f32e6-9ad1-3f83-b142-95180abfe239 | -1.3927 | -49.2727 | 2026-10-07 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 450c3343-1b1d-3faf-a96d-0fb88e64ccf0 | -9.0612 | -65.4729 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a97892bd-233c-3b18-85e3-bba066524506 | -9.0988 | -65.3596 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0f02499a-8939-34ae-89e0-98f6945e0904 | -2.4245 | -56.5402 | 2026-10-07 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c3c775b3-d052-3c0b-b1db-22006fec91ba | -1.4569 | -54.7761 | 2026-10-07 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 102b7338-13ba-3039-88b5-f30310617eee | -3.4495 | -56.9498 | 2026-10-07 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| f1745833-8095-3dfd-8ff2-7a0137c2007b | -6.4413 | -55.0224 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 383bdae5-2c6a-31b7-bef9-42ab1631eca6 | -4.0614 | -55.3175 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9f34e7a7-2358-3e71-b8a1-f0101b0fdd73 | -6.1217 | -53.0584 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a9e903af-96a5-3e6f-8209-310066802207 | -3.8382 | -55.9972 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| f19e28ad-22c9-378a-9d7e-7a13439fca75 | -3.4312 | -56.9502 | 2026-10-07 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 35e894ae-acd7-3a7a-afb9-54ab8c64a7ba | -2.9739 | -56.6278 | 2026-10-07 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| bf6d3ec0-3dce-3012-8ebf-ec5d06b61995 | -3.0265 | -57.466 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ecd5732c-7850-31e3-8bfa-f8bc7bb4041f | -9.1408 | -64.3836 | 2026-10-07 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f5bc15f8-e7f7-39d6-86c4-09c3cccb0eed | -3.1697 | -58.6437 | 2026-10-07 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| c8df50c6-980e-3b8c-af4f-30bd99b0ce5b | 1.8768 | -55.7227 | 2026-10-07 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3a951ec3-67fa-3c8c-b4f2-2ec83855916a | -2.9271 | -53.9295 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7503c4ee-46a7-3a60-9414-d409f481cfac | -7.8789 | -72.3492 | 2026-10-07 15:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 2ced504c-fb39-3cf2-86ef-8c4bde0cce8d | -3.5495 | -54.6352 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1a6968f0-ef1c-3d9e-8a07-cbb7a8ff25a9 | -9.1257 | -67.8322 | 2026-10-07 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| acf94dc4-7cae-3518-9497-cfe3ca78a315 | -6.0076 | -53.4919 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| afc96dd9-cb9f-3fdc-8b45-15f78c3ec7a7 | -3.2577 | -54.0217 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d7103b5d-e83c-30b2-87ca-1967025c2c88 | -3.1697 | -58.6244 | 2026-10-07 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 653f56d1-64c6-38c5-a21f-da7d190d8f10 | -3.2761 | -54.0011 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 024699f6-3208-33b8-bb9a-376581ff9414 | -1.4847 | -49.4411 | 2026-10-07 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5296df1e-c4c5-3aa7-919a-3264126cbb57 | -3.0992 | -57.6395 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 89053c89-d57b-3d01-bad2-24f5d0bc4be1 | -8.6325 | -44.871 | 2026-10-07 15:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 2c1eaf33-5488-3669-9997-87bbb1638533 | -4.0614 | -55.3175 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6c60c87a-bddd-36e6-b772-70aefca92510 | 1.8768 | -55.7227 | 2026-10-07 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 222d863a-7bb5-30f2-8890-844133822f34 | -12.1742 | -44.7284 | 2026-10-07 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 543.9 |
| 4d32815e-b29b-3d0c-ba3d-3338ad38fdf3 | -12.2132 | -44.6991 | 2026-10-07 15:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 9bc15a16-8eb6-327a-9e2c-04454b4583e8 | 0.7266 | -51.3749 | 2026-10-07 15:30:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e533f70a-87e4-3478-b42c-91dfdd637d62 | -9.0232 | -65.6982 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6b27005a-8810-338b-aa08-b02e0d1dd3d6 | -3.0992 | -57.6395 | 2026-10-07 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 7fea45fe-4adc-3aba-b9a0-a34107bff632 | -3.0192 | -53.887 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 546d9a84-9d38-3f8b-a372-642634776977 | -8.6106 | -67.0486 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c03531be-3d5d-3bb4-a5ca-8fa972694f47 | -2.8575 | -59.1107 | 2026-10-07 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e31c7d14-54bb-34be-b184-030ad6159366 | -3.9666 | -56.0527 | 2026-10-07 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b02b6c98-735f-3700-b041-ae04d86bc2fe | -3.0992 | -57.6589 | 2026-10-07 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| b0082f75-9297-3389-beb7-bb822975163a | -6.2159 | -52.8285 | 2026-10-07 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 250.6 |
| 4bcb0e0f-0a45-378f-a66c-34cfee36282c | -3.73 | -55.486 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ddf9852a-4f5f-36ea-84d7-f25bc4b0999b | -1.4569 | -54.796 | 2026-10-07 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bc5e9eea-e323-33c4-b497-c6563f7de0a0 | -3.1114 | -53.7839 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 99ba177c-0c1f-3b48-b032-8326a14d4283 | -4.905 | -55.8642 | 2026-10-07 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ffe7e30b-93d8-361a-a251-192aa691f493 | -9.1542 | -65.4138 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 65ac4ea4-ea04-3890-96ec-dc0f293f5b3f | -3.2951 | -53.8395 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1aeb42cb-19ef-36d6-af98-1945293d0dab | -2.9739 | -56.6278 | 2026-10-07 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| c38a0c52-0f08-3669-9695-97fe70763ebc | -3.4944 | -54.6167 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| b35cce69-8132-370b-b9be-9a944a7feb18 | -0.3768 | -51.9947 | 2026-10-07 15:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5ef5942d-66ab-3217-a402-bea8aec9a120 | -3.8756 | -55.8184 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4fb19eb2-5ab7-3343-8f56-b6c4fd83c2a8 | -3.2483 | -56.798 | 2026-10-07 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 34699c45-ec55-39d1-92b3-9a2644a8d301 | -2.8573 | -59.2066 | 2026-10-07 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |


[Clique aqui para ver as próximas entradas](README141.md)
