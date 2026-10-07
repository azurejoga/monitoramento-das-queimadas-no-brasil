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

## Dados Diários - Página 235

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2218d92c-c204-32dc-9d63-d9c6c5696c90 | -3.0422 | -53.90701 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41c0948d-084a-3b77-aa17-0669a55e16f6 | -3.94079 | -52.02447 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e86894c4-9bff-3cc8-879b-ca62b567b55b | -1.80585 | -57.10804 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 60e863ab-da81-3e0f-8a0a-c57b416f5953 | -3.54054 | -50.10428 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea688d8a-a25d-3b9b-b42e-883454a8dd46 | -2.22354 | -53.71947 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53bead97-afb6-3ed2-a8aa-40062429990b | -3.56504 | -54.49234 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9855da57-7e62-3036-8c66-2089b47e15d4 | -2.46942 | -56.06787 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4352fe0d-dd49-37ce-afca-7c02232f574b | -2.77767 | -54.06017 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| b92dd2a6-c0ac-3380-8637-4ef598bab77f | 2.17871 | -50.95653 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1a9587fd-7259-3046-8ffb-ffde81640799 | -2.80376 | -54.08749 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3951b07c-3e91-38e6-afff-df4b05380afa | -3.50219 | -54.6317 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8fa52c80-9271-337a-813c-a8a6b42524c1 | -1.48171 | -55.87261 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 832dd47a-8e7a-3855-b3c5-3197a77901ca | -4.36488 | -56.23545 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b8768e31-8bd1-3926-87da-4343d06c06d9 | -3.08605 | -54.24605 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67e20e51-1467-3c71-82c8-583a60292e97 | -3.5061 | -51.6925 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 10a87963-ab67-3bbd-b548-ee5e7f885f3e | -2.64971 | -56.82089 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8815c4bb-7fd3-3923-891c-e1cd4d667919 | -3.63098 | -55.51268 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| fb57658b-0648-34b3-aa93-982c9b38bb75 | -3.13175 | -54.36677 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| fd1f22fd-a946-31f9-8b03-154cff72b86e | -1.71646 | -55.43637 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f6eb5ccc-f68b-30d8-8235-e842684e41bd | -1.47293 | -54.76753 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 519332b6-cd99-3ac6-9561-8ec236280497 | 3.2213 | -51.31841 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5e6fa50f-d8ef-364c-a2dd-d3aaddba91de | -3.86341 | -56.00131 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e749d28-f959-3a22-8301-59c6f150c72b | -1.28152 | -55.419 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9a58329-5633-3bf0-820d-9481a24a5fd1 | -2.94407 | -44.22663 | 2026-10-07 16:39:00 | NPP-375 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c984ca0-43cc-3b13-90e5-418f46462513 | 1.97412 | -55.87469 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d58455ed-309b-3d57-bb80-d23101f12672 | -3.12315 | -50.34216 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d8c6904e-4d2c-3ee4-9db7-0c1810f6811c | -3.1013 | -53.72111 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b53a47ce-1e80-3cba-997b-8fa331798aea | -3.05409 | -54.14061 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6f8721d7-a4a1-3717-b520-28855bb38b91 | -2.94221 | -54.06357 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b7a0abf9-41aa-367d-b599-2a44b618ddc9 | -3.10341 | -53.77059 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5aa27b6b-6652-3b94-b091-a15c73b4660d | 1.53205 | -55.96424 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08f37d9b-439d-3814-a17e-627db660add9 | -3.24378 | -56.81013 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1b5b0e7d-781c-3636-81f8-efd1f45bfe5a | -3.10214 | -54.27976 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 166fe3ad-7150-3cd8-9be1-3e0755faee61 | -3.58221 | -54.65091 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 074599f7-e57c-3fb7-912e-6e6b5f63d30d | -2.9499 | -54.20356 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 573c0f72-a371-3c13-9584-dc0ac72115aa | -2.64017 | -56.53967 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0d6ceb52-b48a-359a-9404-375d8cfd0e6a | -1.80042 | -57.11642 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ca6d01dc-0c1e-358c-9d95-ccaf1f9d417d | -3.69689 | -55.49083 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a7c829eb-7122-3148-a487-441ef90efa91 | 1.89384 | -55.70806 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5387a442-4c3e-3289-8f8e-071302bc4b59 | -3.08934 | -57.64835 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0cc8b746-2eb6-3317-94ab-a5b1d2c30f76 | -4.92097 | -55.85546 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ee8d0909-84f3-3e26-9bb8-f3ac58a60df8 | -3.2662 | -50.40397 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f11575b1-8667-394c-b493-5cd7a123a751 | -2.78273 | -54.09407 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2c041935-8c8d-307f-acb8-904a9cc2f50d | -2.58102 | -56.14867 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d3eae77b-486c-3d4b-a8ee-872b80d1021a | -1.40376 | -54.60555 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 78aa890c-a0c2-3d88-b3d3-925ef2fb1946 | -3.54414 | -50.09996 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d2524dbb-68b6-3e05-9723-ed85f995664e | -3.53264 | -54.64254 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5d0d6df8-2fa3-3b78-abd2-22f8b7a49390 | -2.49575 | -56.12199 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3724e483-666b-3ce3-bb42-2d4b631a994e | -1.28252 | -55.85849 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 4fa1ff82-422b-3346-8e26-647d08396316 | -3.88501 | -52.21228 | 2026-10-07 16:39:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac4839b7-7c27-3b29-9223-80f94bda8c43 | -2.46528 | -46.02309 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b9062b6-6b5d-3d26-9865-51bb02d4904f | -2.79299 | -54.08905 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| a6c4d93f-2d6d-3329-995e-40ac6abd045f | -3.06917 | -54.2464 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 63bdfe56-72ba-3022-aecd-ee0e5be6b116 | 3.21147 | -51.32786 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e27727d9-4ed5-3a59-af4e-c9e56aab6dad | -2.78533 | -51.68021 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c05b2c2a-bb43-373e-845e-79e4d14f7b99 | -3.26424 | -50.41996 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6137bc3c-cb71-3956-982c-2f60ab3e4020 | -2.98234 | -54.03703 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66f83168-7111-3f63-b80e-6a934955ea45 | 2.11124 | -50.83288 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 60264e64-ee3f-36c7-a967-2a7f0feb6e47 | -3.0982 | -54.29116 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 69de7a4e-abd5-3414-b704-d6e98c691ed3 | -3.06479 | -54.25434 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31aa3605-e3ca-3b9c-bbf7-497dbc47952d | -3.99632 | -56.25899 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b39d35b3-043d-339e-8df5-97af63f9f535 | -3.21857 | -53.87712 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b83239f-e5d7-3d66-971f-c0ecec3c946b | -1.74295 | -55.02813 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 35b3de50-235e-38cd-b398-bc45dd0718d0 | -1.12362 | -54.11522 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bbf41d01-520b-396d-950c-285d3640a170 | -3.289 | -56.9859 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| a4c5cc74-193c-3629-a817-0dc2e3dc2b99 | -4.12968 | -54.25064 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1282a1c4-0a8a-3679-8f5b-72ee96de010b | -3.01104 | -57.74262 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 886963ce-5688-362f-b92b-f2dcb81f121d | -3.63701 | -55.51206 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4c103371-9060-3519-8cf6-616abb7024e4 | -3.16245 | -54.73309 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 89835738-d28e-3013-92f4-b3673021c16a | -3.22487 | -53.883 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0e55e126-4c73-37a9-8907-9cdb4f9b2db8 | -3.44265 | -56.94527 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| c32b0a61-5e83-397d-bbd1-b4d0d0d50c99 | -3.4455 | -50.62696 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 82b19fb0-95ec-337a-81a0-6d5c7feb7da6 | -2.79096 | -54.07553 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 234.7 |
| a0afdd4d-e512-3e10-bd0e-d34ac6de830c | -2.50376 | -56.12902 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7258e450-208e-3fa8-87c8-4d88fea10366 | 1.16818 | -50.03943 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14c3baf6-06d3-3938-b8d7-ae41eaba4124 | -2.99512 | -54.04897 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 611155fe-7541-3b17-ae6d-6a6016ecbfb8 | -3.18527 | -50.55785 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7ca1e400-4e3c-3685-acd7-bb77062b32e4 | -3.07076 | -54.25686 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b2062449-34db-333d-adfc-c5cee11b62a4 | -3.27126 | -54.05238 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e89cd74f-870f-3c98-a512-dd8c79a81337 | -3.26003 | -50.42059 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 537cce51-a6fe-33d8-9896-3288f441a630 | -3.29443 | -54.05957 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d78ac4d-dac4-3bdf-800a-aef8fbcb8055 | -2.95559 | -54.16788 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21ffa689-34c7-3849-bc27-ae874f51e54b | -4.2468 | -51.04735 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9c17a760-cf3b-3d43-8fd1-4d18c563f780 | 2.0153 | -55.85114 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daa87c09-e178-301a-ac5f-903ab1cbc2c8 | -3.09699 | -53.72829 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 594a6aa3-f7cb-3b74-959a-c975200a091c | -1.48208 | -54.49781 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ae245430-978e-34d7-b1b7-cda43c210703 | -3.1097 | -53.77634 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 75a9159e-40f6-34be-989b-0ba4b966c44e | 1.76036 | -55.55869 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b8a02ee-a8fc-3b9e-85a7-3a5e53233e18 | -3.5645 | -54.48863 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 299f0e6e-ab12-3b22-a495-a4e4d394707e | 1.75695 | -55.58371 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b6cab436-ba2f-32c4-adc4-2c9d1a20f233 | -1.74021 | -53.70476 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 974bb967-0ad0-3333-aa30-1f3f02adb14a | -3.18702 | -50.56972 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 119732f4-9790-39d0-9fb0-1192b5ddf33a | 1.76723 | -55.58597 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d86209d1-7bca-3588-a5ca-17d969fedcc1 | -2.99884 | -54.11112 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 62b54361-a798-3ad6-ae12-874c8a761a87 | -3.10893 | -53.77855 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 627a60bf-f817-39a8-84ea-31be000b3b86 | 3.21257 | -51.29536 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| de870e97-a1a4-3af6-8363-97e0f351f5db | -3.28512 | -54.07165 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 45d548b6-2fd7-3710-9209-62457e89ce8b | 1.8094 | -55.5364 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fb5a378c-4bfc-3ac3-aea2-3a35c1e9bcda | -3.99258 | -56.26138 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ff9e9c8-eda7-32fd-a931-9b9d99aec96d | -1.40361 | -54.60666 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README236.md)
