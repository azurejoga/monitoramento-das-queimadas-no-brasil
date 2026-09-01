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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 436383e6-7963-340f-8b38-95a8fb3207fb | -9.5238 | -65.7008 | 2026-09-01 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 56352d69-952b-397a-b286-d951812b8981 | -5.9451 | -57.6906 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 05a4381b-2620-3657-9692-bcff3d163c66 | -3.1266 | -61.2188 | 2026-09-01 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 0f354d24-e0b9-30b3-bbb7-914dc665fd37 | -7.5526 | -60.4651 | 2026-09-01 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 68a15e88-fb03-3a57-b1e6-64ac267a9d4d | -5.9452 | -57.6711 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8f6593ac-0a2d-3dbe-8f75-0502bbbfb962 | -13.9477 | -54.3971 | 2026-09-01 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 38c2ab2f-d378-3c50-9487-75c76934b5ac | -8.3717 | -62.716 | 2026-09-01 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f7c5aa3a-ce37-379b-a20b-be1b4ff20dd4 | -7.2536 | -61.1074 | 2026-09-01 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d8286a31-ffa5-3ad8-8890-e374afb3e778 | -8.7803 | -62.5103 | 2026-09-01 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0000b986-0a33-34bb-adc3-d88788d651f8 | -9.6776 | -55.082 | 2026-09-01 16:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 25776ab5-0f46-3a81-941e-edc9baa8ee88 | -8.2043 | -54.9423 | 2026-09-01 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 06bb9ecd-34a3-32aa-a1bf-7d3cdab5a25f | -11.2767 | -50.6029 | 2026-09-01 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 641f88dd-bf1d-3c46-a914-ec639e2d9796 | -6.8357 | -59.9571 | 2026-09-01 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 97b70f7d-042f-33df-872b-7dd84870dfea | -4.181 | -63.1543 | 2026-09-01 16:00:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 7b1c0f1d-6a2a-378a-9074-25db6f84001d | -14.481 | -53.5018 | 2026-09-01 16:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 0a7590b7-c30f-32c8-a7b0-8a46eab37ec5 | -6.9872 | -59.2582 | 2026-09-01 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 56b7f998-b5ff-3411-8b6a-f2e474dcc215 | -10.3205 | -49.9567 | 2026-09-01 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| f474c224-25cb-3965-944d-bd9557daa318 | -8.8758 | -71.4622 | 2026-09-01 16:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 47.6 |
| da10bd47-fcf3-317c-b2c5-bb04b086b772 | -3.4185 | -61.3461 | 2026-09-01 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c58d6128-690d-3f59-9182-346a5db0597e | -6.1659 | -57.7403 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cf2a284c-95d1-3cb1-9a0f-ec2336afd48c | -7.5475 | -61.3627 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5f29e612-1353-3f1d-aedb-f15c566bdaac | -10.8017 | -50.7178 | 2026-09-01 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 64e96b04-cfa0-3239-92ec-e8ea94f84866 | -6.1845 | -57.72 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9409d3cb-c201-3c15-9898-2776c711ba2d | -5.9636 | -57.6704 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 067d74fb-044f-365a-87be-8acaeab20a5e | -9.5424 | -65.7002 | 2026-09-01 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 22fde86c-31c1-3820-b639-79194c8c9272 | -7.5659 | -61.362 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 30ec5124-7cf6-3b59-bc85-980d8e0be89d | -10.7271 | -50.6405 | 2026-09-01 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f650aa53-cf99-3ac3-bac3-ccd9208edaf9 | -8.7804 | -62.4913 | 2026-09-01 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8a887e27-7a3e-36f7-9dd1-bf4930c30fcc | -6.369 | -54.7655 | 2026-09-01 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c64ff606-24c2-3709-a528-de0c58794a75 | -12.9032 | -45.8382 | 2026-09-01 16:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.5 |
| dbd8944f-00fa-37ff-b41f-f914d9ae526a | -6.7813 | -59.7864 | 2026-09-01 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ce75d0e6-7bc4-35cc-90dd-d0fb8ee33ccc | -3.2623 | -58.2367 | 2026-09-01 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 9eb81bac-dc28-3070-b399-3d1c96c6da5a | -11.2767 | -50.6029 | 2026-09-01 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7228643a-920e-39a8-a3a1-83c04ed49665 | -13.4516 | -57.0592 | 2026-09-01 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 2cfca96f-8a57-3850-a166-8367931f1d3e | -6.9113 | -59.6275 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b3745d57-9d7c-3783-80f5-5882b318bd4d | -8.5966 | -54.8159 | 2026-09-01 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 751096a3-4d15-3ac0-b0e1-8c800cada802 | -11.175 | -54.001 | 2026-09-01 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c2e1be8b-1562-3349-84ac-4f2c372d5875 | -7.2006 | -60.6706 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 358.1 |
| 8f48e228-ef0d-319d-abc9-f0e28b27c3ef | -7.1822 | -60.6713 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4372a7d6-5fc8-3397-bf93-0c45bda16adc | -6.369 | -54.7655 | 2026-09-01 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e6ed7949-1a68-3651-92ae-455fb8191cb5 | -5.9636 | -57.6704 | 2026-09-01 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 84bd3b1a-1c31-3358-9a7f-c25aaa3a854f | -8.7804 | -62.4913 | 2026-09-01 16:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| caec0363-3e2b-39c2-a94e-6dff97f9f19c | -5.9452 | -57.6711 | 2026-09-01 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 871f5d8e-3ddd-395e-a0af-0339e224b594 | -5.5649 | -60.193 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 344.9 |
| b1e9236d-a971-3295-822d-911991a29323 | -6.9482 | -59.626 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 02a12e4a-8f87-3b80-8c6c-430c28849f93 | -9.0802 | -65.3789 | 2026-09-01 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 912466f3-7ad6-3fa7-bf66-676c203642fc | -3.1998 | -61.161 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6a2291d7-7fce-3ecc-a947-8ad08a1064f0 | -6.9515 | -59.0473 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 22d61c68-b0e6-31d8-8e28-b81f3b835268 | -3.1266 | -61.2188 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 3d88bf73-7abd-39e2-84f3-68dd622dd125 | -7.0243 | -59.2181 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d6a5ad3c-e764-375b-bdf2-70dd831d20bd | -11.2954 | -50.6222 | 2026-09-01 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 79233cfc-1a5a-3833-b485-e118b4992f51 | -7.2934 | -60.5713 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d053c24e-2e36-3426-87da-7d0d534505bc | -8.6556 | -70.677 | 2026-09-01 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2d73761e-5f9b-3cee-ab63-f585bf206650 | -6.9112 | -59.6467 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 338699e0-f49a-33bc-9e53-34588b30c4cc | -3.1267 | -61.1811 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e0846463-4108-369c-b6d9-2b717cb6b8de | -7.5847 | -61.3042 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9a173eef-2b20-377e-b5f3-42d6589a13c7 | -11.0247 | -49.6656 | 2026-09-01 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 351dc373-50e6-304f-a189-4854f69ef432 | -9.5238 | -65.7008 | 2026-09-01 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 15500143-fefe-38e0-b4bc-c45c97c2d9c6 | -6.7513 | -55.6853 | 2026-09-01 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9fee60a2-6f84-3dc4-bec8-c14d9469334e | -7.529 | -61.3635 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| aa037ce7-7b97-36a6-9dd9-8ae480857aa1 | -15.1827 | -46.2336 | 2026-09-01 16:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 6a6f335e-5cf5-3097-b2a4-e6cecbf4ffb9 | -11.2391 | -50.5857 | 2026-09-01 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a0e220ef-a6b3-3818-b664-0fa417a887e8 | -3.4185 | -61.3273 | 2026-09-01 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6e35136e-73ec-3a93-bda2-c2f8c90b5022 | -7.5104 | -61.3832 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 77a42482-4262-3031-8a9b-0368e3624606 | -7.5475 | -61.3627 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7386b516-efff-39c4-82de-fab10bc9cb62 | -3.4185 | -61.3461 | 2026-09-01 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cc3f7ce7-980c-37f9-b44b-3046c90b2907 | -14.6535 | -53.5642 | 2026-09-01 16:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 75cf0a2e-75e1-39a3-906b-644f1c951d78 | -10.4961 | -59.6195 | 2026-09-01 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c81a19f9-0059-349b-b8e0-486781ad0964 | -5.565 | -60.1739 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 992bbaa8-13b8-3d5f-bc1f-a2f61e2613d9 | -6.7514 | -55.6654 | 2026-09-01 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9783a68a-9100-37f6-b454-c729ba94770d | -6.77 | -55.6445 | 2026-09-01 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2d25a477-d81f-37d3-8421-a736cca746fe | -5.9451 | -57.6906 | 2026-09-01 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 36712474-d025-32fd-b06e-d397613860f4 | -11.0744 | -51.5365 | 2026-09-01 16:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 16c11745-a605-3f18-aac7-25c62c36ce3b | -7.77 | -61.2015 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 905aa211-d02c-3c53-9b16-1d87a4145d43 | -3.1083 | -61.238 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| b73b6fb8-a0a4-35f5-99ff-e99c54f50d3a | -6.861 | -41.6772 | 2026-09-01 16:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| c1ad8de8-a1fc-3de3-acb0-ea0a6f580ca8 | -14.6732 | -53.5408 | 2026-09-01 16:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 6be47cdb-fc53-35eb-a661-c7a440487eae | -9.6776 | -55.082 | 2026-09-01 16:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c396a129-5783-34dc-8b1b-1f96e4c94952 | -7.5289 | -61.3825 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 4c2dd096-2de4-3d7f-ac8d-134e2c98c314 | -3.1083 | -61.2191 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| d7bfc018-5126-3108-abc0-541397969a61 | -8.631 | -66.5473 | 2026-09-01 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 199fa143-5300-3ced-8e0f-487122e86272 | -8.8954 | -70.8571 | 2026-09-01 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 41.5 |
| c2bf50e0-ed08-382e-9a5e-600187578054 | -6.6233 | -58.383 | 2026-09-01 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| dc09100d-8e1f-3c9a-b469-c78fa19e2910 | -5.8537 | -57.5576 | 2026-09-01 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7ee0afa9-e14d-3882-9a45-9aba05120eb8 | -6.3875 | -54.7646 | 2026-09-01 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 56751777-1667-3b70-ac66-30c806547f67 | -7.5526 | -60.4651 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6f134ea1-1258-3881-a99c-08a7352d859c | -7.3488 | -60.5691 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8b6b1256-e633-33ea-82d3-afefad939e6c | -6.8009 | -59.5742 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 30d00077-31c6-3812-8df5-be2322f8cc8f | -7.4549 | -61.4044 | 2026-09-01 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e4ed37e5-d4bf-3f98-94a5-6c3b35ea086d | -8.9242 | -63.2804 | 2026-09-01 16:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 36c9d07d-4c81-355f-b956-72dc0764749c | -7.5711 | -60.4452 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 7f91339e-c27b-30cd-8731-e24ac3b2c418 | -3.1449 | -61.1808 | 2026-09-01 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1fec8ef5-d35d-3ced-922d-940aaf8b4eea | -11.2957 | -50.6008 | 2026-09-01 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| b8e59099-cf6f-3ecb-ac7d-8b2af1e633c1 | -3.4002 | -61.3276 | 2026-09-01 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 713e89b1-a078-3784-8fb5-cb4034eacafa | -6.641 | -58.4987 | 2026-09-01 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5d4297d6-67a8-3ac2-a7d6-e3d8db66d359 | -8.9428 | -63.2797 | 2026-09-01 16:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b48a493f-11e6-3b4e-b159-5cb7c4c7b12a | -6.7123 | -58.9412 | 2026-09-01 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 76c57c26-f8d9-3316-b379-7b059dccb93b | -7.7515 | -61.2023 | 2026-09-01 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a2e9bee2-de6c-364a-a666-62ee75bc0f47 | -14.81 | -41.71 | 2026-09-01 16:15:00 | MSG-03 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 54309422-50af-3e63-95b7-687fa9230c5f | -3.84 | -44.07 | 2026-09-01 16:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README111.md)
