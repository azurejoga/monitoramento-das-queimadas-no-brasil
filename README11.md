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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea4e8e13-0bef-36a4-a21a-1a02e2db3fac | -7.26539 | -39.6706 | 2025-08-20 04:08:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| acbd7c83-edb0-3d46-b41f-8babf8ed61b9 | -6.95921 | -42.87046 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 49c911a5-745a-32b7-a0b3-1382d8530b29 | -3.82007 | -41.55077 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f3c3472-8f56-3c8d-aa01-96939c86b387 | -3.98895 | -47.88808 | 2025-08-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 617f3db9-ea21-3a4c-8997-82eedec234f1 | -7.13426 | -44.39835 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e94c051d-0e38-3471-8c75-02560a4d5569 | -8.17445 | -47.35261 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a086565-3918-3d4c-ad5b-20d75e8adc85 | -6.94715 | -43.86625 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ea537d38-cc5b-3104-9488-a1e4fd7f71d7 | -5.25409 | -45.06238 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a9a7937-6b79-3767-894c-d9214bbac96a | -4.60742 | -43.32391 | 2025-08-20 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dac0a064-5676-3628-a6b8-91d21f7dff4b | -7.39151 | -43.08464 | 2025-08-20 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 733adefe-aa47-37c1-aa1e-1c98c041de9c | -10.27772 | -46.76775 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9aa31e-4e44-3cbd-8b35-220acfc51740 | -4.91385 | -43.23079 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5891ea2-9b1f-3788-86c0-73edc37a06b4 | -4.42542 | -47.75966 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5efd0b7d-3490-32c6-ba16-472c7514d614 | -6.55754 | -43.00317 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11310af6-6138-3bf0-a79d-087e68272630 | -9.25114 | -44.49966 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27737139-8f53-32cb-9174-12f113b1552c | -2.84736 | -48.78517 | 2025-08-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7d88b9f-7bef-3e1e-a33c-4493f5e3b04c | -5.98931 | -44.14032 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 905f3ce6-2b69-3a8f-9452-a35cf3feff89 | -4.77834 | -45.31897 | 2025-08-20 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e74da4c9-63c9-3475-b02f-088cbe76eee9 | -8.79681 | -45.47525 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 792f79df-2554-36ad-99d1-2b48445ded34 | -5.66377 | -43.50348 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e6889aa-3372-34b9-bc0b-e59385a6f04d | -7.2743 | -50.18583 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b6e5738-41b1-3b33-9371-de4b8946ea25 | -5.51086 | -35.57698 | 2025-08-20 04:08:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 309f3686-7c43-302a-865f-28a5cfd93fb3 | -6.17061 | -46.14925 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8826362b-a744-30e9-9c32-d101847de49c | -3.97861 | -42.50838 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4588b373-99fd-3c0b-8968-81141aacfc03 | -4.91206 | -43.24187 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6fc7fb9-f61f-3a40-b55b-f0f5b35f7caa | -9.92354 | -49.29077 | 2025-08-20 04:08:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5304f169-86b6-333b-b827-78e9b877af55 | -7.26678 | -50.19919 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 986b8bf6-c2f4-3e39-adcf-e88f162e0a23 | -6.94655 | -43.87 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33dbc3d6-ba0e-3a1e-8a47-833b13086aab | -6.94595 | -43.87375 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dab04e87-9e76-3b04-ad6e-d182709147df | -5.48942 | -42.16232 | 2025-08-20 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cde30a86-620e-3c0f-a111-617d0036735c | -4.95389 | -43.09016 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ec3a63c-fd17-3dba-a8c4-1d01c88c442f | -6.42102 | -42.48904 | 2025-08-20 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dbdb9921-f71b-3a3b-a303-e5324ee15952 | -5.87468 | -48.11551 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de32874c-1a2c-3d74-86db-50e9b70eaba8 | -6.02507 | -44.38948 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b64ae6ba-2d9d-3e45-9f22-dce1df0b5f06 | -7.12786 | -44.63667 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 974b6f6b-96e0-3cdd-ae95-6e44c184bcfd | -9.47513 | -47.33635 | 2025-08-20 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a785cc3e-f6e4-3e99-a9d0-116d7fe5ba18 | -3.23566 | -46.79771 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e7d73486-faef-3d19-b451-e35229c31a37 | -3.6925 | -44.2086 | 2025-08-20 04:08:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83ef9299-3a51-338a-b2cc-05f4c07af1c7 | -4.92008 | -43.23558 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41fcdd7f-d125-3b4d-b311-069c89148624 | -4.17018 | -42.02874 | 2025-08-20 04:08:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bff934a6-8b70-36ad-9d69-58aafc50ea44 | -7.64512 | -45.28517 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4354de3-ae40-397e-8d68-20e7027ae8a0 | -6.46511 | -53.38156 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de976575-4dbe-3e92-8409-ea5e824a532d | -2.90358 | -48.29843 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfb16b30-41f0-38b6-8544-aedcf0027e7b | -6.94938 | -44.55121 | 2025-08-20 04:08:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e9bd4d3-8409-31e5-84e5-18d253cc4520 | -4.48584 | -43.90195 | 2025-08-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 69d8deb5-dffe-3abb-ad64-c1b98b94ca7f | -8.24459 | -44.33449 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df0c58d5-d612-36d1-b15b-5ea33c827245 | -6.16944 | -46.15164 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 872a20cf-e54c-36aa-b2d9-a5fd992fe2e2 | -8.17101 | -47.34826 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50d7506b-b502-35e4-9c1a-078b550258a5 | -7.22633 | -44.7009 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7456963e-cff0-3b57-91a9-205ad99ac262 | -8.30673 | -46.35331 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5405b438-4112-35d8-8b95-6882043bed82 | -6.49328 | -42.97476 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebabd80f-95db-3560-8d0f-9cb8f1edbb9c | -5.86944 | -48.11938 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 982da0b6-7e4a-3057-9657-5f5e0825097f | -7.64359 | -45.27196 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e696f3ca-7646-306a-af18-5ea6dc01ea3d | -6.51374 | -43.41786 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f05cb7cf-3566-3ef9-9fb2-cb8b814d8c7e | -6.3244 | -43.6104 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0238a65f-b84e-3425-9ece-009977cb9a66 | -6.13282 | -42.95748 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f9415b7-b5ed-314f-81ae-00f3fb1432b9 | -5.34619 | -43.53463 | 2025-08-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68e1b909-75a8-3d77-a085-cce2cc253c4d | -5.63555 | -43.39292 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 491db56a-a1c1-3b4a-91f5-35f161e5919b | -5.40483 | -45.14648 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| af0c02a3-6b7d-3c88-b303-98d36d0b991f | -6.07068 | -44.12526 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29e3e252-c20f-3e54-aae5-6bf162632de5 | -7.23215 | -44.258 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b49a7884-bd96-395d-9afe-6f62e3929b55 | -9.26977 | -44.53781 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6e58755-ef9e-3348-843c-ae7f9540ac91 | -6.06144 | -44.11571 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f419a1ce-b16e-3c77-b247-0e0700726fd9 | -6.57262 | -43.01653 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5acc3415-8144-3ed3-a1e9-28f346a2305b | -6.03785 | -44.35471 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a060344-34cc-3bcd-a335-88db5d56bb95 | -7.66091 | -45.25733 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28e88641-ccba-3d0e-ba0a-6fb725520284 | -6.59832 | -42.2711 | 2025-08-20 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0cdc3a48-5538-3f54-9b14-fefd9bcddb7d | -7.65952 | -45.26577 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a0a0bf9-5f46-36d5-ad4f-4ff288788fed | -7.64442 | -45.28941 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 210688be-86bc-35a4-aed2-b31fc3057d2d | -3.05173 | -47.02109 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd491637-3104-368b-9a7b-7615074c1e39 | -5.64871 | -43.37939 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13d118d-e0f3-393e-be4f-e6fbffc9269f | -6.94673 | -43.84695 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0098ba72-5c26-3ee8-97d4-ee0b0149857e | -3.97918 | -42.50481 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c72a0cc6-d650-35ea-8987-1a16e283f612 | -7.02728 | -44.28982 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c250aea-a2ad-31e2-b383-1253a672f28a | -3.98477 | -42.51299 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32318496-23e8-3523-95fc-5593cc646b03 | -7.65156 | -45.26887 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8620718-f696-328d-b21a-c61198444f98 | -4.43063 | -47.75584 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ced37570-c55b-30a1-b967-3c8d01519dcf | -6.86472 | -43.61323 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a78ff522-1b80-3ae2-9d83-074b59fd1964 | -8.80839 | -45.32763 | 2025-08-20 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbef4309-6039-3c1b-9f80-276c77162f09 | -7.51365 | -45.00864 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f49cb7a2-c074-324f-97f0-0f2d9c791391 | -5.54181 | -45.37359 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a313809b-f05a-3f4e-a23e-cbf10ca49a19 | -5.78362 | -43.89023 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 894c7d9d-bd42-3cd2-867e-874773f5e580 | -5.64812 | -43.38307 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a761e717-4344-356d-87e4-7abfa903e141 | -6.27113 | -43.70139 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d805312a-cb3c-33d1-a88e-5163d2d2f409 | -7.14219 | -44.18495 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e53fd104-c3c7-3c3d-a05d-747bb7b589cf | -7.78458 | -45.16856 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31a36739-4aad-3ac5-8932-ce7473667e31 | -6.68659 | -43.67218 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1e11a9e-bbdf-3f4c-a154-abb613097cd8 | -6.95196 | -42.87294 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 2865b7db-13c3-39ab-bf09-b41714b50751 | -6.08029 | -44.58752 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69ddede3-e966-325a-ac88-a3c1e0399070 | -6.35942 | -43.32597 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68b8193c-158f-3398-a10a-add61b706827 | -6.61888 | -43.87629 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05abc275-d674-3c7c-8eee-0b8b542bca1f | -7.17926 | -43.408 | 2025-08-20 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98866d84-4963-3367-9804-ed230e031161 | -7.63492 | -45.27924 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec153858-fdbc-3a42-b5a1-f39149c38c30 | -6.33248 | -42.89787 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0369f3a3-db41-3b00-886b-f2d1509ecb07 | -6.95253 | -42.86941 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 98f77667-65ad-3dfa-a606-abca7b7684d8 | -6.72709 | -44.33434 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a19ae4c-cfdc-3d4f-9210-e63caf5ed01e | -6.45976 | -53.3756 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08062333-8672-34ea-9b4b-a8ad53ca2d96 | -6.71371 | -44.32817 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e419c6d-adc4-3d02-bae3-06adbef7b3f7 | -8.17038 | -47.35192 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3882fd7d-8342-37a5-aa89-dc3da0e95b9b | -6.86179 | -44.41979 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README12.md)
