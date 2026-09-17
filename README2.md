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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15bb61e5-125b-38a1-8b28-1b06f5c6e407 | -9.6094 | -45.3315 | 2026-09-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 2b583430-500b-33f7-a248-66a5c3ec2806 | -4.5044 | -54.9845 | 2026-09-17 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| f6687122-9c88-3ec2-8540-dca0a7878013 | -8.4796 | -57.6478 | 2026-09-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 934aa41f-a3a9-3410-9290-efead039c9d2 | -5.647 | -44.8192 | 2026-09-17 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 885b79ed-6a5a-3f0f-9381-95159095730c | -9.2753 | -60.6355 | 2026-09-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| d560c8ba-846c-3316-ab56-d14dbe140587 | -13.3758 | -57.026 | 2026-09-17 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4705e9cd-ecef-3948-91b1-04f8fc2b5f3f | -9.8692 | -48.4033 | 2026-09-17 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9f6d14f6-f324-39a2-8586-f56230d9d6f7 | -4.5045 | -54.9646 | 2026-09-17 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| a3d6b64c-b5b7-38a8-a8cb-52136fe94bad | -2.9582 | -50.3149 | 2026-09-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 1d108857-fc17-35aa-abfb-6241ffc0c314 | -6.8216 | -59.1686 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| fcaa708d-7835-3391-a824-fd67c3fb9873 | -9.5152 | -40.331 | 2026-09-17 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 205.2 |
| 4c43c3b5-20e2-3717-b476-a12c654a2868 | -2.9079 | -54.1911 | 2026-09-17 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 9f4032da-8c05-308c-b563-93bf5a49073f | -8.4982 | -57.6468 | 2026-09-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 8cdb3a32-3d9c-3670-80bc-4aef57d8f90a | -2.9581 | -50.3359 | 2026-09-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 31b7cd09-50fe-3632-89d4-b705cbe0c0d3 | -2.6965 | -57.6278 | 2026-09-17 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 91cd2a89-9f7f-3f9b-97cb-1ae5e0b33945 | -5.6472 | -44.7964 | 2026-09-17 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0b2dd09b-f3e5-3d7f-bc07-5875faec133c | -9.112 | -45.7294 | 2026-09-17 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 1a0a3ac6-f674-3c20-94e5-4d6fdf04744b | -2.9767 | -50.3144 | 2026-09-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0a1df614-cf9b-3cae-942a-5e0f52109eff | -5.79 | -45.1 | 2026-09-17 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 303a7162-6d7d-398f-a82f-3959c1442432 | -5.76 | -45.09 | 2026-09-17 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eddb227-f9b9-3b62-b6f9-653af711b4a2 | -5.76 | -45.14 | 2026-09-17 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 812dd8e3-c1c0-3219-aef6-14648d37ca9d | -8.7419 | -66.5628 | 2026-09-17 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 74c65133-5478-30ee-93f2-2797a95085d4 | -9.131 | -45.7273 | 2026-09-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 4a615051-3a1b-3399-b20e-a5b1e08ae66b | -9.4102 | -62.7113 | 2026-09-17 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 303ba5ba-7107-3fef-aaaf-7fbb2d1b6eed | -12.5104 | -50.8021 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 39102143-1a15-3df8-8995-c6f7b5fa4d8b | -12.8543 | -44.386 | 2026-09-17 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 43d766c5-239e-3d8e-a64f-141bda16f634 | -2.9581 | -50.3359 | 2026-09-17 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 10b2592a-7ba3-3d89-bbeb-f00c3d2befab | -2.9766 | -50.3354 | 2026-09-17 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 91b0eda0-c383-3179-ac92-64808702c7f8 | -5.6285 | -44.7977 | 2026-09-17 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f027dea2-b8d0-31e3-b228-897e94068011 | -9.8694 | -48.3814 | 2026-09-17 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| bdff8850-a4eb-3212-8fa1-8cb595dc94a8 | -12.4916 | -50.783 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 4c18e125-90f3-3884-8ead-d8324cb8cb53 | -11.277 | -43.4592 | 2026-09-17 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e1023b2c-37a9-3a25-a163-2c17d1f85be3 | -2.9079 | -54.1911 | 2026-09-17 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2db9ee46-22b7-3daf-8684-ff75e51d5236 | -6.8215 | -59.1879 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 2e2ce38b-1b16-36ba-b17e-4d8cb2675c58 | -3.4757 | -54.6972 | 2026-09-17 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 6a4960f7-555a-35a6-9678-a8d3de529ecc | -6.8962 | -59.0303 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 257e8af8-c7c1-311c-9165-335612248053 | -14.1405 | -48.7317 | 2026-09-17 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8213ef79-5097-3b67-9740-d9a8d883d195 | -9.1056 | -60.9703 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 6f2f67ef-e030-340a-a512-196e378a4f97 | -9.6284 | -45.3293 | 2026-09-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| e2d2e13f-2812-380f-b5cc-b30ef335d8c3 | -8.7604 | -66.5623 | 2026-09-17 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 044a114a-c974-3cdb-a664-3042393cf8aa | -2.9582 | -50.3149 | 2026-09-17 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ca1245a0-649a-37b0-998d-f50313263d2b | -9.8881 | -48.4013 | 2026-09-17 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0eddb9eb-f9a5-3591-9948-45f5648c9f4f | -4.5045 | -54.9646 | 2026-09-17 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| f8f1b9db-dabf-39ff-85ad-b038936bf857 | -9.2753 | -60.6355 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2c7c89ba-769d-39fa-8572-0f01674ddaae | -13.3949 | -57.0242 | 2026-09-17 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| d19e606e-4b5c-3278-a013-5ffdd12b7b41 | -9.2754 | -60.6162 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9898be72-76d3-35b8-9d8a-0643cb81a56f | -9.8884 | -48.3794 | 2026-09-17 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1038011a-5981-3ba7-8a5b-74a1e3c451dd | -12.5101 | -50.8236 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 018f9ce6-4b7a-372e-a400-6824c8e6395e | -12.4913 | -50.8045 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 350.0 |
| 3f209337-afe4-366f-ab3c-142235506620 | -4.5587 | -42.9523 | 2026-09-17 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| bd7e3341-48e2-3b09-90f8-64d839a49278 | -12.491 | -50.8259 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 182.7 |
| cc98a304-c377-3cc9-b5b9-11d1d315f026 | -6.9309 | -63.0301 | 2026-09-17 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8a3b51b3-ffe1-3483-919d-33e1747880b7 | -9.2939 | -60.6345 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ed14a570-3de4-3494-b13d-596fe006048d | -5.6472 | -44.7964 | 2026-09-17 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3cf7a8af-8fb1-3cb9-a75f-e7e8d48faf27 | -8.4982 | -57.6468 | 2026-09-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 4d03a8fc-00fb-3264-9775-922c267449cc | -2.6966 | -57.6084 | 2026-09-17 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8938504c-bc3f-3b9d-9dfc-c1b4270965e6 | -3.4941 | -54.6967 | 2026-09-17 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| bf7ed721-9118-3bb2-9946-80174279e644 | -6.8031 | -59.1886 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| dd062040-9522-3234-b0f8-ccec0986c6a7 | -9.6091 | -45.3544 | 2026-09-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 338.9 |
| 8fe02fe8-2846-38e2-9648-001511afa062 | -2.908 | -54.171 | 2026-09-17 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| cef6053d-e414-3255-ac1d-610dfc998243 | -9.1117 | -45.752 | 2026-09-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bbb06029-8158-3538-89de-6790a485278c | -6.8032 | -59.1693 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 658defa6-ed60-3339-a5ed-f5086ae21ef0 | -13.3758 | -57.026 | 2026-09-17 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 49660258-1f31-3984-a746-41af920132b0 | -9.6094 | -45.3315 | 2026-09-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 444d1a7d-b734-3c8f-b5ab-053d96dcd40e | -6.8216 | -59.1686 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a32cad99-235a-38a1-bb4b-cdd5f62eae29 | -3.8096 | -58.8994 | 2026-09-17 00:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a0c0f5e2-0c28-3733-87eb-26b38a76d5d9 | -3.494 | -54.7166 | 2026-09-17 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 5196de9c-af22-3aea-94b3-7687265d3529 | -4.5044 | -54.9845 | 2026-09-17 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 19cc8e1b-a4b1-3a14-8c6a-6c8800ad0724 | -6.713 | -58.8058 | 2026-09-17 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 35d5b3ff-3a83-345b-9af5-5421fecc2ec0 | -8.7603 | -66.5809 | 2026-09-17 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f28d0db9-a4d5-3153-8b7c-e8ad51f17ab0 | -2.6965 | -57.6278 | 2026-09-17 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| fe5a96ac-7475-3044-95f8-eadbca951c62 | -11.2766 | -43.4829 | 2026-09-17 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 632955ad-4225-3426-8318-aedc1eab2798 | -12.5097 | -50.845 | 2026-09-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 65fd6005-e166-3abc-8882-1a4222daccbf | -6.8401 | -59.1678 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bd4b24c6-c297-3d58-8eda-0e1b31dc16c8 | -9.112 | -45.7294 | 2026-09-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 233.8 |
| ffddf547-e31a-34da-998e-3b7be924c6f5 | -3.4757 | -54.7171 | 2026-09-17 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 215.5 |
| ec6ce349-e61b-3f0a-a217-9178ba67ec81 | -9.1057 | -60.9511 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| afc260f9-8e91-38fe-a2e8-16a920409277 | -8.4796 | -57.6478 | 2026-09-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| c7e81f72-37f9-356f-ad0e-358a8dfb3f0e | -9.628 | -45.3521 | 2026-09-17 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 351.4 |
| 7303068c-7aed-356e-a134-6c03ae8bb22e | -8.5986 | -44.5762 | 2026-09-17 00:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8115edaa-d85f-356a-9eaf-c2b92d475014 | -9.1123 | -45.7067 | 2026-09-17 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| dd2814cf-190d-3933-af97-a57814b6a884 | -8.4983 | -57.6271 | 2026-09-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 824e659e-7219-378b-b98f-d069f1f5ea8d | -9.294 | -60.6153 | 2026-09-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 3c8a8065-0ae8-3c34-933a-f01dab26304b | -6.9147 | -59.0295 | 2026-09-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fac2c2c0-f8cf-3008-aa4b-25a2caacd3a6 | -8.5797 | -44.5783 | 2026-09-17 00:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| ab4c2b80-b7d2-3b78-9d84-d3ccb048f7f1 | -9.8884 | -48.3794 | 2026-09-17 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 47c8c6e5-f49e-3a3b-a008-a483515686b2 | -11.277 | -43.4592 | 2026-09-17 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3993d5d0-25ca-35be-ba4c-05821b367387 | -9.1056 | -60.9703 | 2026-09-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9389cfd9-9954-303d-82ed-c8f4a35baf31 | -9.2753 | -60.6355 | 2026-09-17 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7ea5e1d7-f531-3244-b1a3-d2062952f11f | -9.6091 | -45.3544 | 2026-09-17 00:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 874c3f07-3da9-3c34-99b6-f5aa3f0182bf | -2.6965 | -57.6278 | 2026-09-17 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ce20cab3-1b8a-340d-a242-8105c3216a03 | -9.1117 | -45.752 | 2026-09-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 69de5e19-5896-3e7d-8cdf-efe40fa7c185 | -9.1313 | -45.7046 | 2026-09-17 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a2a057f7-c46c-30e2-89e2-2f47aeee8fdf | -13.3758 | -57.026 | 2026-09-17 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8f3b1f02-909d-3c4a-ab70-21e89c7b5077 | -5.6285 | -44.7977 | 2026-09-17 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 1bab5b9a-80ad-30f0-8980-5835ad2bc9fb | -10.7412 | -53.9991 | 2026-09-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 1bc6106e-3086-3eea-b5da-c43dad08f744 | -8.5797 | -44.5783 | 2026-09-17 00:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 01b66647-2cc4-3510-88f2-292bed061859 | -3.494 | -54.7166 | 2026-09-17 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 903e4a39-b87a-3710-b85d-a87ebf4387d6 | -11.2766 | -43.4829 | 2026-09-17 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 94be5a92-ae7f-3fff-8058-96a7a3dfd2a9 | -12.491 | -50.8259 | 2026-09-17 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |


[Clique aqui para ver as próximas entradas](README3.md)
