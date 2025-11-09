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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d1c9bc8-f7b6-3918-a0c6-2bd34ba7a6ba | -11.95102 | -46.24008 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec2cc276-e61b-3875-ad66-c27549cc6363 | -11.95517 | -46.24775 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57f7cc85-e38d-36eb-9d19-030b33d08747 | -9.75536 | -48.17514 | 2025-11-09 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e8607ad-a489-3a90-b7ec-5139bcf98e58 | -11.9503 | -46.24503 | 2025-11-09 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8e9b5da5-1e4c-3d29-a184-a392682e460c | -10.71395 | -47.73716 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb8f5341-653a-30fd-be21-6234e8828cd2 | -9.95802 | -48.58919 | 2025-11-09 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dd7a57a-6e13-33a4-822c-5a8ea1afcbad | -10.71749 | -47.73759 | 2025-11-09 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a8ae919-3cd7-352a-b985-c4acd2245545 | -19.78704 | -58.0484 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8f97d057-91f1-36c4-ab38-e6e5972e0f84 | -19.71655 | -58.10869 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 854fb1e5-9e7b-334f-8719-3490fa10f5a9 | -19.76533 | -58.11914 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4ae00d1a-7219-389e-a9b4-0880bef1dcb6 | -19.77085 | -58.04493 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 20013501-a684-3205-86b6-1fc5267040b3 | -19.75575 | -58.12507 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0392be0c-734a-3177-a964-b8fd29a0c226 | -19.73833 | -58.10538 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 92f5c1ac-082d-3c93-827f-a7ce54851306 | -19.76271 | -58.11061 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f929c383-b68d-3611-be2f-3f588b065d40 | -19.58548 | -51.08231 | 2025-11-09 04:42:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bfac6c7-669a-3a2f-bec0-9fe3b7ef7be7 | -19.72874 | -58.1113 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d6258f86-9a58-3f4e-9d87-5073111eb740 | -19.77895 | -58.04667 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0bb816f9-7c2a-380e-a69f-35999aed78ed | -18.19069 | -56.71187 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1ad527b0-754a-3092-908f-508655f06b77 | -19.75052 | -58.10799 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8b67162f-a49f-3526-8990-8e07b1e2f10d | -19.75792 | -58.11356 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c6af3127-6296-3650-a09f-55e7abb59536 | -19.75747 | -58.09357 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 018162c1-b570-3a49-9a62-353a9871140d | -19.74863 | -58.09565 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5bb41f78-0846-33fe-9dd1-ea8c73a875a8 | -19.7572 | -58.1174 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d340c1bd-9ae6-35c5-b99c-e9957baadd10 | -18.51002 | -55.52007 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a90839dc-ecdc-3076-b488-b5c56fd6d8e2 | -19.76225 | -58.09061 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 251857ce-976a-3c1d-b56f-ebffe46c421a | -19.76199 | -58.11444 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6f77bc4a-c6be-32fe-a99d-2b0ea0625f08 | -19.7553 | -58.10503 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 656889ed-f44c-3bb5-8fbf-67a50fc66f30 | -19.72467 | -58.11042 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2c23dd44-e602-386a-84f7-6a7cc182b248 | -20.64944 | -51.9865 | 2025-11-09 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6eb33fa2-52cc-3d99-b12b-b268fa4f651f | -18.50927 | -55.52441 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 906a8edb-ac8b-3eda-9de2-e2cf10b392cb | -20.254 | -58.15287 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 81f3840d-2a74-3cbe-862a-778ff841e7b3 | -19.73354 | -58.10833 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b81257da-36bd-3d64-b58a-eba00304806d | -19.76677 | -58.11148 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 87ffc4e9-631f-35ef-a6e7-7eac945c8444 | -19.73572 | -58.09686 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e0177329-fe61-3918-bd09-5707e0b590dc | -15.9665 | -58.23016 | 2025-11-09 04:42:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c737fe-dd93-3899-8028-d2c134dfcbfe | -19.76204 | -58.047 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 97ea9e68-4c71-36f1-b671-75874d8d92c3 | -19.75819 | -58.08975 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 92729978-7446-39a5-a6f7-91db47c296e7 | -19.75341 | -58.0927 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 53524385-1870-3c01-a62d-64ad27a78332 | -19.77083 | -58.11235 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3bcde1fa-4dde-3ae4-b5f1-0d165308b496 | -19.76276 | -58.04321 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| df7a061b-1142-3ded-8140-575ae4305cc2 | -19.76009 | -58.10209 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 13e3cc94-5f28-3832-b987-09ddd0774676 | -15.96734 | -58.22559 | 2025-11-09 04:42:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7143e3e0-2b0e-3769-b0c5-5cad9e1304ca | -19.75937 | -58.10591 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7408f106-ff0a-339f-acfb-13bc99049343 | -19.74834 | -58.11948 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8824cd4f-c329-3971-a86d-64d276a221a5 | -19.758 | -58.04613 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d296253e-b696-3601-8efb-bfad8e9ed377 | -19.76681 | -58.04407 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 510d2769-3ad8-307a-8379-9dbf19d9605f | -19.74935 | -58.09182 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 064e1cb2-96d2-3f61-a267-f1944c14a40d | -19.75982 | -58.12594 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4f10770e-e42e-3d11-b31f-90fbcbdea3db | -19.72614 | -58.10277 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c71daa70-2c5e-3b0b-883b-4346d1f2af30 | -15.9666 | -58.22873 | 2025-11-09 04:42:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b2d6e24-cbf7-3b52-a24f-73548c281b4b | -19.75458 | -58.10886 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a4717a8b-0e8e-3c74-af62-9dab8ace49e1 | -19.75313 | -58.11653 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7862252d-ae90-39c5-94fa-1476b801ae86 | -19.74355 | -58.12244 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 02f39ff5-3b6a-3bb5-8885-7a12e1e6e4b5 | -19.76054 | -58.1221 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cc5c7a27-13a4-3167-928a-e9511d3c921a | -19.74762 | -58.12332 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 97b44d0f-aa24-3907-9b33-9e6b2770b65d | -19.7646 | -58.12298 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 03c5d189-096b-3ed3-814f-797d91ed2d98 | -19.74457 | -58.09478 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 32b8fdd3-0738-325d-9f3d-fca86907fc25 | -19.72394 | -58.11426 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1b9977e2-0fc1-3d26-aec7-a39ae1d1c60e | -19.783 | -58.04753 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 72c706c3-756d-3bff-babd-ab9640271256 | -19.73093 | -58.09981 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8795f704-e822-3e6a-9ee2-3bcf74748367 | -19.75241 | -58.12036 | 2025-11-09 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c1b15c09-772c-36c6-b8fb-72700398c090 | -23.77843 | -52.14545 | 2025-11-09 04:44:00 | NOAA-20 | QUINTA DO SOL | PARANÁ | Brasil | 4121109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8c2f405-d051-38b2-8205-4d2dad8cf790 | -29.76854 | -56.02166 | 2025-11-09 04:46:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6fa67a7f-290a-3caf-9b9e-6b16cf23f149 | -29.7692 | -56.01764 | 2025-11-09 04:46:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| a1d2b0b2-5675-3cf1-9ded-1884f583fad2 | -3.3369 | -44.3806 | 2025-11-09 04:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 2bb730ff-4056-3dcf-a6e8-7d883e9142b2 | -10.3248 | -49.6341 | 2025-11-09 05:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| f05335e8-074b-3715-b7ab-294b17a96a88 | -3.3369 | -44.3806 | 2025-11-09 05:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| db0ee66e-edc8-3b5f-9cca-d9fe939198b6 | -10.3437 | -49.6321 | 2025-11-09 05:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f15c2946-76a3-38cf-b914-ff2d820da270 | -10.3437 | -49.6321 | 2025-11-09 05:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c980d67a-75e3-3d7d-9924-2affa47f2886 | -3.3369 | -44.3806 | 2025-11-09 05:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 747fd335-3e79-3ede-a19c-a52b84960a12 | -10.3248 | -49.6341 | 2025-11-09 05:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 06757df5-eda2-3160-93ef-53e17f1e92c9 | -10.3437 | -49.6321 | 2025-11-09 05:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e42a4221-ca77-30ed-887e-4037f51000bc | -4.472 | -44.6436 | 2025-11-09 05:20:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c8320409-1e16-3b48-97e1-f3a2e62ee587 | 0.13098 | -51.45064 | 2025-11-09 05:27:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9945b36d-2f44-392f-8cc7-8027ea4abbd4 | 1.92981 | -55.86917 | 2025-11-09 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40192ecc-4caa-3f8c-87a1-c108fecee6ec | 0.66243 | -51.54036 | 2025-11-09 05:27:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df26c098-208c-36db-be47-f2d9326513ce | 3.53058 | -51.77582 | 2025-11-09 05:27:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efd193f3-6296-3e82-978b-44f6f19d57e6 | 0.65722 | -51.54126 | 2025-11-09 05:27:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d6b8df7-dcbf-3f08-a081-0f80d75e6d11 | 0.66293 | -51.54354 | 2025-11-09 05:27:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd2159af-fbb6-31e1-aa74-487406bfe9f3 | 0.13218 | -51.4527 | 2025-11-09 05:27:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e5e6fd1-31e3-393e-85d3-0ca5d204e337 | 0.13167 | -51.44937 | 2025-11-09 05:27:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 163adf1c-5be7-33fb-baa8-56fd2b3d651c | -0.6414 | -52.36479 | 2025-11-09 05:27:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2a385bd-7f77-38c1-ae2a-ec885d9ee80b | 3.53328 | -51.77889 | 2025-11-09 05:27:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 287ed66d-6d4b-3699-8f5c-0c5eb5a47a0f | 0.65772 | -51.54441 | 2025-11-09 05:27:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf7983c2-d689-332d-aa4e-cd8e8042d3a0 | -6.00336 | -57.83247 | 2025-11-09 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adf0615f-ff98-3a39-adec-f30e05cf68aa | -4.26374 | -60.01181 | 2025-11-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee03b8e6-90ea-337f-9c5f-b20c9169bb47 | -3.25869 | -50.07554 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3beaaf5-851a-320a-87de-13309c199fdc | -3.79766 | -48.89953 | 2025-11-09 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f95de24-a30b-3204-8f0b-58db92319d8b | -3.46363 | -48.81843 | 2025-11-09 05:29:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a796855-8962-3e0d-8f9f-fdac015f3833 | -3.07477 | -49.37735 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf29b11c-bb8e-3b13-b839-b6a64fd2ad28 | -1.32128 | -55.84451 | 2025-11-09 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c03974f-8de6-3e06-9d2d-5cc34b48a528 | -5.12143 | -56.20449 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24527b1c-7cb4-3daf-8fec-ff397468e35c | -3.31813 | -50.10143 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2f3c1ac1-0065-3a9f-b3c5-fb14e3cfb8d5 | -1.65655 | -53.71536 | 2025-11-09 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5402ff2a-502e-3efc-8f57-57335be811a0 | -2.83537 | -50.4434 | 2025-11-09 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a9acab8-54a3-3328-935b-720289a90040 | -3.10022 | -49.26174 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f44a943e-9596-30ec-ac7e-233183e68636 | -4.29262 | -50.66309 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4d59f624-f991-34e1-b57f-cb567fc8f5e3 | -3.42725 | -52.89312 | 2025-11-09 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a0734a7-e37d-374a-8f18-8d2e11e741f0 | -3.7557 | -52.10304 | 2025-11-09 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfa34223-2fb9-3c51-8fb7-f45395c4d6da | -3.57375 | -52.25462 | 2025-11-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README33.md)
