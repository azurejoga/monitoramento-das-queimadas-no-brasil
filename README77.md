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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c00e3b7b-096e-31c5-b0a1-9069c760512e | -11.446 | -43.6461 | 2025-09-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| b2b5614f-cc91-3dc8-a4ab-7c29981e957b | -12.1988 | -53.9024 | 2025-09-09 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| febd96d8-83a2-3feb-907f-933eeed287a8 | -17.2557 | -46.7578 | 2025-09-09 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ccac998d-b20c-34f6-8c51-5f1eb61c8458 | -12.1991 | -53.8817 | 2025-09-09 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 1bf3f466-e4f9-3319-8859-2f6e0016bb73 | -12.2178 | -53.9005 | 2025-09-09 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| dd99e717-69d9-32c2-8399-ed46c4b5aab9 | -9.0232 | -49.7834 | 2025-09-09 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9bd4e3e4-6f69-3f78-9a09-8cf532b77bea | -5.5506 | -45.1664 | 2025-09-09 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| be6d8639-e9c9-35c5-a2b7-c7ed04ef67be | -17.2973 | -46.6799 | 2025-09-09 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b480993c-271d-35d0-ab51-74c71a7c9be3 | -5.5702 | -42.9062 | 2025-09-09 13:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 243.2 |
| 8f961404-3a0c-3881-99dc-677487c54b0e | -5.9899 | -46.2141 | 2025-09-09 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 513ae6a9-0d0c-36a3-a7d5-f47f2737abc7 | -6.2224 | -43.3693 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d836367b-8732-3e85-91e2-4576ec079a23 | -11.4322 | -50.3504 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 306.7 |
| dad0e072-8e33-30d7-aa6e-2aad87414e6c | -15.2683 | -53.8012 | 2025-09-09 13:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 636bfe39-a2b1-37bb-a5d0-6ebe7b274461 | -7.789 | -46.0891 | 2025-09-09 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 32188a93-aba6-381d-a43d-275745ad0b5b | -6.8259 | -44.9091 | 2025-09-09 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c22b7bea-da75-3378-9600-3ae4ed59cbcd | -7.5799 | -44.6579 | 2025-09-09 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3f19a234-671f-3eb3-843b-b6169e8d3c3f | -17.2563 | -46.7346 | 2025-09-09 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a16af0c5-bd22-33bb-900f-f462d43f59b7 | -5.453 | -43.4525 | 2025-09-09 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7cd6a3a7-96b6-3602-89a5-d4e2978af98e | -7.5799 | -44.6579 | 2025-09-09 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 787d1b53-b8a0-377f-b64f-79dc65b7945a | -14.9082 | -50.1105 | 2025-09-09 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2ff3e71a-56eb-360c-80e4-24559966d846 | -17.2967 | -46.7032 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| fda5cdbb-66c5-3fd8-b2ff-b8576e1de683 | -17.2757 | -46.7538 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c5b29540-3b03-34ec-912f-c7eab059cc83 | -12.0291 | -51.1149 | 2025-09-09 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 233.3 |
| ff39fe3d-d471-330a-b6e2-8a70757c5aae | -11.446 | -43.6461 | 2025-09-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e32c84d6-b3b9-34bd-849f-c34d06e5ae44 | -5.5506 | -45.1664 | 2025-09-09 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d5b2e22d-98e2-309e-9a2f-7895971a6082 | -11.3549 | -50.4447 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 240e9b07-d978-3619-b696-fafdd025796a | -9.4436 | -60.5114 | 2025-09-09 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c518b026-ca1a-3118-b3d8-d96bd289a01c | -21.127 | -48.8519 | 2025-09-09 13:10:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| a63ffe89-0283-3a86-b4b3-1cb2d849cf7e | -17.2762 | -46.7305 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 49a94968-63f6-3e62-b922-14d48eeb4987 | -12.2178 | -53.9005 | 2025-09-09 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 935a0776-678f-3389-aadd-c5a04861b988 | -5.8406 | -44.0951 | 2025-09-09 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7f3d1566-0b44-3768-8534-67aeea124acb | -10.2982 | -48.8148 | 2025-09-09 13:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 4013029b-403a-3218-b180-3c81ff70ebca | -15.2489 | -53.8036 | 2025-09-09 13:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8bcc8608-3c48-3427-9664-99ec6a840ea3 | -10.8913 | -55.693 | 2025-09-09 13:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d7f1174d-031b-3319-b017-6cdb36da7aab | -11.0231 | -46.0412 | 2025-09-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| eb2499dc-38fd-3fbd-97cc-ac98ce1542e5 | -6.2224 | -43.3693 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 3e8e7b19-7b95-3e90-b49c-c5ac0aa67cbe | -5.5504 | -45.1891 | 2025-09-09 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9e6a430c-7229-3beb-a182-21683f469825 | -11.3552 | -50.4233 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| b15f0b79-0b87-3896-a09c-05217387e138 | -15.8205 | -52.2444 | 2025-09-09 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c1f1b4fe-3c25-330b-b194-6f2bcac0cd9c | -5.8395 | -44.2103 | 2025-09-09 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 0e038a37-dbca-377c-83a0-f8f8eae4d695 | -17.2973 | -46.6799 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 97574751-7a5b-3cef-85e9-3ba119eae7e7 | -7.5611 | -44.6597 | 2025-09-09 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3ca68715-5699-346f-b4a5-25e45f145047 | -11.4325 | -50.329 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9b3594da-5fd9-35a3-bbf0-73fd068a5e9b | -12.2181 | -53.8798 | 2025-09-09 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| deded3d0-02ad-3582-9f7c-c3db81980e19 | -11.4318 | -50.3719 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4c7d68fb-49cb-3a77-a2b2-a30ad2613c07 | -6.1846 | -43.3958 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1b32cca7-96d7-335a-bb43-96cfa7906fc6 | -7.6744 | -47.9796 | 2025-09-09 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 8935ff3b-39eb-3969-8c5c-69b9836432ca | -5.589 | -42.9048 | 2025-09-09 13:10:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 280.2 |
| 08703c05-0672-3677-b8c0-50986e0af32c | -8.4119 | -49.0869 | 2025-09-09 13:10:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8843e44f-13ee-33e9-b18e-d353e14a56f8 | -12.18 | -53.8836 | 2025-09-09 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8e4b18dc-5b5c-3bc9-8c6b-f83cc2960b46 | -11.9926 | -51.0126 | 2025-09-09 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 237e05ff-d220-379c-ac60-be58e3997d0d | -5.8582 | -44.2088 | 2025-09-09 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d40ec4bc-ce83-333c-a5d0-a2d278d4cb37 | -12.6343 | -56.9725 | 2025-09-09 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a7fae161-755d-3f9f-9e0e-7b5ee4baa89f | -7.5407 | -48.2303 | 2025-09-09 13:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5bdd5147-4dd6-37ea-9f03-345c92db8ba8 | -13.9568 | -48.2269 | 2025-09-09 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ecb9679a-b55f-3c35-a7d1-735010dd2574 | -14.4471 | -53.2124 | 2025-09-09 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fdf447e2-7631-304c-94ee-7e20275298ac | -11.3389 | -46.5419 | 2025-09-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| b951c2de-d63a-34ba-a116-17e33983861f | -13.9375 | -48.2299 | 2025-09-09 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3b7d5fd9-400f-38d1-bc80-5b499d0cc56e | -9.0934 | -45.7088 | 2025-09-09 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 32d90845-d7c5-3ab0-8305-cf45f32fe015 | -5.453 | -43.4525 | 2025-09-09 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f2dd24c7-0599-3fa0-a2e6-cf9029c42f6f | -13.937 | -48.2522 | 2025-09-09 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 11873998-d420-38d7-afad-2788afecb60c | -5.8397 | -44.1872 | 2025-09-09 13:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| aa5a96fb-ca0c-343f-9402-4b124ca91a57 | -11.4277 | -43.6017 | 2025-09-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6f6d31cb-eccc-355a-95cd-e1a8d9c914c5 | -6.2407 | -43.4144 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 3d6e1b7b-58a7-3c36-b8ad-b58f1df3aefd | -9.7203 | -46.8526 | 2025-09-09 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3bdf5ad4-67b1-308c-8475-bd987cccfbec | -12.0295 | -51.0935 | 2025-09-09 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 02d4d549-1be0-33b9-8dcd-4349d621d874 | -12.1988 | -53.9024 | 2025-09-09 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| c8b41bff-77a0-318c-bca9-1a605784b65a | -5.5702 | -42.9062 | 2025-09-09 13:10:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 296.0 |
| 70d59435-2b76-3ec8-8828-4877c83d4387 | -11.4322 | -50.3504 | 2025-09-09 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 3136db3a-55f1-3e3b-93d9-448347dd9994 | -11.3385 | -46.5645 | 2025-09-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 44eab942-df23-3063-b1c6-b40a45100818 | -21.4355 | -48.827 | 2025-09-09 13:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ce3514eb-38af-38ed-b90f-70e34f6509be | -17.2563 | -46.7346 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 18572cf4-e263-367a-8227-351c7e0e8aab | -15.2492 | -53.7826 | 2025-09-09 13:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 47f7d705-7e38-3bcc-9b81-be9736ca1952 | -6.199 | -45.8186 | 2025-09-09 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 6305d908-db1b-399d-9626-54f39b41cbdf | -9.4435 | -60.5307 | 2025-09-09 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 4aacb93d-4f9a-3a04-9b14-17245830d762 | -7.789 | -46.0891 | 2025-09-09 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e6f9e542-636d-3d36-8cef-736a2c1c5c93 | -17.2557 | -46.7578 | 2025-09-09 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0aa7a4cc-779d-33ba-9a8d-702980880c2f | -13.9564 | -48.2493 | 2025-09-09 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4f8204b9-665b-38d9-b0ea-0cf0b4479957 | -9.0931 | -45.7314 | 2025-09-09 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4e4ce714-8ad1-385b-8ad9-97be6adb00c1 | -12.1991 | -53.8817 | 2025-09-09 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 261.3 |
| 5740af2f-7480-393f-bdc3-684cc8970268 | -17.2557 | -46.7578 | 2025-09-09 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6919b9df-5b39-359d-9d12-1ff44976a136 | -17.2762 | -46.7305 | 2025-09-09 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ce0205ef-8955-3f08-b9e0-80c55dc17306 | -9.9653 | -51.1822 | 2025-09-09 13:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 56f6b0c6-5882-3302-b1b7-5f33ae6eea06 | -9.4435 | -60.5307 | 2025-09-09 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9e1f039d-7f4a-3d69-be35-68fa7594fc25 | -17.2967 | -46.7032 | 2025-09-09 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 32d0ea73-4e05-3238-95d6-1bd9d8cc2213 | -5.5702 | -42.9062 | 2025-09-09 13:20:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 361.1 |
| afafbecb-eb12-34eb-9490-4e5008cbae7c | -16.6297 | -51.8446 | 2025-09-09 13:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f3fb138e-df22-311a-84fa-84bf7a6a566b | -12.6343 | -56.9725 | 2025-09-09 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8a9814b3-7386-33db-bd72-1e38c0e44fbc | -14.2757 | -44.9357 | 2025-09-09 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 895efa7c-d7d8-36ba-94c5-61d5cbc12f94 | -5.4343 | -43.4538 | 2025-09-09 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 96c44680-ce8c-3c89-aed2-b9e7e2623dcd | -6.2407 | -43.4144 | 2025-09-09 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| a98573d6-257a-33af-b8a3-71d453e2e08a | -12.1991 | -53.8817 | 2025-09-09 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 260.0 |
| 5cc80583-82f9-3240-b10a-c54d3ffddb05 | -17.7127 | -44.4684 | 2025-09-09 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 92e5aa20-e293-3938-84ce-4676a0ac1c63 | -5.8582 | -44.2088 | 2025-09-09 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f65ca9b0-0194-3b2c-b423-c4ffb5b1b943 | -5.9899 | -46.2141 | 2025-09-09 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f8e4d7c1-7266-3639-8247-766570926a57 | -5.8397 | -44.1872 | 2025-09-09 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b67e8a6c-3acc-38b0-8eb7-9ac9e3f87f4d | -11.3011 | -46.5244 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9e9e6939-e41b-3635-9f0c-69c98f7d3edc | -11.9926 | -51.0126 | 2025-09-09 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2d6913fd-560f-3d46-89a3-765a1e88ccb4 | -11.2823 | -46.5043 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| fde89748-9016-3cdc-a348-37163b399b14 | -11.282 | -46.5269 | 2025-09-09 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README78.md)
