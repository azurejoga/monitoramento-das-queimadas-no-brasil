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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 846d91e2-376e-34ab-aaf6-720f9bb3af7d | -21.5913 | -43.90973 | 2025-08-25 03:25:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9d7968a6-45f8-3262-a99a-06bffe2ef1a0 | -20.44007 | -41.68943 | 2025-08-25 03:25:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3f63ed0-75f8-332b-a76e-bfbd72754770 | -19.17996 | -44.51302 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db89a555-7676-3067-ac0b-a4e921163296 | -20.50534 | -45.99287 | 2025-08-25 03:25:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79ef286c-e2fc-3235-933d-ece60febe876 | -21.63233 | -44.01735 | 2025-08-25 03:25:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 756d6418-c8d7-3b49-a69d-c341b60e2690 | -20.3596 | -46.72363 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b86d844-65b0-3b7d-9761-51041b8bbb99 | -14.92398 | -45.53054 | 2025-08-25 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ea66481-d184-3741-9e97-44b626bfebf0 | -20.3585 | -46.72826 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d1a36ce-c0e0-385c-96f2-ab3a30bacf0e | -17.7963 | -44.48561 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e895636-9461-3a69-aa3b-a9b21f6e7b53 | -17.49963 | -44.78722 | 2025-08-25 03:25:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c931ef61-4da4-3b6f-9cfa-cd5a852949db | -20.36073 | -46.77585 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc65befe-7d6a-3431-a957-1d2fabdd17db | -20.36071 | -46.71897 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a848751-2577-31a9-a6c4-0d25bf06348a | -20.29772 | -47.18645 | 2025-08-25 03:25:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0317487d-6060-39a0-a740-efb6231a4abb | -21.63156 | -44.02085 | 2025-08-25 03:25:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 8bd94d24-8870-304e-adc1-8166a2ee1912 | -16.4852 | -46.76628 | 2025-08-25 03:25:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62aa1d34-85fb-3e2a-89aa-64cdab777fce | -20.38108 | -46.7468 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b9ea92d-5da1-3fd0-8479-3589d9c6f307 | -19.57324 | -41.61073 | 2025-08-25 03:25:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| baf89504-0066-3934-920e-5e82d08dc3a0 | -20.36185 | -46.71415 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 10884495-88a7-312a-9b7e-45ad6d78c2d6 | -20.3839 | -46.7348 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7b380d2-3999-3950-865e-4863d82115bb | -20.90606 | -44.08388 | 2025-08-25 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ed6a039-b75b-3ec0-91e6-fb5fb67e5776 | -18.44715 | -47.55818 | 2025-08-25 03:25:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e3e7c6a-c916-3404-9b53-9b49577b6b36 | -19.91441 | -44.63355 | 2025-08-25 03:25:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5c42450f-09a8-39b3-95eb-fc7836697d95 | -15.05127 | -43.84097 | 2025-08-25 03:25:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e4aa187-d136-3080-933f-7d0b110d5c11 | -20.37237 | -46.75512 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5dda95d-3f20-3550-9784-ceb796925b36 | -19.17853 | -44.51797 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ddd2edb9-0cac-361d-aabf-dea2331abc2f | -19.76782 | -43.15952 | 2025-08-25 03:25:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 378a3f3a-83f8-30dc-a87c-6bd2bda4d255 | -19.36936 | -44.22099 | 2025-08-25 03:25:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 771bc7d9-c0f1-307c-8cfa-d206b29e7b21 | -16.48694 | -46.75883 | 2025-08-25 03:25:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5bfbb630-1315-372e-9b36-fd4a114d115d | -17.79244 | -44.48732 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 554c4ce0-9c26-32ff-bba5-9e2ef603a061 | -19.17322 | -44.51616 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c236b9c2-bb0d-3ad7-ae78-8e13baef2a1c | -19.80534 | -42.00576 | 2025-08-25 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ec40eac1-a958-382a-97ed-8b46ec420028 | -17.84289 | -44.41365 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d2e1532-2270-331c-899a-1d396db6ec18 | -19.36646 | -44.21864 | 2025-08-25 03:25:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a76abff-3259-356b-9ed5-04bd63f5b2c4 | -20.04746 | -44.47928 | 2025-08-25 03:25:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70c15664-49ba-3203-aa5b-be738e005431 | -21.15975 | -42.91299 | 2025-08-25 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8eb10d8-54fa-3c08-9b89-2a554ea2f245 | -20.2447 | -42.03861 | 2025-08-25 03:25:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e08dea6-8860-351a-bffa-aee6960e91b0 | -19.36559 | -44.22252 | 2025-08-25 03:25:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adecea3c-3fe9-321f-8c0e-892bd4c15734 | -20.35333 | -46.72171 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65949df8-880c-3a95-8822-3883e827b0f6 | -19.7651 | -43.14647 | 2025-08-25 03:25:00 | NOAA-20 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf680334-7f64-3c5e-b55b-d9c9d51e3399 | -21.28007 | -43.78411 | 2025-08-25 03:25:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ebba4df5-6953-31d2-b9f6-0c63e9ed6a56 | -20.29688 | -47.18214 | 2025-08-25 03:25:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06559476-6057-3a9b-8acb-67c636b273af | -20.61894 | -45.02879 | 2025-08-25 03:25:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e7567e4e-979a-30ce-a9e2-a6e3302188fe | -19.95824 | -42.84867 | 2025-08-25 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a9640d97-182c-33e7-9cd4-f4c4087bc049 | -20.0484 | -44.47513 | 2025-08-25 03:25:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73eac08c-bb14-330e-a15a-93f23e2e5dfd | -20.45124 | -47.41208 | 2025-08-25 03:25:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1abf231-1715-371c-87db-20a9d506e535 | -22.01412 | -42.09491 | 2025-08-25 03:25:00 | NOAA-20 | SANTA MARIA MADALENA | RIO DE JANEIRO | Brasil | 3304607 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4f7ef244-54f9-308b-b3ae-336ed02c9ce5 | -21.15844 | -42.9133 | 2025-08-25 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 190de896-c79a-390f-9c16-718af89b48cc | -19.36381 | -44.2194 | 2025-08-25 03:25:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a8da03-3e07-3a6a-9d86-5eb6e6cefff5 | -14.92542 | -45.53624 | 2025-08-25 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30d632a9-2982-3ac6-a82e-8ce71bd7d336 | -20.27439 | -46.65305 | 2025-08-25 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5adcee5-99dd-3ce0-9866-670e8a86257b | -20.34571 | -46.72543 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d59e4a00-dd4d-3111-807d-2fb96306a6db | -20.90062 | -44.08279 | 2025-08-25 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2ba9718-7113-37f0-a042-85d0496921fa | -19.57284 | -41.61138 | 2025-08-25 03:25:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1c94f8e8-b5cc-39b6-b912-ebe412b921b8 | -19.95765 | -42.85149 | 2025-08-25 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8c40c3c6-46ec-3653-a4bb-5c17b3c23254 | -19.5685 | -41.60957 | 2025-08-25 03:25:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| acad8628-3dde-3a47-844f-167123683713 | -19.34721 | -46.15105 | 2025-08-25 03:25:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7775f4bb-7d3a-36b6-982e-1be498b34fee | -21.63078 | -44.0244 | 2025-08-25 03:25:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ebc58483-2f2f-3810-a5a3-9af71fedd014 | -19.17222 | -44.52058 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48ffff81-5d2f-358b-8a38-33ae5ae64028 | -17.4986 | -44.79187 | 2025-08-25 03:25:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71abd17-6f73-31bb-858b-e657825098a4 | -19.47448 | -44.35667 | 2025-08-25 03:25:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ceedeab-6bc2-35be-8b8c-741285f1318f | -20.90496 | -44.08443 | 2025-08-25 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ca74fe2-d56c-386d-b379-335a95ae9fd4 | -20.38977 | -46.73846 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 967f91cf-ff4e-33ed-9812-45a841ce68e7 | -20.38523 | -46.72913 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4377e66-aa4e-3de6-9c00-a1261c8c2cdd | -14.65108 | -44.07988 | 2025-08-25 03:25:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b75cd0c-bbd9-3fb0-8650-5977f1b87dca | -20.36692 | -46.72115 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da9c35b0-01fd-3b47-8b0d-b091018b0056 | -20.45631 | -47.41992 | 2025-08-25 03:25:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a364891a-3005-37ee-bfdf-4ba6e78d06fb | -20.61985 | -45.02481 | 2025-08-25 03:25:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b28fb94e-819e-3e2c-a14b-ff21f9c6625f | -14.92666 | -45.53051 | 2025-08-25 03:25:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97b3259e-715a-372f-83d4-c5889d0c36df | -19.5681 | -41.61023 | 2025-08-25 03:25:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6c10a662-39cf-3de1-b185-b4beaedd6602 | -20.29115 | -47.18501 | 2025-08-25 03:25:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37a946c0-80e8-3237-940d-41e8d08ca569 | -19.17756 | -44.52242 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a566228a-6c14-3837-aa07-2f0777bd0bea | -20.43951 | -41.68699 | 2025-08-25 03:25:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b7fe256c-27ab-32db-8d3b-57b2ed2554cb | -17.79346 | -44.48254 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfe2b8c9-dca8-3243-b8d8-d15cfd4cd18e | -19.17951 | -44.51346 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e26f3309-2043-303d-97ab-ec050f133c39 | -20.26808 | -46.65134 | 2025-08-25 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfd5057d-02e7-36f5-8570-702d01b294b5 | -20.45243 | -47.41949 | 2025-08-25 03:25:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6c4b7a0-7a83-378e-8ee8-49ebb596e26a | -20.04552 | -44.47688 | 2025-08-25 03:25:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52546078-ef51-3bbb-bb27-ec608cc0148e | -20.37098 | -46.76102 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8458cb9-211b-30ee-ad9b-713b0d2b8840 | -18.38491 | -46.84276 | 2025-08-25 03:25:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d79511d-c1c5-3794-81e7-8fc6008637f6 | -19.17421 | -44.51173 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c0a8fd4-659b-322c-a72b-36e5865e6b15 | -22.68558 | -47.34993 | 2025-08-25 03:28:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2226b054-cca8-3d99-b6ff-1457a293d2c7 | -22.00835 | -44.29186 | 2025-08-25 03:28:00 | NOAA-20 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 742ce2e2-0a2e-33cc-8bb6-eb07cb8e2990 | -22.5357 | -46.8173 | 2025-08-25 03:28:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a3b37504-bf39-34cc-810e-cd5bbcbee92d | -22.9504 | -46.93544 | 2025-08-25 03:28:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edfeadd5-ea7c-396d-96ca-8d752d12b62d | -22.68777 | -47.3504 | 2025-08-25 03:28:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6a39b757-2616-32e7-8bf4-675f2a8c548b | -22.94907 | -46.94096 | 2025-08-25 03:28:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 580855ce-2054-3579-9a1e-6895625037a2 | -22.00916 | -44.28827 | 2025-08-25 03:28:00 | NOAA-20 | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 506eecbe-5d97-30e7-8a23-fbe1cc45ec53 | -8.9874 | -65.4192 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 56ff33da-4cc5-3bc9-8711-27081d2c9f4b | -8.0493 | -49.6967 | 2025-08-25 03:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ba6fe64d-639a-3497-85ef-7b36dcc85710 | -8.8734 | -62.4495 | 2025-08-25 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 221.3 |
| b34e7df9-d8e9-31f1-ad0f-1cec2b5278ff | -9.06 | -65.7344 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 24bf6918-8216-3900-b73a-fd8c67fbbfba | -6.8229 | -58.956 | 2025-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 43e48aed-3e10-3bdf-a2ad-a101aaef4eb9 | -9.0416 | -65.7163 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| cb4756a7-7008-3710-97cf-20cb7c68259b | -8.2128 | -61.393 | 2025-08-25 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 82fd93ad-9895-394f-ae56-48c665f95515 | -6.8228 | -58.9753 | 2025-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 4826782f-b3b1-3601-9471-c2550d15e8ee | -8.8733 | -62.4685 | 2025-08-25 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 7dd71f81-bb4a-308d-ab73-a80fc30a792b | -8.8918 | -62.4677 | 2025-08-25 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f91ce91a-0611-3fd6-afd4-a0fda69676e6 | -8.0496 | -49.6753 | 2025-08-25 03:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| efa3871d-aba3-3c5f-a43a-28017512d8c6 | -5.0994 | -43.1977 | 2025-08-25 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| dd4e0cf4-e836-30d4-bf2d-29a653857571 | -6.8413 | -58.9552 | 2025-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |


[Clique aqui para ver as próximas entradas](README20.md)
