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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e64fd09-50d0-3a56-8980-f4f85fc5397e | -5.90589 | -48.07998 | 2025-01-22 03:53:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd2b7191-0264-3bf7-a32a-451702dcd41f | -11.23434 | -40.3727 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d911ab1f-9940-3d6a-a3c7-cf6f8db71451 | -18.41108 | -41.65944 | 2025-01-22 03:55:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 681bd428-cf55-3d68-9eb6-2459843cdeea | -18.71422 | -40.57105 | 2025-01-22 03:55:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ca09c266-69c1-3a12-97f8-40cfbe933564 | -17.59583 | -43.19899 | 2025-01-22 03:55:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6520347-0258-3b47-889f-c7c9a8e97708 | -9.63572 | -37.98952 | 2025-01-22 03:55:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f316ecbd-4222-3bfd-a260-0f9d79d5003a | -9.01021 | -35.43599 | 2025-01-22 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2a42cba2-f880-3d0c-adbe-6f51753bd303 | -8.70875 | -36.15889 | 2025-01-22 03:55:00 | NOAA-20 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e656957c-c651-3ec8-93a4-50ba588d5257 | -18.008 | -43.48391 | 2025-01-22 03:55:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58bc967d-81f6-384b-80df-c4d59a1c072d | -13.82032 | -41.73449 | 2025-01-22 03:55:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3558be9-c110-33f4-b47d-2874cfc1bd7b | -8.43852 | -36.31968 | 2025-01-22 03:55:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5902bbe4-0bc0-394b-908f-4911d158b3d5 | -13.47512 | -44.01979 | 2025-01-22 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39b66331-fd13-3e75-977e-616f652f017a | -17.09289 | -43.80457 | 2025-01-22 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe4ad8ab-176d-3e19-9ca2-3911cc59d10c | -15.26295 | -51.46429 | 2025-01-22 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 030420a3-9994-3457-809a-b51c47d7fe0a | -8.98306 | -35.61631 | 2025-01-22 03:55:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0704c24b-b7c5-3114-852e-a4f583496a8c | -13.80277 | -39.59174 | 2025-01-22 03:55:00 | NOAA-20 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 11d65b31-27ff-3a5c-ab32-6e6a85f422cf | -18.64297 | -51.45797 | 2025-01-22 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78b22d34-97fe-3c15-b175-f081817a9399 | -8.98335 | -35.61369 | 2025-01-22 03:55:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e9154c3-6b76-3858-83dd-3982bff6af93 | -9.00954 | -35.4404 | 2025-01-22 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92ba9f3c-5904-3edb-a89b-33eb729a9f5d | -15.25712 | -51.46299 | 2025-01-22 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f8eba44-697a-3b76-bfc0-15ef176782b0 | -8.91173 | -36.39568 | 2025-01-22 03:55:00 | NOAA-20 | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 85d44c15-fd83-3105-b010-88ac34a579dd | -18.60942 | -40.25629 | 2025-01-22 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 860d8c93-af1c-3a3e-8420-c4c2cb463194 | -18.03954 | -39.92497 | 2025-01-22 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a460d9e8-a346-3940-b88b-c6e9f3928af6 | -8.72255 | -39.54929 | 2025-01-22 03:55:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 507d4394-7179-38f6-99d1-f108f2cf192c | -14.13302 | -41.69063 | 2025-01-22 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa7e613a-73e8-38e9-92d0-352530fdce4c | -9.90952 | -37.06426 | 2025-01-22 03:55:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79ff8092-be4d-34f4-85e7-dc17696c32d6 | -15.87521 | -38.98788 | 2025-01-22 03:55:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbe65583-f804-3fea-84db-1a3c025545f2 | -19.85148 | -41.16101 | 2025-01-22 03:55:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d2769d85-33fc-39e2-a3df-eef33c0d3623 | -19.83873 | -40.08213 | 2025-01-22 03:55:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0c8ffd97-6e6d-3f4b-9481-cf95b5d13c88 | -15.27188 | -51.47985 | 2025-01-22 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cc209d6-21ad-3f2f-8b65-3687d090f022 | -17.22406 | -41.58154 | 2025-01-22 03:55:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95aba9a9-c7cb-3f06-9d33-88127a60571c | -16.42078 | -42.3961 | 2025-01-22 03:55:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bc34091-594f-3b49-9021-2ca66220598e | -15.26511 | -51.48298 | 2025-01-22 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5a56d2d-0d86-3a3b-8cbc-0840f8d782dc | -16.13415 | -42.51509 | 2025-01-22 03:55:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f7aad4d-d1d5-38d6-b32f-6b81371dd5c8 | -16.68029 | -43.88588 | 2025-01-22 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdbf56d8-7288-3390-bbbf-e74da86aab3d | -9.01317 | -35.43455 | 2025-01-22 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b2fe445f-94be-30a6-b11f-ea0747be91c3 | -8.98732 | -35.61262 | 2025-01-22 03:55:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f763df4e-8c7f-3710-a873-cd9784bfdd89 | -18.37013 | -39.9586 | 2025-01-22 03:55:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f96da3a8-c00b-3413-a84b-348fb7e9c0ef | -9.01254 | -35.43891 | 2025-01-22 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ceddde43-2f78-3cf0-aba0-561393e60e81 | -13.47432 | -44.02445 | 2025-01-22 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78bf8097-24cb-3fc6-a6b5-4b5fad9f5600 | -16.75819 | -41.05373 | 2025-01-22 03:55:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03c63434-558b-3983-a153-d77e3e196c5e | -15.69754 | -40.32849 | 2025-01-22 03:55:00 | NOAA-20 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d8b686e2-b0ac-356c-9490-e23196560a25 | -16.75156 | -41.05262 | 2025-01-22 03:55:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d2d488b5-36df-356a-a1f0-9e6792b36a9e | -8.70815 | -36.16287 | 2025-01-22 03:55:00 | NOAA-20 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ee6217c-6b8b-3eb1-bbe0-2d9616ba345d | -18.7109 | -40.57048 | 2025-01-22 03:55:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5fc171ee-bcc3-3e22-9492-de4303d67973 | -16.41572 | -42.53158 | 2025-01-22 03:55:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8c71adc-054e-3d9c-b769-ce69cb455e45 | -18.71033 | -40.57413 | 2025-01-22 03:55:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbc7f5cb-221c-3463-bb28-5e6cd5ca125d | -20.3494 | -40.36276 | 2025-01-22 03:55:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58226735-f0d3-39aa-a940-47dfca16391a | -18.64845 | -51.45917 | 2025-01-22 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c3ee021-a6c9-39c4-9b10-79690022ace2 | -9.01622 | -35.43948 | 2025-01-22 03:55:00 | NOAA-20 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a83683cc-723c-3a70-a2fd-d850416b0d96 | -18.61276 | -40.25686 | 2025-01-22 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e6e2dc2e-804c-3784-aa8b-faee72298edb | -16.87419 | -39.25103 | 2025-01-22 03:55:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 00112aa0-0348-36ac-b1a7-1eb4b9e5336e | -13.82093 | -41.73076 | 2025-01-22 03:55:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99b7c687-9964-3161-b390-dd84b9a4ec77 | -15.87859 | -38.98843 | 2025-01-22 03:55:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa3ccf70-21af-3beb-abf8-0d28b4d47204 | -15.27094 | -51.4843 | 2025-01-22 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfc53829-6963-31eb-a456-aca13e5864b7 | -8.98368 | -35.61204 | 2025-01-22 03:55:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8329180b-2fca-3c67-b911-652486838c4b | -21.28974 | -48.60562 | 2025-01-22 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb81b41f-e65d-3489-a70e-9030fea90169 | -25.19134 | -49.32687 | 2025-01-22 03:57:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97750cc8-1e44-31d3-8d44-60dcc30796e4 | -21.60018 | -48.45943 | 2025-01-22 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a620ecd9-f48d-3493-821f-36e451c38a80 | -21.10906 | -47.76864 | 2025-01-22 03:57:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1e53c26-dfd0-302b-b6f0-34c764e396ee | -23.33963 | -46.77246 | 2025-01-22 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d4baa26-3be3-3cf7-b6df-f6ab4d61cbc3 | -22.53732 | -48.81264 | 2025-01-22 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f4ca47c-5350-31de-81ae-e2a382c631f0 | -22.53974 | -48.81591 | 2025-01-22 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9676e736-4df2-3e4b-acd5-656b6d5a70af | -21.10976 | -47.77063 | 2025-01-22 03:57:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 889ab8cc-d1e3-3e31-a0a6-589577118d0c | -22.74576 | -42.95362 | 2025-01-22 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33a5b22e-5763-3b51-bf92-5bd31e511475 | -27.68601 | -48.74991 | 2025-01-22 03:57:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa8df022-62c2-3633-8ec9-af4a14bc47ca | -27.68482 | -48.75086 | 2025-01-22 03:57:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82188f39-5a0f-36c7-b59d-58e0c55c9212 | -21.60104 | -48.45506 | 2025-01-22 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3592706-9733-3b58-90af-352162b69aec | -21.10831 | -47.77258 | 2025-01-22 03:57:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98ee33eb-a6c2-333a-a34a-53620127de4f | -23.40635 | -46.55664 | 2025-01-22 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c83a0e1-e724-3f2d-b7b7-9854158d1111 | -27.46716 | -50.7719 | 2025-01-22 03:59:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a46408fa-95e5-332e-86e2-52c7e1d1fabf | -27.65143 | -50.37045 | 2025-01-22 03:59:00 | NOAA-20 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a042c95-16d7-34cf-b28f-87cff4c5cd00 | -27.74272 | -50.56842 | 2025-01-22 03:59:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a5eb5627-5b0e-3f54-8f66-36bb532635b9 | -32.10167 | -52.1204 | 2025-01-22 03:59:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0fef7150-b3d1-3a3f-918d-cf3ded744028 | -27.87416 | -51.15199 | 2025-01-22 03:59:00 | NOAA-20 | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 659304d1-f3eb-31fa-8c23-646839e810f1 | -27.46819 | -50.76697 | 2025-01-22 03:59:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cae81b78-952d-3eaf-9127-d90d6050eadf | -29.7507 | -51.13711 | 2025-01-22 03:59:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ab3489ea-9111-32e2-9f2a-b8eb1a665c6d | -28.94291 | -52.10179 | 2025-01-22 03:59:00 | NOAA-20 | ILÓPOLIS | RIO GRANDE DO SUL | Brasil | 4310306 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2b50cef-5428-3410-973c-5718afcb171e | -32.09737 | -52.11909 | 2025-01-22 03:59:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 86e57e55-95ac-30d0-9486-9655e414faa9 | -27.74368 | -50.56379 | 2025-01-22 03:59:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1958e642-3e5c-3da4-9278-0cc8e1236e80 | -27.73561 | -49.94022 | 2025-01-22 03:59:00 | NOAA-20 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8db054b9-088d-30d7-bd04-88c654234f60 | -2.42269 | -48.05407 | 2025-01-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48ef0628-8dd7-3e61-9d63-146a6905e06f | -5.35904 | -45.17888 | 2025-01-22 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64c6926e-e7d1-35cc-adcd-c64899761021 | -2.43179 | -48.19947 | 2025-01-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1d13b82-d59d-3b53-98ae-e310f7ad641a | -2.68628 | -45.64989 | 2025-01-22 04:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaca755d-ee5e-3900-9019-8866dae792d5 | -5.3596 | -45.17506 | 2025-01-22 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d5ba01-71c7-333e-a3e3-e4cd6ecbabef | -2.42612 | -48.0546 | 2025-01-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bdf4d42-0098-3315-b13b-c0436950bc15 | -3.22409 | -46.80059 | 2025-01-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5af5b17-8c7c-3c1c-8693-71289e8b67a5 | -2.59158 | -46.87259 | 2025-01-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d53b4012-4635-30e4-9193-4e16dfed9d4e | -3.22343 | -46.80489 | 2025-01-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f89764b6-dd59-3d77-b8fe-c69a90ce9574 | -2.2748 | -48.12372 | 2025-01-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dae5d1f-69ac-3b0d-b768-2b3f9c395a0c | -3.22043 | -46.80002 | 2025-01-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55957c66-bc73-36f0-aa7b-364ab04eb03a | -11.02657 | -45.05443 | 2025-01-22 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01a2eeae-7faf-3df1-baa1-ff976a2a1e45 | -11.02938 | -48.80109 | 2025-01-22 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d40bdd5-ff10-3b33-b15b-feaf3542a080 | -11.03179 | -45.05022 | 2025-01-22 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ed0dba2-f070-344d-9ba7-88c4365a5717 | -6.22823 | -44.82391 | 2025-01-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc13773c-f392-3a51-8aba-6ad8882375aa | -6.09147 | -46.23692 | 2025-01-22 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be0dbf54-fcfb-3f45-8fa1-f777add65353 | -8.15359 | -45.90044 | 2025-01-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66f31c5d-dfec-35bd-bf84-36ab4cd48504 | -11.23662 | -40.37508 | 2025-01-22 04:46:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6396861e-8dff-388b-a381-4a79173eb065 | -11.23232 | -40.37635 | 2025-01-22 04:46:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
