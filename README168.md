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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f597ca02-e86c-3f39-abfa-5c8a4130f75e | -9.1076 | -67.703 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d06c9f90-4733-32dc-93d4-1e41a86a39dd | -5.1305 | -43.9844 | 2026-10-05 19:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7a08b7d6-31c8-35df-8c42-a8a912cec9f8 | -7.4889 | -42.8059 | 2026-10-05 19:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 82f1ca91-4299-32c3-8809-36fe5d3e4cda | -5.9417 | -41.3524 | 2026-10-05 19:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| c37ff539-db36-34c7-bfd6-379de1aa37c1 | -9.0892 | -67.685 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 77750d94-789e-32e3-8f01-01eefbd7284a | -9.7672 | -65.3182 | 2026-10-05 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1896c63b-8935-3afe-b688-c67dbacea8ca | 3.5071 | -51.4649 | 2026-10-05 19:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 561c050f-0775-3c8d-af9a-fa093d100986 | -9.1429 | -68.2202 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 41e8a8d2-f411-3126-8658-f52f39c7315e | -9.1613 | -68.2383 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 574796f8-af0f-3037-a4ca-6ac44e083235 | -8.8519 | -66.8012 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| a3a356a4-85ea-3389-a696-8c943f85895b | -5.8321 | -45.0332 | 2026-10-05 19:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c0360e24-2852-32b9-a6e7-685961630d9c | -9.1428 | -68.2387 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7ae5f717-b285-3696-9e6e-5b3788e158be | -6.8952 | -43.6833 | 2026-10-05 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 9024ad93-0cc8-33c6-b5bd-3a8d2c1e039d | -6.9328 | -43.6799 | 2026-10-05 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d90a9495-cc72-355d-aee5-884a3548a865 | -9.1072 | -67.8141 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 9c69acdc-c0d2-347f-a8a7-7749760642f1 | -9.1243 | -68.2206 | 2026-10-05 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| a6a53542-71b0-3e6d-89bd-d0563a30a788 | -5.8323 | -45.0105 | 2026-10-05 19:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 5803039d-9f4b-3356-bd2b-619bc08ab60a | -6.8408 | -41.7994 | 2026-10-05 19:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 2879749c-bd14-34c0-b43d-570c87f65da9 | -6.4279 | -43.4686 | 2026-10-05 19:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8d4a5e37-0aab-3239-9d7e-e13f1e2fcb1e | -2.5535 | -65.8634 | 2026-10-05 19:40:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| edd0c062-27bf-3fb9-a315-da08857ce5c1 | -4.5091 | -42.0584 | 2026-10-05 19:40:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| b11394ad-1c01-38d9-9b3c-9cd5cb955ac2 | -9.9176 | -65.0126 | 2026-10-05 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 20707116-c5aa-3a8b-a11e-bf4d9b963f7c | -8.5929 | -66.8266 | 2026-10-05 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 99363639-4daa-31e8-b1fa-acda68293c58 | -9.9175 | -65.0313 | 2026-10-05 19:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| af4f0c8d-6fec-358a-a5b4-2d3b3a80d1ba | -6.8764 | -43.685 | 2026-10-05 19:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| b5dec540-dc9f-3a87-a009-30d204e8c4f6 | -9.1075 | -67.7401 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2f697ecc-2f91-3c39-9626-1ed6b857f1b0 | -2.5353 | -65.8635 | 2026-10-05 19:50:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3d803083-13f4-3941-a4c7-8ea97d5adfe8 | -5.8323 | -45.0105 | 2026-10-05 19:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 49f37a5b-6551-337a-83b7-8e752a023f61 | -9.006 | -65.4 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| aa3c3087-2c8b-3016-aa1e-92af420b4634 | -13.5007 | -61.1333 | 2026-10-05 19:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 08e07d34-717e-33bd-b3d3-64d576acdf51 | -13.5197 | -61.1319 | 2026-10-05 19:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 2c94e16e-5025-3574-bd70-4baaf143d39e | -8.5929 | -66.8266 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| c9dc29ce-ed6f-32a2-ada8-ab87be93b81e | -5.9603 | -41.3749 | 2026-10-05 19:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 72287d19-13a9-322b-896b-64a5007d11d4 | -9.7313 | -65.0757 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 82bdce99-65f2-3cba-b0f3-9257c70dbb63 | -5.9791 | -41.3733 | 2026-10-05 19:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 5d480355-98eb-3e2d-8e9f-b27eee8daea4 | -6.914 | -43.6816 | 2026-10-05 19:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 136d1dd5-b403-3ecd-887e-8639a3edd4cd | -8.5183 | -67.0139 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| dfe02ef7-0125-3ab7-ab04-7e5eea80945e | -9.1055 | -68.3135 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 93ff0e1e-8987-3fe4-8676-3f908c6dbcb0 | -9.1257 | -67.8137 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| da2e3440-6db5-315c-938c-f37460050f69 | -9.1334 | -65.9 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4e412e5d-8bed-3744-9dc5-ab9faf93e6d7 | -6.8952 | -43.6833 | 2026-10-05 19:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 973e067c-a5f8-38f8-abd6-d0c93f39eea9 | -9.7312 | -65.0944 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 165.2 |
| c107fa8a-f91c-3dcd-b7d9-b2ac907ab021 | -9.1072 | -67.8141 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4825c166-e6df-3880-ab07-74a2b1457781 | -9.4435 | -67.1008 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ff358518-b369-3bf7-9e3c-249de5288fca | -6.7199 | -44.2771 | 2026-10-05 19:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| d9875e5e-c12f-3b59-ba0c-139c0308b35d | -9.6672 | -66.834 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| b21cd1bd-1a5f-34c1-bc11-d4934e7ec874 | -9.7498 | -65.0938 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b5157fdd-235f-3114-a20d-a4582d9b8a66 | -2.5353 | -65.8819 | 2026-10-05 19:50:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 21aeabab-caf1-321f-8f86-bdead22d71aa | -9.0892 | -67.685 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0f56e110-4972-3db0-8d96-ee40dbe7774c | -5.1303 | -44.0074 | 2026-10-05 19:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f465a8be-8648-3f69-89f0-2d2741c1b216 | -9.5425 | -65.6815 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3249a4f4-23ae-3477-9551-35bd04c8c5ef | -6.8597 | -41.7975 | 2026-10-05 19:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 0890b049-faeb-3445-9637-8afde9acc73b | -8.537 | -66.9764 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| d8c57fd1-8214-3db9-bbdb-ad6d32a090e3 | -9.9604 | -43.4574 | 2026-10-05 19:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6d00af00-5859-35a4-ab71-1749d0fa61a9 | -6.8764 | -43.685 | 2026-10-05 19:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 1845a29f-6f36-3f58-afab-de495cf4e091 | -9.3259 | -68.8811 | 2026-10-05 19:50:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f89e5285-f3bd-3f5f-acdc-eb83a398a899 | -7.4889 | -42.8059 | 2026-10-05 19:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| fb1189fe-d4c9-394d-b6f2-39e0ac57f5a2 | -5.0463 | -45.1995 | 2026-10-05 19:50:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e4295cd9-5aaf-35ea-9534-52638bb573f9 | -5.8509 | -45.0318 | 2026-10-05 19:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 90c1e5db-cd1c-3b07-b262-4eddbc869832 | -5.8511 | -45.0091 | 2026-10-05 19:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| e282b465-64f8-32b3-94eb-0ce235ae4fa7 | -8.593 | -66.8081 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 176.3 |
| fdaf0111-b714-307a-8bb1-63f0d737c076 | -6.9328 | -43.6799 | 2026-10-05 19:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 0ad19d61-5b60-38b6-b4e9-292d5ddfcba8 | -9.9176 | -65.0126 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 74d518ad-2e4c-3937-9053-8b4ac8e4b8ce | -9.1076 | -67.7215 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0745a3da-2d03-3b59-bb81-a2075a9984c2 | -8.852 | -66.7827 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 391abea5-f46e-3d1e-aa27-9adb88662b30 | -9.3494 | -67.4374 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fac7e3d9-bbe8-394a-a1f8-ca911bbb6f69 | 3.5071 | -51.4649 | 2026-10-05 19:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c3720270-de3c-369c-8af6-947b579ba354 | -6.7387 | -44.2755 | 2026-10-05 19:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ba40622f-80a3-3507-8e37-2bc30efd2d30 | -5.9606 | -41.3507 | 2026-10-05 19:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| f57d3f53-1aab-32c4-b8a3-64f6f5e9d156 | -9.0429 | -65.4361 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| fd65e56a-c5f9-3a90-ad9c-c3f467298bf9 | -9.1257 | -67.8322 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 991c9866-1e38-3282-a8a6-dff9991e59e6 | -9.1076 | -67.703 | 2026-10-05 19:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 0f4aa21f-f511-3f70-b703-942fdb091d43 | -2.5535 | -65.8634 | 2026-10-05 19:50:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9f0f2f8d-98f0-312d-995a-92bcd6cceb74 | -5.1305 | -43.9844 | 2026-10-05 19:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 98af73e5-495b-3d53-aea3-c54444e10a1f | -9.7127 | -65.0763 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 12973321-96d0-3e5f-a06c-a2499a81a590 | -9.0982 | -65.4904 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 4289de6d-248a-3d77-80e6-f2bec2a3ee84 | -5.8321 | -45.0332 | 2026-10-05 19:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 53dc1458-6a3c-3f59-a433-48145170e9d8 | -9.7126 | -65.0951 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 147.8 |
| a0801a79-7509-3095-a9a7-9d32bcbfe399 | -8.8519 | -66.8012 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| c3359f43-0aa6-3f3f-bff1-790b127a9f42 | -9.4751 | -64.3336 | 2026-10-05 19:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| ccf92359-f46c-353b-9f52-410e188b6190 | -13.5199 | -61.1124 | 2026-10-05 19:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| fe77ac2a-9843-3803-994f-3b01207b3112 | -9.077 | -66.0881 | 2026-10-05 19:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b559988d-6ef3-37f2-8509-3e9c9bbd63ad | -7.3638 | -72.8446 | 2026-10-05 20:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| f4699d2a-c03c-3dc6-80c8-0ca2a77aa7c1 | -10.2827 | -60.5432 | 2026-10-05 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| b89fdfcf-09b3-3e7b-b26d-a15c61d7cf6a | -9.1243 | -68.2206 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f225be1a-4755-3c61-ba03-b781705b7813 | -9.1072 | -67.8141 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 45aded1e-c89c-3e13-b9a0-593f16de5c69 | -5.8509 | -45.0318 | 2026-10-05 20:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 613d6996-0b3b-31f5-be9d-55cb0128215a | -8.9873 | -65.4379 | 2026-10-05 20:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7229c0e6-9c60-3f28-952f-bfe933eb8469 | -9.4751 | -64.3336 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| e9e69f7a-337e-3f23-8a13-a1c44990f1bc | -6.7387 | -44.2755 | 2026-10-05 20:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5b31d34b-58ed-38bb-b6bf-3431b9156345 | -9.5425 | -65.6815 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 4a9c1c8f-2f3d-3721-98c3-251c1a07e139 | -6.3851 | -43.9826 | 2026-10-05 20:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fcb984aa-b081-3fc8-957a-0b4ad7281f80 | -9.1611 | -68.2937 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e21efc89-4b87-3c8c-a50e-cd4b99f9b83d | 2.4769 | -50.8294 | 2026-10-05 20:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2dc5efe6-af31-3237-9444-47faca51b80b | -5.8094 | -43.4025 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 30bb3333-2c27-308d-b9a1-5a8bee879a28 | -9.1426 | -68.2941 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b1bba673-4902-3e1e-9eee-1e5350c3a6e4 | -8.9014 | -68.5211 | 2026-10-05 20:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| cdd66771-1e7e-301e-b34a-c2596306576a | -9.5424 | -65.7002 | 2026-10-05 20:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 4ba89672-2f83-3947-bda9-2285e4160e08 | -5.8092 | -43.4258 | 2026-10-05 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 192.0 |
| e05bd8b9-c7a7-3c8c-abd1-06b44b02eac1 | -10.5508 | -69.2427 | 2026-10-05 20:00:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 56.8 |


[Clique aqui para ver as próximas entradas](README169.md)
