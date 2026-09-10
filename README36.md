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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57765a55-329e-3b54-9ec6-d85d6b80d387 | -6.79227 | -58.8946 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707b41cf-045d-332c-bcf9-71cac53632ba | -6.78385 | -58.90425 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9372bd6d-ceae-3668-82ab-5a6de6eefe8d | -6.77285 | -58.61166 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 661745d8-d9ff-3ec6-80ac-1a5ef890e0d2 | -6.0614 | -57.7911 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deb5dd63-657c-34f7-8309-aed549480dd3 | -7.74773 | -49.20128 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5eddb484-5fed-30ea-b3e5-5e54756b065a | -6.50954 | -58.38259 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09e7a7d2-8441-3abf-bd93-787313802cae | -7.24306 | -59.52354 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c2d990c-24ee-3c1f-b453-57a505a90c06 | -7.7508 | -49.20216 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 58eddaa2-2638-316b-a70f-f5791f8e7b1e | -6.18658 | -57.7547 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6111c80-019f-3f3d-a63a-7e74bbf2beca | -6.95951 | -59.75711 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70549cd6-e56e-34e8-862a-9f6ef5fe64f5 | -6.90303 | -62.98477 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a0f9f5a-27e2-3ba5-9776-bda95bfe3eac | -6.79505 | -58.8987 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a052be1e-2148-3f22-acf2-414651ce43d5 | -6.45668 | -60.02879 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdc9cc8f-a432-3421-80a1-7764cb978d0e | -7.56647 | -47.20698 | 2026-09-10 05:12:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c50cfd94-ae97-36b9-a243-8c9cc49bf6e2 | -7.75122 | -49.19909 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7ff10707-c173-3647-8f2c-6e286bd6a6b9 | -6.82171 | -58.99097 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cd05e493-f979-34e7-88b4-fbc9100da982 | -6.46309 | -62.86542 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38d343b3-8188-3ded-ada4-5f955d60c899 | -7.97873 | -43.98703 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e1fc774-4763-3f7c-9b8a-fd172dea3ad1 | -6.79448 | -58.90228 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82a05ec2-1892-3454-8294-1f62b243f44d | -6.78221 | -58.89301 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4dd94c0-257e-3c37-8dca-245d634a6023 | -6.77562 | -58.61572 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d2843c-2241-36fe-a9f8-7cc02876bacb | -6.76071 | -58.96289 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5ba9c62-6a2e-3d9b-a8f1-1a2602f1465e | -6.62604 | -58.37649 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c6d11f9-3812-3ec2-a906-d17710e8830e | -5.59158 | -60.24421 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d33acc6a-2290-34fb-93c5-39ab02dcba05 | -6.79715 | -58.95035 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a58551f-e2e6-3348-8054-0e7c869220f9 | -8.08845 | -54.84118 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b94293b-fcb2-3203-b653-4edcbfedfb6c | -6.7934 | -58.88746 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c263b3f-c085-3fe1-bd38-660c9439bcc4 | -8.81878 | -46.92525 | 2026-09-10 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8452165-96b8-364b-99b0-5b24bfb5b7ca | -7.75637 | -49.19979 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ec3679-a17b-3438-83aa-48d1932f89b2 | -6.96234 | -59.76141 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 377071ba-01fd-30ee-9edc-0265c8669413 | -6.78442 | -58.90067 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbf9907b-4fb0-3616-adf0-263e9d005d41 | -6.82228 | -58.98738 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca97d150-d9b5-3fae-b8b4-34a66b8a8f67 | -6.54716 | -58.51065 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| feb52d1c-dff6-3d8d-b213-5bc5dcc49dab | -6.78164 | -58.89657 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c237e5b-adac-3245-97c1-dbee0aa51408 | -6.7734 | -58.60815 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faefdadf-b657-3bea-8140-c72c1f8b81e3 | -6.76506 | -58.61769 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e7a6ea-6e03-3980-a0ec-6417781444f0 | -6.4309 | -62.86066 | 2026-09-10 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e63e5e27-c685-3a33-8aa0-3708a68eb7df | -6.64164 | -59.43993 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9b6187a-034e-33f4-a477-01c3ec6f7e27 | -6.81113 | -60.13114 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fedc34c3-7090-3e39-82d0-48dadebb2ba2 | -8.08662 | -54.85355 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d41d223a-fa2f-3686-9e60-8fa0033be762 | -6.55097 | -62.88845 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 81a00d5b-9438-375c-b285-d6ecbe2391d4 | -6.829 | -58.98843 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae2849f4-82c2-333a-834a-a22b83d3b954 | -6.79284 | -58.89103 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 336d1bb6-62c8-3c22-8438-306eacee4e72 | -6.55382 | -62.89642 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e9c8e5eb-81cd-3178-a180-247c223077aa | -6.55854 | -62.89345 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f846754-6761-3807-83b4-c00d39290845 | -6.46289 | -59.98981 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea75af57-5bd1-3968-ae7b-3c15a5d84237 | -6.5532 | -62.90009 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 449875c5-e091-36e9-8f75-1db9fd9d80db | -7.17174 | -59.55036 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3816852-fed9-348e-9fd4-bbb68b62c2bb | -6.78049 | -58.90372 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b388926e-9713-3dc0-9646-6dbc07a562e0 | -6.95607 | -59.75657 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 935cff44-9192-303c-b2f3-610632ee88b0 | -6.50567 | -58.38557 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b84e498-6da3-315d-b03c-3d09408ced93 | -6.95202 | -59.75976 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ddc580d-98cc-3660-9d90-66dc9dbeed6e | -6.89894 | -62.98408 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9b5cde-f19f-3849-92cb-c4cbf65ad14e | -6.76618 | -58.61062 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 576fefe5-a5b0-3404-8d3a-725dc9bf77e2 | -6.80325 | -58.97703 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 005e51ac-8a07-3c1c-85e9-b80545ab1214 | -6.77942 | -58.8889 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 428b787d-32cc-33d2-bd50-112319076052 | -6.80387 | -58.95143 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 38e40551-b304-3167-b0f2-29363a738846 | -6.77005 | -59.77837 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6bb5a78-9a83-3475-811f-e6fd10b127ec | -7.56043 | -61.37597 | 2026-09-10 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6174ed5f-10f4-376b-89a1-d5f8ad3b235b | -6.76784 | -58.62175 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c1d5d3e-490d-3071-956b-d190f57b61ae | -6.9589 | -59.76086 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45cb9dc4-c4dc-3ba8-b9c3-2e49f5371acb | -7.97684 | -43.97819 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdd8a698-42ac-351d-a0a3-843fc7d7aa68 | -6.82564 | -58.9879 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9da9a34e-c84a-371f-8096-307ff0c4b3c6 | -7.75288 | -49.20198 | 2026-09-10 05:12:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d7fd9421-a3f4-31e3-9ad4-2531ef60576c | -8.0896 | -54.85819 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f3f5bd2-a916-30ca-b079-7411e7c3a24d | -6.83322 | -55.29742 | 2026-09-10 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da37d667-8fc5-3a95-813c-b01f829334b1 | -6.65475 | -58.82189 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75be1162-f620-3042-8f8c-7cb7026897a3 | -8.32075 | -45.11087 | 2026-09-10 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 130dc1c1-f7a3-3296-912f-2de5042b7610 | -7.98227 | -43.99305 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1dbba638-ffb5-3169-955d-e6c859fa7f4e | -6.7917 | -58.89817 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 879efceb-4da5-355e-bd3c-e06c6f3c2bda | -6.7772 | -58.88125 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d72477a-ed8d-310e-8ffb-7d8e9409929b | -7.01899 | -59.7821 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b23e953-075c-338e-bb55-49b7e37b19f3 | -6.8658 | -56.57673 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a685201-fbb2-30c1-8002-153410166100 | -6.55916 | -62.8898 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 843781ef-2e5b-3f48-8ee6-9fae7b7aec79 | -6.55444 | -62.89277 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 32f6cfdc-4696-3ec9-a371-50db28571c6a | -6.54785 | -62.90676 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 731c200b-6fbe-395c-a1b2-a88536330d09 | -6.0997 | -59.97326 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6112734-1576-3d2f-b7c2-978d5d77e5da | -6.39075 | -55.20876 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9927a84b-580a-3d58-81ea-1fd06a629d38 | -6.87895 | -56.5135 | 2026-09-10 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17815d75-a9be-34be-b538-5e172b845c28 | -7.24365 | -59.51987 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b833463c-a273-36aa-a691-84722fa1035b | -6.82957 | -58.98485 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8098b75c-89e0-37c5-a145-4077fe9eb196 | -6.77007 | -58.60762 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8ac4bdc-5c4f-3736-923d-be17e05b0120 | -6.50622 | -58.38206 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a115cf7-7a5f-3919-8e4e-e67d8e1392df | -7.5757 | -45.6806 | 2026-09-10 05:12:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f5a3eaa-952f-3064-ba1b-ab5a581dfa82 | -6.79113 | -58.90173 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f4bd07-9ab0-3453-a1e9-94970f7f4aef | -6.63823 | -59.43937 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28b63748-ca7d-360d-a288-5a4893574eed | -6.54972 | -62.89576 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| abb6e025-ffcf-3c17-889e-6f7d38c89da3 | -6.09271 | -59.97214 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1ffed9b-7ecd-3f8f-99b9-0f74aa7a2b93 | -6.5491 | -62.89943 | 2026-09-10 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f2247cea-b30c-3ea4-bc6b-2042f9b909ee | -6.15568 | -59.9456 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d1f9994-9475-3400-9d20-b7802739c9b0 | -6.8328 | -55.76292 | 2026-09-10 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26068980-254c-30bc-801e-8b7770cd9847 | -6.51009 | -58.3791 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 365f5c98-9d21-30dc-a9a8-802513ddee1a | -6.50179 | -58.38854 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80e41591-7de1-301b-9a8f-a5157b7b5eea | -7.01554 | -59.78157 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 474e2023-3bba-363e-9c11-23db86d6b999 | -6.78499 | -58.8971 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3598777b-8fcf-344e-8ba0-5a0b5124001f | -6.77229 | -58.6152 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e08bb8d-f5c1-3056-ad4d-b740acda56c8 | -8.28835 | -54.90715 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3521a284-4e87-3285-a405-537f9482ceea | -6.39364 | -55.21312 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba531116-6c17-3809-bf88-bdc6efcf47c7 | -8.09081 | -54.85003 | 2026-09-10 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5d3f163-5d85-3b5e-8465-9ceae1a9adc1 | -6.62548 | -58.37998 | 2026-09-10 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README37.md)
