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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67b1df09-500d-3487-b660-0ea717c3e764 | -12.8131 | -43.45354 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76c39bf7-ac78-3fd5-80ef-6a2d47a00b93 | -16.20423 | -45.05167 | 2025-10-30 03:38:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c00b923-f4d1-3fb1-809d-454952c430ce | -16.03602 | -43.72788 | 2025-10-30 03:38:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c54774b8-e1dd-339d-92cb-c3844a6c3014 | -14.41123 | -42.65685 | 2025-10-30 03:38:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 921da12b-b0d4-34a1-8927-09edd1c82909 | -14.75477 | -44.95822 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34096a14-cc0c-3b59-8fd3-8c088ed37b18 | -12.70679 | -46.29814 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3aa46e22-f1f9-37a9-ba4e-784353c62926 | -19.91506 | -42.32744 | 2025-10-30 03:38:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 14060543-00fa-3150-9602-66402e4ee4d1 | -13.47185 | -47.99795 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12723a53-8d3a-326c-8d58-ef431aa19656 | -14.97837 | -43.39064 | 2025-10-30 03:38:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 094be2a3-7370-3e94-be7e-aa013d179d98 | -12.81286 | -43.45185 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531c74d9-11f2-34a9-b3ab-fd79db7df3c5 | -17.14412 | -41.93421 | 2025-10-30 03:38:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 173ad2e5-5764-377b-a1ef-3ef830d5116e | -11.86921 | -46.75563 | 2025-10-30 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22afb585-a8c6-3a80-91e5-5f2596aed587 | -13.441 | -47.37114 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b7f492f-428e-3f25-9614-04cd719612c4 | -12.8329 | -43.45576 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f9a6ba4f-65ea-3902-bff6-b1c8d244c989 | -14.692 | -43.15368 | 2025-10-30 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 768b9a9c-10ea-36fb-b124-a07fdfa94ccf | -13.88479 | -43.93633 | 2025-10-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 636624e3-db49-32c5-9a8c-cca11d7dbdbb | -16.81446 | -41.22839 | 2025-10-30 03:38:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad788038-c1a7-3cd1-af8f-805583d48213 | -14.75872 | -44.96629 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2ae0336-975e-3e9c-b6b9-1399da5566e5 | -12.88216 | -48.64059 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fce657bd-1297-3543-85ca-53a45097aa3f | -13.46404 | -48.00245 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 935e2872-367a-330e-8d93-648fd91c76ac | -13.07588 | -48.20807 | 2025-10-30 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8eb9f394-f890-3318-b81b-516a540001df | -13.52253 | -47.34012 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4891aad-f3a4-39e0-a593-64a9332bf96e | -12.40161 | -46.82409 | 2025-10-30 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b23651fe-b971-3c8d-97ab-97657d0e6387 | -13.31888 | -47.47933 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 538bc394-5b79-3ad6-8e33-c61edb9e8e35 | -19.33418 | -43.06562 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6b88d922-3975-3514-bafe-9029cdf1a49b | -16.82691 | -43.10933 | 2025-10-30 03:38:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53d72aa4-e91a-35c3-888a-7242de50ac6a | -12.91413 | -43.19279 | 2025-10-30 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2a9a11c5-d4c1-3284-9b8c-847ba4d49859 | -13.32503 | -47.47499 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52b22ae4-0853-34ca-9906-9553060d3894 | -16.16158 | -42.31481 | 2025-10-30 03:38:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b17c942d-9176-365d-84e9-cd0baf17063c | -11.8703 | -46.75029 | 2025-10-30 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbc16f96-7c80-3124-a7fb-19d43367a18f | -16.59212 | -43.51782 | 2025-10-30 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ca5450e-d060-3f9f-a204-ab76f2b3e116 | -13.71702 | -48.7653 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 802d0e09-a4c7-302f-bb54-6996e4dc2c49 | -12.81787 | -43.45282 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0058bc2d-513c-313b-a269-60de9484b4d8 | -13.43145 | -47.3655 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91f1919a-4da6-306b-ade6-eb8ad449c1c9 | -13.42506 | -47.36448 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65f23dc9-4fb9-3b03-a8c2-3c44d99df436 | -18.24858 | -42.6274 | 2025-10-30 03:38:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| acfd8d29-61ce-347a-9e33-b5dce3241d6d | -12.81729 | -43.4558 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5793b1ba-84d9-3be1-ab54-87ed8aa0fc34 | -13.35953 | -43.08513 | 2025-10-30 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ad12a83a-16de-3eb9-b856-a45f73e5eb91 | -13.98761 | -44.02208 | 2025-10-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da00fbfc-0192-3d7f-9454-1d5ca1f55551 | -14.23447 | -44.31961 | 2025-10-30 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58bd5d81-4972-3c9b-b606-b3b055bd53e8 | -18.04347 | -43.14825 | 2025-10-30 03:38:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 12a2ded0-6836-3c9f-9f6b-a95387e96a3a | -16.88765 | -41.99886 | 2025-10-30 03:38:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bdae9a04-b8d6-30c9-9322-1c902e61dc76 | -18.54206 | -41.58558 | 2025-10-30 03:38:00 | NOAA-21 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f87e7674-e320-3887-8545-4a5a7256d66d | -17.38273 | -41.03279 | 2025-10-30 03:38:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0023219a-1dba-31f2-8518-405b815b748b | -13.36332 | -43.09163 | 2025-10-30 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1f02bec-ff1b-3fc4-a799-fcd7f86db039 | -14.7204 | -45.10199 | 2025-10-30 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 329f9786-fe01-32db-af8f-26334fdc5030 | -13.9882 | -44.01897 | 2025-10-30 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ade87ebd-a924-3de2-8137-b8a7e5466dec | -12.83347 | -43.45279 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d061f257-7e28-3826-8569-044c0811a74c | -13.52957 | -44.34073 | 2025-10-30 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 555bbb2b-0cd0-3666-a36e-17cebb975a7a | -16.20423 | -45.05077 | 2025-10-30 03:38:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a2d2d6b-9e52-3523-b441-5d478953022a | -17.96438 | -44.07988 | 2025-10-30 03:38:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f68fe47-9b8d-3380-8fef-5ce4e2e68dff | -18.35247 | -42.24205 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 57ea1eb7-0c60-3391-aa60-523d2a50bebf | -18.56554 | -42.40977 | 2025-10-30 03:38:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83e246d5-878a-3265-a333-630f39873129 | -13.92957 | -42.37389 | 2025-10-30 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 33a9ebbe-0ed5-326e-ae5b-a78a984dd67c | -16.60381 | -41.90425 | 2025-10-30 03:38:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 46038ca3-a028-3e49-899e-9c58453a94c8 | -18.23133 | -42.37608 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 13be6265-bffc-3875-9a97-d7d4f87bcab4 | -12.6075 | -43.19874 | 2025-10-30 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d094ddd-b6cd-3699-8411-359d20084d76 | -14.71556 | -42.44954 | 2025-10-30 03:38:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ea1778d-4932-39b1-b906-8848e02e9a05 | -13.07461 | -48.21399 | 2025-10-30 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2afdf5a-2f6f-3f98-a759-cf3a651d2c6f | -12.68843 | -46.32642 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b90a106-00c8-3c25-8b5b-0a4772e36bc8 | -12.39538 | -46.8228 | 2025-10-30 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3902e617-683c-3c09-be4b-5da4ce16f0b0 | -16.05123 | -41.47477 | 2025-10-30 03:38:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b4fa4d20-68a6-30d3-a8ff-ed7bc53a3c69 | -13.41354 | -43.74512 | 2025-10-30 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ef7e132-71c8-397b-84a1-52b61994a1be | -18.04707 | -43.15363 | 2025-10-30 03:38:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ae37a47-2b1b-3f8a-a8ed-ccb9502e7557 | -14.31936 | -46.53648 | 2025-10-30 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb71744e-87c5-3f45-8999-f6b222a10d27 | -11.84933 | -47.92735 | 2025-10-30 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca836367-cc63-3e2d-a7c2-565215912a68 | -12.7065 | -46.29111 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 404820be-1a9e-39a3-9628-587a5a89a20e | -13.2974 | -47.06998 | 2025-10-30 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15009775-c0fe-3c6a-a5f6-595e56b78987 | -15.58895 | -43.15641 | 2025-10-30 03:38:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 224acb97-0664-3a65-bb52-34daee24dc7e | -14.57611 | -41.14536 | 2025-10-30 03:38:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37240aae-615a-31b9-bde4-64ca44793b99 | -13.48111 | -40.40932 | 2025-10-30 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 78cb08ec-53f5-3a57-85bd-5bb89ad37452 | -13.29809 | -47.06672 | 2025-10-30 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202087a9-20ba-39f9-905f-752959ff4579 | -16.83561 | -40.99633 | 2025-10-30 03:38:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9fb74b6b-f869-3563-b2cd-ee5a6e544b4b | -14.31441 | -46.53049 | 2025-10-30 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91446fd9-e943-3184-a782-13d303521480 | -12.1896 | -46.70959 | 2025-10-30 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6db18281-ad10-3ac9-ad12-ca2e6cb04b1a | -13.20254 | -44.4866 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92b6e1ff-d655-3a28-8a89-47aaa4df3162 | -13.60124 | -42.5114 | 2025-10-30 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35e77e8d-bc92-3907-9803-79537c77a853 | -15.32956 | -43.1077 | 2025-10-30 03:38:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81ef1594-d5be-3097-905e-7eb53845c9c7 | -17.01822 | -41.85905 | 2025-10-30 03:38:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4042fff4-406f-3eb1-adb5-971bce1e791d | -12.58153 | -44.97272 | 2025-10-30 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71009a13-a4ff-3d05-953a-75dbf27c0744 | -13.29984 | -47.06936 | 2025-10-30 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ad80879-8515-351c-8d89-f885360a09b2 | -12.81255 | -43.45652 | 2025-10-30 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 134354be-62d8-3d5e-a293-6f1041cad371 | -18.71058 | -39.84818 | 2025-10-30 03:38:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0e5d08ad-d532-38cc-b917-477663b0aa04 | -14.13204 | -44.07101 | 2025-10-30 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4d5a962-fa3d-3898-b0cd-c79cfc5f1d41 | -12.70794 | -46.29254 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 903badea-e03b-3e50-8e6e-4d1d37af82bc | -19.3351 | -43.06094 | 2025-10-30 03:38:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5bb8ea08-9ca4-3582-af90-032feaa467be | -16.68052 | -41.36639 | 2025-10-30 03:38:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 32ee044b-d53a-37c9-ba36-636c600edf68 | -20.0313 | -41.45486 | 2025-10-30 03:38:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7085f0dd-b61f-307b-9da9-bf8cfd88b9cf | -16.68465 | -41.36688 | 2025-10-30 03:38:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| afb63421-c70f-3dab-b745-e4feccbc4acc | -13.7194 | -48.75438 | 2025-10-30 03:38:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d823b96-983e-306c-bc4d-c2e0cf953134 | -14.39234 | -43.71879 | 2025-10-30 03:38:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1320b8e-35b9-3f92-83fb-053f076d5143 | -14.77266 | -44.97997 | 2025-10-30 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f5a7683-4683-37f1-9810-58500af6549a | -13.51823 | -47.32915 | 2025-10-30 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2a6da20-772e-37ba-a140-73f08fb938f5 | -15.58635 | -43.15787 | 2025-10-30 03:38:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e37673ef-c0ba-3ab7-807b-6a7d2c574f2b | -13.99086 | -40.44262 | 2025-10-30 03:38:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3007be6d-41d5-31a3-b14f-cea3b4388d65 | -12.71275 | -46.29964 | 2025-10-30 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ce120ad-5118-384d-9b29-0fbbb511a142 | -12.84921 | -48.6277 | 2025-10-30 03:38:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da3630ad-9fe7-30fd-93f8-f01fc14b0598 | -17.85164 | -39.65964 | 2025-10-30 03:38:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 554a97a7-95c2-3058-ac5a-3c3477a11b1f | -15.06676 | -41.97581 | 2025-10-30 03:38:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7344b732-68e4-30d7-b9c7-0725043e3ad8 | -13.11579 | -40.22559 | 2025-10-30 03:38:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
