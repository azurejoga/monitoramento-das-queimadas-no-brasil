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

## Dados Diários - Página 371

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c8bf75b-8251-349d-bfd8-523a2171ca6b | -3.2214 | -43.97559 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83f4a20d-5b0d-3f0e-8e02-91ca3519aa71 | -2.88876 | -56.54714 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b3a76caa-10be-3df3-8b80-44d69e36bd7a | -3.70335 | -59.04388 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6dfd2b18-e9a1-3745-a3af-79a7290f4752 | -2.89896 | -59.22151 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 64d06a07-737a-31e8-ba5a-25955fbca9dc | -2.98339 | -56.83461 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cce8e715-f5f3-3ae5-bbb6-b12c74c985e0 | -5.40611 | -45.92132 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd3b6aa8-328a-3663-8853-456df032134b | -6.94419 | -59.09584 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d65f53ee-44cd-3371-8f94-9e9135ce96bf | -2.75539 | -54.08871 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e150b84a-0c79-33ee-9885-10daf12bc4bf | -2.73363 | -57.46799 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7d06dd30-0897-3f8b-b712-e9aa79024c12 | -6.48773 | -55.30188 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 491c62c6-0977-3c4a-9a8f-58d37b056e5b | -1.60353 | -48.7441 | 2026-10-08 16:39:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bb35c91-31ed-3e19-a163-b2db8bba8e52 | 0.52792 | -50.79779 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15e92e27-242b-3f76-aac0-4d6fae593184 | -3.44701 | -58.5039 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8b1c84a-91ca-3ef8-a046-e26b0ea7ce58 | -3.65568 | -58.57804 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6ffbff0-2b4d-3463-ae93-e007c7daff69 | -7.23635 | -55.13098 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| cb4a3d14-31c3-3975-8651-4691411f3f3c | -2.98952 | -54.08467 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9f5b44e0-1a89-3955-a249-82b0ce4e3cd9 | -1.83127 | -55.03452 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7630a84b-aac6-3511-bae1-f4f67f26495b | -4.08949 | -44.11448 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 0c14f6f9-bc63-318d-a3d5-25b70e1f8517 | -0.08333 | -49.47791 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 889c3751-191f-3ef5-908a-d6a9b6dd8f74 | -7.00188 | -59.10852 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 68eb1f19-2c1f-3621-8adf-c6bdad28bba8 | -2.28634 | -48.74535 | 2026-10-08 16:39:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 52092aaa-d2b1-39cd-bc31-76d9fa902e91 | -3.29779 | -44.68085 | 2026-10-08 16:39:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 67ae5898-4be7-3ceb-8803-d28aa277d837 | -3.38363 | -50.21231 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e42a3174-b925-3058-9111-97988d440f7d | -2.30956 | -57.98952 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e70ee1ce-ea32-3dce-9a6c-cada0ff8492b | -3.45783 | -59.83302 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a28287d-667c-3139-a037-987184b9d837 | -7.21893 | -55.09703 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2cdb41b8-3f92-369f-8de7-0b87dffd73c6 | -3.17469 | -50.59529 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4091c872-17a8-395b-9857-31a78e907e85 | -3.31712 | -58.27064 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddca84e8-3fbd-389a-8c7d-a1d74866a6b2 | -1.47155 | -54.76151 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| aa90cab2-feeb-3aa2-90b3-d4a7ed4c1df3 | -5.45536 | -42.90843 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| a02f63cc-95dd-3826-8695-edf975ebe256 | -3.63018 | -59.31956 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 936af738-b55c-354b-8a60-f69af6fdc093 | -5.77535 | -52.36259 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a6c1b596-df45-3df6-b795-42805f351d19 | -3.84881 | -44.12366 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| a01d3e63-da86-3650-9be1-97321548742c | -3.68952 | -55.42997 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e83b3aba-926f-3e8f-96f8-155535d3b105 | -3.51583 | -54.52422 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3fbca9a8-67e1-33e3-85ae-36f5a2edc052 | -2.74969 | -54.11528 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| c2c0f06f-2bb6-3ec6-9094-1df04cf4c707 | -1.52617 | -54.82531 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3f7f5612-bff6-327c-a9c4-3e50a3d0fd8c | -0.08792 | -49.48489 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2f529523-4698-3bb3-9552-f740bfe1abd4 | -2.69829 | -45.06404 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9abd4cb0-5cd8-31a9-a420-6b443722ad07 | -6.20266 | -52.84822 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e8fe84fb-c5e6-3609-9edc-20a90b4ff0b8 | -5.09606 | -46.22419 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f8c80bc6-1032-3b41-908c-889291f22b4f | -4.05403 | -38.93812 | 2026-10-08 16:39:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5367187f-3259-32ed-8982-42c240f89ed5 | -2.92903 | -56.58719 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5c4cbf33-58b8-32cf-83aa-c3e07f142407 | -1.75469 | -56.19685 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e7a2f3e2-ee9c-3a8b-a031-a6b90366ff27 | -3.28706 | -53.69981 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 443f317b-140a-3b48-8beb-e86d30744192 | -5.45975 | -45.58589 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d9ab36a-c22c-3c07-a44d-3ab0edb0969d | -5.8048 | -52.75246 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d5b59ed4-5307-3fb1-bd59-730aa435fa12 | -5.88327 | -45.97982 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 53a07444-b22f-346f-adca-6e12529d4109 | -5.47403 | -45.70082 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 54878fd1-79e4-3556-a0c3-5af8f8e502c5 | -2.39622 | -57.89004 | 2026-10-08 16:39:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4c52762d-dc59-3137-9ab7-0079377977a2 | -3.76718 | -41.77023 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 49006bb0-db07-3d3e-9055-9305552190b4 | -3.20688 | -57.86788 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4a21e5b1-d817-39d8-b824-95261a4fedb7 | -6.33532 | -46.94695 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 14a51f96-b4b9-3f43-a4bc-7f87d846eff8 | -6.13561 | -47.94981 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d25da34a-3002-3f4d-84d3-a4f8ec84bb37 | -2.06516 | -56.88206 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d16c8873-a924-387f-88de-751df3b43b90 | -6.8352 | -52.85907 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a786440a-5238-33a3-90f7-23b375c57ff5 | -3.79958 | -47.49643 | 2026-10-08 16:39:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 31cd9e66-2714-3931-846c-ad92e51c020b | -6.32482 | -53.58599 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a639d3ae-4ac7-3407-864d-400fc32af977 | -5.66813 | -43.62467 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8163d11a-0bb6-3e1b-af9d-4fdd30647637 | 0.3858 | -51.16055 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be7c3d14-da3d-309a-8362-aa77c2f1bbca | -6.20591 | -52.83815 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 52c6a740-2f48-3fb0-8ab3-43a0c3bb4007 | -5.50111 | -42.84534 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9c4a5a46-b90b-3c0c-bd98-a0fd82960689 | -1.93762 | -45.24208 | 2026-10-08 16:39:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2845fe16-03cf-3e5a-819f-6c7fb071bd2e | -6.2471 | -52.86571 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| b9a1bbc4-4a5f-3628-a1e8-9e7e0678c3e2 | -3.26538 | -53.996 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 947b1095-acd1-3d8c-b95a-ad62bb871c40 | -4.16449 | -43.34144 | 2026-10-08 16:39:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 33f8bdc8-112a-3ae5-ab3d-f3b15b901379 | -2.7584 | -54.10888 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9dd39468-8e93-3a80-ae18-fc95f9055227 | -2.98595 | -54.02879 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2f283df0-14f5-3881-9886-f49818ece071 | -4.35714 | -55.22543 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dc06066c-8c69-3c57-b8d9-c1e86a80fc4d | -4.4337 | -43.90313 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 26e8bd03-3a27-31c3-848a-6c5670ca2a96 | -5.30685 | -45.71749 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 98eaffe1-3786-3c0b-a2c6-11493792ff15 | -3.45221 | -58.0466 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c786e4ed-7727-3f7d-b103-9734e5e4f273 | -5.28402 | -48.104 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 50622869-8dc0-3d0e-998c-905f545cd767 | -4.15179 | -55.13748 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| edd5bd66-2290-3545-b56c-c6eef4b3bd7e | -5.10938 | -43.16114 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5ec24f33-65bf-345b-b716-723de60d2d0d | -3.0764 | -53.94672 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| cdce2db4-592f-3a16-ade8-c11e930832f5 | -3.5719 | -59.40894 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7674acdc-038e-36eb-a040-5c5d75ceb4bc | -2.99926 | -43.28477 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 55db527c-362a-38bf-8f2b-abb0f4b0157a | -6.45261 | -52.69979 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 05de749b-7b01-3011-87af-e505adf9ff46 | -5.38175 | -45.93914 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff4b9810-61cf-3300-876b-875b23094287 | -3.35555 | -59.50727 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d4402f4-2fb4-3a95-bfe7-6c4650a98247 | -1.77432 | -55.06743 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12aa5151-9913-3510-9af2-e96458c2c0d3 | -0.57403 | -52.22417 | 2026-10-08 16:39:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 891d1828-978a-3505-a8ec-ddb248d89ee4 | -2.47048 | -46.01365 | 2026-10-08 16:39:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 275da447-62c0-3a15-a873-121434432b02 | -4.96992 | -37.9707 | 2026-10-08 16:39:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 41617130-a259-3d51-b2a0-0233e2d9c346 | -4.4623 | -55.39816 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b28a7303-7a5b-3827-a5a3-00b55363ed0e | -4.017 | -41.77332 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 3e5967cd-b92a-32bf-91d6-04d91afac40a | -6.15504 | -47.93921 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 7cdcf54f-d419-343a-9145-a3528857ce4b | -2.83145 | -40.22706 | 2026-10-08 16:39:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 3e33a856-e3a3-3a5b-8c73-57509a375569 | -2.74272 | -54.10083 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1a8721e2-c743-3f38-8e16-b0afd88cc3ab | -3.6208 | -58.60976 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9853eb7-d794-3404-8d4f-b42f2a6e8a45 | -2.97951 | -54.05017 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 49b5284b-3937-3749-a600-2e00e9c86ad8 | -5.48508 | -44.60107 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 237cbd97-71f4-3b23-b2e7-69e912fb6407 | -2.5801 | -56.16862 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 3ae4ad28-b298-3c91-b0c5-9c556963800d | -3.16958 | -50.58674 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 75a5c54e-63e0-3abe-9091-b051764ca87c | -2.78996 | -45.17971 | 2026-10-08 16:39:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba712381-c105-34b1-b937-17cf18239a10 | -3.89633 | -59.44473 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 56051b52-0f16-3a02-9793-add69e36103c | -5.14079 | -42.97807 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e85ef3c-efd7-39e9-b2ce-d808e8d4b8d6 | -7.23311 | -55.1198 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 90cea203-1148-398e-8aa9-7cfef3ace700 | -7.24175 | -55.13 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |


[Clique aqui para ver as próximas entradas](README372.md)
