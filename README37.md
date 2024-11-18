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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37ce08ad-06dc-34ba-94f1-a7bd8f3ac150 | -0.93259 | -51.63437 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74fe1a1a-157a-336a-8104-948c2daf5c98 | -2.96583 | -49.20021 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b31826e-065a-3b5f-a151-d6beebe6a472 | -2.78433 | -53.98294 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3470ecf-68b8-3e4d-9641-bf9add544350 | 0.69433 | -51.44328 | 2024-11-18 05:03:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e5e405a-0325-3225-9682-cbb92fcd5b49 | -1.61822 | -52.62783 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90c6edaf-fe75-3e42-886c-b7441d0ab244 | -2.98001 | -45.74311 | 2024-11-18 05:03:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eca37851-e3f7-3d99-9b04-a3375e3b9c95 | -2.1869 | -50.33321 | 2024-11-18 05:03:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c27be3c-13e7-39d4-a851-dae2c0e4770a | 0.16705 | -51.26442 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 320d4494-2821-3bdd-a370-ae88a34ef0b0 | -3.1881 | -53.2505 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d785c6b-50a2-3d81-8515-40c0aed59193 | -3.57707 | -53.11601 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93060dd3-a912-33ec-a2ef-dd3d370dde26 | -3.3751 | -53.31276 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e87c3d9-6112-3b6f-be38-0b2de44c1307 | -2.53804 | -48.9292 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a34ae93-e8d9-3173-b45f-982823509dae | -1.61587 | -52.48229 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bf5c863-e8c2-359c-8456-f96b0956ca46 | -1.18949 | -51.98293 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36e64af2-e086-391d-9b6b-c68bb6a43a9d | -3.52989 | -50.25144 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0d20605-056e-3c30-8f78-2c31607471e2 | -5.26988 | -47.18623 | 2024-11-18 05:05:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6443cb9a-2a1c-35c7-8e43-83c55f963cda | -10.63104 | -49.43999 | 2024-11-18 05:05:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6f01940-2a35-3481-8e12-b5b85f3db539 | -4.70697 | -49.6278 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745e34ab-ca61-3165-acc0-b3f532838031 | -4.63387 | -50.41461 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 396be544-0f80-317e-a634-b1ae0490a880 | -4.27565 | -50.88369 | 2024-11-18 05:05:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb46478b-431b-323e-9543-1fe768199395 | -3.74469 | -54.65483 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 920ab6ab-9df8-3c98-a210-5a387e780719 | -4.18663 | -53.85587 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c27e5915-06e4-30c5-a423-d7bcca949f18 | -4.00612 | -54.02029 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c0104cd-61e0-3785-b295-9f89f9a94051 | -6.39731 | -44.7413 | 2024-11-18 05:05:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52c223ab-5d5d-3457-8618-5f25cc2e7781 | -4.50074 | -49.6395 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 568b9c71-077f-3270-af0d-226c37394617 | -10.20856 | -50.54215 | 2024-11-18 05:05:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b34d61a4-af7d-3b3d-9e2c-ddd87a97fe94 | -4.63112 | -49.54481 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4094fd0e-5554-3e77-a32a-7dca2687120d | -3.87725 | -54.34925 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db9f87cd-4a3b-32b4-89fa-4cd56396a270 | -4.00333 | -53.74568 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33e17d10-4c4f-3d6f-af03-26d0ac70728e | -5.24803 | -50.11821 | 2024-11-18 05:05:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f49b0c6-0d24-3aad-a2f8-e682b7bf2b35 | -4.61231 | -50.91496 | 2024-11-18 05:05:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 934eecfa-7abd-3d13-a0e2-ff522f107be3 | -6.4932 | -47.49854 | 2024-11-18 05:05:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cf45926-0f8d-3afe-b33c-26832bf645f8 | -9.28021 | -50.65567 | 2024-11-18 05:05:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8d515bd-f270-3cae-a4c2-53c9e526485d | -5.26945 | -47.18917 | 2024-11-18 05:05:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc002a3d-09cd-337a-a43c-6add7fd7732c | -7.04684 | -46.721 | 2024-11-18 05:05:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0890166d-fad2-3f90-a2ff-8e16c5158690 | -4.95343 | -49.49479 | 2024-11-18 05:05:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f31c4337-a46e-3289-9e94-749959f841e1 | -6.27452 | -47.22564 | 2024-11-18 05:05:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cc585e3-7a2e-3c93-8c75-f79a5592ab6e | -9.2993 | -46.21178 | 2024-11-18 05:05:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58fb3291-48ef-36c7-9b16-812f0334b756 | -7.71207 | -45.66362 | 2024-11-18 05:05:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89cfab05-1c9a-3579-9c9e-0051fe47219b | -9.6471 | -47.41584 | 2024-11-18 05:05:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24385b1e-4621-326d-a260-2cf5c90dab33 | -4.0808 | -54.89885 | 2024-11-18 05:05:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e4db378-282c-3093-b98e-62e35842ee62 | -6.49276 | -47.50161 | 2024-11-18 05:05:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff06fd55-caa2-3162-94af-3b6e6f6fdf3d | -4.43058 | -50.0952 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41b4a740-d7c8-329f-a787-f1355693083f | -4.08134 | -54.89538 | 2024-11-18 05:05:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 355f53f3-1f6f-3d8b-a2d8-9cf26ef4d42b | -3.91894 | -54.51734 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c8814b5-a1da-3762-a70f-47471055dc17 | -4.37368 | -50.51529 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4354f5c-198e-3ab3-a11a-9bac2942e71a | -3.75161 | -54.71987 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6aa148c-db7e-3de1-921d-a9809b317c6a | -4.27489 | -50.88873 | 2024-11-18 05:05:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac1efddf-bc67-380d-983d-58238b4900c1 | -4.72026 | -49.6151 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b69befb-bbaa-3273-a431-c948f4a3efa4 | -7.89127 | -61.46524 | 2024-11-18 05:05:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c130cd-63c1-30d8-920b-662be9b786cf | -4.27959 | -50.88427 | 2024-11-18 05:05:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f48284c-cb63-33f5-bb54-1ec24e420325 | -7.71307 | -45.66699 | 2024-11-18 05:05:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d38457d9-7b2e-3643-9c8e-ac1268b2e475 | -4.6175 | -50.82723 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efa32b94-d77a-31d0-a284-d99978490507 | -5.27216 | -47.18901 | 2024-11-18 05:05:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55cf83b2-0a7c-3fea-a1ec-d843e8a2a91a | -6.39794 | -44.73653 | 2024-11-18 05:05:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9c15dbc-1ca2-35ed-8145-636ad9d45d0e | -7.92219 | -61.67898 | 2024-11-18 05:05:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16857bed-ae0b-3d0b-88fa-3db303823340 | -3.919 | -54.01437 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f62dc6dc-2788-358a-9ce9-a523438aec4f | -9.29878 | -46.21586 | 2024-11-18 05:05:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06436bf6-ea86-32c3-87a9-538edc0db46f | -3.7483 | -54.71936 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de572fda-f392-3be7-a764-c8e54901cba8 | -4.1238 | -53.4621 | 2024-11-18 05:05:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4586907c-3dd2-3968-ab45-a0fd37868b84 | -3.81772 | -54.66604 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f3efe46-1b7b-3fe1-ad37-45259580e290 | -6.27494 | -47.22255 | 2024-11-18 05:05:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edd82600-8a1f-3d98-98c7-e8d76b4e4065 | -4.7007 | -49.62897 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecfbab27-5c58-3073-852a-220ea8a38c2e | -9.30463 | -46.21629 | 2024-11-18 05:05:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21182504-48b3-38a3-9cb0-e6e03705bb00 | -7.71952 | -45.66356 | 2024-11-18 05:05:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad5fa895-f832-35d3-9690-f76c11ad3f73 | -4.50016 | -49.64351 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb85f4b0-6daf-3122-bf49-280ce740726b | -4.71966 | -49.6193 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57c78097-5315-36de-b9fd-644f7861cca4 | -7.13202 | -46.63823 | 2024-11-18 05:05:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74e17482-7b50-322d-97c4-7f80433dc75f | -4.12037 | -53.46156 | 2024-11-18 05:05:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49a5c398-637b-36fa-9e87-9c8a33d90d5b | -4.59496 | -49.62479 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db6cc358-089b-31c6-ac64-9e317d8241dc | -4.06542 | -54.05105 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c83c7bd0-cf08-3c79-9be6-a2b020bf0538 | -6.00408 | -46.40121 | 2024-11-18 05:05:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2362d88-f634-3084-9024-06a59a0502f0 | -4.04584 | -54.53309 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d7776b3-789a-34b8-b5b8-4dfbca4ceab4 | -8.58216 | -50.98053 | 2024-11-18 05:05:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c180eb21-c928-3341-9005-365f2cadf2e0 | -4.66618 | -49.5165 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1edca436-f5b4-3c60-9c68-7a307d447e18 | -10.12825 | -49.14531 | 2024-11-18 05:05:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 327ab30f-3e88-3db8-a6ec-4f7d97684f05 | -4.66185 | -49.51586 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c397f196-f97e-323d-bdce-87e8dd5191e1 | -4.70499 | -49.62971 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067af867-b49a-3888-a0f3-576aa9ef1cdb | -4.03982 | -53.50643 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60408604-190e-3dc3-9f79-ac98bc7769f8 | -6.22505 | -55.65558 | 2024-11-18 05:05:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e145b2d-31f9-3bfd-ae39-7e17b64fe68c | -11.12182 | -45.29264 | 2024-11-18 05:05:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e9861a4-b5e1-34da-8a1c-86e672c5a576 | -4.63742 | -50.41879 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98eee1d-f366-3fdb-80ce-6464791e8a06 | -8.58162 | -50.98431 | 2024-11-18 05:05:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 904f154d-24d3-3f1d-8cc5-46128e24ae69 | -4.25175 | -53.51918 | 2024-11-18 05:05:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1500b21d-267c-3f9d-ac7b-6cf5e5be92e7 | -4.63171 | -49.54073 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c71ad67d-0e90-3c5b-9a05-9961bcc03d81 | -3.83454 | -53.94605 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13d8303a-9a06-3504-a2b3-691cb7cf44d9 | -4.80117 | -50.80345 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d226aeda-79a0-3121-aee2-39649973b915 | -3.74498 | -54.71885 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 475799f7-21f1-3416-a0cd-9ebd9bce55ed | -4.70129 | -49.62481 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57ffbecb-e31d-37ee-aaef-9b0af7496027 | -5.4986 | -49.58077 | 2024-11-18 05:05:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35c15f12-f16b-3c3a-9832-c68a86fb2a0f | -4.08849 | -54.08024 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2dbe63-0e6b-33b5-b1b6-49ea805829a2 | -5.24317 | -44.75484 | 2024-11-18 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31d2aef1-1e55-3dee-8eb1-0a29214785f4 | -5.24382 | -44.75015 | 2024-11-18 05:05:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1d6b0c2-acfe-3831-bee4-656fe26ae9d8 | -4.37316 | -50.5188 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbb33206-1939-3d55-9191-b316dc467957 | -3.71885 | -54.7999 | 2024-11-18 05:05:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6739cce-328c-3689-9f3a-489be232a9eb | -4.00331 | -54.01622 | 2024-11-18 05:05:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 776e7957-9e76-31f0-9368-d2258f88dbdb | -7.71795 | -45.66447 | 2024-11-18 05:05:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae25ac7b-344d-3094-9ebf-504a0ab31135 | -10.13307 | -49.14601 | 2024-11-18 05:05:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d29dea27-efe2-39ce-8081-aa03a8959698 | -4.70558 | -49.62552 | 2024-11-18 05:05:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d29a8f-1223-305e-9b03-d74cd5258e3c | -9.64667 | -47.41928 | 2024-11-18 05:05:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
