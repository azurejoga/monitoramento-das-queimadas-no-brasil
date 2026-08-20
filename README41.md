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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8194d814-da65-36db-8c2f-7653fbeb5513 | -7.75735 | -49.20163 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3be61d89-3d14-3266-9cbf-ce3a3fdb4031 | -7.96522 | -44.67044 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5db011c2-8307-3ac3-ba55-140f41edb854 | -4.45666 | -55.45275 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc7e8051-e28b-352a-8b69-0f3e5ffe88ba | -5.80026 | -55.70991 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c74dccbf-a0bb-3428-bce1-78d521fcb4f2 | -6.58674 | -58.97533 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d93d94b-c728-3d4f-bfff-7403d1b028d5 | -5.80525 | -55.72128 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a49a434e-a1ce-3d12-b458-0834e3241be2 | -6.62141 | -56.26812 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 497a5949-d107-34c8-8c49-b5951bf0874b | -2.80541 | -48.59292 | 2026-08-20 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4670fdd5-bbf1-38de-8b16-c055f45ce499 | -1.83806 | -54.48996 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 482a5cdd-9b97-30f6-b2e1-3b0b70515644 | -6.59589 | -58.96412 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70112912-871d-35b6-aa9c-5696856102e5 | -6.08466 | -57.91975 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 886bbaf5-42eb-35f7-9205-ddc0ea27cd07 | -7.46433 | -45.15108 | 2026-08-20 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d65bf78-d623-3e39-873b-0499fe5129f1 | -6.25169 | -55.40981 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79496420-e5e2-346e-ae6a-32a79540b2f1 | -6.87592 | -56.42228 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e24674a4-9c47-3bf2-b782-84b6c911ad12 | -7.36115 | -45.82864 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83fe1608-4f0d-3389-a16a-37543bb4dd7c | -4.01599 | -48.9596 | 2026-08-20 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117fd597-c96b-3113-b746-f15d48df1fe1 | -2.57281 | -47.24698 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 17497b55-6aae-3ab0-a28b-ee53ca9f0c52 | -5.82401 | -57.63814 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de02727-d34a-34cf-ad35-64d3ed7600ea | -2.84936 | -60.16867 | 2026-08-20 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb86a8ca-b53b-3deb-9173-0d35843ed093 | -5.79641 | -55.71285 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e7b5ca5-2a41-3f63-b217-157f6b9a7fe7 | -1.81121 | -47.19686 | 2026-08-20 05:04:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76fd24fd-7c7f-3344-a5ab-cb57ecd0a4be | -3.1026 | -61.21991 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64b9607e-14b6-32e7-be7d-b490b13747b8 | -4.12799 | -49.44566 | 2026-08-20 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbf97029-bae4-304f-b3fd-02daa1c998f4 | -6.4408 | -52.74402 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b06da553-8bf9-3cb3-b5f9-04b357841e22 | -7.00135 | -48.04361 | 2026-08-20 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c37b1d5-e874-3060-938d-6ace65ab30e6 | -3.05514 | -46.92799 | 2026-08-20 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7c85b1b-4128-3ae9-ba12-68767030e649 | -6.43671 | -52.72205 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90003ce2-5ee9-3d91-96ce-a1fd02ac766f | -3.05556 | -46.92511 | 2026-08-20 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b3340f7-d167-305b-ab52-68d7cfc7a232 | -6.29459 | -43.64987 | 2026-08-20 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9112f586-c15e-345c-b028-41e9cba4a6d4 | -6.24838 | -55.4093 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ddae452-0140-3f68-b92d-7934b5126744 | -6.3577 | -54.90095 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38e13425-4957-3e10-a98b-fd38713f6df8 | -3.84033 | -59.37337 | 2026-08-20 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fcfb4f2-b589-3e1e-970f-63886dc56540 | -7.35562 | -45.81797 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e5eaf898-6bbc-3c42-870b-19db4bf76cb4 | -7.35016 | -45.82307 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 641f0adc-f051-3deb-9282-5303fe9cee7d | -7.59963 | -45.18187 | 2026-08-20 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be01042c-4f8d-35d4-996a-a8a204dece07 | -6.39088 | -54.94907 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 735cfebf-5b4c-3433-bd00-8d337b51e82b | -3.9682 | -43.11366 | 2026-08-20 05:04:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 721eed32-efe5-3b58-9a52-ef50bfcb6b58 | -7.97273 | -44.6613 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cce40a40-e27b-350f-9a0f-b54046048cee | -5.4337 | -48.41416 | 2026-08-20 05:04:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc4e3158-6613-3eda-8ba7-5c1a51bb535c | -3.93297 | -59.32992 | 2026-08-20 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ce4d47-d868-35f7-af30-14dee669aa85 | -5.8041 | -55.70697 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d6dfb94-b6d3-349d-89cd-b41a6a6509f1 | -2.63781 | -47.98449 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c05f1d93-33ce-3027-9c13-93f81bee627e | -7.36028 | -45.82678 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 252c40df-54de-3723-914b-e5c226dfff6d | -4.95424 | -56.27081 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46e26d15-63eb-33df-afe7-7572aa08900b | -4.90069 | -46.82965 | 2026-08-20 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13159325-2d9b-3d34-a308-d9a463f31e46 | -6.43546 | -52.73041 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 00afd4ea-16ed-306f-87c2-15e137e4bb38 | -6.71603 | -59.08797 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e03f80f-8bdf-351b-8c3e-b18795c32d84 | -7.35343 | -45.834 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 878804ba-b421-3355-8975-0efe0e685ae5 | -6.20677 | -57.77076 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ab6fea-1b96-39e6-b13f-57f5701bde32 | -6.15074 | -57.85728 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35a02904-2187-34a6-b367-386a21c00db1 | -6.64602 | -56.41394 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| daabe821-cea0-3850-b07e-dc6f2298aeb7 | -6.2473 | -55.41623 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0299e149-2904-38ee-b94f-863505268986 | -3.12723 | -60.69796 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71fac455-421b-3fa0-b590-324fbe2825d5 | -7.34932 | -45.8212 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5a9ab621-e59a-3f75-80da-1643aba8cf4d | -6.69212 | -52.09383 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 516faa0b-3f3f-35ba-9766-bbe83cc7b5a4 | -6.61499 | -56.35225 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69c20c43-5af3-3902-81a1-58d01532ab71 | -6.40862 | -54.9446 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35c13cab-d0b8-3768-ba01-033ce3bcf0fb | -3.97639 | -49.19169 | 2026-08-20 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 344ce7f2-33d6-3c4e-9608-2b67fc3b962a | -6.35715 | -54.90448 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69b44923-47a4-31de-a38c-2f4aecae2694 | -6.09989 | -57.86834 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff68b7ef-dcf0-3a98-862f-e7035efaf3f9 | -6.0051 | -57.8691 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e914b787-dd3d-314f-b945-d570dd6f87f6 | -8.05522 | -50.10447 | 2026-08-20 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e5cb618-fc69-3836-9c2f-939b881dbbb1 | -6.70183 | -59.10689 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8d06a5a-5d51-3ff3-9907-95aef8f7600b | -6.70147 | -58.93848 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b950f092-0a75-3f26-a73a-ad87db5651d5 | -6.35824 | -54.89742 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0e81b92-dc69-3d18-bfc6-1d6b97a9a419 | -4.44384 | -55.38018 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d2e18f3-1828-3676-aa92-26687290e156 | -4.90028 | -46.83261 | 2026-08-20 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d407054-0ffe-3f78-a5f9-ea24ef81ed59 | -3.25429 | -52.91656 | 2026-08-20 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3466ec4-128d-3457-b9af-9195a9141938 | -2.8105 | -48.58924 | 2026-08-20 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0ab0552-5167-38c3-ae9f-e227c1699db2 | -2.56795 | -47.24617 | 2026-08-20 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cd995b9e-ead9-3252-b33c-3c82d3f1bfc4 | -6.31856 | -55.91919 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b21556b-63d9-38cb-9013-ce830cace49c | -7.34987 | -45.81715 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 730a7348-7c34-3506-a379-c34b6148a0bc | -6.43769 | -52.76482 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92387df-c7dd-3a1a-93db-1322dd0afe0b | -4.95478 | -56.26734 | 2026-08-20 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2920c773-9590-332f-9067-8a10415cae43 | -6.83296 | -56.4582 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce98a910-6c64-3999-9528-13faf40d3c6b | -7.76195 | -49.20229 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dcb4c01-205b-3aec-8b8d-fc7a29fb1a09 | -7.34338 | -45.8303 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d79a50e7-63d4-3b89-a8f7-572dd3f08ad2 | -6.78283 | -42.87778 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c152ad10-3df6-3ea6-9851-59a5dcc20214 | -6.00854 | -57.86964 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 565179fd-0143-39d1-a0d7-ff3bfef0de16 | -6.60175 | -56.35019 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f9524d-a4b3-3302-9baf-818470794c35 | -2.64171 | -47.98999 | 2026-08-20 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4afea51-7c86-3cda-8fc5-d0ee554851d3 | -6.65268 | -56.43635 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b183e7ab-ab5c-3cdc-95a9-c27f7aac85c5 | -4.3853 | -55.47332 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9afb926-0311-3d5f-9d32-99dc1e95c7c5 | -6.31141 | -55.92162 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6156d0c-4cae-3805-b9f0-1b84665348dd | -3.91299 | -56.12133 | 2026-08-20 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fd09f4b-d206-3cc5-9783-7a296bfde598 | -5.42883 | -43.43579 | 2026-08-20 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cf3fc1d-ee23-327f-ab5d-216099732858 | -6.38249 | -54.93699 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5c7457c-02c3-36c4-8e58-61664e180806 | -7.34714 | -45.83726 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98afb0c5-7de5-320d-beb6-4ec46470a2c3 | -6.73923 | -59.03644 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29398517-aab7-3d97-9477-3b7b4a41c773 | -6.00287 | -57.86098 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329bad2e-e0f4-313a-92c9-64ebb8c1980b | -6.58316 | -58.97474 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 24572045-8b9c-3dac-a335-929da32bcc33 | -6.35436 | -54.90044 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54fc217-3dae-329d-bfee-dc52592b85ae | -7.76198 | -49.20435 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 06f14949-b73e-3bc6-b7f5-c60277dbe768 | -6.22329 | -55.61438 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09d3557b-22c4-3d05-9860-c312ad34b134 | -6.38141 | -54.94402 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 408787e7-2166-33c2-9cf6-0c4840642d0b | -4.09657 | -42.50312 | 2026-08-20 05:04:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 234aaf50-7ae8-330b-9a87-16819eabbbdb | -3.01322 | -51.06152 | 2026-08-20 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3be33909-de9d-30f9-b3c2-d269951aea89 | -6.95138 | -52.81026 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e725a8f4-671c-3b34-8171-12ed448835d6 | -6.39878 | -51.75187 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a21389c8-cde4-3bbf-9309-5471ec2b07d3 | -6.70096 | -59.0897 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README42.md)
