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
| 88d8b22e-aa96-34f0-9670-f24b658e5b43 | -21.33046 | -47.07959 | 2026-04-23 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a686a6-6f4e-31f0-8be6-a1dce459871a | -21.93633 | -41.13341 | 2026-04-23 04:00:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b75783c-c2e4-3faf-a76f-f3e40573fd75 | -18.26979 | -52.88855 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b58e6490-b14a-33a3-af31-ba1b64403a9a | -18.28233 | -52.88628 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86b31adc-b669-3b7d-b8df-b114e676d4ae | -20.24197 | -46.76936 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13fe326a-fc1a-32fc-8a55-e9618c581072 | -20.19098 | -46.90721 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed7e19e9-7e31-32d1-8841-34d0c64d6761 | -20.23564 | -46.80318 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd1d7305-4f51-3875-ba39-a3ecca0e852d | -21.39651 | -48.67018 | 2026-04-23 04:00:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56354655-ef55-3444-8816-6ee493212982 | -20.20268 | -46.73539 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdbcab15-ea44-36c2-8ff2-3a62df6f7170 | -19.9108 | -49.88187 | 2026-04-23 04:00:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08ffef36-526a-3ac6-bda2-b5dc664d669c | -22.78862 | -47.04781 | 2026-04-23 04:00:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 88744b82-2c69-3076-91dd-b5841b5513b7 | -20.24407 | -46.78038 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ec21983-0a37-3c29-9fc4-328610e20747 | -20.2012 | -46.89754 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3c9546fb-02af-3a3b-afc7-eb44c6b1d4a9 | -20.19478 | -46.88716 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f189e7d-1b61-3683-add1-e76ba72bec2e | -20.18465 | -46.8084 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7374d68-aa21-3700-8186-e8d518859aa4 | -18.41394 | -54.55001 | 2026-04-23 04:00:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18a8f748-a0ad-3b52-a96e-b6107d7a1849 | -20.19579 | -46.904 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9b638f6-148d-3ef8-a670-e78e7ec851bc | -20.20597 | -46.73998 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1d92a4d-981c-327d-b490-ede2cf7aa29d | -22.79738 | -46.35307 | 2026-04-23 04:00:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68e5d813-47f9-3a4f-9389-44a3891313d9 | -21.33691 | -47.07311 | 2026-04-23 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66df6bdb-4760-3cc1-881d-23115e62a9ae | -20.19876 | -46.88826 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1970919e-cb3c-34c8-908d-e87eb97cb596 | -20.19975 | -46.90523 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0dbeb130-4384-375c-8280-b779f06ed6bb | -20.20916 | -46.76702 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| addc30c8-cfaa-37db-ace6-e71714bfb0e5 | -20.19939 | -46.7309 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3eb37dc-908a-3cd0-8490-fd7404a623e9 | -20.18923 | -46.89437 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d7c73cc-6bd0-32f4-b026-a36485457095 | -21.70365 | -48.42887 | 2026-04-23 04:00:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 957567bf-2fb2-35f7-b362-cd615aa1ac25 | -20.24135 | -46.77265 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cb73ac3-5c69-307c-a063-ad2f21e0be07 | -20.24072 | -46.77604 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bff2f50e-9d67-3d73-8dde-e74a70fa479e | -20.18996 | -46.89051 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee5f0b8f-fa7a-36f1-9cab-6efce5ce4596 | -20.20925 | -46.74454 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de243cfc-0381-3b55-8d42-ecf73d907e10 | -20.23244 | -46.79807 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaecea30-3c96-38ce-b158-9988affc429a | -20.23956 | -46.8045 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 048ded79-cb9c-370f-a5c0-f6b574a0483c | -19.68576 | -51.3407 | 2026-04-23 04:00:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80967e26-0dc4-3b45-b311-1260fca381a2 | -22.10476 | -48.45385 | 2026-04-23 04:00:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4551cbe4-e35f-3d26-99c0-77e439bfde3b | -20.20048 | -46.90131 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9bc417c0-bce1-3ae1-99b6-b6609795c5f8 | -21.33221 | -47.07588 | 2026-04-23 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4ead5b9-ea71-390e-8a59-484c1813d2ca | -20.39497 | -42.82265 | 2026-04-23 04:00:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12cd507f-a92d-322e-a5ce-9d31695ccd82 | -21.4 | -48.67578 | 2026-04-23 04:00:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffcded1e-ec23-3024-8df4-18af4d6b8de0 | -22.96991 | -52.69676 | 2026-04-23 04:00:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1442ad1e-eee7-38b9-b4c2-f7fdff745f62 | -20.24113 | -46.79612 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5d3a782-228a-3aa8-87ab-4d9b878dcc02 | -18.2752 | -52.88982 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d48ec80a-f16f-3055-8d34-c6bd995e9fd5 | -20.18443 | -46.89758 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ea7a90-6f9c-3b6e-a5a8-83be3ef934a8 | -20.24033 | -46.80035 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdb7b6d-2530-3d95-badb-591f187195bd | -20.19498 | -46.90823 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7aef411-326a-3dbd-a812-959cd08bd5c8 | -18.27589 | -52.88974 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f97834a0-4e25-3a25-8041-dc1d44c22fe7 | -19.97881 | -44.85513 | 2026-04-23 04:00:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace25988-abdf-3258-81b8-0337bd78eabe | -20.18069 | -46.80729 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db49d76-cf9a-3499-b9a6-aceb40afcf6a | -21.04986 | -48.67064 | 2026-04-23 04:00:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2165f931-9d10-3b4c-a9f8-a59b1eee3b75 | -20.1775 | -46.80219 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d35c77c-4ac6-3d4c-b578-9e947744d42f | -20.17365 | -46.95425 | 2026-04-23 04:00:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aba18ec-40fc-3645-8484-e27e89942add | -22.10905 | -48.45476 | 2026-04-23 04:00:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c4e3dcb3-ac99-39bd-85b2-ba2b9ec4243c | -20.39558 | -42.81888 | 2026-04-23 04:00:00 | NOAA-21 | ORATÓRIOS | MINAS GERAIS | Brasil | 3145851 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e514d8c-1a57-3631-b25a-739643b1d407 | -23.32692 | -50.12777 | 2026-04-23 04:00:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6d58225-53ee-30cc-b0ed-2419b69ff43a | -21.33151 | -47.07953 | 2026-04-23 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 666d888e-88aa-3c94-b2b6-ad2d5a9011ac | -18.28305 | -52.88621 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a938bae-a4e3-3690-a063-fa1c48c59360 | -20.23799 | -46.76845 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45db4037-fedc-3f97-90d0-724e2e622a1b | -22.1056 | -48.44957 | 2026-04-23 04:00:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 24e0ba1e-222b-3396-a000-14692ff87e54 | -20.18697 | -46.90623 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a6ade78-2b5f-38f9-ada1-fa9d2bcd72aa | -20.18366 | -46.90159 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53aaccb1-ac52-364a-a1be-5451ef5e0507 | -20.1726 | -46.93773 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a239a935-a42a-3d3e-8278-c45d92192c0b | -20.20192 | -46.8937 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e382a7-d528-3ca1-90f3-8cca0a898e04 | -18.26301 | -52.88738 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 778b2d97-a814-3158-8969-dca173b22bae | -20.23393 | -46.7901 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aaf188b-1260-35b9-9b5e-e62d279601b2 | -20.23318 | -46.7941 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9acefc4-b8ef-3a1f-8a91-97aee08f9a07 | -20.17977 | -46.94417 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd70e963-e968-37aa-983b-8df7219a257a | -27.94465 | -50.20401 | 2026-04-23 04:02:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0fffb551-3a07-3b89-8bf3-8e6c5e5e77f8 | -25.16018 | -50.19736 | 2026-04-23 04:02:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 58e76131-dd3f-3cfa-b304-52be2647742b | -24.95629 | -49.63451 | 2026-04-23 04:02:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 458d6899-2b3a-3d57-884a-1a27dd55f473 | -27.93761 | -50.20417 | 2026-04-23 04:02:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ffc3d4e1-82ad-3a98-9ce8-0c41d3c4c526 | -27.94187 | -50.20523 | 2026-04-23 04:02:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| be66b1f2-ecfd-347c-bea4-7e5282976e0f | -27.94368 | -50.20864 | 2026-04-23 04:02:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e28a886f-4448-33cb-8418-249f84a2858d | -27.93615 | -50.20192 | 2026-04-23 04:02:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 2d9991b0-ed5d-3154-9dc5-43a01836742c | -10.00621 | -48.66775 | 2026-04-23 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05153270-fa6d-3731-ad9b-a4df03c1819e | -8.78681 | -44.83239 | 2026-04-23 04:27:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bd15e48-5d5f-390a-a48e-c7bda42960d6 | -10.00481 | -48.67597 | 2026-04-23 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 366b445a-56ac-3041-b40f-d6abbc9204c3 | -10.00823 | -48.66952 | 2026-04-23 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8d086f5-d2e7-3933-9c25-bd445c1ad330 | -10.00328 | -48.67715 | 2026-04-23 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db319365-72cd-3d00-9cdb-1ae8f69f78c8 | -6.04007 | -44.23376 | 2026-04-23 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b332ec8-7040-36dd-b792-ef79e891c4fa | -11.7814 | -43.62114 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf66ab1c-728d-33af-9219-fa9af56850e2 | -11.76278 | -43.64763 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1bbdd75-717a-3446-b0be-acd4fd53fe21 | -11.77559 | -43.66055 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b385a4c8-157c-32fe-a350-2b64d485ce86 | -11.77675 | -43.64983 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6fedc08-9e25-391e-9bfd-8bfc7ceb4dc3 | -12.24091 | -44.18782 | 2026-04-23 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2fa58f-739a-3549-ab2b-011569058d7f | -12.56969 | -45.47628 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0011e115-4801-3753-9479-223635621fc3 | -12.58593 | -45.47175 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f8df1ca-d6af-366f-9d78-f8b3f7966e28 | -12.55523 | -45.48125 | 2026-04-23 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a5577c6-b4a4-3d3a-8bf4-c48b653d8b96 | -11.77909 | -43.6611 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 052c1625-9207-3d1d-b79d-c3eb6d251ad8 | -11.77095 | -43.64088 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a987b0ed-481a-38de-b804-ae54d843e3c9 | -11.77325 | -43.64928 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61dff42d-6d07-34f0-be4e-319a2d66f3f3 | -12.28396 | -44.61886 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e07218-a921-33d9-8e2e-2ad96dab16ca | -12.27974 | -44.62261 | 2026-04-23 04:29:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 764c6b7f-f2ce-35a4-baef-80b4eeecff22 | -11.76917 | -43.65266 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6acb3b68-2628-3d20-9009-c938bd25e833 | -11.76337 | -43.6437 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58e09c22-1ea9-32ad-961d-0a7686025a57 | -14.09772 | -47.21007 | 2026-04-23 04:29:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4514f4bc-b71d-3b1e-931b-2eb93aa4310a | -11.78957 | -43.61435 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37e2b086-b6fa-38ce-96f5-a7fe99e7ece6 | -16.75629 | -44.02132 | 2026-04-23 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72feca40-174d-3ac9-a923-060f7aa09d53 | -13.00332 | -55.97717 | 2026-04-23 04:29:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8305016-b0dd-3c6e-bf48-47eecb62c9eb | -11.7884 | -43.62223 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43c7d8de-a96a-39ed-a08a-0a7a388e4b92 | -11.79307 | -43.61489 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| beb8fb93-e14d-3223-9c84-5b17aff7fb08 | -11.78444 | -43.62281 | 2026-04-23 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
