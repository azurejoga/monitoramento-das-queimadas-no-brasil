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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c62c4c47-63db-3ea2-855a-36e60c550325 | -6.673 | -55.0802 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2a2ecb0-a448-3b9a-8c56-e84d6c532d24 | -14.951 | -41.423199 | 2026-10-09 00:06:00 | METOP-B | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1b844175-528e-3b52-ad29-fccb0509f0ea | -11.3038 | -46.666901 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64a05232-68e6-360f-882f-0fffc42edf9a | -7.2152 | -55.085499 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cda5eed-447f-33fa-9a4f-2db3bf81582f | -2.5113 | -56.2505 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 593fde40-206e-36db-951d-ed4721021653 | -11.6111 | -43.6856 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed19970-a2b5-37b5-9048-09faaa8c3817 | -11.7772 | -45.581001 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05fd3874-6b88-3814-bc18-026fa5d8137e | -11.4557 | -43.381802 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 423a5c5f-440d-3ea5-baf4-4923da8bdc4a | -2.3324 | -48.4841 | 2026-10-09 00:06:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d451693-00ff-343f-a224-8da59d720e54 | -3.2037 | -50.833698 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a379684-5425-33f9-bf25-6f5c27243fe7 | -3.0368 | -54.231499 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97bb9d2e-c63f-3511-b81e-c232ca34021a | -2.8628 | -54.187698 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ea86d9-c89f-3116-b374-9cb174a4ed39 | -5.9576 | -55.363701 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d55fe3-8ead-355f-8f6d-404ae26f776d | -6.9941 | -47.671799 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2358a9-e6e0-3f49-b511-8ad40d80efc5 | -9.1188 | -48.820099 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b6ddad5-1053-3088-a8df-bd5a32dd0d4f | -3.0079 | -54.055302 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5372ce56-0d3b-30a2-ab38-7ae249a9e0a4 | -4.2696 | -46.538399 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da62c9f6-f9de-34ce-ba45-46ba8d83a560 | -3.9033 | -55.882 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee5e731-5388-3687-ba90-2b6c50e59bcd | -3.1783 | -50.583698 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e85cc69-2e01-32f2-ae82-3dc42cbf47d7 | -13.7238 | -49.133499 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 92d9fbaa-c72a-32bf-bed2-7291d229db5f | -3.3124 | -54.0392 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5deac5c-6d45-3fbd-8d76-1dd312b2e050 | -16.877001 | -40.710701 | 2026-10-09 00:06:00 | METOP-B | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1b2581d-f181-3230-bb39-82939be66fd1 | -5.9716 | -55.334099 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 816c854e-a6aa-3302-af7a-e83b48386448 | -3.4931 | -60.203499 | 2026-10-09 00:06:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1921718e-d7d2-3003-b948-a5b2e5ec2826 | -9.6938 | -58.0686 | 2026-10-09 00:06:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3278cd07-82c3-3e23-9bb1-dc075ded7fff | -6.8774 | -45.9062 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81cd47c4-3cc1-39e7-b1a0-e82c338c63aa | -3.192 | -58.825699 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d4e0a26-acaa-3dc1-acbb-a465c670fee0 | -3.2037 | -53.873699 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b07d134-322a-3f41-be74-5b053a4fd602 | -6.8853 | -45.895901 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc06b0ce-d247-338c-9fa3-71b65a8b96b9 | -3.0786 | -58.077801 | 2026-10-09 00:06:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11ed5d28-cdf1-3ccc-b09d-9c0afdda861c | -6.1454 | -47.930401 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d94bea4d-5fd0-3896-859f-1e0b7fb33257 | -16.9111 | -40.8885 | 2026-10-09 00:06:00 | METOP-B | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c74dc0a-4a1c-3c92-8ae4-00215cc43f35 | -7.3934 | -45.6404 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f42e81e4-f911-3a13-8c3a-3cf365dedbe2 | -5.7581 | -43.8554 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0500674c-35ff-3034-bbc6-6fede15a4570 | -5.179 | -45.6101 | 2026-10-09 00:06:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d445330a-b78b-3b15-8309-3d4e69dbc014 | -3.5434 | -54.6656 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6951d90a-eec4-3456-ac44-872bbd0798bc | -3.0045 | -54.086102 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93a5652e-b304-399b-bde6-c24e15c71ad0 | -10.0249 | -48.034901 | 2026-10-09 00:06:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b07e44-3e49-3a4b-9138-aba76f04900f | -2.5848 | -56.166698 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f46a48f3-041e-3dff-b377-fd73f6aa3307 | -3.9811 | -59.3255 | 2026-10-09 00:06:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07af6978-4bc9-3c60-b88a-99a0edf2c678 | 3.5525 | -51.2724 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 22d79a2c-91fe-3628-a9da-93014cf07ceb | -10.2751 | -47.8181 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 333d2833-8709-362a-8005-d4c7dd8c7ce7 | -10.7584 | -46.627998 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63abec59-8649-3be2-9875-aa9219bde855 | -5.2309 | -43.979 | 2026-10-09 00:06:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3ea189f-605e-3a21-9d7b-0d1f3c1b33a0 | -3.7213 | -54.217602 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5710a427-ec26-35e4-bdaf-5b2bf542a083 | 0.6841 | -51.417301 | 2026-10-09 00:06:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b26f39df-23e7-3a64-88be-3687f69dd4e5 | 2.4157 | -50.827099 | 2026-10-09 00:06:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce31c04-5bee-3cbd-a4c4-12d610c4b2d4 | -11.8612 | -43.5648 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39b9a4c5-6673-3acf-8617-16a731d6a37c | -4.1244 | -55.023201 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186eb491-3dee-32d0-b36f-8100566b255a | -9.8529 | -47.454399 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95076a0d-3c8f-3988-a9ad-72ba09514336 | -3.1001 | -53.916 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c1ddbb-27a1-38b5-96d0-f165a25585f4 | -3.5384 | -54.688999 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d27f0130-dddd-328f-9356-09ae38183373 | -1.1571 | -54.234001 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8dd458-319e-3680-b2b0-7c54735b8b7b | -13.3729 | -43.878899 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f97a4627-5614-3ff3-bec9-454aa9b2a682 | -7.0917 | -47.738201 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0336d422-4d22-3910-88d1-071dde8d4f58 | -11.177 | -45.3083 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1760dbd-c8ef-3803-adba-22dd090c1e5d | -8.0815 | -45.626202 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69b717ff-553c-3927-bdc9-ef8266f8d5db | -8.1911 | -45.786701 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98a21ffe-3576-36be-8fd4-38f4ccb852e2 | 3.5034 | -51.261501 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4efd8838-6591-3b8c-bc75-8c7d08b263b5 | -1.085 | -46.897099 | 2026-10-09 00:06:00 | METOP-B | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489c9857-1294-398d-b4a1-373d52fd8811 | -11.9942 | -43.472198 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35f8053c-23bf-399e-b2ea-903b0f93e275 | -5.3912 | -45.902802 | 2026-10-09 00:06:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e30906a9-2c2a-3d10-8b75-ccfdf6eb5bd3 | -3.312 | -53.713699 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d3d7c3-1200-3e48-a1c1-d4dbb43c7219 | -1.2055 | -55.681801 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac0b175-0497-35fd-9be8-b52705e63b73 | -11.5045 | -49.892799 | 2026-10-09 00:06:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a999627-08ce-3189-a0fa-910ec5900c32 | -7.1995 | -55.155998 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e707ed5-f87d-3b63-a404-2e8fa4408162 | -8.9557 | -45.169498 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8bd9e45-a340-35cb-8587-101199a0c47d | -5.0947 | -46.1366 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 921818ab-6ac5-36b0-ae02-ec75edbc7327 | -5.8721 | -49.8708 | 2026-10-09 00:06:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41739772-ac91-365e-b609-a52001ae5bb1 | -5.1692 | -45.6124 | 2026-10-09 00:06:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b427ca6-4dd0-32da-81a2-d6b287c42cef | -11.8515 | -43.5672 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 001f59d1-c499-39eb-8efb-bc39fea1b5f6 | -5.4347 | -43.4454 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1d576be-da09-3ca7-a123-d27c9325b9b8 | -4.5373 | -49.6623 | 2026-10-09 00:06:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c6d25-1173-3525-a157-10216780ca4a | -5.3701 | -48.967701 | 2026-10-09 00:06:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cadf6a9-e2bf-36fd-8e97-0711a3c0ebb8 | -6.8204 | -39.321201 | 2026-10-09 00:06:00 | METOP-B | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8756d577-805d-3f5d-85e6-df7a4114d6c5 | -3.1734 | -58.602001 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5091006c-3065-3045-a033-9f0e973842dc | -5.3485 | -45.185902 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 870d99e9-fc18-31d0-86b8-6abac8f17966 | -11.7621 | -46.777302 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4621d019-20d3-3240-8f2a-0c4bb074826e | -11.6231 | -43.692501 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0980f3f9-bbe3-36c9-b9b1-9749b935ddc2 | -11.6306 | -43.680801 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2d5a3f-90c0-3483-9c48-a75bc335a085 | -11.0816 | -44.066399 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77168543-7f73-391f-8d91-43f3074c649e | 3.5049 | -51.2547 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d2aa3c95-9b53-3fb1-aca3-842dd196fcb9 | -11.2039 | -49.407799 | 2026-10-09 00:06:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 776188d0-005c-3314-8d6e-3ec6a8c92ae8 | -13.8874 | -43.824902 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d49ad864-61f5-3f20-8f36-bc3f19d9aae8 | -2.8282 | -54.1245 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1366161-89b8-38ff-a1e6-c9870c996640 | -6.9625 | -45.251701 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f173e7fe-7e12-3b87-a505-6e50b08b36b9 | -3.0058 | -54.0457 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9b638bb-88a8-3e4b-95f2-d9f8c1f3248b | -2.9929 | -57.734699 | 2026-10-09 00:06:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89f24c3f-726f-3156-8534-7f576cf5b667 | -9.6886 | -58.092999 | 2026-10-09 00:06:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b488538-6a5d-3eb9-82b4-9d1b5f17abc4 | 0.7765 | -51.9655 | 2026-10-09 00:06:00 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c205f218-33eb-3954-97a7-ad440cf564e8 | -9.8333 | -47.458801 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54a69bf4-e8c8-341d-bde5-174d040e7bd1 | -2.1327 | -54.459702 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4410bf9a-7733-3f65-ab5a-d78e981dc19a | -3.2061 | -58.843899 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcaf90f-48c3-3bf3-bf7c-d3cd45d6e1d8 | -13.4585 | -47.3074 | 2026-10-09 00:06:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8533e5-6c14-389b-9c4c-e775cdc5d8d4 | -14.5586 | -50.0233 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df96c5d0-4bec-3d49-b9ec-4483625b970c | 0.544 | -50.896999 | 2026-10-09 00:06:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 909111e5-b936-3161-9f82-22d07970bf98 | 3.7302 | -51.626701 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0134c3fc-9154-3b62-8549-0fb7382ca4a3 | -9.2985 | -47.419601 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1896bb41-fbb0-303b-a317-cec47825a7ea | -9.2722 | -47.440201 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c09eb26f-a58e-3ddb-8738-f60ec2fec369 | -3.1243 | -53.7934 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
