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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80d506ec-3ecc-379f-94ad-4e751e44878e | -8.23672 | -49.54456 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc935b6-4bf6-3418-b711-cdcfe54cb9b2 | -11.97745 | -51.00992 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6287dfef-43f8-3847-8a59-d9431f71efa7 | -11.15208 | -48.3553 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7ff24ab-39c7-3b0c-b397-a72c7457c8f8 | -8.05166 | -48.65332 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b14a08d-198a-39c1-835d-44eedd6653a0 | -12.61515 | -56.96443 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 439f8f7c-e45e-31ca-9879-ab8349177706 | -13.8289 | -46.23162 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d83cc41-d1ee-379d-bfec-60b31c94311c | -6.27833 | -53.42132 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6084b1bd-8c74-3d73-b061-40eedbdf1f4c | -13.01323 | -54.8187 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20c206f5-3bfd-304f-acc0-524a32389479 | -7.71286 | -44.74181 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac1f1662-88df-323b-8955-dcbcc30d9430 | -11.30714 | -46.49321 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef39605-169e-3f38-a920-89512cf6ea7f | -12.15313 | -43.70754 | 2025-09-09 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b4c1c7a-4e7b-35fe-b88f-a7eeec1d21e8 | -6.72224 | -51.96119 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 380758b7-3785-3e73-afdf-cd17dd81b363 | -13.02031 | -48.02886 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7f4c34cf-9272-3624-8bba-63b953f293c6 | -9.70759 | -46.8221 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3fc96dbc-05cc-31de-97c0-078cf09da4e6 | -11.80993 | -46.76683 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff6409c8-c851-3967-a241-3ab27599e489 | -11.86382 | -50.95322 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e4e11ff-7505-329f-86a3-b3c0a71649da | -12.8308 | -52.93521 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81fc0939-1970-3fd6-a771-17652675b5ea | -6.552 | -54.98746 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8b6a681-93f8-3bd2-adc8-c8ed979d046d | -13.65239 | -46.97504 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c54557f2-8b28-3641-80f8-2a4214cf8444 | -10.02294 | -48.31274 | 2025-09-09 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34e287ad-5437-3aac-8d78-f5e938528006 | -10.17234 | -46.21418 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28565cc2-91af-347b-84a2-56ce1dfb929f | -11.83897 | -46.76326 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 818fed9e-6358-3924-b6b5-1083dc9255fe | -11.36948 | -43.52785 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 151e4c3d-aa4b-38f2-8023-660dea7102fc | -10.75042 | -47.73756 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3fa927c-583b-3aae-962c-03dc5f436f89 | -9.62495 | -48.00592 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f0c226c-4223-34fc-949b-cd35faca06bb | -8.00849 | -46.35088 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 040c163e-6f2e-3b59-a229-d548941ea109 | -8.06209 | -48.65147 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6719118f-149d-3847-a634-92316bb12620 | -9.59278 | -47.97206 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 450a7cfe-8fc2-37bc-a94c-5c4a092078a9 | -13.93851 | -48.2427 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 83a5361e-8361-3062-ba2c-79223fa701e2 | -13.00918 | -54.81796 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 116dc3a0-cae3-395c-802b-c3327ca11110 | -8.05811 | -45.48794 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50b4f3d4-6db1-3691-b367-6249aaef7396 | -8.86317 | -47.23326 | 2025-09-09 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36be14c7-817c-3c25-b54b-2e0e15de596c | -7.72453 | -44.73919 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 402ec5b4-3a36-3094-9358-1de0f7b37671 | -12.18618 | -53.88884 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ddd135a-b5e9-3cfb-8dbd-3ca3b22f92ca | -10.97452 | -45.10139 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 00497b88-3cc5-3092-a09a-ae1878cca83d | -15.02627 | -42.15075 | 2025-09-09 04:34:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b1cc139d-9341-339d-a62d-e43d9719b0fc | -9.86754 | -47.41674 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c78f746c-47b6-343b-81fa-0953b6522c3e | -13.82097 | -46.2349 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e751c5b3-5c00-3e0b-a0f5-b6c071d0b63d | -9.24263 | -57.06435 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1813a3b8-ce26-3bbc-a42a-3e6a386340b5 | -7.50662 | -48.24363 | 2025-09-09 04:34:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc18a31-998c-3e13-a58a-bea2a16d1a96 | -13.13272 | -54.92466 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b18fd2d-f461-3e18-85be-56f1a071ff87 | -8.02649 | -47.2828 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e4723a-10f1-3b55-b282-f9ba0cbc9983 | -7.78578 | -46.08176 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9e9c542-2bd5-3e3e-af71-3b59cdb26e10 | -12.82785 | -52.95252 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4756215b-97e7-3ba0-9716-fc20512700d6 | -14.2595 | -47.0988 | 2025-09-09 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7b7dade-8fb0-3da1-85f4-6c8a9a497645 | -11.32776 | -55.22034 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 086ce2dd-269d-31ff-af08-ceca0772d4b3 | -8.05221 | -48.64987 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c271fcf9-ae53-3733-a4ee-fe5aa160e00c | -10.18817 | -46.22862 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9a61788-bfcf-3c67-a674-bb303fd40eae | -12.87177 | -47.97238 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2ad1a100-b6bc-3c24-a88e-5325c1b39b39 | -11.62652 | -52.23484 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8074d6a7-9bad-3614-9eb0-5a4a09145bfa | -8.37346 | -45.02969 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 376e3ae9-f8bd-35ab-ba28-8003b522a170 | -11.29968 | -46.48921 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cc63de7-92e6-3df9-a6ce-c806975ee7ef | -12.52153 | -45.28667 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd8c688a-86ad-3ada-a0b3-c6bb97e9d9c7 | -13.02313 | -48.03301 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f578bcc-07eb-35e2-b3b7-cd78baff011f | -7.66541 | -50.29558 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0056186-96b5-3a68-9686-dff22eff153a | -10.33956 | -47.73674 | 2025-09-09 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afb5faa8-d58c-38d1-af0a-03ea40e65910 | -10.96076 | -46.80621 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb64ae59-f474-339c-b5da-e3eaad1af0e1 | -9.44944 | -60.51033 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1da9b797-a2ad-358c-ab19-598058707ce9 | -9.47827 | -60.49522 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78e8658d-80d1-3141-b67a-e10024ec9459 | -7.52211 | -46.0664 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67dc119f-abc9-394d-93da-29062aa45b4f | -12.9683 | -54.76525 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98e69d95-9d18-39b3-9227-e8c1d4e34176 | -8.47922 | -48.26716 | 2025-09-09 04:34:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb4bef4b-e088-3c94-ade2-8ed73ad2d23c | -12.62053 | -56.97887 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0674fac-2efb-3990-a093-39bb27ff9e3a | -8.06536 | -48.63068 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47f8151f-e079-39bc-b80a-c5607fff1416 | -12.20466 | -53.89734 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4fa5fe4b-63a5-3721-a443-1ec31b6f7d18 | -8.40579 | -49.10238 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7738276-b75b-3263-94dd-f5da5721ed41 | -10.04778 | -45.95365 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96d915c6-81dc-3b65-a40d-614630621065 | -8.88674 | -45.87568 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59c9dbcd-e6fd-3c30-8a79-8d8be989f762 | -12.83981 | -47.97849 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d3d0e7-f4df-3777-96ac-191c007b3b7c | -12.94498 | -54.80245 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c34c441-787d-37ef-915c-f1fcaaa69bd9 | -11.81621 | -48.23428 | 2025-09-09 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ffaf673-8a4c-36d2-86b5-c64d3a8e1007 | -12.83196 | -47.98484 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1675d7bb-de1d-35e5-9d3f-cc2263758b66 | -6.74531 | -51.96785 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fedeae95-c5fe-30b5-b1f5-323bafec3c76 | -9.94963 | -60.13068 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 822c322b-0547-362a-a307-ac18548d3635 | -9.0998 | -49.51329 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe793ec-0c93-3edb-b329-3bc78888eeb1 | -8.00218 | -46.34624 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6039e54f-039f-37ba-a71c-cc9e3454c143 | -10.81949 | -47.25919 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d08d894-6e98-3104-9870-9d52bb430b66 | -11.44677 | -49.26119 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c5d3caf-39fc-317f-bc25-87bd5d614fd9 | -8.37907 | -45.01723 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6705e3e2-db79-372f-bf81-47ab4e37ef51 | -8.05274 | -48.64642 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d7789793-83b3-3de0-b47b-19afa32441c9 | -11.704 | -54.54604 | 2025-09-09 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ccba889-dc66-3fe8-bf69-f1d5e60f0516 | -10.83928 | -47.26616 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a87b52df-c784-3115-8757-d95392928eb0 | -9.5577 | -48.65656 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5de61a3-aa93-3083-a578-54cb1c4fc401 | -12.87457 | -47.97677 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2c74c3a-746d-3301-9027-0bbe06d554c2 | -12.40637 | -47.79892 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8681ddc-032c-3dfc-a115-d8feacad0011 | -9.65264 | -48.02465 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e36d619c-8d65-3947-8257-8911737f3a08 | -12.82568 | -52.94325 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cf014215-e54a-3faa-a4c8-3e5d70c7b297 | -13.05008 | -48.02534 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cdac47d-5937-38c7-844f-fa712f23edec | -7.33013 | -45.96886 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9df6a032-acf0-39de-aca9-8a845c35bcf6 | -13.04223 | -48.03173 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be1095a1-6203-32a9-8bed-6f02aad7c93a | -12.9549 | -54.77021 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77c94790-52e0-3b1e-b715-bf081c63040b | -8.05821 | -48.63311 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bba7cebd-a3a5-38d0-9789-106525852560 | -13.18549 | -47.25089 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7f7470d-a9e7-3de4-aa3c-9fc095db4863 | -11.2034 | -54.99104 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b491937c-f4fe-3bf2-9aea-10406466d1e1 | -12.19392 | -53.89027 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ba3032d-1521-3910-a021-50c9f7c12f98 | -12.89422 | -47.98369 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdad4534-f6f8-3ad2-97a8-d620e7e212b0 | -14.17242 | -48.98511 | 2025-09-09 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9c1ef5c2-e852-302d-9f25-36d053f50ad5 | -9.19117 | -59.3779 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05083608-8402-37e9-aaf6-800e6e1b5d31 | -9.86011 | -48.85474 | 2025-09-09 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f99352ea-6f6a-39a7-84e8-1b77ed66e31e | -14.32716 | -47.32705 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
