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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1783f2a1-f603-34f0-8fd2-2e5dee2abf2b | -12.4173 | -46.81369 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f4359340-60e4-338b-a3d3-70eec95a9f70 | -13.42957 | -46.93302 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 119cb046-4058-3b38-8a47-4c53211421de | -12.76037 | -48.14677 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbd9b877-2f7c-3a84-9cd3-8529f82bec59 | -16.40295 | -49.48397 | 2025-08-26 04:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db9dbec1-a7d1-3bac-9b1e-857d18333f67 | -12.42122 | -46.81067 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 37e6e8b3-bd50-384f-b61d-154877fdf834 | -13.61139 | -48.15498 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12e5b5df-0ae3-3e3c-b8c1-0df2b256bcad | -13.45145 | -47.01027 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb5038c-1346-3c43-9d82-8b8a947d5fee | -13.5078 | -46.88709 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 503575ed-eb03-3a5f-a20d-114026590301 | -12.7576 | -48.09866 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dea205a-ced1-342e-a0e9-0193e9a1820a | -12.4131 | -46.49783 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89f6ab38-7258-36ed-a3eb-34c9847c0fc2 | -14.24885 | -48.04 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d2527817-2d2a-39ff-a06c-df96061e228a | -15.02099 | -48.5056 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05d257f7-97ad-3639-b90d-8502bef81f5a | -15.1616 | -48.31063 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00f48c4a-f9f1-35e3-a116-3f6b8efd717e | -12.76328 | -48.10722 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2450e076-a24c-354c-abb8-0285a5256050 | -15.02443 | -48.50618 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77750f49-9fee-3b3d-984a-a4a2904e2852 | -15.13489 | -48.68404 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7532516-f819-3166-9282-1c281da62e4d | -16.41186 | -49.6464 | 2025-08-26 04:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb0af3e1-a434-3def-ae51-542b2c4fb1c3 | -9.19248 | -59.53819 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ceb1603b-d8ca-3d52-b4f2-5ca4b2da5e92 | -12.70615 | -47.87512 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1227ceb0-544e-3373-b0a7-57879fb29c58 | -11.63519 | -46.41 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6626f8a1-2115-357e-bc9a-23805da3367b | -15.10102 | -48.73781 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bee4692c-5c70-3241-bcaf-c36bb66e2af2 | -11.55049 | -52.14132 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebf50d9d-807f-3dc6-b2af-b98c91bb0587 | -11.30773 | -55.11906 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ac69354d-c1be-3368-9b7c-c10601ec3193 | -11.303 | -55.11456 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 665adce0-8b6a-3e5d-9650-a798044c1338 | -11.64008 | -44.85914 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caf3df3e-8718-3bd0-9e8d-83a4cf7f3ccc | -11.54411 | -52.12658 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8299b8a0-8458-3ec0-8634-806b787f1db7 | -11.56477 | -52.11271 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5820029c-ee85-3ff9-9017-bdea8ced5616 | -11.54724 | -52.10947 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95cb226-31ed-31eb-bb45-771861c0155f | -11.62226 | -46.21901 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 820468ea-caab-3dcb-b28f-f5b2a57075aa | -14.27901 | -49.13628 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6de429b-3da0-3e6b-b565-390f219ac180 | -17.75147 | -41.51955 | 2025-08-26 04:23:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1fe36fe3-bec0-3da4-b992-883e15718657 | -13.62531 | -48.14856 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58b2dee4-17b5-32b6-81a8-ff00556f910d | -9.1867 | -59.52948 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5e912301-2cad-32c0-be20-f672b89c1dd0 | -16.74131 | -47.60113 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efc7d033-d790-3c5a-b833-d48016e1b156 | -11.55366 | -52.12394 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fadbb91d-56c9-3984-9f0c-8cc60828b903 | -15.05311 | -48.70526 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6c1fcff-5be4-395c-8715-c42d862fdf2d | -15.62664 | -52.72365 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a3194bf-c8d8-36f4-9f46-a9304dc6e730 | -12.74058 | -48.15895 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa168825-52f7-3d14-98fa-5a31fb4a1b67 | -12.7274 | -48.15265 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e9dbc9-9068-36cc-92a9-977e19565f10 | -9.17851 | -59.45862 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a62fc93-cbe3-3393-b0e2-cdb2383d4807 | -12.76112 | -48.13007 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ba6e765-0bd1-3765-a067-648ea15cb6d2 | -11.30512 | -55.11245 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 774e6be7-fde0-3801-a2cf-cf27b6c1c3d5 | -13.62637 | -48.14972 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ba42af2-3975-3fe1-a638-f476032d48f9 | -15.06806 | -48.54146 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15cfa4e2-1475-31bd-90a1-cda9144b5ea9 | -14.84383 | -47.15091 | 2025-08-26 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a73411a-f76c-3435-8284-dca40b772e4a | -14.39961 | -51.94227 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ff517a2-c769-3143-89f3-3c7514caa768 | -12.73338 | -48.13795 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fde2c0d-ccd6-3d17-b698-a49253c867bf | -9.15897 | -59.55452 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2b730877-de19-3626-bdac-1e0362f9444e | -14.28967 | -60.36621 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feac3d92-f9a5-39d6-a62e-26dee3efbf03 | -9.16047 | -59.54713 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9a3da39c-764d-3f68-b7b4-6f356647fbc1 | -15.6429 | -52.73109 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37f7c35b-80e4-390b-9111-0b893925d72b | -13.4433 | -46.86903 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d482ff07-61c5-31a0-9779-b554f83e3e54 | -12.07707 | -46.63261 | 2025-08-26 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfe56e63-a728-3923-844e-affec24843aa | -13.4821 | -47.01196 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37def630-5358-3d80-9705-cfdbb60cb0f9 | -12.67648 | -47.86692 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f68fada-06ce-3a99-866d-5b58e133ab13 | -12.08041 | -46.63317 | 2025-08-26 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b0ba60-0b82-31a3-b558-a2870458abe4 | -12.09759 | -45.84412 | 2025-08-26 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccbbfc2a-bab2-3471-ae40-79010191184d | -11.62948 | -44.8611 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd9d583b-d5a1-3ace-bf30-2159c68411a4 | -15.02726 | -48.17197 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98f809dd-ed0e-3e43-bbdf-7cd4c5e91310 | -12.76047 | -48.13395 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 366e4ca2-fdf0-3314-b5f3-76cae7b92b25 | -15.02722 | -48.51064 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 008c4736-25ca-3c29-9264-42ed3e1f046d | -9.16259 | -59.46296 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e32d2acc-5a1a-32c6-8c46-36ccff187fac | -11.54715 | -50.45724 | 2025-08-26 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47ea2836-dc0d-398f-bacd-cf3a95003f8a | -13.42846 | -47.0251 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7807740c-fd99-30dc-bace-0a19df1ca1ac | -9.65235 | -59.6326 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f313501e-f80d-386f-91c9-1f7cc989fe58 | -10.64301 | -51.59213 | 2025-08-26 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0158b61-d4ee-34de-a7dc-7947f44f6d25 | -11.30235 | -55.11803 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 364d7c54-b286-347c-b9e2-fe8b13ecf83a | -12.37109 | -46.56762 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85768a86-feec-3bda-a5f4-5346249925f1 | -15.06131 | -48.69884 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be7f5ab6-d9d2-3cf9-886e-d1a568823336 | -12.67367 | -47.86256 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8130d20a-5090-3f95-ad00-255df98f7e60 | -11.53533 | -52.125 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bf39914-97ce-3873-9fb9-ccaa4e6d292f | -9.58381 | -55.37378 | 2025-08-26 04:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7537be1-b97e-3849-95c2-405575892948 | -15.02034 | -48.50949 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ecb911-0441-340e-9874-053f04af582f | -13.43995 | -46.86852 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73fc8ad7-6b75-34a8-ab2a-2f835809423c | -9.17702 | -59.4659 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c130763d-b6d6-3dfd-a68a-624d7caf43f6 | -15.0626 | -48.69117 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc0560ed-a47a-3ea5-95e9-3e6ad347c035 | -13.41188 | -46.91516 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6e2d855-67b0-3d1e-a8df-3ce2b9dadd7c | -12.77707 | -48.1409 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1ccf3c7-3a98-3020-b714-93b39fa3e7ea | -13.44721 | -46.86599 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1186b6d-8a1a-31e3-bd89-d3b83206a23a | -12.19999 | -47.21165 | 2025-08-26 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2249becd-ff1e-308c-9926-1237421f11bd | -13.61265 | -48.14726 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655a56a4-2d9c-3a51-8143-e25a1f716ef8 | -11.56117 | -52.10756 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08df7c38-eb42-3f03-9b36-e2a523dd5a84 | -13.43684 | -46.93051 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5420f530-ac3a-31d7-9e4e-ad2df1c7d2fc | -11.55882 | -52.12049 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b956b443-5815-349d-8cd2-33cad1c8232f | -12.78461 | -48.13831 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6526de6-d69b-3e9a-a30d-e273a7d925bb | -13.83706 | -46.69669 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ceaf3cb-f9aa-39f9-bd07-25a64ac14f30 | -12.72676 | -48.15652 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cee78ff-d29e-3d46-ba61-59297a49ec51 | -14.10922 | -53.98109 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad710d94-1634-3d4b-acff-9a4c2ff08f08 | -14.27193 | -49.13503 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6ec4210-1b43-3d92-8482-c848070b3a3d | -11.55129 | -52.13694 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bea25bda-b34c-3574-95c0-2868224f4d1f | -13.40808 | -46.89619 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 62207773-34d4-3fe9-b7a4-51e678d98fbc | -13.42154 | -46.87647 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e8e9aae-db24-3b29-8a43-99ffb2137c62 | -13.77393 | -42.7033 | 2025-08-26 04:23:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc1a3c9b-e529-31ee-a178-3c18a4f13a8d | -15.18373 | -48.19809 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de751ee6-ba10-3e1c-9017-bf19d3d9d51f | -13.4182 | -46.87592 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94fe3ae5-38c5-32a7-a580-d2a99947477d | -9.16198 | -59.53971 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ddb445f3-c346-3d97-b47e-e409ef89628e | -15.0788 | -48.65834 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 650bd196-fbbb-367a-a7ce-663908fe65e9 | -14.11871 | -53.98295 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 89827636-8c51-3cb0-9412-eafed027114e | -13.49334 | -46.87756 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01da1cec-c5f7-33a7-8e8f-f4702d8e6404 | -14.84717 | -47.15147 | 2025-08-26 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
