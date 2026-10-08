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

## Dados Diários - Página 365

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f54a4e0a-66f1-3b91-bb92-fc29be04640c | -6.20126 | -53.26657 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0c0ceebd-b4cf-3205-9d9e-90d6adb69127 | -3.79231 | -59.37339 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1ed7e162-4d94-3bba-8454-5e2924231f2b | -2.7608 | -49.53522 | 2026-10-08 16:39:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2bbace0b-5186-3d84-8c1d-ca51d584a948 | -3.7775 | -52.62807 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f1864919-3d33-36aa-ab74-a2b5ec8011d7 | -1.47823 | -54.55016 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 306e35c5-c3a5-371e-b179-fc1093c08e39 | -6.14422 | -47.93702 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cea6c2e8-898f-3221-9fca-a314d057caa8 | -3.46891 | -57.90253 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c9d893f-8040-30bc-83f1-1fd73ce1e1b5 | -3.47495 | -44.30685 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bf837c4c-be86-39a8-8aa5-a65d2f326d3e | -5.48048 | -45.63244 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7836681f-ee9c-3ef6-8ca2-22748cc52238 | -1.11077 | -54.15442 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3e71b4a5-2011-3136-9bbe-e71cafabbb3c | -5.71385 | -53.47468 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60709460-b4ae-3e8e-91d5-ebb556f8d27a | -5.69738 | -53.46849 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f41df47c-9a72-3341-a288-71681803aa96 | -2.98478 | -54.08537 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 238da8c0-edff-30fd-aa1d-bb6470855299 | -3.16621 | -58.62957 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 30ea858f-f589-3dc3-bfaf-3e78d18c56f6 | -6.19877 | -52.78723 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61b65ae8-eb9c-342d-b44b-0156c8003226 | -6.17546 | -53.42583 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8bcafeae-267e-317a-aa6d-fc52d66db31a | -4.1028 | -44.10846 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 918e3a39-1e96-36f9-912b-77d1fd8d71c1 | -6.45127 | -55.03985 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 071621e1-e932-380d-b32b-b892ab22c5d8 | -4.44269 | -41.46746 | 2026-10-08 16:39:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5dc7412b-673b-3835-8aa7-7a4f2b7f7b49 | -3.57002 | -58.99593 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ee7d3856-e523-3aa5-ad93-9beba19d887f | -5.89579 | -44.17556 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 228f5923-4119-3d94-b984-75e32721255a | -6.66682 | -58.85805 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fd6da278-1656-340d-bb9b-b7ad3780c9b2 | -4.57573 | -54.9544 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9cf04d7a-9a49-3592-83d8-19b25dcc3396 | -5.81615 | -53.85978 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 30bc83a2-71e7-38ac-8748-249ea9ed6c21 | -4.09237 | -44.11008 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| dd06b6e3-a483-3581-bfbd-c593108a03ba | -2.84374 | -57.48957 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 9266f387-cf18-31ab-b840-938819245c30 | -3.88119 | -55.82269 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 330ef871-8afa-35b0-9f80-c37f7c29b02a | -3.03807 | -54.2775 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 91c174da-f444-3bd7-acc7-52df79a92c5c | -7.00392 | -59.12103 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c1fb7d97-69e5-3fd9-a190-42745315236a | -5.23795 | -48.40637 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3dc1582f-79e0-3a99-af01-3db17d3c1cea | -3.40184 | -58.0048 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ea0318b-974b-32a7-96a8-3e52fa108ec9 | -2.06549 | -46.56009 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c649618a-ed80-31a8-8bec-32d0431c2c33 | -2.9308 | -54.04701 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 21a32592-e39f-3db5-85ca-51adb546b818 | -1.13226 | -53.10971 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f17ca7a-82fb-3caa-9b85-c814ec6d5a85 | -2.39539 | -57.89441 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6f14fcfb-10e5-342e-a349-b7a8f1ae0593 | -6.14622 | -52.64157 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 319e313a-f897-3f25-a1aa-8b9132e72da1 | -3.90145 | -44.13121 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 43a0f882-1f90-33c9-b0eb-e72bfd21145e | -3.79261 | -41.67467 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 58c709e2-c11b-37f2-aff4-88934cab2753 | -4.17079 | -46.81227 | 2026-10-08 16:39:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b24c851-e267-3480-950b-06e970a6f040 | -5.63515 | -45.79974 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 598.4 |
| b136a32d-c9cc-393e-bab4-cccdf636b710 | -3.00849 | -54.2438 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a63aad46-de79-39fe-ad45-64c7dd4adb62 | -3.7864 | -59.38025 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1e55dec6-1df9-3b7f-a5f1-27e6e037254e | -6.65887 | -51.82606 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b348a19-e8c6-3435-8473-cd1c11fa2ead | -6.04319 | -53.21238 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 24936a17-0244-342b-914c-f0f51b8603dc | -3.79398 | -52.39717 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e16f3efa-49ac-37e1-870a-1e8b663cc3c2 | -2.26685 | -54.80313 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 36abbd02-88b7-395c-b43b-b8d3992253c1 | -3.30828 | -54.05685 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| fdf053ad-c515-3518-8eeb-196a4c71d12f | -4.50563 | -42.09187 | 2026-10-08 16:39:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ab805e57-3c04-3fec-b12c-b71ca916d1e0 | -7.2097 | -55.19124 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| cba3cdd6-63ef-3c10-a041-b223c0f6e2c8 | -3.77306 | -58.52108 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17843dfd-c89c-3807-a8ba-7089d6084e3a | -2.41594 | -56.85073 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 02410edf-76ca-3554-a068-45ac91757f34 | -2.73716 | -44.32526 | 2026-10-08 16:39:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3955fa1c-00b0-332b-a1a0-ab4a4904aa38 | -4.27877 | -43.93471 | 2026-10-08 16:39:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf4a3e91-004c-3b6d-b32b-bcc0c620432a | -1.88321 | -48.41708 | 2026-10-08 16:39:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90b57f58-ad83-3ebd-a3ec-0d282e69f3f3 | -3.91076 | -55.74456 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ce35626e-a5dd-3b15-8666-bf429b45a32a | -5.34685 | -45.68974 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98c3c6ee-fdd6-3db6-88ba-09ec65d4f654 | -6.45219 | -55.0465 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 3a79aa66-1636-3935-9427-22b06231659e | -3.15138 | -43.0368 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d17c5b8f-e74b-383d-98ce-ddcabdd61d25 | -3.01256 | -54.04526 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c2d34e88-af22-3301-812a-7b365c55ae57 | -5.51663 | -42.82565 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f93acee7-f158-3fa9-84f7-6356ae933eed | -1.21351 | -55.64448 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 00d03ecd-022a-36fd-bc09-58769c994d06 | -1.4244 | -55.71897 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a42bed72-aae7-3244-a50b-c4da4d668176 | -3.78152 | -41.78362 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 873fab9e-88d1-310e-b7fe-b24a89506014 | -5.9535 | -55.34388 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b0254ff-4e26-39d8-b0c9-85fc22331843 | -1.39873 | -48.94048 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d29c72bc-a0fb-3498-8858-9d00522fa76f | -6.17139 | -53.43143 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 8276ddc3-e2d1-3337-826c-cac95b2b4867 | -4.09016 | -44.14182 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 362bccb2-3a1f-3f2d-9cec-7c5426285f98 | -1.32184 | -56.40646 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 249b00ad-4b70-3e2d-8224-412e20c0db11 | -3.52023 | -44.3115 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4850019-8607-397a-ac36-8227c6f138fa | -6.08136 | -53.72608 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8630c751-28de-315b-af37-e571ada7a9a9 | -0.21401 | -49.78889 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 42bb7b1a-e3f8-3b45-9b93-fd31f348a3a7 | -2.46106 | -56.08744 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 813e7fc1-bb19-329a-b9cd-60f6c13b5861 | -1.47745 | -54.54511 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a908ee63-232e-3bd6-8948-7a73f776019c | -1.82515 | -55.09491 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6d8e9ee-e241-3aa0-a141-0cc0a6298b0b | -2.47824 | -56.09188 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a1ba78d1-14ca-3038-93f2-c29b30e3ff38 | -2.98724 | -54.06953 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7bf13b55-cfa6-36e2-9091-b1309a957c46 | -6.12841 | -52.72485 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 03a0fa23-200b-3f5c-8e4f-7e38eb4f1ee9 | -5.52252 | -45.61896 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ffd3a71-6bce-3ff2-b386-9ed1fc874eff | -5.4705 | -41.2195 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bb0c48da-8670-35a2-8930-2fd284463982 | -2.91215 | -57.47835 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 548c516a-3dce-3059-b221-d7931cf7c5d7 | -6.12779 | -53.04942 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 31971522-94dc-3c4e-a0fc-3786c8f52a3c | -7.2167 | -55.16131 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 144eb0f6-9cc1-315f-935e-95f631784208 | -2.39541 | -57.23047 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7e649eb3-976f-36ad-b558-13e6ba47aba6 | -6.17085 | -46.01831 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 354d48a4-7b3d-32bb-93b5-9ac1905d94d3 | -3.28836 | -49.12452 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4d58016b-e5da-3574-b41e-208e2382ed05 | -6.17125 | -52.6565 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 32b28213-ebec-31c9-bf8b-c799542e4a31 | -5.37881 | -44.20782 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2813be53-be64-38ef-a87c-7da72d2d8f15 | -2.94587 | -54.11695 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 491d6ace-800b-34ef-9f2a-4cad4c9cbc01 | -3.25184 | -57.87404 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 261bd587-e1b0-3f2c-a15f-3d1194ced2ea | -4.18888 | -40.39695 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b5338e85-4043-35f9-bc74-4eceb212daa0 | -2.96922 | -54.17665 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3247e661-e270-31e2-aa3f-e0b5029e67f6 | -7.18966 | -52.61816 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 376b7e7e-d8a8-3a9f-9c96-5bf791c456d4 | -2.9571 | -43.51633 | 2026-10-08 16:39:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b410776-b84a-3492-bfc7-73930d24eb28 | -3.11856 | -53.79357 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 94c48585-efee-3a79-a383-59ddeea6a135 | -3.02062 | -57.88018 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 79cb8d47-0b69-3712-8d5f-ef404af038e4 | -3.30643 | -49.12578 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ac25d855-1915-3839-b5ff-7385ef319be8 | -6.23993 | -52.88102 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6bf12fa4-ca16-3b77-b434-edc11c51e830 | -5.10004 | -46.20595 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 2d3f0e88-5171-3c56-a30e-9b7258d553c7 | -3.73711 | -58.86076 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7c9301cc-4c16-3d97-a38c-e8681f10ea0e | -3.38799 | -50.21614 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README366.md)
