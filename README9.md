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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edb627d7-0b36-3001-a227-f4daad067da8 | -22.3869 | -45.4716 | 2025-08-13 01:20:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 207.6 |
| cb91f145-3aa3-3f4e-b5d0-4c13ae2587bf | -11.7695 | -48.2021 | 2025-08-13 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| fa3c24ae-dcf7-3d80-af84-5d5ca30f3ecf | -15.0981 | -51.3612 | 2025-08-13 01:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0289ce99-dba7-3bbd-8a7b-3e5953968841 | -15.0787 | -51.364 | 2025-08-13 01:20:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| d6f38f0e-6098-3df2-8102-02346e6b9d69 | -8.1246 | -55.569 | 2025-08-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 78c3b2e9-f461-3503-a6b4-684c0fc62203 | -7.1298 | -60.1374 | 2025-08-13 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 32f8b5e0-b314-35d5-8501-0780a9a50272 | -7.0935 | -60.0237 | 2025-08-13 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b7eb7370-6712-3136-a418-023d4487530b | -8.1061 | -55.5501 | 2025-08-13 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3e09bb8c-48a8-3ce5-9c39-f755a206e847 | -7.1483 | -60.1174 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 77100104-f1df-3fef-b325-ad167af6860a | -22.3877 | -45.447 | 2025-08-13 01:30:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.3 |
| 7d6126ef-dd3b-3be2-89c7-b80554782df8 | -9.1892 | -59.6752 | 2025-08-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0ded7c44-84ab-325e-a2a9-2335684565c4 | -11.9938 | -45.1496 | 2025-08-13 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 993b5016-0dbe-366f-bd12-26da0a762cc6 | -15.0981 | -51.3612 | 2025-08-13 01:30:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| f2898fd7-7f52-388d-a6b7-b7a975093d14 | -15.0787 | -51.364 | 2025-08-13 01:30:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 8cb094e9-7cd8-3f5e-8bce-894795a31e42 | -7.0935 | -60.0237 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| cfd407f7-6bc5-36f1-b2fb-a8467d0bedc0 | -22.3869 | -45.4716 | 2025-08-13 01:30:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 169.2 |
| 7d9b800e-56ba-3a5d-8a75-355dc1506cbb | -2.9108 | -48.254 | 2025-08-13 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3884f48c-a125-3941-9271-7fd661743b56 | -7.1299 | -60.1182 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0143ab4a-6f7a-3398-8612-644fcfbaf7b4 | -11.7699 | -48.18 | 2025-08-13 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 20347ce4-fc75-31fc-bb6e-6a5883e3870a | -7.1482 | -60.1366 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 888d0ad9-9a2c-386f-83cb-8975366c3218 | -11.7695 | -48.2021 | 2025-08-13 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fe26f228-9c1a-325b-afa1-cd29320dd1e8 | -9.1894 | -59.6558 | 2025-08-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 284b28f5-37a6-338e-a8a3-66a3e24ce907 | -7.2562 | -60.6302 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a19a47f9-6029-377c-9e70-325f392171ce | -7.1298 | -60.1374 | 2025-08-13 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 211b2faa-04ae-363d-add2-59c0465cd7ae | -7.2562 | -60.6302 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 58530e9a-3ad6-332a-9e06-bcd0bc1d0832 | -9.1894 | -59.6558 | 2025-08-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 96a96958-df43-30c1-8db2-79660544629d | -7.0935 | -60.0237 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 451b9a98-3b91-3f2c-9cec-0f8ad94e2d56 | -15.4616 | -49.6524 | 2025-08-13 01:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| dcee4779-30b0-32b3-95b3-12a9bc3ea565 | -7.1298 | -60.1374 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e3d6c3f6-4df2-3c88-8358-38dd9f7ea57d | -8.106 | -55.5701 | 2025-08-13 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 15bef609-db52-3a35-bf01-5b19e9ea49b9 | -8.1246 | -55.569 | 2025-08-13 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 13a725fa-4ba1-33f0-9990-f0480f27df1b | -7.1483 | -60.1174 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cf6dd284-ca1f-3043-a2c6-9d17cda9797d | -15.462 | -49.6303 | 2025-08-13 01:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 733a409e-01b6-3fbb-8e6a-a5d6ead35c3e | -11.7699 | -48.18 | 2025-08-13 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f99d2b28-636e-385f-924d-ae8f287780af | -7.1299 | -60.1182 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 23d1afe2-366d-35ed-adf8-4985770b74be | -11.7695 | -48.2021 | 2025-08-13 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3bfff0d7-7770-3d39-8af4-3944b2436a10 | -7.2746 | -60.6294 | 2025-08-13 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e57c5049-98c8-3e08-bd07-789b3bbb6977 | -9.208 | -59.6548 | 2025-08-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 55fe2033-5f85-3a85-bc97-c630efd8eff2 | -22.3869 | -45.4716 | 2025-08-13 01:40:00 | GOES-19 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| 61e3aacb-829c-3ca9-ae7b-d00d251e6fd3 | -2.8923 | -48.2546 | 2025-08-13 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a9e9a6f2-8232-3ad2-a4d3-99b36d6a1d5f | -15.0981 | -51.3612 | 2025-08-13 01:40:00 | GOES-19 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 9d5075d2-ae1b-3da5-9549-45dfc149f62e | -2.9108 | -48.254 | 2025-08-13 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a442afc3-b48c-35fa-9dd6-0dd6cf072286 | -6.86457 | -59.15441 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 77a154de-1c4d-3090-a931-61b5a770cb01 | -7.25271 | -59.99986 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f0755029-25f7-3f55-9bfe-576481ee07a7 | -6.88246 | -59.17688 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| b69a7e50-021f-3bb4-917b-9ae19be1cfe6 | -6.8862 | -59.17063 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c8e728d2-29be-316e-a7b3-30f790ae9278 | -7.45946 | -59.88976 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6bb6e714-70a2-3902-ad47-c121de2da981 | -7.08519 | -60.01711 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| a32f7361-cbe5-3296-bada-152aeda4f2dd | -7.07512 | -59.20433 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 41bf7af1-6f2d-34c7-a785-f4c1869dff3c | -6.8721 | -59.1729 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d58f675a-27dc-3ce2-9638-bd067e84e4fd | -6.86814 | -59.14819 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| bdd261db-7e59-38a0-b209-6dbdcf5a5f19 | -9.06288 | -60.64706 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 275f9919-5280-3d7f-a85d-06d9696f3e57 | -6.92463 | -59.13899 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8161b276-ca64-3f9d-a15f-48cd47236dcc | -9.05087 | -60.64909 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 335b5256-1a55-33d6-ae19-7e6a1ee54f29 | -6.87488 | -59.12697 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 914dc4ae-7932-3c13-8ac1-e55a51780297 | -7.14072 | -60.11448 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 1f41928d-9902-358a-8289-e82b5a233c8c | -9.19593 | -59.6604 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 977df566-b207-3df1-8822-99302c17ca21 | -7.13096 | -60.13733 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 4725a7cf-1e59-37bc-ac80-e9e7643a59b6 | -7.08856 | -60.03822 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| fe23d5e2-3694-368b-a724-2bcb4dde66e0 | -6.86412 | -59.12314 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 74829e16-c52c-35e1-8f57-d0e0c69bb789 | -6.89636 | -59.14344 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1113.4 |
| 25d86b61-a467-350c-ac39-bb5ddddc2ea7 | -6.93256 | -59.15636 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6d7e90c1-198a-31d9-9224-6026e7d4ee80 | -7.07077 | -59.21039 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3c04c3f9-524f-3b06-8497-4dfc2a469479 | -7.14396 | -60.13532 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 8c20ac58-8792-37af-8058-25a62e14ab2c | -6.92854 | -59.13171 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a9561c1a-748d-3ab1-9915-f59a2bbf444e | -6.92846 | -59.1636 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 00b77a6c-72a9-3b2d-b99c-ba4376817b7c | -6.90662 | -59.11651 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 77f82837-89ad-3b52-9d3f-b1845cd68196 | -7.45532 | -60.63041 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a6effa69-6d2d-3860-b018-8aaa029b3438 | -6.87826 | -59.12072 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6fc89534-70ad-3ea8-9ff7-307727d59da5 | -9.16993 | -59.66452 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| c5485570-8436-3980-a169-77b48d216709 | -6.90028 | -59.16828 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fd64f56f-ffc8-3e69-9c87-d596b305d02b | -6.87869 | -59.15208 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 466.7 |
| d3c81b34-eb9a-3962-a6f7-3ef3519a851c | -7.12771 | -60.1166 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d08659a4-0777-3364-940c-892d2932e03b | -7.09141 | -60.04442 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 10eb3648-16b9-34d9-be72-15f799cffadd | -7.45731 | -60.6245 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8cfd4218-68fd-3e29-bacc-7f951da5526d | -7.09832 | -60.01507 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e3114a2f-44e3-3003-9263-702869086cec | -7.08823 | -60.02336 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 0cbb5703-dfce-3a0d-9cf2-c63f1d87f0df | -9.38378 | -61.52864 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c9bb766f-339d-3043-931f-491cbed65809 | -6.91048 | -59.14114 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 63b16138-c3f6-3a08-a7ee-26efcc3b7ec8 | -6.88225 | -59.14579 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 822.3 |
| 3a686082-aa4d-36f5-bb65-2e2a33d879a9 | -9.05358 | -60.6663 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 73e9c017-8454-34a4-abff-f649b53b7d5d | -9.06557 | -60.66426 | 2025-08-13 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| dc2b7d89-30d9-396f-9646-b1a16918d840 | -7.25573 | -60.00592 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 144a3b32-6650-330b-800d-d68c9b8effb5 | -9.51256 | -62.37348 | 2025-08-13 01:47:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd8119d2-05c3-3339-b140-2885b871a78d | -7.10168 | -60.03631 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 543e235e-4962-3699-83fb-4e924aecfc60 | -6.89245 | -59.11868 | 2025-08-13 01:47:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 842df52e-b9d4-3957-9b30-ef46950e3b52 | -7.45002 | -67.7375 | 2025-08-13 01:49:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9386bc80-85c9-34c3-b392-bfd6b050c1a3 | -5.88394 | -57.749 | 2025-08-13 01:49:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| c4d7e8b2-078a-342e-8723-57a78b8761fc | -5.89202 | -57.74211 | 2025-08-13 01:49:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0a611ed7-1405-3456-813a-a6d7db7fcb44 | -11.7699 | -48.18 | 2025-08-13 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| b753b4a8-f85c-3367-96ca-63a58aeab8f4 | -8.106 | -55.5701 | 2025-08-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8c30bce2-04d4-378f-9a2a-541fcbd8ab57 | -7.1299 | -60.1182 | 2025-08-13 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d97e06da-74d1-3718-a8d8-b593d3fdd525 | -7.0935 | -60.0237 | 2025-08-13 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e77cba88-e569-3672-b6d5-df7eeeae60a9 | -11.7695 | -48.2021 | 2025-08-13 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5f9a8baf-f020-3d38-93c2-671c3ec4bb0a | -2.9108 | -48.254 | 2025-08-13 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7ad2aad4-0937-3d07-9c3c-a703d7fddf36 | -8.1246 | -55.569 | 2025-08-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 49e3db0a-c1a5-3a2d-aa1f-bfe4fc4b0036 | -7.1298 | -60.1374 | 2025-08-13 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 934d649b-b373-3df6-a457-92fe5e933dbd | -9.1894 | -59.6558 | 2025-08-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b38cdff8-bc74-3e26-8982-edc5d11a7276 | -9.047 | -60.652401 | 2025-08-13 01:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 713b0eb6-efaf-365d-8414-15c3d0f67709 | -9.0374 | -60.654999 | 2025-08-13 01:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
