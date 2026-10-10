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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6701958e-433b-365f-8d41-04181259181c | -7.02341 | -45.31414 | 2026-10-10 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d91f8df-e185-3f4d-afbe-91efef19895e | -5.14519 | -45.76717 | 2026-10-10 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f344ae22-2ab1-3398-88c0-436438472d88 | -1.2659 | -55.74547 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f8bf6b-087d-3f62-917b-2375eae094b5 | -3.30811 | -54.02062 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75f71760-19e7-3f3b-9d35-a76eb00b6e2c | -2.37954 | -47.60627 | 2026-10-10 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8437721c-4353-36a9-b6a1-1ac8fde436d0 | -2.0451 | -56.38432 | 2026-10-10 04:44:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fb028d9-4c5e-3295-8489-7e1253051d3e | -3.52038 | -50.40105 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16550c56-1af1-3487-b8fc-db800d5fb813 | -2.44954 | -58.03251 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98eca0cb-9362-3b1f-bde1-073a0d84cdd8 | -3.34693 | -50.41499 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a90b9a5-a791-333c-bb46-389abb995887 | 0.49386 | -50.78849 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6834b863-6387-3543-aaa2-10e95d3e4b73 | -5.74957 | -45.12196 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4888fbb5-8f77-3ecd-a1a6-d66b31610a70 | -3.29754 | -50.3306 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c1a30c9-3d3f-3938-a08a-ff263227fad3 | -4.09936 | -54.01841 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e4db1ff2-8432-3c2b-b2dd-3391245c95a2 | -1.51141 | -54.52483 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e6f0a80e-985d-3999-9c18-a491cc82ea2a | -4.74245 | -55.67469 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d39d1c46-1ac0-3d2c-a69a-d7160f7d3ac9 | -6.33932 | -46.03086 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ca4b813-e311-333d-979e-5ef143cf0307 | -3.48731 | -50.48763 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d6a40b6-90ae-3739-a41e-422aab3f697b | -4.09781 | -53.99916 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48ad34a9-f666-381b-90de-bbe69dde13c5 | -0.91702 | -52.44053 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d72a7aa1-d015-32e8-b24f-e24be00aa335 | -6.88028 | -45.91459 | 2026-10-10 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a876cb-4cab-35f0-bf4f-2202c16bc6c9 | -4.10129 | -56.12822 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb26b2f4-a612-36b3-8b58-2da666f85e28 | -3.56763 | -54.69595 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 732a2ed5-086c-34a8-99b2-7f3d4a307892 | -3.77493 | -60.71248 | 2026-10-10 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff9ce18e-2e3e-3ceb-a876-cd09560d887c | -2.858 | -48.72174 | 2026-10-10 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53166a73-8b47-3a5f-8755-fd1d5e06d864 | -3.58907 | -54.71575 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 383c5d08-3889-3cb9-bd4b-79b4ade18697 | -2.89049 | -54.07182 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57d64158-01ca-30de-a9e4-6879e7105954 | -2.46638 | -56.05807 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b5ff149-4581-3d2f-bd35-0aae65bb0f50 | -3.90624 | -58.95265 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 173aab54-c9af-36f6-a480-81464f329290 | -3.77765 | -60.71262 | 2026-10-10 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 414766d3-a73a-3e60-9fc2-62589b209a7b | -1.08029 | -54.10934 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b95d1cf-b010-3572-8fef-4f6cd13a6394 | -4.12731 | -46.86989 | 2026-10-10 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd02d0d4-820d-3d82-aaf0-2d9bb98cccac | -3.90305 | -55.8141 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e0b8f79-c5d9-33dc-b78d-540de8cbd640 | 1.73345 | -55.5691 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aacda192-098b-3437-a6a5-ed16a0319d85 | -3.11744 | -54.17364 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 879d416b-fcbf-31d9-8721-18046518d5e1 | -3.54026 | -54.73999 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7aa5b456-aaaf-35b8-9163-75b3a2181377 | -5.1095 | -46.21768 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88225138-6df4-3489-b6af-f69115e93a03 | -5.79971 | -53.80423 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a26b34ca-0018-3277-b274-ecbcb7a4764e | -3.7613 | -45.95826 | 2026-10-10 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7b4a242-1f3d-35cc-a21d-f51ff5d159e2 | -3.53544 | -54.73908 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6ecdf66e-b625-386f-8519-e2f26895e6c4 | -3.21032 | -50.5453 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 947d29d6-85ba-3340-a88e-eb6a9b4fbdd9 | -5.53507 | -43.05441 | 2026-10-10 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab9a5369-1993-3df7-a81f-e61d2f3a5914 | -3.75118 | -50.01234 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e6e8486-9322-357b-9cdc-007d2c2a0537 | -4.40133 | -49.7813 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| acede256-5669-3f57-a95b-3f68ea414d95 | -3.38035 | -44.4846 | 2026-10-10 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3d4410c-4045-3a95-a465-eeea1698827d | -1.64926 | -55.19891 | 2026-10-10 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4055cab6-77f8-350f-ac07-639acb64a4d8 | -4.68335 | -47.43671 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62003613-a232-3230-888f-5caa27539357 | -5.8883 | -43.4116 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e30c292b-abe6-3a15-8cd9-36de29ea1c7f | -1.8845 | -54.68502 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 568f90a3-3092-3baa-b432-67b0d589c725 | -7.06152 | -40.95826 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2e11e73f-4435-350d-8085-7211cdced539 | -3.75183 | -50.00829 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f8dbb4d-5b47-3650-b0d3-34a75b3c7b0e | -3.04289 | -53.89351 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3fd8be66-f33b-39cd-86a3-4354de06bfd4 | -3.54418 | -54.74617 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f3780d51-12d8-3494-bfbb-d71bbb17da64 | -3.47213 | -46.06931 | 2026-10-10 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff97f9bc-b1d5-344f-857a-2de447ef859d | -4.74298 | -55.6716 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c82e81a5-5998-3a03-acae-59175a980750 | -2.61284 | -59.98046 | 2026-10-10 04:44:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07709c08-3307-379a-a89d-4ffdd0d81d56 | 0.4773 | -50.78598 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| eeacf6c2-21f9-3c4d-a120-c5f38ce2eab5 | -3.2784 | -54.7021 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d3f97fb-0020-31c7-909f-756976bb5075 | -3.22674 | -53.97469 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0183da1c-1402-3eab-b461-ecd64d856ad1 | -3.17959 | -50.59405 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1905bc64-ee0d-3be7-8411-55c5900bffb2 | -5.23198 | -50.68101 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85a9c223-719c-3093-a2b5-ad4545cbd2ab | -4.36843 | -54.76327 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e456521-c44b-3b43-8228-ce322aa1f564 | -2.43082 | -48.20154 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f02254a-d48b-3c38-98e1-145276491e3d | -1.62959 | -54.42437 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a4ecf71-069f-3581-8392-7f4da64e13bd | -3.95593 | -51.88748 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e649db3d-5d07-32c1-8716-86d0aa1b4fad | -3.87839 | -55.99216 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c99a7e3-3daf-3282-ae67-cd682ffb1594 | -1.63876 | -54.39845 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06484827-3f60-30da-ade8-8dfb42c0105c | -5.79463 | -53.80768 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e57b399-825b-3fab-8471-0ac22aab5148 | -4.81902 | -56.07875 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a048596-7f1e-3b5c-9c28-426017f5541a | -2.52625 | -56.26847 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4f60377-06f2-3fa7-919c-721bbaf663b4 | -3.05217 | -54.03643 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 728258c5-228e-3d85-9fdf-c43404696e0e | -3.19482 | -50.54726 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4d64d89-3729-3e6c-bfbe-3ae5b32fda7f | -4.31904 | -46.29861 | 2026-10-10 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37b038e4-7207-34cd-84f6-89155edcf344 | -5.62066 | -43.64819 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35ccf509-a0ee-362a-896f-39a616f3633d | -3.30046 | -54.00947 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b18363-fc86-3ada-b4e3-c2d7b278382b | -1.6328 | -54.43555 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd6b04f0-b65d-3875-b613-947f80913cc1 | -3.16918 | -50.58788 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58efaf57-1bd6-3bc3-8d13-dae87f11e951 | -6.544 | -46.55209 | 2026-10-10 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b544f915-5791-38f3-9806-d999b1cc39f0 | -2.5662 | -57.42081 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 52b63e7d-d68a-31b5-8a5d-d439c514fd98 | -2.99499 | -53.90244 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fcee4af-b134-31cb-a809-39dcaedf91e7 | -3.2201 | -54.29116 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 789e10dc-ab55-324b-84f0-d3f8f6a6e74b | -3.26564 | -54.68916 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 604ecf06-62f8-3749-905d-194222ce7bdd | -3.37675 | -59.3863 | 2026-10-10 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bac3fcc-a7c9-366e-823b-fbe5b8197968 | -2.54859 | -58.03714 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb4102b7-34df-392e-8484-7f3f5cfb1df3 | -2.20732 | -50.82552 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27e113b5-14ae-383a-a4a0-efef674106bb | -4.09856 | -53.9946 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 386f8dfa-0a8e-3b01-9d0d-2d576a82d2a0 | -2.99026 | -54.17649 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87464202-e2b5-3c1b-90f5-1bc7918f119d | -2.72558 | -54.14504 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2b5c764-af03-3984-a362-271588821102 | -6.3591 | -46.43897 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db889cd-7f8b-3b4c-8b80-4772289d1813 | -3.11567 | -53.7957 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7474072f-d5bb-3b6a-b764-50ffe476e75a | -3.18307 | -54.75066 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f71bf6a9-5c0f-3733-808e-5c9c40770a22 | -5.89215 | -43.41221 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f52b6872-b459-3ea2-b7b5-43bdede8c3ce | -5.69715 | -53.46254 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65a6bad1-4274-3328-9fb9-e1d73ca34fa3 | -6.72974 | -46.45578 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0e3808e-03f4-3179-bef8-2bde24a8396b | -3.10453 | -54.18495 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9450462d-48c3-38d5-a4f2-ff0d24f7a922 | -7.20545 | -44.35041 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0332897d-7381-3ab5-b48b-bf3d61611feb | -3.24866 | -54.03524 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b470d017-c9e7-3a79-8e7a-4ba373bef9e2 | -3.1094 | -54.19279 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f1200bd-b832-31ff-8474-d59d86f3fa9a | 0.28525 | -51.41216 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e2ef24-ca2a-3ef6-84f5-d2453a3666ea | -4.22424 | -53.82915 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b3e75ac-1189-3e8b-9741-6c8a2380a00e | -2.39647 | -57.90013 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)
