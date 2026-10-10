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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24b052da-a647-3e98-904a-d33a753c522f | -6.12364 | -55.69294 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1a03aeb-03aa-3c91-b098-238026856ea0 | -4.09945 | -54.02079 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1c7a00a2-0087-399e-bf7d-59ad48704a53 | -6.35817 | -55.15418 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9282740-925e-3791-9b08-78515a383afb | -3.25627 | -54.02321 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b530c7f9-2630-3e24-bd95-7c1b342251b0 | -6.32148 | -55.33306 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7725fd1d-bd9b-36da-8bc1-df67056643b2 | -3.85081 | -55.7914 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6f7730f-2ef4-3756-bdec-0dd7e903a884 | -3.95406 | -55.33791 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90f89165-70a3-3b6e-b26a-65a1e7c35cd2 | -3.26788 | -54.69385 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 022ad19f-7252-3a1f-baf6-4a1c660dff55 | -3.19198 | -60.05611 | 2026-10-10 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbf74bf2-ff49-305a-8ae4-de0ffe5ab9c2 | -3.83898 | -55.78957 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e51e19c4-3b35-344a-ba77-d314a98877c8 | -1.11469 | -54.16465 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98645b39-6cde-3d7b-9fb6-fa2dc99c3eff | -3.2787 | -53.87002 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2f524586-c04b-3e3c-8a99-4219c6957d31 | -3.94388 | -56.05161 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b51c4b1-eb4b-3b0c-83f8-87ec3af8e5aa | -3.405 | -54.18734 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4267213-19d0-383f-ac05-9b80c2829825 | -1.88683 | -54.67503 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e1a14599-6733-33bc-a065-c1e1f140694e | -4.59646 | -55.72029 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73ec7e3f-cc88-33ac-b37b-6e2e2bff3fd9 | -5.95159 | -55.35095 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75dd0ae2-aac0-3c27-b022-93415bc136d1 | 0.30379 | -60.44304 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa793f1-81e3-3eb7-ac0b-64592e0885b7 | -2.7332 | -54.1476 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ebfdcbd-126e-3cfe-b671-7e471f4cbf46 | -3.53595 | -59.57676 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40bb1cbc-9b11-3858-b1b9-8614ce435424 | -5.71296 | -53.47857 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56f9398b-b6ba-3081-91e2-b1eb8360503e | -5.08587 | -60.21503 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16a579eb-c585-3fcd-bc97-c8ac83a392b3 | -3.98442 | -54.45221 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 224242b5-632d-38c1-a899-3658248e397d | -4.11207 | -54.01194 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10f09866-1d96-339d-a206-96a1e3416533 | -4.10496 | -56.12844 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 804f755c-be4c-3808-954f-84a023a171a7 | -5.79616 | -53.80571 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b6977284-6089-3684-8ef3-f65fb8d592e0 | -3.58204 | -54.70664 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b7ad7e5-2dc1-3b46-b450-8e9fc62c697c | -6.12287 | -55.69588 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ed3f7d9-c063-3b40-b39b-006022fd343d | -3.27619 | -53.87367 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e8afd9bc-a834-357c-8c6b-7f2503eb1de3 | -4.11445 | -54.01065 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc216278-01ee-3a67-af8d-2c9b8b111f87 | -3.59915 | -54.60666 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e0ac55d-4761-37a7-8843-5c8102ff24c5 | -2.92865 | -54.08317 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f03bbd7-e83f-3886-95bf-9772d4e92eb8 | -2.6091 | -56.48812 | 2026-10-10 05:48:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 550c379b-9bb3-3c37-8dce-4eea32c08cca | -3.64443 | -59.56944 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5592fa6d-d4c6-340a-b4b2-d5ee7e9e914f | -3.90065 | -55.89518 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c85c8155-eb81-361c-b938-56935c611a7d | -5.0846 | -60.22394 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53617669-ec92-3311-bfd2-3f50c4a47282 | -6.09012 | -53.50537 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6939d534-b643-32d4-89e3-9bfdbf64913f | -3.10633 | -53.78167 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f6038480-563e-3c6e-85fc-500fcec31272 | -3.2073 | -53.86372 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce8e7145-b45b-305c-bb6c-03bf94d39920 | -5.07183 | -60.21745 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a7dac84-9aa3-3f5c-a9eb-b5dad79e5c6b | -3.18823 | -60.05117 | 2026-10-10 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adea171b-0bc9-3f07-97d6-5ffc77889ceb | -4.82857 | -56.08647 | 2026-10-10 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e62160de-6b73-3933-b682-f0139be320bc | -3.5984 | -54.59422 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 331582f4-f9dc-3883-9a3c-08a66b64db30 | -6.12839 | -55.70159 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65b49212-836a-3512-9c7c-4afd79891f71 | -1.10985 | -54.15368 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2219ff79-89c1-3649-8b19-a31d24e9c84d | -3.28447 | -53.87679 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f43cc260-00f5-32da-99f2-ac21446894a9 | -5.18109 | -60.30453 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd68238a-d909-36ed-9dd2-08a03b596592 | -5.96 | -55.33639 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a1d2f57-74bd-3cd2-9eee-e4a7eb99a870 | -2.99443 | -53.91109 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a8d1eb9-7207-338c-a41a-268a277ed99d | -3.63915 | -59.57343 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f6a8cc-fd13-3337-b03d-f1cd6ae4ac92 | -5.97557 | -55.34427 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb216678-1032-3afd-87c0-41b544c57284 | -5.98609 | -55.36134 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a816689-781a-33ad-abcd-8af387befec1 | -1.32846 | -55.44846 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 058e75af-5288-3a42-b89b-1825b9bb7e3c | -3.56599 | -54.68362 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 636f3421-ab5e-3439-b2b5-d192b6cd7afc | -3.376 | -59.38551 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f400730-5b03-36c3-9e28-9106ead5de02 | -3.53902 | -54.73655 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b10455c6-9d6f-3205-812c-4d7c029f8e30 | 0.23929 | -60.3788 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 457c9091-6ca3-3d11-83d1-b6e31cafa4dd | -2.75161 | -54.1116 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 308d1665-cb92-3616-8069-50f53bb13145 | -3.28615 | -53.86533 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ca017dc5-d7b4-30f7-898a-f9a62c3e8bd8 | -3.20071 | -53.86249 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12f284a9-8f63-39bd-a4a6-811ea949a162 | -3.2775 | -54.6927 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5511d13-4b67-3b00-a4af-71ae05ce151a | -3.44232 | -59.56908 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fe63a89-e5e7-3161-8a02-2ff1bc3587f4 | -3.90854 | -58.95763 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a84a693d-1628-33db-9ebb-1a37b1ff2a15 | -4.59041 | -55.71969 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccb12d89-c8ec-3ef9-9177-e159e9481a33 | -4.34995 | -59.95167 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b83fe98-f7fa-30ca-aae0-3e1f790b838c | -2.22816 | -58.10702 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5791b280-25e1-354a-b7d6-c00de31f4fe1 | -6.43834 | -55.05276 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07aef4b9-49ad-37cd-b2da-fca34679a4fb | -6.4356 | -55.2723 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a50aa3-4031-3df4-8ef6-ff58eb7923ae | -3.58112 | -59.08193 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f251572-112c-328a-80c4-ae4fa18a43c4 | -3.60059 | -54.59628 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d771b10-6984-3231-8a60-d2ff39653d8c | -3.54391 | -54.74739 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1104b2b6-a02d-3303-b6fc-b099cc2d7029 | -3.26566 | -54.68564 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56893919-5795-3d49-a5fe-edd006e52fc2 | -3.24973 | -54.02206 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eae7be6a-063e-3e1e-bddc-5b11ab70d853 | -6.43904 | -55.04736 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b9be56c-796a-3d38-9d03-6512be5fbcfd | -1.28188 | -55.75175 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ded48c4-2fd4-3f29-828d-0077386fe766 | -8.65222 | -54.53966 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a09d1ab-c801-333f-b8f2-216b6e88dec1 | -6.04618 | -59.9248 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcffacf6-81f9-35df-a29a-a5a6bb199f86 | -7.50505 | -54.99608 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| adc2a0b1-7443-373f-a283-6b5cacf825ac | -8.62377 | -66.78412 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8c7ea8e-bb20-36eb-8aeb-e150cfc6d12e | -6.34011 | -60.03231 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cda72ddf-9b46-3d37-bc47-a8d98fcb5ed6 | -10.60268 | -60.48436 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1f6097a7-1c67-3a96-8931-cee90f064a17 | -6.07567 | -59.88456 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4711f9b-8650-380d-8d51-9ade83caafe7 | -7.91141 | -54.7184 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a29f1f1-456c-3570-b3b7-6185f10d2b71 | -7.60118 | -63.41456 | 2026-10-10 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d1fb5b-cb25-3389-88de-e7509278138c | -8.49723 | -54.60711 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4951b6b9-db8b-36e4-92b6-b67d7a7f83b4 | -10.55443 | -69.18719 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb3be41-8c70-3992-b1df-6bfaa9ab1ca5 | -6.94673 | -59.10575 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23fb4b0e-1ded-37d1-8d9e-ac79316753ab | -9.51483 | -54.6703 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb1badff-b5b6-3191-a616-71b9049cf8f9 | -6.4603 | -55.50402 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbd2dee5-e932-32f3-8d9c-bf9f09b4968c | -7.57547 | -61.54385 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f2e52ed-6713-3443-b990-f4bc05030458 | -7.47268 | -55.70594 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8f43fb0-8fbf-3834-bb87-185d04e0c92e | -6.48214 | -55.95713 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 314b1bdb-858f-3e88-9aa0-c808df825a3c | -7.23638 | -55.07973 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b78ac5d9-8451-31c8-89ec-3c42a09787a1 | -8.23145 | -61.18132 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ab5db3-e1ee-3cce-b1c9-9ae81aba6298 | -10.79963 | -68.34857 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47527d57-e582-33d7-9291-5391c30e021b | -6.62519 | -59.9452 | 2026-10-10 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff9cb546-db94-31f7-a91a-cf9f1ff223e1 | -10.59723 | -60.48885 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8f8fe94a-2136-361e-abb1-7a84560ba769 | -10.48903 | -68.97569 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bdf7685-17bd-352e-bf51-b6df9d5fcfc6 | -7.2265 | -59.64799 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efc30531-d7c6-3ad4-8e9a-8093120f18c7 | -7.09437 | -55.73538 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README145.md)
