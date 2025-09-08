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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b63b8041-017a-349c-ad32-39bfa941fd49 | -5.94865 | -45.67077 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd1fc4e4-1d61-3071-a415-e1937e86fae5 | -6.11787 | -44.25361 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78f439fe-f12a-3019-9e33-bf1300a44949 | -6.40636 | -44.41938 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5de6aa4-438e-3bde-b5e0-c8a5379c95b6 | -9.98007 | -51.67654 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36e2349c-a37a-3c98-b32f-68c6142879a2 | -5.65263 | -45.11719 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f351c408-e841-38f1-acb0-b53c26a0a052 | -6.53194 | -49.50485 | 2025-09-08 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8af4d71-17f3-39d2-ada3-8b9719ab39cf | -6.8492 | -52.85465 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 290af3dc-9ae1-39ad-a0d7-aa56932533dc | -9.68525 | -51.07251 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a60f2b8-bf03-3b37-a6ab-7f4c80727239 | -8.19607 | -50.13902 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eb3cadd-81a8-3fb2-8af0-b9c556f3e1b0 | -7.87035 | -46.26367 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4e2c3e41-41ea-3e1c-97ed-6c979b55255e | -9.14273 | -46.05745 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac617975-9208-3c32-82ef-d0c962920b0b | -5.85696 | -43.85719 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30596fc-adb9-3818-a7d6-d83a9bca90fe | -7.77215 | -61.37801 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1119a9de-80d4-309b-b82c-8e7167f1f2e3 | -11.15258 | -45.25016 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b7b8983-3819-3d8a-bf19-db2b554cc069 | -11.3296 | -46.55502 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87d8b05d-9b7e-32dd-b1f9-dd0d0e6999b4 | -6.79119 | -44.77746 | 2025-09-08 04:51:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 666c2789-a869-3c1d-817a-1c25b69600a3 | -7.704 | -44.79871 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb687251-9df3-3571-aa16-8df38d14d6a1 | -5.87473 | -43.96919 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2d212a0-cb78-3881-9267-0fab00b56ccf | -4.47305 | -48.11679 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f65622c8-a539-3d6c-9075-bed4eedde40b | -6.22351 | -49.41522 | 2025-09-08 04:51:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3a283bdf-d2fe-33dc-8c8d-709563bdf3b8 | -8.13998 | -48.4776 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04416d05-1afc-384b-91e4-86301fad788f | -5.64467 | -43.91433 | 2025-09-08 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62b1016e-01a9-3779-98ef-71d06c302b0d | -5.54096 | -43.05891 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73d2f445-f03e-393d-9e8a-acce35a586cb | -11.32577 | -47.38422 | 2025-09-08 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef7fb285-926e-3ddb-9ce0-501ca41f343e | -10.286 | -48.79745 | 2025-09-08 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9af679f3-26c1-3b39-a7f4-cc5f4b6238df | -9.04893 | -50.46263 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f1a1207-3dec-3268-856c-077cf61b1592 | -7.2968 | -44.14976 | 2025-09-08 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba0d3ef9-2d4b-34b3-93d9-4c43437be31c | -7.936 | -61.79568 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e83068-28f4-384c-8621-887199e9f6ab | -6.21115 | -44.53362 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ffae354-f87b-3a4c-b037-35efc6634c1b | -5.06667 | -48.41993 | 2025-09-08 04:51:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2093f60-fa96-3fd5-9a7f-ae1a8f212f8c | -6.27983 | -53.42326 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e53cc3cc-ee3b-308e-9955-800339f1134f | -6.27375 | -53.41874 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0caf9cc9-3908-37db-8036-b46f9c5bfb40 | -8.07165 | -50.19645 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3498913-a23a-3f14-a30f-8cdcd4275569 | -6.19872 | -53.26805 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc862b9c-f7eb-36ff-812b-6c1b876d57c5 | -6.20365 | -43.60419 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fe85be9-2a49-327a-a19a-9196b1ce0d82 | -6.17451 | -51.52217 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83aed74a-48ed-3222-a7d8-9913941bb543 | -7.42392 | -49.26613 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b6358b9f-cdca-3436-8930-edd7cebca1a9 | -6.54627 | -54.99647 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50f751a-7e51-3468-8cd9-1ec693663244 | -7.73889 | -44.72968 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c64a5a50-49d2-346e-8317-139a5a1cbb9e | -9.24466 | -57.06865 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a3a6ea-c62a-3aa9-b916-d7890de3e9b1 | -6.26802 | -52.80483 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4452be35-ae2d-3033-b6f0-ffa314dac880 | -5.73417 | -45.36869 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09f02623-cb43-3604-adf2-b160fb64a1a6 | -7.36575 | -44.31589 | 2025-09-08 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c12025cd-0efa-3d49-9ccc-a5247a4da326 | -6.61558 | -53.14992 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41c69cb0-e7f1-3dba-a22f-76eab91b5fbe | -10.95948 | -46.81621 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f44f287b-8cc7-337e-b137-956e7c6548c4 | -6.61869 | -53.34552 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 346d24d8-0dfd-3a4e-a910-33cb06cdc1a1 | -6.72551 | -51.96476 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2302721-5a48-3abb-8cdc-9c8a994b2414 | -9.15008 | -46.07418 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39cb2f98-2f4e-3408-8005-d108222b4840 | -7.8264 | -45.41781 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 066da457-9ae2-39a7-bea8-3c348b9c51f0 | -6.35052 | -55.55632 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdf37a8a-608d-3cbf-995f-1225a21b8579 | -6.82217 | -52.80742 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28b09354-0d6b-3690-b150-a1112e164531 | -5.85764 | -45.29172 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4093507-eac0-3301-9e9e-0459c812f6b2 | -6.84644 | -52.85069 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 295a37f2-e241-3e9b-84fc-481f9ec868e6 | -8.20686 | -50.14024 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9c74c5d-22b0-3b28-8f37-ead38c10f0a9 | -10.95884 | -46.82087 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 5888d9bc-1a95-373b-951e-4a3b5d3d2186 | -9.33249 | -55.1939 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a635fd8-361a-3eeb-857a-7a872888c9f1 | -9.53986 | -59.06289 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5dbd8b3b-92ed-324d-9747-b3b86b2cbf12 | -11.0288 | -45.9319 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f7122b1-85bb-399e-8914-b7b5ddabd613 | -11.03092 | -45.95372 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 13d1b88d-256c-38b0-bfc6-7002e6544fb9 | -7.04037 | -43.25609 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a03285da-4bcf-354d-abcd-2be434348ebb | -6.2081 | -53.27309 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4b6661-1ca9-3076-9c04-59673a4c06e2 | -9.33263 | -46.52742 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51822fbe-1c4b-362e-b107-6617d8f81686 | -6.17673 | -44.73856 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618acb07-6c2e-3aa3-9402-c092d0441b17 | -5.88869 | -52.09781 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b3d9b91-a59f-3627-acae-596e36a478c1 | -9.99198 | -51.66693 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b3bf0af-2cec-35ad-9f5d-689740232da5 | -6.22804 | -55.93642 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66d86c3c-44f4-309b-936e-bc9ad5bc6069 | -8.48142 | -45.16854 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f554a1-72e9-3647-a74f-18e373f8ee8b | -9.83627 | -47.79204 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cabca5b-9195-39bf-820e-87f045169bf4 | -9.24541 | -57.06414 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125a6605-b068-38e2-8639-14ab2d5a075a | -6.87961 | -44.25491 | 2025-09-08 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b2a977-d3f3-3ddf-8fa9-6a66df1b1bb2 | -6.62202 | -44.10896 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dea72552-46e3-381d-8848-29e76858be05 | -6.2277 | -45.03134 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4e20ca9-0070-35b3-9326-7189ee1237be | -7.81568 | -45.42199 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbf6f232-38a0-3350-b899-866768c471f7 | -9.14204 | -46.06271 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0a56f4f1-050b-3298-8079-05bb1f94b230 | -6.17909 | -44.7738 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29227a17-fbc8-382d-b687-f39b8e71b96f | -6.38345 | -42.59844 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fcff94c-f76b-3f83-9ddd-0cc3e1eed5aa | -6.61403 | -44.01106 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| adb8ab3b-5b1d-32ac-952f-ca0bdbae3e9e | -6.31216 | -43.82452 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd0ab7e2-8938-3747-b878-92885ea0b3c1 | -6.18988 | -53.25959 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f331dc90-d10e-34c7-bcbc-4fbb4a985206 | -6.6216 | -44.11209 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 693437f0-4098-391d-b92a-1230b4fbbc00 | -9.72267 | -43.98664 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61630db6-a2d2-367b-8022-3317799aa33d | -8.86653 | -52.01266 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e255246-fac1-3286-a3fb-29f4c6572528 | -6.96632 | -62.9394 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45424117-d23b-3ef4-a846-246d2ce8cb64 | -6.53832 | -44.79666 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e848036-af6c-3fbe-8ea9-9486bdfbfe53 | -5.98453 | -53.59076 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42dbf36d-c705-3f15-86bf-a5104fc3950d | -9.99141 | -51.67077 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45e376c7-ed9b-3fc0-bbce-5334e544f49e | -6.96207 | -62.93075 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fea0ec8-fced-344f-889e-52068e180d0b | -6.1357 | -44.23774 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ffbab87-d8b0-3001-926c-a3cd2589fd95 | -6.10761 | -44.14096 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 179c9a06-34a4-3ab7-9ea2-ccb06de6d01a | -6.54688 | -54.99269 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47222888-911d-3a48-a852-e604ccfdb4fe | -7.09931 | -42.93926 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2138e4c7-9eab-3bac-b73b-af5c4935c2dc | -6.46107 | -43.95009 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9836baea-5bb6-3221-aa88-97cab4c3c5a4 | -10.00502 | -51.62653 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc7d3450-d063-34da-9222-e3c9c48f1801 | -5.07949 | -42.41703 | 2025-09-08 04:51:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 833c904b-ee7d-36ae-ab5a-72fc81f0caf6 | -10.28843 | -48.8092 | 2025-09-08 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c3e5de7-0d4d-316e-9005-8daebc88f62b | -9.19846 | -46.03482 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9330edc5-4739-3549-83cc-a8e99e74cdc9 | -4.19839 | -55.12978 | 2025-09-08 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f468b75-89af-39df-a024-349446ade53a | -4.43165 | -55.16895 | 2025-09-08 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 038bba39-ff65-379f-9dd6-38a27daa8583 | -7.22009 | -46.19055 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bfae8e0-8473-3dca-bbf1-b3cb167a27f1 | -8.20326 | -50.13982 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README63.md)
