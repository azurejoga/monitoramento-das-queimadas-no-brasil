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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 024c58ee-4c3c-341c-9597-f7308a796bbf | -15.29059 | -46.41648 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5400491-e41b-3483-aeab-3a5e4fde31ff | -6.74904 | -44.7508 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 216f1e7e-e6d0-3956-ac68-1707be93fd5f | -7.17852 | -41.70276 | 2025-09-29 03:47:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a316d6b2-c9fe-330c-8b7b-3dc6e49ffc77 | -11.6664 | -44.29185 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d624db06-de3b-347d-9ecf-8c39d1ca9525 | -6.90567 | -44.00117 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ab92965-041b-315b-975c-ce9835105008 | -15.25764 | -48.77604 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d1902bb-66b6-3a16-ac94-9523c27cba5f | -15.9115 | -46.2022 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9acd7224-c1a3-389a-8853-784bdfa56a47 | -11.65159 | -45.33733 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12357152-3f40-3ce6-a524-a003bb3cf4eb | -7.24826 | -43.00992 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8ca09d7a-7959-3bc9-83b2-db0152c0bc92 | -12.59091 | -41.29013 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dc19b8c-e444-3080-8640-a12b4d895376 | -10.76563 | -45.37762 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55fa9f3d-d775-374a-a529-71d791a8168f | -5.89599 | -42.50387 | 2025-09-29 03:47:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cb983546-74db-3e3f-b332-57716ed26e49 | -7.02 | -44.78228 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55061d2e-f259-3e5d-9eb7-cd8801c6e4cf | -7.58733 | -44.80799 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| babfb400-e3de-361e-8409-cf77054fd0c6 | -6.08448 | -42.46261 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e83596c-71bb-37a5-b8ff-32f109b0fc2e | -11.98591 | -46.58575 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68c772f4-988c-3577-8a81-b446aad44109 | -19.2041 | -43.98708 | 2025-09-29 03:47:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffe93bc6-befc-3db5-bd3b-d9ad95032f7f | -7.2226 | -44.78746 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1659714c-221d-3d52-95d2-f3a077e780c2 | -7.44544 | -46.98787 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4c2b948-c627-3507-b60e-dadc969dbd9e | -9.04831 | -46.70955 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a10cb68-b111-399a-9d06-38692d8b3f43 | -9.63862 | -48.13284 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55f5a7bc-57af-3e3c-8c46-c74d63087359 | -15.86662 | -46.21452 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 298eb29e-a915-3e52-8603-775e55fbf89f | -11.98167 | -47.12871 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd675ed4-4552-386d-a766-c105fa02eb1b | -8.86975 | -46.61832 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 918e7fa1-f0a4-33e3-898e-8378b4ad7ef3 | -6.05914 | -42.46842 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f627e270-4f2a-317f-b50e-d69e5c5c1120 | -9.54078 | -44.66805 | 2025-09-29 03:47:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a7d06b6-aeaa-3349-8fb3-1e9aca715c2c | -7.30305 | -43.81661 | 2025-09-29 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d2cddf8-fdb8-3081-b1c1-21dde7560766 | -11.9248 | -48.03136 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc8fb6cc-2133-3a71-bbfc-6c3c9b04d92f | -11.26376 | -47.19815 | 2025-09-29 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb628ea2-a20c-3723-a130-380e5a4fc621 | -9.10219 | -45.84311 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f6b585c-edb8-3ea7-a4ef-6f6ab9bd1d99 | -6.46284 | -44.01283 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a3bcf098-a45c-3fc5-ae79-cf537648f0d2 | -20.04745 | -41.335 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51bd4ade-b4e7-350d-a3ae-eacfbbf6a4ea | -11.939 | -48.02435 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a23cd9b0-149d-37a5-a9ae-65a066082cae | -11.45518 | -45.01109 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ba73e75-04b0-310b-a423-2e7b8b078f8f | -7.58094 | -44.8018 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 095c36a2-89f5-3799-a20e-5b83d5889a97 | -11.99908 | -47.10206 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a25aee2-ddf6-3e51-ab6e-5c0cf85c3d70 | -11.70804 | -44.43118 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00988738-fcd6-3f24-b2a7-63aa05cf796d | -8.86293 | -46.62188 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 508ce5d3-827f-3952-9676-0636c8845973 | -15.27902 | -49.49796 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4373f7d-8c4f-3090-8d82-5a45d0dccf56 | -5.67403 | -45.28976 | 2025-09-29 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5af4834-4b72-3444-acec-a49c371c3eb8 | -7.31429 | -44.71823 | 2025-09-29 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be73635b-654d-362c-b8d4-d4f8945d9554 | -15.87078 | -46.83649 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d201a70-a703-31b2-8b8b-2a40277eafd7 | -8.25898 | -45.4897 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e2a182f-1f17-31c1-908a-5e19c65aca55 | -15.19403 | -48.47781 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29b3de9b-e429-32c8-bd0e-8c185cb6e911 | -7.85292 | -44.59321 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0dfc8b67-98fe-3f2b-aa70-44201dcaa649 | -7.8498 | -44.58876 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b10f85fc-23b2-34f3-9815-3c87eafb3f89 | -10.00764 | -46.69415 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ebb1aad-4e5b-3e01-8e59-4b9b0139c0f3 | -6.05871 | -42.46517 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aec7efaa-1abf-3ac9-a6af-4ed3a6eb6401 | -8.7774 | -44.94995 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0183b2a0-466c-301e-a53d-d9356e7cd6b2 | -8.71719 | -50.05213 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa436c67-f667-35b8-a564-5f88fc6db098 | -17.39283 | -47.12457 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78f903c2-c68b-36f0-84e2-2700286fe586 | -11.67325 | -44.29392 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ba3b4c-d580-35ad-97d6-e258ba52afe9 | -15.21876 | -50.10425 | 2025-09-29 03:47:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09bad0af-5fed-39d6-9f7e-b7da08c86f75 | -17.95825 | -41.51068 | 2025-09-29 03:47:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c80f974a-fc7b-3e34-8395-4fe544032048 | -5.79301 | -42.85582 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 634f4605-4a25-3b96-8c1d-77e32629fe8c | -6.06926 | -42.6064 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54bc4c46-1edc-3b88-b479-dec40e6cc8f6 | -20.07922 | -41.36372 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d2ee8014-1e1e-3b6d-a78f-5895d57afc07 | -15.51863 | -47.93253 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 540c2fb1-fa8a-35e4-92f2-621966d272a5 | -17.71436 | -46.69201 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb89ccbe-0ab2-348a-9612-3b1968100f9d | -10.81253 | -46.66629 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f1093ca-0ecc-3616-a4fd-135946367d5a | -10.76505 | -45.38073 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0716fed-3d79-39f2-ace0-75de375ea031 | -7.29279 | -42.83834 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b8a8975-2ef4-315d-a9ae-235308782461 | -8.86384 | -45.03562 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b5420f-1be1-3623-bd4f-4017971c363b | -7.22084 | -44.76607 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1b4d679-3bef-3a7d-8277-8a14559623ec | -11.6685 | -45.33333 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f88d161f-cd76-3204-ae7b-56e5b03bc93e | -6.86231 | -47.35687 | 2025-09-29 03:47:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66a8c17f-3874-3daf-a131-74c6282c4923 | -6.1157 | -47.17877 | 2025-09-29 03:47:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| efb77cff-2cb3-3b33-83f0-109cf35409db | -20.04827 | -41.33039 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a9f0bca6-ee59-3946-a857-3e1b23c0da66 | -11.65218 | -45.33418 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd46147-ceea-310c-baac-b052a86791b9 | -19.20067 | -43.98232 | 2025-09-29 03:47:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afe3e44d-1f34-32c2-9d58-bda81832c23f | -15.33644 | -47.91452 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55aadc3a-7fdb-36bc-bb3e-7f0640e8dc47 | -16.50763 | -46.03308 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 929b55ac-b207-3340-92ef-dae096b79ce9 | -15.87014 | -46.22337 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0098504c-3327-37b7-8135-a2ffba9d5ec9 | -17.08315 | -48.56945 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01e1ea4-bc99-394f-b70e-01cd6af95f12 | -15.54121 | -47.88153 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f3dd36d-ff0a-34f5-884e-aab5c289b847 | -8.86468 | -46.61279 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ec281b73-6f37-30f6-a614-092ee0b3f3fa | -6.35605 | -42.64572 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9bb30e51-b3c3-341d-959f-04ddde3ff393 | -10.40541 | -48.11683 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f575b8f5-1bf8-3c13-a7c3-1baf02583538 | -12.66119 | -46.90855 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cabbd28-0c37-3ff5-90e2-217732655e3d | -20.08278 | -41.36442 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c069e4ff-6033-39d1-b91a-142748bba1c1 | -6.74842 | -44.75424 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e381070-33f0-3b39-8205-25632caa6f70 | -6.26459 | -43.6354 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c759f69-4d8d-3fd0-8f20-d29554e427a9 | -7.58314 | -44.80049 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b7b56e5-4f02-37d0-9665-65c90740d5e6 | -17.09224 | -48.5787 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 482dd690-9fb3-327e-ad85-ba019924a9de | -20.05822 | -41.33653 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 8ec0aed0-5e53-33a3-90cf-27abb63cd94d | -11.92377 | -48.03643 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fc33407-1d92-3746-be56-d77242f09532 | -6.14669 | -42.80811 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 44fc7ebf-278f-32fc-8c96-7ea5c9f2f11b | -11.36525 | -44.94284 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12d2d81e-ce98-3052-8fe4-00bb5f60a05c | -8.29626 | -45.44318 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d503e9f-4765-3fb6-9056-e683ba56ffda | -7.10534 | -45.53846 | 2025-09-29 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9effa135-55e8-35ef-8cb4-2bb9e378712b | -12.96794 | -45.1959 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 446c77e8-08df-3e20-a54c-c7592b6bd0ad | -8.71783 | -47.98941 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c71edd4-3e4a-34bf-973c-c02f189972d9 | -7.56562 | -42.41599 | 2025-09-29 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51d6756a-e216-33c0-ad2d-7fe9e0257b03 | -17.08756 | -48.57243 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 874b1f59-cfb4-3a58-91e6-33dd35b87ecc | -20.05384 | -41.34052 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 28884b89-44f1-3fb1-ad3c-ec901e11555e | -9.40122 | -46.24224 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31cf5136-69d4-3e84-a3ce-72e70b6426a9 | -9.39548 | -46.24117 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42d646f6-1383-3fa8-ba5c-09b65a8fc554 | -11.4239 | -44.9109 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5ba9c5e-a14b-3edd-993e-5d076bc2c7b9 | -12.01151 | -47.79097 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5288dff-28ad-303c-9fcd-8c7702aa3022 | -7.38466 | -47.03716 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
