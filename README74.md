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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a801d5a-ac29-3b9e-8563-4e5e79655f14 | -13.51704 | -61.75854 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036456ce-02a8-3831-b080-1b525714ef15 | -13.51301 | -61.75794 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a985d9b-65e1-3b34-90f3-3c601aabb993 | -13.51252 | -61.76157 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86dadcc3-6b09-31e2-91ab-e90a78e9205c | -13.37673 | -61.96537 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb18a278-c664-3c9f-ab68-70b794329b25 | -13.37601 | -61.97063 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c981daf2-74be-3e0a-b1d5-baef3a701e5a | -13.36144 | -61.34336 | 2024-10-15 05:44:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 363f40ec-99bd-3e22-9de9-2956523e8cbf | -9.11355 | -62.6392 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8687ef1e-eb88-339c-81d2-0739639886a9 | -9.19541 | -61.67121 | 2024-10-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c87b066-3868-38d9-8419-e0fcfa11c0c9 | -9.15801 | -62.41608 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8ffc98-1d70-343f-9a71-10796abf4259 | -9.11484 | -62.63764 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e775f969-4b0a-340d-a5d4-7a9bc60bb0fb | -9.11423 | -62.64186 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 476089d1-ff0d-3340-a478-3849b448e09d | -9.01293 | -62.56748 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78f6151a-43f6-3902-83b5-42d3cdc3b247 | -9.01231 | -62.57174 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2034fe6c-3af4-38a7-9510-6256a8b68f73 | -9.01169 | -62.56933 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25db7cdd-2718-304a-b253-208f2663b87d | -9.01106 | -62.57357 | 2024-10-15 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d6eaaaf-37e8-375f-b144-8a149fd72398 | -10.34798 | -61.65421 | 2024-10-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d5c1b1-f801-31df-9f47-0b82afbaf1fc | -10.20491 | -61.39439 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 930d337d-ab75-3de6-8cab-7ded31368eed | -9.74865 | -61.99327 | 2024-10-15 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6f1dc02-aa30-3382-93d5-7b4fd0071d27 | -9.74801 | -61.99617 | 2024-10-15 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2228d06b-0caa-36ec-a66f-869238fc4cd0 | -9.61701 | -62.47411 | 2024-10-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70542e4a-94f0-375e-8242-33f1bfeced4b | -9.48477 | -62.37922 | 2024-10-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f0b7ce6-8405-3eeb-862c-b403c398fc40 | -9.43548 | -61.99174 | 2024-10-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 590452b9-2853-3955-a814-6fe2c30f755f | -10.61634 | -61.65854 | 2024-10-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf38f603-1c5a-3d80-9a0f-105615e41373 | -10.34921 | -61.65176 | 2024-10-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef61cf85-aff8-3613-ab61-db0e16443026 | -10.34532 | -61.65115 | 2024-10-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f905bf9-da9d-3b8c-b1ec-32af43bb95c2 | -10.34409 | -61.65363 | 2024-10-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e59d4f-7105-3792-ad42-d8278366b349 | -10.01115 | -62.10371 | 2024-10-15 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13632c40-b05d-3294-be3d-da1eed7e3be0 | -10.00737 | -62.10315 | 2024-10-15 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93e763f6-ae1d-3fc5-a7ee-15fd619a19d5 | -10.0067 | -62.10781 | 2024-10-15 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3830409-f69b-3a92-9087-9835a7ab15a3 | -11.03686 | -62.58351 | 2024-10-15 05:44:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d130515c-d93b-308b-95fd-d20240de18eb | -10.86454 | -62.33001 | 2024-10-15 05:44:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 393c2107-99dc-3e3f-bc5b-8ae2356a8708 | -10.8601 | -62.3341 | 2024-10-15 05:44:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01556f21-9b8a-396a-a7e7-7bda67e28003 | -10.86386 | -62.33467 | 2024-10-15 05:44:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cd2c058-755f-3473-8e38-89943563b18e | -12.96535 | -62.78659 | 2024-10-15 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0b90427c-3d54-35aa-84f2-ac3c2e5b1df4 | -12.82223 | -62.92326 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a49f1992-259e-366e-ba6c-69d40eb117d0 | -12.76687 | -62.93811 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfc6a012-657b-3a2b-b240-cad31980db40 | -12.74366 | -63.03316 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4320e125-a85c-3869-a35d-ec725e6c9985 | -12.74301 | -63.03765 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf2c749c-9cfa-3e46-b55f-54a4d14e365f | -12.71405 | -63.02872 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f61a409-34de-3cae-892b-03156339a586 | -12.71035 | -63.02817 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cebcb1d1-a753-3132-b365-546481e692c9 | -12.69924 | -63.02649 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e53b378-356d-3407-bb21-16a7d53ffbac | -12.6986 | -63.03098 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b36ffddc-2223-399c-abd1-175a142fe275 | -12.69107 | -63.05726 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41961dc3-3512-3564-bb57-33e025cc4d8c | -12.67871 | -63.06456 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5aa31f78-fc73-372e-912f-faa3fde6c761 | -12.67438 | -63.06846 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a348dad-84f7-3870-9e26-2afb46fef339 | -12.66204 | -63.0757 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 609663e3-190f-3bbf-94be-d1951ddff180 | -12.66141 | -63.08017 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2f5ee70-7c3e-32b8-8cd3-11cae97317cc | -12.6571 | -63.08405 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6869285b-f3bf-3d4a-8add-1b928e45d94b | -12.51895 | -63.26765 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57843332-45aa-3137-bcab-f65e073d2e2f | -12.51469 | -63.27144 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0e85752-7248-390e-be59-bc2f062e9642 | -12.51105 | -63.27089 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede13592-412a-3d3f-bf14-60296fbd3989 | -12.508 | -63.00732 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 253814b7-0318-364c-b646-8d842e35facf | -12.48774 | -62.99061 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b6f3fc3-bbea-33e2-8247-a275710a4890 | -12.4797 | -62.99397 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83377641-e4ab-3260-b6e8-d17072d6e1f8 | -12.46618 | -62.98279 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6977f15f-6cba-39ac-a3c2-5fdb2763d2af | -12.46353 | -63.02795 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 406e9577-22dd-3c52-a757-72dd432f0334 | -12.46184 | -62.98669 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59f8e738-ab1d-36c9-a56d-00bc1a5319c2 | -12.45984 | -63.0274 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 943ffe9a-55ee-306e-93e3-a144c7745eea | -12.45183 | -63.03074 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 058cfa8f-b8cf-3eb6-b62b-e673306226ec | -12.44877 | -63.02574 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c357bb00-d782-3c6f-8dbf-11f3b5434de8 | -12.44382 | -63.0341 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a1a0ab-67bf-3a70-a8e5-4a02e230d32c | -12.44013 | -63.03355 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83ac7376-9a07-33ec-b322-e4acf6841a5e | -12.96469 | -62.79124 | 2024-10-15 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 905b2964-10d4-3f67-83c1-8008c903e6fe | -12.96026 | -62.79533 | 2024-10-15 05:44:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfb0732d-da5e-3471-b330-41f202596963 | -12.83472 | -62.91581 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 57c0b583-4de1-3d00-8951-ea15d1ca3733 | -12.74558 | -63.03646 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce7abd56-0552-307e-b174-84ad63857c50 | -12.70294 | -63.02706 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1982f890-5ce3-3d04-8c0c-bb32a1ce488e | -12.7026 | -62.97642 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41a62ce5-22a0-3e41-b2c8-effdad36fe76 | -12.69889 | -62.97585 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98ae8fb5-2095-307b-a643-3c790c482d19 | -12.68865 | -63.04779 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 550946dc-3aef-3119-835e-a0e3a79e9de2 | -12.50237 | -63.02012 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da86a773-d150-3536-a254-83f51b218724 | -12.49868 | -63.01957 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efa2e28a-23e2-33ec-9783-c7724650fce5 | -12.4834 | -62.99452 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf8890b9-b012-3f32-b948-fd203287fb07 | -12.46248 | -62.98221 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b159d69-c526-312f-810f-e3381da805c0 | -12.45814 | -62.98613 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 46236607-b5bd-3944-911d-2ec793e010f0 | -12.45678 | -63.02238 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 82126447-950f-3a0d-9b81-13a9922999a9 | -12.45615 | -63.02685 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e17681f2-643d-32ab-b943-cd631126f4cf | -12.45552 | -63.0313 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c4360aa-4dd0-303f-8c21-d3250e0b462e | -12.45372 | -63.01738 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c913ac5-87f3-3475-8f55-05df3e4f39a0 | -12.45309 | -63.02184 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 20392085-32ed-3b5a-b54a-77f6feb7d44d | -12.44814 | -63.03019 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 348181a7-554b-3cb6-bf43-cbc025da8361 | -12.37397 | -62.97516 | 2024-10-15 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13987345-6285-3b29-9167-6221a6d6c0ef | -9.35308 | -63.57559 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4a204674-6047-3297-807c-4f3cbbf19847 | -9.3525 | -63.57946 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 12e0b04f-6083-3f1e-a415-8e8c51a58b28 | -9.35019 | -63.57117 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d9d6b293-a85e-3994-a58a-b6ca1939e3be | -9.34961 | -63.57506 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5850689-e1c7-3d73-9d66-c9181752cdbf | -9.34903 | -63.57894 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7794b225-87cc-37c1-85be-4d794ca3843f | -9.31161 | -63.82824 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5cf44b4-f885-381c-9a83-90fed42b73e8 | -9.30818 | -63.82766 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad7c2f47-6554-3221-9255-ee1611a5b832 | -9.18115 | -63.41599 | 2024-10-15 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b86649-b8da-336a-8cb6-146610d5f711 | -9.12186 | -63.5739 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66bd038b-4635-37c0-a155-2ad1308724f1 | -9.12128 | -63.57776 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fecbb8c-05b5-31e2-be25-205d83a003f0 | -9.08817 | -63.43023 | 2024-10-15 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a914780-0475-3f55-8f6c-95a2662992dd | -9.01906 | -63.65267 | 2024-10-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9efa080-9ccc-32d0-ae3e-78c680a8be42 | -8.93341 | -63.87195 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| add53b8a-1701-3ade-99ba-af1773cc02b3 | -8.93285 | -63.8757 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef230f28-7594-3856-af11-82dd4309e8a3 | -8.77393 | -64.02016 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bda6bba-31d6-3cc4-a713-5ffdd2c240a7 | -8.75756 | -64.10445 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24fa96be-5713-3811-b79c-c41511395484 | -8.72851 | -63.97521 | 2024-10-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f97cc3-156a-3a6e-b00a-b75d8c7e1c42 | -8.56537 | -64.03009 | 2024-10-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README75.md)
