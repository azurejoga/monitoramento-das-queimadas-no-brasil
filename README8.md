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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ba8a20c-62c5-3a42-9e02-514abae0e26a | -10.64217 | -45.23369 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a93eafe-2aad-3807-b736-a5a08486db49 | -10.69579 | -48.86715 | 2025-07-31 03:45:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d5c626a-c6f0-31f4-9d11-5a9f99dc9019 | -8.0651 | -43.10912 | 2025-07-31 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c75c4967-e12a-3810-8de7-5789e41e9283 | -7.5924 | -44.80745 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9670655-a24a-39f2-b8bb-9c45de8dd022 | -7.32447 | -44.67611 | 2025-07-31 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3034562e-54ce-3c4f-ab61-9d03a6aa4099 | -10.52416 | -42.55126 | 2025-07-31 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d6118290-329a-32df-b7b5-6c3d2bcbc8c8 | -8.45038 | -45.14942 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acefa5f4-a0ac-3747-8507-01a186a4da47 | -10.5285 | -42.552 | 2025-07-31 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b7929d0e-8e48-3bd4-9f58-cdae46e3391d | -11.98503 | -46.67442 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd642aad-1b2e-3b95-9b61-69079b7db6b4 | -8.95881 | -46.74676 | 2025-07-31 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1a1332a-edd6-3cdd-b6ee-c7e819b12ab9 | -8.17229 | -45.01539 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c825bc1-9623-32fb-b2c7-a3daada77782 | -8.88222 | -37.02164 | 2025-07-31 03:45:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e40fbd8-f49c-3a00-be29-951bebb81062 | -7.12506 | -44.90639 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8c7aff-5435-33cd-bebc-cd97739563b1 | -9.22433 | -48.59833 | 2025-07-31 03:45:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 851464b4-389e-342a-8b24-2347b837052d | -7.58596 | -44.81273 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 229ea276-1ed2-365e-a6e6-9df76716196e | -8.17763 | -45.0163 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56c54892-46f1-3b52-b826-c3e5d31d72d3 | -7.59768 | -44.80857 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 835439c3-a2ea-30b0-b62f-d8764d89b79a | -10.64736 | -45.23458 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20ec5d3b-d5f7-37e3-9252-9a12a4db1019 | -7.35276 | -43.76098 | 2025-07-31 03:45:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 257ae57f-1770-3409-a5f4-508fce610a17 | -8.95476 | -46.74517 | 2025-07-31 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80d8770c-acbb-351f-9b33-8fbb33a44bfb | -10.61851 | -45.24575 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12a91c91-8e6c-3426-a5f1-7d813f082f52 | -17.66886 | -44.12728 | 2025-07-31 03:47:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 204d4f75-ed9a-32eb-9d30-747a2890b42b | -15.89591 | -43.45725 | 2025-07-31 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 366a8af2-0138-34bc-884a-f8adff9c576f | -18.6768 | -47.04135 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 682f23ca-1830-3f8e-9a4a-53b8d891ed2b | -16.13131 | -46.88066 | 2025-07-31 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90fff3a3-4301-3337-b9b3-c9f15c6567f4 | -27.68726 | -48.75333 | 2025-07-31 03:47:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d72896fc-c061-356d-93d3-233e7f1ff61a | -14.70844 | -47.85353 | 2025-07-31 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea3e243b-9ef6-3964-8eae-6b8fa2db1ce8 | -16.62206 | -44.09303 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 270bfab1-7936-3f40-9aeb-1fe81eabe5b2 | -18.46571 | -46.90863 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d90ecba7-a750-3464-9e4b-278c91903e04 | -15.89096 | -43.46049 | 2025-07-31 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4c1b50be-51c2-3e2f-9040-424fdb521521 | -18.96554 | -44.56211 | 2025-07-31 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97433abf-0473-3815-8718-079562fe75e0 | -18.54101 | -46.69264 | 2025-07-31 03:47:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 484049b2-d45c-35de-ad08-8f734fefb263 | -21.31153 | -48.5659 | 2025-07-31 03:47:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d346152-e3d4-3de2-ad09-8ade5848ce45 | -21.04192 | -42.94099 | 2025-07-31 03:47:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05a90480-a587-357a-bb41-99027b595f42 | -19.65317 | -42.16084 | 2025-07-31 03:47:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 353ca86a-400e-3a1c-9033-cbe38093f7e7 | -16.96796 | -45.69108 | 2025-07-31 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc27a12a-9dbe-37be-98f6-ed6407d8f409 | -16.62029 | -44.09401 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66292021-ad83-3165-a165-653e29dd3e10 | -16.62381 | -44.09917 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70dd6805-80e4-3363-adfa-a0198f41265e | -18.44994 | -46.90928 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d31ad0a-0501-379b-a134-d6cbdbe1df59 | -14.3795 | -50.32624 | 2025-07-31 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6745d017-6c6e-3cfa-aa30-e2bf3449fbad | -18.44936 | -46.91214 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b2a4a95-d0fb-3a98-8c09-61502720ec79 | -16.13653 | -46.88168 | 2025-07-31 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37d155c9-cbae-3909-be71-f1856cb82bd6 | -14.70763 | -47.85743 | 2025-07-31 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23f9778a-1704-390c-88e1-3da025b2da85 | -17.24114 | -46.93464 | 2025-07-31 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdc03139-47a4-3bce-99ee-3223e681f12c | -18.46527 | -46.90834 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc8ab4d3-93cb-33e3-9afc-d8fae57506ae | -18.28894 | -45.09015 | 2025-07-31 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fcd98d7-99f3-3a18-abf1-42c70d463f7c | -20.53203 | -46.10759 | 2025-07-31 03:47:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ca048f5-6779-3f2b-a4a4-a3e7748bf5c0 | -21.32158 | -48.69686 | 2025-07-31 03:47:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4c1e5ccc-8b09-3415-b9ac-0eae4a1bdb27 | -19.79068 | -43.69349 | 2025-07-31 03:47:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 022d745a-d6b6-39f4-a396-97de137bc574 | -16.62107 | -44.08979 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b4d73b-f914-3e4a-8191-894ad6de59bb | -17.66461 | -44.12642 | 2025-07-31 03:47:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d3f395e-0599-377e-b471-6e0ca82cc18a | -19.45526 | -44.31044 | 2025-07-31 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baf8f602-2263-3c37-acc7-73224b96e9a8 | -17.045 | -43.77627 | 2025-07-31 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe173854-dc4b-3b9a-aac9-026f65145d6e | -18.54219 | -46.68691 | 2025-07-31 03:47:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1fd96902-fce9-3f17-b385-eb5dbf18add7 | -18.61636 | -44.26474 | 2025-07-31 03:47:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aae8f881-77bd-3e83-9dca-0c50c7e224b7 | -21.04279 | -42.93621 | 2025-07-31 03:47:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72bff6d1-d403-33ec-bcbd-548b6f99b0fe | -19.78666 | -43.69288 | 2025-07-31 03:47:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27e44081-01d6-3052-9d4e-31b915aab463 | -17.6731 | -44.12814 | 2025-07-31 03:47:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dabe0cbf-e0d8-32d5-93d9-e13eeed0a6de | -19.65606 | -42.16597 | 2025-07-31 03:47:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d0f8085-84a6-3cdc-91a8-864e1e462841 | -18.45053 | -46.90641 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2793061c-375f-3ff4-884b-49b9c12c1250 | -22.92155 | -42.88023 | 2025-07-31 03:47:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 573312e0-bd06-39d4-b305-fc0054308044 | -19.65686 | -42.16145 | 2025-07-31 03:47:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a91868b1-99ae-361c-86fb-262d877fefe2 | -17.49745 | -44.98112 | 2025-07-31 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bf31906-61b6-3746-bd6f-179dde3f5520 | -18.61215 | -44.26391 | 2025-07-31 03:47:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a7652b6-30c2-3d2e-95dd-394e55ddbd20 | -20.01166 | -46.19367 | 2025-07-31 03:47:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 027a0f9f-700f-3d91-8e89-4563e542ad82 | -20.37166 | -45.475 | 2025-07-31 03:47:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65115d7f-e546-3347-8d24-53477539286b | -20.58321 | -44.19257 | 2025-07-31 03:47:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b880ecd9-94aa-340d-b1a9-5f8cb8559f43 | -17.47315 | -48.76607 | 2025-07-31 03:47:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67f4178d-1245-3f1c-93aa-80de685797b4 | -14.70283 | -47.85194 | 2025-07-31 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 780251f5-c882-3c2c-a3fd-cac390c80aa9 | -19.72003 | -46.21983 | 2025-07-31 03:47:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fad1587-c305-3938-a9fe-41e56db298be | -21.31077 | -48.56934 | 2025-07-31 03:47:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b33a5437-546d-31a2-a1bc-4e44ee52b925 | -18.45502 | -46.90994 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67029292-4785-30ae-bc3c-66f1c3f88be9 | -18.90444 | -43.15096 | 2025-07-31 03:47:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0a85cfb1-37ec-34bb-bff5-76da0405c440 | -18.96978 | -44.56311 | 2025-07-31 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dca14653-2c57-38ac-8464-7f74baa2a7b5 | -19.45406 | -45.30692 | 2025-07-31 03:47:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8503e6fe-77c4-3402-9c00-83c11da35c7b | -19.65238 | -42.16532 | 2025-07-31 03:47:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30a046ae-61c5-36ec-a358-2fd2063a1fc2 | -16.6246 | -44.09488 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78d6bf7c-f8a2-30f6-8385-fa8acdca9454 | -18.73703 | -47.53236 | 2025-07-31 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78d43485-b7ff-3915-88d7-4b78edff02e8 | -19.81424 | -46.46288 | 2025-07-31 03:47:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb302461-01f0-357f-8da7-98182b3289d8 | -19.82004 | -46.45858 | 2025-07-31 03:47:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c6de28f-1d97-3622-95ac-02778a732611 | -17.29329 | -47.18848 | 2025-07-31 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b95bdc-bea6-3f34-936d-61d0da5ee875 | -19.64333 | -51.8784 | 2025-07-31 03:47:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48a2ddb4-dc91-3d3f-a0a6-43add3633863 | -17.67966 | -44.43413 | 2025-07-31 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31277d7c-cfde-381f-89f9-8491b58e400b | -19.4547 | -45.9358 | 2025-07-31 03:47:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c8a4a93-d7b6-3265-a9af-c1caa36f494d | -18.974 | -44.56417 | 2025-07-31 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccec871e-892c-35cd-8aaa-2eb90865c74d | -16.96817 | -45.68917 | 2025-07-31 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78b8a398-0e91-3374-a070-beb4a6ea99c3 | -14.3767 | -50.32624 | 2025-07-31 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d55b8e4-666b-3234-8776-bbed60015396 | -15.89171 | -43.45646 | 2025-07-31 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 48fb5b8b-24d5-3427-8056-106f070a3780 | -21.43019 | -45.96866 | 2025-07-31 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 897591f9-a98b-36db-9c81-7984311def9d | -18.45443 | -46.91288 | 2025-07-31 03:47:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab3ba7da-495f-37cf-aee4-9b90d7964ed4 | -16.62555 | -44.09818 | 2025-07-31 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 720c7ec0-b939-3d71-aa5d-afcdd2f91a16 | -17.46748 | -48.76461 | 2025-07-31 03:47:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c45fdf1-c084-364d-a4c3-9173b2383aef | -23.58278 | -47.03241 | 2025-07-31 03:49:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f40ef5db-76a9-3f73-8f5a-bf8e5cc7c2d0 | -23.58226 | -47.03435 | 2025-07-31 03:49:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9864bf64-b035-3eb1-8615-080c13a585ae | -23.42844 | -46.76059 | 2025-07-31 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c057eb92-bbcb-33f6-84e7-3e19205d1d56 | -6.6725 | -56.4029 | 2025-07-31 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e041b02f-1084-3541-8694-9761c3785c24 | -8.0513 | -43.1001 | 2025-07-31 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| a81addc3-751f-31a6-ab56-473788b1ed9f | -6.526 | -56.1923 | 2025-07-31 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f87578d8-98ee-3e68-b7aa-634021b31cbd | -6.5258 | -56.2121 | 2025-07-31 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| f988d36c-fc21-3b4b-8553-870faf22d19f | -6.5258 | -56.2121 | 2025-07-31 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |


[Clique aqui para ver as próximas entradas](README9.md)
