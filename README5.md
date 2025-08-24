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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe8781d-8fde-396e-8dbd-712d24d99310 | -13.4743 | -47.0191 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3d1cf4-e05d-3896-9ab3-f72f87942df5 | -23.3127 | -45.534698 | 2025-08-24 00:34:00 | METOP-C | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05cfd644-6588-33ac-a5bd-0360cc02fae2 | -15.0657 | -48.521 | 2025-08-24 00:34:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9fd4c6-fc59-39de-9a0c-825a4ccad15e | -6.4288 | -44.544601 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 009f2f9d-1927-3a63-9edf-7266eb4e357c | -13.0376 | -45.236099 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34a9d856-e8c2-3489-b254-ce300b6d7a60 | -10.4043 | -47.181702 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e30fbf17-c825-3a6c-8623-ff407f6a2f3d | -8.1847 | -45.0825 | 2025-08-24 00:34:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a5ed6dd-5949-3533-8961-2d617b0abfb5 | -10.5949 | -50.174801 | 2025-08-24 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57882f63-d61e-3d8e-8509-9e787d0712ce | -12.7261 | -48.115799 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01a6f03f-2011-35e3-a382-1cf9ad3275b6 | -13.489 | -46.897999 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3e69ae-f6bc-3e3b-b4e0-993b631f3e10 | -6.4356 | -53.370201 | 2025-08-24 00:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac559430-8012-3df3-b4ba-464187747d6e | -8.3115 | -47.2626 | 2025-08-24 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db35651a-202f-3418-a97f-0c2c17558e71 | -7.5935 | -45.248001 | 2025-08-24 00:34:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94d00886-b021-3d16-ab42-f1420ff8e8a1 | -8.7724 | -49.9902 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ef96a1-9fc6-352f-a7c2-c7b611bc0725 | -11.131 | -46.333599 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0baa1aee-c20f-3757-9ad1-05456a93e65f | -12.7226 | -48.099499 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a229007-82ed-3379-91a7-fc4ade1c2fdf | -17.795601 | -40.172501 | 2025-08-24 00:34:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d95ab948-3dbe-3e66-8867-83a7f9c5ad45 | -23.623199 | -46.019699 | 2025-08-24 00:34:00 | METOP-C | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e3d37bb-4bd0-3d6d-a774-4a1903938ffc | -13.4645 | -47.021301 | 2025-08-24 00:34:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b072eedd-3d29-38a8-aa13-72b6b2b1c9d9 | -14.8112 | -55.9589 | 2025-08-24 00:34:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77974f9e-cdd6-37ad-ac5d-aaf5347ea929 | -20.9711 | -42.8699 | 2025-08-24 00:34:00 | METOP-C | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a4f8ee8-e579-3a17-8a84-30d610d527ba | -16.7994 | -51.3498 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57d0ca93-ef8a-3df2-90b3-41e722f6aa2b | -5.7404 | -45.357399 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 058a6aba-e117-3631-baf0-1ebe6aab6f2c | -14.8066 | -47.9198 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 78f0bf9d-fc1a-3ec7-9401-bc879843cae4 | -8.1101 | -47.146301 | 2025-08-24 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44da9821-e5f0-3db1-baff-7b65933e770f | -13.0555 | -45.224602 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39983e93-637b-305f-a524-9a386fc6362e | -8.1749 | -45.084801 | 2025-08-24 00:34:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f485a634-7f3e-3a26-b8f6-11c1a3696724 | -8.0409 | -44.995899 | 2025-08-24 00:34:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| acc4e918-5beb-32f1-8ed4-ef9ee162750f | -13.4644 | -44.075802 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3eaa748f-8c89-3feb-b8e8-a4e1eadf159b | -15.2393 | -43.8493 | 2025-08-24 00:34:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8da0f8bc-df15-3349-872c-37952699db64 | -10.806 | -46.399899 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68f546af-7581-3335-9ea3-2438c6394f3c | -20.3606 | -51.679199 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 423c0112-354a-3e5e-a293-9a1f1a2e8d5c | -5.5756 | -45.804298 | 2025-08-24 00:34:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaaeed51-ab48-3e7a-b800-7918de3e4c32 | -6.6109 | -48.034401 | 2025-08-24 00:34:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7f81e5-ecb9-3572-aea8-5197ebe4f91e | -19.627399 | -43.179699 | 2025-08-24 00:34:00 | METOP-C | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b11c271-7fc5-3dad-aea8-5ad6210814d4 | -11.519 | -51.856602 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e66ea28f-fe53-32ae-80c1-c5010eba0171 | -8.845 | -49.899601 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2185e3d8-b7bd-300b-a14e-de9de4be9599 | -18.7528 | -45.1045 | 2025-08-24 00:34:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 789b66cf-59ea-3bdd-b467-40e2be459d89 | -20.357599 | -51.662102 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3037dd-75c1-3ac6-91ca-ed8b167d8e53 | -20.691999 | -42.317101 | 2025-08-24 00:34:00 | METOP-C | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f72541c-9423-3972-9ddd-ab63dd628063 | -22.299999 | -47.609299 | 2025-08-24 00:34:00 | METOP-C | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 841aa21b-e940-3c8c-9e14-422ec85617ca | -4.7818 | -45.317699 | 2025-08-24 00:34:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9289a25e-4ae1-361f-b1e0-4170969191ed | -9.8216 | -47.7542 | 2025-08-24 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec36d9d-f24b-391c-98ec-51b5c599f6fe | -5.6626 | -45.155201 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55faf056-0693-32e7-86dc-b2697a7e1651 | -5.957 | -52.206699 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0f2250-8645-31c5-ad4a-df23334bda25 | -9.8232 | -47.7616 | 2025-08-24 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a806e0cb-a0dd-3840-918e-180da69a37e6 | -11.1059 | -44.771301 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84595b46-5dc4-32f9-89fd-afa4e67eec72 | -17.5994 | -46.097801 | 2025-08-24 00:34:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 467533eb-5b0d-3e0a-bcbd-9eb871099630 | -7.6229 | -45.241299 | 2025-08-24 00:34:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8be6c897-8917-3537-be42-f60e43b8766b | -4.9678 | -55.8074 | 2025-08-24 00:34:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6b3c45-75cd-3baa-bee9-1f0cc015c42d | -11.1408 | -46.331402 | 2025-08-24 00:34:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0bdff1c-9a41-3e85-ae56-f8a57637007e | -7.3513 | -43.854198 | 2025-08-24 00:34:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a652655e-9893-35f3-92e3-cf1d6a5e7f96 | -3.5974 | -47.5205 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487391bb-7d92-35a2-a38d-1e388ff90947 | -13.0474 | -45.233898 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 584af464-3063-3346-8753-5d35e0290a50 | -14.8084 | -47.9282 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3687463-38a8-3541-8f30-a3ebf55a6521 | -10.5929 | -50.165001 | 2025-08-24 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec6ac2ec-01cd-3b44-8a9b-d866549b7e0d | -11.5393 | -51.905998 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e64df02c-2ae5-3329-abd3-1adfd61ebbc5 | -8.7627 | -46.751598 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44ba783d-d475-3f4c-bcec-c57c480a36d3 | -14.8257 | -55.984699 | 2025-08-24 00:34:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69b4ae73-9522-3b23-9b57-3aa69d6be991 | -20.959801 | -42.865002 | 2025-08-24 00:34:00 | METOP-C | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9df59047-0b53-325d-8e2b-1f5f3c9d4f1d | -14.7986 | -47.930302 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa64789-b205-3de2-be03-0a6129f89d10 | -3.4359 | -44.144699 | 2025-08-24 00:34:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91584599-615c-3deb-8c34-c96d01bf47fd | -6.1901 | -45.427299 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 741f0ad2-3cb0-3d2f-92b3-554d86c0d1ad | -7.6212 | -45.234299 | 2025-08-24 00:34:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc4619a-ed1d-3667-a751-81b5cb11917b | -7.0214 | -44.6511 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72a3e12f-88e8-3e3f-ac00-198fbed75ea5 | -7.6973 | -42.1343 | 2025-08-24 00:34:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2bb150e-53b1-33fe-81bb-5614c2c23554 | -6.1933 | -45.441399 | 2025-08-24 00:34:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24abe8fb-32ef-3325-a570-d046be1d5314 | -20.3636 | -46.731499 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 77f9c4c8-d6b5-3128-bc48-6044e9f699cb | -10.5333 | -47.1604 | 2025-08-24 00:34:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51bc12c7-8091-396e-9491-3162cebdf57a | -15.7015 | -41.928101 | 2025-08-24 00:34:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbffbd29-ae0d-38a3-b8c4-c9a288ace63f | -11.5224 | -51.923 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09fc1607-eabd-3362-84e3-9d633ea1a77e | -3.7347 | -48.935101 | 2025-08-24 00:34:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8331b2-feb9-3971-9126-2f1bc5decb25 | -3.5142 | -47.202702 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7536f850-fe34-3f7a-90a0-ded021bd3e5c | -20.355499 | -46.7425 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b04476c8-fc72-3097-82f6-a10e22286a50 | -22.065201 | -53.7705 | 2025-08-24 00:34:00 | METOP-C | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 367310d6-ee19-372f-b078-1940e9de221f | -20.3671 | -46.749001 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8863297-177c-3f8e-a397-a94a7b25bef8 | -12.7244 | -48.107601 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f76d9ce-da39-34f4-9576-239ece4ff5af | -8.7498 | -46.739899 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bab63a7-f251-3f34-a499-bd3547ae99fc | -11.3111 | -47.841499 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4fc835-a1f6-3060-bba1-c4044969115a | -11.3128 | -47.849098 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8ce3f7b-1fbf-34c1-83f3-888369abeea3 | -18.761 | -45.094799 | 2025-08-24 00:34:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5deada6a-f14b-3274-8e73-596235f93d4b | -18.6996 | -40.0112 | 2025-08-24 00:34:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee7c38c0-c438-3387-99e3-ba061eac1afb | -13.0442 | -45.219898 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 179a6d0f-ab07-390b-afa9-ff9499305291 | -3.5126 | -47.1959 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24213895-c50c-3edb-a682-9847da510a59 | -2.9367 | -53.686501 | 2025-08-24 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 898f44c4-0aa8-38d0-b8a9-5705b5b19f7a | -6.5862 | -44.555698 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec50c90-1916-3163-9ea4-69be79c8f6ff | -11.5164 | -51.8438 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2a45bda-1bf4-3029-945e-4c032ccb7cbc | -7.4267 | -45.419601 | 2025-08-24 00:34:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3de378f2-e91b-3546-b835-33b057ef10b1 | -5.4998 | -47.497799 | 2025-08-24 00:34:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b57cfe-6d5b-3006-bd17-1e8b3dfdadaa | -10.2976 | -46.7505 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64842f19-7860-3173-b659-1f82b4f3d647 | -18.7642 | -45.1096 | 2025-08-24 00:34:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 073b59d1-8a8d-334f-a27a-422fb61759d5 | -4.9637 | -55.788502 | 2025-08-24 00:34:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f35dd4f2-95d4-3bf4-8aea-fec9d686981c | -8.1183 | -47.1371 | 2025-08-24 00:34:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b3e3d73-9404-3c83-ac45-901658e4b5f3 | -11.326 | -47.862202 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6bcb6c-6d34-300f-8ce8-56181dbdd581 | -10.7993 | -46.416199 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03395af6-df97-37b0-86ed-5ccbd95bebc4 | -14.8063 | -55.931499 | 2025-08-24 00:34:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a2ef938-4465-3e1c-b9a4-8d789460ccd5 | -10.6104 | -50.151199 | 2025-08-24 00:34:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7768498e-bf99-3229-9263-b0300f11259a | -11.5366 | -51.893101 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1617cf94-4fc4-38ac-9a2a-1b92f2a6b1b8 | -12.7279 | -48.123901 | 2025-08-24 00:34:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed9d0792-ccfb-385a-baca-8594b9c78262 | -20.365299 | -46.740299 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
