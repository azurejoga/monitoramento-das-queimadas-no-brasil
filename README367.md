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

## Dados Diários - Página 367

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c4000af-b405-304d-a46f-fb18685f2c34 | -4.33305 | -43.79433 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 75b06f6c-df12-31e7-8f00-a698f6c02706 | -2.51085 | -56.1259 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bac3664d-ae89-3687-85de-7b74647d8213 | -5.41059 | -45.64095 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ae9d13c-89db-3a2e-ac19-6f638350d699 | -4.55627 | -46.31387 | 2026-10-08 16:39:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c7c078d8-3654-3a26-973d-e805e062b49a | -3.77559 | -59.25941 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f0876e7c-ffd1-324e-bb65-7c6b839d71bb | -3.25044 | -57.86639 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 231fdbae-761e-350c-898a-1ecb1ee09b24 | -4.31991 | -55.53249 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba8c2724-1b70-3969-9e05-9925212f7bbe | -2.54458 | -49.75504 | 2026-10-08 16:39:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f191cfe0-3e15-3b05-831c-8f7449748065 | -1.48876 | -54.55257 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 90519df5-64fa-3092-b8b5-02b2df353389 | -3.58038 | -54.31504 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d77d8895-35d2-3494-8d00-a8e02b72c96d | -3.2837 | -53.70235 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| efa88c50-c248-309b-b66a-9ab25dc9d9b1 | -5.37707 | -44.19667 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3bfd035-bf71-3d8e-9185-d3312b0bd215 | -3.80918 | -40.20153 | 2026-10-08 16:39:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 47998bb6-228e-39ec-a73e-683aaad5fe39 | -3.23404 | -57.84018 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25f6d7db-b04e-3796-992b-9147b7a4d4c8 | -1.98142 | -56.05962 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 86ecfa98-1faa-3645-9b68-774f2ce1e000 | -1.33492 | -56.40504 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c4e0afbf-fec7-3c21-b329-ee93a5ad7a43 | -3.15071 | -43.03247 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| daec35b9-f2eb-3935-be95-96df75d6fd9c | -3.80939 | -40.20255 | 2026-10-08 16:39:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 927e3308-2e14-39a8-acad-4d78ec53169f | -4.16809 | -43.34088 | 2026-10-08 16:39:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 13052c24-5f7f-3715-b602-bf50ef34cb0b | -2.55133 | -58.05444 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a580d36b-c31d-3d9d-b819-10c279130896 | -6.4454 | -52.64951 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8facbc0f-9847-3f5d-8bee-9d8ec1f01eef | -2.98251 | -54.0702 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 48016791-eeb6-33d8-83d2-a63460e541c3 | -7.20695 | -55.13041 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 384ec226-88b5-3510-b6c5-a7d6915d89d2 | -3.26017 | -57.05924 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 17bb0dfd-cc75-3106-88ad-083c3f991048 | -5.87124 | -45.96752 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6ceba686-3757-304d-adc9-3d097f18c8fc | -3.00745 | -53.90139 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c7f08b13-6753-3b3a-ada8-504ff8464037 | -3.87609 | -44.11547 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 8f8e6d42-f35d-3398-aa95-3e78e44d9bfb | -1.9577 | -54.05313 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 46d74bd6-62f5-35d6-87b0-e16382de1277 | -3.06203 | -57.48156 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c04ea24-1b07-3e5f-a144-a42f54ecd66e | -2.01912 | -47.88141 | 2026-10-08 16:39:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569dcf2a-2ec9-317e-bfb7-3762744a3cc3 | -3.0873 | -53.95533 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 89c2c438-1bbd-332d-bda9-99c19d3b0df1 | -5.28441 | -42.72917 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4e4766b8-4124-3c9d-9504-3f9efbb456a9 | -3.76836 | -44.35063 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| cba50089-c6e5-3895-bf08-e76494645d36 | -7.33755 | -55.08745 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8ffec460-8337-3ec6-baf1-bf0350ae0a11 | -3.40698 | -42.81 | 2026-10-08 16:39:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9c7a32e8-f89c-309e-8ff3-dfe158a3309d | -3.5919 | -54.68811 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f3d28d4f-4772-30c0-8a8a-8bb4f21d2a53 | -2.57568 | -56.17641 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 44831110-20bd-3e56-ba21-4c54c0b20001 | -2.69287 | -49.04448 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 17e1ba1c-af96-34d1-b89c-41b91825b0a4 | -3.11846 | -54.16237 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 334b322c-e6a7-3b16-a540-15cf5b6fc81d | -3.01577 | -43.34347 | 2026-10-08 16:39:00 | NOAA-20 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0e751b75-98ff-3218-94b8-8057b411bcea | -2.84807 | -54.11884 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 284a44a5-0d86-3312-a568-b48eb1816754 | -2.49019 | -56.13567 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| feec213d-3846-3880-8615-23c442b61ecc | -2.92541 | -54.11779 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| af34a44d-7d33-33cb-a411-5be5aa04eacd | -3.46962 | -57.90732 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 508a511d-65df-341f-b423-6f423f69ea3b | -2.93625 | -54.05133 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7bad3406-8175-33d1-98c6-41cc68466255 | -2.83638 | -45.763 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3909d70e-0052-36b9-a1b3-06cba4123d05 | -3.47951 | -59.50225 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 2c82da0a-c616-31f8-bac4-4a7e6b360130 | -6.61759 | -53.01225 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 86e39560-d388-3169-afc3-e41e4469e615 | -1.19443 | -54.20593 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 92b0c948-6e70-3d3a-ae01-7910fc756a32 | -2.21175 | -56.91606 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c0515267-974f-3b62-a13a-b30aca0487dd | -2.84882 | -54.1239 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 13dd6d4b-8655-387d-85d1-6cf68f7cec99 | -5.40503 | -45.6489 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b1173b6-faaa-3ef3-8b6b-fbdd4294f24d | -5.40068 | -45.90801 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 11d52a09-6726-34c8-bc51-5ced9343b956 | -5.62231 | -43.04119 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 325929d5-9db1-3624-a5a6-9e11b1f98d9d | -5.09396 | -46.2104 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0c6da051-1efa-34a1-891a-73d3f0bf0c37 | -3.78697 | -41.66495 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 78f72fe8-4884-3fb3-9758-0bb51dc7cc36 | -2.3089 | -57.98514 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e10570f5-d179-3389-a74c-d9a65d1646b3 | -4.57596 | -55.99057 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2901dd1d-59b1-33da-871d-fae874281428 | -4.58567 | -40.64717 | 2026-10-08 16:39:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 801ed05a-a8f4-3280-b329-f534516a5547 | -2.07753 | -46.57237 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| c7d49371-658c-3b5e-8a75-8783aec44227 | -4.36146 | -55.22195 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 49a2d25c-da3e-3df5-aa6b-d4c706f11e3c | -3.31626 | -54.04533 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 05e494b8-e1c9-3779-99e2-f65223de74b1 | -3.90084 | -44.12737 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fec94217-031d-3e80-8f0e-e0408b11f7bf | -1.19754 | -54.2034 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f8b00bc3-ccfb-3d2e-8f23-ad8f7731ec1d | -6.14598 | -47.92534 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50c4f14f-d888-3dfe-a898-79a5fee6cc75 | -6.13578 | -53.07276 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 077c959c-b690-3db4-b974-0aeeb90076db | -2.28746 | -48.75272 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 623d3c52-5f95-3249-b7c0-19eb03cd890e | -2.48441 | -56.17181 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| acadd483-a8ea-3f4d-be2e-653a64df10ba | -1.97658 | -56.06374 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d17898d4-6472-3908-a364-c4ac55c43d20 | -4.79085 | -42.75855 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 48eb90a0-05b8-37fd-846c-0278a4bc44c7 | -2.60159 | -57.58309 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c44fde5-3fa2-3966-9a1c-2614f973604b | -3.18238 | -42.58998 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 08262f64-d9d8-3342-98a5-182a49294a91 | -2.61791 | -57.00719 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b0041b1-eea3-3b2a-9f9c-c9d4716e9729 | -4.09592 | -44.13306 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 608064c3-803c-366c-938c-0fb01b74667f | -4.37087 | -40.41519 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1583e0c0-b42a-3f8c-b6b0-8886706fef0d | -3.01729 | -54.04458 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d06d9076-fcd5-3766-940a-356ae6a90ca9 | -2.10532 | -56.61676 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0c45c34-7d68-3821-b5a4-da6106b6d24c | -2.06572 | -56.8859 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 30fbbead-e741-36b1-a903-81471350d38b | -3.91427 | -55.74802 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| a68ac145-306a-37fd-98bd-241884f12558 | -4.66277 | -55.93018 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 208413a7-e4d3-35e6-92ce-3125cca9cba4 | -5.49814 | -42.85011 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bdfddccf-2b4c-3f31-8f00-f594efee845a | -1.53555 | -54.83369 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 2b3685f7-f6a5-344e-b9b3-8568981be85a | -5.70766 | -53.47283 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 32238dfb-d62b-3ec2-b245-95c4f6049a99 | -3.94325 | -40.72002 | 2026-10-08 16:39:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 3f286962-d326-3d78-9a1e-5371e024fd2e | -6.72386 | -55.12545 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5baa35dc-3cfd-3d5d-a5e2-a4c51833b38a | -4.03343 | -55.3241 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42394e94-1e71-374c-8ad5-96315c28d621 | -5.28457 | -48.10771 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 548c716d-392a-38bf-a148-ae067ee55aae | -2.28246 | -56.67283 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| be10785d-046e-36dd-b2d7-6df03f4df003 | -3.04456 | -54.25797 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 942d4b52-80d4-3f91-80f9-ba6ffc158558 | -4.577 | -55.99769 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 420d8035-a218-3087-8494-a8329b2270e8 | -5.48251 | -41.21761 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 857d37b4-4c81-3b8e-bf6b-d289e4790f0f | -5.513 | -42.82624 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 7514fc48-0144-34e0-b4f9-415e294ba953 | -3.73642 | -43.33298 | 2026-10-08 16:39:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2114dedf-ca66-30d0-af70-bbf8af560547 | -4.72638 | -40.92421 | 2026-10-08 16:39:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 85df3442-b4be-3489-b6cf-c154bd64828c | -5.34224 | -45.72589 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 75cb9480-cbb4-3a12-bcff-609ea5d9a3d4 | -2.90253 | -59.22904 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 544182b6-54e1-32d1-93a3-796bfd3cd389 | -6.32641 | -46.5509 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ccc0feb4-f433-3a64-be21-a198f33f52ea | -3.09746 | -53.95896 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 833b1855-6d62-3330-a411-f75708cba82f | -5.31325 | -43.65184 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c5d3a70f-aa8e-31d1-bcb9-fa73db92f3ca | -2.99272 | -53.85226 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |


[Clique aqui para ver as próximas entradas](README368.md)
