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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8a1302f-0bc0-30e4-9766-471c981408ce | -2.77303 | -54.06852 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b13c90-ebc6-395a-bbae-32ca1023c457 | -11.75039 | -61.06138 | 2026-10-08 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e79f7243-e8c2-3fc9-abab-4cd2dd7660d5 | -6.95074 | -45.27616 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 54fe4c92-d263-3f3e-8aa8-103321f3e6c7 | -3.96632 | -55.83694 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc357e32-d7a0-3173-99eb-902a4f8a0b2f | -3.10003 | -54.28523 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 609273a7-14cf-30bb-894b-2ab9b540c5df | -1.28826 | -56.98129 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| faabfb40-2d26-34bb-8e9f-cf4d3eba9283 | -5.72895 | -45.14703 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eedc3f0d-3aef-381a-9f86-3aab76b7ee43 | -13.30102 | -48.67597 | 2026-10-08 05:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce2885a3-aa9e-3787-b620-d2fb5365ba36 | -2.9409 | -54.05693 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4be620c2-fe80-3f1c-991c-6012f1228cdc | -3.0416 | -54.26524 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 725f2109-333b-315f-9d62-7bc23e9f52af | -8.61727 | -67.02995 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 03c2d0c8-68b7-33f4-a0f5-46073dc51e3d | -2.98823 | -54.05614 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3ae2c0b-c238-3457-b601-3e74b077285b | -4.29903 | -50.78434 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2026593e-16de-3657-a9cd-e4e658f4cfca | -4.60617 | -55.72218 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a9d8910-2883-3e57-b71f-7743ab68d3b5 | -4.264 | -46.40035 | 2026-10-08 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595d52af-4b2c-3da7-9b4b-8e3d9ea041e5 | -2.49303 | -56.14817 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90ce9e58-4b86-3bbb-a51e-a5c4c32a48ad | -3.10292 | -54.28959 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7302356-82b6-3481-8c83-a32f364a53a7 | -3.1995 | -50.5577 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a9575e1-2ee2-3cde-bb01-ee8893287c2c | -2.98214 | -54.14227 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c31ea47-dd12-30b3-b420-1e168db510c2 | -9.11504 | -65.35766 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce0f0407-78ff-3591-80a4-b92f55656321 | -3.572 | -54.48766 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 018b700e-37b2-3259-b464-505430c1b157 | -3.01251 | -54.13127 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a0c1f4-863d-3379-8570-1c1c919fb7ff | -3.10411 | -54.28196 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b835f73c-5150-3332-8e8a-853e9d0a8a0f | -3.26498 | -54.03716 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bcde074-2ba8-3fb1-b686-ac39a8fa6192 | -3.61051 | -54.59367 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 91fba19f-d27b-35e5-8768-5d01bd223ef5 | -2.45675 | -54.80798 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e593a4-c329-36ee-94c0-c06fc42def87 | -1.20627 | -55.68723 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 236054d1-283d-3911-a45e-4bc25d08254e | -5.70361 | -53.48526 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4389ea0e-31e5-38a9-a960-2e5863c430fe | -3.14891 | -51.62687 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3964a0ba-1f41-32d7-be68-238d3ecb5994 | -2.96074 | -54.15878 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 840b022d-bf37-376c-8ebe-120a42a80789 | -3.50902 | -54.63978 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 743b5851-4e2a-3cbc-9647-ad79397171c9 | -2.78382 | -54.07325 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a47bd8e-3524-35e4-9fd1-2b6fb3c33353 | -6.30289 | -59.97053 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5012ea4-5988-32d3-89fd-83fdb1e7c70f | -3.20854 | -53.86781 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3382fba-c54b-36f5-a59e-00a2aa589253 | -4.07215 | -59.84933 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 409cb5e6-c40e-3da0-bc3f-e889cb739891 | -2.87819 | -54.88002 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3651dc3b-8ecc-3815-827b-4148cfccf0c9 | -3.0021 | -57.75327 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 172f61c8-2624-3810-9cd1-a3a7aba65039 | -3.28691 | -54.01245 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af2835bd-f378-3e9e-a990-f1282832ae72 | -1.10944 | -54.16857 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7a763d-e02c-362f-a11b-0763dea4546d | -3.52581 | -59.32605 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c019c5c2-c9ef-3e39-9987-77ab6d32df12 | -3.22625 | -54.30778 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bae9abfc-7797-3fc2-bce4-27ee3f7e94b7 | -2.3381 | -55.69419 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5fa532c7-fa24-35d5-bcb2-cf4ad68abece | -3.06993 | -54.2492 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 156a8adb-c79a-34b2-93c3-3d03f753f142 | -3.02335 | -54.06161 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 073d6cc3-5d2c-387d-81ec-344a73f6663b | -4.76521 | -55.72943 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5682489-9944-3871-bd5e-fb37298d2969 | -2.7809 | -56.50858 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e12860c-f272-3631-a4e1-2a118c51b4a7 | -2.55161 | -56.28817 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f42b53a-74ab-3f45-aba3-41c8ac407fcf | -4.12311 | -59.87885 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c4c48f7-f63f-39a8-ae72-7883e298b9c0 | -4.45158 | -47.92433 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c8ee993c-41f4-3c82-8e1d-833080003998 | -6.23562 | -52.86445 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2073cf56-e344-38ac-8552-312c12bbbf09 | -3.38963 | -59.59115 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88c99c0b-7713-3a46-be93-b582ae86251a | -2.87706 | -54.88731 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 279cf006-f534-30ee-b27f-ad2804507610 | -2.89643 | -59.20263 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f61a92-78d1-376d-bc17-0d5f3b5c01c6 | -2.99382 | -54.13624 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 740d122d-3353-358b-a5e3-ff05e278b22b | -3.00981 | -54.07936 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6abc8fec-fc3d-3de3-b6ef-282f4eaa730b | -2.97627 | -54.10601 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e5274cc-228a-322d-9202-5cbfe0b894a7 | -1.28761 | -54.56283 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5729a49d-77bd-3752-aacb-e85248e2d30a | -2.92583 | -60.9888 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c27da8f-d23e-3f0b-89b7-873d0dd91082 | -3.01462 | -54.04831 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf6bf6ab-f2e3-3ddc-983c-6ea29911f643 | -3.02554 | -54.0937 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e682bc7-d67b-34af-8843-943ab815394d | -3.64142 | -58.94384 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0afb845e-0d90-3899-b6d2-f4359c33359e | -5.99768 | -53.50138 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fd48c15-0fa5-3599-94af-e9d49cc7ca55 | -2.93739 | -54.05639 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34e73ed4-7693-31be-a17f-84eb4851323e | -3.5239 | -54.65743 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04f145b0-9f90-3601-8cfd-5a0c5350c274 | -2.48907 | -56.10858 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa100daf-54a6-3c94-955b-b03a61dc020e | -3.01211 | -54.08766 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 388191a9-a474-3380-8ee9-72da5bb6d384 | -3.09575 | -53.7128 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab1dead0-4ce0-3430-8c0b-e8650472f592 | -3.52045 | -54.6569 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27dc9c73-1fef-3feb-9415-06d436b2b7e1 | -3.09595 | -54.28851 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 412781ef-673a-3ef5-82d8-af15ec1b4039 | -3.28674 | -54.03651 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b36f9ff4-6a2e-3cfd-9069-fe1a7e426b2c | -1.10374 | -54.16011 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0edf64ab-147f-38e6-b190-1f4ee63e5414 | -4.14135 | -54.92522 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60ca12b0-59cb-3471-87af-55bdd49bfd9a | -2.57738 | -56.14705 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2721b39-da3f-3449-8679-2e659c05cda0 | -2.57723 | -57.78931 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a729a27b-0ee4-3cf8-9e8f-9c8a3f00b955 | -5.74202 | -45.14671 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a346432-4446-30c3-9993-df9486fc4071 | -3.70397 | -54.22539 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a15bfd7-7f36-39d4-8b97-fe4462f61036 | -3.27454 | -54.68797 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45686791-46d3-3c88-9cbb-2fa8b8de29bc | -3.19947 | -50.56437 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bce1497-71e6-3dda-9bc6-3c75e24ca56e | -9.48826 | -64.3589 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa88ff7e-252b-3542-80ca-c7a7da8adfd6 | -3.70684 | -61.32637 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8dc7605-3d8c-3ff4-a4cb-eeeb9af09a53 | -2.83897 | -54.13309 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c23730bd-a5ad-31e3-a603-be50aa122c49 | -3.23005 | -57.87674 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d610898-118c-3766-aede-5613c8e31fb0 | -5.70154 | -53.49896 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3710f1bb-6172-3abf-8d4a-5fa7111a51be | -3.36406 | -58.1977 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32359451-70de-3484-b7e0-c0430f835fd1 | -3.72344 | -54.21537 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59dca4fa-5c60-33be-8e8c-38e3a85b0fbf | -3.36464 | -58.19406 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c61eb82-7bd3-3798-bdc1-b8fb182dac2b | -3.26404 | -53.99687 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df87006-a4f7-3e2b-8fb5-42e6e5cc7a93 | -3.22021 | -53.88596 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e741ee-81df-30f2-90f1-c97c8adde27d | -5.25515 | -55.92128 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd075c30-a209-391a-a391-81758aabed09 | -2.79543 | -54.09086 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8fdd9d1-25c8-3379-9a22-055753ae8b68 | -5.6863 | -53.47365 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1c3870d-91cb-33ad-ad27-cbbd398bccf9 | -3.02143 | -54.09703 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5552b06e-ff15-3dfc-a7f5-57dbac867ee0 | -3.27066 | -54.07 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 954eaec8-41a6-37bb-a2b0-c2c2d6e2ff40 | -3.06094 | -54.23324 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c85fd62-548a-3160-82b7-0bef658804b9 | -2.86751 | -54.15998 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 55ce9107-fd79-3256-8868-1fdda31520e0 | -10.41818 | -60.64989 | 2026-10-08 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 045edf29-da38-34e6-b78b-bda0c6c14a03 | -3.3402 | -52.51455 | 2026-10-08 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b227ec3f-6d00-3579-884c-37bcee49b16b | -3.57028 | -59.49293 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b4fff25-6fdb-3681-bef8-88370e1c6d88 | -3.23806 | -46.95426 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22c4f988-b8c2-3013-8104-01c25c85e550 | -1.18462 | -55.6732 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README151.md)
