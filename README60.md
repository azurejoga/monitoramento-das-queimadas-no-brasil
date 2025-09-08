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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2d32030-c995-324e-98be-2f62d6e21330 | -5.00088 | -56.25911 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c47aff7a-331b-3f49-ad80-b1d27b4a87d3 | -11.28438 | -46.51595 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fbd17e7-a9ad-3f8c-8c41-06a70b14fd38 | -9.1843 | -46.0686 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc7f2319-6858-30f6-acc1-b7af81c54474 | -7.13731 | -44.56951 | 2025-09-08 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c82632-6d6b-3c90-a715-2496588be1a4 | -8.19331 | -47.56066 | 2025-09-08 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b6505c0-cee3-305b-b8db-2eb1fae05e11 | -10.78266 | -47.72038 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46c6262b-428c-3968-9c70-000904a9f542 | -3.92942 | -56.06295 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 936b8766-2a6d-383d-b6ba-fef7b7b1188a | -4.00603 | -55.42901 | 2025-09-08 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22cebcfb-46d3-3745-8b9d-7aed83e99c3b | -6.41603 | -44.46041 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04c901aa-cd7d-3340-8c69-d12db1ee19d3 | -6.27156 | -53.43266 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b92fe954-0a3a-3c0d-9e4f-f3a2871b3886 | -7.66129 | -44.81113 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9eecd89-ca47-3a2b-b2f2-063c6f01378b | -6.35428 | -46.37072 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b16b0cc-b46f-3cee-804c-bfb16ab93b8e | -9.82155 | -53.31704 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e6f4837-c02f-3373-87f3-c35a944601b6 | -9.67541 | -51.06686 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d37dc5d6-6235-3cd5-bc43-4ff4d8084b10 | -7.73347 | -44.73175 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bdf5479-63fa-3dd4-aee8-331bbb1c5aa3 | -9.68991 | -51.06516 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ebbe2ba-6e3f-3e25-bef2-537b279c2445 | -8.83107 | -45.89185 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca688932-5057-3c22-afc6-f20fb626890c | -9.15076 | -46.06905 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cec3e4d8-9627-3f3f-b417-eaafb36cd93e | -9.84924 | -48.85734 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6b1f811-8d0f-3111-ba40-d8d74f005338 | -5.25282 | -57.12143 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f32e45d-bed2-378c-8e78-3d7f9716ee84 | -5.4298 | -42.84895 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 695d2f1e-f525-3043-964c-e704e0704262 | -5.88668 | -43.95894 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e910887-0b48-3b5b-9342-7f585e988898 | -6.83369 | -52.79861 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 949bc055-5806-3a13-8da7-9f9d0f042d5f | -5.44198 | -42.80208 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bd95c448-943d-32ef-95ec-f880139c67b7 | -5.8854 | -43.9544 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09af25bb-8445-3481-8ee1-8294464e318f | -10.08357 | -48.09822 | 2025-09-08 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26bb9741-0f30-35cb-9af1-342ad788c1dc | -5.87763 | -43.97165 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1323b164-c3e7-33da-88ec-c43848b73482 | -9.05523 | -50.46634 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 475163b1-84f6-398f-b7e9-c77296dee62d | -10.00221 | -51.64524 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e30cfaf-78ec-3926-8c5f-75edf5652dfd | -6.78087 | -43.42262 | 2025-09-08 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0416a75f-13b2-371d-9073-dfbd376551fb | -8.69857 | -45.31523 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb3d6bd6-a8c6-3d0b-806a-bc37a4579071 | -9.83994 | -47.79649 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e242309-2042-3e40-aa44-b2989c55a498 | -8.14379 | -48.48097 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09f3c5b7-a1fd-3f65-9344-97b6558142ec | -7.7853 | -52.12579 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc552eb1-9442-3769-9cc1-44ecf1f18c73 | -6.2516 | -42.44101 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ade1f081-68dc-3343-9820-e5a9e209d3c1 | -11.32175 | -47.38498 | 2025-09-08 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae471730-ae77-35d5-9719-98afdd84d25d | -6.63527 | -53.36944 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e289b710-b97b-37a3-8444-4d34fb81af27 | -7.22717 | -46.20578 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10a4f6cc-3e0f-3eea-9bd4-ea9993d1957f | -7.432 | -49.26281 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45cdbade-6357-3e35-95eb-ec81354b01ae | -7.68101 | -47.33179 | 2025-09-08 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a41b629-44b9-3ff5-92e3-03cb2ce9b602 | -6.63138 | -53.35106 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe29ae1-f724-3ade-be94-9c7faf7b7c90 | -6.47973 | -41.7738 | 2025-09-08 04:51:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f70dda3c-b7a7-32a9-802e-fc854fad4edc | -4.41609 | -46.29581 | 2025-09-08 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6300d6ee-b2eb-3e9d-a415-4e735227a055 | -6.21387 | -43.37212 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06725bed-b5ed-39aa-b1cb-861595f3af5a | -7.11146 | -63.07325 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcfa5443-0599-393c-928f-1588935d01c8 | -10.99914 | -49.77573 | 2025-09-08 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb49655-5d9f-39d6-b02e-6c3d3013c74a | -9.37534 | -50.38594 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e5a985c-702a-3bde-a191-c7c5540cb379 | -10.82379 | -47.73946 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d29445a-4933-37d7-9c29-b6bfb65ceeaa | -4.89843 | -42.22619 | 2025-09-08 04:51:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13af936e-1dd8-3f13-ad83-8df8e9ccc3f5 | -6.24758 | -43.70899 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db57845f-0c4f-30e3-aed2-3fe59e011611 | -9.9965 | -51.63668 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e03e8d4-7dbf-3183-8784-828d97442f43 | -9.04814 | -50.4651 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f4ac56e-d830-3831-9d92-81ef02144190 | -5.22503 | -43.69684 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7064cbb-6811-39a9-87a0-4ae7bc109569 | -8.03693 | -43.81356 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 38186a17-ac95-3279-9a9c-c2b560418fe4 | -6.28038 | -53.41978 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2bc580e-15b5-318a-ba81-ca927fe57818 | -5.47131 | -42.9145 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6a246d7-ca6b-3826-8217-00b8bc07d5aa | -5.79604 | -45.65538 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2253e528-576e-37bb-bb2d-49b7bc780e30 | -7.02246 | -44.94793 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d35579ce-d304-33bf-8cd3-4db137abc751 | -7.99077 | -45.46502 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7101f742-013d-34c8-a741-6dce22638082 | -6.52866 | -42.92604 | 2025-09-08 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91b24642-dc87-31ca-bfc5-6684a38d44a6 | -7.8679 | -50.9911 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d69455e-e66a-3bd2-a364-82bfd9561986 | -7.78493 | -50.75301 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2ebb75c-d526-3cf6-b446-ac94662920d6 | -5.21982 | -43.69602 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c21c766-b0c5-396f-87c0-7a75add399ac | -8.03446 | -43.811 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8e96c30-d1f8-317f-9c6c-1687ee9d3286 | -10.47506 | -47.73074 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24eed6b2-9d2b-3258-9771-87aff0f77a7f | -10.96407 | -46.81861 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3a388a3c-de3a-3bfe-8b8c-c4f76cdb5775 | -10.00273 | -51.61847 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e782dd53-51e7-3da1-809f-40975c88a1f2 | -3.82052 | -54.1187 | 2025-09-08 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebd19770-d9f6-3626-b958-13d53f7c8dca | -6.54404 | -54.98835 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c33c051-0773-3e63-b9b0-c36fc3ac7b24 | -9.56688 | -53.59688 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b132343b-d14d-345a-8885-fff5bc39b4f0 | -6.70321 | -52.08666 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720e0ef5-1469-3039-b5f5-6b01b8f11315 | -5.88501 | -43.97107 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 222491e3-ce7d-3478-acea-aee67ddf439c | -9.97084 | -55.04261 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d91e61-1ac0-3085-a98b-cd5bc18faf6d | -7.7306 | -50.34612 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a222043f-c503-3438-8d65-c515784dcaf5 | -7.0002 | -44.92798 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b176c95a-afd5-3e3a-ad92-58f280522da8 | -8.1967 | -50.13476 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69fce098-4281-3ffb-9a26-d8499ae19ba2 | -9.99597 | -51.66357 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8e714cf-4945-3b5f-9a29-cd6601af1e02 | -9.14606 | -46.06846 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 229ab3e4-6396-3f6c-be3a-56a57fe2fd97 | -10.00732 | -51.63452 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f96a5e51-35b3-3da4-b9f1-e6f0305239b1 | -7.78839 | -50.75354 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a25942e-5d91-334c-8f44-6cf4d726f20c | -7.70912 | -44.72173 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c375dfd0-d919-31a9-b55d-4b589d9b50ce | -5.82454 | -44.12237 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0719e22-59fc-3402-953a-6ca82bbb2de4 | -6.40064 | -44.46029 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 484af670-20f5-326d-97ec-f5776f168612 | -5.83273 | -46.11969 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df7cffa9-0475-30dd-a53c-738d4ad84a2a | -11.32828 | -46.56548 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7102bc71-e2bf-3e8d-bad5-25962f673279 | -8.56529 | -51.29379 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd8a6916-cbb0-323b-ab5d-e8186cb639a1 | -8.84027 | -48.10397 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72decdc7-a2c1-381f-99fa-e02949ba3826 | -7.03584 | -43.24985 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0448edd-8d98-368b-a3ab-94e3219e89f6 | -5.95062 | -45.75298 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cac24874-a3b4-3957-ab33-29980ea41e1c | -9.85177 | -53.29683 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60922559-da7b-3f6f-97f5-1d524db65ada | -5.79536 | -45.66013 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 263756cc-6858-37f3-b552-f07b41d1afc3 | -6.62479 | -53.37136 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17732c25-3ab7-32c1-9387-47f0aee493e2 | -7.90172 | -61.7803 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8462523c-466c-35ae-821f-6d881ce12e17 | -5.55502 | -43.79079 | 2025-09-08 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56ea4326-699d-36e6-9edc-00427e847633 | -6.81785 | -52.83502 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25a9de05-6596-3da8-bf0f-e28c2d6e4c9a | -5.56467 | -52.08229 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 581e108e-969d-3149-b15a-f746b6db5627 | -7.44438 | -44.93475 | 2025-09-08 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8894a7e4-5d3b-3afc-be27-4c10ef3d7e29 | -9.20315 | -46.03564 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 396c4ab2-31cd-37fb-b4af-0c76acb185b6 | -4.45403 | -50.67236 | 2025-09-08 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1687b1c5-3105-3a84-8bae-262518a8ae44 | -5.88153 | -43.95804 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README61.md)
