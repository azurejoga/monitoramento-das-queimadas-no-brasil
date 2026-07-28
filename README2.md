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
| fc89e564-3a76-3f11-9b2f-c24d539908f5 | -14.2938 | -58.952 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e14cdd0-5a34-3afa-8eb2-e037519c7a08 | -15.7658 | -48.381901 | 2026-07-28 00:10:00 | METOP-B | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9f0771-cfa0-3c12-9dc3-20100e743904 | -15.243 | -48.5784 | 2026-07-28 00:10:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e50f7ca7-c90b-3649-b83c-743275930857 | -14.2358 | -58.962799 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f139147-efc7-339e-a728-2bdc5c4cbeb8 | -9.3904 | -40.3633 | 2026-07-28 00:10:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 296945bf-a0c8-3939-91ee-66253fb3dc46 | -4.3698 | -47.765999 | 2026-07-28 00:10:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a36f53d-608b-3825-a7d7-3853cd24c9ac | -3.6787 | -49.470699 | 2026-07-28 00:10:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff0c1cad-1809-3cb7-aef0-5b8271d9ba90 | -9.3566 | -44.724998 | 2026-07-28 00:10:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29407375-99b4-3eae-9755-aacf098fd67b | -5.8118 | -43.479301 | 2026-07-28 00:10:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1a2670-0711-3635-bcf6-266270cf847b | -11.78 | -47.0774 | 2026-07-28 00:10:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b1bd81b-f4e9-36a8-885e-66d890c91ecf | -7.7088 | -46.520802 | 2026-07-28 00:10:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af571d1e-6563-32a9-b01c-c8654eae4370 | -12.4841 | -50.5364 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5211d3d8-0ead-3819-bb94-e2882660d167 | -8.315 | -49.420399 | 2026-07-28 00:10:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb28ecef-e4f7-3bac-9c21-ddc2dbf4b343 | -11.4928 | -47.531898 | 2026-07-28 00:10:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d656071-94f9-3a57-9258-88bb43cb6f99 | -6.8643 | -45.9981 | 2026-07-28 00:10:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcde224b-0837-31fc-9658-37653be3aa18 | -9.3664 | -44.722599 | 2026-07-28 00:10:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1d3c2eb-fe6c-3f4a-9e60-6a7c231b5410 | -16.866501 | -49.571999 | 2026-07-28 00:10:00 | METOP-B | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f37e139b-e5de-3cdf-a20d-a978985e829d | -10.3766 | -49.5639 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 159f6656-1e8c-3df9-ae97-5a7ba78564a2 | -11.9787 | -45.544899 | 2026-07-28 00:10:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d14a9e4-c392-3fc2-b1ae-c9ff81fb909e | -12.8448 | -44.372002 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6b3755-f182-3133-b5c7-419dfec2dfd4 | -12.8496 | -44.3918 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22fa9e39-d2b6-3349-aa6a-fa9a6d82af90 | -7.004 | -45.410999 | 2026-07-28 00:10:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3e1b6f-5666-3cb0-958d-588068ab27f9 | -16.7306 | -49.415901 | 2026-07-28 00:10:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 126d3b87-f9eb-320a-88cf-a317148d307d | -14.2841 | -58.9538 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09001682-eb91-3016-927d-b045f3cdf7aa | -14.2798 | -58.929798 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc893215-c88f-3011-8c0c-e1255cd59e29 | -2.9093 | -52.717098 | 2026-07-28 00:10:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b437d57-0e98-30ca-81eb-02d828664b03 | -12.4882 | -43.754902 | 2026-07-28 00:10:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ab73764-7606-3a86-86f6-67d5801b172e | -14.2648 | -58.957401 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a51ce0c7-1af8-31d6-aefe-00ed9549bc98 | -10.3782 | -49.5709 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7db815a0-e55c-3586-a68d-c98f50952837 | -20.7202 | -49.424099 | 2026-07-28 00:10:00 | METOP-B | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4ff1dc17-f96a-304e-9b45-19792f1c551e | -19.230101 | -46.957699 | 2026-07-28 00:10:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7d8d341-0ca1-35ba-86f5-c756194e6165 | -4.9425 | -48.239101 | 2026-07-28 00:10:00 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a7cee5-0f38-3607-bf0e-073b064faacc | -17.403799 | -47.316799 | 2026-07-28 00:10:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79747d3d-10b8-3484-ac21-a1d6bfd64792 | -12.8472 | -44.381901 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 777f424e-4fd0-37d2-a06b-1bfe6948c5d7 | -14.2745 | -58.955601 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb5a5f1-2a84-3f53-a55a-1496a0fab25d | -17.3004 | -42.6619 | 2026-07-28 00:10:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bcba455e-7b6b-3469-9592-a57be65511eb | -15.8094 | -41.8806 | 2026-07-28 00:10:00 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c1b18ab2-e363-3e39-bd3a-a06b83b58e55 | -9.3399 | -47.903 | 2026-07-28 00:10:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8c05035-8703-38f3-84ac-df1384df5e98 | -12.4645 | -50.540798 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2bc2ff2-0cce-30fa-80ec-acbc4628c65d | -14.2411 | -58.937 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a20245fc-ff78-3723-9f4c-0efc9710301e | -12.481 | -50.521801 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9995f345-586a-3b8a-9f63-b017908ba36b | -12.453 | -46.508598 | 2026-07-28 00:10:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d21e720-ccfd-3f0f-888b-6a6afb687989 | -7.4563 | -49.723999 | 2026-07-28 00:10:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a74a339-92b3-3516-90ca-2b7ba52d9634 | -10.3864 | -49.561699 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1f6e07d-4e5b-3156-a3a9-d81114867688 | -14.2895 | -58.928001 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64a0a39c-62b6-3bac-8224-9e6d26ce2925 | -7.4072 | -46.818501 | 2026-07-28 00:10:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dafa5ef-63d9-3145-bea9-996b6a5d0f8b | -16.7208 | -49.418098 | 2026-07-28 00:10:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23498eb2-02f4-34f3-990f-272163ec93ae | -7.3613 | -48.133301 | 2026-07-28 00:10:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 207d3442-6298-3126-8409-a1781d578929 | -14.2605 | -58.933399 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 225ad67c-256c-3589-bf06-79e534118b1b | -14.293 | -45.6339 | 2026-07-28 00:10:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dede61fa-e9eb-3677-9e6e-1ce84de942bd | -9.3639 | -44.712101 | 2026-07-28 00:10:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e2ac726-2cfc-3375-ba39-698db2b38f0d | -6.1884 | -47.296299 | 2026-07-28 00:10:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6a9503-08e2-3306-a892-8ab29d4507f5 | -7.831 | -47.0881 | 2026-07-28 00:10:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 864329fc-a052-308d-8ec8-75d1e34f0532 | -17.312799 | -42.6702 | 2026-07-28 00:10:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b66174c2-6523-3098-855c-2f7709d7599a | -17.393999 | -47.319099 | 2026-07-28 00:10:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6dd11f3-6275-3e17-ab40-a7abf96a56de | -12.4511 | -46.500702 | 2026-07-28 00:10:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1329a35e-e810-38f2-8e74-c9c3f7ea154a | -10.6738 | -49.6497 | 2026-07-28 00:10:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59b1061e-0177-3dde-a71e-a89ac10e2592 | -12.4548 | -46.516399 | 2026-07-28 00:10:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7076ec5-dabb-3639-a220-9bc0e466dfa6 | -14.2552 | -58.959202 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3144ad3-55eb-3e72-ad29-62472efb0fa6 | -5.4139 | -43.4058 | 2026-07-28 00:10:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db7a147f-ad9e-363a-83f4-bca5a7202003 | -5.4174 | -43.420502 | 2026-07-28 00:10:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 168cc548-42a3-3746-ac8e-c5cb8c7ed659 | -12.4712 | -50.523998 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf2b685-41ea-3782-9a5d-83f3602b6281 | -8.8772 | -50.041302 | 2026-07-28 00:10:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ecb0f69-f19b-38eb-add6-63a8cd20a134 | -10.388 | -49.568699 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3c2e23-57fb-342e-a3f4-4314f0c53eb7 | -18.8083 | -51.246899 | 2026-07-28 00:10:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b06107b-c4b6-39b9-a133-fe585ceaee03 | -12.3411 | -48.222198 | 2026-07-28 00:10:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 809136ea-aee5-3f40-800b-76a922f1e2d2 | -5.8216 | -43.477001 | 2026-07-28 00:10:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9cbff4-1c33-31ca-9212-86366bf4aa60 | -14.2702 | -58.931599 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23bb0486-e091-3c1b-8e2f-446e1fdb8647 | -15.4307 | -41.368698 | 2026-07-28 00:10:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb1801a8-51d5-3830-8602-8c9402aa8602 | -10.7392 | -42.070999 | 2026-07-28 00:10:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9de4e2f8-29cd-3477-a69c-75e4762189d2 | -9.3382 | -47.895599 | 2026-07-28 00:10:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 815b1e3c-d33b-3a11-bbe6-f03a3969b753 | -9.6032 | -47.747898 | 2026-07-28 00:10:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 422eed08-8e89-31c1-90d5-0d412ac76a53 | -14.2314 | -58.938801 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6ef20e9-8259-3a7f-b3bb-f02ffdf456b5 | -4.366 | -47.7495 | 2026-07-28 00:10:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6821a4f-749c-3656-9bbe-e2df0c0eae75 | -5.4806 | -45.111198 | 2026-07-28 00:10:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69e727d6-7605-3fc6-9b71-adf60ba6d6f7 | -15.3161 | -43.013901 | 2026-07-28 00:10:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 20464fc0-ee4b-36c7-93d0-98574c2f6165 | -18.859501 | -43.442402 | 2026-07-28 00:10:00 | METOP-B | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca45cd8c-896a-3fa8-ab78-814be1c8d5ec | -16.4538 | -48.988602 | 2026-07-28 00:10:00 | METOP-B | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c406d021-5725-3740-bb49-5b418f9b3ce9 | -11.7782 | -47.069801 | 2026-07-28 00:10:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0f8c216-8a48-33a0-9c13-999f9caaf280 | -9.5223 | -49.291698 | 2026-07-28 00:10:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eeb5ed3-e774-33fd-aa11-dc35411759d0 | -13.7063 | -51.888599 | 2026-07-28 00:10:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed243690-686f-3682-8bc4-2518c009c7dd | -11.0893 | -47.7967 | 2026-07-28 00:10:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e90bc4ee-411d-31f8-8e01-307a71ff87c7 | -6.8621 | -45.988499 | 2026-07-28 00:10:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37a39c40-a230-3455-b0f6-5e7b93e378f2 | -12.3188 | -46.7304 | 2026-07-28 00:10:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 042fb1ac-93c3-3e28-8ff6-9acb3513378f | -20.301399 | -46.3536 | 2026-07-28 00:14:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9f2e0f4-8fc6-3825-84b2-5226e03d78cc | -1.5152 | -54.526299 | 2026-07-28 00:14:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d10d4c6-93e6-36d3-bcf3-37165386fc83 | -1.5134 | -54.5182 | 2026-07-28 00:14:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ed7189-cf79-31b3-8560-ea6a4ae58918 | -20.729799 | -49.421902 | 2026-07-28 00:14:00 | METOP-B | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03f8407c-1fba-3b81-a7cb-9c7cab7e54d9 | -1.6744 | -54.4571 | 2026-07-28 00:14:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db3a69c-267f-3f85-8a93-0c2abb6f52be | -20.728201 | -49.413799 | 2026-07-28 00:14:00 | METOP-B | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 685c7135-3cce-3072-af1a-20c79f4eb378 | -20.299801 | -46.346199 | 2026-07-28 00:14:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 707ceedf-fa2f-34c8-b44f-c21ddd2479c8 | -20.7314 | -49.429901 | 2026-07-28 00:14:00 | METOP-B | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 48ddb9d1-c0c5-3b0f-8ef6-37d557cbe823 | -12.86 | -44.41 | 2026-07-28 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e383e673-8cc9-3b39-bb87-e190d74cae05 | -12.83 | -44.4 | 2026-07-28 00:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25bb6be0-baf0-39af-a6c2-35e8906e270c | -11.7882 | -47.0659 | 2026-07-28 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ce5f6043-d724-30c0-a68c-e9a8765f3b47 | -14.2499 | -58.9671 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2f0325a2-1164-3e51-9b57-581cdd391edc | -20.723 | -49.4242 | 2026-07-28 00:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 199.8 |
| bb09b983-5e39-392c-ac74-177bb18f65ac | -11.7687 | -47.0909 | 2026-07-28 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9104b412-082e-3828-a176-fb9a18847999 | -4.3774 | -47.7627 | 2026-07-28 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 25eebb6a-a0ea-3c50-8b1c-9f4531d0758d | -14.2496 | -58.987 | 2026-07-28 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |


[Clique aqui para ver as próximas entradas](README3.md)
