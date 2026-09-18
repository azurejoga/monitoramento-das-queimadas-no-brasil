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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e666349e-3088-3238-abe3-ba2c54878ed3 | -2.89757 | -54.16753 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd7e249d-4335-31b1-90a9-ba602d1e611c | -3.04664 | -51.37302 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4df9ee-a2fb-3e3f-aa2a-1930898d6bdb | -2.60944 | -54.76131 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 03171195-fc72-3076-9e06-9c682d88e4a4 | -0.59864 | -48.48468 | 2026-09-18 04:55:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89da04b4-8ade-3831-ab40-d344023c989e | -5.1404 | -47.60285 | 2026-09-18 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c409c193-aacf-35a9-a19a-6819663a3614 | 1.24806 | -50.7772 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ce5bd35-3ae7-3648-a104-fcda9a460b81 | -2.49162 | -49.41323 | 2026-09-18 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3e80f1-b693-302c-a09d-76cb11b080c3 | -3.04272 | -51.37603 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31366121-14b8-303c-bb94-4050dc312845 | -3.0282 | -51.33749 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 558c6d89-4144-31ac-8c86-af3bc8b81237 | -2.90061 | -54.17271 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86f16520-3280-35c7-b313-1ad166dd6619 | -4.37227 | -55.42321 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deafa356-4528-3df3-b757-88418d997ac0 | -2.89129 | -56.93504 | 2026-09-18 04:55:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6a780d3-f7a5-3298-b6d8-6534018602ac | -3.36858 | -50.45297 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f42d6db0-f6d8-3a8b-b529-5d50709b30b6 | -3.7039 | -54.17451 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851e9989-3f25-3316-a423-1f62cc894e41 | -3.37355 | -50.44313 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| edceb669-70d5-3249-bf29-dd9f1c1f6f97 | -4.56582 | -54.91576 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2ed911a-f137-3832-97c9-d4c15742319c | -1.22711 | -54.1224 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e350a14-6cde-3ecc-b7f3-053d3534fc50 | -4.08527 | -49.49252 | 2026-09-18 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c831b335-78e6-3394-b13a-878f3c0ec3a0 | -3.92157 | -55.7579 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4ba2224-3e3d-3c07-b908-660dddde139f | -4.4339 | -55.0805 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91c72eac-5600-3513-bbd8-a23574aa8ce2 | -2.63302 | -51.7109 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a5aefe-bd92-33df-90dd-e7fb8017d5d3 | -3.29971 | -57.8764 | 2026-09-18 04:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e9c81a2-8bf6-30aa-ac04-c309a62fcc92 | -2.96421 | -50.33597 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3970a5af-9230-33b5-9806-d0833217b7a8 | -3.37577 | -50.45056 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fd7e11f-de04-3399-9219-66333d2339c6 | -4.38557 | -55.03581 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7cc3414-601b-3544-a17f-9bcf034d0986 | -3.70404 | -54.17135 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a962d6c-e9b4-3b22-a22f-fad1389914cb | -2.95866 | -50.32802 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3cd15a5-e00e-3da9-9480-6a5aa4250b35 | -3.36635 | -50.44554 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73181dc4-00d5-3dff-9b73-cb08433633b9 | -5.73479 | -43.28127 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c98abcb-396d-3e40-9d50-544ce83c43b3 | -3.03879 | -51.37904 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98f304ba-b9e7-3d29-8aba-fa28552f984a | 1.20173 | -50.76966 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21579a3-f2de-364a-9797-087e682c8563 | -3.44171 | -58.19809 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a02292c-d952-3121-a741-5925181b179a | -3.35806 | -50.45486 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e01e81ff-f516-3614-ad05-226a7882b7bd | -2.83044 | -50.47355 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ed48ce-4287-30e6-937e-979576e51f71 | -3.44391 | -58.21523 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecb80800-0226-3d61-a1e0-0606eae6bf51 | -2.82324 | -50.47596 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 67f25b6d-3306-3e72-8b19-6d9aec955284 | -3.24846 | -54.30933 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08086f5-d28f-30a7-92ce-1c1defb5421d | -2.74853 | -57.62728 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 839c2fef-f36f-3031-b1d1-3e6ff9a8f84d | -3.37687 | -50.44365 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5305d4b2-5209-3425-9b56-7844e3c2a0b1 | -3.46958 | -54.71185 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea3b7e48-ea7b-3995-a33e-3662475c29c0 | -2.96531 | -50.32906 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccd85e7e-e494-36ae-92ff-48d83f079d79 | -3.21138 | -53.9503 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63bd993b-af1b-340c-8357-4a0b9bac6187 | -2.74768 | -57.63237 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c046ab89-7106-3106-b554-be2bb3bf8b83 | -2.81769 | -50.46801 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| d8d011ab-a1c3-37eb-b32d-bdba851d4c42 | -4.59183 | -42.95461 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fc7f559-b62c-32d6-bb10-7a45437c2a3c | -2.82047 | -50.47198 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| d8ff6966-fe71-3c66-9bf7-725abe457134 | -3.378 | -50.45799 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 319d7129-15fa-3734-92f8-8bcc599617b4 | -4.48379 | -54.97306 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e9b5005-d24c-3292-a4fc-9c3d0d518780 | -1.78431 | -47.83744 | 2026-09-18 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4a18337e-9cbb-3794-9daa-fd9a914653b7 | -3.44328 | -50.6629 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc65c163-e26f-387f-8b78-b9a32be996eb | -1.49633 | -54.97278 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fd87744-393c-3f48-b315-209ef0200aef | 1.28448 | -50.87169 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0277ee-dc60-3127-8389-9cdfddf0d683 | -3.44882 | -58.21604 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bff5e2af-2f11-319f-a653-7cd44ffcb279 | -3.68746 | -52.38671 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c45c216b-1d84-3ff3-bc84-a5feb38de2cb | -5.73133 | -43.27949 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b33d1e54-5bba-377d-abb8-23a96f7ef37b | -2.81882 | -50.48235 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99b1720a-9aaa-31bd-9144-b7f480c5107e | -2.83201 | -48.65163 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 13e1dd8a-fdb7-3150-b97f-03cf5de7a73f | -1.49172 | -54.97561 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d5881af-e366-3854-ae00-b5c49547b11f | -5.75377 | -45.09361 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1239745-4d23-32bb-aa79-a8f1026d748f | -4.56425 | -42.93974 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 698fae26-4bfa-3858-860d-069ba62eef2e | -2.95253 | -50.3023 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ff23da-7876-327d-ba2d-defae4a393b2 | -2.5495 | -48.16005 | 2026-09-18 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 732a10f5-bc8d-3c20-a74c-4a2ae0a36e5b | -2.87031 | -49.62597 | 2026-09-18 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8dd9ed-b9b0-3a66-8ddf-d68d988edd70 | -4.50785 | -54.97219 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b684fa66-626c-3962-b0bd-f4339ea60736 | -3.26289 | -54.26925 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 34be69dd-7daa-3997-8b2d-b95a9d45da12 | -4.5683 | -54.91813 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 593b829b-87c6-3f59-ba73-85aa6ba86b2b | -4.55186 | -54.92796 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f931421f-9dad-3008-aae6-499c321945cc | -3.44606 | -50.66688 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d23ac0b2-a212-34a4-acda-c587b7ba1139 | -3.48739 | -54.72476 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b350b5c8-4e76-33a7-a47c-9ed88a5c22de | -5.73616 | -43.2802 | 2026-09-18 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa5b64a-84ae-371f-b6c3-33472a68f64a | -4.36917 | -55.41721 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06238940-5022-332b-b744-5e757472e4b2 | -3.31797 | -57.849 | 2026-09-18 04:55:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa3f91ba-c9be-35cf-aa15-5535b7b0d651 | -4.55135 | -42.95969 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3a5f9ff-5e5f-3c2d-9b88-e256f4f89640 | -5.63675 | -44.80022 | 2026-09-18 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cff8bc5d-f7c5-36a9-a0cd-6cbdf40032a7 | -3.37742 | -50.4402 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d19938f2-fafa-3b98-8890-40f05b1f425d | 2.09359 | -50.86691 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0508c5d0-fd84-3c88-b90f-a07e279bee63 | -3.104 | -48.69613 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba38d796-ae9a-3386-8374-b6d8f8ee05b0 | -3.25951 | -54.27126 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8bf2da61-413a-3136-8bf4-650ad4158169 | -3.36416 | -50.45935 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 195a3e20-2630-3485-a3ef-dea650aebc19 | -2.8946 | -54.18582 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12642cb8-0a9d-3691-958a-28a6b170fe87 | -2.81937 | -50.47889 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 50593de7-8331-3d87-ad2d-9b9309222420 | -2.90218 | -54.18703 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 144b4431-d1c2-3abf-a7d4-fdc1fa00e28c | 1.3334 | -50.60981 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58de4b42-53bd-343c-8230-e99d29a188b2 | -5.42983 | -43.43846 | 2026-09-18 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4de56e1b-c8f6-3044-9e13-92c836993264 | -3.57437 | -43.46862 | 2026-09-18 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c98f866d-3f26-3faf-9d72-eb5c1733e5eb | -5.77895 | -47.29087 | 2026-09-18 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4e9f2db-32e8-3ce3-b693-293cd14d7853 | -4.56833 | -42.94569 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 899e57c9-8359-3c2f-9d3d-82afcd57c53b | 1.96147 | -50.93639 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40579730-0845-3eb9-82fb-f0d77944cc86 | -5.22782 | -49.30616 | 2026-09-18 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66f7d416-93ce-33b7-967d-81eecec0ff0a | -2.89581 | -56.93582 | 2026-09-18 04:55:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d242924-c4e0-3237-bd46-a1108ecf61d4 | -4.01292 | -49.95118 | 2026-09-18 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b56ef339-ac4e-3a23-91f5-a8aae54d584c | -3.2151 | -53.95093 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcdcc842-1cac-3f7d-adbe-c0480e3abf0c | -4.51015 | -54.9825 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eadc2bb8-f969-3b04-888d-ea40a9b599b8 | -2.96699 | -50.33994 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55d7756-74fd-3d68-90d5-ee45d66ddbfc | -2.82767 | -50.46957 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d5cea64d-0720-329e-b500-accccdf47463 | -4.4896 | -55.49169 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7f39e8b-8fe1-3905-9459-164ecd6378ce | -3.43901 | -58.21441 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 735c0a77-3738-334a-9ff0-627b1c1ed6a5 | -1.8357 | -54.92725 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c5329c1-e862-3047-993c-82e05e6b012a | -3.26403 | -54.26725 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58ee1150-2bc0-3212-a55a-2f9980e32155 | -3.036 | -51.37497 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README56.md)
