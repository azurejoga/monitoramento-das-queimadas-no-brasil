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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71c1b9b9-c0ea-3c01-9677-e4d85a28edb2 | -9.27666 | -49.6335 | 2025-07-18 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c3cedfa-97b9-37b5-9171-b4f3f654f606 | -10.61761 | -48.07467 | 2025-07-18 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b11c8e5-f7de-3c06-97c8-ccb863be6946 | -13.61719 | -47.92508 | 2025-07-18 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cce0c338-19f3-31c0-8c1c-44e9e980b8c4 | -10.89909 | -49.20778 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbdeaa57-54d0-36bb-9042-945ca1c05e9b | -14.15466 | -51.02858 | 2025-07-18 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 886326a9-43f2-3756-9ab9-25f36e26d4b5 | -11.57007 | -47.09663 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6faa9d6-4ad8-324f-bf53-bfa31ce49f4a | -14.27831 | -50.50472 | 2025-07-18 04:27:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 661ee99c-5560-32ba-8d0b-b1439a6ef533 | -12.4263 | -50.03672 | 2025-07-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25aa2663-9080-3aba-94ff-fba699412c69 | -11.85473 | -46.74946 | 2025-07-18 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d31edd7-00c1-32ac-9e02-5bd06e34d44d | -12.7084 | -46.81035 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ade7f562-5b06-399e-a4c4-96859264a780 | -9.43485 | -48.85534 | 2025-07-18 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca526a2b-2b1a-3d3d-ba9d-3405cf486646 | -12.58026 | -56.97165 | 2025-07-18 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dde3953c-9fb9-328c-bcd3-5ed976bfc2b7 | -12.48468 | -46.9181 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7630a29d-7984-327b-9099-240e9688de50 | -11.738 | -48.19649 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| dce2fbc3-372b-3376-8e0e-3446d0988bde | -11.85697 | -46.75708 | 2025-07-18 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d420cd86-e8ee-3c6f-9a34-c28f08cdc925 | -10.8193 | -49.2901 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a4760ef6-ad76-3513-8169-98f8a376d741 | -11.56176 | -47.08447 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c18b5d25-208c-3e4d-854d-b55eb45a85ef | -11.46169 | -48.1584 | 2025-07-18 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83eb5aab-a448-3b7f-82a9-34544968f06e | -14.72202 | -45.1042 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12f58c2d-8561-3d89-8cdd-2848f70b6764 | -8.86849 | -49.03543 | 2025-07-18 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30ff4c5-8036-39ee-a523-abac88f6c4de | -10.72049 | -49.4859 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9443cf5-4e4a-3ae1-869f-8996c18f0318 | -8.25302 | -46.07998 | 2025-07-18 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34181997-a376-394f-a179-eb005f0d9dc2 | -12.98627 | -46.92448 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33662734-97b4-34db-83e8-49a1bd768b44 | -10.88208 | -49.55197 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8112d0f4-04a0-3566-ace5-bc0dc8c0ddd4 | -14.70746 | -46.19254 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9357225d-2ad3-3bda-8899-605ea0f186ea | -9.05213 | -49.29124 | 2025-07-18 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2eda114-33d7-3b34-be6b-e6a7094ddab1 | -9.80346 | -47.73756 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba48f8c0-a7a1-3c5e-9277-0df07ba2c78c | -10.06497 | -46.67386 | 2025-07-18 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402e0066-ee5b-3cab-ae0e-7a5c484b4d75 | -11.32875 | -51.44024 | 2025-07-18 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b45e639-fdf2-3c32-8499-b2e3ade744ba | -8.03975 | -46.62077 | 2025-07-18 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33d0e537-61a0-33b6-836a-f965e8156c4c | -10.72111 | -49.4821 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 00aacfc2-e7e8-3c37-9f0d-e05690bca2a9 | -12.70895 | -46.80676 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77545ddd-7217-32ad-862c-5d403cc899d1 | -14.71957 | -45.06867 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0279a537-eede-3f89-8e3c-3975c9647458 | -8.88867 | -44.79322 | 2025-07-18 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4aea5da6-cdfe-39eb-8650-6e6733d188bf | -14.71686 | -45.10542 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03b3a26e-985a-3983-ac3f-fe67b398ab7e | -10.93374 | -48.88564 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ea3ec1-c281-3510-adda-107e10021d70 | -12.03231 | -48.7624 | 2025-07-18 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e16d7043-ed5e-3cba-b790-00942fd3fec7 | -10.54737 | -46.2527 | 2025-07-18 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 667d3027-ec51-3e47-9c87-f446d2e76ead | -13.07446 | -49.24634 | 2025-07-18 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bf00042-9a77-3870-94ee-69bdb169a54b | -11.74323 | -48.52782 | 2025-07-18 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 143742c2-fd51-3f3d-8473-63e3a3c2f3a0 | -15.63868 | -41.25825 | 2025-07-18 04:27:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a64bdf05-dfd7-387c-a9d1-255c9117b815 | -13.6205 | -47.92561 | 2025-07-18 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e05ce8-609f-36ff-b2f3-21e6234a2847 | -14.71203 | -46.18536 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbec98d7-deb8-35bb-b44c-f219b29caed9 | -11.74656 | -48.52837 | 2025-07-18 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ada550f-f4d2-31f5-9615-2333094a8800 | -12.99943 | -44.86225 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d7d908b-815d-31e0-8ea9-5c1bb6b33e74 | -14.71317 | -46.1776 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a822cb01-6141-3b5c-83fa-36d11b316077 | -14.30896 | -53.33641 | 2025-07-18 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e054b4-b16f-343f-b775-0be3192ad970 | -10.38252 | -49.90385 | 2025-07-18 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dd0e78c-6d8e-3f4e-805c-5a5444abc4db | -10.50867 | -43.92212 | 2025-07-18 04:27:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5effe285-bd28-3726-bd1d-a7ccab8137d0 | -8.36712 | -46.90015 | 2025-07-18 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422479b4-28d1-3f86-8d97-c14f055fb1e0 | -8.88222 | -50.15652 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| faf19e24-4b3b-3ab3-970f-d74d5945c3d7 | -15.1857 | -43.53721 | 2025-07-18 04:27:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3339fe3b-6c37-3ea4-bb2d-f565f70596c4 | -9.76668 | -48.7586 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 952531f9-41b6-359b-bf52-56f372481749 | -14.7785 | -48.30463 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 820b1435-8368-3f3e-85ae-ec7cd0b7623f | -8.88581 | -50.15713 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90882ecd-5473-366e-badd-dc1439703b44 | -12.47802 | -46.91704 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 658dce3c-b450-3614-aa97-40115ccf620f | -11.73856 | -48.19297 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| ec38ae59-4c3d-36dc-b8ea-b42bdb70342d | -8.6479 | -47.75209 | 2025-07-18 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7427d438-c1f1-3403-b618-549ab6b3ad91 | -13.3067 | -44.18177 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85aa7466-9871-3549-af80-2b3c33932a5c | -14.73646 | -45.08001 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d4fc35-f458-3c5e-89ce-b64c25c56889 | -14.01492 | -51.20918 | 2025-07-18 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 625374ee-6596-3e78-b559-ce543066eea6 | -11.94178 | -46.35077 | 2025-07-18 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19d8f63c-a311-3c7f-b6e1-6303ef48cf92 | -8.8829 | -50.15234 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 85e9f62b-c07e-3efa-8fab-f395c05f90fb | -11.78364 | -45.21852 | 2025-07-18 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20b6c39e-e4de-340b-8cf1-7470d71c4868 | -12.10128 | -45.84324 | 2025-07-18 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ad269c9-71d2-3f85-9378-b3404bb37fc6 | -9.1615 | -49.67196 | 2025-07-18 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0063c445-859e-3fe2-9131-15fb8aec03e7 | -13.5426 | -43.71037 | 2025-07-18 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eeac20b-a0c9-385b-8ef8-57321a0203ed | -14.15113 | -51.02798 | 2025-07-18 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10e5ef19-7e0b-31bc-aeee-14d41c7e6155 | -14.7178 | -45.10801 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d5276f5-00ba-31bb-9149-a05aacad882d | -8.04343 | -50.07365 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbb516f1-2046-3074-97c7-3ca2daea5694 | -10.35651 | -48.26107 | 2025-07-18 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 627db441-00b2-3dea-90e9-0abfe4d60b30 | -12.57442 | -44.75249 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16a11829-7fa4-3cbf-aa47-acbddf804252 | -9.85342 | -48.0664 | 2025-07-18 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b78e0135-db9f-32c2-9e49-900cacd213e1 | -10.841 | -48.33982 | 2025-07-18 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8c68629-4658-36ff-88eb-3a1e624cbbc7 | -14.72022 | -45.11717 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b57efd0c-0e12-3e16-ab43-5ea454e4a389 | -11.36089 | -48.7034 | 2025-07-18 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a7ec208-ae6d-3b5d-aefe-80276ed065ec | -11.56617 | -47.07795 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e58274d8-71ec-34d0-876f-9a5b18232c6b | -12.57503 | -44.7483 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8213b005-b346-344d-8878-e720231c99cd | -12.71174 | -46.81089 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f120b0c-1965-375e-9e06-25c78c596961 | -9.77066 | -48.75543 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f81cb2c5-487a-317b-bd3e-c101d8be38d4 | -10.6623 | -49.36831 | 2025-07-18 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78ad2980-8b86-3c38-b49c-9157b13ebfc0 | -14.74823 | -46.29768 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95489c54-7a8c-3517-8c1e-87056722af3c | -8.38374 | -44.03549 | 2025-07-18 04:27:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d591e272-ec2e-310e-b4b8-f280f771e48d | -9.86458 | -44.70922 | 2025-07-18 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 594ac52c-567f-3848-8e3c-228ecff65370 | -13.00363 | -44.85855 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac155b2-d018-367b-ab9d-0eae446d266d | -10.68219 | -56.54636 | 2025-07-18 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5b36bd2-b65d-39ec-8ae2-7fcd2b6a7290 | -9.76728 | -48.7549 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3420a6f4-88fc-310b-b412-9cdfc288fe98 | -12.70857 | -49.94135 | 2025-07-18 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560ec47a-6113-3c8e-a99d-5f9c77302422 | -8.03645 | -46.62025 | 2025-07-18 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0add511a-643e-34ce-9077-aa8e2982d08a | -14.70689 | -46.19639 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d6da0af-db55-3157-aab8-59ee3d86fe61 | -14.72563 | -45.10472 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d9865c4-790a-39a5-99aa-2435cc25eb8e | -10.05778 | -59.10091 | 2025-07-18 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b2ae9f8-b824-32f9-a830-2b142a4ce8e6 | -15.41076 | -41.99726 | 2025-07-18 04:27:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4024e429-4515-37ec-86de-a525fc7b12d4 | -10.93769 | -48.88255 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 981885aa-6fca-3146-8570-b786b17af3f8 | -10.71424 | -49.481 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a6b25361-466b-315f-bfb4-eb61e826b9c1 | -14.20632 | -45.33472 | 2025-07-18 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d65f6ce-7d6a-35c6-8441-1eac4dafdd8b | -8.87571 | -50.15114 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ca6412-082e-3012-bf2a-2722a214cb40 | -10.76693 | -49.59133 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e37dac74-e6c8-3dff-b1ec-94e0303da0fd | -12.57964 | -56.97486 | 2025-07-18 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d39d2ef8-c1d9-35e9-8905-706d67516e83 | -9.04867 | -49.29068 | 2025-07-18 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
