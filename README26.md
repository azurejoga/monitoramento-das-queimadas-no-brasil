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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef61cc2-f18f-3c6a-84d6-5e0c4845ecf0 | -1.46457 | -46.04072 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea89329f-9593-3220-8dba-7398dab9255a | -4.31897 | -38.12626 | 2024-11-24 03:34:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a9a4e4ea-05ef-3b3b-94c5-10aa274408b6 | -4.54297 | -42.91493 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a879fb4-9363-3e7f-8037-efca973a3454 | -4.99747 | -42.94854 | 2024-11-24 03:34:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c349ae-ed3d-3aeb-8f07-2e8b76d1ef89 | -4.53006 | -42.90555 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4b5fac0-8a9d-3fd2-adae-6c6e56c1e71d | -4.69825 | -45.69461 | 2024-11-24 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18747ab5-6153-357b-ad03-c322357025cc | -3.9502 | -45.99634 | 2024-11-24 03:34:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 10846054-83ea-3144-9a9f-d2048bc9666c | -2.2114 | -46.38854 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc63ab1-757f-39c6-9d1d-25129dde94b1 | -5.06879 | -42.57092 | 2024-11-24 03:34:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6858e968-1a3a-3430-ae37-a190825ba551 | -6.25168 | -43.56245 | 2024-11-24 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a839e10b-9e5f-3234-bb81-687c6ad5f844 | -3.1737 | -45.30314 | 2024-11-24 03:34:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78bab34d-b05f-3935-b53b-fe933608f48b | -6.03776 | -44.03973 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95acb851-d3dc-31a1-868e-40bcc8448e6e | -5.10394 | -43.15473 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d9197192-3afe-3bfc-97a8-a90814fd5793 | -3.13383 | -45.37368 | 2024-11-24 03:34:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81c43fb3-8b6d-3e5d-980e-bb677f7f0b18 | -2.21858 | -46.38979 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 063abd6f-7705-3015-868b-cd0b9446ec65 | -5.06819 | -42.57438 | 2024-11-24 03:34:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 20b2711f-2de0-3fe7-b3d0-47b528e081f6 | -3.29824 | -45.72376 | 2024-11-24 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980bc452-be6f-3df7-a6f1-5e0d95abfa7b | -7.64093 | -37.99617 | 2024-11-24 03:34:00 | NPP-375D | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1fa8482-5c2a-383d-ae1d-df3c8ee10b0c | -1.42536 | -46.05599 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e606e0d-edae-3cc0-8b91-74bae6c40afe | -5.68863 | -38.04351 | 2024-11-24 03:34:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dba5b398-267d-3961-b7fa-f86ca1df1661 | -3.28935 | -45.72802 | 2024-11-24 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a7d48bd-c86b-3418-b40b-29c1d764571f | -4.19235 | -42.96597 | 2024-11-24 03:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab7e7b39-e653-32ef-ad86-bc7210ca1076 | -2.21944 | -46.39539 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f14a7ffd-8910-3f45-a929-69e949bc85bc | -1.4634 | -46.04766 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4427cb76-a21a-30e6-b394-885826ada616 | -4.54735 | -44.01417 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aba8c47-478d-395e-8c17-6011536dfb84 | -5.07793 | -44.16961 | 2024-11-24 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30527430-c50e-321a-9201-2944f51da609 | -6.84555 | -39.43439 | 2024-11-24 03:34:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4e091bb2-8011-303f-a207-d19cee16ff80 | -7.39747 | -34.82545 | 2024-11-24 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 67b3c072-63e6-3333-92ff-760b87ff0c7a | -6.05551 | -44.04239 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f444409b-ba73-3e9b-aa5d-41418c5185c0 | -2.70234 | -46.28661 | 2024-11-24 03:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2826e6a4-a714-3d2f-bd7d-f89eb0d25373 | -7.31225 | -38.57208 | 2024-11-24 03:34:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17fa796a-332f-3f65-b4e9-590331c9ab99 | -3.60169 | -41.67522 | 2024-11-24 03:34:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bd85c01-3759-34b4-89c2-68fd306b7c08 | -4.41273 | -44.09729 | 2024-11-24 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b70da528-ce7c-308b-a209-e441a791e009 | -5.00372 | -42.94566 | 2024-11-24 03:34:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5696fd28-e5ac-352e-a948-591e0119e2cb | -3.29615 | -45.72924 | 2024-11-24 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35cddba7-1cdc-34dc-b2be-d1c5d9b5e6c9 | -3.13279 | -45.3796 | 2024-11-24 03:34:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5343e565-3a7e-3ead-8a91-1fe2f7455240 | -4.4248 | -37.80463 | 2024-11-24 03:34:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bd63603a-99ec-3cd5-98e7-80c535cda4d4 | -5.00305 | -42.94953 | 2024-11-24 03:34:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e70e5372-1822-38ea-99b7-d90cdc83c289 | -8.14287 | -34.97001 | 2024-11-24 03:34:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b675e8fc-abab-3b65-9e3d-4bef36be62e0 | -5.60242 | -46.29357 | 2024-11-24 03:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f1c75e4-b41c-3118-b4ee-865fc32fe5e9 | -1.42242 | -46.05725 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45a29919-93bb-3379-9814-41a07b0daa33 | -3.69767 | -42.30802 | 2024-11-24 03:34:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ece8b27d-dac6-3ce4-b2a3-8f25aa8e2d1a | -6.0578 | -44.04881 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99bc84ec-ffd0-304f-b23a-1d7ae1229700 | -5.07965 | -44.16759 | 2024-11-24 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47fd33d7-563a-338a-b4d2-b10e5e5f96f8 | -6.05266 | -44.04363 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f990d0d-8a05-36dd-9bea-e067247390dc | -7.63961 | -37.99353 | 2024-11-24 03:34:00 | NPP-375D | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9513703d-afe8-357f-833d-bc98866da385 | -3.10464 | -45.77869 | 2024-11-24 03:34:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| dfd6db06-b26e-36a1-9e47-af27d89cb389 | -2.86798 | -45.83875 | 2024-11-24 03:34:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8a9a13ca-434a-3072-af20-5ee3adb75a56 | -8.1007 | -35.20966 | 2024-11-24 03:34:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 76194bf4-cf9e-3e86-9e09-8e5f281076f4 | -4.53247 | -46.42333 | 2024-11-24 03:34:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f406cf4-3a19-301f-81b1-362351d400ab | -5.07871 | -44.16508 | 2024-11-24 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e9771ec-92f4-3f4a-8e0d-cb970a0c86af | -3.29033 | -45.72881 | 2024-11-24 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bf5ef1b-4dfc-313f-ad9f-4cb4e38653d5 | -7.09928 | -39.93086 | 2024-11-24 03:34:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4feb5e17-ee72-3ab9-bc64-fbc84bc3e632 | -3.79211 | -40.99997 | 2024-11-24 03:34:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5719a4aa-649f-3f48-abb1-aa2cb21a25e7 | -3.07897 | -40.06712 | 2024-11-24 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 242453a9-1119-3f27-aff8-636d21f869bf | -4.535 | -42.91031 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5f45d36-0d39-36fe-afde-a6d6fc2317a1 | -4.19445 | -45.36155 | 2024-11-24 03:34:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dd7e14a-f249-3154-b47f-0833c98f9d7d | -4.53298 | -42.90561 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 802942c3-309c-3d3b-b1ae-e9bbbf8155c2 | -3.10271 | -45.78832 | 2024-11-24 03:34:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5b617353-ce07-3d74-8f34-38566e22b8b2 | -6.05407 | -44.05068 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b80eb20-1067-3a6f-9276-8e67eb194c9f | -8.14622 | -34.97057 | 2024-11-24 03:34:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 63bb2505-70ec-3f9a-b955-95ecbcaf0dd2 | -4.54656 | -44.01862 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e405cc2f-0e43-388d-b725-c0b5b1077c76 | -6.34367 | -39.61376 | 2024-11-24 03:34:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c308d61-0d6e-352d-a36f-b1b4eefa1a2c | -6.05481 | -44.04643 | 2024-11-24 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5853be2-668c-3eba-a898-6d76a8e4ae77 | -4.5336 | -42.90195 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b80e29-a439-3617-8c50-f7947ad6dbf5 | -5.64814 | -35.47108 | 2024-11-24 03:34:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea091534-1de4-3b70-8a8f-046c082ffaab | -4.59812 | -44.72665 | 2024-11-24 03:34:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8437712c-7e90-3b47-b54d-908e5efa00bd | -4.70108 | -45.70204 | 2024-11-24 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f830ff0a-f094-3c2f-859f-515e457a08bd | -1.46862 | -46.04331 | 2024-11-24 03:34:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61225894-5125-30fd-a460-3a04df96451e | -6.4377 | -37.45135 | 2024-11-24 03:34:00 | NPP-375D | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cac93dc9-2083-38f8-985c-46ce7a698b7e | -3.84298 | -44.05419 | 2024-11-24 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b9c5f30-4b42-3905-bc54-a7429c5775fe | -7.69253 | -42.98154 | 2024-11-24 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45c393a0-45d6-3d92-8423-32638cfa2c18 | -8.05484 | -47.09032 | 2024-11-24 03:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e5ac7d-935c-3f96-a693-3fe884b9fc40 | -8.04796 | -47.08916 | 2024-11-24 03:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f945dbf8-5a9f-37a1-acb2-0c652fe56f74 | -8.75678 | -35.2377 | 2024-11-24 03:36:00 | NPP-375D | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ed64b432-2f0f-3601-b120-49c1d251dcea | -7.77795 | -38.39544 | 2024-11-24 03:36:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b50752a-1877-30c8-b675-81859254f661 | -8.11721 | -37.19088 | 2024-11-24 03:36:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73c0720c-4a71-31b7-af5f-7a6e6ea66316 | -7.32433 | -45.47588 | 2024-11-24 03:36:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90883774-b50e-3093-b154-782c375632bd | -7.68779 | -42.9772 | 2024-11-24 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f06e841f-dd3f-34f9-8d1f-5abd00e42d91 | -6.63434 | -47.34692 | 2024-11-24 03:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 473d02c9-2907-3f0f-878c-3420a62002b5 | -8.8296 | -35.67057 | 2024-11-24 03:36:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9a5729c8-eda0-3d45-b6b5-f8b2dc21e9fa | -8.21991 | -37.38424 | 2024-11-24 03:36:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2e55f44e-fac8-3c27-aa29-8100b9a5da7d | -8.75342 | -35.23714 | 2024-11-24 03:36:00 | NPP-375D | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ba7df707-9e4b-315e-bd52-7b3521cdb6d1 | -8.50214 | -35.0351 | 2024-11-24 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| de0922f6-7d2e-3f27-8020-b8c674f90940 | -6.63701 | -47.35098 | 2024-11-24 03:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5299b4a2-05bf-30e3-9c80-23a3272870e2 | -6.64138 | -47.34859 | 2024-11-24 03:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d511383-9d7c-387e-a279-3a36de3f4549 | -7.68718 | -42.98057 | 2024-11-24 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8707989a-4a5c-3c56-a218-2d3f6fd96657 | -7.81889 | -44.19042 | 2024-11-24 03:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79593b25-835a-3f84-be72-d583a796ec1f | -7.68839 | -42.97384 | 2024-11-24 03:36:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0af2b9e3-b31d-3a77-a253-a30b3824cf62 | -7.8196 | -44.18652 | 2024-11-24 03:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae0b0017-5ec1-30ef-b440-8f7a82190649 | -8.30953 | -35.28049 | 2024-11-24 03:36:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9c9301e0-80ae-3a10-bb6a-886ea02ea36d | -8.73638 | -35.53548 | 2024-11-24 03:36:00 | NPP-375D | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ffe1bc4d-0a5c-35ce-b206-c03d86018c56 | -6.63837 | -47.34385 | 2024-11-24 03:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4cda2a6-77d9-3911-806a-7d9c7feaa826 | -7.69192 | -42.98491 | 2024-11-24 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5be1819c-c9f7-31ca-8178-6dcbd5c7665d | -20.7943 | -41.12742 | 2024-11-24 03:38:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 85816caa-3292-3acf-8d62-d00bdcd85d76 | -5.0998 | -43.151 | 2024-11-24 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a199f022-2e13-3811-a575-aab9c505410b | -2.8651 | -45.8437 | 2024-11-24 03:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 88de972b-8f08-33c0-9e84-7733a435054a | -3.5159 | -53.8132 | 2024-11-24 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 54117e9d-27d3-3d88-b0c1-dee05a6a6e77 | -1.5129 | -54.1759 | 2024-11-24 03:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 10174d56-3a32-3020-945f-90643f553ae5 | -3.0355 | -49.4476 | 2024-11-24 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |


[Clique aqui para ver as próximas entradas](README27.md)
