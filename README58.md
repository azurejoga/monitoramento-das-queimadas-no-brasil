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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af3e4720-32c2-3298-9b1e-979cb38d8365 | -6.16521 | -60.09303 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dc1dc35-f06b-348a-b0f0-3558edaaf0e1 | -6.47381 | -55.87693 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcdc8619-d6fd-342a-88a0-cf999a1b6cd9 | -6.5702 | -59.87217 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d881a9e2-c199-3088-bf13-7a167b08b4d4 | -5.80683 | -59.22537 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a442d5c3-36e1-353f-aa84-65c13e0f66b5 | -5.74127 | -57.60195 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4cf0e00-739b-398f-95ec-8073cb7e4570 | -6.578 | -59.88793 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e32152-789e-394f-b9b6-e67a7768bafb | -6.5797 | -59.87732 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| effc7458-586d-3efe-8e11-10844500b950 | -6.75671 | -56.85318 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c78c291-2471-36a8-825f-fe817872a712 | -5.61497 | -60.23236 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f7d159-b7fc-3a47-a5ee-af6bf88ab9ad | -7.64762 | -46.27977 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de4184a-3ef5-3533-aae4-82d53e1a1385 | -5.83247 | -52.06656 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 219b3e44-890b-3f93-997e-ce50c279a624 | -7.62869 | -45.2425 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c1421ae-90d2-39e1-98f3-4e23e0726fca | -5.80405 | -59.22135 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a81911f-ced5-3ce6-bd3c-a3fbc68d674a | -6.7943 | -44.99316 | 2025-08-23 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f23d9560-bc19-3b40-ab36-619ae8a9449d | -6.37854 | -45.54401 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dee6eba-497c-3e2f-8cbe-6ab11ae62edb | -6.57634 | -59.87678 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8965ed7f-4b95-362a-967e-ddc9ed788fdf | -6.47616 | -55.88555 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 999f4ca1-c456-309f-b051-dbdf82ed266d | -5.24001 | -60.30462 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a565c18c-7681-3fab-913f-0a08f5fca30e | -6.47678 | -55.8815 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f21f111-33fe-3043-977c-7921f19aabe0 | -6.57913 | -59.88085 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44c6dba5-231b-3311-b360-404e19622aa6 | -5.15049 | -62.51368 | 2025-08-23 05:18:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f72e07c-74e0-318e-8630-5c97c8f3e340 | -6.06718 | -53.88039 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82d128a4-2350-3744-9920-c1a5b772f09c | -3.78008 | -55.96107 | 2025-08-23 05:18:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b3e2a8-0758-39f5-b96f-41c6fb630b80 | -7.39858 | -48.1843 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cb96486-70e5-3872-93f5-249ad3176df7 | -5.75581 | -57.59696 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 723c201b-0d0d-3d75-8b07-ec555d2aeb11 | -5.74573 | -57.5954 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2cfa6539-9871-3497-8bd2-061f8265322a | -3.13737 | -58.04489 | 2025-08-23 05:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff24363-20f6-3b52-8182-72302e69ae0c | -6.7269 | -51.98226 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de924296-df67-38c1-9125-54979ab42dc3 | -6.45697 | -53.39553 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b7ab1c1-5e25-39e6-8354-2768ee4c2c92 | -6.11992 | -53.77498 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dea01a7-0778-38cb-8711-c32805973a8e | -6.0584 | -53.88443 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c9984b0-901a-3c4b-a769-72cc60e144d6 | -5.75636 | -57.59341 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f598f46f-6035-3939-8a27-30dea0cd18c9 | -6.27623 | -52.82792 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9870ffb8-42e1-3463-b618-5c735668554a | -5.74349 | -57.58776 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70aad21c-9216-3626-a1b2-f849d43ba04d | -6.65318 | -58.81819 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81024a2c-3277-36d5-8ff8-e6ebc92348c9 | -7.17293 | -48.42122 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1970dda1-9334-3037-8084-afabdbe15e94 | -6.44088 | -53.38931 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c33ba9a-d52a-367f-9ac3-7d8ed72add9b | -5.87804 | -57.76091 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 112637fd-bbca-304b-a3bc-57be64cecc08 | -5.74629 | -57.59185 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4283b863-ebbe-3960-bf63-875a0cd32ce7 | -6.65713 | -58.85793 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa4e22a1-fe1d-3ad2-b0eb-03e4d482c7ee | -7.43243 | -45.41672 | 2025-08-23 05:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 063c75ff-a063-3a5d-973e-d303b7e3fd34 | -6.162 | -53.7699 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8af1f0-94e0-31a3-808b-67cef273251e | -6.31358 | -59.88566 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f48613fa-a2d3-31e1-8fe8-991ae00d65d0 | -6.28006 | -52.82186 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f705c63-462e-3b9f-8238-b80b416bb266 | -5.88248 | -57.75442 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4cebb8f-cbef-365e-afdf-2fc4dbc42040 | -5.74909 | -57.59592 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cc420ab2-0768-311c-83fa-642e0cf32256 | -6.72733 | -51.97618 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5d6e276-d0f6-3e51-b5e9-4cd24ee36827 | -6.62827 | -58.54387 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62111ed6-4fd6-3502-ae58-9b7014a84ffc | -5.83571 | -52.07584 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73b67811-7c2b-3481-894b-7e51b7149da9 | -7.04808 | -51.41811 | 2025-08-23 05:18:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 835deb46-411c-30aa-8b93-9792c0d83814 | -5.74854 | -57.59946 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c8c377fb-54e7-38f2-93f8-0a29660307de | -6.62142 | -60.01505 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96e61977-e973-30af-9712-a17c07a4f627 | -7.63129 | -45.24442 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1436c635-fc44-3f99-92f6-6bc8fd355401 | -6.56422 | -60.06099 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b93e70f7-748c-39fc-9b73-f088f15fa693 | -6.45641 | -53.39932 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4625184-fecf-3164-8809-ec83db32ac7e | -6.37046 | -45.55671 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d74a4f67-2026-3127-879a-4e6d60be2f80 | -4.95233 | -55.78924 | 2025-08-23 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5763c3e6-ad3d-37fa-8c33-62ee90e3f11e | -6.57355 | -59.87271 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 424fc95e-3aa7-34f9-9231-fea7af269400 | -5.61216 | -60.22818 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0631d4f-989f-3fe7-9ed3-5fb76a3571d1 | -5.82726 | -52.07066 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa5ae2a4-497d-38e6-96fe-6011c8dcd327 | -6.0624 | -53.88503 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd681b46-b741-3d7f-b37c-0d6f65944788 | -6.25488 | -53.67473 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf747e3-13d7-3d90-83db-082499540ea2 | -5.75356 | -57.58935 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 05f68cde-e3cb-3b31-b867-40fa636607db | -5.83183 | -52.07088 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8320b04f-4fa2-33c1-94ae-ea05d738929d | -5.75189 | -57.59998 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 012cb9e3-0e6d-3574-b19c-e5ee8b1c3ac5 | -6.47526 | -55.87564 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5cc9977-a7e0-3d18-889d-3c014362460d | -6.37073 | -45.5495 | 2025-08-23 05:18:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b70f5e65-536e-3b37-8ab4-6a9c4d190e70 | -5.43793 | -60.15947 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c116140-0207-3b97-9b1d-6b8c8aa13d85 | -7.04881 | -51.41284 | 2025-08-23 05:18:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48281fb6-7fa9-3e50-85ff-643b0064ba69 | -5.8035 | -59.22484 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141e3b66-ed88-33ad-b674-ad033f88493d | -6.46058 | -53.3999 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f9f5cee-4789-3c52-acad-e8fc2a37514d | -6.64986 | -58.81766 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd31a47-4dd9-30ae-b84a-b58b33f3d3ca | -4.38002 | -55.75929 | 2025-08-23 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb7eac2-5149-32e5-85a9-2cdacf3abfee | -7.61416 | -46.26269 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d07e5f3-6782-332f-9bfc-0aade0e40b9c | -6.57691 | -59.87325 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b6e4799-3c3e-3d7f-8920-f7572676c64e | -6.06317 | -53.8798 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fa5d989-f50a-3fd3-b6f1-964d56ace29f | -6.62904 | -58.40849 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9716147-7e23-3dfe-b6ac-59699748f2c7 | -6.25433 | -53.67832 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dad88174-d935-3985-b94b-9733d383c15e | -5.80295 | -59.22834 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30451ac2-138a-327a-bd2d-c1457f3c79a8 | -5.74293 | -57.59132 | 2025-08-23 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a6eeb259-5843-3a15-a586-9b6bf19ceb85 | -5.89257 | -53.63322 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbfb7575-8fa2-3937-a124-8c8c801c78f8 | -7.64011 | -46.28464 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8664dff-e61a-3686-bbbc-1b2d8155fdea | -5.80738 | -59.22189 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e6cada-cbcc-3935-b694-3a3bd1f300ea | -4.10249 | -60.66018 | 2025-08-23 05:18:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8be22c56-edc0-3c7d-80f2-b76d79fffcb0 | -4.23344 | -54.92263 | 2025-08-23 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 901117c7-60f0-326c-a1b2-0c9283fd3328 | -6.26988 | -53.71301 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ad6a691-2d5d-39ea-9e84-ab6364cac662 | -5.79961 | -59.22781 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 170eafce-01db-3fb4-b32a-f2357148d1ab | -5.83639 | -52.07125 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a640126c-471b-3b1f-ab64-6506f0134d4b | -6.62881 | -58.5404 | 2025-08-23 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd5eced3-4b6b-3c4c-a3eb-49263dc4b65b | -6.27944 | -52.826 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6b42cff-3c4e-3139-8cc3-ab9f5ba63825 | -7.63673 | -45.23691 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 054788d3-a1c3-3652-ba75-da650e97d8cf | -7.63299 | -45.23076 | 2025-08-23 05:18:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfd6afee-219e-376c-80ea-a518349d6070 | -6.56479 | -60.05742 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3f9cc88-595d-34a2-a09e-fe2f1f55018b | -5.439 | -60.17458 | 2025-08-23 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7ff8f1c-9766-3d77-a977-87aaa9f7f0e0 | -7.65445 | -46.28025 | 2025-08-23 05:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e491b632-2edc-3257-97bb-dfcd4233bde1 | -6.72816 | -51.97367 | 2025-08-23 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d566a967-9a8b-36a9-a846-ea4799b39247 | -6.57299 | -59.87624 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00c9ed4a-7eca-3683-8372-6f37563ece0f | -6.00836 | -53.31786 | 2025-08-23 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d86901b-8f8f-388d-9c3e-98f02e118a6e | -5.81182 | -59.21544 | 2025-08-23 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ad9972-7334-3bc9-8e85-aa09d7b631c6 | -7.39317 | -48.17901 | 2025-08-23 05:18:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README59.md)
