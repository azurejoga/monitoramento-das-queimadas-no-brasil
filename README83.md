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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e03a7a07-94eb-3b52-aa3f-4a377ca13bd0 | -7.9611 | -44.275 | 2026-08-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 297.4 |
| f8a152da-d776-3c1d-a0b8-cc4759f2087f | -11.1726 | -51.2728 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d7fe1fbe-49f2-3e96-ad40-6af8cd685a89 | -13.8557 | -54.1383 | 2026-08-30 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 73d7c959-780d-3718-ae5a-330a3503ba8f | -15.4048 | -52.6437 | 2026-08-30 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 4967c7d8-640b-31ca-9321-a75c76c9d14f | -12.0921 | -47.1812 | 2026-08-30 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ced4eff1-1ec7-3a17-8bef-bcf9812b4fd6 | -7.1123 | -42.7727 | 2026-08-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 3ed7a3a8-2f18-3978-bd29-24a50f4e0567 | -4.9604 | -55.8424 | 2026-08-30 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 548.8 |
| 197cabb1-63cc-32fd-92a3-4a7c8b5d706f | -14.1459 | -52.7871 | 2026-08-30 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| c0baec6c-1f90-30a6-898a-212c0eaeada9 | -12.9216 | -45.8812 | 2026-08-30 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 9a3dcf0f-aae1-38b1-806c-a62d2fa665e1 | -14.2989 | -51.7072 | 2026-08-30 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 3fb1fc38-b300-3c24-8842-af5ffbb140ed | -14.7601 | -48.7467 | 2026-08-30 14:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 53dfa3d1-0eae-3edd-8d83-cc3259bd27b4 | -10.7647 | -50.6579 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| cd4ee473-6f17-386c-8d31-1f68f959c004 | -10.8653 | -50.2203 | 2026-08-30 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 666e70cf-cdb1-3a30-b686-1e0ca1adf4e9 | -14.4004 | -52.5438 | 2026-08-30 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| a90cb31b-fda6-35e9-9248-1c35febfb774 | -6.8568 | -59.4757 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 266.5 |
| fc00dbb9-1245-331d-b327-e9046a3a233b | -11.2638 | -45.3241 | 2026-08-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0bef8298-e7c0-329e-999c-3387a01872dd | -11.1534 | -51.296 | 2026-08-30 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 66fc8321-2eee-3d17-8f53-213f76d4398e | -7.3117 | -60.6089 | 2026-08-30 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 509eb398-5769-3934-816c-ae2cb5e2f8e1 | -11.2506 | -53.9941 | 2026-08-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 454bdd8f-fa84-318e-897e-32a99a1c2ea3 | -13.4135 | -51.7571 | 2026-08-30 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bcf4cdd7-1cad-3164-bd88-80725b908aeb | -7.2933 | -60.5905 | 2026-08-30 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5d759d6e-f87f-37f0-931b-a676d78c7b96 | -10.7431 | -50.8514 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1ee3f401-565a-3c82-bac9-3c59e0f88f9c | -14.4004 | -52.5438 | 2026-08-30 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3fd235bb-46ab-3ad9-aff3-eadfeb016480 | -9.0673 | -64.2548 | 2026-08-30 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0ee388af-632a-31c5-a8b9-e72d17afa9cd | -13.8752 | -54.1153 | 2026-08-30 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 16d63124-1b4c-3f81-a9ec-83cc3d713daf | -10.7615 | -50.892 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e29eb3c2-4fc8-384b-b443-0ed4fc16bc3e | -11.1723 | -51.294 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| bb2df9f5-2941-324d-bed2-e8b243d2635e | -7.1312 | -42.7708 | 2026-08-30 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 207.1 |
| e4b7c779-2494-350b-ba0a-4c3309873e7e | -13.2092 | -51.3569 | 2026-08-30 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| cf7eb145-9cc0-3ab3-9f68-cf0eedb2ed8e | -3.6216 | -60.547 | 2026-08-30 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| bdd37078-4a73-39cb-bcf3-178183a5131b | -8.5925 | -66.9564 | 2026-08-30 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b900f638-bffb-3b60-a00e-a47c86fe27be | -9.8927 | -60.2752 | 2026-08-30 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a415a26a-4474-349e-a976-a28584d71014 | -15.4048 | -52.6437 | 2026-08-30 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 17099c59-87d5-3865-9f3a-0a8fbb7e73c6 | -9.1532 | -59.5221 | 2026-08-30 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b6535b85-3311-3f65-a81f-4c9ffe8cd831 | -13.8381 | -54.0365 | 2026-08-30 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 87f87460-89b6-3d15-8b8c-d2e2189f0e7a | -14.1456 | -52.8082 | 2026-08-30 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 15511919-3d82-3ee3-a1af-33c750aae55c | -12.0921 | -47.1812 | 2026-08-30 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 82394c7f-10aa-307a-b738-28af7475bc55 | -6.8799 | -41.6754 | 2026-08-30 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| d5dfd8e5-b434-3cc4-87b6-f576e4c79375 | -3.6398 | -60.5656 | 2026-08-30 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 42341b1c-f699-3111-bcb7-081c718003c3 | -6.7699 | -55.6644 | 2026-08-30 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 31735b3b-5d2c-3a64-9ad0-9de50361c089 | -6.861 | -41.6772 | 2026-08-30 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 457.9 |
| 4001f5ce-c454-3adf-be5c-6ec27e3a8a6c | -7.9907 | -46.5177 | 2026-08-30 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 23704476-4601-35a9-8144-96135215358d | -9.1533 | -59.5027 | 2026-08-30 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b4198817-9c50-3e74-9ad2-39430e6ec772 | -11.1726 | -51.2728 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5ca7ea82-59a7-3ebf-a70c-337c802b81ec | -14.4197 | -52.5413 | 2026-08-30 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 5e2ee02f-4d38-3a6c-8622-bb2493529a6c | -6.8802 | -41.6513 | 2026-08-30 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| c9e13680-756b-31ba-bfa6-22312a05708c | -8.1534 | -45.4904 | 2026-08-30 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 71f995f2-8c58-3669-8bbc-9302193d0657 | -16.2735 | -42.5653 | 2026-08-30 14:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 95fc146b-65df-3fab-a68d-131344ab2f56 | -11.3427 | -45.1751 | 2026-08-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 349fd79e-0e1e-3fb3-a07e-133b6164d48b | -4.9604 | -55.8424 | 2026-08-30 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 597.0 |
| bb4352ca-561a-3443-80aa-f3c85ebcc79b | -11.2503 | -54.0146 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 178.9 |
| fd7e59ad-c599-36d1-ac7b-88b131236d2f | -13.8749 | -54.1361 | 2026-08-30 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| c18bc22b-05e2-305b-86ed-87a1f8e5716d | -10.8653 | -50.2203 | 2026-08-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 74252f37-4c72-3563-9fde-eb3508c07118 | -6.8569 | -59.4564 | 2026-08-30 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 14941db5-5a5b-3659-8071-dff4830e4634 | -8.3158 | -47.6383 | 2026-08-30 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 00349784-6718-3bfe-8f0f-c76b42ee11a7 | -9.7832 | -46.4202 | 2026-08-30 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 290.1 |
| f2427ceb-48a8-387a-a762-1f4ca4ea9fdf | -3.6215 | -60.566 | 2026-08-30 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4602a44a-478b-302b-991d-609b3a4c2646 | -10.8235 | -50.5026 | 2026-08-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| cacd05ca-eb65-375e-8e49-e41e7ac66758 | -10.7407 | -54.0401 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| dc5fbcb5-f705-34bb-849b-24b5c0bb8e4c | -8.5969 | -54.7755 | 2026-08-30 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d69c85ed-6bdb-30ff-9bc3-1fb7bf8fb263 | -11.0057 | -49.6677 | 2026-08-30 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| dc1d419d-b08e-343b-a1f6-119cd649fbde | -10.1538 | -45.6982 | 2026-08-30 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f870610a-4dfa-3e56-a61b-78cd90a5e909 | -7.991 | -46.4954 | 2026-08-30 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| ed28fd85-646a-3f85-830f-7a11adca5946 | -9.1719 | -59.5017 | 2026-08-30 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b918fe73-a35d-3392-a05d-3eedb0b51e98 | -6.8613 | -41.6532 | 2026-08-30 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 257.5 |
| cdf7fdf1-c0c1-397a-89f8-b3d0f92444ca | -11.2294 | -45.099 | 2026-08-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4a804520-3a48-3ffd-98c7-9ca0715a16dc | -13.2287 | -51.3332 | 2026-08-30 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2cf5aeb9-e9a7-3157-95b0-a9f4c66fc1f6 | -7.5272 | -44.3413 | 2026-08-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c92a45f6-d340-3bd8-b6a5-01728c923d34 | -6.9361 | -55.7157 | 2026-08-30 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| cd2c3edc-74fc-3079-92f6-b32821935f74 | -6.8568 | -59.4757 | 2026-08-30 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 291.9 |
| 1c801630-1f30-3e91-81a4-efe36aa4583c | -7.546 | -44.3395 | 2026-08-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 2e3edf5b-6d81-357e-8d61-8d6f60f9dd1b | -3.2361 | -61.2548 | 2026-08-30 14:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 430677d9-de42-3d1d-8430-5dfe0f20a14e | -13.3412 | -51.4896 | 2026-08-30 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 0357e6ad-b887-3f4e-a6bd-be3f73bd5429 | -14.1459 | -52.7871 | 2026-08-30 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fbb10868-d1f6-3001-804b-f5ebe2606515 | -4.9605 | -55.8226 | 2026-08-30 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a963b3a0-a817-3db8-a93a-d6ac61a5a55e | -5.4876 | -57.1416 | 2026-08-30 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3358b321-c824-36c1-bba5-20bac257a4cd | -14.4193 | -52.5625 | 2026-08-30 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| c256130b-6144-3b6e-8b1e-21bf8bce96b7 | -3.6399 | -60.5466 | 2026-08-30 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e23fd609-8735-3e5e-8641-e1c6a0a2392a | -7.1123 | -42.7727 | 2026-08-30 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |
| cb162c4f-1b40-3ec3-89f3-e9389fb9b832 | -7.4949 | -55.3462 | 2026-08-30 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8373c587-b1b2-36e3-a93e-ef65a6cbfa78 | -13.856 | -54.1175 | 2026-08-30 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 151.2 |
| c5c1f10e-1d8f-35d3-a8c5-f4826d449d11 | -10.8915 | -51.0693 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4938ad6a-6ce2-38e1-83ce-8f24cd0745f3 | -11.2317 | -53.9958 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 260cc6f7-1314-3eb6-bf63-e1292b3a7a29 | -10.7618 | -50.8707 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 41265e47-ce5e-397a-944c-89ff6402e5ef | -10.7434 | -50.8302 | 2026-08-30 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| db3ba345-16ee-3c01-9c6b-da428cfe90a3 | -10.937 | -50.5118 | 2026-08-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 7c474083-7789-35d0-99f8-c75e8c29cf5a | -10.8539 | -54.0301 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e98cad96-069e-35bc-8742-3eed936a39d1 | -11.1349 | -49.9117 | 2026-08-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0d6f7bae-8f56-31e5-83fb-57eb5a569c7a | -8.9739 | -50.8078 | 2026-08-30 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 652935d0-e312-3387-af50-8eb9971240ef | -7.5323 | -55.3041 | 2026-08-30 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f4ba2b65-08e5-3ea0-9682-ec209f20132d | -7.5644 | -49.5857 | 2026-08-30 14:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| f91c50d2-5a03-3770-b9b1-7327c200dd6f | -13.3604 | -51.4872 | 2026-08-30 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ab568525-2c62-3cb0-85df-73888c960189 | -11.2443 | -45.3497 | 2026-08-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 368.3 |
| 0b5c3891-ff3b-3344-83d2-506b6d0a1151 | -11.0054 | -49.6893 | 2026-08-30 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 26ce2680-9fa4-3a19-baae-d4c014d1b7b0 | -7.5477 | -61.3247 | 2026-08-30 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2c298d3c-4ecb-3f91-b9f8-fead2da6a9ab | -14.7605 | -48.7245 | 2026-08-30 14:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| babba821-86b7-35bd-bded-9d5d2b55de7a | -11.3619 | -45.1724 | 2026-08-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 17685109-c321-3493-b771-d45b8ae344ec | -11.2506 | -53.9941 | 2026-08-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 193dfc37-4e28-3aee-aef8-0c8c0874db1c | -15.2283 | -57.6517 | 2026-08-30 14:10:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5301686c-9247-308d-8c8a-39ce9e171e59 | -11.2446 | -45.3267 | 2026-08-30 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |


[Clique aqui para ver as próximas entradas](README84.md)
