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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90fa9bf7-60ab-31f8-8e63-4f1a25ae7435 | -15.7239 | -48.99964 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9b07f844-4b05-3b46-b70c-b1f08a286c95 | -12.60214 | -48.2197 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b17e7946-00d8-3840-bfa7-241b7c464b83 | -14.49955 | -43.81121 | 2025-09-01 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a185c9ca-42d5-3053-b4a1-90311ecf9225 | -11.51773 | -54.47795 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 931dd374-3774-30ab-8e1d-13a034c88467 | -13.68403 | -46.92357 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ca6c3b-4ec1-3813-b4cb-350b297cd742 | -14.94015 | -40.67658 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ecb42e2-8e74-34a8-9480-3967d2b4228a | -13.34649 | -47.03934 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a74bc81e-0387-3225-969e-8c63990dcc8f | -12.02364 | -49.70998 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8da5490b-ea23-3d1d-9426-23163579916e | -14.04521 | -44.56871 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4355e0b-9acb-3fa1-a8b1-ec6942800c93 | -14.79299 | -46.72913 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 902ed426-9b67-3be9-a8a0-f23e655a2ff7 | -13.165 | -45.28621 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 7ad28bc1-e095-3477-afed-9ef7a3daa4be | -17.61075 | -46.66977 | 2025-09-01 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf532eae-74e1-3611-bb1e-220907602424 | -13.97841 | -44.55008 | 2025-09-01 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b195f19-f362-3654-8754-b61d58309013 | -12.56389 | -48.22047 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17a2b2fd-2679-3382-8bed-bce0f39d91b4 | -12.56866 | -48.21745 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 967a0bb3-0727-30a5-8e3f-257dc7e83b3e | -15.72865 | -48.99683 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 52427dcd-8781-3766-a5bd-3662bf9bd802 | -13.99658 | -46.31409 | 2025-09-01 04:12:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d46db5a7-980f-37a4-9b49-aaa0de447ad0 | -13.37135 | -46.94263 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d4b3c39-3a4a-3bb5-974f-fbab78956869 | -17.2355 | -46.92017 | 2025-09-01 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a03cd6cc-3f19-3c7e-b94e-d2355d306861 | -15.58755 | -48.34642 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 21a64a81-08f9-3b40-a31d-f139421aa526 | -14.85149 | -47.09486 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a3a35b2f-628b-3216-981d-b6f856450a84 | -13.69629 | -46.88014 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a50a348f-30e4-3f90-9171-be76a71e6787 | -15.69604 | -48.92777 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da2c3888-2181-30f9-a42a-6951189cd1ee | -13.47692 | -46.93817 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7ac1374-d36b-3665-9334-cd6e2f4c8e34 | -12.96576 | -48.11459 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0ee36c3-3095-35bd-90e8-9431afc0768e | -12.83599 | -48.07221 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 962a33f9-87dd-31f6-a27c-c55358b1ac41 | -13.58305 | -46.92729 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8a221f0-a5a5-3a67-9969-1bb0eec111a1 | -15.72259 | -48.89713 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fba47c82-01f6-3082-bfe9-78c0e8e11efc | -14.02364 | -43.90807 | 2025-09-01 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90ada61a-87ae-3ba2-aede-273cc2b86171 | -14.00696 | -44.50537 | 2025-09-01 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f08f6a3-653a-3ca4-a601-0ec790271bee | -14.74612 | -46.7612 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d571a45c-e8b0-3dec-bafe-6de6dd7f0df9 | -13.52344 | -46.98184 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 29f1142d-8d95-3168-8a12-ed466bd91c8a | -12.83951 | -48.0757 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4f1f960-4b88-3918-a237-4811acedbfac | -15.68853 | -48.94599 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ef0989e-ee5b-3841-bdad-0b2a884596c8 | -15.59346 | -48.359 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f70bd10e-0742-3b2f-905d-2df3aeb1c468 | -16.15524 | -49.63857 | 2025-09-01 04:12:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6be933f9-e381-3829-a120-da7db3d2ca98 | -14.41687 | -51.66877 | 2025-09-01 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 83439bbf-34be-36a5-8c2b-38b337cf9cba | -15.09658 | -48.14492 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7905bb29-046d-3b74-923c-6b0b67d5a495 | -13.47584 | -46.98813 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a41cf970-f25f-3415-a5db-e20adf56bd1e | -14.83361 | -46.73173 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad8c4d2a-6579-35c4-a3b9-18570cf84780 | -16.13708 | -49.04879 | 2025-09-01 04:12:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d55ccd4c-9d0b-3d2b-bd0c-b82af4c671c4 | -13.34233 | -46.97785 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea57c159-508e-3ea2-8b25-bcd218dcf0f4 | -14.79511 | -46.7388 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6747acca-6e79-3a20-9217-0452c3a92f03 | -14.75709 | -46.76308 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1df393d7-be9c-33dd-935d-af974c797196 | -12.3911 | -46.47751 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d1f803e-7e7a-3ae6-80aa-388b745694c1 | -10.88006 | -55.76189 | 2025-09-01 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f147f214-f599-3efc-9173-6cf8a262a553 | -15.10105 | -48.14946 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 470e5e33-9825-3e48-8f94-862fb03418b8 | -15.72603 | -48.98817 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 023a88ef-619b-337b-bcb7-abe4cc33b136 | -12.83542 | -48.07545 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddd39a67-2d5c-3106-9c44-be1de4aface8 | -14.23433 | -48.05613 | 2025-09-01 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e8ab70-442f-39ab-acb5-3f8d4ea45273 | -14.16243 | -43.67365 | 2025-09-01 04:12:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8d29fabb-bcfd-3e53-9980-c963e7681d5f | -14.78648 | -46.72326 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c63736-3d80-3ec1-816a-242a110067d4 | -13.5498 | -46.96364 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2838a00-2490-3eda-9095-4c31117848ba | -12.58966 | -48.1943 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66989ed0-f4da-333f-83db-56b018723a74 | -15.71421 | -49.00618 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4645ac3e-0085-3d7d-94b1-aed29743c785 | -12.80571 | -48.07803 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07586080-3a8b-36ae-8235-7dfad199cad5 | -15.58741 | -48.32431 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4d2f3fb-ed83-3531-a04f-7d91783adb09 | -14.81262 | -46.72416 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f07a58-8dfb-3b32-8654-5611113d1784 | -12.6028 | -48.21593 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ed61fa51-03d9-3774-8157-47796a17bcb3 | -15.22808 | -53.78838 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ffaf3c-ffce-3f6d-9df2-dac1b785fcc6 | -13.47753 | -46.97853 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6393d0ae-a690-324f-ac81-622bbbdc78fc | -14.23037 | -48.05541 | 2025-09-01 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 459e068d-1be1-34e7-a8d4-b1f9f513ea0d | -12.84004 | -48.07291 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 857a1c1f-0cce-323e-8511-710eb75f89de | -15.6994 | -48.90921 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c144c06-1df0-39f0-96d4-f2fdce49b6d8 | -16.11594 | -46.82254 | 2025-09-01 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c346252-e968-32c2-9ba4-84db91a542a5 | -12.9738 | -48.11642 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92c1a423-e583-3756-b35e-7bb5e4fb845a | -13.5782 | -46.93357 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca5e290-3713-3de9-8d27-59a72653eab9 | -15.32546 | -46.10265 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a45550e-a0b0-3dd5-8951-4677fcade298 | -14.04641 | -44.56134 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7847ff37-78db-3798-a397-e670936a4f98 | -13.51523 | -46.82965 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d660c0bb-a7f1-3a10-9cb9-d6474b33abd3 | -15.10049 | -48.14572 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c3135b-8999-330e-bafe-ebe0a778941e | -17.15741 | -46.0827 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bec78f9-e01f-338a-b2b1-8180dfd44d52 | -15.69475 | -48.93493 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1fc6e215-6901-3885-b638-8431e8555f49 | -15.16075 | -52.34451 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0306484-916d-33ec-a0e9-8a25374a6ab3 | -15.59826 | -48.33188 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fd25760-bbf1-35e1-9c7a-efc1359a192a | -12.97849 | -48.11361 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55ca7607-8a31-34bc-9461-04a81f7d6f0d | -17.15259 | -46.09023 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5062d0bf-26b7-37e4-b6bb-496a0aab00d4 | -15.68705 | -48.9542 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a90e17d-3807-3570-8a66-931f7cfe096b | -14.768 | -46.76533 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d69cbdf6-3289-331e-ab0e-50e0a881521e | -15.69793 | -48.89408 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5248b5e4-a9d2-33ba-9cdd-73f305047ec9 | -17.37539 | -45.02288 | 2025-09-01 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea3085bf-f8c7-3210-a4a0-9e475ebf2749 | -13.37274 | -46.31534 | 2025-09-01 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccc32e8a-4cb7-317b-995b-0b034b2b4131 | -13.40799 | -47.02157 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbd946f4-4d8f-389b-8b8e-74bba64ed906 | -13.36381 | -46.94149 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 149c75af-8674-37da-b0e6-9834029f4128 | -13.47614 | -46.94046 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0377e99e-ecaa-3688-8832-bb615375126d | -15.32763 | -46.11132 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71bc5acf-7fc3-36ab-99e4-38fb26526b34 | -13.33937 | -46.97246 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8921b2f8-daa6-319a-82ad-84e86bf85dcd | -13.53165 | -46.97912 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8160e7a8-11f4-392b-a236-34b89bc97761 | -15.08112 | -48.12467 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4376d3a5-8cf9-326c-8e43-13e3e1736807 | -15.22527 | -53.78836 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9116a7ba-a6f7-3a29-98e6-ce15ea31ba6f | -13.37058 | -46.94704 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca58dc78-a50f-3411-9482-cad009e1e14f | -14.00636 | -44.50904 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc57a1c7-3940-346d-82c3-aa9122ba9b0b | -13.47452 | -42.48026 | 2025-09-01 04:12:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd88ed1d-edbf-3f42-bea9-f949a24f962b | -13.49003 | -46.99565 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 011fed30-5efe-3c31-996e-01f1099a5e17 | -14.98275 | -46.71206 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4e3869-54e3-3630-97a4-ee444272ab32 | -13.50104 | -46.97701 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51f19e1d-7c54-3b5f-8604-5e082daa52ce | -12.95432 | -48.10847 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35f852ad-a421-3325-af5f-a3dee0ae3131 | -13.57774 | -46.93583 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e679236b-9c19-3919-9bd6-a3f8821526b8 | -13.49348 | -46.9319 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd41e92c-e37c-3900-9b87-d54fe7387db6 | -15.69798 | -48.96379 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README43.md)
