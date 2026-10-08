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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a267e4e-f8f1-360a-830c-042bb752d7d0 | -3.05621 | -53.92545 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e00d171-b9a9-33ab-84d3-8e99ecf9c878 | -3.71672 | -54.22766 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3c86559-e5c2-3876-9e87-8689c1905bb5 | -7.00424 | -59.1154 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cff512df-ef7a-3357-a3a3-4c00b5d4ba68 | -4.15241 | -54.9189 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb55e7ef-5af1-3caf-a490-9262bf56ab2d | -2.46273 | -56.08683 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5633d5c9-c9a3-365a-b2ec-50f44301a529 | -3.08592 | -53.95079 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 64f7e84a-052b-3398-88e5-fd782e5da8f5 | -11.86316 | -43.55674 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3383b171-f2c9-3d2c-b1e0-a84fb6cfc9d6 | -5.81637 | -53.83553 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63bac85f-a01b-39c1-a623-795211f3536f | -5.95617 | -55.34168 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac37c6e8-a94c-3a13-9518-ffeffdc71aa5 | -3.63617 | -58.93995 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4538f60e-0f08-373c-a1b4-83c6143c3733 | -3.17687 | -58.63515 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29475e1a-04ea-345d-bd20-c46579a24a13 | -2.9546 | -54.13657 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 53422a48-b091-36de-b12a-4a20bacd7b43 | -3.30653 | -54.04885 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1fa867c6-886b-3902-8521-363e3edddd28 | -6.95584 | -45.25337 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4ec8cd5-c33f-3d5b-ae52-7546800bb7f2 | -4.27022 | -54.86305 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eb76f47-9341-304e-b55d-4ba6eb1f75ae | -10.50209 | -47.2941 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45459615-77a6-3e62-8e7b-1076e042f23a | -2.77139 | -54.08802 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 720295f3-793c-33f1-88a2-706f73dee9a8 | -3.02127 | -54.07498 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6498c77e-83af-3ed8-adb7-208c83abcceb | -6.43488 | -60.05906 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff1babb7-40d5-33df-a382-2e2a7f753c63 | -3.57407 | -54.67706 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58f1d22a-b794-31c6-b342-9ca81fc255dd | -6.99751 | -59.12537 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38ac67f6-fb73-3f13-8b85-dcb9b0f03cfa | -3.00343 | -53.90414 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf37fbc0-efcb-3636-aeb6-23798f27d113 | -5.3751 | -55.88327 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1409e6a6-3b23-3c13-a433-0eca15486bc5 | -3.29046 | -54.05516 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41bbb915-29aa-3a41-8112-98a282c157bd | -6.31402 | -43.34828 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7349b3eb-48a6-3082-8b4e-1e01999cf44e | -3.58922 | -54.67949 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 29a42e9d-9d3c-35a3-b036-fe278fee5f83 | -7.64213 | -44.37246 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 653c66ed-f264-3c90-8f9f-41d1e78c4201 | -2.88919 | -54.07858 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16776026-025b-3024-bfc3-88c35d1ca19b | -4.2139 | -56.05042 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81fde7ed-5684-3772-9b07-f1a3e5a5c399 | -2.7698 | -54.07426 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b8e2d00-2bea-33f8-a541-384ec38e0f25 | -3.978 | -56.21805 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ab9713e-fa3d-317d-bf29-29c30d2ccfc8 | -10.34245 | -47.75606 | 2026-10-08 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b76b6536-4b08-35f3-b382-37fb8f256207 | -6.32955 | -46.54121 | 2026-10-08 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9967ef95-94e7-32d9-b388-6807fe0ea986 | -3.28436 | -54.02332 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30573aed-e66c-361d-99c8-315d814771be | -3.54301 | -55.52318 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 289a5a45-0431-3276-8264-31d07fec3dab | -3.1651 | -54.73603 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dce61252-d9d0-34bf-a839-dc0857de78c7 | -6.99363 | -59.11926 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d68e969-6607-3998-90c8-b1cfa9f9778b | -3.28872 | -54.01961 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33467d98-7161-36b5-926f-0dced9aaf1cd | -3.04048 | -53.95381 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38eac5f4-3943-321b-9334-fa4517e3d052 | -3.12406 | -53.76117 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 887cf13a-f09e-3eb9-9bed-73a557a719da | -4.44937 | -54.97862 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb83a548-8bc1-340d-8735-667c53dc7dd5 | -8.07028 | -55.29272 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1886c6a-f022-3077-b8d2-5e174a023379 | -7.89876 | -54.71268 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4a5b4e5-8f62-32f5-9eec-934d93d61152 | -2.98423 | -54.14115 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a8143ce-30d8-3b03-8511-ec8fa15f6d2b | -5.83357 | -52.06194 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea9f358c-2614-3b4d-a6b3-9510efb719f4 | -3.55857 | -59.4735 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a8a5180-a5b1-3da3-850e-c211591b6b39 | -5.7293 | -45.15357 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c24c8a64-ebbc-36d0-b733-56a6512e7b45 | -3.29132 | -54.07307 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 273e29a0-337f-38b3-9c97-3e77f7191d8e | -3.30128 | -54.03481 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cca7d4c-ea74-3311-ad68-6fbde1d7ab85 | -2.87206 | -54.4766 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63472bb5-29b1-3805-8022-a47493d4e38d | -2.96286 | -54.15595 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e7347c2-f269-3997-b4e1-4ba58aa7cccb | -3.02888 | -54.09858 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a758c34-eca0-30c2-a5c9-6dff97bd4172 | -2.69732 | -56.53906 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 687ccd44-1653-3943-b7e2-23b594b6ff0c | -3.59024 | -54.57583 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7591d816-b837-32ca-9ca3-6de904c56e55 | -7.87549 | -54.99053 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6249f18b-7ac2-3b87-8a41-227a4a793faa | -2.4838 | -56.09023 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86148f9a-57d4-3fd8-bdf2-c073b4620b1e | -3.51572 | -54.65352 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea7f26e5-bfe8-3384-99c1-32ce78bb0f82 | -7.22218 | -44.15845 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34270d2e-39d5-354a-96e4-d184c9029214 | -4.77494 | -55.74007 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07e8be90-43d8-3305-ba6a-21ce5fb9b886 | -5.73747 | -53.46369 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d77b6149-e9a4-3db5-af66-2f473713e38b | -3.04675 | -57.48608 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb319402-ef33-390f-8a38-19dfad2d1380 | -3.07742 | -54.28566 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7f053c8-1be6-344e-ae78-a7b82431521d | -3.7255 | -54.22005 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a97b5731-b879-3ec0-924a-ff1f7643d9cf | -7.62071 | -45.28936 | 2026-10-08 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 787c7216-1547-33f4-bbb6-09a268c9ecdf | -3.01455 | -54.14133 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aea9ac6c-4ddd-3d8b-b001-2f83147e77e9 | -3.01225 | -54.1319 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58914cf5-ab2a-3434-835b-c0510dde4e75 | -3.77352 | -59.25502 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4feb4be0-eeb0-39cc-8b66-7ea56169bc5c | -7.87464 | -54.97285 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 999623e7-573a-317d-86fb-e043261bd49a | -2.76927 | -54.10128 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3032dd9f-e87b-3890-8cdf-23d918f0992f | -8.29053 | -50.26318 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| becc0dfc-04f4-31d4-90a8-8217be7ddc18 | -3.06352 | -54.20601 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80e5748e-6941-3ad7-ad08-3b915e5c2dd7 | -3.25661 | -54.0337 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9357fd64-7047-3f38-ae52-95c22a9b7741 | -3.01342 | -54.10067 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5a7df9e6-ce09-3a53-b554-de0f63b8baf6 | -3.14966 | -51.62095 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92a2d34-55c1-3185-9f22-0667203e2673 | -3.08328 | -54.27288 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64abb2d3-8241-36fd-9e10-861bbe1c8c92 | -2.84633 | -59.11604 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6404cc9b-5077-3a20-b9a4-fa2f0de77180 | -3.49985 | -59.27232 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 406dfcc4-b0d6-3733-a4dd-eb33a1d46620 | -3.06822 | -54.24779 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8baef8d3-bac0-3785-a8e2-6a803bb51cf1 | -3.30606 | -53.86206 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e524c0bf-8396-3252-b7d5-d99ba9b7d77d | -3.12175 | -54.17451 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8559a18d-052d-3489-8150-ba99eb0b8b27 | -3.65229 | -54.28207 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b5603a57-5073-3d05-879b-09a503205605 | -6.88144 | -43.69007 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a128aa45-3c92-3aa6-a2fe-0e0362d136f1 | -4.34961 | -43.79624 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 589f4844-0629-3953-a64c-90bc74af5e0e | -6.13502 | -47.93724 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cda2bbd-b495-3289-9e43-3521c4cd0d53 | -7.60037 | -42.37943 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57e5fde7-9c1c-338c-9133-62cc0848aaf9 | -5.67982 | -53.48997 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 480b180d-adb0-3f3b-a0d5-ee38e55753d5 | -3.28172 | -54.06266 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53d3e170-ea6b-3629-87f4-39317f04de39 | -3.58293 | -54.31199 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d55a517a-8f9c-348b-9f62-1fb06c40eccd | -2.94077 | -54.17504 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27cbc13d-2c5f-3e3a-8790-7c1df906f94e | -7.21521 | -55.17332 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3246b859-a990-3df6-a0fa-b70d90737359 | -11.06729 | -45.77417 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49d9b603-f85c-36e8-b3ba-a5f3b0563e81 | -4.66286 | -56.22011 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2207b192-bc04-3c26-bbfb-5b4d1ac1b917 | -3.29343 | -54.06007 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324fb5ff-1f05-3269-bd2c-60865d2f1492 | -3.14577 | -51.62395 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d947bffa-fad5-3c11-8c21-c8f73675e3c7 | -10.42087 | -47.27517 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 55c66f1e-23b9-31b7-9431-02fa4823eb6a | -5.39293 | -42.95987 | 2026-10-08 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a8b8695b-3bfb-3196-9126-eb84f4c324ff | -12.03732 | -43.44038 | 2026-10-08 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45164e63-3b2b-329a-920e-c436b79b32a1 | -3.51904 | -51.32851 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfdad672-cba0-3567-845c-ac21907e3e85 | -5.96529 | -40.91403 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72950da9-ecde-3d27-a44a-f0cda199b29d | -4.17418 | -56.34695 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README97.md)
