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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eac76d5-81cd-34c1-b61a-a4402fa3e5d3 | -5.369 | -56.06212 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 155366c1-9ea3-3410-8029-3292b0eb4bec | -3.68946 | -55.95908 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f80280-f90a-33a9-886a-dac872377091 | -3.48064 | -54.73079 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aefa197-ffe9-3f77-933d-278d7056bd19 | -10.88258 | -49.14705 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c50cb29-e331-3b90-abce-c175f4ccab73 | -2.57687 | -56.17176 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 949720e5-0b79-3842-bd28-22753bc676c3 | -8.85157 | -66.80152 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| f738fac1-7640-3f6f-8300-7de087f68839 | -9.24881 | -64.4398 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118c21d1-fa20-34b2-885e-7479933a542d | -1.18702 | -54.13797 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbd61b5e-71da-3e7f-bbcd-72a6205da36c | -2.50246 | -56.15319 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfeb660e-8404-31c5-b8b6-c67040c0b003 | -3.2079 | -53.87183 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f368b1-02ed-35ea-93f0-3d99335dba72 | -3.797 | -50.61016 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b99a1ccd-0f1d-361b-849a-6a8f54be68e6 | -3.27969 | -54.03543 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b3dab20-8c75-3ebd-b666-47a9b0c1b577 | -3.61522 | -55.47115 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9a47e70-116e-32f2-b964-668542790f82 | -2.93449 | -54.05196 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8d9743ed-43be-3c2c-aab4-b4e1fbb8c9f7 | -3.09884 | -54.29286 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8494d49-96a2-3f93-b37b-8934e9c8a86f | -3.44604 | -56.94297 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d478ab22-f724-3dd5-bd08-4a027fcd077f | -2.93963 | -54.17914 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7756a9a-6588-3d0f-96fd-b7b170d0d73f | -6.735 | -55.12708 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf054f2a-57a2-36a2-b62f-2acce191aa42 | -3.53902 | -59.50449 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43f5ee81-7332-3e86-878b-dfffc486e45e | -2.94292 | -54.11271 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71216805-c3d6-35e6-b09d-6186912c2554 | -7.23293 | -55.11809 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a63a7ed8-4eb2-38dc-8781-e61f5b937616 | -2.50465 | -56.13936 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d17c4e4-0a33-31ba-a7ff-6f158ba7268a | -3.31494 | -54.04087 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3cb9b8a3-fa3e-391b-a52e-5da3472ba850 | -2.41162 | -55.86938 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 673b9be9-53a4-34f8-b113-8db1e6a6cef1 | -3.28965 | -54.04097 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62c1741c-96ae-3cf2-a60d-1c55a18f8eba | -4.56584 | -54.95544 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a127a8a-4ced-337e-bbc0-cbb86f475f68 | -2.99466 | -54.06112 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b0cfdbd-5495-310c-b9f6-c006251f82ef | -2.76624 | -54.0942 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9bc828a-efd8-32cb-a27e-8472089dc197 | -3.5372 | -54.64031 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c6855b2-738c-35ce-94ae-c3873000cbab | -4.14146 | -54.03136 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5d261e6-8ac7-340e-9f5e-d98970b4e0ba | -9.14051 | -65.30154 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be9b7b03-9f00-3bee-a55a-9bda5d14a522 | -3.01892 | -54.1362 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d27c192-bf0a-3cd4-a94a-ccd9a05b53c6 | -3.07973 | -54.27815 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e40b4193-b287-373c-ad48-a7a0f3f8efef | -6.5125 | -55.39891 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d6054b9-b506-3272-ab8a-9851ffc9c0ca | -2.98644 | -54.06778 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9a4cc28-ea37-320a-98b4-54d5fb6719b3 | -4.50735 | -54.99192 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93655e36-395a-3ba8-a79b-d8d94e5df4f4 | -3.31578 | -54.05585 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2da9ccff-39c1-39a4-b6c1-0ba9de20be69 | -2.57851 | -56.1614 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3ca1df6-fbdb-31b3-aa8f-9cf403c42c43 | -3.58671 | -54.67805 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f31357e2-9c2d-344d-b534-f51933bd7d40 | -2.87997 | -54.0792 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c745a1e-e256-3b40-ae6a-a1bfbdad5cd5 | -2.96135 | -54.15492 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c030bf97-1c52-360e-93e2-f6b97512b388 | -3.04874 | -53.92141 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8366792b-2571-3691-bf7d-0ab41bf36890 | -3.03229 | -53.91078 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9778a72-8e02-38f0-8677-c61eeae17727 | -2.56466 | -56.16277 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6c8e671-5031-30a1-85d8-e9ee897647f2 | -2.4657 | -56.06239 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a0688f0-9031-377e-8f8d-968198b2e4ce | -3.2878 | -54.05272 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12f50abc-4125-341f-b4e3-0c6c39e5fdd3 | -3.85395 | -52.03263 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f40de36-6a2d-331f-a464-7cc49052a17f | -2.88577 | -59.20095 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 322c92a7-ea22-3ca9-a55d-5ef0f74efcbb | -3.64084 | -55.49314 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb0ebc7-d774-3da8-a59e-f8f58ed7ef30 | -3.30313 | -54.04704 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6ace118-8ccc-398e-ae76-31191443d43a | -3.50336 | -54.60825 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2d33cc2-2064-3f30-baa9-700f0f83d905 | -3.92978 | -54.57948 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9690a41e-929d-3ae8-bdd5-27b7b1c8cc4a | -4.51839 | -54.89828 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdd34230-3dae-381c-a0db-3ede9bf6a68a | -3.20008 | -50.56029 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a163537a-2cc9-3b84-8851-e5743328e154 | -3.03931 | -54.25714 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cc802e6-eb98-37aa-8546-aabfedf672ae | -3.95382 | -56.11091 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62cafed8-0c4e-369b-a240-6cfa5361df7c | -3.58866 | -54.57479 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38758dca-3001-33ce-b430-01943a8b663f | -4.11068 | -54.01852 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd9f252b-c971-37cb-876d-7ac534e4177c | -3.68946 | -57.01016 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 738d2be6-aee3-3109-8cd6-e11657498a8b | -2.46727 | -58.08382 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1919d0c-0443-3208-9857-2f552753fe63 | -7.21616 | -55.08749 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2184ea00-64fb-35b7-ab49-764ca6dc0e0b | -3.28813 | -54.00462 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e32dfbbb-bc45-3795-b0b1-c3be3c124c42 | -3.0445 | -54.15596 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 458dad87-01cd-3866-a70d-05aef7ce839a | -1.47639 | -54.53941 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 054fd58a-67b4-3d8d-b0fa-a7d9b4466d8b | -6.09753 | -53.49845 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 545a1c91-1162-34d8-a621-192f3a7ba02a | -7.18271 | -52.6165 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffa0c5dd-5e4e-3521-ab92-7c7e3be67a4d | -3.32425 | -50.18232 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d4297fee-b7be-3a6d-a5b9-1f597b9a25a9 | -2.65224 | -56.55233 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee45fcb7-1568-3daa-8521-30e3103c4eac | -2.77086 | -54.11067 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d80b960e-5c72-318f-9771-92c9b3a548e2 | -3.25825 | -57.04152 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01718340-657d-32fd-9da9-cc6821d1eb12 | -6.14714 | -47.93088 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e2c54b19-80dc-3e87-b219-2427b8cf444a | -2.84892 | -59.11383 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fc66573-91ec-3fb2-9ec6-4328a2088c6e | -9.05787 | -65.48524 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67cda2f1-a1d1-3cbc-b6ec-0f43e7323df1 | -3.32411 | -58.22872 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf48a82-2ee4-3f96-b6a6-ba6ba801fa5c | -3.21835 | -53.96645 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce4d7f3f-cb77-3f12-a0fe-87264185f555 | -3.05289 | -53.91803 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd0817c-7a87-3a45-b1ad-b8375c28e094 | -4.29965 | -50.78025 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703e111f-2099-3b6e-a0d1-9a334dd81609 | -3.2102 | -53.88035 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 079abc86-6bcd-3334-801b-55934db6d8b5 | -3.27138 | -51.06527 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7a9c148-46f9-3f99-96c6-4d66b492e3eb | -2.65964 | -54.31269 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa8fc65d-e488-3c17-a25d-f4fd2f2ac74b | -3.10775 | -53.77617 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56d39c86-8aa1-395f-90d5-9199d7475da4 | -3.25977 | -54.02431 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| fcce6c52-91aa-3b38-b4b5-79ba7ffb115d | -3.72093 | -54.23184 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b9b1376-5d6d-3d2a-aacc-48f766d2a789 | -3.17265 | -50.44368 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 111bb2be-72a4-3bc6-991d-cfdef9861e88 | -9.54353 | -64.81759 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3700eb-c05f-3a7d-a5a6-1a0c69add9e0 | -6.33078 | -55.71459 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cb2ae95-2250-33e8-9db2-23d7bb561ecd | -6.44766 | -59.9488 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c524684b-0f77-334a-9287-e65a10253f62 | -6.14796 | -52.64763 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3441be4f-fab3-38b2-9e4b-735514752897 | -2.78433 | -54.09307 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d5b350d-60bc-3223-9ea4-9ffeff9b015c | -3.10506 | -54.18393 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b3096f31-ad9b-375c-93b8-9b1d22d74fe3 | -2.87612 | -54.19676 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9294a174-c85f-35d5-8fc4-9a8c453eeacb | -6.93329 | -43.67193 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1da21834-cf00-3bca-b5f6-256aeb4089d3 | -3.73708 | -54.65489 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3856a102-8110-3454-80c4-594e671b1a31 | -2.76525 | -54.09491 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b27e8b97-fb4b-3921-bcbe-2f112c777118 | -3.58384 | -55.60421 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab5e72e4-0f43-32df-9fb5-95a2cdffbd0e | -2.50356 | -56.14628 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f36329e-4208-34ce-8275-824144307414 | -2.97968 | -54.03908 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 421da4ef-22bb-38d0-b4a3-c1b1b14ff6e8 | -3.06446 | -59.27639 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 269cdb56-219d-30d3-8025-3755ec982d6c | -2.51427 | -56.25063 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| debe8a31-3cac-3f72-9c02-8b099a457ad5 | -6.09005 | -53.49729 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README170.md)
