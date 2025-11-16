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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cf00aa8-cca7-365a-abc3-394dd06efb86 | -12.0004 | -49.2683 | 2025-11-16 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| cf38c478-4242-3784-9ec2-fca3d289c7a3 | -4.7027 | -46.3176 | 2025-11-16 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 72462637-6666-333e-87de-2b129989a32f | -4.8119 | -41.6803 | 2025-11-16 00:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| a8783850-9dd7-35d6-8499-4f1638d5bad9 | -4.7029 | -46.2953 | 2025-11-16 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| cacd80a6-aae3-3577-91b1-a6f3e58c1bed | -12.6557 | -46.7407 | 2025-11-16 00:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 47694a7d-6b5f-3be6-8bb8-8102fb657b37 | -1.9886 | -47.3465 | 2025-11-16 00:10:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| dc2ea537-4b78-3ea7-bf66-b9d7db9e3584 | -2.5238 | -47.8115 | 2025-11-16 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 629849ae-7892-393e-abaf-261b69f011f9 | -4.8117 | -41.7043 | 2025-11-16 00:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 5bd0d1b6-a891-3e5b-92dd-3c3d2097b11a | -7.6331 | -38.9265 | 2025-11-16 00:10:00 | GOES-19 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 17149cbb-356e-3bd4-98df-1abfbd91c652 | -10.94651 | -48.69772 | 2025-11-16 00:11:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c5190dcf-3dc7-3949-8dc0-19d6f33d923e | -12.41421 | -48.60701 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2fcdc4ac-36c7-3a50-a138-5c0e006885f6 | -12.00509 | -49.29152 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6cc9183c-4d37-30c9-8717-bdf900f1b9e9 | -11.97092 | -44.9632 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f65de495-e469-3723-bd62-ee1adf78a2f6 | -11.81095 | -45.55249 | 2025-11-16 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 47490101-69d5-3a91-a374-a1372b3002a4 | -14.66779 | -46.54961 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bc98dba8-eb78-3ccc-9664-49164ebb9a23 | -13.81653 | -44.45662 | 2025-11-16 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 073ccd56-84ee-3592-b1a6-a043918b64c2 | -15.46369 | -39.24279 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| d8be3de7-02be-3716-8f06-0644d50b5f77 | -12.66374 | -46.74207 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ad68397c-c572-38b4-9b7d-786a4dfe06de | -10.66054 | -44.80234 | 2025-11-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5d746ea-46a9-39dd-84f8-3b97df1a10e7 | -11.90704 | -46.20232 | 2025-11-16 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 26e38dd1-5f11-3d7e-9cea-9b9786b44e0b | -11.96968 | -44.95401 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e7517a10-ffc0-3458-ba3a-fea3774ee486 | -13.58515 | -42.99311 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1ab0d4a4-bc80-3e21-8782-c2a87ada376b | -13.82593 | -43.1908 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0233499e-dade-3df4-a3f4-3d3fdcae7453 | -12.39987 | -47.56093 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 4da9e2af-2f46-341a-892f-f609c11a5db6 | -13.86884 | -46.84191 | 2025-11-16 00:11:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f5dcbdc-b452-3292-851e-89ff0e5ab2c0 | -13.75602 | -42.89852 | 2025-11-16 00:11:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 475a1455-f17c-3358-a19c-6be4dbfd41ca | -11.42274 | -43.13887 | 2025-11-16 00:11:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 27706ff0-fbdb-33ec-bfcb-bff4305a3cff | -10.50816 | -44.83642 | 2025-11-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| acec186c-50e0-309a-b7f1-f3c98f8a35e5 | -10.12213 | -43.9146 | 2025-11-16 00:11:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6dc8b9c5-70e6-3fcf-a3a1-a1d3749fd04a | -12.42342 | -43.18203 | 2025-11-16 00:11:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 71db584d-a852-371a-9cf9-f7f172fdb0a3 | -10.51702 | -44.83514 | 2025-11-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e7c6cde-f806-3da8-8653-c0b2e601aaf7 | -11.04927 | -45.16137 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6b78d891-9613-3ff0-9f64-3f5bebf03557 | -12.67802 | -47.1805 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 4a903571-821e-37c0-80c7-34e71a6e7f1d | -12.05512 | -48.21571 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ae7b31a5-ae66-3bc3-84fa-13b59fa320cc | -14.57947 | -45.21757 | 2025-11-16 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9ec51200-7417-32a2-9f20-8de129b2b7e9 | -10.54709 | -44.92244 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 740e2a19-5464-318d-bb1a-1cf321fb5604 | -10.16909 | -44.51109 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f197c9dc-ac67-358d-8ca9-12f520f5bf27 | -10.77373 | -44.49639 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 56477fd0-bc9d-3496-ac62-54c5f9e2c817 | -14.64272 | -46.58913 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9de3891d-d3e8-3cd3-b56f-7437b01030b7 | -12.20181 | -49.60424 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c0e4bf42-0a31-395f-8b2b-eab8cf576d8f | -12.85875 | -46.45134 | 2025-11-16 00:11:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 22a2964b-a55e-3b14-a642-0b403765ecb8 | -12.06739 | -48.22747 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| a0d77a67-3326-3e88-bd49-456b4f1427aa | -11.71295 | -48.86282 | 2025-11-16 00:11:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| a3250722-5432-33e7-bec1-811dd6169059 | -12.40138 | -47.57304 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c56cf925-aa7e-310a-92f2-76546fbb239b | -12.66511 | -47.15881 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ef9cd21d-b79e-3bb3-865b-f62bc41e0592 | -10.54022 | -44.1409 | 2025-11-16 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7f36bbb0-d52b-33b3-ae96-37d41b3480b6 | -13.39153 | -44.38145 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4190d541-61e1-3c2b-baef-dede2273341c | -10.63345 | -44.60509 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 92e75574-2d77-34f3-b61c-24e1529df96d | -11.71057 | -48.85394 | 2025-11-16 00:11:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5fbcf88c-1122-3b6d-8526-1c65c4649fb2 | -14.0642 | -43.12385 | 2025-11-16 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5bddf636-7855-37e1-ad70-732e4e392e2e | -12.86826 | -46.44977 | 2025-11-16 00:11:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a651ceb5-d6dc-34f0-9f90-1bd873d76b8c | -12.42471 | -43.1912 | 2025-11-16 00:11:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bd7819ea-a8b8-3a1a-8f3a-7d1c4022fc3e | -13.38141 | -44.37362 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc163b93-9275-30f1-b762-18276f345426 | -11.8456 | -47.60958 | 2025-11-16 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 213509bd-7cec-3ec1-a682-ba9278f9296f | -12.66658 | -47.17027 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| a6786327-5b2f-3822-a0da-6d5b0c425e59 | -10.16786 | -44.50216 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 10cf6240-2eeb-303d-a6a6-bbb112a79023 | -12.21946 | -49.55082 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8bb3fed5-274e-3e75-87a4-8e249964fc24 | -11.42229 | -43.33369 | 2025-11-16 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0daf8485-4cf8-3c46-a061-a56ae352f57e | -11.71257 | -48.40722 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ac7cd8cb-e563-3808-afe1-2c3ffa952571 | -11.03096 | -45.29446 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 51ea674b-10ee-305f-b0cc-41a0884721c4 | -16.34988 | -46.64393 | 2025-11-16 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4536440-8c49-3798-bec8-3bebf83d3a46 | -11.8441 | -47.59757 | 2025-11-16 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| dc949e8d-c131-3150-96a2-55f0ced40efc | -15.16938 | -47.93166 | 2025-11-16 00:11:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fe91b023-2c66-3fb9-bc5e-96876629113f | -12.06573 | -48.21426 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 65854b0c-cbad-3954-8dbe-7c4c956f2b26 | -17.42575 | -41.69247 | 2025-11-16 00:11:00 | TERRA_M-M | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 22b39eb0-a4c1-3691-b541-9e7f3a3a2f1d | -12.06117 | -46.97753 | 2025-11-16 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4a6e7fe1-7bf9-3276-b65d-363a215bc9e8 | -11.16268 | -47.45093 | 2025-11-16 00:11:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 386ee03b-9912-3141-9a3f-63019105444f | -15.46155 | -39.22946 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| ca5774bd-7368-3007-9216-36ff6bbc3b85 | -11.1647 | -49.43706 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 96f509c8-b35f-3873-a34d-a25bd18de9a1 | -13.79488 | -46.90269 | 2025-11-16 00:11:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6984d6aa-6a72-3140-9a37-4c79ec634a48 | -10.6694 | -44.80106 | 2025-11-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 902cb927-0684-3c78-a60d-693feb5ffefe | -11.71468 | -48.87735 | 2025-11-16 00:11:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e5666518-bdfe-38dc-9caa-961f738695d5 | -10.12086 | -43.90557 | 2025-11-16 00:11:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| fa5bb1f5-3db0-3cdb-8822-d039ac2297ee | -10.25428 | -45.06477 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3f034b0a-05d9-35bf-8fdd-e4152faf846c | -13.81712 | -42.55037 | 2025-11-16 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 89442f7e-8390-3ba7-b3e0-60dd01ccab79 | -11.67746 | -43.90413 | 2025-11-16 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 26e98a1e-a4a7-394d-adc0-b0b6f235c08b | -10.17033 | -44.52002 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cb383bbd-6257-386c-bc83-ab9b6e0cfd1b | -13.81578 | -42.54099 | 2025-11-16 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 620e7b92-151e-346e-859c-e32ee27b5dea | -11.08515 | -44.81779 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc2ca0f4-976f-35bc-a79c-f4f95c822bc0 | -10.44951 | -45.07995 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74ae6c51-0c6e-3282-8188-ead5d5c48905 | -11.66555 | -48.46842 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ef748100-1bb6-391a-b30e-09e9442824e7 | -12.80301 | -45.95601 | 2025-11-16 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2d50575d-b3e3-3603-934f-104f718b8450 | -11.16417 | -47.4623 | 2025-11-16 00:11:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dd41c830-cd1a-3012-86fc-6c108ce4287f | -13.32076 | -43.67101 | 2025-11-16 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6a2d79b-6327-3f0b-ada9-84bc70aab0af | -11.41336 | -43.33503 | 2025-11-16 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d510927b-195e-352c-9949-c5bac2fdff9d | -13.75472 | -42.8894 | 2025-11-16 00:11:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f3a4201e-72af-3a58-8ae9-128ad1ac1556 | -10.99412 | -47.72294 | 2025-11-16 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2f52f70d-8af4-3ad0-b75b-332d1ae4d7d0 | -12.01467 | -49.27417 | 2025-11-16 00:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4fddcd39-99b4-3ff2-a028-c7f040f8c65e | -12.51108 | -44.94273 | 2025-11-16 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d65987cb-7895-3725-8d5f-02a9a9e5627b | -15.52609 | -44.38247 | 2025-11-16 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| c20a94ab-e580-32ef-bc06-13da40fdcb7f | -12.21572 | -49.61979 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 27cc0a05-9dc8-3b76-bb57-80c898e17d1e | -12.21369 | -49.60284 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 690bff37-4e59-3518-bb12-a8de168b7253 | -10.62338 | -44.59744 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1eadeffc-e7df-3553-9342-e4ef9ee2eb9d | -13.71585 | -43.65535 | 2025-11-16 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e6afdfe3-2daa-3ace-a892-03869c2f5f98 | -11.05845 | -45.15426 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 4d1fbecb-c3a4-370d-ba38-4ff3f40fef6c | -14.36199 | -47.87908 | 2025-11-16 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5335d6c7-28d2-361f-b163-362ee3ea5265 | -11.05968 | -45.16341 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8efaf743-2d91-323b-b1df-2f99bbfc01a6 | -15.36885 | -45.64059 | 2025-11-16 00:11:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ac1b43b2-8a45-314c-8a86-346a031d6947 | -10.1767 | -44.50089 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 32ee2d5e-a046-30fc-b75c-b993c8b6e2f8 | -11.91504 | -46.19109 | 2025-11-16 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README3.md)
