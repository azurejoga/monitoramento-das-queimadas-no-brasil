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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b50cebf-91de-3f17-9bfc-fc36e1f22bd2 | -2.33949 | -48.87268 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dea43dd5-a213-3d94-9908-b849b78a3e45 | -3.09189 | -53.95393 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97ce8dab-539d-3bb7-9f3e-e9e293e66eb2 | -3.56999 | -54.68749 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 13ed34e8-cfd6-38c2-ab18-9473f8031496 | -5.5749 | -47.42807 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ab0ed84-060c-3c5c-a2cb-346408e19dc1 | -6.16731 | -39.45177 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d3f33980-3e9b-34f0-bcc9-bf9ac2b8a416 | -3.26569 | -50.39068 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7b34cf5-40a2-3282-8c2c-168f4ad4aa24 | -3.95278 | -55.33199 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4691597a-c18e-3122-b522-e72af96fdf96 | -2.88397 | -54.19197 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8afc8d40-1be1-3e43-b3e7-3bf7274fecaa | -5.41488 | -45.86351 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c91a88d7-7b50-39a1-ad1b-6c5ad2b184e1 | -4.15183 | -44.35098 | 2026-10-09 04:25:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c624cda-85f5-322d-b02a-c54c31cbccb4 | -3.87095 | -55.99154 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c10dcc3d-cd8e-306f-9ec9-6ece6fd9e8d9 | -2.93988 | -54.15866 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bad666b3-89ca-3f58-9cba-2b8604d5ded1 | -2.73684 | -54.11166 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7405b0e-4537-3f9f-bf8d-52a07a922562 | -3.26098 | -50.39507 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d613e49-9de4-378e-970a-44f168b3926e | -6.03788 | -44.03114 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 24aa46e2-9272-3233-bfda-bba815c18d0d | -4.55275 | -54.97218 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ffab2261-9bbc-358d-acde-dbca0d2b0ee2 | -6.42156 | -47.71406 | 2026-10-09 04:25:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23890ace-e742-3790-872e-ebb6370dd3e8 | -3.56816 | -54.66197 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89d780e3-86ba-348b-8b6b-225f58aad19f | -0.65889 | -47.33026 | 2026-10-09 04:25:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a93ab17a-a256-3fc7-9168-b727dad75cba | -5.88108 | -43.40868 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 743654c6-4ca7-3856-b903-c96a9ea82aef | -4.40435 | -50.79434 | 2026-10-09 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08ca5bc4-2698-3465-b41d-93ef0f34c369 | -2.75766 | -54.11201 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1fb17a67-c2c6-3329-852a-5d97715f43ac | -3.98167 | -56.11377 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c210eb9-e1ad-3973-98b2-d13deedd2d9c | -3.79483 | -52.39312 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c95770b-ba8a-30e5-b20c-3a3ce6e208dc | -4.57686 | -54.95665 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05b2f99a-e775-3ba5-a119-ee53cef608e8 | -3.17752 | -49.45552 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ee8d27-8d82-3da2-bfaa-ef414e5e7fde | -3.1892 | -50.59022 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6a1be9e-5868-3620-b50c-76285d1cb573 | -5.70508 | -53.46745 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7dc1aaee-e9ea-3f77-beb0-72fcdc6ee683 | -3.10893 | -54.19008 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa4e67f1-b80c-3cef-9bd0-e906b279278c | -3.2906 | -53.99741 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63d16d7e-1e65-3201-b206-bb90562fec94 | -3.19569 | -50.55015 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e58765d9-5891-3b0f-bcf7-6bb8188ffae2 | -5.953 | -46.38558 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772fa1f8-9807-3008-996b-ed174c802cec | -4.40769 | -43.11758 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 027cc498-d520-3e40-bebb-c6b4b0481a9c | -3.29075 | -51.27657 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdb3483f-2286-31d9-9943-b608d3359a61 | -3.18739 | -58.6421 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28ded702-7945-3645-bf4a-175b422300dc | -6.386 | -45.94107 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96079ebd-3fa8-36af-96e3-83d424499f62 | -3.17275 | -50.59116 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8d44af1-3988-38e1-9d4d-8901ade6da7b | -2.94545 | -54.15652 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddad7cc2-c9d8-32c4-a69b-e72e72cdfc28 | -2.88495 | -54.12111 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfed11b5-29cf-336c-b719-a15264d0d174 | -5.69887 | -53.47616 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de9d2258-e1be-300e-bb78-2a2f24bc182c | -3.54266 | -54.68697 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f1dc30ba-a758-3af2-8b67-545005f673d7 | -1.10311 | -54.17564 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 766b8411-b5da-36b8-9e31-5319054f2f37 | -4.32926 | -55.01776 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c9aef96-71eb-3a38-a542-abdf86c4a996 | -2.26814 | -48.05646 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de35bd1a-7e40-3203-86ae-cc0671e13cc8 | -2.74603 | -54.11932 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1baf76bc-a518-3c8c-80a1-9aca7e96ab7b | -3.39395 | -50.21767 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf6fd3d1-0eda-3419-8178-30054a0ca8c6 | -3.00003 | -53.91864 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 35543ec2-62b5-333f-bc87-8842e315c268 | -3.91798 | -52.13836 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcc66474-95c4-35a3-b1f9-1edb58ea2f31 | -3.54379 | -59.40161 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a0f3df24-9466-367e-853c-a9203383cde8 | -4.15764 | -43.18863 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af4c9590-d45b-32b3-87c9-c3a05a2edc51 | -3.19255 | -50.54443 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dae88b9a-6cec-398a-a1bd-46662d58bd80 | -3.09776 | -53.7642 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a46c3405-fdfe-32e8-b195-9187c1f97319 | -6.88451 | -45.90907 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f187740-af25-3f55-b913-ba17662a2f06 | -5.9994 | -40.97503 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81fd9cdf-548c-3820-85e2-ad70bb4fd96f | -1.42328 | -54.62239 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 551efba0-a288-3920-8dc1-2e07d5e6ba58 | -3.11889 | -45.61943 | 2026-10-09 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd642ee2-259a-316f-8598-efb590b6960a | -2.74995 | -54.09533 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c50b4de8-29b0-3905-8c8e-ee132b73dcfc | -1.486 | -55.87033 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6be2b3b3-d088-347b-9aba-e72632131dff | -3.01231 | -54.09066 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b8e094f-50d6-3caa-8889-8d0be5dccc0d | -5.09559 | -46.21125 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f275e50-3f3a-3b06-b818-b4cf66dcdb79 | -2.47878 | -56.07252 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93267848-ae72-3c98-a072-eab3166d6566 | -3.25076 | -50.40874 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b327f5b-366e-3f6f-926e-45d3949d6fd2 | -3.05384 | -54.02827 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40243bab-d060-3f54-9c91-a2a91e77bd59 | -2.86474 | -40.0139 | 2026-10-09 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9b2945f-cfd0-3ae8-bdef-04edea49705a | -3.01836 | -54.08553 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e33ffd3f-d4f1-31ab-90e2-411bdbaa0291 | -2.47534 | -56.09286 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 236bed3d-0f95-321e-a342-8486b9f029d2 | -5.98586 | -41.37617 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6793745-7e85-3578-9c20-8d888f419ea3 | -1.18886 | -54.17951 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17eff15f-2583-3143-84e1-f88b65938db6 | -2.8885 | -54.18454 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca5609ec-1243-36d6-8b25-6fc4e8ffe676 | -5.09899 | -56.19526 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce57f8cd-cc1e-3d2d-8688-548e24fc1c5f | -5.4575 | -42.36695 | 2026-10-09 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 531dbc83-37ae-3414-b095-f7efe79fc813 | -5.88342 | -43.41726 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90295afb-a891-3cc4-87b6-4e570511fc22 | -3.93865 | -56.02182 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a54720e-f73e-37a2-9f99-7d0bd1066714 | -4.07947 | -44.11283 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa311bd3-ce88-38f5-b8e7-68133e67af01 | -7.06717 | -40.95039 | 2026-10-09 04:25:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bdf76660-9a6e-36e1-8ba9-67470f8bcf81 | -2.738 | -54.13645 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f51f9ed3-d1f7-33e6-bab6-3f401bad2fb1 | -3.30309 | -50.23023 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4964ec9-c1e1-30c3-a9bd-24c49f77bd06 | -5.09666 | -46.20438 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 826cd650-56ed-3433-b113-d0064777ef2a | -1.15525 | -54.22008 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6749a2c1-817c-3358-942c-18c88a013508 | -3.87398 | -55.99133 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 171ea88a-c286-3702-a90f-8650e6a83331 | -3.31905 | -54.04325 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dd56925-ba17-3014-88b4-b98b29cdd03c | -3.10879 | -53.94478 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d57b1c4-6d65-3260-9488-8abe480bf220 | -3.39008 | -50.21708 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51fde2fc-fe03-3b1a-a111-4de8a6ed2697 | -5.75394 | -41.69221 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6632a0f-9c2c-35d0-974d-bcf16fa2b784 | -4.86254 | -42.84021 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32282275-2a5a-39f9-b5e0-b0d30b9da025 | -2.8808 | -54.17915 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26e21b3c-4fe5-39ec-830f-ed9f6fee2ca5 | -3.10354 | -54.28433 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 569c6e7d-24a2-3de0-9e9c-223b7bbaafc1 | -4.73807 | -55.6551 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2685c1db-9a59-367d-b52a-12d278a48b3a | -3.21235 | -50.54754 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2a76d92-3ce7-3235-a9a5-da26cb65f3ec | -2.74799 | -54.10732 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18908a96-3e23-3ca7-b90d-c8f6b99d4e51 | -3.56878 | -54.69112 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 810ba033-29f1-3a5c-b6b2-bf2839590102 | -3.99289 | -59.35281 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc96ccde-4c67-3522-bf94-1c95fb975cbf | -5.09612 | -46.20782 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b962ad4a-d013-37b9-8a45-951c511a8450 | -6.93513 | -44.56994 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dff06fe0-76f1-3fe2-a8b3-979a725d85c4 | -3.52355 | -50.34269 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a72e3373-76b2-3fac-ba14-6233af44f04a | -3.09237 | -53.95103 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90c7b5a4-8741-386b-a35a-e0ec1ff7c571 | -6.0118 | -40.97667 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 1d40aac9-49e2-3a96-9c1c-dc5fb0995693 | -3.30616 | -54.05903 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e18b900-5533-3603-9557-81158776fe1c | -5.63185 | -51.16659 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 211dbdf6-53be-36c2-aa3c-8e580446ba8a | -4.29634 | -48.60265 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README86.md)
