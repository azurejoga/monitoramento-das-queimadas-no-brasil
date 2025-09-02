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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43203966-732f-316a-a00a-1e0fd5359815 | -8.46627 | -43.61959 | 2025-09-02 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4283618b-ad8c-3b18-8de8-9411d2e999d8 | -9.1195 | -46.04841 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 931a6bf1-817f-3b64-8e67-949d5eba9f48 | -11.38864 | -46.86364 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d2481b-64b4-39c3-bb18-63c05846174e | -7.06622 | -45.56618 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8546c877-2d82-39c4-b707-14e500bf14e5 | -6.86191 | -52.81627 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50cfaaab-4c81-360c-bc65-71c0ff18c1c6 | -6.80995 | -52.8201 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57e97e64-87c0-3516-8b98-35ddb3ee056f | -13.36988 | -46.93703 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90ef3005-bdc7-32e0-871f-b9b7872ff203 | -11.9228 | -50.61605 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c090995a-c8cb-3d36-9e15-aaf70212c95a | -11.79028 | -46.40681 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4154143a-bd98-380e-88ac-1a59c5e14c5a | -13.70342 | -46.89289 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44dd1772-eaa6-3970-8101-7f749affa4f2 | -6.7814 | -52.82215 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cf0dcda-c4ee-3d55-ab97-9a0cdf2a536c | -8.85327 | -47.49676 | 2025-09-02 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9782140-7ad7-3c5c-b1c0-2a5499ac8290 | -10.04726 | -48.14868 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff8716c5-3c27-31b6-b33e-dd293724798d | -11.10316 | -44.64234 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 7cd79f64-ca37-378b-b103-d88ff964e3c9 | -11.67005 | -52.21472 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 254c62cc-8106-3922-8284-4dfa966deb93 | -11.43386 | -46.81372 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eacc83b2-bd1f-327f-8e10-62e1b8ee3c30 | -12.57774 | -44.78916 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d3d9ed-3619-3c06-a551-09ff0d8b858f | -6.17246 | -47.2816 | 2025-09-02 04:14:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d6b8a1d7-94a5-3f06-ab3d-4ba3e748839b | -10.75356 | -49.56903 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7db0013d-128a-36af-97e2-108b7193e067 | -11.89998 | -46.67301 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cacd9c9-b7fa-31c6-994b-7cfc57b018e1 | -6.7901 | -52.80474 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d9a0403-57f9-36d0-8800-c13aeef90500 | -7.49389 | -45.3469 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf94624-06b4-36aa-b0b0-617de66e04ab | -6.84615 | -52.80994 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eed2bf4b-af75-3224-85c7-b4d284fbeb70 | -13.48694 | -46.92319 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afc2493f-efa8-39bf-9969-6d30a0407986 | -11.3798 | -43.61812 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f48a324-8b1a-3abf-ba42-a0eafe6b7689 | -11.09106 | -44.61153 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cb525a2-187a-30dc-8d8e-bca6968131e7 | -11.86419 | -50.61035 | 2025-09-02 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a14f28d-9370-3b84-83e6-bcc3de40f300 | -12.61424 | -48.18369 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 13b79dfb-a3c0-3839-a603-4f39133128ce | -13.70662 | -46.93248 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e249e706-ef30-3b51-8c91-edc0e090cbd6 | -6.96393 | -44.35046 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af970751-73af-3255-86bc-38cfbbd03afc | -10.8012 | -46.33894 | 2025-09-02 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0c11172-d3fb-3cf7-832f-0b7127215332 | -9.47503 | -47.60996 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 558dd018-acdb-3ca0-abac-a7808daa9f01 | -7.49449 | -45.34316 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a72aa8e-b93b-32dd-9918-3340c4b7849a | -6.98622 | -44.36116 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dfef5f1-b3ba-3a51-8991-794e2ebb5218 | -10.43965 | -54.7758 | 2025-09-02 04:14:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22865541-5a4d-35d0-9139-5f7f8739d7e4 | -13.32677 | -46.96152 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b6b8655-33de-338e-badb-e6bbd6d05d06 | -11.43735 | -46.81435 | 2025-09-02 04:14:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 226ca7ef-b59c-3491-b0a0-0dc94db7b3a2 | -11.09489 | -44.63017 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 303c7227-a912-3ef1-a34a-afc1aa8dfd67 | -8.74109 | -46.12719 | 2025-09-02 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 591997eb-7fc1-3eb6-904e-ff93e7b1e4c3 | -11.65458 | -52.17113 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ce65546a-a7bb-3cf5-8caf-99e02469d2e5 | -7.67262 | -44.7415 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 215180c8-2641-333a-9589-219189e94fed | -11.55093 | -44.83839 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 933393df-2590-3ddc-aedc-6771b7b248d9 | -12.8549 | -48.05307 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7fca6af3-33c6-3f62-9110-0ac792f3a4d8 | -12.77438 | -47.66321 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dff8ae25-99f9-3857-9b51-50a853eaa1a9 | -9.27638 | -48.56212 | 2025-09-02 04:14:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76138296-0015-35c4-9edb-4b8ec7220aad | -10.72844 | -44.79842 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c841038-5112-3312-bc57-54eb1bc12231 | -11.65443 | -52.19909 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 83cbd7be-318d-3e48-9417-954de5f169ae | -10.03958 | -48.05695 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30cda345-acab-3cdd-b195-ba2c7047e8ec | -13.31304 | -46.83081 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b378db52-154a-3b48-a492-d3f54ee39e3a | -12.1313 | -47.19415 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 757c76f3-fbd6-3461-8c2c-419574df3851 | -9.73759 | -48.97205 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06cf46d5-e864-3512-8fb9-543a9f1d8034 | -6.79994 | -52.81613 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e1e761a9-326f-344e-b302-a7d34cf4824c | -9.2884 | -47.11623 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46b60886-1de0-3773-82f1-70a31f5d604c | -12.86241 | -48.05215 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0a58308-d629-3ba6-ab11-fc8ddefd5aa6 | -10.04806 | -48.14402 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cda8ca85-61f9-3b01-a8ae-79f054561908 | -8.70712 | -50.44323 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec4860d7-b209-3863-a8a9-46baa3c2df29 | -9.75245 | -46.93902 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 333fbe83-f8d0-3704-9eca-c976318bff25 | -11.65531 | -57.35994 | 2025-09-02 04:14:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1fe8b56b-8a01-3b2e-9419-37482a914477 | -12.5645 | -44.78698 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d6ac6d3-9196-39ca-952c-2e90f4fbaddf | -11.07034 | -43.90397 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9cdfcb4-cadc-31b0-9c19-e30279fceefc | -7.16548 | -44.92365 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d23547d-8627-33ef-8fc2-f5673cac0ec0 | -11.37699 | -43.5705 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b44f7896-f24d-3101-bfc7-29204a29fd5e | -7.85079 | -46.74231 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d66a8dd0-3e05-310d-a5cf-4bca264549a1 | -13.53153 | -46.99606 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc3b5589-c163-3dad-9853-79595d8bc0d6 | -7.23897 | -44.05469 | 2025-09-02 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e6381f-87a8-3788-bc98-ee9804bf0e1f | -13.65895 | -48.15659 | 2025-09-02 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d21d9c73-f28f-3a74-90be-e652f85cf9fe | -7.06216 | -46.24524 | 2025-09-02 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b3c698-4cb0-3c69-b2f2-58f49fb34b97 | -8.85993 | -45.79217 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b063cc62-d8d7-3c70-9264-ac0e69e2d5e0 | -12.98127 | -48.10346 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bf8d953f-ad6c-33b9-b312-860b74a8d8f7 | -9.76099 | -46.93186 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4b1d206-6dcb-336b-baee-98c149c73fd8 | -6.82308 | -52.81294 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7421dce3-6fd2-340d-a09c-b1a955366e81 | -11.10208 | -44.62773 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eb2b82d5-0b79-3e1f-8b97-c75126f5727d | -11.65359 | -52.17651 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 75cc2c82-f1b8-396b-af78-29399714151d | -11.75584 | -47.83158 | 2025-09-02 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b3aa13-6d99-3a00-b924-d8e7c884c903 | -7.9914 | -46.47707 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afe98d8b-7da0-3bda-b485-c9e4e5b9665c | -7.9906 | -44.05011 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55bbefd-718d-3b63-86ff-2cdb7dcce66f | -6.87172 | -45.85444 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 86c281c0-1711-3d27-903f-c281a6221db0 | -11.66976 | -52.22447 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| be9d8311-d080-3139-8998-e1d0a88ec05b | -10.75834 | -49.56602 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed48206e-715b-3a66-bdc3-4834fa2351b0 | -7.98762 | -46.45521 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f7047df-5d8c-3a79-89ed-a9665758da75 | -10.75289 | -49.57281 | 2025-09-02 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d06f227b-def0-341c-9b7b-66ca56084e34 | -10.0508 | -48.0824 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cd7cd57-d1be-32ed-9ac1-64128943a2e4 | -12.55457 | -44.78536 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f50880c-227b-3023-98b3-e3f0d37e3bec | -11.35922 | -43.53136 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3092070-f838-37f5-9d96-a563bfb756a2 | -7.55145 | -45.72905 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00153db6-2475-3dc1-acd8-0dc0034d7f2a | -12.92851 | -48.10505 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbaf20aa-8af8-35c6-82f8-5cd82924ea4f | -7.2218 | -44.05552 | 2025-09-02 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e65ca5a-ce44-398d-b601-dabb095eb0d8 | -11.1026 | -44.64585 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 9401c61a-0bad-3eb0-8af6-650e6af58051 | -10.0699 | -48.88628 | 2025-09-02 04:14:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 933c952f-d976-3d08-8769-37668048d377 | -11.28926 | -43.56716 | 2025-09-02 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d851399d-aab1-3b85-9ecc-96ac30be8a0d | -7.84716 | -46.74169 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d39d06b6-4fec-39b3-a104-1348d104ff40 | -6.97624 | -44.33783 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18120a66-f101-33b6-bc8e-c2b125b96e87 | -7.76582 | -49.48716 | 2025-09-02 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d7ffd22-5c5b-3235-a225-f762f4040194 | -10.9637 | -50.78793 | 2025-09-02 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15029ab7-7dee-39f9-999f-77f9c23a08c9 | -11.94982 | -45.77676 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d60a98bc-ffdb-3cd4-9303-a90bc935f8b9 | -11.09597 | -44.64478 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d815c673-6330-3055-9f94-423385c3e386 | -8.18938 | -46.78389 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| cfeaa336-f64f-358d-b275-d3c194a78e2b | -9.29121 | -47.09922 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98d60858-03e3-30c0-b0d8-e12324cb7564 | -10.04849 | -48.0959 | 2025-09-02 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58c1152d-9e22-3ecc-8d21-d8cef93d6aba | -9.52196 | -46.51083 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README35.md)
