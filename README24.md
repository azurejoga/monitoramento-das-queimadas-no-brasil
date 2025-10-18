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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49574189-94f4-3b7f-8c98-f51b9972e274 | -13.73652 | -48.11827 | 2025-10-18 04:02:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd4735a3-59bb-31d9-9b25-3aa0c6408b6b | -11.36298 | -47.29672 | 2025-10-18 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d5f4ceb-3488-3616-a813-3603a5899c89 | -13.04224 | -46.95221 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8849a9f8-8703-3df8-a05a-02ef00016f67 | -11.35222 | -44.20845 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de8d3b2e-1329-3fc5-b7d5-f5c4bfb22a78 | -7.9568 | -44.11927 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0381d862-0cdd-344d-9a80-af7202c2a403 | -10.24394 | -44.04419 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ea7fc32-06da-3737-a709-99f28d15f6be | -9.55562 | -47.77488 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5386805c-4307-3466-8726-21c6ed6498ba | -11.00352 | -47.89983 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f95ea00e-698a-3bb0-aadb-34c30f5b592d | -8.21074 | -46.93106 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b9a7d4-6374-386f-a688-ee29123e9122 | -10.25548 | -44.04171 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c37b4d62-b2a1-32b1-a48e-38a12be6bc1a | -10.24262 | -44.07479 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb49828f-ae2a-35de-9eb8-2888b9e19dbf | -10.49061 | -43.42931 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ab052e02-6051-321c-b534-5547ecc9d04e | -10.24755 | -44.04476 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ecd68f-a056-3d8a-8d58-b0144531104b | -11.37696 | -44.30387 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b273fb4d-4180-3134-8589-099315be4715 | -11.48764 | -44.16136 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e2a9125-9328-3510-91f4-5bb395df1daf | -10.15208 | -44.53127 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a028e766-30c7-3d00-8c1c-0412600def92 | -10.62428 | -42.30848 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2438e014-c037-3ded-af20-53da0e0bf18f | -12.49017 | -45.50138 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64f98a5d-8e2b-349f-91fe-1d792313bce2 | -11.47918 | -44.0153 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00effa61-1c46-3f6e-b769-4030636a5814 | -12.4593 | -45.4764 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc7b523b-55de-3b3a-865e-399e8ae7d0c3 | -10.74736 | -47.28943 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ba763fb-2284-3d18-a0e2-2a5842985333 | -13.04092 | -43.80724 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc1e2ff9-41c0-35fa-8c2a-9aafad03c115 | -11.35787 | -44.17493 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89896db9-049a-314e-bccd-a05332314ab5 | -7.822 | -40.20676 | 2025-10-18 04:02:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 957a1a04-f4c9-3b7a-83f1-b07bc28787d1 | -10.42049 | -47.74832 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18faa6dd-1edc-3265-9720-0e1db33b25aa | -10.48645 | -43.43271 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ece0c372-f555-3034-8851-31c565c844fc | -7.76311 | -42.48812 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 632a3c64-3a8c-3534-b49f-f2c285b70af4 | -10.49781 | -43.45094 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3185442d-9420-37e9-9a57-34d27a0d16ad | -8.20736 | -43.3068 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| abfe11e3-ecc4-3879-b400-f68e45ab3943 | -13.1918 | -46.43984 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0157c41c-2069-37aa-9617-58826aaea0c4 | -10.6239 | -45.23784 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94305eff-0319-3ea1-b81a-afcfb389e0bc | -11.58249 | -44.04878 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b007904-4232-379b-8a14-de8eecebfddb | -8.39047 | -46.23445 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3ca39403-d7bc-3dbe-9d8d-8b013819ea4b | -7.46364 | -42.16496 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 750f46ef-759c-3f9b-8d8a-5db3c59e777e | -11.36826 | -44.2893 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 593e0568-73b8-3eee-a26a-6808818cc8ce | -13.513 | -48.00147 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6787bb2a-4eb7-329c-a845-25a46fa77e37 | -11.51863 | -47.7421 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f26994b8-8a76-3476-81cd-aae7a15e0f31 | -10.1149 | -44.54809 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb061006-1f75-34d1-9221-2d9523d5d638 | -11.61035 | -44.07897 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ca58263c-02f5-34db-a23f-cea480c7e53d | -13.45728 | -43.76115 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc72523a-fdb7-3263-b664-835dcb1f1af0 | -10.95429 | -45.44823 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecf5e378-9784-30d5-89af-9e4874c73626 | -10.78985 | -44.09177 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0770551c-d93e-3f9a-a17c-6bc5a8891e5a | -11.47675 | -44.11675 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0bae2cb-e864-3a5a-847d-596461471fb0 | -11.25529 | -43.21075 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ac3e37c-6fa6-33de-a3f0-e6f35edc346b | -10.68814 | -44.55921 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e07b7f4-8a26-31e0-85ff-5e473db42be7 | -13.50848 | -42.51803 | 2025-10-18 04:02:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e351a33-0235-327b-aada-46a1d47a3a28 | -9.19419 | -46.87063 | 2025-10-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6b8852b-2cb0-3f2f-94c7-66e8fbe610ca | -10.12758 | -44.54085 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cda744d-b713-3b98-abdb-7a803009514a | -10.7466 | -47.29373 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a34b53e9-dbd5-3dc6-9316-e89f452f28b1 | -10.62856 | -45.2337 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cd0ffb0-5a7f-3ecd-8ff2-0e7d6cd4c46f | -10.64386 | -45.30602 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdb38ee6-6c15-317e-aa31-6e0e9e61f730 | -9.13375 | -46.61722 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dc6a056-798f-3672-841a-4695b8eda8ba | -8.3049 | -43.39759 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25ba72de-33c7-3e06-9303-44c47355d0e5 | -13.46255 | -47.97812 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d2f1db-b37e-3e43-a5af-f34613d05171 | -11.36371 | -47.29266 | 2025-10-18 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab82e3a9-2861-36d1-9d76-c0c531d466df | -10.53105 | -44.50734 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0106673-4d0e-3242-aa8d-c93524abaf63 | -10.25464 | -44.03241 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbbf8a37-f08d-3f9f-81ae-c5d52e7ddea6 | -13.20159 | -46.43067 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a9ffb01-523e-3f97-af51-07b759ad2450 | -8.82694 | -49.68128 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc567d62-f474-3b32-8599-3f9aed64ccc8 | -9.7561 | -43.95478 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3668ca8f-aaa4-3b91-a509-b3c348a4974b | -14.39346 | -40.77666 | 2025-10-18 04:02:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e701561b-6079-3950-b21d-cc8e93926431 | -11.35232 | -44.25179 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbeac20c-a580-3e3c-a364-c2727b3abc88 | -10.49411 | -43.4299 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2b4679e0-b65e-341c-9195-5e3c8b319553 | -8.30132 | -43.39701 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 03d22d5d-ce2d-3991-a6d1-3919b39b287c | -8.61667 | -40.19899 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9066549-244b-32e1-82ec-a6b03b97fb00 | -9.65009 | -48.72224 | 2025-10-18 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44c3412-c845-369f-bde6-18f49c04f0a8 | -8.64699 | -47.08009 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7671394-2f0d-3ac2-9420-1b1133f59eea | -6.89769 | -45.45109 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00a48a15-3abd-38d9-aa81-14aab393936c | -10.46488 | -44.12204 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70e364e6-50a0-3aba-a49c-dbeca26ae177 | -8.38408 | -46.24611 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1581596-6a05-319d-960d-ba6edf279b2a | -10.71186 | -44.54785 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4895151f-f6b0-3f62-a1e2-5458ee7a2532 | -10.71541 | -44.55489 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3fa82a5-8d01-3995-9e8d-3b7c3064c347 | -10.4898 | -47.73365 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88fc9061-3c81-3e28-a349-2b01deaddd04 | -10.68371 | -44.56304 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9b8fc0f-b11d-39e7-9425-d127f21e97a0 | -10.23737 | -44.03904 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98b70656-5862-30bb-87a6-3427f3b3b05f | -11.37604 | -44.24282 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f45269-b0b0-3cb7-a0b2-dde561e1c49f | -11.36537 | -44.28445 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd7bf420-fc28-3847-8553-f96ec4c82705 | -12.31296 | -47.83653 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267297c8-c70b-350a-9ba9-66a8f46d7b78 | -10.26257 | -44.02942 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f770b102-98a0-39ef-9c98-f716aabf76f9 | -12.19351 | -39.77937 | 2025-10-18 04:02:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| abad24c6-497c-3a38-a1a1-c0e9d0f173b2 | -10.10443 | -44.56482 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 033429b0-9fd0-3100-a99b-a35f9798e9dc | -13.76047 | -48.23632 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a04b483-00ef-35b9-99ad-dd51cc581e22 | -7.82066 | -44.12264 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83dc9e16-fa29-3ebb-af63-8fe498c7e82a | -11.36294 | -44.18871 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f593cfc-54af-3c62-a8cd-aee846dc8026 | -9.75249 | -43.95415 | 2025-10-18 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b47329a9-de99-3ab0-ba2a-208502f40960 | -7.3646 | -44.22505 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96f4fadd-9b23-336c-8627-b98cae587caa | -8.82754 | -49.67793 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aee81361-1c9e-3648-9c21-de4e2b316ad4 | -11.44965 | -43.47652 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a7411ce-bdec-3c1b-b5a2-230edc959046 | -10.18754 | -44.53678 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66b3ffd5-c460-3961-b412-a7be68a2c17d | -8.24335 | -44.01452 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64796b77-bc72-3a26-ab2a-35cbe8dc960a | -8.19903 | -43.96185 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05d9786b-f3d0-3b52-96af-1346d9b27231 | -13.00618 | -43.85387 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bfe5ff6-6891-39df-9673-a9285ce8675e | -10.84392 | -43.9463 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e7f7a64-be98-39d1-ab57-56e099d1a587 | -6.94043 | -43.69257 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4bddcdb8-a49c-32dd-8707-ff8679077e6e | -10.50714 | -43.39475 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6d075d7-de1b-33a0-a5d0-ba816a06b1eb | -10.25036 | -44.05764 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8efec8c-f787-3bb0-b252-7465d2b5b32a | -11.47849 | -44.0194 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ca48788-866c-3a8d-b2bc-1fd4a7fe6f10 | -8.1138 | -45.43435 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a00c3c2-d154-3158-9214-d37a1f68d76a | -6.98969 | -45.20285 | 2025-10-18 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5ab84d5-e25b-30ed-9c2c-dce71072600b | -8.20101 | -43.30684 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
