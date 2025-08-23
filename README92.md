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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08227ccd-9573-3405-b921-15cc99c9c63e | -5.7429 | -57.6009 | 2025-08-23 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 9928762a-33c3-34a3-8f71-ab065af1f093 | -7.0352 | -44.6396 | 2025-08-23 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| dafbf2f2-0cfe-35f4-b06b-401412435f0b | -6.3698 | -45.5582 | 2025-08-23 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8e9b096e-2df1-3a53-b88e-bcce7a8ec75e | -8.0379 | -47.3117 | 2025-08-23 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ec7a5a52-cc25-3f43-b4b7-4e1353c5dad4 | -8.9579 | -40.6311 | 2025-08-23 14:30:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 158.1 |
| 716e2bc5-c84b-3c15-92e3-08da99de850a | -10.4784 | -46.831 | 2025-08-23 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 2c090f8d-4c51-329d-9529-8de9a1712cb3 | -5.8323 | -52.0681 | 2025-08-23 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f48b4e18-f4f2-3b5e-b1d1-13f28c71380d | -10.639 | -50.1589 | 2025-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8c2fdbc6-32c9-3fda-b8dc-a65ec659b531 | -6.37 | -45.5356 | 2025-08-23 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f6cbd7bb-4aac-3ea6-be57-2a412d753fa0 | -6.558 | -45.4531 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| dc5e18e1-7b6c-31c8-ac74-51df13f630a9 | -6.4842 | -43.4637 | 2025-08-23 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b0f68304-c09f-3937-9f55-d67fb7369e07 | -5.8309 | -45.1693 | 2025-08-23 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2713da1f-4a6f-3a21-99ae-dc00b4885c18 | -15.0183 | -54.8942 | 2025-08-23 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fe026875-2db9-3d1b-9f2f-95a14e18a6c7 | -11.14 | -44.7422 | 2025-08-23 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ab43fac1-6852-3cb2-a44b-8b2058c4b8e7 | -6.3964 | -44.7396 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 6a5eedfe-492f-39df-9837-d696d4fdf23a | -5.7431 | -57.5814 | 2025-08-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 316.7 |
| 3f5348b2-aead-33bf-9b0f-eb2f937e117d | -5.4364 | -60.1779 | 2025-08-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0776cf3d-2f4a-3207-a28a-baf9da201e07 | -6.6044 | -44.5624 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2b9a5a28-7cba-31c5-acaa-d4698d4c2b59 | -7.6107 | -45.2481 | 2025-08-23 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3d80b313-f0d1-3036-83bd-c242ecc42f17 | -3.1347 | -58.0459 | 2025-08-23 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9f1fb2e0-2579-38b3-be3d-723265e8e75f | -7.9447 | -63.0528 | 2025-08-23 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 7dc5daf0-f9bc-34a6-a197-4ab07811c8ea | -8.613 | -62.6118 | 2025-08-23 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9213821d-eabd-3e6a-b846-818a1e580148 | -11.1208 | -44.7449 | 2025-08-23 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 12a7590a-34ce-3564-ab59-bab560f9a18a | -7.602 | -44.3801 | 2025-08-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 24b5fb15-1b8a-3273-97aa-886c2c622171 | -6.37 | -45.5356 | 2025-08-23 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2726929a-f7a0-3085-a087-2c00c99cec61 | -8.44 | -48.2612 | 2025-08-23 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1a3accdc-644a-3d97-aac4-7f0f5d0bfb16 | -13.478 | -47.0227 | 2025-08-23 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 001c4f87-7758-3232-95ed-b12640a461ea | -7.0352 | -44.6396 | 2025-08-23 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 128a665e-a726-32c1-9c8f-5c9ab3dbec6b | -6.2275 | -44.7758 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a418ba42-0ed0-39e5-ab4e-bc385f00fe73 | -8.7783 | -46.7305 | 2025-08-23 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cd20c257-0107-340f-bebb-d0aa1f3a5ad1 | -14.3704 | -52.0386 | 2025-08-23 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| dfa310cd-f7e5-320f-9154-1a09af7ab305 | -10.6769 | -50.1549 | 2025-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e394f5ea-c9e2-32dc-b3db-93dcd496d120 | -9.9493 | -60.1947 | 2025-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b3b939b0-0b88-35f4-a2bc-ddead9117a72 | -9.0494 | -47.6332 | 2025-08-23 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e69045f1-ef3a-378a-866c-cc4da5a21590 | -5.8323 | -52.0681 | 2025-08-23 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 81df976d-c948-396a-b626-fac472613f2b | -10.4784 | -46.831 | 2025-08-23 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| ff1b0c59-2ee4-3f20-aba7-a8c6266150e8 | -6.0784 | -44.6961 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7f12ff4d-ebc1-351c-8f19-b406ecd11000 | -12.952 | -46.3104 | 2025-08-23 14:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| bdd8c0d8-ad32-3609-b333-1d4a7a79e45d | -13.4969 | -47.0423 | 2025-08-23 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| eb0f71d2-6c04-353d-8370-d42e175bb772 | -10.6201 | -50.1609 | 2025-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 92b196cc-234b-3e4e-bacb-7031768fdca9 | -10.4239 | -64.4281 | 2025-08-23 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 72e7d869-c065-31b6-81c4-99f12a6b5905 | -9.7241 | -47.9588 | 2025-08-23 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1e543d53-9a9f-344a-bda3-995859864596 | -6.097 | -44.7175 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a2107a5a-cc2a-3c86-82ce-e161b9411dba | -8.0379 | -47.3117 | 2025-08-23 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 87342212-a99a-31b4-88b0-fac06e8c14e5 | -9.1895 | -59.6364 | 2025-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9917bd25-e713-32c4-924b-db1149dc98a2 | -7.9448 | -63.034 | 2025-08-23 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 52673aa3-8eaf-306a-a435-da80fe017161 | -15.0183 | -54.8942 | 2025-08-23 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 10961753-c9dc-34ec-83cf-db3dfc398da0 | -6.1189 | -44.3726 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 8f2a5b4e-a3e4-3c90-ba95-7ccbec7bf884 | -9.1711 | -59.618 | 2025-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 42521599-5954-3377-948f-5a813c787e87 | -6.5781 | -59.871 | 2025-08-23 14:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8325aff2-0788-324b-80f7-d5ef07ed56d2 | -8.9579 | -40.6311 | 2025-08-23 14:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 187.7 |
| 9a867d22-b166-3a5f-ab48-8168561cee9d | -5.4365 | -60.1588 | 2025-08-23 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| d0b1adac-1f10-3e29-b371-8a7133a74100 | -15.034 | -56.3928 | 2025-08-23 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c9da44cf-c186-3768-b902-ab2c083cbe52 | -8.5458 | -48.8592 | 2025-08-23 14:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 35550dd2-bac1-3192-8a89-ad0afc6ed3f5 | -9.1898 | -59.5977 | 2025-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d56abea9-464e-33e5-9b58-120ceda04971 | -8.546 | -48.8376 | 2025-08-23 14:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8daff4b7-90b5-3bc1-b407-21e68dd77edc | -15.2288 | -53.8481 | 2025-08-23 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| dfeee1b3-3e65-3508-8503-0a89b1cbca28 | -6.9837 | -44.1847 | 2025-08-23 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 85e5775a-2fad-3d5c-b2e5-ecdf6832dbb2 | -10.6772 | -50.1334 | 2025-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 70e5e029-096b-329f-ab21-f755ada00bd4 | -13.4775 | -47.0453 | 2025-08-23 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 79df2413-a700-357b-bac2-e97e2bb7006a | -8.853 | -49.8843 | 2025-08-23 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 47255c5c-1782-3c5b-9e91-3d5d4d1eea91 | -7.6298 | -45.2236 | 2025-08-23 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6a11b4d1-157e-329b-856c-1bf41b81ec73 | -15.558 | -51.7035 | 2025-08-23 14:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 145.9 |
| f94cf234-168d-3047-8c8e-403420c1f9dc | -5.7615 | -57.5807 | 2025-08-23 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 257.4 |
| ac001592-5433-3cca-9a1d-7b1161de6ccf | -9.1712 | -59.5987 | 2025-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| bcef9c4a-fbb7-36c8-a5ad-c9e6443f932b | -15.5385 | -51.7064 | 2025-08-23 14:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 75d10d99-3093-3db3-b0f3-80216f94972b | -10.6393 | -50.1375 | 2025-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 05d96dde-05de-3701-a408-d7cac684a626 | -6.4842 | -43.4637 | 2025-08-23 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 29ec302b-8d86-37aa-8534-9fddff06d194 | -14.5079 | -53.0365 | 2025-08-23 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2c459ce6-c869-3c03-be23-ec0f471076b2 | -6.0972 | -44.6947 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 279.4 |
| ebb0d00d-ccf9-34aa-ac19-84f300891e1e | -8.5944 | -62.6126 | 2025-08-23 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b3508074-a5d8-3e91-a237-e063f178d71e | -14.6899 | -54.912 | 2025-08-23 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 594da83e-23b0-3f03-a44e-58969e384218 | -11.1396 | -44.7654 | 2025-08-23 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| c2f8ffd7-d5d3-3d8a-a350-b40464bb6410 | -6.9449 | -44.3033 | 2025-08-23 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e45d2064-a897-3be6-8cac-f07ea79c588e | -7.6366 | -46.2823 | 2025-08-23 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f0251394-b2f8-3fd6-9419-9b99bd211b0a | -6.1187 | -44.3955 | 2025-08-23 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 36f246dd-e221-30ea-9489-4e78f2075b37 | -7.6296 | -45.2464 | 2025-08-23 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 8c518660-9040-3d16-858a-7af3d82dc20c | -8.527 | -48.8609 | 2025-08-23 14:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 1f208fd2-91c1-36fa-9ad9-c41021375245 | -8.8921 | -62.4297 | 2025-08-23 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 106.1 |
| e9a2c996-671e-3aa6-ab4c-bf2e2a703e9f | -9.1897 | -59.6171 | 2025-08-23 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| dc8e5ef5-de33-3190-9c5a-1905f022088f | -9.9495 | -60.1754 | 2025-08-23 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 1edd16e1-d681-3a85-89f9-297ea2aa5dcc | -14.7521 | -45.4091 | 2025-08-23 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| a1efb7f5-9ee3-3012-8cc6-2dce7a542e87 | -8.5272 | -48.8393 | 2025-08-23 14:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 66068c85-65e7-336b-844e-3da6ea4650aa | -10.6962 | -50.1314 | 2025-08-23 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d3743978-fcd5-30e2-a5fb-30601fbf60e0 | -13.4586 | -47.0257 | 2025-08-23 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 5abf43da-44cc-3fd9-8e76-73bbb0f98239 | -8.9388 | -40.6336 | 2025-08-23 14:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 6ac2a55e-7e62-312c-acd7-3bb1982ab05d | -11.1204 | -44.7681 | 2025-08-23 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 395.2 |


