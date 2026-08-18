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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 934cfd8a-2730-3d0e-9d5a-84b77c07257b | -2.70728 | -54.22393 | 2026-08-18 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 946f5046-b81d-3be7-b20a-c83d8b168bc9 | -8.3588 | -46.47807 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10b357c0-d546-3ef1-b8d0-1ce19c393216 | -8.19639 | -55.01805 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45a1ee2f-2b46-3497-abea-958f888baecd | -9.46057 | -51.61438 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d887a9b3-40b2-3975-91cc-d3a2388bd837 | -7.39018 | -55.48452 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d7961f7-461e-36d9-8f4a-b7e6795bb362 | -8.58027 | -54.6873 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 94db9888-d236-3469-911c-f1b95a602b52 | -8.33277 | -46.47037 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 794c1e86-91ba-3c91-93c1-07ff508a8a4d | -9.07147 | -50.83495 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d8342d90-afdd-3384-a19e-e1ed4aef8f1f | -7.54776 | -55.56463 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87483ef1-dd15-35fb-95a9-f9272b95792e | -6.53452 | -43.12297 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b13296d2-0492-3907-be0b-50cade8d0927 | -8.56719 | -54.68756 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59b792e2-a300-3e5e-bad5-3675ef1b3a57 | -6.16086 | -47.79305 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 534fe1c4-7007-33db-88bc-a2347e9256a4 | -5.80277 | -43.63891 | 2026-08-18 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9682d9a2-9d7e-34a8-9856-10a0bae184b4 | -8.02787 | -55.13142 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff103cb-6b7a-3896-98de-0d1466854d15 | -8.04297 | -50.10616 | 2026-08-18 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f0af55d-8fc5-321c-bd04-2ea3f40b212f | -9.21678 | -50.09945 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2893e2a9-b09d-3a7f-9d93-20c410a4f092 | -6.74875 | -59.15922 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a1ce76d9-d538-3340-9092-16ce1733f662 | -7.46176 | -46.16088 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63fb512f-74f0-3f0e-9859-e13e6b3d52ce | -9.06926 | -50.82522 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41bda038-7011-3807-9b1c-0224c8e82a3b | -8.56768 | -54.70145 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bf4f9f60-f5be-34a0-8c59-87776e5b2792 | -9.42594 | -48.25929 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 844e3c11-f2af-3f78-ada0-ad31d6827a16 | -8.21632 | -55.02181 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd45d955-5d07-3bd0-8c89-17ebdc3c1d81 | -7.38961 | -55.48769 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7277d865-721a-365b-bfa5-cb5d01bba917 | -7.38495 | -55.4836 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a932dad3-9ce3-342e-a430-3f8e4bc150e5 | -9.12986 | -46.0085 | 2026-08-18 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc3b27fa-8a0c-3d79-bd6a-e4001b96ea25 | -5.26953 | -49.05196 | 2026-08-18 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3092be22-1062-3f43-9d90-8125adb8a745 | -8.64806 | -43.89724 | 2026-08-18 04:38:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c7e8b3-8c7e-31ff-8c0c-b81b16695a28 | -7.81599 | -44.60543 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f313a8f7-cd99-34eb-9061-8e15562db26d | -9.07446 | -50.81717 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24e5ee2c-dc92-34ef-aea9-78c97bc83074 | -8.48973 | -44.73241 | 2026-08-18 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5e2275e-9663-38be-b750-1fbc44e9ffac | -6.10723 | -57.73795 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7111097b-d1b2-3058-9858-44367e9b4407 | -7.80855 | -44.09365 | 2026-08-18 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f889ffa4-7402-3eeb-ad9a-3e1f61536299 | -8.53111 | -54.89447 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bbfef84-f17d-3941-aa1e-e9d959a34213 | -8.55759 | -55.3167 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 174adae0-f611-36ae-94e7-5a1d815001be | -6.99694 | -59.04911 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73482197-78d5-3dd6-9ca3-27d0df6af12c | -9.82215 | -47.28155 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c07479e5-9847-308a-9902-1ae1ce8aa58c | -8.33058 | -46.4843 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1445ebd4-f730-3519-b020-7fa61aefd5fc | -5.57317 | -47.44991 | 2026-08-18 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fdf9c81-b6e8-3949-af6d-500be491c580 | -8.55413 | -55.30711 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da4a80e9-c439-3c36-b550-f6f73bbfd3c0 | -8.5321 | -54.88874 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec1d2a7c-9baa-353a-8421-e512924c381b | -6.84828 | -58.99513 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22374965-bd64-37c6-91c6-2e4c21f6a150 | -8.5735 | -54.69703 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3b5b06e-812a-32d7-836a-437894cd10f3 | -9.76145 | -46.72636 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8d68142-d853-35c7-896c-5c3f4104246b | -9.1979 | -49.96909 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e44579c-536f-36b6-ac58-c8341f213339 | -6.53151 | -43.11819 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea9dd2d1-165f-3afc-9f3a-773d79f04d0f | -7.62867 | -55.62627 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b3d4ad-483d-3d2e-b431-cb7ae4776a39 | -5.38097 | -46.55948 | 2026-08-18 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f714e8c0-5dec-3b79-9276-d273de7db958 | -9.07361 | -50.84515 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 23520e7b-6092-322a-a6a8-24539cc3d93c | -6.16556 | -47.76413 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26f71154-8f18-3432-ba68-6920648d95eb | -5.14387 | -56.28129 | 2026-08-18 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb24e69e-adf3-3fbf-baa0-31fbcc3b3c5a | -7.37336 | -55.48813 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a4d712-6638-398c-a64e-4d4a8d0c93eb | -8.48816 | -48.80537 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dcba899-e141-3d0f-8ec4-7a9ccb5db45d | -8.31784 | -46.47872 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36484a36-4de9-3fe6-84ba-c10d56f15238 | -6.53087 | -43.12242 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f6f3b9e-52ec-3b44-868d-bfbec22b9419 | -6.18291 | -47.7855 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b7874e-6778-3865-a435-f838f4a8ff7e | -9.79891 | -47.25939 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42caf54e-d498-3eaf-b5e1-f6a3b73fca3c | -3.50506 | -48.03892 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 236d0108-b2dc-346a-af31-6c5783b9f0d7 | -4.17897 | -49.39796 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dffc4641-8055-302d-912d-adb6efd8f46e | -8.21928 | -45.78975 | 2026-08-18 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de1d63ff-443d-3b5b-92a1-5fb1f4ffbe20 | -7.24225 | -49.89045 | 2026-08-18 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| b3c2950d-3dfc-364f-a8ee-09e20947d585 | -7.39074 | -55.48134 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284d6481-3381-38d2-ae0f-08fce9a875f4 | -7.6277 | -55.62611 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5a38db-2330-3ffb-b801-3efe89837439 | -4.53281 | -42.93475 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10778ed5-f0de-3593-8413-ba63cfaed9f1 | -8.5536 | -55.31002 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb637b2f-aef3-300e-b548-bdb77d272ee0 | -8.03545 | -47.27999 | 2026-08-18 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28a1a27e-e294-324e-96f2-c6c57b376732 | -6.72386 | -48.65275 | 2026-08-18 04:38:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dbb9f26-9708-3823-ba11-4a4955293cd5 | -8.02837 | -55.1286 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3d5abe4-7bee-31e4-acef-fc819d30a3e8 | -9.07819 | -50.81789 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59868868-49ac-383e-891b-c7912f7345d6 | -7.408 | -46.81832 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61e8d899-d40b-37c6-af46-e0385d019e1b | -4.48764 | -42.55551 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ba4cb720-8a0f-3dc0-8843-b41a26401a23 | -8.60032 | -50.34605 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08938aa5-541f-3708-9dcc-51b42d9850f3 | -8.56626 | -54.69289 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85a7c756-d3f0-398f-9992-dacdd649d21c | -6.10809 | -57.73326 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f08b6df-1160-30e4-a947-3b23e0d2260c | -8.60839 | -50.34296 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 51132742-2663-308c-836a-a551fc7d7d6f | -8.55362 | -47.38493 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adecce04-288d-30da-9e86-90a63b31c8e1 | -6.99667 | -46.23365 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38cbe4a8-5d22-3b21-bbf2-92b552e6f894 | -7.5698 | -55.56223 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21325dc0-c9d3-3141-bc05-be7684164f39 | -7.81254 | -44.60487 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d062e8cc-4e1e-39e0-a05c-d6b0ec9e59f3 | -8.74107 | -45.30148 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fa0ce86-8a25-3d06-b4b0-8749a7f970ae | -6.40057 | -54.93873 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f443e639-0578-397e-9d2e-9d76f606edf0 | -7.81195 | -44.60868 | 2026-08-18 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5a8eaa0-5db4-311d-a5e0-dee58d17be9e | -9.46534 | -51.60996 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12873181-6ce3-3067-bc8a-5029591d6d78 | -3.72194 | -49.82835 | 2026-08-18 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed1419f-bfdb-3c7f-baed-33b9496ce8a2 | -8.80292 | -45.78206 | 2026-08-18 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d0a0802-1ada-3d96-a494-2afb2490eccf | -3.19319 | -48.7383 | 2026-08-18 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9c79556-f163-3152-91e1-8aa6018a4147 | -7.82584 | -44.09509 | 2026-08-18 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01a59b28-f243-3653-bf7d-98badb4f68ff | -7.61178 | -55.6299 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d250834-a92e-33c6-91e3-da31596a5d8a | -6.34924 | -47.42751 | 2026-08-18 04:38:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d89339a-639f-3bee-a835-34181e049648 | -8.53009 | -54.9003 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f39bb271-22e3-3785-aa35-94be1366e6c6 | -6.2686 | -43.27897 | 2026-08-18 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b6e3888d-3068-3a13-a94b-eaa5d48f7077 | -9.40358 | -48.24819 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f23f07c3-1a3b-35af-bb99-a0eeff639519 | -7.38269 | -46.8109 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9fa76085-37c5-378c-9193-fcc2a771d852 | -8.49255 | -48.82154 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a7b2e1d2-06cc-3728-b9b5-ed673160736e | -7.17845 | -43.42153 | 2026-08-18 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e318153-a104-3fb7-9ce3-8b9408c5528a | -8.32726 | -46.48378 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f84d701-c925-3c73-bf2b-8d64ce8c9973 | -8.36695 | -46.36126 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ecdd5a4-b428-3cc6-86af-049fbccd3a4d | -6.85175 | -59.01299 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cae43484-834e-3f04-b44a-6cabef07f345 | -9.08638 | -50.81495 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc32f8a-6c4e-3552-a05f-6a0ae40026d6 | -3.42631 | -51.51131 | 2026-08-18 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aed732b-02cc-35cb-bfcb-69696b83a059 | -8.56319 | -55.31467 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
