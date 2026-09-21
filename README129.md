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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9ff3cff-4416-39eb-86d8-e6282fd99e4e | -10.4099 | -50.3324 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d2accfd8-6eff-3f2f-aaf6-41a9fb4ea401 | -6.3383 | -59.9374 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1fa9231f-e13c-3b41-a0af-e4488201563b | -13.0357 | -46.9775 | 2026-09-21 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 95dd3ed0-5006-337f-89de-f1ea935b1c50 | -11.8014 | -49.8129 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| d5d94d1f-e0df-3013-890f-94fb83cc7f06 | -5.9151 | -59.9522 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d78140e3-0d44-31fd-9139-80d72d5ff866 | -10.8921 | -53.9857 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6747ba10-9e64-3109-92aa-43de43b9f718 | -8.1876 | -54.7219 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 055c8096-68d4-3496-866f-fcec50bb6df0 | -10.3914 | -48.9133 | 2026-09-21 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 83c7f1c0-887f-307f-8085-9a18a05073f7 | -6.8058 | -55.8217 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e73a3d5d-4f93-3f03-b921-5578a9fb08af | -5.6221 | -43.3934 | 2026-09-21 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 340.7 |
| 4824e049-f2c5-371a-8960-912101cf0482 | -10.0898 | -50.2795 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 442132d3-7da7-370f-8362-628442c3b5b7 | -3.584 | -40.3264 | 2026-09-21 14:30:00 | GOES-19 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 2ea2c877-4603-3178-8747-b655817800d4 | -5.841 | -53.5205 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 26d75e55-e30e-31ec-9d1d-2c3d413cc30b | -9.5594 | -66.0359 | 2026-09-21 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 739e286d-182e-33fb-9988-2fe8328e2a36 | -11.6802 | -43.4209 | 2026-09-21 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 26ddc186-5211-3d42-965a-c49a5e27e44a | -8.1874 | -54.742 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 902d4dab-8871-39e2-b9d7-4ae2f1ea3666 | -7.5477 | -61.3247 | 2026-09-21 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bf94b0a1-37e8-3ba8-9950-8714428b4f04 | -6.4741 | -48.441 | 2026-09-21 14:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 4ba0a6ba-b706-317c-83e9-4ab4fb45b040 | -3.6632 | -58.8643 | 2026-09-21 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| c690ac13-2492-3f96-9b3a-2f9e26d66912 | -6.8468 | -55.2617 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 86578655-f4b2-309b-90af-064bb7d1f2c8 | -8.3167 | -45.9934 | 2026-09-21 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 327900b5-0128-371f-99d3-cc4b369a0110 | -11.0221 | -54.1584 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3b3e8f7d-3d14-3577-b150-731a2e50435e | -10.4486 | -50.2644 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 774a65c7-3f67-3591-9add-7307f3810437 | -12.8899 | -50.9695 | 2026-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 17540e48-4a44-3306-b1fc-ee39234c90d3 | -10.8911 | -54.0677 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 56e58aa7-06b0-3f38-a555-afd60dc6099b | -6.8448 | -55.5411 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| cead1c13-fa80-3b9a-b208-9f167063d7ce | -6.9223 | -42.9323 | 2026-09-21 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| b3b5d61c-d886-3344-a3dd-9cab5f2df280 | -6.9034 | -42.9341 | 2026-09-21 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| b4201da2-934a-3867-94cf-1b1106207c20 | -9.5593 | -66.0545 | 2026-09-21 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5b82a7e0-60de-3add-aba6-73b3d572e2b7 | -5.8225 | -53.5214 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e8f054f2-ccbe-3a3a-8d1b-f11162391882 | -6.392 | -45.1948 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 40ec4f1e-2438-3e4f-83c8-1ce85bfb187e | -10.9544 | -50.6165 | 2026-09-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7efcba08-cf36-352f-b115-0d25e38ae873 | -8.1872 | -54.7622 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8293313c-895a-309a-93f0-65caa1ab1d37 | -3.3823 | -50.4486 | 2026-09-21 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4896fbd9-1945-347f-a9a5-27ccbf462a94 | -11.4718 | -47.7538 | 2026-09-21 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bd391069-1c64-3ee7-a511-904f2cb035a3 | -3.3267 | -42.7606 | 2026-09-21 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| add6f275-69d5-3c9d-8a99-c5a7d15e7ca4 | -2.2619 | -48.7445 | 2026-09-21 14:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 25272773-2d5c-3c59-9fab-18b570c66d82 | -11.8168 | -50.0482 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7f409839-566d-3ca2-ac13-c63751907c7a | -7.3291 | -55.1955 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| af9ac3c6-37f2-370e-b31d-ce4e6427a81c | -3.6947 | -60.5645 | 2026-09-21 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| abfccc5d-7c93-374c-9e5a-d63e43b4b540 | -6.5759 | -45.5419 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| a01d5fd8-a0d5-37c3-8ddd-172559a56f93 | -10.8011 | -50.7604 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| cd81872a-3caf-3be9-bbd9-14c1670a93f5 | -11.9967 | -58.0821 | 2026-09-21 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 010ae43e-6aa5-368e-b7e5-3a84ae8c1b62 | -7.4283 | -44.7639 | 2026-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| db0e45fe-eac0-34f8-a97d-57106cae331e | -5.9334 | -59.9707 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 2909227e-f210-35a8-8d64-6167f25dece2 | -7.4286 | -44.7409 | 2026-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 71e10802-3d0b-3dad-b3ca-d979d1cabc1b | -10.7652 | -50.6153 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 978f42e6-d812-350b-b4ab-3345a2e03307 | -5.7692 | -43.7077 | 2026-09-21 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| d61a1ca3-b1fd-383d-a6b9-e443f5c41da0 | -6.815 | -47.8953 | 2026-09-21 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7307665c-eafe-3943-8043-12137190eba7 | -10.8909 | -54.0882 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 06e55f2b-72bd-301c-957c-f8135b278070 | -11.7823 | -49.8152 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e9bf172e-8483-3b36-bad3-e3141ee5c8d5 | -2.9157 | -57.7983 | 2026-09-21 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8a026572-d10e-3e8d-8d62-137367de0750 | -6.6763 | -50.9172 | 2026-09-21 14:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ec9c31f1-e271-31f2-87fe-5792439f7a27 | -10.7521 | -46.3252 | 2026-09-21 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 247.8 |
| aeb444a3-de59-3015-a4f4-2bfd6228cb77 | -6.8264 | -55.5222 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 523d569f-b487-3c2e-9699-f3b31545aedd | -2.8608 | -57.8188 | 2026-09-21 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 26f6bbf3-e908-3c22-873a-90d430fdb33a | -9.9448 | -45.7238 | 2026-09-21 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 03afafd5-9479-357c-8af5-2a4c5978a062 | -10.4917 | -51.3001 | 2026-09-21 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f73af5ce-acc1-39dc-8723-42af6857a0d7 | -12.9091 | -50.9672 | 2026-09-21 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 95493ce8-7784-360c-b865-c5f8cc7cb5b7 | -7.3289 | -55.2155 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f8dbd3e6-c517-3038-9c89-b7b3dc42a370 | -6.3197 | -59.9764 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4051dc09-aa46-310f-aea6-9833c1466b06 | -6.3198 | -59.9572 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ba802ed3-3222-3ed5-83ba-90d4428261bb | -6.0196 | -51.7893 | 2026-09-21 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 93aece5e-aeac-3a1f-a138-ff76dadc62c9 | -12.026 | -50.0663 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 070bc928-df52-36f6-8202-bfab60a84f44 | -8.0466 | -61.3237 | 2026-09-21 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 60e72295-146a-3f21-94ea-a8ac4362984e | -9.2756 | -46.2077 | 2026-09-21 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8f8bce56-71c5-3479-adb4-6f0a76554dd8 | -6.0033 | -44.7247 | 2026-09-21 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 143d7392-5229-398e-aad6-3d75746a5d5c | -9.0239 | -48.1622 | 2026-09-21 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 76c9b83e-8186-36d2-9f1e-105675d573cc | -6.8263 | -55.5421 | 2026-09-21 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 32326b47-d392-3544-b1bd-1da069494a5b | -12.0451 | -50.064 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 780799a3-5eda-3a8b-b5cf-4ad6040e20b1 | -8.4922 | -47.0257 | 2026-09-21 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cc840c55-9f56-3a8e-b5f8-7032a7ceab74 | -9.4564 | -45.4406 | 2026-09-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d4d13b30-ad66-3451-9907-8fd304088391 | -10.2793 | -50.2177 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ec496888-56f3-30b3-9029-d984c4513cf2 | -10.7999 | -50.8455 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 00a16180-c878-32bb-ae99-8aabd87d9865 | -8.0094 | -61.3633 | 2026-09-21 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9580c5dd-d333-367a-9860-c4ebd2e0f3c7 | -11.0804 | -49.7456 | 2026-09-21 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| daed75a5-76c6-3a48-aff1-1e7755e97f13 | -10.3725 | -48.9153 | 2026-09-21 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0f8dda14-b496-3111-b704-fa5319090d51 | -8.7914 | -48.7285 | 2026-09-21 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6e66376e-72d3-3dfa-8ff3-ba180be06cdb | -9.043 | -48.1384 | 2026-09-21 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 27373488-2df7-3ade-ae52-c9b2efb92f7d | -13.2596 | -51.7973 | 2026-09-21 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| f05b380f-6c0e-3e8b-98b4-1cf885432837 | -8.7706 | -45.8567 | 2026-09-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 321f17b3-e1fd-316d-abd5-530ea210b46c | -7.4092 | -44.7885 | 2026-09-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 06f7c3c1-d79c-348d-95c8-c441f9fcc895 | -10.911 | -53.984 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9f3bb084-e59c-305f-80fe-10f9d6c45778 | -16.9964 | -56.4525 | 2026-09-21 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 38c09af1-f39f-3a6b-859b-0e1f4dac3152 | -15.4471 | -48.4566 | 2026-09-21 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8a1c5369-2a09-3b61-8118-e4e30327c0d8 | -12.3025 | -50.6774 | 2026-09-21 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 196.8 |
| bee0087b-7c1c-3c65-bfc8-63a4e53cdc0b | -12.5231 | -50.0051 | 2026-09-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9cb0d70d-ae3c-3c9a-a356-671bef6eee24 | -7.5889 | -57.6757 | 2026-09-21 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6653f588-26d6-3ada-8fe2-2c0e4d7a3ed1 | -14.1815 | -51.808 | 2026-09-21 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| ad12144d-2c3f-3a79-a264-c9980bc1060c | -5.6781 | -43.4125 | 2026-09-21 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a42d7997-2974-3913-b0e9-d06e0b3dde56 | -3.3453 | -42.7832 | 2026-09-21 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| fb6c7726-ae03-394d-8cf6-d5bf080dc4ba | -5.4378 | -47.6178 | 2026-09-21 14:30:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 74030d09-aaf9-38e1-b531-660da1f8a716 | -8.7912 | -44.301 | 2026-09-21 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 265.4 |
| a226a603-f0d9-3702-b672-f9ec21e7cad7 | -5.7504 | -43.7091 | 2026-09-21 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 01503262-abeb-303b-9821-11c7f47da63e | -10.2979 | -50.2372 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 62322148-83fe-3098-98d6-10fe522459a7 | -4.2239 | -48.6127 | 2026-09-21 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d968c19e-f495-395d-801e-ee87e300120a | -8.1871 | -54.7824 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e8fd23c4-5672-3454-95ef-6d9dc51d908a | -9.0428 | -48.1603 | 2026-09-21 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 71f5ae59-b83d-39f2-92bd-f3791f623c64 | -3.3454 | -42.7597 | 2026-09-21 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 177.4 |
| f9a5de65-0f7a-3e79-aaf5-da30777aebeb | -11.8362 | -50.0244 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |


[Clique aqui para ver as próximas entradas](README130.md)
