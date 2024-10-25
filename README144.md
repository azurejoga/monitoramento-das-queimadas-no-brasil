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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86436ae5-4d3d-3bf2-a3ca-f3021d4ce617 | -11.53854 | -43.98217 | 2024-10-25 16:50:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1d4fd5aa-574d-31ae-a1fa-19e961b3ee77 | -11.53232 | -43.9947 | 2024-10-25 16:50:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 874e4c01-14f9-3d0c-8e30-1a3c3eac1f31 | -11.29358 | -44.18828 | 2024-10-25 16:50:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 13ab542e-3aef-3159-8baa-32799735d7b7 | -11.29112 | -44.1738 | 2024-10-25 16:50:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0d79a8ec-4080-3a8e-b475-df8731e05ea1 | -10.88244 | -44.40245 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f4022e7c-30f6-3e83-b456-e45bd31efe2b | -11.68797 | -43.2478 | 2024-10-25 16:50:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 522e0f20-6919-3c45-96c0-f4db5907b7ac | -11.02318 | -43.34596 | 2024-10-25 16:50:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 849261f2-3ee4-3eb4-9195-3c1d671e1f81 | -12.11938 | -43.64206 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1fc6a5c6-08ee-3bb6-8327-7908c7c8fe13 | -12.1187 | -43.63824 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a2d9fc02-7412-3a41-b1be-2f179624244d | -12.11458 | -43.63899 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 11a28a73-4281-3abc-bfe9-fe8e65010451 | -10.86615 | -43.64494 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ba013570-885f-3ee3-9e2b-e980e161be1a | -10.86194 | -43.64568 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 658e26b1-328f-3cf2-9a91-00152170a809 | -13.57596 | -43.66095 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1ab6f1bf-4a69-3f8a-9bcb-45975996a26e | -13.57533 | -43.65733 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f41037fe-ea10-32ae-8311-a2b1efda7634 | -13.53905 | -43.75721 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6993b1e-2eaf-380d-b0ee-656074ceba22 | -13.47889 | -43.7765 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4bc16223-6a46-3e15-af00-8fc70cbce6c4 | -13.44056 | -43.58108 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb615862-af1f-369b-9c14-1dc1a72aa8fb | -13.14192 | -43.54826 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6d8f0295-6376-3c6c-ab2e-12939a0f0e00 | -12.97699 | -43.46972 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5916e410-345c-322f-b6dc-c722bd1585af | -12.97355 | -43.47426 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d952d805-188c-3e93-a3ef-44bd0c751863 | -12.97288 | -43.47049 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| edebd3ee-784e-3a1f-87fd-50bfce160f00 | -12.88584 | -43.52172 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a45b962a-d1a7-325d-8bc7-1e23467d5a40 | -12.86376 | -43.70653 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 980ac3ab-6066-3c0c-a105-13c218f4d6a3 | -12.69534 | -43.45804 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f73a1122-8b0d-39cb-9e08-45776e6ed9f7 | -12.57051 | -43.36558 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 83b61221-e6d6-3b4b-836d-70e785b7049b | -12.48084 | -43.71975 | 2024-10-25 16:50:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 617dec79-de85-3e42-be70-77ce99e1ac52 | -12.47676 | -43.72051 | 2024-10-25 16:50:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 67c55704-56df-3796-abcc-4eb0693efa5b | -12.46012 | -43.55272 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef55f27d-468d-3e51-8385-07fa6f06b1e2 | -13.74505 | -44.03131 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9bb2ccdc-d7c7-34ea-8e26-171bd4f352f4 | -13.72953 | -43.60246 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a9828c7-6d1d-3538-8af3-b9db4684ea43 | -13.67712 | -43.59307 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 841944bb-44b2-39a0-b0af-b7e8358b4bf4 | -13.66784 | -44.30727 | 2024-10-25 16:50:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c9a16a79-9d71-3718-a695-ff3cc4377222 | -13.66398 | -44.308 | 2024-10-25 16:50:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 280c9e15-2f02-3963-902c-3be18331cff6 | -13.65517 | -43.8208 | 2024-10-25 16:50:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74553464-9222-3db9-9177-77ef794320be | -13.55949 | -44.83271 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0fff33a8-840f-3a99-afdd-d1e4d5119305 | -13.55713 | -44.18121 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dac83411-c13e-368d-88f5-efcc1f94f0c8 | -13.55324 | -44.18193 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| fa443ce9-9acb-39b9-9aa9-ee0d9e159b45 | -13.52649 | -44.30479 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2dbefdbd-e00e-3c78-9ed7-a6b749739a81 | -13.50293 | -44.32971 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7515253a-a325-347a-9dfb-7876f4f6c0ae | -13.50207 | -44.33183 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f542d3b0-dcd7-3774-9011-54634fd1e41a | -13.49905 | -44.33755 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a64ce0e6-d897-337a-b5c9-509018b919d3 | -13.43754 | -44.28168 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6190ecfc-a9f2-3cb7-acd8-f26930f9d32a | -13.43278 | -44.27732 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c1532be-d4d5-3fd2-a8c5-23d4fce43ec8 | -13.42981 | -44.45457 | 2024-10-25 16:50:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6f3e3275-2cbf-3678-b445-9d09d6a5a844 | -13.41007 | -44.35326 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 192dc7bb-871c-30b7-a227-82d423ce8c39 | -13.40928 | -44.35625 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cbbd08f5-fb68-320a-98ae-bf09ee7a3bc0 | -13.40845 | -44.3513 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2c0878fd-6551-3c0d-aa3d-59ddf8b29c24 | -13.40562 | -44.4287 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a106fef5-6cad-3b19-baae-379403a92cd5 | -13.32831 | -44.16397 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c70abe06-9a22-3e34-9f06-f87feae12b55 | -13.32439 | -44.16463 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cb48643c-0efa-3e63-bd45-71d8e84a3614 | -13.23205 | -44.2369 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 92b93bf4-4fe9-3741-aded-37b279466133 | -13.21708 | -44.48397 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 40d948fa-2f3f-3ef3-a3b8-5add77245c27 | -13.17981 | -44.59068 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| eb9851e6-38a9-35db-a7f0-ca91dc4560b9 | -13.0811 | -44.62677 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| afa73b69-4d80-37b4-80a6-e45bb1d526e7 | -13.00637 | -44.21442 | 2024-10-25 16:50:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 22b9d6f9-d850-3aed-bf67-268b3f6a2b2d | -12.98947 | -44.56588 | 2024-10-25 16:50:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7d2bba7-54a0-37da-8009-9c7c99549fa2 | -12.90787 | -44.08583 | 2024-10-25 16:50:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 561ea1e0-d3d8-3f53-94b1-faf99bbf9b68 | -12.89815 | -44.07676 | 2024-10-25 16:50:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4b4c156f-8744-3493-b164-5f04d124b839 | -12.87821 | -44.59836 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff2f7350-f51b-3ab8-b8b5-6b5593a8edf3 | -12.87739 | -44.59351 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acd45eff-c8f9-3fdb-9dfb-6aa0c92b33da | -12.87354 | -44.59414 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3246eaa1-2e46-34d7-beba-6e9bee2c4db3 | -12.86118 | -44.59134 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8ff77de-1c90-3e8a-b431-04f4d126abc2 | -12.8585 | -44.62204 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a3e6a6ba-0bab-3732-b097-b2fbd56ee382 | -12.85733 | -44.59202 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20728334-185e-3a9c-982a-aeeb3dfc8090 | -12.63832 | -44.8606 | 2024-10-25 16:50:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4bf21e51-6b94-3a52-85e2-c891eeeae28e | -12.43577 | -44.62732 | 2024-10-25 16:50:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7167feff-72f2-3560-886c-2b79a24ff68c | -12.43192 | -44.62805 | 2024-10-25 16:50:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3674c978-31d5-39c7-be30-c2dcfd875b33 | -12.42752 | -44.1814 | 2024-10-25 16:50:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17d32b27-d101-364c-b607-dea364021497 | -12.4211 | -44.21484 | 2024-10-25 16:50:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fee14b57-b9ff-3dd3-ba67-2ec2fb70d92c | -12.4138 | -43.96052 | 2024-10-25 16:50:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a2318b66-3b88-3ac5-9b70-fbbe258d456b | -12.34873 | -44.2839 | 2024-10-25 16:50:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4705e15-9b23-3a5e-9801-7124dced148a | -12.30834 | -44.35205 | 2024-10-25 16:50:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b42655f9-e0fe-3e52-9f11-3757c3a5695d | -12.3074 | -44.34963 | 2024-10-25 16:50:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d7a2108f-0c47-37e6-85e5-c762be087e01 | -14.13305 | -44.01165 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b4afc721-8c11-3780-874c-a4fb4e824987 | -14.12915 | -44.01239 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b97ca655-f36c-319b-a970-d66279353be1 | -14.07327 | -44.10898 | 2024-10-25 16:50:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| fc39708b-037e-37bc-850d-060e7bb2aaa7 | -14.06939 | -44.1097 | 2024-10-25 16:50:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f5ee1d1-c823-3c29-97c6-7710d470f721 | -14.05565 | -44.00758 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 376ec053-87e2-3c23-8da7-90ae226625e8 | -14.05263 | -44.01341 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f9af454f-c752-35b3-a076-90df972504a9 | -14.04417 | -44.38862 | 2024-10-25 16:50:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2126ce36-dc1b-34b4-beb7-767a4cb6c8a2 | -14.01988 | -43.91875 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 92d849ef-ae88-3df5-a04b-206684d2cd28 | -14.01897 | -43.91359 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d55fcbca-1655-3241-94fc-51e5d23ecbc1 | -14.01595 | -43.91949 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ca2fb3e7-da5a-3511-85c6-95d14c92ed8f | -13.94203 | -43.88752 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b33194e-7beb-3982-b415-a827d9a6c24c | -13.93627 | -43.87783 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dec6e5e9-7398-38ff-aaf6-59187c28f0e9 | -13.93472 | -43.91568 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ed0433d6-a5ab-3d99-945e-6ffee804c97e | -13.88984 | -43.89181 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| de81cf40-c757-3723-aa90-f0935ac6f735 | -13.84218 | -43.77375 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a1221ab8-2e69-331c-876d-7630c44c376a | -13.83608 | -43.7383 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 256e2272-0f5d-319a-9b9b-6b0d37676978 | -13.83547 | -43.73475 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fabece31-7e64-345e-9c49-289c251fb675 | -13.7675 | -44.23077 | 2024-10-25 16:50:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 315f245d-1895-346e-921b-5598ef6c0f6a | -13.73333 | -44.39954 | 2024-10-25 16:50:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 25a518da-47d7-3db0-aaa8-7339be867012 | -13.73095 | -44.39767 | 2024-10-25 16:50:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a23a652c-c6e3-3dd4-b833-984a34586166 | -15.48514 | -44.30594 | 2024-10-25 16:50:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 6d7858e3-d976-30df-badd-412ee188ca7b | -15.48432 | -44.30122 | 2024-10-25 16:50:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 3ff0ef9f-0577-3d01-bd2e-5f2477b2d835 | -15.48349 | -44.2965 | 2024-10-25 16:50:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 89ab8e76-4fc6-3e88-ab36-6f4b51d207f0 | -15.96137 | -44.44756 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 718dfe36-f03f-3636-b813-6be925ad41d4 | -15.90329 | -44.72067 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| be48d993-e782-37b9-8175-f7f16ba07a39 | -15.47429 | -45.16191 | 2024-10-25 16:50:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0dd2baac-c4b0-3f34-91ef-7678e16e8c41 | -9.62401 | -45.63804 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |


[Clique aqui para ver as próximas entradas](README145.md)
