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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 786a95a2-c237-3364-8e45-75faf1810e22 | -6.06362 | -55.61767 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8021270e-b6a7-37b6-a88e-50fe117a6b94 | -2.90786 | -54.18814 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50f6fd63-ee10-357b-9e7d-138cecaed304 | -3.39487 | -50.44004 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cee7773-04fc-3b38-a35e-646c9411bf0f | -3.49362 | -59.56839 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc87107b-dbaa-3863-b4ba-a59a821972f9 | -6.13665 | -57.72804 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e63dfa0-a028-39b3-8e55-52229f22f8f4 | -7.18738 | -47.45304 | 2026-09-21 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db3ba04a-2458-3e81-9d37-b9e4a84ba32b | -5.83223 | -52.07542 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87b5a60a-a72d-3c31-bb28-ec986fc64349 | -5.80857 | -57.73711 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae271de2-7050-3ccd-bafd-170cf1e3df59 | -2.85707 | -54.20913 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfb206a7-ac63-3d55-9a36-2d008a9c19eb | -5.26376 | -55.92573 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f370a265-d9b1-3283-ba55-c106756132b0 | -6.7209 | -55.08278 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe749106-b6b4-3e92-a533-e0902e883af0 | -5.97559 | -52.19862 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26eea168-c7ac-31f2-813a-476c1989e67d | -7.41714 | -49.84282 | 2026-09-21 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed1f38bd-21a5-3dbb-85af-04608a7dfdf8 | -3.82306 | -59.33102 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07ba873b-4581-37c4-bb25-bbe072a837c7 | -3.33832 | -42.76583 | 2026-09-21 05:04:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aeedc13-8de7-3b14-a8c4-bcdc9a3f50c3 | -5.61243 | -44.84237 | 2026-09-21 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8d678a10-44e0-3794-a921-f15c00c2bae9 | -6.30722 | -60.01374 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c231ad6-bb32-3c4d-a420-e01dfdbc5c15 | -4.56163 | -56.1508 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6215286b-dff1-3888-ae2b-d48ff29517ba | -3.40254 | -61.34269 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd81ff43-8574-3498-9560-16bdbfa1178a | -4.4416 | -54.82576 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb6b23be-5b5f-3711-b046-340df8105765 | -5.27647 | -49.34033 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03840d52-c785-3894-ac89-f6aef5f8fd96 | -3.36712 | -50.44603 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf6c9ae8-bc0b-3d5f-acfb-48d6739df085 | -5.97297 | -55.36644 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 813b1d03-1036-3f9f-bcd0-37bec87ddaa6 | -4.26016 | -55.77101 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad054488-68c7-34bf-8ba3-01f88e965bc8 | -6.3464 | -59.96313 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b59c6a0a-d47f-3a83-918e-bd6d73ef64a0 | -3.44576 | -50.61017 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9919649-a98c-3bdb-9ad0-c3002c4c4d19 | -6.72423 | -55.08332 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53c5d07e-2957-36f3-915d-02164e2e108b | -4.35216 | -55.66214 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b87bb83-ec5a-356a-9f19-b6c6cbf64a57 | -6.72747 | -55.06223 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8643a11-93ea-3095-97ef-adfd4146bbb6 | -4.34502 | -55.66455 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 034b7511-0d4b-3cfd-aff8-2ebc7f6934a4 | -5.86653 | -60.16111 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b8d764b-8c71-3f6b-b17d-2598076e8ed6 | -6.20539 | -53.25176 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5bc743c-14c3-35e8-9271-c66de6738e3f | -3.08061 | -61.16946 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d409367c-707c-3bfd-9ebc-20fb54445323 | -3.30765 | -59.51973 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b985aa00-151e-389e-bd11-dcf38115ccd3 | -6.1566 | -57.95588 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1be976a2-1868-3335-9cd7-087f2630728a | -2.9666 | -54.16128 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d5567c-e5d4-3f9b-ad16-783cb2fad41a | -2.61426 | -51.72727 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35192a7b-a01f-300e-8f0b-870b6c2a43ff | -3.39498 | -59.53087 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dd9fbb9d-fcc0-3c2d-9377-a9fc96c31ea0 | -2.46305 | -49.22243 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9467fe33-bbf8-39af-8da9-5342bdbd6bc7 | -5.28088 | -49.34098 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55193067-f6dd-3848-9c8b-8e111fabaafc | -4.88178 | -55.88659 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07ed371f-9b96-3f9d-a5af-947149bf182d | -5.85408 | -53.5189 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d893777d-d467-3838-b48c-e1023ba7dfed | -2.82153 | -50.46615 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55efa9e3-d10b-341f-a514-28107f06610f | -7.44627 | -44.7455 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da3e5887-406f-3d4c-87e7-ff5186e3c87f | -3.65813 | -58.57529 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0193310d-9d64-3b21-b930-4be2f4b49224 | -3.18321 | -60.64944 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a8abb21-185e-3b14-bc2b-14a659ae409c | -5.73463 | -53.4587 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5553a70c-ad3b-37b5-a24f-1ae68868a0e7 | -3.48359 | -59.60581 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6a48ec3-794d-3f2c-b503-1b6a657bf749 | -4.3615 | -55.51577 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0335d67b-f491-3419-85b5-2033e1208dc1 | -3.36315 | -50.44541 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f23ca2-556e-3661-82e4-0a8864abf23c | -6.40123 | -55.25894 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df3979a-e46b-3fa1-9b38-fb543f0dc25a | -2.50438 | -56.59962 | 2026-09-21 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de5bef97-9512-3822-9b33-3faa15f72b1c | -6.20177 | -57.76141 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a33e16d5-a7c7-3827-8341-c234f9577892 | -3.54229 | -58.94829 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0d56739-6c36-30b3-9602-a5ac7b4a26d1 | -6.23202 | -55.93405 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee982640-5f77-3452-9bfd-3f32238e5327 | -6.28351 | -56.03742 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 740f81a2-e156-3375-ae11-facdccc74e63 | -4.50456 | -59.56198 | 2026-09-21 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c07c36e7-9d28-3810-ad81-73c110af87d2 | -4.15386 | -50.23658 | 2026-09-21 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a80594-63e7-36be-a119-b02b99c399b0 | -3.33317 | -59.81302 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 983c8289-77ed-3438-ad99-40994b129998 | -5.85524 | -53.53481 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0e3e6f4-6768-3fa6-9526-2576c4c0e90d | -8.00546 | -44.8103 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c42569a0-a7b0-3a36-8254-5a26db962c47 | -3.07171 | -61.28066 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8596fc8-a532-3bd8-b57d-baed892c3bee | -5.84018 | -53.4932 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17342929-1104-327b-8cdd-ee5a56fdbe02 | -6.64927 | -50.92875 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e03730f2-6c3b-31a6-9796-37f6d923118f | -3.17292 | -57.86594 | 2026-09-21 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d61c05f7-de03-3279-b2f2-ab4e105071a3 | -7.41165 | -44.76965 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5cf88c10-7cc4-3266-bf59-e24c5393b467 | -6.13376 | -59.95846 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17808ca8-785b-358e-b657-0c467263247c | -6.08531 | -55.54327 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81788e76-d2d5-3726-926d-ec3dfd79eff7 | -5.82986 | -52.02779 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a7c6ba3-3ea0-3829-ba3a-8b293656bf08 | -5.9851 | -57.77632 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a68e4b10-77a1-3c27-b490-f2fc7d78ae5b | -6.19548 | -55.44751 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c2249a1-1bbe-3382-aeeb-a48795fff88e | -4.40968 | -55.07591 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 231e62b2-072e-30b9-a427-009e37cd41f7 | -6.10925 | -57.6374 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8661b508-4cff-3bb5-b2e9-706cfdc241bf | -3.68444 | -60.62739 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcff0c90-873a-3ea1-916f-8009d61653ff | -1.24376 | -54.19347 | 2026-09-21 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01a3e51-0a14-37ed-b505-165682c5f0b5 | -3.1099 | -60.71873 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3084e177-c208-327f-8980-a74282456ed4 | -7.4128 | -49.84175 | 2026-09-21 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1e21306-93eb-3cc1-bf88-e006baf108d3 | -7.38816 | -51.77214 | 2026-09-21 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fcf6dba-447d-3d28-996f-2188ead6a526 | -3.4884 | -60.36846 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb98674a-a784-3e4c-9df6-f8c223e86543 | -2.68602 | -59.78201 | 2026-09-21 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd9d0ca8-1609-3404-8a44-3b84fb3e662f | -7.48122 | -45.47765 | 2026-09-21 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bdec200-7e3b-3015-a260-14aafb3b335d | -3.50335 | -59.92844 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede5d4c0-2657-344d-b19b-4b9c8f9720bf | -3.08424 | -61.17418 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c062da8-1b45-3842-8a20-1c3bb4af9105 | -2.45936 | -49.22347 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5390f385-52dd-377a-bb5d-34e902f183f3 | -2.64303 | -54.68997 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 648ecb8f-64c9-3cdc-a128-cee846bba6b7 | -5.82865 | -53.50756 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce0bbc48-6192-3217-8dfe-85ba66671484 | -4.35431 | -55.64839 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad48c664-dc50-3326-b639-b174679b022b | -5.97218 | -51.93676 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33857e27-e733-3406-99fa-4a70a33d6a06 | -2.89203 | -49.48155 | 2026-09-21 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff66fceb-380e-3d60-a494-a866199ac5b0 | -6.2943 | -59.92652 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3632c23-1ab8-3c17-81b9-3cf8511cd919 | -3.53815 | -58.69138 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94e69fb1-42f9-3873-9983-dbfc6cf8e416 | -4.68392 | -55.62973 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a27f811-742e-3c90-9034-699d71304a4e | -3.07647 | -51.19756 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c02b1347-7f7a-30fd-b4e3-2f71c9bf43ab | -2.68025 | -49.02245 | 2026-09-21 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d136b05-1952-3b93-beee-7f32f1850eaa | -3.39496 | -59.57951 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 043606dd-0393-3d60-985e-4a0a9a1d2ead | -6.31553 | -60.01036 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd4a78b8-2d37-39d5-873c-617cfa510ff0 | -6.45401 | -48.45095 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54384540-5a84-34ba-85be-ea722236a496 | -5.83617 | -53.52009 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af819851-1296-3122-bbe8-9d392c4e6913 | -5.98066 | -55.36055 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9762c8bc-474b-3879-92e3-92eca92b1f86 | -5.80859 | -52.09288 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README57.md)
