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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c304244-3b42-3089-8e23-ac0ab1e1f9e4 | -12.10666 | -44.84637 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc6373d2-466b-399c-8a39-a8fb3c92b4d2 | -7.8799 | -45.62885 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d868f34d-ee6a-3640-a12c-d6fdb58f8d00 | -9.18277 | -45.32284 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1676d6d3-033e-3f9f-9a9b-5bc4fbde54e4 | -9.2087 | -40.24826 | 2025-09-19 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e84cae17-37c7-3d9c-aa70-f533bab78998 | -5.98444 | -45.73023 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e07b02d1-b29d-3c54-96f2-72acb0a85a62 | -8.09058 | -49.91653 | 2025-09-19 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe06b61-05c1-371c-8f78-e68c03dd7454 | -10.33147 | -45.25039 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 479104e6-b877-3932-ad36-5e0de77fdf54 | -5.66535 | -45.03724 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d45660a-9a56-33ce-8f77-fc40f25d2ea5 | -8.09003 | -49.92018 | 2025-09-19 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c68ce649-a96c-3d43-8bfa-b9198c305f30 | -8.04193 | -45.73512 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22325745-9b63-375c-b9b9-3e9f23b1dbd0 | -7.947 | -43.87553 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caa34b1a-f7d4-322e-b21c-cf7935f8bf17 | -7.23379 | -46.59692 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97af1756-da99-3207-8d61-c0cb701b250b | -10.9176 | -45.64309 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 934a0557-4030-339e-8e13-43b644c116dc | -5.707 | -49.10019 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adc41252-4031-39cb-ae49-1208e3500ec6 | -10.67212 | -46.4468 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f88bf115-84bc-378a-bad5-55e5a4c72952 | -8.04728 | -45.72778 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88657a4f-b079-35a3-b234-64dbc0be6ea9 | -5.63293 | -45.94354 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c33a365-ccb8-30fc-a1b7-9e266ba2d786 | -6.19118 | -41.19512 | 2025-09-19 04:46:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ad27340f-a15b-379a-9907-4311981def3e | -8.23617 | -47.83593 | 2025-09-19 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5553b14-6d91-3ce7-bed6-800b704de880 | -10.37313 | -42.45885 | 2025-09-19 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 0906cc63-811b-3436-bc89-8a78135f7d4d | -9.16009 | -45.32396 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bbc5ab6-0183-38b3-948a-e99753b63fb0 | -7.57679 | -45.48201 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ffac67b6-e2ac-344d-8558-28f543bb50d1 | -7.70904 | -44.39112 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c0d81c-a55c-3f61-85f7-5c6e18c04073 | -9.18337 | -45.31844 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eafbaaa3-8811-36bf-b76b-103be67cf7b5 | -5.87788 | -45.74863 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12862d48-12df-339f-b12b-adc95b2c14c5 | -6.51195 | -51.19536 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 836cbdf1-1d29-3548-b9c1-033b1a47feef | -7.83644 | -46.216 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf8fc8b3-b1eb-3046-aaaf-164c289cb4ad | -12.10147 | -44.8447 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 936c5c06-7976-3d76-bca5-7a8a365a3d4f | -5.6863 | -51.75175 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3b4b53d-7ad8-3e41-88ff-06e5f45a6b91 | -8.02891 | -45.70485 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f413c7b-d322-3e19-b772-7024b1573685 | -7.54475 | -44.79408 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c648a49-5677-33c5-bab9-874faabd3e8b | -6.20438 | -45.1075 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a43e73b-ee97-3e2f-809b-cb033031fee7 | -6.20522 | -44.05618 | 2025-09-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46f2a390-fab5-3d17-9258-a05b6aaa1401 | -6.93551 | -44.90474 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49971c5c-f199-3ab0-a9c3-edaf926cd754 | -7.54352 | -45.50153 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1cd2d5d2-74e4-3d62-9a99-59053238a8ec | -6.2716 | -43.92151 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58c8d647-4851-3784-a384-d05c77474a5e | -7.17347 | -44.33561 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66ca0d64-9817-3936-9ed1-80a77bb0fc39 | -7.58589 | -45.4794 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| de9c180e-9f71-3279-9fcc-ad21c11099f3 | -7.56826 | -45.48075 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dfc1265c-0629-3adf-88f6-5f0049119587 | -7.22378 | -44.37675 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eccf4bb4-98ae-3605-bdbe-474a9d0d757b | -12.11207 | -44.84185 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52c88616-c925-3c20-8da3-8935edabb901 | -7.43785 | -46.38224 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59b9c2fe-e74f-39da-af9e-2b97906c2c02 | -7.54778 | -45.50213 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df49c4b5-a878-32a4-8f04-f078c16bb5b6 | -5.63644 | -45.94768 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 137e5d5d-8a9a-35f7-a891-214a61f017ac | -9.51682 | -43.06203 | 2025-09-19 04:46:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a38b3ac6-e414-369b-a67d-85ae1b5ef865 | -7.35906 | -44.5817 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a7e8a111-b8d3-3813-b089-b4c62818c69b | -12.09726 | -44.80294 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555f2002-981a-354e-821b-b0c936f33b91 | -5.83273 | -46.27807 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 223500c0-e666-353e-a512-6e7bf727dcc6 | -6.38968 | -43.32468 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a27db453-44f9-32ef-b16a-fff38ac871c7 | -7.31071 | -44.05621 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a269e991-839c-347b-afa9-e5dee8b5974b | -8.8886 | -46.13143 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1f8b86f-596f-3f7d-95c9-c15b71bb03ef | -8.92895 | -46.31075 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 019b79bc-fa6a-392b-a5d9-c53e31c6b8b2 | -6.90945 | -44.77344 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| db39bfa2-90a9-3043-af23-715959aa3181 | -11.16682 | -45.36281 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f07353dd-c4f4-3e31-8387-0e4f6116170f | -5.86834 | -45.89914 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba29746e-c359-34c8-8c82-3bec74dd278b | -9.1884 | -45.31467 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fc9ba336-869f-391e-8730-92af7391d752 | -11.18125 | -45.36793 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e334ec4c-725a-3eed-954e-1594a0302b2f | -11.09274 | -41.07049 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| eb6b8386-1c8c-3729-a8a3-7e878b6cd7ed | -11.4521 | -43.5449 | 2025-09-19 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e8e43d4-f3a9-352c-bdf8-e900be8b06d5 | -10.24874 | -48.04171 | 2025-09-19 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5ffb4fab-ccfe-3258-9368-cb1a6b9cce2e | -8.06911 | -44.09036 | 2025-09-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8114f2e0-1229-33bf-936a-79cf07aecaa9 | -7.28977 | -43.92881 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7527865a-6e19-3be7-a715-d523360cc712 | -7.57196 | -45.48528 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a49afb29-5b92-33e5-86b9-1697b33fb27c | -10.61271 | -45.17036 | 2025-09-19 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7055b4d5-ef0d-3de0-a9c2-8f046091b666 | -8.13773 | -46.78098 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a177bd46-cf70-3fab-a24a-2d2026195699 | -12.14584 | -44.9566 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab5e0746-388f-33ff-b98d-d3f7ef321da0 | -7.9266 | -43.882 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9355190-b099-3ed2-91e4-0b598da9dfef | -11.22476 | -49.63932 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f99f3df-e316-33ed-a6ec-cdeafb4cee1e | -6.38259 | -43.34029 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54c96896-4855-3ac5-9b02-09462349d893 | -8.03009 | -44.94999 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e01bc0f-3501-39c5-82ca-09b15834564f | -7.54295 | -45.50555 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3aea088-e01d-32bf-a924-150e9d1fa9a6 | -9.14903 | -44.84862 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48e77e2c-3cde-3ec8-a12d-34c5a0a782ef | -10.66853 | -46.4419 | 2025-09-19 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b63f83e2-aff7-38bb-8ac0-f13a7656320a | -5.81189 | -45.71654 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 111f65b0-aad8-3e7a-99cd-2d67058d5083 | -11.17134 | -45.36353 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 981c63d3-0247-3c76-8459-38493d59ad68 | -7.5805 | -45.4865 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d95e20f-dfff-36e6-a277-e2a67cc0a85d | -7.56086 | -44.74479 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2bd4780-e3f5-3a10-8045-2c3f8e8725dd | -10.36149 | -47.87854 | 2025-09-19 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9157488-702e-3a47-84ac-ee4b3b581b38 | -10.32692 | -45.25005 | 2025-09-19 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40fa0efe-c243-3405-8775-630cd9eb71ee | -5.47318 | -46.68976 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a74d586-9355-3896-af66-60773f18d636 | -11.08862 | -41.0686 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| d0cce3b4-52fd-37d9-b739-3fc038ac502c | -8.49032 | -44.7367 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42c900fc-c2d2-3cdf-a210-c508f9fdcbb0 | -9.04257 | -44.87426 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 331b008f-ac6a-3b33-b925-854eab5ebe8e | -7.58589 | -45.69176 | 2025-09-19 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a0478be-c583-3431-be20-4cf03b68d567 | -7.71229 | -44.4015 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afed6106-0735-34da-b199-b2569339d968 | -11.17914 | -45.37409 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09619472-f986-355e-a8ab-8f0a6e366c28 | -5.55873 | -46.2846 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68666be0-bdff-3b48-ac33-018ef9d49407 | -5.30392 | -54.45916 | 2025-09-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f39e19-a7dd-32ba-9a14-28958bd2e040 | -5.86487 | -51.63365 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6cf2575-5e95-35e2-8464-ece4f7199f0e | -7.2958 | -44.12913 | 2025-09-19 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| daede5b9-2fba-3d8d-a346-39c77bda023d | -7.92509 | -43.89323 | 2025-09-19 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1193849e-997f-3bf3-9b83-c730ef196a8e | -6.31608 | -42.9232 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a663900-2385-3396-bcb5-52351e0aa499 | -8.14278 | -43.62579 | 2025-09-19 04:46:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92f83e2a-78a3-3a60-aa92-8b6b433a70a9 | -7.50171 | -44.39989 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 532a9e0d-251f-31be-9406-3baee186d73b | -7.21975 | -44.37297 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7248a9e7-2d2f-351b-8bdd-49a2339dc355 | -9.14324 | -44.85695 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b65d508f-2530-37bd-8dab-d1f16a187a15 | -6.90499 | -44.77296 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2b981c2c-4dbf-349c-a0e7-6f802e3ad646 | -6.5333 | -45.73393 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0edb98e-64dc-32ce-a359-60db60cc232c | -11.19351 | -51.12078 | 2025-09-19 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1963e6ff-bdf3-3fdd-8459-192990734b1a | -9.72554 | -45.92271 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
