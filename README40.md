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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aad363ee-539d-31f9-8214-de589e1abb72 | -22.49652 | -47.44753 | 2025-09-05 04:40:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40b26d54-e180-3dd4-81c5-269ab0ba902a | -23.33655 | -46.02016 | 2025-09-05 04:40:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b04e2e4-d944-3d3e-ae6d-bd5e53645c8f | -23.33606 | -46.02417 | 2025-09-05 04:40:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c92c6e3e-f8fb-3965-abb6-9e2f8e3c7984 | -22.5093 | -47.69577 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0057dc7-ad1c-31d8-ab95-a29b32244de7 | -22.55066 | -48.68647 | 2025-09-05 04:40:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 771327b8-9cbb-333d-91cc-a2e24558e13a | -22.27509 | -49.56345 | 2025-09-05 04:40:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d4ce82fd-50cb-366c-ad6b-42bd4861532c | -23.43353 | -47.05312 | 2025-09-05 04:40:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 403a059d-aca3-36ed-810f-aadb21c45908 | -22.49223 | -52.7702 | 2025-09-05 04:40:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc184002-5a6c-3872-962c-9b1d742b7906 | -22.50577 | -47.69708 | 2025-09-05 04:40:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 500933df-095d-3fca-bef2-f7857f4b64c3 | -23.47104 | -46.82312 | 2025-09-05 04:40:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 901195e6-2a66-3152-b965-0a01b43288d9 | -23.36998 | -47.1775 | 2025-09-05 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8460ded4-dbc7-38c4-939e-8e990f04fd80 | -22.76395 | -46.4535 | 2025-09-05 04:40:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c99f4d22-c1c7-30a8-9e91-796855147f87 | -20.88964 | -54.98094 | 2025-09-05 04:40:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e92e78c-5515-3d9c-9409-f73627b879be | -22.51603 | -47.08767 | 2025-09-05 04:40:00 | NPP-375D | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d7a99119-3f9a-3e98-8682-19c64e2abccd | -22.92213 | -49.61097 | 2025-09-05 04:40:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5366fcea-a92f-316d-a4c9-24d41f963c8c | -23.37063 | -47.17235 | 2025-09-05 04:40:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4f90a3b-e259-35f6-bc03-117440c11bf3 | -6.61105 | -43.97645 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1976b224-fd75-3f64-a519-f3104fa0b8ce | -5.10264 | -56.14695 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 492bfc62-5d1f-3d5e-b867-c1a0dbe9d36d | -6.50978 | -43.50316 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5fd665d-cec6-3ed2-abf2-44be3ef8c384 | -5.09328 | -56.16103 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03dda397-70ec-3fdc-a1e4-3242de2e3bc1 | -7.16128 | -43.89478 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27930961-2d29-3187-bf80-199f6f1acc82 | -2.95927 | -49.36086 | 2025-09-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c9120c5-44f4-3384-895c-edddb57412c8 | -5.54844 | -45.67724 | 2025-09-05 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66e58f73-68ca-3c2a-9a1c-d424e99b98ea | -6.0212 | -43.70486 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ceb50081-41f8-3702-bbd8-380bc5198b2a | -6.61055 | -43.98001 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cad30bbc-69ef-3d3e-b6f8-fff0d0d1c43f | -5.37664 | -45.10403 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98711b97-bc99-32a4-83e1-54bab08f0a25 | -5.10386 | -56.13936 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ad6f996-38fd-3ac7-8422-046e8c4b4741 | -4.88116 | -41.76907 | 2025-09-05 04:55:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56b16640-3779-39dd-87db-f76fd7346bc2 | -6.02761 | -43.70156 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdc168a9-9347-38ef-a684-9fbe55efffcd | -6.88818 | -45.55087 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccae4a3f-314e-3c77-8e55-ccfe89378a0a | -3.22138 | -50.91504 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f327d720-e105-3c62-b674-ab8fd86594f6 | -6.5495 | -43.90826 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a9200a7-95ac-3667-a0ea-639518a1bb35 | -6.21452 | -43.54693 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b288ca6f-0ce6-3572-92a1-00d7fe39767a | -5.55513 | -46.19871 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2c52c43-e193-3e81-b18c-aabbc7a551f9 | -2.95997 | -49.35623 | 2025-09-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0cc2793-90d2-39a6-97b6-957e10595e1f | -4.07269 | -48.04003 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae0c5287-eaa6-3757-8cb6-7a83ec14af01 | -6.51041 | -43.49843 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b637b82d-683c-358f-9f10-55d4002f800e | -5.26641 | -55.95652 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1de4ea6-abd4-3b2c-b191-d4e1ae231d18 | -5.63325 | -45.73443 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49f36e2b-0f80-324d-8dec-9f057dc11889 | -3.68432 | -49.01702 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3f1b7a3-0b27-36b6-9a51-c96163efd987 | -6.31136 | -47.7708 | 2025-09-05 04:55:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca36d06-7cfd-3be7-b5ca-0518c3838c07 | -5.59709 | -45.02342 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 509e4dee-35d6-33e1-bcf9-821ca22414df | -3.23632 | -50.05079 | 2025-09-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba08c33d-43fb-352e-b33e-0900f827a2a2 | -4.23541 | -48.56044 | 2025-09-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cb3230a-4cec-30cf-ad5f-eae0dc1f3ae8 | -6.1771 | -47.28486 | 2025-09-05 04:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd0c2d0e-f9f9-36ae-9593-3a289c3f6c80 | -4.24326 | -54.91465 | 2025-09-05 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 047f6a6a-9b7c-32ec-8c41-fa185be3b1e8 | -5.88133 | -45.57687 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47a18fcb-17e4-3b7d-b566-945721095e64 | -6.80831 | -45.65794 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d789aac-ac24-3a4b-a4a4-3a3cf47d1cc0 | -5.08837 | -56.25806 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0463a0-e0f6-30b1-8942-dad9d288a79a | -5.09938 | -56.12307 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8176617-8ae5-3d6d-8c4f-e50e4aad6eba | -5.95423 | -46.16751 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a66c4bf-9b32-33a0-88a5-fca0245a6f85 | -6.89611 | -45.19019 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6142499-4325-33b0-a7aa-1fe8557a7310 | -6.00647 | -46.68804 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de47c338-34ee-38cb-ada8-9f4314cfc592 | -6.49625 | -43.73632 | 2025-09-05 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1955039-acc0-347b-aa23-42de91752961 | -6.51258 | -43.49994 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d60bc699-ddeb-3ae6-9d13-7386825cfb77 | -5.72662 | -49.29326 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f978c411-f444-3c65-b043-1b59ebddcf33 | -5.99249 | -49.23479 | 2025-09-05 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3207aa37-8b68-3642-bdb7-7d0afa6d4131 | -6.90576 | -43.81322 | 2025-09-05 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c30721a8-a8c6-3d36-b3ef-800f36359db8 | -2.9435 | -48.98563 | 2025-09-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4633b5c1-f749-328e-b902-69c05d46ec4c | -3.9679 | -48.13252 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dd1c2fa-f851-3ebe-8cc9-4a6cdc035b97 | -6.89416 | -45.1909 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fef06f3-0899-321e-9f89-cffda7d70720 | -5.53632 | -50.89534 | 2025-09-05 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eaa87ec-fb95-3590-b215-641003ca7679 | -6.35324 | -47.1011 | 2025-09-05 04:55:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68968aeb-9cc7-34e4-af19-316182d516d4 | -2.43382 | -49.30669 | 2025-09-05 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74a2bc76-2d41-3457-8232-63252b1c3fe5 | -2.57675 | -54.66431 | 2025-09-05 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b8b5633-9956-3e64-9ef3-39a1bdc4869e | -3.95622 | -54.73223 | 2025-09-05 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4000d361-b57b-3de4-8140-ee703bff8a57 | -3.32629 | -54.90973 | 2025-09-05 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 914f7231-b305-3673-bc8b-e3766c85ecf2 | -5.31388 | -55.85738 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93352aae-d11c-3b7e-baea-0c7a24d0ef7d | -3.82494 | -51.19857 | 2025-09-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae63874-d8bc-3c8e-877b-d6fa444cb0fa | -6.24046 | -42.43977 | 2025-09-05 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35afc549-0a1e-3bb0-8702-0ee2ed7a383e | -5.94254 | -43.0254 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 898cbb59-37e7-36d3-a458-b06aea313417 | -6.22876 | -42.62122 | 2025-09-05 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5cfc6cd9-6322-3199-ba01-536cb3f57a3d | -5.60285 | -45.02101 | 2025-09-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87f3fe37-f63e-3153-b23c-4b776b3ba7f4 | -6.26248 | -43.50526 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6724dcca-1350-3843-ac15-51a62f0c28a2 | -6.05486 | -45.99881 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 260fcb77-16d6-3af6-83b6-617ce6176b49 | -2.55141 | -47.72371 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d02714e-7ab1-3d05-b00c-6eeeb0067a53 | -3.22527 | -47.12722 | 2025-09-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 631d3251-5620-3490-9a69-561f0c3d0783 | -5.09877 | -56.12686 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126631cf-15a7-3079-bcc4-2ebc53c13903 | -6.00098 | -46.69246 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3271371-aedd-3aa6-91ab-ad7c593fc558 | -6.72389 | -45.92476 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37375188-9bd6-30bd-a9a2-069bc8c7d325 | -4.48397 | -47.66574 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dee90f18-98dd-344e-97b1-9df69aa2b098 | -2.55563 | -47.72737 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df240a45-6550-3254-983d-a2199c0ebf5e | -5.03478 | -56.11286 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ef8c75-032e-3d5c-b1ea-018b115fe7d5 | -4.30028 | -48.07792 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c1ffb64-4e0f-3073-bd96-f4b2b0f6bc9f | -6.90517 | -43.81761 | 2025-09-05 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8841f43f-b55f-36f4-a883-2ff117f1924f | -5.96864 | -44.74782 | 2025-09-05 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a994c7d-da00-398b-9984-d3e91185b51c | -5.20434 | -43.695 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b17f7eb-ce4e-3497-8a06-330d3a659756 | -2.55199 | -47.72298 | 2025-09-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c852d51a-e365-37bc-9efe-f8d9d5d22924 | -7.16072 | -43.89888 | 2025-09-05 04:55:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d0eedbf-de79-3130-ae5e-f5cd7c646124 | -4.79029 | -43.81847 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 284c66da-cf4c-3b36-aa7a-488c9a77439b | -6.29321 | -43.50143 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1e8fe65-50af-30ae-afb2-28fa0ae93731 | -3.32339 | -52.62416 | 2025-09-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df8779ce-02f3-3371-a187-40418daed63e | -6.89661 | -45.18666 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69681673-aee4-327e-9029-284a362bcc13 | -5.39295 | -45.94821 | 2025-09-05 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af2ec222-241d-3390-a961-e57fc8bb596a | -6.22752 | -45.64282 | 2025-09-05 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ba029a-4ec5-37e5-825f-62e42c604b28 | -6.54306 | -43.91206 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f78edcc-5ed5-39ba-ae86-d53394786295 | -6.89999 | -45.18804 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fd818ad-79ad-3515-9487-a6c75127b801 | -6.01122 | -46.68883 | 2025-09-05 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e08c699-73df-3a64-945a-bf7bd5a5f293 | -6.22711 | -45.64578 | 2025-09-05 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e05b405f-2b8a-3c67-894e-acb885161850 | -3.9927 | -47.37494 | 2025-09-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
