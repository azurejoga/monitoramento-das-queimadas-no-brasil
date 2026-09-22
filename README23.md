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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5fdc9e2-cffa-318b-9461-75d0aa14ce8d | -9.2573 | -46.1647 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 06f48c77-beb9-3a3c-959d-c1b0138e350a | -6.467 | -59.9902 | 2026-09-22 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d673cbe2-e984-3205-ba71-cf3019114d3e | -2.8608 | -57.7994 | 2026-09-22 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fe5a5141-f82c-378b-bd9c-27298ac7c0a4 | -7.5704 | -57.6766 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d13f9e07-6533-3b74-af95-d0d5edd636b9 | -10.6097 | -53.9697 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.9 |
| bcfb8011-80ed-3491-82c5-d4e764114af2 | -2.6852 | -54.9753 | 2026-09-22 01:50:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5306bef0-a8df-335f-8b61-5415055ad0eb | -5.7382 | -45.0853 | 2026-09-22 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f6347b34-0da8-35ab-a616-553b5ee799aa | -3.2211 | -53.9623 | 2026-09-22 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 275.7 |
| c0f8844a-7dc0-3598-9b23-85396da231e7 | -10.5906 | -53.9918 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d1d1b219-c03b-378e-839c-4a8c29ad88f1 | -12.574 | -45.9576 | 2026-09-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 6e64f540-d322-33a0-97ef-ad6260c3a6c7 | -11.7675 | -50.804 | 2026-09-22 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5f3066d9-cbaf-306d-b2d8-41784d00fd39 | -5.7569 | -45.084 | 2026-09-22 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 326.6 |
| ef7b49a4-48f0-3431-846e-4c07eb1328f7 | -9.2383 | -46.1668 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 847509e7-5c24-305d-b698-f093efc73f3a | -11.3257 | -54.0282 | 2026-09-22 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 1d3f18a6-5aaf-3663-b83a-e3c1eb58b8b4 | -18.7472 | -46.93 | 2026-09-22 01:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1b022fe1-a911-392e-aa2f-c89024d75f18 | -6.6148 | -59.908 | 2026-09-22 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| abea48d9-6cbd-3457-a4eb-8cbeba7b34d2 | -5.7567 | -45.1067 | 2026-09-22 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 4f1a7987-d701-3f43-b6b7-5663e46b9046 | -6.6516 | -59.9066 | 2026-09-22 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 086ab611-e996-3b41-a192-6e59471d6940 | -10.6092 | -54.0107 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e6803796-057f-3527-bcbe-2c653890823d | -6.0925 | -57.6847 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a2f79045-ae7a-31d7-a734-c0296365d05a | -6.0365 | -57.8235 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9bc254f1-2565-3829-94a4-7c67cbfd9c6e | -9.5594 | -66.0359 | 2026-09-22 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ccab066c-e028-306c-ac67-606c44193544 | -18.727 | -46.9345 | 2026-09-22 01:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8fed7134-a776-3bf5-9ae7-cbd58832f2f3 | -10.5908 | -53.9713 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ac9ee21d-1ca3-34d8-a495-7698129e1605 | -6.6515 | -59.9258 | 2026-09-22 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 2fa9e40f-a519-3dcd-9bb0-cf2d11e5763e | -2.6853 | -54.9554 | 2026-09-22 01:50:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5cc58997-b60a-3143-8ba0-52b70f15c4f1 | -6.0928 | -57.6262 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 548dd155-e112-3d9e-babb-f7c9d23fe93e | -11.7672 | -50.8253 | 2026-09-22 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| ecd7c8ec-c896-38e1-9eb7-83550975e65b | -12.5551 | -45.9376 | 2026-09-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8575ce76-3359-349f-971c-c65976039567 | -7.7144 | -61.2419 | 2026-09-22 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7d3dc172-27f2-3505-8ce2-5221f9f17837 | -11.8686 | -46.8304 | 2026-09-22 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| dc19bc34-6815-3a12-98e8-8b4f7ff5bc43 | -12.5744 | -45.9347 | 2026-09-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 76a8e25f-896f-3c79-8bda-ed98bd2712a8 | -6.6146 | -59.9272 | 2026-09-22 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8f81d571-c0e6-3f33-81bb-dc3a76b2cfd1 | -12.5547 | -45.9605 | 2026-09-22 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 2f738569-5bdd-3cae-a84d-b661d2570274 | -2.6669 | -54.9757 | 2026-09-22 01:50:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| a9acca1e-514a-3328-ab03-30d31a6dc96d | -6.1109 | -57.684 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c469c7d3-7de7-31d1-9559-cbb06abcf324 | -11.3255 | -54.0487 | 2026-09-22 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 83ee73bc-c31f-3b0c-8f78-d681fb0286b0 | -3.2212 | -53.9422 | 2026-09-22 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 489.6 |
| 78ea35e1-aa2a-3196-9b85-0846292edb8e | -10.6094 | -53.9902 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 322.6 |
| 35da5f39-4b0e-384a-a8c3-961a072f48cb | -9.2576 | -46.1422 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5b154660-6337-39ce-9d21-812c4cbb1c23 | -6.571 | -44.1516 | 2026-09-22 01:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 77e24cdc-b11a-38e5-9342-ef931297abdd | -10.6283 | -53.9885 | 2026-09-22 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 08681100-13b2-3e0a-9734-4190e94fa48a | -6.6331 | -59.9265 | 2026-09-22 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 227.3 |
| 09863628-e506-3c34-9bba-a4dd1e5a0071 | -6.6332 | -59.9073 | 2026-09-22 01:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 26138e1e-96b7-3d70-b4ce-58765d9c43fa | -3.2396 | -53.9417 | 2026-09-22 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 457.7 |
| 89773106-5e29-39f8-8626-06933d979fce | -9.2762 | -46.1627 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| fc1336a5-af60-3d5d-97b7-dd2b4547f5a6 | -8.7916 | -44.2778 | 2026-09-22 01:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 03145bca-54aa-3002-91ab-c9612bc12cfb | -9.257 | -46.1873 | 2026-09-22 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c60e3584-ea5b-3a39-b58e-8bd62f51bfd6 | -2.6669 | -54.9558 | 2026-09-22 01:50:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 35fa03c3-0181-32e3-b7ef-1d147c9f572a | -6.0549 | -57.8227 | 2026-09-22 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f0bd7853-e857-3151-b201-4e2f1a3982d0 | -9.2383 | -46.1668 | 2026-09-22 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 228.8 |
| 7b6d47e8-b019-3294-82a5-fe302c4eeed4 | -2.6669 | -54.9558 | 2026-09-22 02:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| ca547b60-4f8e-3f49-aca6-330db0b2831b | -5.7756 | -45.0826 | 2026-09-22 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 74ac3950-2363-3899-8c7f-1495b7b23d0a | -5.7567 | -45.1067 | 2026-09-22 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 94476d09-1459-363c-b234-bebfa36f016a | -18.7472 | -46.93 | 2026-09-22 02:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 59d4379c-f5dd-36ad-a3c6-fcddd5430a95 | -6.6516 | -59.9066 | 2026-09-22 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d2c31e9a-63ce-3724-9643-3f8665a08942 | -8.7916 | -44.2778 | 2026-09-22 02:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5f92288f-d964-3cb8-a64d-72e8b98838e7 | -6.0928 | -57.6262 | 2026-09-22 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| aa0dc3c8-7dee-3bc5-8f26-dc308c2ad241 | -3.2211 | -53.9623 | 2026-09-22 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 8ee5fa38-19ba-3b35-b199-8a34a351aeef | -3.2396 | -53.9417 | 2026-09-22 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 329.0 |
| ece497ac-08a1-3a10-abac-e3a5c2f48300 | -7.5889 | -57.6757 | 2026-09-22 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 75eb31a8-9bc1-3aa8-a53c-fed9d4f92276 | -3.2212 | -53.9422 | 2026-09-22 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 242.1 |
| f6e6b634-5461-3259-bc0d-c86fc9119131 | -9.2573 | -46.1647 | 2026-09-22 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d614d6a8-db59-3e95-9dc8-d48ff3c9acef | -11.4213 | -47.338 | 2026-09-22 02:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 66babd8f-9c07-31a4-8a56-d5108cbb67c1 | -5.7382 | -45.0853 | 2026-09-22 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bdd4221a-54c3-39ba-8a84-6bb1c50c0241 | -10.5906 | -53.9918 | 2026-09-22 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| aef71ee0-c17c-3f9b-b483-8f512dbcf64c | -6.0925 | -57.6847 | 2026-09-22 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 96f97085-d84e-35ff-a936-dff28db3c656 | -10.6097 | -53.9697 | 2026-09-22 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| e7f527e3-1703-3fec-80b9-98033741267e | -9.2386 | -46.1443 | 2026-09-22 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 68dbf8a5-7ea1-3692-97b4-a0e067317154 | -3.2395 | -53.9618 | 2026-09-22 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 225.9 |
| 607ee02b-43fd-3d4e-a307-2c61e0396837 | -9.2194 | -46.1689 | 2026-09-22 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 64510164-4984-3139-9e46-0c5d16a6c955 | -11.4404 | -47.3355 | 2026-09-22 02:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e2a7162c-a80b-3346-b900-3c0d644416b0 | -10.6094 | -53.9902 | 2026-09-22 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 289.4 |
| 042b13d8-86a6-3183-bc55-06478ee0af64 | -6.6146 | -59.9272 | 2026-09-22 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 0a7100a8-79ae-3b4e-b561-6f8a44d0097d | -2.6669 | -54.9757 | 2026-09-22 02:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 1ab799a0-5129-327b-be81-3be3be472e41 | -11.869 | -46.8079 | 2026-09-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 35f90e2e-b9ee-34cd-9aea-a7c16bc66638 | -11.8686 | -46.8304 | 2026-09-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f241d848-961b-358e-ac9e-5ca0d0a73300 | -6.6148 | -59.908 | 2026-09-22 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 34a4ddb4-767e-3cce-bd75-e430bf1022f1 | -6.6331 | -59.9265 | 2026-09-22 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 97b62fd0-1c6d-3b8e-8484-070b55d4b833 | -6.0549 | -57.8227 | 2026-09-22 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cbbffe15-3c00-336b-a65d-39fdb4745e3f | -12.1462 | -47.3751 | 2026-09-22 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 469d2b4a-61a4-3ce3-a518-5c2932518f5e | -7.5704 | -57.6766 | 2026-09-22 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5664143b-8294-38b6-a9fc-7394d7d7f061 | -6.6332 | -59.9073 | 2026-09-22 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7eff1f5f-c2b6-337c-8746-f5f01b375fba | -2.6852 | -54.9753 | 2026-09-22 02:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| dfd32252-35b3-3492-a5f2-6b938a0ae5da | -2.6853 | -54.9554 | 2026-09-22 02:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a94e1989-eb17-3899-b853-c326553ea0e8 | -12.1458 | -47.3974 | 2026-09-22 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1f57570a-cc71-30a3-889f-1f2f495b0407 | -6.6515 | -59.9258 | 2026-09-22 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 562883ed-f1fa-35e7-afb7-b107a1c2a0bd | -9.238 | -46.1894 | 2026-09-22 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ab864ad3-979c-3a6f-8f0e-6808010b1714 | -5.7569 | -45.084 | 2026-09-22 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 477dc797-60f8-3bb1-b968-caa085f82983 | -10.6283 | -53.9885 | 2026-09-22 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 5b91544b-0607-33b2-8372-cbf5e8aee9df | -11.3255 | -54.0487 | 2026-09-22 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| b051c098-5694-3f50-adf3-70a996aa7ea3 | -7.6621 | -69.9215 | 2026-09-22 02:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e29ef6cd-afff-37e4-9086-cc75c3c82d7c | -2.8608 | -57.7994 | 2026-09-22 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5c9042be-36f6-3afb-9321-5adbff1b6d0b | -10.5908 | -53.9713 | 2026-09-22 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a1910ab0-8fd7-3508-b342-dc651055524d | -12.5547 | -45.9605 | 2026-09-22 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 62ae0052-1d61-3d55-a51f-2e333d50b665 | -11.8499 | -46.8105 | 2026-09-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 62c6cb01-127b-3724-b26a-20197d0fb69d | -9.5594 | -66.0359 | 2026-09-22 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a6791972-51a6-37b1-8529-a2b288aed24b | -6.467 | -59.9902 | 2026-09-22 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c9ebcd30-0ab7-30c1-87b6-5fa1de2af447 | -10.6097 | -53.9697 | 2026-09-22 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| b65b3bb0-4787-3a5d-855f-80a68dbb7b91 | -2.8791 | -57.799 | 2026-09-22 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |


[Clique aqui para ver as próximas entradas](README24.md)
