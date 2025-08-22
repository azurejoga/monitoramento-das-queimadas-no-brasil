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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54e73bdc-750e-39a9-8abb-b3ad29bd35c0 | -6.16226 | -53.77126 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f274237-1099-3136-bea2-f0daf65490ca | -5.88121 | -57.75308 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f412b7be-c8cd-3b59-abdc-4ef8ba4c5287 | -3.48067 | -48.93444 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a5eb211-8c10-3dff-9b49-27c27584adfa | -5.67847 | -52.20959 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34d4539c-003f-37fb-a46b-e0b585d55840 | -6.5053 | -44.58569 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6100204c-5c29-35a4-b850-f44f7b57aa7b | -4.55758 | -55.96799 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3d07b2e-5ee5-3829-95a8-9d7cebe96d02 | -6.89348 | -52.86044 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fa913ed-4072-3977-abc8-c1784c131110 | -4.83732 | -55.7666 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f5cd136-5f42-3059-b7a0-652a9c48e80a | -4.77688 | -45.32335 | 2025-08-22 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a7075d9-9ed2-3a40-baf3-693223ccab99 | -2.30268 | -48.14698 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36882d35-d712-3aa9-9c86-cc8a600a84ff | -6.06837 | -44.1052 | 2025-08-22 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09bdbf10-d132-341d-85da-00e132f5b1e7 | -3.59441 | -49.44916 | 2025-08-22 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e3b64b6-113d-3ace-b657-deb349760b62 | -4.14004 | -46.46148 | 2025-08-22 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96773b5f-9e27-3ff5-8349-f027a1fb4c2e | -4.83003 | -55.76914 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac415b26-2104-3ead-8116-faad079e4a4f | -7.62024 | -46.26595 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04e2cc78-8661-3db6-8614-d347c1ac9845 | -7.61466 | -44.37905 | 2025-08-22 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f433cbe-2e8f-3b49-91a4-86c4e35eefa9 | -6.29027 | -43.70355 | 2025-08-22 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5084db88-02e8-3dfa-8bfb-f70054f29dfc | -5.87687 | -53.62997 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f7c9cc3-4f31-3f66-99a1-77796819c695 | -6.2525 | -53.68659 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4248e6b7-a0e8-34eb-b678-7724f9945e05 | -6.93792 | -44.28921 | 2025-08-22 05:10:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49f5064b-ba85-3d87-a249-f5902cfa7801 | -5.52748 | -46.41807 | 2025-08-22 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef135014-c50c-3663-92bd-713566c16f09 | -3.92346 | -47.68596 | 2025-08-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6057cd33-a503-376b-ab5f-425089093784 | -6.30142 | -43.8937 | 2025-08-22 05:10:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dd68e9d-e36c-3877-bd27-e2a56a6ec6f3 | -2.6975 | -48.21006 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8855823c-2d8e-36aa-a47b-9da65b940683 | -6.25527 | -53.68474 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6f0550-b1d6-394e-8081-61ebe4441633 | -1.50063 | -55.92145 | 2025-08-22 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97b98a37-787f-3c71-9791-a1d9a5d97703 | -2.91433 | -48.30338 | 2025-08-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4abed7b-0e41-36e2-942d-8dadbef60cac | -5.87446 | -53.62053 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d918e7b-d4bd-30ff-bb74-734822a280bb | -4.32499 | -55.13446 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 168f7cdb-d4e8-33a0-9913-37bf3bc45e76 | -4.12949 | -54.89849 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 520477a1-b61c-3b27-9d32-8a5ea73701f8 | -6.16532 | -53.77622 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4510124f-9fc8-3cd3-8af3-d1d2e11b622f | -6.29905 | -43.89154 | 2025-08-22 05:10:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8adc64b-231d-392e-8def-93feb5dec467 | -3.88527 | -54.21548 | 2025-08-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 811aa4f4-7c26-3a89-925b-8972e11f575b | -7.64143 | -45.24268 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0dc255b3-9a98-3035-99ea-80ce5b52d48d | -3.17348 | -49.47627 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 241dd771-633e-390d-a9cd-69daf335d0b2 | -6.94578 | -44.28316 | 2025-08-22 05:10:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 544bcee4-115f-3358-8c55-7fa53709d7aa | -7.16437 | -44.67027 | 2025-08-22 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bb726d9-398e-315e-8e07-edbf0abd3e57 | -5.45832 | -51.44603 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be38d218-8ef9-3267-b293-5240111dd1fc | -6.63183 | -55.27452 | 2025-08-22 05:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b65bb12e-6e99-37cb-a4fb-0d03277903ed | -7.86754 | -47.00462 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 168f9569-b2dd-3775-8207-6464678f9b25 | -6.74037 | -50.95357 | 2025-08-22 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2becfc4d-7ee2-398a-bb64-75553bac178d | -2.47348 | -47.76723 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a33b39b4-0947-361a-8474-47fef2cc694b | -6.29438 | -43.89254 | 2025-08-22 05:10:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f46fdf8-5824-398c-b57f-9033f95653ad | -5.67791 | -52.21336 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8da6a8f5-3642-3aaf-a8fb-b815a4caa9b0 | -7.64075 | -45.24812 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 81fa2ebe-0f48-387a-97e4-dd965a907cdc | -4.40792 | -44.08742 | 2025-08-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acfbdb58-a675-3746-a1e6-2dc6a89026f6 | -4.40695 | -48.94748 | 2025-08-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da948db3-6d5f-327f-8d1a-716174c67ad1 | -7.84591 | -46.98373 | 2025-08-22 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978b4845-4824-3654-89f1-6a843a289f2f | -2.47252 | -47.77348 | 2025-08-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b63de09e-d9b5-3599-b9f2-0595a8177a41 | -0.74797 | -47.75408 | 2025-08-22 05:10:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b7cc5a9-10bf-33dc-aeec-850ee304fce7 | -6.4501 | -53.39397 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfc1dfe6-771b-317b-bcf4-4d92f61b9da6 | -6.27228 | -53.70811 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d9e7fef3-1393-3e8d-9b47-5d14a741bfa7 | -4.32841 | -55.13499 | 2025-08-22 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a300b915-8f51-33e7-997e-a5b17255413d | -6.44316 | -53.38809 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f581319-3978-3322-9efe-24421f5d008d | -7.62068 | -46.25065 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1a8e4f-9a5a-3549-aebd-c5ce15cee3d6 | -5.43854 | -60.16242 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ca4c23e-f214-3a7f-b99e-8a657fe41044 | -5.80368 | -59.21374 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e980aa02-2cd0-302b-a122-bc2ff6ce274d | -5.87887 | -53.61654 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d36ff57-afa5-3471-a353-a02288c4f160 | -2.84661 | -48.78582 | 2025-08-22 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b956e8-5572-3592-a89a-d7df62eb5e34 | -5.81049 | -59.21482 | 2025-08-22 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93079555-6bc6-37f1-b1b4-b0e175dcce37 | -4.94906 | -55.79153 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f3080b-9dcc-3830-a1b0-423ca14f85fa | -6.42425 | -44.67831 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d98251-b15e-3c38-a1af-12bb9202f369 | -5.87993 | -53.63503 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e196c1d-5f49-3ba5-aae3-6630555b3edd | -3.23693 | -46.78604 | 2025-08-22 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80ba6b85-c4bd-3e5c-8887-6ed3bd5b3a55 | -6.44698 | -53.38866 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03d1949b-d489-3bb6-951e-caca891301f7 | -6.52007 | -43.86462 | 2025-08-22 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1b66855-e3a2-375f-a2ed-651b4242b92b | -6.27293 | -53.7037 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a28ef76-2af9-306a-bad9-ba26a11b4e75 | -2.93206 | -53.69984 | 2025-08-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7309d9fd-f4cb-3f5b-ada4-eede41de1d44 | -6.26372 | -53.68829 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7614e5a9-f32e-3bbe-8551-49915dc40200 | -4.7739 | -45.3263 | 2025-08-22 05:10:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 197893f8-0942-3e13-b404-ca27d6c762a7 | -6.74486 | -50.95426 | 2025-08-22 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a620ad60-d8cf-3906-b565-3f608fd4da2a | -7.62563 | -46.26159 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f013c035-613c-3683-bd98-f18a9e1f8fa9 | -4.10176 | -60.66282 | 2025-08-22 05:10:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| db6f0837-8040-361a-8253-49d03d195d60 | -3.92297 | -47.68937 | 2025-08-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7a71b2d-6cb0-3dcb-9ca8-4443e78c5ec5 | -7.25034 | -44.70396 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 138a011b-de4e-39ad-817d-463298d2a681 | -6.25315 | -53.68212 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9bd9b17-b025-3c21-b524-8cc4ea2456b2 | -6.63719 | -47.90138 | 2025-08-22 05:10:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5348a3e9-19f2-3d68-a221-2e70ddc3e630 | -7.62165 | -46.25549 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 228a2695-225c-38a5-9190-29b372ed6c7d | -7.64406 | -45.24125 | 2025-08-22 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5833a20b-2c15-36df-b542-63194f139ba7 | -4.21119 | -48.56276 | 2025-08-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5af6986-ccd1-3f4f-a374-e6c4d43f6ec8 | -5.22294 | -60.28809 | 2025-08-22 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4521326-0601-39f5-85e7-465595d3007b | -2.8129 | -49.20174 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6152c94f-d901-3364-9a5c-7c5221d76026 | -5.88398 | -57.75704 | 2025-08-22 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b97c94ac-489a-3412-9250-56a403a496b2 | -6.44906 | -53.37452 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da2a337-7317-30fd-8a15-c7ab8d5097e5 | -3.04355 | -49.42966 | 2025-08-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c931e11a-34fb-3df3-bf3b-24228c7d39fd | -2.93565 | -53.70039 | 2025-08-22 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92d83509-bad1-3f95-81c2-c4bea2358096 | -3.7404 | -54.26312 | 2025-08-22 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f079e0c3-2482-3891-a8c8-1425718c072d | -6.72056 | -51.97732 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef35b1d3-33ae-367c-a705-190e91791408 | -6.43702 | -44.52354 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f854f4a6-1540-3ac0-99be-bc4cd545ccb9 | -2.2562 | -47.85109 | 2025-08-22 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e164d01-6fc8-3041-ac6e-73f4749969ef | -6.94495 | -44.28967 | 2025-08-22 05:10:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e87e720f-7ce5-3c9a-9da1-d3f67679f509 | -7.2518 | -44.70285 | 2025-08-22 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82883b0e-003c-385b-b6d1-f9e55b2d869a | -7.62844 | -46.2522 | 2025-08-22 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf7dc9ec-a061-3a88-aa8b-5adb20e5fb86 | -6.93956 | -44.28374 | 2025-08-22 05:10:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 715056d5-4fcb-33d8-ba05-70621f213dd1 | -6.44247 | -53.39282 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb89389c-6f42-35b5-8502-e2ef3056e990 | -6.27183 | -53.68514 | 2025-08-22 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5d763a0-0866-3164-bbf8-38938482db64 | -4.8334 | -55.76966 | 2025-08-22 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 073dc405-3869-3a3c-967c-07f258c7ae9f | -6.29828 | -43.89757 | 2025-08-22 05:10:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4ba7a5d-a35a-3332-a03a-32b9566ed6fb | -4.40245 | -44.08635 | 2025-08-22 05:10:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 82340b54-474d-3612-8403-314f70b5a09e | -6.53616 | -45.45742 | 2025-08-22 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README44.md)
