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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71ffa8ea-18bf-32d6-9294-4d2a3898ab88 | -5.0374 | -43.12351 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1194bc30-c0bc-3653-8b1d-d3d2c3b27c3b | -5.66647 | -43.90415 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 258e4448-6138-39d1-92d1-789aa530596e | -5.8199 | -43.96752 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c061ed7d-06c0-3320-b95c-fb99dd11dead | -5.71456 | -45.41117 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2da7637a-cbaa-302c-9a8d-03b57abedf5b | -6.29504 | -44.21202 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71198331-0d08-3a76-89d0-8724fc13247e | -5.64377 | -43.91851 | 2025-09-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b050374e-3193-3cce-ae4e-1fdb1065e882 | -8.344 | -45.04633 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d30a0a4d-88af-381b-9c59-93e4f5b3fe56 | -8.07189 | -42.11139 | 2025-09-10 04:14:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ce056b5-793e-38b2-8f2e-d7f29749774e | -6.84389 | -44.91343 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e508cb1-bb18-3288-ab5b-f939fa451d6a | -6.24759 | -43.41008 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad969a40-ee28-357e-84a7-21adb6a32f1a | -9.01733 | -49.78677 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb84bf90-e7dd-394c-a9d4-61c3b8f37c64 | -9.06435 | -46.98016 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 062eae67-c7c6-31b7-963e-1c07966cc464 | -6.20333 | -41.02724 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 276efce0-a961-363a-948b-bad345ef1fe9 | -6.05409 | -43.12564 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 683d054e-498d-3475-9609-88b65974156e | -5.74154 | -47.47424 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58007bd7-fdb5-3ee1-bb30-b1e652c1d096 | -3.63881 | -49.21075 | 2025-09-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47d7e539-8914-3c6c-9ebd-02951b7d92c3 | -6.2559 | -43.40493 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8562d659-d23e-3a73-ae86-a12b88d516b9 | -6.3554 | -44.06706 | 2025-09-10 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6993c28-ad04-36c1-b276-a1d30798fe0f | -9.60427 | -48.04226 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c19abb6-e510-32bd-8147-47fdc552e826 | -6.64584 | -44.78949 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faffdb3e-c1f8-3620-82fd-2e501b367a43 | -5.56177 | -45.17689 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5114c607-4209-374f-97fd-75e2bc786781 | -5.67145 | -43.89421 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6bb541e-f5bf-30c6-bb58-59f6fd8c482c | -10.18306 | -44.76173 | 2025-09-10 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc8c0472-45fb-30af-9288-b67a290c96c0 | -9.06783 | -45.74722 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8238294-bc81-3192-983e-77492a20056b | -6.35124 | -44.8581 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acb60905-960c-3d57-a116-b8947ae4a83f | -8.10878 | -44.85429 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16ff0bda-2b18-3e39-8e37-2b57bf8cfc5c | -4.86837 | -42.76901 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc1634f3-a03b-3f59-ad7e-85c422b8c88b | -9.75657 | -45.40363 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 970c190d-1110-3c12-91c8-b1867024d42a | -5.58306 | -42.92043 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3b832f06-565f-33a7-bd04-97e4b991a2af | -6.20059 | -45.02512 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 329dfc7c-5bf5-3dbe-8948-c3295f0e07ed | -5.73826 | -43.10027 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f6e38ae8-8617-3e66-a899-6286afff7b82 | -8.04061 | -48.66111 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b651e694-880a-345f-9787-b59fb8d2094c | -7.98445 | -46.33176 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a39f0140-7f0f-310c-8014-1fb1a0c6d119 | -5.84965 | -43.86487 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 856b1c3f-9701-3251-a103-da8beb634e93 | -8.44335 | -47.27929 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f068489d-150d-3345-9695-38836c9f77f8 | -6.58595 | -44.00741 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a108adf-e89e-39b9-b0e0-47dd336f0d0a | -5.96853 | -45.80051 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86498f3b-e62b-32db-9a8f-59bb41ca60bd | -8.48978 | -45.66998 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc061d44-724d-36e6-baa0-9cc91547774a | -7.35506 | -44.30933 | 2025-09-10 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d8b4be9-7177-30d3-8301-aa48d1414650 | -5.73505 | -45.28177 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dde78d0-3476-335e-b064-fb3c3fbc8566 | -5.48946 | -42.16488 | 2025-09-10 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24685092-6d83-32b5-8bb4-f9b3b546de88 | -9.05633 | -49.80926 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 806692b8-5111-32eb-8658-5b91455692b2 | -6.06951 | -43.13511 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb7648a1-0aaf-3ffc-8909-c2a41b66bb26 | -9.14253 | -45.56556 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ea38855-254d-342c-b6b9-a66eba11bb38 | -8.07619 | -45.5546 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baeb3dd3-04dd-3938-8a80-5f3879eca4a3 | -8.04465 | -48.66161 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6763741e-4866-3a6a-89e4-f794b5c1c2f8 | -5.95323 | -45.80602 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b58377df-5bd2-39fb-aa90-caf8bd2c8245 | -8.06964 | -48.66021 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebd741b-6d13-370f-b3a5-df03c8e8b2b7 | -6.17367 | -45.81128 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0455a0f6-5c87-321e-85eb-8b79cbbd6491 | -6.44026 | -47.02518 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b82254b3-0e63-3efc-b90e-53904fd14a98 | -6.48124 | -41.75489 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9f6dbebe-fcaf-3550-8cc8-8efa22ffc479 | -6.19559 | -43.50444 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 581259cf-5378-3877-8cc8-2ada43275777 | -9.02937 | -49.78799 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c154d42-d5b5-3929-b16a-56fc6a1c7f5b | -6.11678 | -36.71556 | 2025-09-10 04:14:00 | NOAA-21 | TENENTE LAURENTINO CRUZ | RIO GRANDE DO NORTE | Brasil | 2414159 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00a29ab0-b91e-35be-95e2-f99522c06a36 | -7.78423 | -46.06244 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 391c4686-45a9-3d39-904c-8fb1bfb156d2 | -6.86225 | -47.9317 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68334c90-266c-31d7-b42d-9906bd019629 | -8.40219 | -47.29981 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c0851c5-4069-361c-8cbc-df66f2737915 | -9.06701 | -45.77381 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6368a6c4-4afc-3b89-89de-78822426fb7b | -8.20493 | -47.1531 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5d9df8f-7894-3462-a34b-31fa7dc05413 | -5.678 | -43.35543 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb3b389-b14f-33a3-8b93-6d8ab9ce20e6 | -7.1896 | -44.94656 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b06e443-9639-327b-bb42-baa342e45275 | -6.28893 | -44.22903 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abb579d3-34fd-3ee6-80fd-ff6d096712d0 | -9.10502 | -46.97943 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac57847b-99cb-34c2-ac24-9f49df0cdbae | -6.35233 | -42.60947 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 934071bc-c429-3e2d-a360-a791fc7c8f0a | -8.48655 | -40.49643 | 2025-09-10 04:14:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87a954bc-ae28-3d19-8cf3-0fb673769c86 | -6.05853 | -43.14045 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b75dd76-b9ed-375c-bf5b-652cee2ce925 | -6.46726 | -44.11343 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e48eaf-06fc-3a4a-9958-298b6094c172 | -5.69494 | -45.33378 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f341078-8f80-3ce2-b258-3944b0b3069b | -6.35981 | -43.04337 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e172a45-ccef-38ae-af72-fa513ad02e18 | -8.02878 | -48.63381 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10485a32-3d61-3da0-ab42-719eab7ea3be | -7.42203 | -40.08073 | 2025-09-10 04:14:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f073ed9b-d8e8-3baa-ba1c-f8e894ee4095 | -9.06345 | -49.81879 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79d23dbb-6bc6-3c4b-b0b9-7a62c480dec4 | -8.33745 | -44.85104 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3288134d-75d9-3450-bb7f-55ec12048f70 | -9.02159 | -49.78752 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 345becd9-ccfc-3ebe-8a98-778d417bee56 | -5.42624 | -43.44264 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f557b9-bc45-3488-a4d4-930643b80d25 | -8.74351 | -47.09955 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ea376014-8b37-3f9f-9c55-48d9cadd0df0 | -7.78199 | -46.05408 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 432fdc53-fab1-3175-8126-f19b63a9d61a | -9.08228 | -45.72287 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44ada533-92f8-3e30-976f-42d68a2ce2fc | -7.3086 | -44.15131 | 2025-09-10 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b6f784-ce87-31da-aac8-fa14a9582351 | -4.47348 | -48.11326 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dadc96e-07c9-35f7-9e9d-ce2819c25073 | -6.55475 | -42.92886 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68a9c174-ba75-3b7a-b854-79a992b97dc9 | -5.54251 | -42.65635 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10e8dcd5-bde2-3b5c-9122-cc6111241dba | -9.07907 | -45.76424 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb5dde9-a6b9-3ea3-af4d-b79bcb532994 | -9.05981 | -45.75353 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b49fa8b4-aadc-323e-bf7e-8cf8b817c58e | -6.1653 | -42.65501 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0f03807-2420-3cbd-92dd-4f68dfec2162 | -7.79844 | -46.07248 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08364c41-4316-3e68-bf11-1f17e8fe544b | -6.38275 | -44.45419 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 486397d0-a68b-330e-8760-1c68840e01db | -9.09212 | -46.96838 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cb7b56e-c141-3204-bed7-7772f26387df | -9.82923 | -46.05794 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdccb66c-7f6a-3741-80d5-1b1175c4509c | -6.28091 | -44.79075 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa060f02-1685-31e8-8977-00926e6b67fd | -7.08322 | -45.19903 | 2025-09-10 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa60c7ae-376d-3281-bc16-423126193f3b | -6.30245 | -42.20825 | 2025-09-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b026cd48-a8b0-35da-b79c-e2be7792ea74 | -6.05709 | -43.32724 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4069d33-d8a6-3e4e-a676-1e8906cdebdc | -5.43947 | -42.79217 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61719d1e-8194-3ee2-80fc-658e3180af91 | -5.85118 | -44.1779 | 2025-09-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 372eca95-d5de-3f6e-9ea8-952fa7c2380f | -6.33875 | -43.54513 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f36a6e3f-6722-34a2-95de-b6a777d2c4c9 | -8.48991 | -44.64297 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a924e3b-e9c0-36be-8271-63dd2b805fdd | -9.5143 | -46.54533 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a3144333-f205-39b5-91d3-85c400160b39 | -7.82543 | -45.41135 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36bd65d8-0c88-3bf9-9d94-754ac4186267 | -8.34735 | -45.04691 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README21.md)
