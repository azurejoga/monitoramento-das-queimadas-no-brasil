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

## Dados Diários - Página 404

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3ffc107-862b-3ec8-8e16-43b36b005c04 | -5.9835 | -40.9367 | 2026-10-08 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 60aef7b8-a589-356e-bdd0-cdffde02a9de | -5.6932 | -53.487 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 375d5bd9-6502-3ed9-806e-7175d6eb7ca3 | -6.0075 | -53.5122 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| f6c73784-e688-34a5-a11e-c60a51dce3ef | -6.2162 | -52.7876 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| ade5db1f-352d-3af5-99f7-37ecabb2e211 | -6.6224 | -53.0105 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b669db2a-9934-3a81-a7e8-e889f25fc294 | -3.8911 | -42.1187 | 2026-10-08 19:10:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| abe1606f-e46c-3c23-8f5e-515ff364969c | -3.4312 | -56.9307 | 2026-10-08 19:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 72633f0b-1ce6-3d48-8a18-44b4c46ec53e | -3.4312 | -56.9502 | 2026-10-08 19:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c28076ef-333d-31f9-84bb-102b77270f44 | -7.591 | -47.0201 | 2026-10-08 19:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 0e2c132c-cf77-3fe8-be2a-983a141afcc3 | -12.2316 | -44.7427 | 2026-10-08 19:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c356ffad-f657-36a3-8aa0-61f1799a5625 | -1.3111 | -54.1982 | 2026-10-08 19:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 53a22579-6bca-3d97-a5a7-1e38a0cb9256 | -7.4097 | -44.7427 | 2026-10-08 19:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 539e3339-610f-3df9-9b45-94c43a7e665f | -6.0964 | -42.8173 | 2026-10-08 19:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| ac9b880b-1a66-3fb7-a27c-63b426bad0a3 | -3.1879 | -58.6626 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 59b50992-b5fe-3247-8a83-c2112ac7c493 | -11.0758 | -44.0299 | 2026-10-08 19:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 4358a7eb-bb89-3469-a889-35bb993ad82c | -5.712 | -53.4455 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| cf871c01-41b0-3b99-a8bb-1df300f1d7ec | -5.3615 | -43.2027 | 2026-10-08 19:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2e614ee8-fa96-3bda-930d-cb5fb7ae5a0e | -12.2311 | -44.7661 | 2026-10-08 19:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 065c48f2-e96a-3933-9757-7bae0f07f280 | -9.0173 | -44.3676 | 2026-10-08 19:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| e872f40d-cf04-3052-b50f-ef2d601da1ea | -2.3115 | -57.9829 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 868f258c-c11a-3568-8191-bfd03bea5065 | -2.77 | -57.5293 | 2026-10-08 19:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 8af4b3c3-0c67-3af1-a8c8-c91707485ab5 | -3.314 | -53.6979 | 2026-10-08 19:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| a4d3811b-6d50-35c1-8ad6-d11a78ed85bf | -4.7666 | -42.6808 | 2026-10-08 19:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 2de5dbc9-f5b8-3410-937d-6d1b615a9924 | -5.3905 | -44.1968 | 2026-10-08 19:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a2ccbcc3-a7d2-3687-8f8a-8edc4b4c54c1 | -6.0447 | -53.49 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 39b5d50c-75c5-3a37-af7e-2dca465e6461 | -8.2435 | -54.7183 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 02b08ce2-e2d4-3c71-93cc-6234d4655d0a | -8.5921 | -67.0491 | 2026-10-08 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 96b252fe-55d0-309f-9ea6-f555e58adb9c | -6.2164 | -52.7671 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| a7d10e34-475a-3b02-bc7f-ab9588cbb3d7 | -2.0576 | -56.8786 | 2026-10-08 19:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| de4c4e3e-f520-3e93-81b0-7108ef98fd80 | -7.7025 | -45.4436 | 2026-10-08 19:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ba5e6aa1-ec43-356f-9bf6-ec643ac8ffd6 | -15.1057 | -43.6168 | 2026-10-08 19:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 68385b3c-01d3-3cdf-a42c-152cd5e94081 | -2.5675 | -58.037 | 2026-10-08 19:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 221.1 |
| f45c7a82-a6c3-38f7-a4f9-d7a9931cc943 | -8.2247 | -54.7396 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 2e89d459-9cb9-3855-bffd-84ce6e5efaee | -6.6027 | -37.8944 | 2026-10-08 19:10:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 96.9 |
| b62c6c56-ab1d-3321-81de-823f7ff7aa10 | -2.8712 | -54.192 | 2026-10-08 19:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 4188c15a-6e04-32e6-9b24-96d3935a2fdf | -12.211 | -44.8156 | 2026-10-08 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| bddbfe07-fe3b-37ad-aa89-16ac72044915 | -6.4567 | -55.4809 | 2026-10-08 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 72dafcb2-95df-3550-b405-3919fc3a112b | -5.9833 | -40.961 | 2026-10-08 19:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 5e8fe640-7c3e-3945-8619-465157f84fa3 | -11.7335 | -43.649 | 2026-10-08 19:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| eccd9c21-b86e-3b24-899f-87e4033b327e | -5.8599 | -53.4586 | 2026-10-08 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| ba8d10fa-c1f1-3c8d-a056-ec7ad5596b96 | -6.1242 | -47.9444 | 2026-10-08 19:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2dfda4a5-08a1-376f-b4b5-69a7ad99978c | -3.2085 | -57.87 | 2026-10-08 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 882de039-23cb-38ca-8bfa-5e003937bbd4 | -6.2348 | -52.7866 | 2026-10-08 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| d70c3099-8307-3947-865e-2a90e4e9e3b1 | -6.5212 | -45.3883 | 2026-10-08 19:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 312.5 |
| b05b54b9-ffea-3c22-bf16-802b5a5d091e | -2.8433 | -57.4891 | 2026-10-08 19:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9aca2d1f-391d-3c84-8d3c-2c115e6cf861 | -3.8749 | -55.9961 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 95056958-9595-31de-a6a3-fb173f31483c | -3.7057 | -57.0998 | 2026-10-08 19:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 15045446-5b0a-3a08-8d8c-ab00f856644f | -6.4764 | -55.3004 | 2026-10-08 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 935855b6-7ae1-3b4b-959e-e5b9dd104f5f | -3.1874 | -58.8358 | 2026-10-08 19:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 315abc65-eb36-3c2d-a5a6-eb24a7fb984d | -14.4591 | -41.1854 | 2026-10-08 19:10:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 193.0 |
| d4f175b5-6645-3524-b136-a7c16fa54f73 | -8.6107 | -67.0301 | 2026-10-08 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 480a7786-c982-3194-8a01-ccd6d6296280 | -4.51 | -47.05 | 2026-10-08 19:15:00 | MSG-03 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4167955d-85e7-3338-86d7-c3e69e85fdb0 | -4.61 | -50.96 | 2026-10-08 19:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e42611-b712-325a-b8d3-e52001c041ef | -9.03 | -44.37 | 2026-10-08 19:15:00 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5161b19e-ae3f-3455-a1eb-422a6389fe09 | -6.5 | -43.95 | 2026-10-08 19:15:00 | MSG-03 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65b13f71-f609-3a7f-a8bd-fab55922313f | -5.99 | -40.97 | 2026-10-08 19:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4ad6a15-315f-3760-b509-d30cadd7f6a2 | -8.9 | -45.19 | 2026-10-08 19:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 60151c0c-3bc2-35b8-bcd4-9b9fe03e02c0 | -9.89 | -44.88 | 2026-10-08 19:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 472399ab-a3b2-3d05-a95c-0ba23ace5f3b | -14.65 | -42.37 | 2026-10-08 19:15:00 | MSG-03 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f81be8ef-b661-3ed7-ae22-36a13175e0b5 | -4.54 | -47.0 | 2026-10-08 19:15:00 | MSG-03 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7480d002-d95f-3c32-9c43-840af0458f84 | -5.78 | -39.95 | 2026-10-08 19:15:00 | MSG-03 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6d41fb0d-86f8-301c-a163-7b0583328316 | -4.54 | -47.05 | 2026-10-08 19:15:00 | MSG-03 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13a43df2-b12c-3ced-a09a-70ebc18d662b | -12.01 | -43.53 | 2026-10-08 19:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7894d037-3075-3f99-8496-2bcaadb50a9f | -13.17 | -54.35 | 2026-10-08 19:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19ca2af0-2a88-30fc-9aa9-0931e0474bb6 | -11.83 | -43.58 | 2026-10-08 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fabd0163-7eaa-3308-94aa-82c0dbab3365 | -5.7 | -53.44 | 2026-10-08 19:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab63ac78-f36a-3b1b-8839-609e06c991a9 | -4.64 | -50.97 | 2026-10-08 19:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b984090-50ac-3f3e-a434-e7b0358e0324 | -5.31 | -45.79 | 2026-10-08 19:15:00 | MSG-03 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 485df99f-bf68-394a-a72b-2580432dfe6e | -5.7 | -53.5 | 2026-10-08 19:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d27931-8513-376d-8b14-7266a3ef7d9f | -8.93 | -45.14 | 2026-10-08 19:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca2a3b4-f330-3787-9d50-38d7f665252b | -14.65 | -42.32 | 2026-10-08 19:15:00 | MSG-03 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ebbf1637-67ed-3d8b-9bda-96cb6132d6c8 | -9.89 | -44.83 | 2026-10-08 19:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb35023-9e0f-3f8e-9a36-722512da7901 | -11.98 | -43.48 | 2026-10-08 19:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19b81340-b110-304c-bf49-f7ceffb8805d | -6.08 | -43.14 | 2026-10-08 19:15:00 | MSG-03 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 7290a497-fc56-3a3a-8a23-b16eb7379e14 | -12.01 | -43.58 | 2026-10-08 19:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98963e6b-df85-3abc-90e9-a715d5dd39b8 | -3.08 | -53.93 | 2026-10-08 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52f6d8c6-9d2c-398a-b319-32c20e94f754 | -13.2 | -54.36 | 2026-10-08 19:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 436e900f-774e-34cd-85a9-d342cb094cf5 | -5.28 | -45.79 | 2026-10-08 19:15:00 | MSG-03 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4b79059-a091-3d71-9920-2cfce3221b38 | -3.23 | -42.95 | 2026-10-08 19:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 286755d8-64b3-32aa-a1a5-8fbdafcf6914 | -5.99 | -40.93 | 2026-10-08 19:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e6725f1-2eeb-366f-8ee3-b22a119d2dc8 | -3.2 | -42.95 | 2026-10-08 19:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2029fffc-a601-3e0f-b087-5e003b86ac37 | -3.11 | -53.93 | 2026-10-08 19:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc809e23-73f4-3bfe-82a8-0197d1cb2ecc | -11.6 | -43.66 | 2026-10-08 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 999bc412-9853-3db9-bcc8-4b86ed56f72a | -4.51 | -47.0 | 2026-10-08 19:15:00 | MSG-03 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b433fe7d-cbb4-323f-a88e-e77ef798b8db | -4.64 | -50.91 | 2026-10-08 19:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5fd013d-ab03-37cb-9928-9982eb7f8466 | -11.63 | -43.71 | 2026-10-08 19:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2d6de9e-5a52-3180-bb17-374c50303895 | -8.93 | -45.19 | 2026-10-08 19:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2ac00c0-6c67-3661-9ea1-4cb86d2d29c7 | -13.3666 | -43.8979 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7ee27029-a7b8-3d68-9245-c2a2ed925e9d | -13.3671 | -43.8742 | 2026-10-08 19:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 3914fcd7-8cb1-37b6-9f96-abbd484635dd | -3.188 | -58.6241 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4343fb9f-5316-307e-81e2-0d70d93cedca | -6.1484 | -51.927 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 7fdc2360-4786-3c80-8f32-89a6619b8eaf | -2.8433 | -57.4891 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6abdd255-ba22-3619-a0af-7d61345a2b99 | -2.7428 | -54.1146 | 2026-10-08 19:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 313.0 |
| 7963aca9-07ff-3afa-aca2-c3a6ad881bbb | -6.4397 | -52.6522 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 639bfa7a-a1b2-30d2-87a7-b9e5f5908d87 | -2.5903 | -56.1839 | 2026-10-08 19:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 213.9 |
| 6391bf39-d620-37bf-b203-522f3ba1e441 | -10.9193 | -45.3942 | 2026-10-08 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 433dee8a-b83f-32fe-817f-9ddb43127018 | -6.4567 | -55.4809 | 2026-10-08 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 6a057ea5-f039-338d-b28e-11b5122fd489 | -2.8896 | -54.1715 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 627f8972-4ac1-3008-9c90-7857a2345259 | -3.8004 | -41.6708 | 2026-10-08 19:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 209.3 |
| 35efcf91-a8ff-3bda-91f2-83414bd44b03 | -3.5726 | -58.5581 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |


[Clique aqui para ver as próximas entradas](README405.md)
