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

## Dados Diários - Página 246

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f1fe433-6daf-3c02-b2f9-d2b38524b035 | -12.2504 | -44.7631 | 2026-10-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 0a0e9b3a-596c-3ff1-9219-d94d24c9d96b | -6.755 | -55.1465 | 2026-10-09 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2bd0ee70-1328-39e9-b6d9-45d709208d78 | -12.0054 | -43.4878 | 2026-10-09 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |
| a7645e6d-86f9-34d6-9d93-5792b6a1bbb2 | -12.2145 | -44.6291 | 2026-10-09 14:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 82e5c663-8ebc-3e9e-ba14-2abb892b87ef | -2.0447 | -54.3085 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7a0972f5-84a6-3d40-9885-9b5f061bbd3f | -3.86 | -44.1274 | 2026-10-09 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ce9adef6-1ee3-37e6-9309-4d33adca2675 | -8.911 | -45.229 | 2026-10-09 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 27e94f52-6e59-3d88-a5b8-6cd3bff5576e | -10.9533 | -50.7018 | 2026-10-09 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4b0c42be-a30a-37a7-910d-cde67ff8aaa2 | -1.1094 | -54.1802 | 2026-10-09 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4ea6a58e-83ce-3a8a-b2f4-a33634fe7048 | -14.3415 | -55.0341 | 2026-10-09 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6b6d03a3-b07a-344f-bf47-39ac8ac069fc | -1.494 | -54.5363 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d95527e1-6dbf-30ee-839b-0ccf49addc75 | -1.3447 | -56.3979 | 2026-10-09 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f1da0d7b-5aba-3a41-9f50-4e6b39e6263d | -2.4623 | -56.0682 | 2026-10-09 14:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0a5426ad-60ec-3730-adf3-31a3dc2c42a5 | -1.3264 | -56.398 | 2026-10-09 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4b0b2c2b-6b52-386d-8e3e-45fe4858c1dd | -2.8712 | -54.192 | 2026-10-09 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e0995d5f-964b-392e-883d-24968aaca61a | -8.2823 | -45.7264 | 2026-10-09 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 241bfc1c-d045-33c9-b34d-da3e5ecef871 | -9.9208 | -44.7893 | 2026-10-09 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 4bee2cb3-fb68-34c7-b67a-d2e9ae8edf2f | -2.7613 | -54.0941 | 2026-10-09 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 0b7b0132-2416-3afd-8808-25945bdd5e06 | -1.1094 | -54.1601 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 901f53ab-f2e2-39e7-8116-1b3c84e8d8ce | 4.2067 | -60.6106 | 2026-10-09 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 59b510ed-b4fa-3d89-958b-1f1f0b8f0723 | -11.7674 | -44.9522 | 2026-10-09 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 12ddf25d-21d8-3385-b4fb-69ddd9cfd470 | -12.0251 | -43.4609 | 2026-10-09 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 9379be85-a0cc-39c2-8d77-701a3d8e526e | -1.3829 | -55.2142 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| b463b4d7-0afe-3577-9067-be350bec5938 | -15.2535 | -42.3741 | 2026-10-09 14:50:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 766.1 |
| d8f541ca-d312-3f40-8d85-8ec4a8ebe98f | -11.0758 | -44.0299 | 2026-10-09 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 487.8 |
| 338420a5-dbbc-3d20-99f8-c1155a5982de | -11.2068 | -45.3091 | 2026-10-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 5cde329f-34f9-36fe-bb9c-a9d21ebcd3a3 | -2.8306 | -49.8768 | 2026-10-09 14:50:00 | GOES-19 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 32c72345-10f5-3494-883e-f97eae8be1db | -1.4569 | -54.7761 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b9d33d28-fd37-37dd-8303-6e78c180528e | -3.8598 | -44.1504 | 2026-10-09 14:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 20e73f75-caba-3f99-be41-c40aa75c2b6e | -8.9302 | -45.2041 | 2026-10-09 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 49dee149-822c-3205-8037-67e83492d3cc | -3.019 | -53.9473 | 2026-10-09 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1bde61da-a76e-3b63-926d-70d6d9d62d33 | -12.1729 | -44.7983 | 2026-10-09 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 98f4ebfa-9ba8-37b9-8df2-bbaeda3aa57b | -6.9851 | -47.6858 | 2026-10-09 14:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8ba9591d-8bf9-33b2-addc-153f87545daf | -11.8783 | -47.3892 | 2026-10-09 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 378.3 |
| b8ac2154-118e-3e04-995d-1b3246a72eaa | -1.4569 | -54.7562 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 308420ab-c1f7-31dd-936d-cad0e5a3b0b6 | -3.0002 | -54.0684 | 2026-10-09 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ddf0186f-3b47-3d06-9dea-8407666263c6 | -8.911 | -45.229 | 2026-10-09 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 392731c6-0dda-3b9a-bba4-48b4ac25cfdf | -6.0625 | -59.9088 | 2026-10-09 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ce289533-7774-33dd-a9eb-d1bf5dd19fb5 | -2.8899 | -54.0711 | 2026-10-09 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4e86629d-fb85-3543-b794-1e6daafbd682 | -6.4413 | -55.0224 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c853d645-f6a1-33bd-9fd0-e438ad643177 | -11.318 | -46.6573 | 2026-10-09 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 7e65d8d1-e49a-39e2-a094-9b277ada2fa2 | -1.4753 | -54.756 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 02582273-b42a-3196-8f2c-a797117c7734 | -1.7682 | -54.9911 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2f666624-4b4c-396b-90ed-05495e21d895 | -12.232 | -44.7194 | 2026-10-09 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| dad9918e-28a7-34b2-911d-9996011a3ea1 | -6.4411 | -55.0424 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 2a223e06-bb3b-3406-a05c-d6ff46fe80be | -9.5502 | -46.8492 | 2026-10-09 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| eda971ca-e245-3b45-a578-ec965c45f010 | -10.9193 | -45.3942 | 2026-10-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 5d4ab7e6-dd04-334b-ac27-0305e4a29dc0 | -12.2302 | -44.8126 | 2026-10-09 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 328.1 |
| b79541ca-12ef-330f-afb7-6f3cb164a810 | -5.9649 | -40.914 | 2026-10-09 14:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 89c66062-e008-3afa-94b4-079bd1081c58 | -10.9953 | -45.4068 | 2026-10-09 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 388c81f5-df6b-376a-8607-2d6ae25452f0 | -1.1094 | -54.1802 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| de0b1d14-c3a0-3a80-b411-052c51d3e0e1 | 3.5493 | -60.2633 | 2026-10-09 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 12c48f27-a034-3046-a6fa-379ebf40c741 | -12.2123 | -44.7457 | 2026-10-09 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 365.9 |
| fe6a22bc-41e6-318d-abf9-183483c7b943 | -9.5541 | -45.2239 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 428b6106-e026-3f4b-afc9-f837d20d3932 | -2.063 | -54.3082 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f01d3f7d-27d4-327a-90c1-50a320ff15f2 | -6.663 | -55.0712 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| cc0022c8-c8bc-30f7-8201-22e6e3fc4c65 | -15.2738 | -42.3452 | 2026-10-09 14:50:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 235.5 |
| ba4c33ba-e18b-3aff-bb44-2f75b83a160e | -4.0837 | -44.1389 | 2026-10-09 14:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 0d1b436e-daf2-30f0-9acb-fef97f7e5149 | -8.9113 | -45.2062 | 2026-10-09 14:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a02f71e4-91e6-383c-a859-ab7caa1df2d9 | -6.3665 | -55.1461 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6c9ff4f1-79fe-3861-9ea2-737cd6e03d51 | -5.731 | -41.7549 | 2026-10-09 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| b16f0d7a-0331-314f-bece-5e481220c14d | -2.9819 | -54.0488 | 2026-10-09 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 11d54a90-2192-3451-8d27-ea0708713778 | -3.0926 | -53.9254 | 2026-10-09 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5733b77c-4cbe-3d40-ac40-b0f8ee32101f | -10.4334 | -47.3046 | 2026-10-09 14:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 4858f39c-1228-3ebd-801a-515ed0312e08 | -1.383 | -55.1944 | 2026-10-09 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 11f52e7d-a5e2-39a4-844b-d3174ebff940 | 4.0778 | -60.8791 | 2026-10-09 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5347a8a2-3211-3eb4-9457-2f45aa8013c0 | -2.1544 | -54.4668 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f4254269-f967-379e-8f10-43b7a890c570 | -1.2175 | -55.6512 | 2026-10-09 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 06443882-dfc5-33be-9862-c973c6967afd | -8.9775 | -45.9023 | 2026-10-09 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| df41a9b1-fc76-3153-87ac-4a863fac0873 | 3.9309 | -61.0906 | 2026-10-09 14:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1bb85a3e-2a11-39ed-96f5-e388a2910766 | -2.1361 | -54.4671 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 60fd3e04-b2bb-3d92-bc20-bb1b3bd76452 | -9.1012 | -45.1393 | 2026-10-09 14:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 915c2fc4-6efc-32ee-8120-9bc2a4d0ed7d | -11.8779 | -47.4115 | 2026-10-09 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 6be27fb4-1c14-3f12-a918-5b977b92513a | -8.0761 | -45.6565 | 2026-10-09 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2e3f1172-a497-3119-ba57-82bad5a6e54f | -10.5281 | -47.3156 | 2026-10-09 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| a88f343a-99e5-3720-83e5-15e6ae485cfd | -5.5127 | -43.0512 | 2026-10-09 14:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| dfa6858f-34fe-36af-9427-de7d6f735503 | -12.2149 | -44.6057 | 2026-10-09 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 80f979fb-68e2-37db-9d33-a290d18f4a81 | -11.0754 | -44.0534 | 2026-10-09 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 89188c59-a80e-3527-a044-1f32a659e7a2 | -12.2127 | -44.7224 | 2026-10-09 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 4b48caee-663d-39d8-a78d-eee0217a2060 | -18.3335 | -42.3598 | 2026-10-09 14:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 206.2 |
| fd483737-e4f9-33f8-9861-d91290ac8d80 | -3.8786 | -44.1265 | 2026-10-09 14:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 72645586-a85f-3cfb-b7b3-ca2ef64ffd6d | -2.4806 | -56.0678 | 2026-10-09 14:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 50115748-73f2-35fd-a3f7-4f117c52a47f | -5.9647 | -40.9383 | 2026-10-09 14:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| bf90c0e1-c23c-3755-a2b2-4f630f7c1d5c | -7.4889 | -42.8059 | 2026-10-09 14:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 04f1be83-63cb-3b17-9a56-cc08431edb0f | -3.0002 | -54.0483 | 2026-10-09 14:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 1f4787cc-a329-3eb5-a427-19873333b02c | -10.7475 | -46.6184 | 2026-10-09 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 426.3 |
| a35fc38f-10a6-3fbb-a2df-79bbc442bbb4 | -8.3011 | -45.7245 | 2026-10-09 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| cf16b446-4683-34a6-9c2e-928db2bd0c32 | -2.4623 | -56.0879 | 2026-10-09 14:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 74a91d6c-b3fd-31ca-a439-b642ea2c06b1 | -10.4914 | -47.231 | 2026-10-09 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 78bdfac8-b435-3cd8-b4cc-d70a25f4d62b | -8.6551 | -54.5291 | 2026-10-09 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8c475bb5-bd62-3935-9547-9c9ae8e20037 | -12.2316 | -44.7427 | 2026-10-09 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 2339d0c7-c41e-3d84-88cb-d9ec3048bf8a | -15.2541 | -42.3495 | 2026-10-09 14:50:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 334.6 |
| 2091d7ff-6b11-36f6-a65a-a1672fa05b0e | -2.7428 | -54.1146 | 2026-10-09 14:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d5361059-b48b-3076-bb1d-566d3fd87fd5 | 3.5492 | -60.2823 | 2026-10-09 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 96dbd02c-a185-3250-90c6-e6abe143fd4e | -1.4939 | -54.5563 | 2026-10-09 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f1c00259-10b1-33f2-85b6-98461e655239 | -5.7319 | -41.6589 | 2026-10-09 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| 8d38f85f-1da9-31c4-8020-571114f82cf9 | 1.7488 | -55.5663 | 2026-10-09 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d5f5d96f-04e4-35fe-8f41-132aaaf30db4 | -11.3371 | -46.6547 | 2026-10-09 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 53e03814-11c3-30e6-b5de-b3f868efaeab | -11.4507 | -43.3854 | 2026-10-09 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 31cafaf8-6c2f-39d9-851b-ed062d38fdcb | -1.1713 | -49.2969 | 2026-10-09 14:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |


[Clique aqui para ver as próximas entradas](README247.md)
