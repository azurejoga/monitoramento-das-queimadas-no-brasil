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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df49a73c-7a31-3acf-9325-795146682681 | -20.1906 | -46.01817 | 2025-10-02 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ff03fd3-50bf-3788-bae4-ef7eaceb16cb | -23.05016 | -47.06059 | 2025-10-02 04:53:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e6ffb62-5790-3cc6-bf3a-8752a1a57e0f | -19.01077 | -45.00548 | 2025-10-02 04:53:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7120ea6-053b-3f54-92f4-a7dfeb580f6e | -18.52285 | -45.04581 | 2025-10-02 04:53:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45426d3d-cf85-3b3f-b735-8d9e268154d4 | -15.78086 | -56.06928 | 2025-10-02 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| de16b237-9e47-32cf-8fa8-45ffc69a7656 | -15.969 | -57.23439 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c85f82-a738-3631-abd0-b002311f3b2e | -20.06086 | -44.58123 | 2025-10-02 04:53:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f52776fc-d9a5-3de4-82b8-f49221d6681b | -18.49866 | -43.40277 | 2025-10-02 04:53:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8ecc9be5-afae-36a0-b6b3-b347251f14c1 | -17.18267 | -47.03522 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fce4600-397e-384b-8ca5-4db79bc7bced | -19.80433 | -46.50476 | 2025-10-02 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c094db59-ee49-3c7d-ba14-9364b043fd29 | -19.63048 | -44.9019 | 2025-10-02 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| abd3b7c4-8ec8-3c7b-979b-5c47efaf02ec | -16.17991 | -57.59354 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 346b99a0-e722-300a-888c-31d9e49a85b7 | -15.97032 | -57.22664 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a7c4a4f-5502-3a6a-8781-b07d81b52834 | -19.96137 | -43.65187 | 2025-10-02 04:53:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3907ee28-179e-39ef-b728-9ede08dd807b | -19.45983 | -43.65727 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28b09054-9d37-3f41-9a4f-3a14489530e2 | -17.17496 | -47.01756 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 296166e0-264d-3dfa-a4a1-9acccc6f5927 | -17.17848 | -47.02922 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07b41a5a-b1ca-332e-b9a2-4ba3ddd283d2 | -21.78931 | -47.19849 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23273da3-8f3e-3fc0-a6e2-0365f3fa1885 | -18.17943 | -53.27464 | 2025-10-02 04:53:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f01903f5-1267-35de-b2e3-b084869aa06a | -19.46026 | -43.65274 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cee53140-eeef-3888-92e1-db0a765c7b76 | -20.24327 | -43.88626 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9c3c193-5ff4-3e42-828b-d33773b172b8 | -18.42439 | -46.53218 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fd4b17e-9ea5-381c-bd7b-964581ccdc63 | -19.45649 | -44.27902 | 2025-10-02 04:53:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c57d3b43-ae3a-3f41-b015-0b7dc6258edc | -17.17296 | -47.03418 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c9a99e2f-b51c-3fae-93c1-371c3c2c5452 | -22.28285 | -46.72076 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0be18c25-8157-3c42-bb71-2a1d128e26c8 | -20.48612 | -43.93471 | 2025-10-02 04:53:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9266b10a-8fbb-3711-8ea9-123a1d961e89 | -17.09094 | -48.56066 | 2025-10-02 04:53:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| edcff7b8-aecd-3f3a-be01-d97a73d9f13c | -16.96319 | -49.72894 | 2025-10-02 04:53:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e26f551-1405-3e4b-a8d1-d5fb5a3b3dcc | -19.8976 | -44.9404 | 2025-10-02 04:53:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9921b310-f92e-3870-a436-bdc7aa64889f | -20.8735 | -51.38144 | 2025-10-02 04:53:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e527bb0a-3255-33d5-8537-1de23593a234 | -17.08522 | -47.11328 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 15797baf-5289-3ae9-8a81-19ecff6caf45 | -20.10889 | -44.39123 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8925dce9-d681-37bb-a8f2-e65efdebe912 | -19.02031 | -49.74821 | 2025-10-02 04:53:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b39d7e87-4195-301a-aa3c-df9b473a2679 | -20.84537 | -49.42979 | 2025-10-02 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e3964d91-e8ca-3398-8ec1-7c8bb21f619d | -20.12778 | -46.3549 | 2025-10-02 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a19368-e86f-3152-8078-f0cc1a09c63d | -22.56211 | -46.79082 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ca53ea86-c211-36f9-8d78-29bdae85579b | -22.28316 | -46.7176 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 649a08c0-7323-3975-bdfb-6cf1c6886b65 | -22.38141 | -50.03007 | 2025-10-02 04:53:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ab1547ce-eac3-3ae8-8810-a25215650399 | -19.04919 | -48.13894 | 2025-10-02 04:53:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00646f0f-9e71-3645-9d6d-44282b0bc555 | -18.42591 | -46.53428 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23c22f9-7bf5-30e6-9351-d31a2bed460e | -17.25656 | -47.02154 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 189ed3ca-f72d-3c61-a579-a23aaf972995 | -18.84461 | -43.15206 | 2025-10-02 04:53:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9ffe9ebd-ea2b-3095-bd0c-5cc978bc772f | -20.12815 | -46.35145 | 2025-10-02 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f281e250-0a97-3653-ae1d-25c3929fa61f | -19.88815 | -42.62524 | 2025-10-02 04:53:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a1925047-521a-36c8-87a9-7234abbb808c | -19.01981 | -49.75219 | 2025-10-02 04:53:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98d1d732-0fd4-3233-8a95-b1eb6af8e365 | -22.25326 | -43.05886 | 2025-10-02 04:53:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 25f7770b-2cf3-3ac4-ba5d-0782c73c23ac | -20.11184 | -44.39483 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8d479e37-a2f2-3a79-9d15-3a81e57b3b2e | -17.96592 | -44.39498 | 2025-10-02 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f858502-b7c4-3c94-b1d3-7ddb709844a1 | -22.56769 | -46.7882 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c3017a4f-2fc1-38bb-9d45-f9e6a4daa6a3 | -15.97663 | -57.23179 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97919132-7e45-3c32-880d-e6534ff7e76a | -17.97953 | -45.01329 | 2025-10-02 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33c2ef3c-997d-3818-98b2-b9c0fa2bcc76 | -19.59619 | -45.89875 | 2025-10-02 04:53:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d7a442a-3e83-37c8-8b7b-715b4432b67d | -15.97315 | -57.23114 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d6ed398-e493-3f42-a25f-aaf76c259860 | -17.09074 | -47.112 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e81e036-03e2-3d18-8c1c-c2ff11824229 | -16.96387 | -49.72906 | 2025-10-02 04:53:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 823abf18-26a9-350e-8890-b7e421023bb0 | -18.43066 | -46.53785 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb18cd83-a1ed-38b2-a422-8884a122aa45 | -20.28397 | -49.23751 | 2025-10-02 04:53:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4ff3f16-22a5-39df-a883-422965e50e71 | -17.16939 | -47.02291 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88b07d75-a015-3835-b2a9-1e98ab8cb954 | -21.78361 | -47.20383 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bea2cc9c-be81-3dec-b364-573dcf321331 | -21.68818 | -45.6077 | 2025-10-02 04:53:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 21eea65b-f2bf-3841-8317-5817bfb51d45 | -19.00828 | -45.00158 | 2025-10-02 04:53:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94f98e2d-46b1-3892-bc06-7922c9d3edc5 | -23.06887 | -46.71336 | 2025-10-02 04:53:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e32e5395-9921-3fd1-b685-3496105730cd | -17.55087 | -44.48431 | 2025-10-02 04:53:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b55da5c-b4fb-3e78-9ad4-69bbc8247398 | -22.27531 | -46.74314 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f603c30a-674f-3015-950a-f38119ec47f9 | -22.56803 | -46.78474 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e0ec49d8-6ca0-3431-9c02-a32d707cd91a | -21.68779 | -45.61165 | 2025-10-02 04:53:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aa71445-c4ed-394f-9147-4c29df5b7601 | -20.22271 | -43.9077 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ea4dd4ef-a8b6-3589-a2f7-e01dc054a6a4 | -17.3945 | -47.16605 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d0d3c2a-81af-35ef-b32d-55ae6aaefc48 | -17.09037 | -48.56512 | 2025-10-02 04:53:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5ae0f4f7-c18f-32da-bb90-23161861d440 | -17.18201 | -47.0407 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f4d5ae4-baa2-3758-b65e-29d79e671aef | -18.50652 | -44.03288 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cf1ba97-7414-3e45-b315-e7eb95ed82af | -22.56737 | -46.79155 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 513bf8cb-2eb4-3d09-9251-005450de43c1 | -20.22882 | -43.90863 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3a6f79b5-a3c4-35b2-a796-2e84a7987988 | -18.34283 | -44.50285 | 2025-10-02 04:53:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6071a3a-98cb-38e9-9c2c-2ffad83206b4 | -20.11916 | -44.3803 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d734e71-93ca-39f1-9dc5-e5694ad50011 | -20.18751 | -46.0218 | 2025-10-02 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa668957-ef6a-3a3c-88a4-f7bb333b2933 | -17.08593 | -47.11139 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10b72ac2-4cae-3645-8965-615f1b4f96e1 | -18.5054 | -44.04445 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5582f3b-461e-32e3-991a-250f5aba8178 | -18.51217 | -44.03696 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d9663bc-4891-3ce7-aa62-dc63c7b35b7c | -22.2838 | -46.71111 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7376815c-63f7-34de-afbe-92eaf3905099 | -18.61849 | -50.71566 | 2025-10-02 04:53:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d60c64-972a-3c20-ad3c-b5795b71da2e | -15.96966 | -57.23052 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d99c4b07-f59a-34d3-9bc8-e7298eb4eb97 | -20.22923 | -43.9042 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c4c5a915-1a1a-3da1-bf82-8e7157fd165b | -22.55716 | -46.78675 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d3a9b2b9-e0d5-3a2c-b318-94aa284c929b | -20.48631 | -43.93812 | 2025-10-02 04:53:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6e08879f-d45f-32f0-91fc-5dee6edc6dc4 | -20.21588 | -44.18385 | 2025-10-02 04:53:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ac5c14a8-a834-3fac-9d03-629c70b29a12 | -17.70431 | -46.88823 | 2025-10-02 04:53:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db60503d-29e2-3d06-acd3-06fd3fae8d22 | -21.63255 | -44.89287 | 2025-10-02 04:53:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 50d3be68-722d-3c52-b49d-de74bc1c510f | -19.31239 | -50.05945 | 2025-10-02 04:53:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6d1a6ef-bd62-3bb8-bbb9-de6241955336 | -20.84817 | -49.47919 | 2025-10-02 04:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05cc35a5-d7ba-3dee-9f36-eec58caf73c6 | -19.96099 | -43.65608 | 2025-10-02 04:53:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 36fbe86a-a1c6-36e6-8c18-0d8fd55659e6 | -18.4295 | -46.5326 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a411fc18-6662-3e60-a74e-a35c90862804 | -22.62016 | -44.51273 | 2025-10-02 04:53:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ff0275d3-4c0a-370a-af40-ecc095a230d3 | -18.10104 | -54.55421 | 2025-10-02 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75f9dd79-0488-3078-8f0d-01fd36799da1 | -19.4651 | -43.65518 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5da48616-a501-37ba-963f-0d3c94d4e937 | -16.97736 | -49.17618 | 2025-10-02 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3476cc19-9192-352d-9e29-33a2fc15b64e | -19.96715 | -43.71358 | 2025-10-02 04:53:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d882a1da-03ec-356a-b13c-60463df4f76b | -15.96616 | -57.22995 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01cdb5d9-37a5-34ee-9c5e-e62a86f7841d | -17.32732 | -49.3909 | 2025-10-02 04:53:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae827f3-2156-3b71-8348-8a9dc1b27ad9 | -17.4002 | -47.16634 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README136.md)
