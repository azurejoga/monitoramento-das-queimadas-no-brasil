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

## Dados Diários - Página 252

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 512b9984-36fd-3691-8189-e96e66818df9 | -1.9535 | -54.0493 | 2026-10-07 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 581d3a5b-526a-390a-8403-67b9b54331ca | -9.5176 | -67.1173 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 39dbe219-c56c-3865-9806-a3e9d76bb8b0 | -6.02 | -51.7272 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 796035cf-af13-33b4-a6b0-165e7481202f | -3.4761 | -50.1094 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e23b5f7c-38dc-377d-ad41-17a4dd48b453 | -5.9833 | -40.961 | 2026-10-07 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 3edd7997-cdd9-3301-a0e4-2acda022c690 | -3.2214 | -53.8818 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 6679f8b2-d212-3675-8948-cbe7ed069a67 | -9.3566 | -65.7436 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 5db25b80-9e6c-364a-9dd5-96b2aed89597 | -9.806 | -65.0167 | 2026-10-07 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 6b974f88-2381-381e-8765-b2fe6154a163 | -3.6603 | -54.512 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 4bf042bb-9f1f-35d9-a186-11f674b9881e | -8.6106 | -67.0486 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 246.6 |
| 3c269ee0-a926-37e5-b32b-1041b4349756 | -3.5061 | -51.6924 | 2026-10-07 18:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 84056c07-549e-3b9c-b51b-32c56334613c | -7.3935 | -46.2144 | 2026-10-07 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ef3601cf-edba-34ae-bace-42fef005b62f | -3.3637 | -50.4701 | 2026-10-07 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 120cbc6c-7a78-3bac-8b44-be5619a1f77a | -11.6186 | -43.6433 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d97fdc9f-2749-3abe-be6a-6db236da0962 | -3.6612 | -54.2715 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6e3fa422-ee98-307d-ad73-1d6f1a5746bd | -5.977 | -43.529 | 2026-10-07 18:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ec3478ad-45ca-308c-9082-2a6e58f47e90 | -6.5853 | -53.0127 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 13424804-764d-3465-a992-2d730455057e | -2.9271 | -53.9496 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 706678e2-e9b6-3689-a460-bd0932dc39b0 | -5.2289 | -50.8949 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cd2ac758-a967-36e4-89fa-00cc9cae4592 | -6.1502 | -39.4158 | 2026-10-07 18:50:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 96bc4c33-6aa8-33a8-b158-bba6fd9c8d5d | -7.5756 | -46.7112 | 2026-10-07 18:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ca113b30-8b40-3351-9b65-da83e0e73082 | -13.3671 | -43.8742 | 2026-10-07 18:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 75419112-ece9-3266-88e4-5dbbcc1290ad | -5.7189 | -45.1547 | 2026-10-07 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 371855b9-5b51-3edd-b3ec-c0ea2724797e | -3.4944 | -54.6167 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a2156c4f-bb93-3768-b523-70871f8b02b7 | -3.203 | -53.8823 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f68172b2-2445-3777-a375-20ea2d4bcacd | -5.9644 | -40.9627 | 2026-10-07 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 212.4 |
| d77cf9b5-a6cb-3165-b827-556e30f6f092 | -3.73 | -55.486 | 2026-10-07 18:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| d449125d-3638-3624-bdf1-b22c97c25642 | -8.5367 | -67.032 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| a556afed-e877-3e41-bea8-59cda815629c | -6.6039 | -53.0116 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| cc8e6c07-7990-3416-b1bb-ee336a974d01 | -8.5184 | -66.9954 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| d3b0adab-e3e6-3335-b99f-0c3ba942e885 | -5.8388 | -53.8448 | 2026-10-07 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1bbeef98-d5c2-384b-b459-a4b695d026a5 | -2.7044 | -49.032 | 2026-10-07 18:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a44cf2f7-c8f6-3436-94c0-b191614d6c59 | -2.951 | -58.3201 | 2026-10-07 18:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| bb7c4825-1408-34a5-a9db-f826f53f6ac2 | -2.6859 | -49.0325 | 2026-10-07 18:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bb12e7f9-0b3b-38eb-a789-3893bd39ff59 | -12.0457 | -43.3864 | 2026-10-07 18:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 636db13c-46d0-3c21-bc0f-eff7dc6e68ac | -3.5875 | -54.3138 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 13d51139-29f6-3749-a646-77e77a7e19f5 | -8.2489 | -71.1583 | 2026-10-07 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 46888867-d91f-3e6c-a6d1-b8da12087310 | -2.7284 | -47.5667 | 2026-10-07 18:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bfe71c20-bbf4-3a0c-a48d-eb02e5edd385 | -3.5866 | -54.5542 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 55a77c4b-0042-3814-a78a-55394c763069 | -9.4621 | -67.0817 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| b265c394-2d1b-304c-8337-ed9bcb1fdce2 | -4.2744 | -46.3846 | 2026-10-07 18:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| cd1b2102-3673-38ce-bba7-441c9dff4cd2 | -4.1458 | -43.187 | 2026-10-07 18:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 844b305c-797d-3543-bda9-baa9e3a56231 | 1.7121 | -55.6063 | 2026-10-07 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 50984858-18ed-3b49-90de-91a4bc141534 | -3.5678 | -54.6547 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 341cf6a1-cc95-39f8-9061-3f7b1a7c8895 | -11.7143 | -43.652 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| f5a21d4f-920f-3d60-a67a-00bf74f46233 | -6.1217 | -53.0584 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ca7e9f91-2568-39ae-8f95-79f2b722f884 | -6.6223 | -53.031 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 395e6f18-6cf1-3f98-9362-919813df8b98 | -4.3471 | -43.8021 | 2026-10-07 18:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 725891e9-19a0-3099-8087-910fab056157 | -5.2288 | -50.9158 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| dc485dc6-6168-3222-8997-7028e5c51435 | -13.885 | -44.1365 | 2026-10-07 18:50:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 8d42c490-85ee-382a-8b28-62112d431633 | 1.6937 | -55.6263 | 2026-10-07 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a5460bac-388b-3e31-940f-b5d6ec24b6cf | -9.9596 | -43.5045 | 2026-10-07 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d64f67fb-72b7-307d-8166-fdb22a8199c6 | -4.3045 | -50.77 | 2026-10-07 18:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0609912a-fb13-38a1-a2db-1f2db9d727ea | -9.96 | -43.481 | 2026-10-07 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 96c78dd1-fc5e-3382-8433-34cd82f43d24 | -9.0407 | -65.9215 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| b1a61537-5704-3d8c-ad74-501eb915a23b | -6.1974 | -52.8295 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 320c8507-ee53-3f1f-9965-da61c6668f60 | -8.5183 | -67.0139 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 61fd40a3-cb59-3c8b-bf8e-0ab2c8c8866e | -9.4509 | -45.8271 | 2026-10-07 18:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 5fb649f0-7c22-3d74-bd3f-cbb1b7992241 | -2.9271 | -53.9295 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| f9233bc5-43f1-3ca4-965f-17db504cf4c4 | -2.7043 | -49.0533 | 2026-10-07 18:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| fcf41270-01cf-35ba-b259-c10c8940d8c0 | -6.1429 | -47.9432 | 2026-10-07 18:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 91bc7e82-3df1-3716-ac95-d92b4247a99f | -5.839 | -53.8246 | 2026-10-07 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 26407c71-b845-3e79-a15f-3e763ff089f7 | -8.6293 | -66.9926 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 0d75a0b0-23dd-3bb3-96bc-8dbaaf512a4b | -8.8573 | -71.4625 | 2026-10-07 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 115.1 |
| ea29d6de-9dbe-3db6-bea9-1e3817850d35 | -5.9041 | -43.3018 | 2026-10-07 18:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 355e295b-4fbd-3e7e-8095-187f4b54bdd3 | -5.9835 | -40.9367 | 2026-10-07 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| 237ffd6b-e806-3f74-831d-16bdd6f63f36 | -2.0447 | -54.3085 | 2026-10-07 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 0a4bf790-b08f-3372-9d4a-0c74b74184a0 | -6.6224 | -53.0105 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3028a01d-31ae-3908-b1bf-592c869766f3 | -5.4835 | -44.2592 | 2026-10-07 18:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 5a0bb348-dd93-37b8-896f-29bf88f2043b | -3.7809 | -41.7913 | 2026-10-07 18:50:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 7d65535b-829b-347c-ac18-923c3d0e8b80 | -10.5287 | -47.2711 | 2026-10-07 18:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ae066739-a1a3-3255-b387-f70a84f84302 | -1.562 | -47.7465 | 2026-10-07 18:50:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c7990025-29af-3e45-9d48-88be1c4fdae6 | -8.2181 | -46.362 | 2026-10-07 18:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0e1ceaa8-85ca-3bd6-a366-286b2f4692af | -6.6784 | -52.9664 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3ca5ee58-9924-3504-9e55-20769360b4a9 | -3.295 | -53.8597 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 64fdf5da-a2f0-3303-afb7-e6cca0a70285 | -4.2657 | -54.8729 | 2026-10-07 18:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e0f1d0dc-39ed-3c19-8298-092ffacd1d48 | -2.9327 | -58.3204 | 2026-10-07 18:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 5d217cb4-ef5a-302f-9d9b-38c89b79bf8c | -2.6859 | -49.0539 | 2026-10-07 18:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 1bc797f8-1c8c-39d4-b4e8-aed905b2efbd | -3.5865 | -54.5742 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| c58d5886-2e37-3474-969e-2a2d13118363 | -5.7378 | -45.1307 | 2026-10-07 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 371.1 |
| 4af11a09-ba2c-3677-8946-86cd3fcb2176 | -11.7139 | -43.6757 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 404cb12f-ef76-3517-b811-3ef4a03cdc61 | -8.6108 | -66.993 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7b5e73ac-1042-3652-b125-472ddcd8a9f7 | -3.7481 | -51.2079 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 57e63872-08d1-39f9-a44d-194e2cbfc588 | -3.1697 | -58.6244 | 2026-10-07 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| f1bc4f20-2b3c-3775-903a-964cc5e14e09 | -3.0798 | -58.0276 | 2026-10-07 18:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 06922c4d-0d0e-33fc-a3d9-5ef74252a99d | -11.2333 | -44.8678 | 2026-10-07 18:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| fe580fc3-ec35-3d72-8383-ef5f3333c211 | -3.5876 | -54.2937 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 66a2e271-2e88-3103-bc26-16351d09467a | -9.006 | -65.4 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 53af5ce0-6861-31ed-96b5-8d4dd7560519 | -5.8204 | -53.8457 | 2026-10-07 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 88eac967-6a9a-359f-8a81-d245b86db596 | -5.7191 | -45.132 | 2026-10-07 18:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 8e329987-7b68-3a6c-8b48-cebc2ad1ec5e | -9.3394 | -65.4638 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 21552917-09fa-3cd5-a75b-e7a44579048c | -5.8205 | -53.8255 | 2026-10-07 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| a7d2fb21-b2d4-31ab-bc8e-9d5d59360e6e | -4.3044 | -50.7909 | 2026-10-07 18:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2bde963e-9e64-37bb-a398-b4fb5d266f14 | -3.7166 | -54.2297 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7d3b42f2-1b5f-38af-b4be-e19aea05cf05 | -6.1402 | -53.0574 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7f0a343f-4c77-3391-a79c-48b3dfdf4326 | -3.5684 | -54.4946 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 9af5cefb-6c83-383f-9c49-472a10c3c20e | -9.0592 | -65.9209 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| d5238bd9-0952-36de-8e4c-5c0d99f7683a | -6.6753 | -44.9674 | 2026-10-07 18:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cbbe74e3-dde0-306a-98d1-82844e6236b7 | -3.2057 | -58.8354 | 2026-10-07 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9941f730-1201-3b1c-864c-3af98c40fe96 | -9.9205 | -44.8124 | 2026-10-07 18:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |


[Clique aqui para ver as próximas entradas](README253.md)
