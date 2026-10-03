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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50e904dc-aef2-3c6d-b0a4-d20cf2d145ac | -2.03912 | -54.29579 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cffd9878-8a59-3140-9290-d8edc558e62c | -2.97022 | -53.26654 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7fc9e7e-e79a-39fc-88d5-a1b6cdcea38c | -3.16824 | -54.1012 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8901850-48d8-3ede-bf12-7fee568bece9 | 1.79637 | -55.59096 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25cf6b9b-cc79-3f13-98f7-1cb542484b4d | -3.18095 | -54.08155 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 669757bd-c6b9-31c0-b234-6761ea202676 | -3.15702 | -54.07814 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bcd4fad-90bf-3281-ad58-18608dc9da0c | -2.89635 | -54.14894 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7219f84f-3d18-3c7a-9ede-fb51af10c365 | 1.7884 | -55.59221 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 105e00ba-a416-30e9-8119-d380979f697a | -3.12921 | -53.74298 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33551d3d-bdbf-3bf0-868a-321ed16e9836 | 4.51134 | -61.20039 | 2026-10-03 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8a902236-9e7a-3827-a1e7-a246b71f3394 | -3.29523 | -53.83815 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9a4706e-a5d2-3c63-ba38-905dce15abe7 | -2.26542 | -54.49722 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88a372f1-83b4-33e4-baa0-1a5294d615c3 | -0.36627 | -52.02355 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c957b400-1595-3a6c-8420-a0d47c1ac748 | -3.12432 | -53.74225 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec7fa092-d7c3-3dcb-90fc-0b5a02286a45 | -3.28224 | -53.82488 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47a59634-67aa-3e6c-b2b8-1cd90c4ab1ed | -3.28842 | -53.82938 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 524d09c4-e0c1-3280-9c99-8df4344f59a5 | -2.25329 | -51.93883 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75488a8a-4a79-30f7-bcbd-38030d498420 | -2.15293 | -53.66152 | 2026-10-03 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24d06465-2b63-30b3-99ba-4829d6c54a4b | -3.12351 | -53.74767 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b1cd2d18-4b7d-3fb1-8a59-3407c56f73ae | -1.64392 | -55.14357 | 2026-10-03 05:33:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0de1f0e-9415-318a-aafb-500e03cdd1af | 1.91514 | -55.7811 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a47508e-6c3e-302b-9cf1-4fa89ad59045 | -3.27986 | -53.84121 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4857ffdd-c80f-3061-8192-ee6693779cda | -0.36678 | -52.02031 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e8600e91-9f2e-36c4-aca2-a4feac43dde3 | -3.2819 | -53.83934 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ac822c-608c-3434-88d8-ed81a41a4380 | -3.01454 | -53.88763 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4eb2875-7b8a-3274-8422-c3d57ba47378 | 1.90822 | -55.81287 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec063b6e-feab-3e89-b3ba-2bdaafd5776e | -1.76996 | -55.02766 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0bdc463-10fc-3767-8ee5-b36d72301fa0 | -3.21892 | -54.30951 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fc64de1-20f7-3c4e-95a2-6a6eb91e5577 | -2.89239 | -54.14315 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e1f2198-f667-3ca7-9bcd-470d8c7333e3 | -3.0278 | -51.27269 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac52699d-5570-38a0-8568-3e2cbb3838ea | 0.62808 | -54.41135 | 2026-10-03 05:33:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21efc3da-1222-369e-a059-91ebb86a5b95 | -1.22031 | -54.54366 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cbd5bf3-b253-3bf3-8de7-da4092344816 | 1.90808 | -55.78733 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88b2008e-2014-32a9-ac3c-749d58831b7c | -2.48624 | -56.09428 | 2026-10-03 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3703e53-25a4-33a5-8dc6-fbd3378b73cc | -3.17056 | -54.08567 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f704f99-f8a3-3fb1-808e-ed9773067811 | 4.69728 | -60.84589 | 2026-10-03 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aadb3c8-ea37-3450-8173-d45fe25b05bb | -6.01946 | -53.53827 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e38af96-5906-3931-accf-022c45bb53e9 | -6.01076 | -53.53402 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00c377fe-f43a-3999-9ffb-c631b7ea2152 | -3.68134 | -60.53968 | 2026-10-03 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d904cf57-7ae1-3146-9997-3459fc76dc06 | -6.01545 | -53.53837 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3245fae0-f67e-392a-aa79-3dce81879563 | -4.40903 | -49.97016 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532217e0-5b78-3ba6-8f06-c3fc9fd4852e | -3.64139 | -55.50157 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17c55c55-0940-3380-a5e9-187eaf8ecff9 | -6.23535 | -53.15511 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10104fd1-840b-3f85-9055-cadc4e652e0e | -3.51483 | -54.60192 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| baa0f50c-f2ed-3d2e-9441-9a445615a4bf | -6.21955 | -60.03061 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d56d983-48b5-31fb-9f2b-59eb868d23e1 | -6.21381 | -60.02193 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4613a03f-8c59-335d-aeae-85d05bd5a5cc | -6.22015 | -60.02679 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d39aafac-d0bd-345f-9986-af29353fe526 | -6.00916 | -53.53635 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c60a8e3-7404-3f27-85c4-094dcfe1ed3d | -6.01383 | -53.54058 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37004f34-b34f-3081-a18f-b8d5b44b71a8 | -4.42711 | -55.75276 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e764917-d16c-30df-8faa-408088ee2a2e | -6.01591 | -53.53503 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 586cc83b-163d-3bd2-bfcb-028140140604 | -4.79163 | -55.71865 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43796a72-8d67-3fbc-a16a-15cb010e6e5b | -6.864 | -59.27504 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69c5c1c2-6273-3b7d-87a9-508e6d37c843 | -6.85636 | -59.25245 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c25b0e1f-82d8-32af-87d5-062aa95e5f04 | -6.91534 | -59.28559 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8309a0f9-cd5c-3e68-9be8-e3e1d22cb190 | -4.26253 | -50.74554 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f2d3c18-e778-30d0-b77c-6271c9a96693 | -4.26309 | -50.74775 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76906da7-975c-382a-a3fc-d2d7752a11e4 | -3.64075 | -55.50578 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df7ab076-9444-31b4-b716-344dfdedf86a | -5.11743 | -56.02799 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff4f740d-65fe-3515-842c-94c88e121a7f | -3.95592 | -55.3244 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e98be8a0-bd22-3334-8533-10ea18c26e41 | -5.25155 | -55.92418 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e160e85-6605-39f2-9762-e685cd83e3cd | -3.64575 | -55.50227 | 2026-10-03 05:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c584634f-e542-349d-9133-69255a6d6fc8 | -5.86276 | -53.47686 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4333e8df-6e0e-3a94-b44c-fc1bbd3111cc | -4.26926 | -50.74199 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e72609a-7d95-3d17-80dc-62cca5228732 | -5.89049 | -55.48615 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93e34039-4bca-3fb6-8621-4a9fd7e09816 | -4.40979 | -49.96504 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 139279e8-0ff9-3093-882c-2f7f8d3de121 | -4.2822 | -50.78794 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820a528e-d3a1-354b-ad8c-b85a4d9620b4 | -5.85807 | -53.47258 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bc432db-2439-3100-8d37-568e48e685fb | -3.24655 | -54.52113 | 2026-10-03 05:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa1ae289-9aab-3880-aef5-4dc91cb9d3b1 | -6.85509 | -59.97068 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97dd8974-74ca-3f20-bfde-13b035be34a4 | -4.42333 | -55.74834 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 293d5f53-dbe3-398a-9c48-3cabd36a35b6 | -6.86463 | -59.2709 | 2026-10-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a37f7009-4606-36bc-95bd-a386d561cbae | -3.62759 | -60.21033 | 2026-10-03 05:36:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc7e3b1d-c46e-3442-b18d-7659d2bafd78 | -6.04431 | -59.9341 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26dc4679-4b1c-312e-946e-f43269975663 | -4.78666 | -55.72203 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1969b5b4-86df-3617-ba0e-dfbe75f48c0b | -5.85299 | -53.47107 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd0401c-900a-3873-86e6-03fce0351800 | -6.07931 | -53.30978 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada9c588-530d-3600-8b3e-15e5ae8f561e | -4.12285 | -55.01871 | 2026-10-03 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd3e3870-f615-3726-aa34-59a2e023717c | -3.58685 | -54.53376 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70f33408-2b39-38d5-bbeb-5384cc0976b7 | -6.07978 | -53.30639 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8655c8e4-ab48-3366-9c28-520c325593ba | -4.71357 | -56.15243 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50b962a4-09d9-31d6-b2b9-1c8e0080f6ce | -4.41339 | -55.75563 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244baac0-9fa5-319d-8156-b3eb7378bf5b | -6.00988 | -53.54042 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6683d7-e869-3514-a6dc-da176ca844be | -5.96205 | -55.34698 | 2026-10-03 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 047fb572-6d41-3193-bac9-e4a911df06b0 | -4.26852 | -50.75321 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 267c946f-201f-37fe-9743-cdf08e90a9f9 | -5.09525 | -56.25715 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18fbe458-3d9c-347e-9165-7288f0987379 | -3.62422 | -60.2098 | 2026-10-03 05:36:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628b8779-cdff-3f00-8d10-fdd57ac2a7d0 | -6.23688 | -53.14429 | 2026-10-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba4aa81f-32c1-3904-a5d5-5e920f2529bb | -4.40336 | -49.97602 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d9072b-2704-327a-8399-bbd78462f6ed | -6.2057 | -60.02847 | 2026-10-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc5493cd-78f1-31ba-990a-ab5bd74095ca | -3.70531 | -59.68671 | 2026-10-03 05:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25779528-7f85-3079-be3b-5c51e8f64b02 | -3.51875 | -54.60745 | 2026-10-03 05:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 627b69bf-b6a0-38c6-a6d7-0d19178c81cd | -5.85257 | -53.47399 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07c0944c-bc5e-3ea1-8479-46d71efe9eb5 | -4.26981 | -50.74403 | 2026-10-03 05:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a8c7ab2-e745-3096-a136-4decebf2b215 | -4.79102 | -55.72275 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cd309ce-7be5-33a9-bbc7-d5874f98065f | -3.08638 | -59.18884 | 2026-10-03 05:36:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db8b5ba1-fa10-3181-94c5-d350d93e84c0 | -4.78727 | -55.71791 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fb5ec7d-8a06-3603-9889-03668cbf22a0 | -4.79225 | -55.71452 | 2026-10-03 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c803e8f-dbc1-337b-9917-4a2621a957e4 | -6.0045 | -53.53205 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 303a4635-9134-3cfb-af2b-eb351108d03f | -6.0103 | -53.53735 | 2026-10-03 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
