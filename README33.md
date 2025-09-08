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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8904f0eb-68e9-396a-b383-ba1751c28754 | -6.35447 | -42.58561 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b2f89569-e470-3d94-8ad3-6a3c7d4fe08d | -7.87166 | -46.25609 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebd45047-c09c-376f-a538-1364b096d7ce | -5.73792 | -43.93164 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2527d004-6306-37a8-87ed-afa29459af0d | -5.81016 | -45.64971 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1cecb65-30a4-3829-94ba-734411cab4d1 | -6.93317 | -43.23211 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb79f036-975b-35f5-ba1b-db2320b9e78c | -8.29804 | -45.95029 | 2025-09-08 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22533cc0-39ff-33a1-85f7-0039b110cfdf | -6.1708 | -44.25087 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33cdd8a1-c1ed-3c0e-8a86-901c8a1b8507 | -5.85661 | -43.8471 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dde01f2-5a09-3e06-863a-135c275328b7 | -5.08115 | -42.41946 | 2025-09-08 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 44f2281e-69a3-3b4f-9a9c-050b59162907 | -5.2155 | -43.28633 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cb821af-7a36-3bbf-bc22-0480375fe274 | -6.85648 | -43.94763 | 2025-09-08 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60fcb8c-5f7a-34ae-adce-c4d1a78158ab | -6.31041 | -43.82457 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ebece03-c458-390e-bdc8-d192f0794c08 | -4.8962 | -42.21981 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5f0447ef-6f80-31e2-af33-e72ae955db8b | -6.22076 | -43.59483 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7528f8bf-63e6-3216-950b-2f4e37d91925 | -7.73082 | -35.14103 | 2025-09-08 04:00:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 67b30398-99b9-314b-bb32-e1bea6fbb42b | -6.68961 | -43.54894 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e42068ca-f729-3ed1-9d2b-9ab41ff1703a | -7.73684 | -44.73045 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff45c994-2687-35c5-bdad-bc29813e5655 | -6.54789 | -42.93188 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c70f6a52-482e-3af4-9335-a32cd2a64434 | -5.96185 | -45.77621 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e092fe26-e6cf-337f-8a0d-75bccb774c4a | -5.55125 | -43.29469 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d18fb5ee-d4d7-3cc2-8533-cbb62202b3e6 | -6.19689 | -42.64248 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e9225fb0-f87f-3252-a25d-064c49d0f7bc | -5.45184 | -42.80681 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 11e07ef7-5159-375b-984a-1829e24ab5f5 | -5.64018 | -43.9127 | 2025-09-08 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f8b6114-ac9f-3a64-a176-426723a69a17 | -7.68734 | -44.80611 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be538a45-e962-3c02-934c-f1f1738f2ac9 | -7.42127 | -49.26513 | 2025-09-08 04:00:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7061fe-1eae-3617-818d-1a25a082fe2a | -4.26614 | -48.18491 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8fa5d62-63ce-3e67-b30d-c504f61015a8 | -7.21829 | -46.19408 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04b06d2e-c4a8-3cd2-95e8-02e95439d45b | -7.24252 | -44.82041 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27af5638-cf3d-3851-afed-ecfd01949123 | -7.09101 | -43.88935 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64622bea-d561-30bc-9be5-a8aca3efdc3c | -6.21463 | -43.2925 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28213a8-e074-3649-9ea4-22097d8bd9b0 | -6.62684 | -53.36389 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 839003b4-5ae8-3b4c-b70d-f77f64875fdc | -6.49381 | -43.9821 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00c3d768-7601-3816-a314-09956c9e60ed | -6.46831 | -43.94894 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64fbcfc2-32cf-3e4c-a61e-631f14b04ef5 | -6.62235 | -53.34963 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10048863-b989-3550-950d-f948dfb00ae9 | -6.38333 | -42.61008 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48c1c3ce-4556-308d-a43c-f905ab9d89de | -6.25518 | -43.50169 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b43b531-8f75-33a6-9656-8b1cb6853f02 | -5.86835 | -45.07377 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32ee767f-1e69-3dc1-8fd6-e6acf4327bf9 | -6.84379 | -52.85951 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2acf76df-6484-3457-a294-9bb135331cd9 | -5.55108 | -43.79522 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4751892-0900-3f8b-9096-3ecaa3439bff | -6.91946 | -44.34281 | 2025-09-08 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8253b79b-ba3b-3d57-b287-eb371186548b | -7.57722 | -44.0018 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70a9faea-c172-3f91-b9d8-a7eaa88be05f | -6.63943 | -53.37291 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b19b296-f951-3809-850b-4eaa131b9e75 | -6.82306 | -52.80515 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 874d5bcf-baab-3aff-a841-f829b2af975c | -6.62505 | -53.37229 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f9c368bf-b9ad-3d41-86c3-1186cad0892d | -5.37298 | -42.63321 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2449e789-c105-3f53-85fc-5f5a3a79c085 | -5.8513 | -43.85568 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d20012d9-0438-3787-abbc-5fc9bafa97a7 | -6.31252 | -42.20359 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a8a1ab6d-12bd-37ec-97c1-83bad3d1b8eb | -4.4722 | -48.11766 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab000e6c-395b-36a7-9b78-f0efefa1f79f | -5.87918 | -43.97033 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1585f1f-17d5-33c4-bc3a-93fe28cdf871 | -5.43547 | -42.80586 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa02e121-d346-3080-bfd5-463b39a1bb1f | -4.89491 | -42.22768 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45acffd8-087d-3dfd-988e-14aa9c93a104 | -6.91884 | -43.80106 | 2025-09-08 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e9eaff0-0750-3a27-8543-9daac29ff990 | -6.62188 | -53.35165 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 974fd6f8-91a3-350c-a240-3cdc610b4565 | -7.09254 | -43.90336 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f65f14f8-d538-3497-8d69-77fac421d5f1 | -6.13748 | -44.26058 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d85ea7a0-dbc0-399a-a3fa-f4fddad72a51 | -8.61948 | -40.19781 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1889775b-57cd-3d55-ab3f-8761b961da9d | -5.7357 | -45.36964 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f191f795-325d-39a2-83ea-f4e7b7a222b6 | -6.85889 | -44.82662 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3ff4d62-8d01-3403-8d88-f24682ade790 | -6.20806 | -43.3792 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 527415d8-87f6-30a1-9eaa-7e53ab79cc3f | -6.17631 | -42.63507 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2fde53b5-5459-3090-8e7b-ada59d3325ac | -8.29389 | -45.94956 | 2025-09-08 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41d5c039-dfc7-3d8d-8e18-b69e360ea842 | -5.99792 | -44.25506 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 090552c9-e629-38aa-aa9a-32f12c0c5d54 | -6.66753 | -43.84579 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b00e0be5-872d-3fec-8b8d-d25e741b2678 | -6.85257 | -44.82291 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfe55a04-a73d-30a2-adbb-66458dcc297d | -5.4947 | -42.65838 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 162f30a8-f2f4-31d9-8236-27682913fd25 | -6.21703 | -43.59436 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27301d08-ec4d-3cb4-8e42-16caac854d81 | -5.2118 | -43.28574 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2adb7972-1e87-3d65-8584-d0a138b24a34 | -6.25123 | -42.4403 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 482574c8-b053-3c17-8e98-d6e3c81911ed | -6.28613 | -44.38491 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebfc71a3-4bae-3f46-baf0-998b4a632ebe | -6.94565 | -43.35933 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81ebdc8f-24ec-3b7a-849a-8a404a5c5542 | -7.11424 | -44.81762 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d49602f9-0a61-3e56-8d2b-c7efe2b15446 | -7.42714 | -49.26281 | 2025-09-08 04:00:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3476b62-7a2f-3453-9777-ca22e2fe1d1e | -6.25975 | -42.65588 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7553fbb3-0b99-3e9b-a8ee-95189574b5e1 | -6.27011 | -43.68969 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5005d34-4433-3d29-8d20-d7afeb2bb107 | -7.82496 | -45.42751 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24e5eb58-5c47-3918-9d4a-0d778628718f | -7.02056 | -44.94678 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b832daee-6572-377a-b1f6-f8b3c04c8f93 | -7.08728 | -43.88873 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9bb24ad-8d84-3aec-9f78-fc0d8b12ae55 | -5.18894 | -43.03483 | 2025-09-08 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a00abae1-05bb-326d-9b68-e37a32414de6 | -6.07826 | -43.55732 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e20863db-c03c-3e3a-a31c-5da7c1821515 | -5.98799 | -44.14928 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28742c5e-94c2-3de6-ab4a-82610af461bc | -8.10873 | -45.30865 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df74ceba-80b6-38af-b433-219de337e913 | -5.80031 | -45.65642 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005c7e4a-cf78-3cc9-b7a0-b7222067e250 | -5.51543 | -42.66591 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69822001-9c36-37f3-96e1-8522a45f0aae | -6.29698 | -44.39159 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7e6c44c-7e8b-34a2-b132-08d77ad91b7b | -5.88532 | -43.95669 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e5c6902-897e-39ff-872c-e438af2a52f3 | -5.63199 | -43.12166 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3088b6d7-f493-3718-821f-1ec8ae84738b | -6.46301 | -43.95741 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69d0e106-7c02-3d70-b43c-fe1696aa3435 | -6.46452 | -43.94844 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13e9d83e-dd88-3bce-ac97-d6e9e475cfb4 | -5.21758 | -43.69979 | 2025-09-08 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b51a2583-08d8-38fe-9ddd-025cc3fbf65d | -6.0227 | -45.8862 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d49748-14f7-3b0c-a36d-71a468762217 | -6.87521 | -45.53603 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 486ed137-27c0-35f7-8e55-6f6210c48a40 | -6.62876 | -53.35296 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c97734e2-bb5f-3d99-b0fc-a6a8776ad626 | -6.61937 | -53.3647 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca2c4ebf-3733-3a97-a295-e8a01d871d63 | -7.44032 | -44.93575 | 2025-09-08 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90483a62-42a7-372e-8182-190a4b999738 | -6.40183 | -42.99059 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 196126a7-78f0-3eb0-92a8-bffa2b5faa29 | -6.25893 | -43.68783 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3239753-3406-34a6-9104-ccc293c1d745 | -4.30258 | -48.09565 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77af1140-7563-3157-94d5-9aa34c9d607b | -2.82519 | -41.74103 | 2025-09-08 04:00:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2bfe055-71c6-3753-bc0e-13b80339b95a | -6.20396 | -42.64364 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f73409c-7ab5-30a6-b6f2-a9c15034f56a | -7.08336 | -45.19636 | 2025-09-08 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README34.md)
