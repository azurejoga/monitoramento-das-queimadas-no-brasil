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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26f6d93a-44cb-39d9-9d76-3ef636ad4298 | -16.3418 | -51.5434 | 2025-09-13 03:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1d738f97-d0fc-3551-b423-7d8da382b678 | -16.0805 | -49.9489 | 2025-09-13 03:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| cec72c63-9e2c-3045-b9e5-4645860f74b7 | -10.785 | -50.5493 | 2025-09-13 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 37923043-c745-3f34-b746-3358dc73887f | -9.5135 | -54.6494 | 2025-09-13 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| bd4ef3b1-d997-3563-ad20-6b052021203e | -9.5139 | -54.6089 | 2025-09-13 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 110324a5-893a-3201-8f23-aad698bf4064 | -9.5004 | -55.9788 | 2025-09-13 03:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 46bd5884-098c-39f7-b683-d5243d5d876b | -9.5006 | -55.9588 | 2025-09-13 03:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 29869219-952c-3ccd-864f-ae8e943bc447 | -9.5322 | -54.648 | 2025-09-13 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 9a14d1e6-4f2c-3cb4-a783-4609c06bd65c | -11.1237 | -50.7049 | 2025-09-13 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d686b45a-9b62-3c83-a60f-7b833c230598 | -9.5326 | -54.6075 | 2025-09-13 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 8e018686-e1e8-33f9-8151-85e0e03df081 | -4.15173 | -43.8835 | 2025-09-13 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aaf8271-db50-36f0-b2cc-57b4996ef7c1 | -3.94911 | -40.74278 | 2025-09-13 03:45:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6168966e-800f-3301-95f0-d18e040dc9d0 | -6.18124 | -43.48376 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78be5d32-0b6f-3976-85c3-68e221161dd9 | -6.10472 | -45.94173 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bdc358cd-428e-32c2-8382-db854e439082 | -6.39138 | -44.37441 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65f5ee36-cc4a-3ab8-9e68-d91acbd94a83 | -7.45058 | -34.85902 | 2025-09-13 03:45:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c0beee50-6a86-398b-b554-eff6b910d798 | -4.91905 | -47.86629 | 2025-09-13 03:45:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 610b181b-8be8-3397-b1e7-84eb400aabdc | -6.16919 | -41.14986 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7b0cd8f-6949-3d2b-a590-91748f2c91df | -6.19128 | -45.28489 | 2025-09-13 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90f794ff-3997-3099-b7fd-21f18d8541eb | -6.71588 | -44.02309 | 2025-09-13 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47d8324e-4bd6-344b-afee-3847ff8f0ef1 | -5.10913 | -46.06889 | 2025-09-13 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6852de3d-4820-3a28-8bd8-024fd6079e56 | -5.11439 | -46.07483 | 2025-09-13 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45a6f54b-1174-3230-a764-7880405edaa7 | -5.35237 | -47.29288 | 2025-09-13 03:45:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 701988a7-8b79-37e4-873f-b7cc71c8f8bb | -6.28991 | -44.24726 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 002eba1e-c83a-30f4-82ba-d026b264ac03 | -6.21183 | -43.33791 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| afda39a1-12dc-32d7-a918-e67088e5c0ac | -6.69669 | -44.13087 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac7ce7dd-4850-3802-9a0b-c5f6fff172e0 | -6.77169 | -41.5951 | 2025-09-13 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13656375-db1a-3079-8b5d-e1645236d79c | -7.3127 | -43.92844 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc5c5f5-5c83-363b-8828-2dceb7b36609 | -5.799 | -42.46814 | 2025-09-13 03:45:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84820f12-488b-37e7-90fe-23c5ee6c89cd | -3.22883 | -47.13478 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8e979e91-2402-3e99-a95c-a5db0f7fd314 | -4.82971 | -42.857 | 2025-09-13 03:45:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b12b9ca2-1e78-3470-8b14-dec738ce0706 | -3.21542 | -47.1324 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 23342cfa-b27c-3f20-9866-58c25c3b7b31 | -5.8946 | -43.45711 | 2025-09-13 03:45:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab51839-a23f-3142-bcca-8de0da67018e | -4.54278 | -43.73447 | 2025-09-13 03:45:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6492753d-34ce-3873-a0c9-cf5b45d458ef | -6.39198 | -44.37094 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aed6d60-1deb-3834-bc33-166665aa5382 | -5.2007 | -44.31087 | 2025-09-13 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f3bc17d-bb83-39e4-b6a5-6bd8fd406be1 | -6.68854 | -44.14621 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e5c3a4-117d-3b0d-a099-d298b6cad2c4 | -6.11704 | -43.91288 | 2025-09-13 03:45:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd8f43f5-ca27-3d08-8072-4a7f2723c767 | -6.17695 | -41.13016 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6570d774-8933-33cc-8a61-baa8ae944519 | -3.22986 | -47.12877 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0d8419ac-1c64-3314-8a88-c8dcc73060ca | -6.32078 | -44.58661 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50028c37-a671-3a16-880f-e32755a36b0c | -5.20011 | -44.31432 | 2025-09-13 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60538945-0be2-327f-8cc3-de00c43e8bc7 | -6.55867 | -44.77608 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f7520d4-df09-32f1-99a2-a90ae62751f4 | -5.58779 | -35.72113 | 2025-09-13 03:45:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13cedb80-8332-367d-b135-ecb10bb8d1f6 | -3.21642 | -47.12658 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46193c8e-2b29-3cea-99b3-d9d8953ddbea | -6.17057 | -41.14163 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84c4e634-4205-36df-83b5-4d27be3c2880 | -4.92592 | -47.86724 | 2025-09-13 03:45:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c8e9b50-d530-32dc-b725-3e25de5b5bd0 | -6.55801 | -44.78066 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d7d82d3-4ef4-376b-9862-8835fbc3aea3 | -4.82908 | -42.86199 | 2025-09-13 03:45:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74e86bf5-ff95-3675-ad63-d26d1be8ca61 | -5.63981 | -45.94357 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f1cdf1d-a575-3b4a-a9dc-3b97f155593d | -6.87115 | -45.6452 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3b45553-c27d-3448-8be8-af881cdde2bd | -5.30101 | -43.06573 | 2025-09-13 03:45:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c416c069-e3db-3383-b3c4-0570bf4d3a69 | -6.10394 | -45.94612 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d466004-4e5f-3bab-a654-1d08931b6c4f | -5.49437 | -42.1545 | 2025-09-13 03:45:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eff1c994-3646-343d-8225-4280e3e0621e | -5.66163 | -42.6125 | 2025-09-13 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1edffdb-ef5c-3bfe-8bb7-b030c22608d8 | -5.80323 | -35.54379 | 2025-09-13 03:45:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b9f213d-0eda-3a1b-af1c-3526dde2d906 | -3.22314 | -47.12767 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3d58acf9-5a3a-3430-9cfb-d23223e22861 | -6.69556 | -44.1372 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 473a5d6f-d6e1-3a8b-9b9f-6b353ee92ebf | -4.83005 | -42.85619 | 2025-09-13 03:45:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a150f3b6-14c6-3036-aea9-a3bfcc7357f2 | -5.4072 | -42.83779 | 2025-09-13 03:45:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fbe82b4-2828-3357-933d-73215597510e | -6.10643 | -45.94698 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c2ff5b9-1a32-3baa-9c98-fb2745622e91 | -6.55867 | -44.77681 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3f983ba-8045-3de0-bf9a-40c3924ac25c | -6.5951 | -44.31211 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7d28a22-3df4-3bc0-b0cd-c887e9942837 | -6.55932 | -44.77304 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 420146dd-d22c-35b9-bcd7-a1c2e07f6a67 | -6.72052 | -44.02721 | 2025-09-13 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05db21cc-8da2-3c5a-905a-f14da15d3cac | -6.98567 | -43.80515 | 2025-09-13 03:45:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a5d7298-93b1-366e-af82-7abeb0f6d427 | -3.22436 | -47.133 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cf75082a-09e0-34b2-b456-39d35c7db9c6 | -7.07387 | -44.12534 | 2025-09-13 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6fc8c38-b571-392f-8934-465ca6b318f2 | -5.302 | -43.05993 | 2025-09-13 03:45:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ad46c22-9499-364a-aab5-995716a91845 | -6.14118 | -43.36332 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d2ed3f8-c686-3687-a98c-1eb47b26c767 | -5.20497 | -44.31874 | 2025-09-13 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dea9b622-287c-3e80-b855-7deeb32c3649 | -3.21377 | -47.63255 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f3768cb-3d7d-3b0d-b245-d65ce44a049d | -6.84422 | -45.66181 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c88e5f73-f56f-3bfe-9f4d-4938d078beb4 | -6.16662 | -43.35938 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58e2fc1c-b61c-35c7-aea4-2c17db51d54f | -6.2951 | -44.24902 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b5e12c-43a4-38e9-a337-8ae7de83d130 | -6.55935 | -44.77232 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7711a2d-5e8c-3399-8f67-8309fb5ed40f | -3.22661 | -47.64061 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9da2a52c-974b-366d-9d58-d67370125b50 | -5.49164 | -43.99457 | 2025-09-13 03:45:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bd12043-0568-3e6f-97e4-30a44f1d75aa | -5.34591 | -47.29111 | 2025-09-13 03:45:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca5cb0bf-7997-390e-a5d3-014652c84d52 | -6.69613 | -44.13401 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07e4e5bc-5d30-33e4-811f-b1c879a30a10 | -6.43347 | -43.33066 | 2025-09-13 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0af356c-8762-35b8-abbe-bd380eac99aa | -6.29051 | -44.24385 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfd14f67-f153-3c8d-947a-4c548d801100 | -6.1616 | -43.35845 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 80597afc-5ad0-3680-86a8-581a232b4b4d | -6.61953 | -44.0803 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce1cdbe0-0422-3481-8dbe-3a842bb7d815 | -6.10988 | -45.9474 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22ee1731-9c06-3ffb-8d76-06c43bc8b48a | -6.55798 | -44.77988 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f0b36d2-5ae2-38bb-815e-8ea3a739b0a1 | -5.4922 | -43.99124 | 2025-09-13 03:45:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21bf8e4b-a85b-305a-aab4-199f4c8731f2 | -7.21864 | -43.97443 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b36e7e-cf21-3dee-814e-b1350a8d73b4 | -6.50779 | -43.80324 | 2025-09-13 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9052744a-727e-3571-aecc-3c93a9231aeb | -6.68834 | -44.11697 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5c3366c-128c-3ab5-92fe-bc1b3a318457 | -7.63208 | -40.45513 | 2025-09-13 03:45:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f4bc630-f723-3269-bad1-c4ede4c5eb51 | -6.20533 | -42.69505 | 2025-09-13 03:45:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0fbf1cba-9490-3b9c-a073-ea1ac37932a1 | -6.28525 | -44.24248 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02debd2f-34f4-3834-bb80-46003b1a48c6 | -5.20615 | -44.31187 | 2025-09-13 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d63c0692-19ba-3c60-b566-145622af0fb7 | -5.35011 | -47.29249 | 2025-09-13 03:45:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 862f055a-a928-324c-aae3-ae3210eda880 | -5.24652 | -45.57941 | 2025-09-13 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 618b0c31-acd1-3787-acc5-c53fe9cf0518 | -2.90817 | -40.40707 | 2025-09-13 03:45:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b44c638e-cc02-374f-a0ca-55da45c92ea0 | -4.15111 | -43.88706 | 2025-09-13 03:45:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05115ad6-3a7a-3063-a8f0-aee48a7ce1e1 | -6.77199 | -41.60189 | 2025-09-13 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22b390a4-4fb1-3483-b80e-1e9fa219c9bb | -5.10826 | -46.07384 | 2025-09-13 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README22.md)
