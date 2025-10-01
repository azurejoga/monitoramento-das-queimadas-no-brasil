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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 441fc453-3544-3fb5-85e8-6c783b3c9ac0 | -12.78693 | -46.86417 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd59eca9-2b1d-37ae-a41e-23cbabbb5929 | -14.79726 | -45.79513 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e166ea46-ad7c-3bdc-a336-6315b68a303a | -11.8126 | -44.99531 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a4275e1-af20-39ef-b4ec-41c39f7efac1 | -9.42303 | -54.71104 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95e960f1-75c5-3921-b27d-4653505d9cc3 | -12.93673 | -47.18453 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38df261c-4cc9-38cc-845f-4216691dc4e5 | -11.85308 | -44.99806 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f0b6dc51-06d5-32a5-a6a9-c1dbf2c8d529 | -12.8773 | -46.91523 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c5b7000-eb70-3bc0-b481-32b86d5b3966 | -15.36092 | -46.11 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dca3010-02c9-3414-a4d4-9ad14b6b493f | -11.83028 | -44.96889 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f63891b7-9975-3db6-add6-33cef187a229 | -10.96117 | -46.54914 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 234a257f-4842-3c0d-9256-aeb35193b3b3 | -10.44759 | -48.081 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f991343-c3eb-3cdb-9e7c-6a0f06b3a48d | -13.28109 | -47.22342 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9787642e-6cdb-3ef1-b3d3-d33d2685c3ce | -15.40446 | -47.05601 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ffda23-10e7-3b79-ac2e-ab835675dca3 | -11.38248 | -45.07338 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a30a7b36-7522-3d50-8a25-f6f6d2e1fa7a | -13.7742 | -47.96837 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2f513861-b061-3e2e-b762-006545d3d0f6 | -12.37335 | -47.17241 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56d7cb56-e741-38a0-888e-859f9442134d | -14.54036 | -41.66527 | 2025-10-01 04:21:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 31093179-1c31-3a12-9cc1-7676fa52a926 | -12.8817 | -45.27341 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4f36cf7-b290-3c8f-bc38-5407b6040687 | -16.4109 | -47.05999 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ee39f7-137d-3472-83ed-cbc33a200bb4 | -12.85179 | -46.94755 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18c32b8c-2f4b-3b54-8443-a3caeae814b5 | -13.80638 | -47.87606 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d3e8960-8d21-39be-be4c-11ac66ddfb7a | -13.24017 | -47.33079 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 554375c6-2511-3fca-bbb6-72f510ba5b8d | -16.028 | -50.89099 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd1d4ab2-2453-3dcc-83be-a4666d2d56c3 | -9.88196 | -47.71461 | 2025-10-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e25e93e-8616-3259-8bba-e642b9433bb0 | -12.84733 | -46.95423 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4075f500-d3fc-3b7b-8919-4a5783af8a7a | -15.59715 | -44.41099 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0bdd2c1e-5a3e-32c1-a752-989d8a4832db | -14.68548 | -48.24788 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131cee9b-d83a-38a2-bff0-167246b8603c | -16.01669 | -50.88025 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ac51144-af24-3583-bf0a-3572fd935d9c | -12.24654 | -47.80897 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ff9babc7-7eab-3a6f-83eb-27d36a83cf04 | -13.37668 | -47.30582 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9bdfc21-7fbb-34d8-83ab-c8e9eba3e90d | -14.61164 | -45.01801 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4735175-ecf9-368e-ae12-c4d0357f4c73 | -10.65727 | -48.52662 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef3905c1-bf6e-31a9-b223-f78f1c9ebfdd | -14.39638 | -46.21266 | 2025-10-01 04:21:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dca0507-f8f3-3886-ac57-2b93ae19117b | -10.90821 | -46.51884 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1936ae64-e465-3d65-99a0-366a4f91ed54 | -14.90392 | -48.37249 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a55bed0-91c0-3a3d-8167-aaae69f97bb7 | -10.90877 | -46.51533 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 128801fa-6a7e-32fe-b900-54f691824fa2 | -16.37783 | -47.07645 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f4c5c3be-f2ab-33fd-ae7d-d4ea474d71c5 | -13.14069 | -47.41772 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7490aec-128a-3769-a83f-1fd6c6b1c169 | -11.52207 | -43.54887 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdb92f51-0213-3f3e-9eb2-a2045a91fab5 | -15.18216 | -46.41039 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c939ba-75e0-34a7-a752-b2d03be4224b | -14.36301 | -47.14108 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69d2d6d1-7792-3738-8f44-b9ceb6ac5820 | -10.03581 | -52.10547 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3664181-0101-3ffd-b1ca-d77f9bcdcd62 | -13.07769 | -47.06909 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6879673-0b48-33c4-9bc0-a4a6133992c3 | -16.3757 | -47.04676 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 800579f6-619e-371b-be77-06a2ed072237 | -13.32985 | -47.87107 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04e893dc-3220-3489-98d2-a7cf750b53a4 | -17.51204 | -43.48732 | 2025-10-01 04:21:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1812dc5e-4639-36e5-88a0-63e62f03a86d | -13.73694 | -48.81973 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7d498651-383a-39b6-a3fa-172f2273c75f | -14.79518 | -45.78717 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 317309ba-6a5b-30d3-8090-e2c4faba4f56 | -9.99191 | -48.35404 | 2025-10-01 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa70f5ea-05c1-3797-8053-92719f725274 | -15.76163 | -43.73742 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17095502-135c-39ec-bdab-8b5defc2c2aa | -13.33555 | -47.81475 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67e1dd86-bf16-329a-9c85-9623051feec0 | -10.47903 | -55.61853 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 182474c0-3c31-38b9-be2b-145511a71cbc | -14.04311 | -47.96482 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c37f202b-4a7f-38db-a35a-ad7f3a944efd | -14.96385 | -46.87331 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf052abd-7d89-341f-912a-b21866ccefaf | -11.84141 | -44.98523 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd3f3bed-fbde-31ac-951c-4b1e3132ef2d | -14.21102 | -44.92907 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957a77aa-023e-3a15-8fe4-14509e42a7b0 | -11.50299 | -43.51007 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 065cc654-10d9-3678-9645-5fb8c67945e3 | -14.67273 | -48.1354 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d0d534-e6cc-31ea-a538-ed8becd4e81d | -12.84039 | -47.0407 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f56a25-0685-3bc0-b665-95bb59671ab4 | -15.99377 | -51.19065 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 325d439b-5ede-38ea-9189-5f21d83ac018 | -13.96649 | -44.9031 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c51fd9b2-706c-3a5c-b4fa-6663cf6eb564 | -15.77057 | -43.69959 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae75724-7b65-33ab-972f-c558f1f468c2 | -13.66795 | -48.08041 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58e079b1-30d2-349c-9494-0ff4cf7964ee | -15.35671 | -47.07675 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ff499dd-2a27-3330-be83-2a3412972b65 | -10.84738 | -45.41249 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaabdd77-7d69-3fba-8621-b547240b0e9a | -11.57011 | -50.18183 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68b964de-51be-33a7-9048-2831b0507809 | -14.68155 | -46.95736 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84ea83e4-66bd-3f28-a983-387fe22fe5fd | -11.95905 | -46.58991 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d4b5986-e7f9-3c05-aa15-3492affd6d67 | -12.94263 | -48.41224 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e485be4-62d8-315f-9841-d6945576e389 | -14.71406 | -48.15742 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb230610-ef52-3f6e-9676-80efba9999c5 | -17.39151 | -47.16209 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 507ec548-6bf5-3ebf-929b-4aca503ceb3b | -12.24376 | -47.80466 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 79fb4bbb-e9c3-39fc-9197-c833ea6c7a2b | -11.86986 | -48.02777 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a19b710-6011-3f31-b5cd-1a45433b7a65 | -14.68456 | -48.23234 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b9c0266-92d2-375c-8b6a-88da2c0610d1 | -10.84132 | -45.40793 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a1fe4fa-ddc4-390e-a0a9-7808da49d8da | -11.39978 | -44.89403 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85db8f00-5a15-3361-a3c7-72c8af358483 | -13.10326 | -47.03688 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07346a8a-2158-3700-be4c-f4caf1cc3d16 | -12.87699 | -46.94046 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4233dbfb-085e-3352-b2c8-fc02b7d30d49 | -14.76416 | -45.76739 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be86b4e5-d04c-356d-af33-969f4b6c1630 | -11.80226 | -46.61143 | 2025-10-01 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0cd35a2-c9de-375c-b910-4d1047caf11e | -11.93814 | -47.88841 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c300da14-6e64-3c26-8130-5afe8a9a284a | -15.32776 | -47.36875 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5ee3a11e-19b6-39bd-9d1a-befc41cc9572 | -13.22968 | -48.44018 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba0d6c51-2268-3d0b-ba03-a42521e4d65b | -10.1897 | -52.55179 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf3acb5b-00de-3802-adba-6279014de93e | -12.78023 | -46.88486 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5c2e069-07c2-31e3-be29-62d3c5c81eae | -10.90933 | -46.51181 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2784a55d-90b2-3113-a13a-688a73ed1ae4 | -11.82077 | -44.94181 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5d75ed1-0bff-34ee-b385-f77c9c945228 | -13.3671 | -47.91866 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79db3cd8-e378-31f9-aa14-01a0afe7468a | -11.81478 | -44.98107 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 118c0a6b-6c40-3260-a0f5-c37810eb6351 | -14.7319 | -46.8311 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6d59d1ef-c6b1-3959-9f85-2f1d15fa092b | -16.93951 | -48.97832 | 2025-10-01 04:21:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a5b51c3-d112-38a5-93af-499dd169da43 | -15.3381 | -47.93956 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce670c40-4b41-347b-9ce6-436fdeebf110 | -10.98077 | -46.53422 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ecbfb4c-aef2-360d-a2b4-ec260dbef13f | -11.45213 | -45.0187 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a61c525-1f9f-3a18-b5eb-580c2e64043b | -12.78528 | -46.85314 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2751906b-a014-39c1-9f37-4bae85fab52b | -14.05738 | -45.02281 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37176774-6621-3e63-b3dc-e39c5d38541b | -15.5416 | -42.66239 | 2025-10-01 04:21:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0d746027-aa43-3420-8ae7-c376494ce7b0 | -15.2954 | -46.40329 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa56731c-22a3-3914-bb3c-b531a9e92ed1 | -14.02914 | -53.88075 | 2025-10-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c395709-5a77-3a9a-b006-664b750cb0a6 | -14.03554 | -47.99002 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README49.md)
