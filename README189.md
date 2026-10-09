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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0869c6-d31c-3937-8175-87d1beba093f | -4.27411 | -55.71486 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb3ac608-7179-31bd-9dcb-f3e529e9d470 | -3.29958 | -53.70176 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec008889-5aa6-3250-9fc2-3577bdc838a9 | -2.98729 | -48.91754 | 2026-10-09 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d93facf-1341-3146-b615-d2a773764c58 | -2.46679 | -56.0653 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbe4924b-997f-332b-b446-21537e7ff51f | -7.5756 | -61.5411 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1bf330d5-71cd-34eb-a6bf-c4c519988959 | -3.46873 | -60.25737 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76d09451-0023-398d-b06f-3bceff99b27a | -3.03068 | -59.15558 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68eeaf3a-89b9-33e8-aa92-02ac7d9ab8f0 | -2.86058 | -59.11482 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b8892da-ae93-31ba-a535-cfe768a66f91 | -3.44099 | -59.56847 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18fcce59-572d-395b-b28d-b698b4364f7f | -3.29379 | -54.05487 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5396b64-b86d-3ac4-affc-8bfefa8d772e | -7.43942 | -63.55814 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6ee1113-4905-3e63-a030-e792307d9387 | -2.41067 | -56.53019 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa5805c8-1948-33f5-a2e5-4b1845299eb0 | -3.26246 | -54.00052 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2845dd6-2965-3cd3-83d2-4ce4057903b6 | -1.29151 | -55.71476 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 799ca439-c070-3778-9ddb-de4b768735de | -3.69502 | -58.82471 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b6b47e-42aa-3cf2-94d1-d2752dbfc45b | -3.70255 | -60.54817 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fad20f01-6d1a-3bcf-b84f-e7a3eaf26b05 | -2.26592 | -48.06201 | 2026-10-09 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e70db052-b7e7-3941-8141-e5f6bad74e65 | -2.54839 | -58.04063 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| debf28fb-d121-3596-9a31-17e79dbe1dbf | -4.10915 | -54.0215 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 727bd869-39e2-38af-969e-5b24f6340696 | -4.52059 | -54.86422 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d838de5-2565-312a-8e4c-61cbc4025572 | -1.37821 | -55.18636 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 234fe907-85fb-372d-a612-f95918f0a654 | -9.20953 | -57.72872 | 2026-10-09 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71775549-2eba-3c24-af1a-6e9c4348c2ca | -8.93031 | -62.41389 | 2026-10-09 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b6b4db-ecc0-37b7-a281-35e6dd1f1cb3 | -2.99557 | -57.7475 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53923ac-276f-3812-b5c6-06f407829421 | -2.83358 | -56.67629 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c989e9f8-dad9-37fd-8195-c9b549183ecf | -3.50098 | -59.27623 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14ba06d3-52d3-3909-9fdc-28a6738c7eb6 | -2.49461 | -58.07819 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90adcd07-3360-39cc-9d83-297ff4d85a62 | -4.63171 | -50.95408 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 535e3d28-396b-3f3a-8bcb-cfeb56ff9a08 | -1.14909 | -54.22099 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57d1b5d5-e309-3d09-9cb9-788b01397082 | -3.72091 | -59.36485 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 905bd504-33e2-305c-8429-9d39806af2a9 | -3.077 | -58.09212 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bb48b9c-1a44-3d65-8ae6-dc977906d140 | -2.81515 | -59.25064 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa66e3e1-aeab-367c-9065-ab938d5a51a3 | -9.22614 | -60.87494 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 328498f9-afef-3e62-9e37-e8cae03e9e58 | -2.54661 | -56.29158 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83577a3a-2486-3651-85c2-66467e6fe6c7 | -3.74456 | -59.62379 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b41125a4-bf5f-3bed-bdef-f5833898f2ef | -10.02909 | -48.03603 | 2026-10-09 05:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05eb105e-45e1-3e4f-811d-078797298848 | -3.84579 | -55.83749 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a6ca442-4145-3af4-bc84-7efb0d9ea9db | -9.25467 | -60.8834 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10152e05-9971-3965-8655-bcb850807130 | -3.31076 | -54.04757 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5519bc2-1204-32b1-9480-1f4f01c978ea | -3.07421 | -50.96726 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f08b52-a108-37ea-a97c-29cade3d9961 | -2.92635 | -57.96986 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f33489ff-2391-3574-8b5e-92aee5529941 | -2.57698 | -56.1855 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d661285-d817-3fb5-b008-46fafa620b6a | -3.94206 | -55.84698 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e235913-595b-351e-9adc-7cc7ce0437e1 | -2.93296 | -57.6486 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f36e65d-aeec-3fc8-b1ca-d430d2d200ee | -3.16101 | -61.08145 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ba5a550-062f-3f1d-b1b4-c281ae394ef1 | -3.82737 | -57.17148 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 599df8d6-e6e8-3032-adae-8e1414d7138c | -3.715 | -60.16526 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41236816-17e4-3229-b6f2-73b63f28f5e4 | -1.1054 | -54.15961 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc08039-6c79-320b-82cd-9811fe3b6d98 | -2.47596 | -56.07441 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abdfe751-c443-3cdd-9ef1-9a2c098eb1e9 | -3.45621 | -58.23 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b72a5e3e-bb42-331f-9871-942f48b65b54 | -3.16391 | -54.7229 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71df3b7b-eb3b-3293-8591-5ef0b4b5e1c8 | -3.5731 | -54.68196 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 865126c5-9c5d-3a8d-a625-8153e3167be9 | -3.09 | -57.6663 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c92cf419-3103-3af7-a594-4c7a6133bc8a | -3.39163 | -57.99379 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f5a47dc-ec5a-37a8-bc77-78c6bfb56d53 | -3.10097 | -53.95201 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 08687ea6-e8d8-3ffa-b5c2-f3515a53b0ba | -7.44403 | -63.55407 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17e074b6-dc42-31be-9900-3c251825297f | -3.63591 | -60.63356 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c9331c-70a4-3ca6-9bdf-540aba82eaf4 | -3.19338 | -53.95272 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5454918b-3102-3c64-ba21-a2a15924a6e0 | -3.01205 | -51.01956 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c726ecc9-fa22-331a-b10e-1bc760c5b8c2 | -2.56488 | -56.17616 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a705894-c52b-3c8e-bca8-1543d50d729d | -2.50528 | -56.15158 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af51c72d-c0f5-3028-a985-54155b5c766b | -3.33371 | -59.51574 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a5c63d-b0e0-3048-8955-b562e7c0ba48 | -2.7538 | -54.04433 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f053ef8-2ad6-37a3-93db-a43c63687506 | -3.31589 | -57.48338 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50705d7f-d3a0-345c-b5fd-d213982fc9a3 | -3.52102 | -59.34013 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be5adb46-d12f-3faf-9b24-871859656b0f | -2.89282 | -54.16724 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 882ff001-6dfd-3d32-a9a6-1ac86407fdeb | -2.4017 | -51.29852 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f39403aa-6d2d-35cc-90ca-d2eac7593dfb | -3.306 | -53.7128 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77c45a4c-fabb-34f4-bc83-112370769130 | -3.09858 | -53.94174 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae41b25f-85a0-389c-8745-8ec46c8ae21e | -3.52447 | -50.34706 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 805b9a5e-d112-329a-8703-eb4949a71e9a | -10.25567 | -59.02879 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c39de82-75cd-389c-b7b2-34574b563d74 | -8.97108 | -45.9087 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8af265c-c321-3a99-9fb8-c58f0c693b38 | -3.79521 | -59.32656 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74a8a488-cd24-32b5-9b6a-19bbc2265e33 | -3.35449 | -50.41809 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a854ee52-b232-32ac-aecf-31cd17120ee6 | -1.54772 | -54.55911 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d696037-62a9-3a62-9228-06e38fa35c59 | -7.45165 | -63.55536 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a26fde-7fb9-3920-b778-9bbd7f2ec9ca | -3.28532 | -57.87055 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 117fa50c-3c87-344b-843d-eafa7ec2ffad | -1.53437 | -54.54816 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e449ef4a-294b-3bf7-9e9f-fdccbf9fc624 | -3.30506 | -53.69228 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb98bf8a-b606-3f05-b1de-931f3492d26f | -3.42876 | -54.06276 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a66f033e-e58a-3f6e-bd91-69f18aace27e | -3.97934 | -56.11733 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3798e5e1-0485-39f0-9b41-bc94a9ceb503 | -3.02736 | -59.15506 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc64f303-37e6-3d60-a096-a0515c122644 | -3.34049 | -50.41027 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6acc37-3baa-3adb-9afa-11854455d75f | -3.89946 | -58.94921 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca09587c-53b3-3759-91ad-2762279d5a12 | -3.68325 | -59.62131 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c4887e3-f1ea-3c18-8656-bee0a5b34acd | -1.10773 | -54.16906 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97af2b7f-a740-3f5f-a5cd-4966d83cbcf5 | -3.54089 | -59.51562 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2007c578-7877-3795-963c-81fa6139fddf | -2.84107 | -57.47748 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb152b2-49c6-38ae-8fc1-c14be9ba3f37 | -9.22793 | -60.87902 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c298cd46-f31c-3d32-bf71-215e5318f7fe | -3.69909 | -47.68448 | 2026-10-09 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1539117f-554e-391d-b35f-4d5ac873e4bd | -4.16021 | -54.33794 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135006b2-cf88-37b4-a698-eb3e86ec1107 | -8.99241 | -45.91178 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 320e8b76-42e0-33dd-93af-68bbb3322d54 | -3.57391 | -54.69406 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d27090b5-d920-36c9-935a-1eec0aa8b65e | -3.0016 | -53.89486 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a1155a1-8b33-385f-b082-50cc6fec816c | -3.09575 | -54.2868 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b39ff67-b906-3e39-829d-72e1946052bf | -3.66208 | -59.15951 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5777d2-2e67-3468-89a9-02c8e7854055 | -3.01324 | -54.09869 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| befd7e0e-866c-3a33-82f1-86d108bfbebe | -3.96525 | -60.00456 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92fba357-b526-3240-bd45-def4c49da4d0 | -3.25356 | -50.40659 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5653d478-acd4-3a3a-9833-b20947959f2f | -3.82868 | -59.37148 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README190.md)
