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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12a58ec1-d7cd-3df8-be53-8dc503176adc | -11.14757 | -54.8062 | 2026-10-09 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 368e2af5-b1ea-39db-88b5-81a540fc2b62 | -9.03314 | -44.38614 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbe256e8-2d76-3616-8bf1-a1fe8fc42465 | -10.17307 | -48.05277 | 2026-10-09 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9acb6b0-9e52-34fe-85ef-6098d2f8f7f8 | -8.90379 | -45.2361 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d333d04c-18bc-3caa-9277-c724a5addb8c | -8.28105 | -45.73728 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8946b2ee-8d46-3b9e-a23d-e05e5ce76ef9 | -7.47717 | -42.85131 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b0112be6-d890-3783-8878-6513667bc06c | -6.52951 | -55.26007 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d356abb6-ca04-3375-8f6f-f74a970dd9e6 | -13.17923 | -54.30745 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23bda38-aac0-3f88-86a4-3951f4df76eb | -9.28982 | -47.43745 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d0bc43f-6ed8-36c5-9f6a-d12865d44890 | -5.95967 | -55.36518 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84976a65-d87a-33dd-9841-38736caa78de | -10.15851 | -44.67692 | 2026-10-09 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccc86bd0-3c20-38e6-ac4a-850b209d0723 | -12.22659 | -57.09207 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 80aee783-3489-31de-8972-5645ed71f1be | -11.7575 | -44.94962 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 119bf13e-6386-38f1-be1c-bb28188e0107 | -14.04759 | -43.83629 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20b63788-3313-354d-b242-873d740ec851 | -7.45848 | -42.84845 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb025215-9ad1-3a2a-92a4-4f5afe1216ff | -13.78646 | -42.61201 | 2026-10-09 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7dfd256-b8b5-358d-9926-3182cf986750 | -6.10768 | -53.50986 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76995216-f8ae-3c1b-9339-f15347a824b9 | -12.0119 | -43.46984 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51b3db9c-96c3-33ce-b7d5-a1d57d8ae7e0 | -8.30497 | -45.73735 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0b82f4ad-fc94-3374-a455-f575c2068b4d | -12.01421 | -44.24831 | 2026-10-09 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03674de8-f933-379f-a667-53de017b80a9 | -8.06233 | -45.63786 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30588add-038a-3987-94b4-2aec53e8d9c5 | -7.39757 | -54.98529 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 744ec276-ed85-3d56-b6ee-4daac1c50dfa | -11.25655 | -45.25281 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a2be46c-38cf-3161-abb1-6b46de381769 | -8.99016 | -45.90511 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a0eae35-d0e1-3489-853e-671cb2cecb72 | -13.49781 | -44.37403 | 2026-10-09 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f230adfc-d198-3fc1-9475-f2daaf420218 | -12.01974 | -43.4416 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a044f6c-9055-39ac-87e9-19b8b948f640 | -8.95409 | -45.17933 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b28102b7-ce5d-3285-ba5b-37e4437537c1 | -9.12795 | -45.82816 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b06a8d2-7b78-37a2-9f9e-9826497a55ab | -6.5384 | -56.04453 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9545602d-d6f0-39f6-9fcb-41f26fbd8f54 | -6.38656 | -55.26734 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 879cfa29-19ff-3d9d-b4af-5e96f6e9813e | -11.76254 | -46.7814 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88b850a1-50a6-35f1-9160-571939db9551 | -13.02548 | -46.8108 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100e5a3e-1d18-341c-ba6c-37ddb2e451ef | -8.72456 | -45.16725 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1679b4f4-3f43-3ce6-974d-d9f6e8dab88e | -11.00449 | -47.96159 | 2026-10-09 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb6b54b7-ab6e-310b-bf7e-e841addd40e4 | -6.50347 | -55.31708 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5c18c43-c95a-314f-8b20-39f9a2f71098 | -10.01896 | -48.54842 | 2026-10-09 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eff2256-0b04-34a6-a763-8f05dc72537b | -7.08786 | -52.68638 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9657ddaf-b0b0-3e3e-b102-76ca87f36723 | -13.16673 | -54.31266 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0493cbf-9a90-3fde-a919-5c3459aae66e | -11.7875 | -46.79626 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1180480f-411c-327d-a654-d143255131fc | -13.21166 | -54.35992 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e2c7424-f6a3-3105-ab6e-325df7eb8f20 | -11.67099 | -56.76494 | 2026-10-09 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41647f29-078a-31f9-943e-a84d81b43524 | -9.13324 | -45.83234 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0d4f599-3765-3905-9434-7905873e1633 | -11.07788 | -44.08017 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee0bd1c8-9cd1-3e16-b578-f8d52ac5352b | -11.13318 | -46.16267 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 209cbfc3-7124-3637-b866-14096dd84db4 | -6.44824 | -55.04729 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21f559d1-e96a-39c7-966e-631a9d228c2a | -9.25287 | -60.88583 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820a90bd-80ad-3716-bf12-b6c52789c93d | -9.12827 | -45.84248 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e506951-3c2a-3efc-a67f-d94bbcf549e2 | -12.22196 | -57.08777 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 403fb266-18db-332e-8f9b-f875fec21cd9 | -12.21613 | -57.12413 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1ae28da5-b010-3121-9b6c-17c20f5ea207 | -11.07726 | -44.0845 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc947e44-870a-327b-9f72-f879f8f4b2f2 | -9.95895 | -55.33326 | 2026-10-09 04:27:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59d7423a-7f83-3460-b323-40513fd02d60 | -13.15673 | -54.3336 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c6af50b-a2fd-30dd-af58-c435d4729ce6 | -9.25984 | -60.88727 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e90d9284-b003-3807-acc1-51ca1877483a | -6.2705 | -55.25975 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ddd6e67-93e4-3607-841e-11c22d996379 | -8.90435 | -45.23241 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a0e003c-ac68-368c-ab81-6f9869e6e188 | -5.85689 | -53.45786 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37e3bb5b-eed0-39c7-bad6-8da7a5f48d33 | -10.28053 | -47.82584 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d10ae0e2-e5c9-3482-acd9-0e6634599f7f | -8.33068 | -45.45512 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30bbb4d4-52f6-3d55-ae3e-1823bc5a72ba | -8.97626 | -45.90653 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56301b4b-b15c-3f66-8377-608c74c2587b | -8.97393 | -45.16335 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 519eb7fc-cd95-3733-9f9e-68b2145d8b6c | -8.72796 | -45.16776 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85c38779-2471-3bea-ac3e-fdd17bac5802 | -12.21894 | -57.13839 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44797771-c959-332b-9131-07ae78105edf | -10.98267 | -45.39623 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93dd45e4-8b0f-3d89-a030-f888a22bbb15 | -9.00809 | -45.9408 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6db5ee41-e193-3e30-a34b-b58bbb561dbd | -6.38063 | -56.23146 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdf8c9a9-a6a2-3555-bc3b-3b812b51ac76 | -11.18688 | -45.2934 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45cb7c69-ec32-3ca7-924c-5f86649c2dcd | -9.63095 | -48.88315 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15898a9e-3fab-319b-81f8-2ab8ef50ccee | -7.40115 | -44.75716 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b826cdcd-70ec-3dd2-ac69-415e94d813b1 | -10.41027 | -47.27855 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad67003-873d-34ad-96f4-66380bf9f055 | -5.9958 | -55.37496 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5be57d2-5695-33d4-bf6a-3d222a4f560d | -14.17779 | -48.66288 | 2026-10-09 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a41f1d05-749b-3284-915e-6319918faca3 | -6.85754 | -48.77342 | 2026-10-09 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6448ef65-cbb9-3ffc-9705-2d8c7ed3a48c | -12.8934 | -50.17381 | 2026-10-09 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70c7b3c2-29d8-3417-8fc7-3006f9587d36 | -10.87503 | -44.80031 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fc063ff7-e789-3f2d-b613-165bd3dda74b | -10.8795 | -47.60802 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45d28998-b7e3-394e-88c5-dfb7c95ccad4 | -9.30521 | -47.42565 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 37c8a4a8-b978-35a0-adf5-6d24f02dba41 | -11.60232 | -43.71301 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a8ef272-4b4f-3969-8021-ad517933f811 | -12.21935 | -57.10111 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2cd1a5d2-dc53-3230-b9af-72290683fdfe | -11.78149 | -45.58439 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6814fc59-f621-32cd-a647-6f1986e24fdd | -10.87914 | -44.79683 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1385e396-47d3-3413-9021-ed254491fa4d | -7.41026 | -44.76618 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f489fb2-2d2f-3435-9e1a-7e074493ee03 | -7.39948 | -55.14902 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e15b9cb1-7793-3eac-b763-c6c357bf618b | -11.78261 | -45.57674 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 186c1aee-da0a-3a73-8161-865bfd3c8b38 | -10.40973 | -47.28204 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5b2cd5b-08e4-3dfa-9cd2-eb1198eb0121 | -7.5112 | -45.77023 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4437cb26-6c70-38da-93c8-9abe9c79e47b | -11.75823 | -61.0618 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c69f97cb-f73b-32d3-89a0-439b2adb1e4d | -11.32966 | -46.65553 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad4c75d5-f853-3189-8575-7bfa13fa5b7c | -8.98628 | -45.9081 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70df6fee-c56d-38d1-901f-cfadcc574ada | -12.21543 | -44.61424 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e9a4d20-5ffd-33f4-b6ad-94c9499c577c | -10.91532 | -45.40218 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39050dd6-8dbc-388a-bbd1-49ccbe6d9684 | -5.86164 | -53.45783 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7ec4833-2208-3226-9819-a07aaa1b9a39 | -8.04852 | -49.40225 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f19977f2-c41d-3223-910a-bf5a518278d7 | -10.52847 | -47.32651 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0abd0554-b811-33a3-ab5a-264dea7d0fdf | -11.19331 | -45.32161 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ee875826-f8a3-3b7d-878d-edf249fdfaed | -12.21335 | -57.10977 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24cdb1e2-a07f-3774-b980-99772278cefe | -11.83948 | -43.59681 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebd0d5c0-7fdc-3c4a-86ec-ee9cfa42dfe7 | -6.41211 | -55.19238 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9bcb311-f4dd-3a4f-b2d8-ea859a7109be | -11.7752 | -43.53209 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60dcd6c4-5c21-32fe-a9bd-5622514facbc | -13.45338 | -46.52183 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc5610ea-838f-3298-b8f8-b404c7e4b982 | -6.99187 | -59.10333 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README115.md)
