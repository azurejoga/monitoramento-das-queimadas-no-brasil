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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e7fd67c-5139-3fa5-af08-0636ccffa304 | -7.4153 | -42.6479 | 2026-09-30 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| f8490e54-847e-34d5-ac0c-d5ec2448cfae | -6.8762 | -43.7083 | 2026-09-30 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 3c7f933f-8fc2-34ba-a2a4-1cb63364e5fa | -9.9976 | -50.1179 | 2026-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9db83763-82b3-3f2e-8854-b4e58e6b6bcb | -11.2095 | -45.1478 | 2026-09-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 93ef56e0-f788-35a5-8ea2-94c0d1492e4d | -7.4156 | -42.6241 | 2026-09-30 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 6425b164-955f-3ed3-816e-916cf3d0c601 | -11.2758 | -43.5303 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| d6dfc637-8efe-3753-bf50-0c64b9ea66ec | -7.4733 | -45.7809 | 2026-09-30 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 77e856c8-f77c-3440-b55e-75a162fb2a6b | -11.3555 | -43.3526 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 18a0f034-df9e-3516-b838-e1e1325ec30e | -7.506 | -44.5503 | 2026-09-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a0666f5a-8247-3f2b-8a28-5776a2cd2f76 | -8.0169 | -42.8444 | 2026-09-30 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 222.4 |
| 13ae8541-aa0b-31ed-897d-1db133f58d88 | -5.8714 | -51.7767 | 2026-09-30 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7195c9b0-8062-34c1-ab7d-7d205823f9a4 | -11.6789 | -43.4921 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0cd38f75-6c92-38fe-a050-db53431ecfc9 | -11.2566 | -43.5331 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 98b0ab53-db12-308d-bfdd-8fa5bda45e0b | -6.1402 | -53.0574 | 2026-09-30 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 69811a96-a967-32fb-9f1e-ba5eaef95075 | -10.0892 | -50.3222 | 2026-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5a1010f3-35d7-30ce-a6e9-4463567fc717 | -6.7254 | -45.5749 | 2026-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3ebb2eec-3e10-33d8-a1ef-1f529e674916 | -8.6448 | -45.3717 | 2026-09-30 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| edb3fa39-7912-37e0-99c3-60e3ada4b0c7 | -8.0166 | -42.8681 | 2026-09-30 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 156.0 |
| dfb8a5b8-4642-3525-a0fb-d0d4188b5155 | -12.3548 | -46.4 | 2026-09-30 14:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 93452f82-27d6-3c8b-ace2-7b78b9f7b2ed | -9.7916 | -45.8328 | 2026-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 34ab4d4b-8f69-3163-9770-3040adc340ad | -8.2668 | -45.4564 | 2026-09-30 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| be0da238-29ee-3efb-a3dc-fbd545ab01bb | -6.9419 | -42.8598 | 2026-09-30 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 714447fc-a462-398c-a404-5a2f7a698c67 | -17.5345 | -43.6891 | 2026-09-30 14:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e2e06721-d291-3cf3-a60a-ef4281420312 | -10.0331 | -50.2851 | 2026-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| aadbab57-7923-3b1c-9e47-0ff82ba8ae76 | 1.8586 | -55.6241 | 2026-09-30 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 47ee6910-6474-34ce-931e-86702e779602 | -5.7873 | -43.7758 | 2026-09-30 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e86ca612-d7eb-37cb-8160-411c59682889 | -7.0547 | -42.8726 | 2026-09-30 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 29274e6c-e66f-3b9a-af93-bfd63754d523 | -7.3467 | -42.0839 | 2026-09-30 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 9df309cf-df3f-369a-bb1f-693cfcd1f8e7 | -6.6129 | -43.7317 | 2026-09-30 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 05d19f7a-ec6e-39c5-964f-2e3fd09490ed | 4.1884 | -60.63 | 2026-09-30 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3f1b6b41-cd3c-3b1f-8f86-08fb88538fb3 | -13.3835 | -44.0132 | 2026-09-30 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 1f53366b-04cf-32a0-8e4b-630a397fae1e | -12.1078 | -47.3803 | 2026-09-30 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 08a4e2de-d9cc-350e-9392-d1315df63f99 | -7.2561 | -43.3697 | 2026-09-30 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 5e88a092-10aa-3e61-b456-0b1af0826418 | -7.0451 | -42.0666 | 2026-09-30 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 85202b6a-03e2-3d6b-baf4-e924f150896d | -11.6395 | -43.5455 | 2026-09-30 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 6c6eb526-1332-35dd-b016-539d47ca874c | -11.1958 | -44.8269 | 2026-09-30 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7afe8309-d96e-3538-a0cb-1ed2b7dd763d | -10.0162 | -50.1374 | 2026-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| db9b3fab-ae6a-3028-9480-320e6609cb5f | -6.7251 | -45.5975 | 2026-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d288918b-6d41-3022-af87-0136f5247244 | -9.6654 | -46.7248 | 2026-09-30 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f30bd6d8-2f2a-3d9a-819e-6fd6b1a55d80 | -3.7129 | -60.5832 | 2026-09-30 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f096b399-d87a-3100-a0db-3b9d6eaf3abe | -1.2085 | -49.0838 | 2026-09-30 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 16e3129c-ccee-3af5-b282-59c181eb3fbf | 4.1884 | -60.63 | 2026-09-30 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c7397984-f929-39fe-856e-c7583137f55e | -10.052 | -50.2833 | 2026-09-30 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b24abf94-bdf2-37c9-b9e5-b2461f8eac9b | 1.6566 | -55.9227 | 2026-09-30 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 05f25bcc-110f-3c96-b341-2bfdc338ed2f | -6.1402 | -53.0574 | 2026-09-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| b4ed7e9b-fa4e-393c-b534-3531248346a5 | -10.2827 | -49.9606 | 2026-09-30 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4c83b687-367d-3cb4-9c19-0ab23b174ffe | -4.3516 | -48.9713 | 2026-09-30 14:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5e4662b6-5fe2-3016-81c3-6d2b3fba242f | 1.6749 | -55.9422 | 2026-09-30 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a196530d-6a56-354b-b2aa-19f4c8cd71f9 | -9.9976 | -50.1179 | 2026-09-30 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2ca6de4a-cd5c-3f41-ac0f-f23bf5849780 | 3.6971 | -59.7263 | 2026-09-30 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| bf2fba0f-6ccc-3859-b261-3e490eb8b4a4 | -9.8064 | -44.8265 | 2026-09-30 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0f23efa7-286c-3bf3-8fe9-8005a562bb70 | -12.5135 | -43.0943 | 2026-09-30 14:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 192.6 |
| f90c2d32-4054-31b2-9075-45e62e954421 | -11.6395 | -43.5455 | 2026-09-30 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 9c5aab89-95fa-359c-a55b-e4d5bd4a408e | -13.3272 | -43.9285 | 2026-09-30 14:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 86812425-03e6-341c-9b44-d3c23847252f | -9.6657 | -46.7024 | 2026-09-30 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 371a25ea-a0ad-3bc9-9947-3b070d4469fb | -0.5258 | -49.1325 | 2026-09-30 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5322928b-2310-3410-8115-00d66b2009ab | -15.4782 | -46.1331 | 2026-09-30 14:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 0adf5535-bc1b-352b-925d-f239fc27bceb | 1.6566 | -55.9424 | 2026-09-30 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 39d01263-7657-308a-91e0-378b04b9492f | -0.8399 | -48.725 | 2026-09-30 14:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f8dba601-e609-317c-8ce7-71f803655e6f | 1.6749 | -55.9225 | 2026-09-30 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8ff0d82e-9333-3ef0-8075-f2b9fdb1f882 | -5.8712 | -51.7974 | 2026-09-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3134b16d-dafc-324a-b6a5-95e9db6840a0 | -9.1337 | -49.9656 | 2026-09-30 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 889bbcf2-7c0a-3814-b977-14a9534b382c | -10.2843 | -44.6274 | 2026-09-30 14:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 197.1 |
| b54e0ddd-cfe5-3162-ab86-7aa6fe935fa0 | -5.6409 | -45.544 | 2026-09-30 14:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2d22d2f9-bfb2-3f27-ac88-b83e470be1e4 | -4.1482 | -48.8948 | 2026-09-30 14:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| d26d658f-3a4f-3df0-a823-69c266b2820b | -12.5329 | -43.091 | 2026-09-30 14:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 00fe36e4-efb5-3c7c-acff-d7de17aa259c | -5.8714 | -51.7767 | 2026-09-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d72ac3ce-7ad0-39ab-bf06-538d2a32c7b6 | -6.8864 | -52.4821 | 2026-09-30 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d7efdd48-bde0-36e5-8089-60bea5b96f1e | -7.492 | -45.7792 | 2026-09-30 14:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8a354d94-cd21-30bc-bc47-f81f8ff826df | -6.8177 | -43.8991 | 2026-09-30 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 955fa788-138d-30ce-b9f3-d30d6f5f708d | 4.2067 | -60.6296 | 2026-09-30 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| edc1e1b4-0013-342c-be5c-6a4900f51f1b | 1.7115 | -55.9221 | 2026-09-30 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| ac8c0a97-e5ca-38ee-8660-ed6de0c05617 | -6.1598 | -52.9134 | 2026-09-30 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b2a1947f-fd08-3de4-a3a2-385d4ad8e434 | -4.3516 | -48.9713 | 2026-09-30 15:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 22b5fee4-f925-3279-96a2-65486b83880a | -7.4918 | -45.8018 | 2026-09-30 15:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3d0af96d-4ed4-3461-bf6d-8552d096d280 | -0.8399 | -48.725 | 2026-09-30 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e1ef443b-2a07-3106-b6f1-22f941b5b861 | -5.9889 | -53.5335 | 2026-09-30 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4e0241ec-5d64-3f27-bfb1-c8678adf2c65 | -4.1482 | -48.8948 | 2026-09-30 15:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a975e9b2-3a4e-3ffe-8e97-71ac7a288f4c | -8.3805 | -45.3994 | 2026-09-30 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 5811f4c9-4d02-37f8-af85-7426c879d08f | -10.6941 | -50.2814 | 2026-09-30 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 87ce99d0-b83a-36ac-b55a-e1554597294a | -8.2668 | -45.4564 | 2026-09-30 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| dfc28d56-5011-3cd5-8008-1183b8a820e7 | -5.8714 | -51.7767 | 2026-09-30 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2e67c2d9-42cb-34c1-a764-eddd3b1cfea1 | -5.641 | -45.5214 | 2026-09-30 15:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a59c30dd-ddf4-3ede-9d1e-7c6bb67e83c8 | -9.4813 | -46.3646 | 2026-09-30 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8d5dbebf-5100-3401-90d0-9a4462f3a133 | -3.7129 | -60.5832 | 2026-09-30 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 42a2b883-3762-3a24-bd1a-c74dfff8b104 | -10.3016 | -49.9587 | 2026-09-30 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 156600c9-e22e-3fcd-b719-ca9183b73f39 | -6.1784 | -52.8919 | 2026-09-30 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4a416f45-859c-3947-a8ed-30523160b388 | -9.5087 | -45.7525 | 2026-09-30 15:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 04488658-e8dd-394d-8428-f36e43e805ca | -9.0652 | -45.0062 | 2026-09-30 15:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b97f6576-3133-39ee-bde3-430fa388e502 | -2.0933 | -49.557 | 2026-09-30 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1d566719-4b11-3278-8f1e-24dbb8dff56d | -10.2843 | -44.6274 | 2026-09-30 15:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 387.6 |
| 6a91641b-20d2-3de3-868a-ee7c8569d73a | -10.2065 | -50.0113 | 2026-09-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b387a92d-5d45-3001-829e-8075ac8ce77c | -10.1878 | -49.9918 | 2026-09-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| fb7d775d-dcdf-3d52-982c-80c81f4e1ce4 | -10.0892 | -50.3222 | 2026-09-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f5391176-9e76-3640-bd69-80f688317c13 | -3.0875 | -50.2901 | 2026-09-30 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 08c7c656-2d84-30e9-a720-44632d5ac7fb | 3.8611 | -59.971 | 2026-09-30 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8fddc09d-ec8b-3f5a-a7ee-928b98c8f468 | -15.1348 | -44.0412 | 2026-09-30 15:10:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 270.8 |
| d8125b94-f2ee-3ca4-a9bb-019c35127c98 | -0.8399 | -48.725 | 2026-09-30 15:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0f6f49ea-180e-35ae-9d1b-4679996d31f6 | -10.2067 | -49.9898 | 2026-09-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| fa6f5644-003b-3942-9343-ca1ba363b5a1 | -2.0933 | -49.557 | 2026-09-30 15:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |


[Clique aqui para ver as próximas entradas](README73.md)
