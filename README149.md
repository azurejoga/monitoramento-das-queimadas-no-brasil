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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06353d8d-379d-38e3-8deb-1f6440149afd | -8.93782 | -62.36974 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7306dfd6-b82e-30d1-8489-63069af5b04c | -11.33945 | -45.15564 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b85515e8-4de7-3e5e-bc6a-19a168f4d773 | -12.95641 | -45.92488 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fae7a73c-ccba-325a-8887-d9f9f2ba1f80 | -12.09182 | -44.99139 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0ebc17db-b63e-3237-a592-3da8e80e1b1d | -8.38758 | -46.46751 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 20d861dc-bbb6-3e4e-b195-523c1d0308fa | -11.21417 | -46.10225 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d2726f63-030a-32a6-b2e2-348334aec355 | -13.3858 | -51.76702 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f0ab2635-c213-346f-b503-d611fd2e70cf | -10.90895 | -61.67921 | 2026-08-31 16:50:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bd4c7cc-86e2-3441-98be-823d7e427580 | -11.37697 | -45.20805 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| f6257036-fb3f-3d19-b70b-639ebb0cd2ce | -11.32298 | -45.16641 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 3bcfc808-50a9-3bf2-8889-59a03ae1a756 | -8.7622 | -46.4463 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 787d8cfc-72e9-364d-9566-7838880fbf5b | -6.69213 | -52.88543 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d9a7ebb2-31df-3f50-9e35-109f91039b6f | -13.42558 | -51.68896 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bfbfa834-5674-3860-b9f0-692d539920cb | -7.36884 | -45.0674 | 2026-08-31 16:50:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e9e9527f-e85c-30e7-bff3-531aa6d60f4e | -9.20993 | -51.56626 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7f4235b3-d8de-3ee2-a13a-9b02d4a80da1 | -12.96039 | -45.92805 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9cc84cd6-c622-3a19-92e0-46088caad7b9 | -10.11115 | -50.30167 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8349fe5d-ebd9-3f33-a7dc-2c551b107904 | -9.41539 | -51.67848 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4217c739-9db4-3e4c-b5d3-4df6aa91362c | -13.44184 | -51.75724 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c10a9b7a-c0ce-3ea0-b1b7-e2c37364a624 | -7.65343 | -46.72393 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cea0db26-b203-3950-9b18-5f2eb731c7e3 | -12.89441 | -45.843 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| ac5d9871-8c99-3b7e-91be-76cf03d318f9 | -9.59222 | -47.59334 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 59723ca0-ec78-3146-bbd6-fca0879fc02b | -5.67 | -40.71724 | 2026-08-31 16:50:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 41f6ddb9-6c48-381f-80d5-0e73df761fe8 | -8.08895 | -45.48628 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 335ffd55-5111-3f6c-9331-dd23862b2c31 | -13.97242 | -54.39656 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7e8006e5-6905-3f81-a3a6-cd1a21e4daa0 | -7.12721 | -44.30774 | 2026-08-31 16:50:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 475cccd4-11ab-3090-8b42-26ef62ce94af | -10.45156 | -46.75111 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 479ac55a-6a49-3210-837b-bff398945403 | -8.74529 | -46.46814 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c7ea693a-2e76-3c79-971c-0d1bc816e85b | -9.64913 | -46.06716 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9fb9f529-54ec-326d-9390-08a9dc8eff33 | -7.69073 | -55.34126 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a2e70373-ef90-37f2-a628-84ca4ea06e02 | -8.4141 | -44.97973 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b090a6dd-a639-3f15-9860-23311ab89532 | -7.02374 | -55.63671 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c131906c-4ed5-31cc-80c3-79c407101167 | -9.56989 | -48.3293 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fefc196a-9b53-3712-a749-53a0b882f6d2 | -6.17948 | -45.90894 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8c7dce9-94c8-3633-87e3-b5870a12ccf1 | -9.28314 | -57.06864 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d37ba6a8-3806-3aa2-ad09-ad26d18284a5 | -7.09551 | -45.78606 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f2f7a886-f185-3f29-936d-434868823db4 | -10.85191 | -45.34322 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 558dfd6e-623e-3ace-af62-d8b9522925b4 | -6.83917 | -41.68903 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| f70c4ea9-40a7-31b1-9fbb-787efabaca20 | -10.12746 | -45.74996 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd6e8050-1de1-38fd-a096-064f38447dab | -9.20654 | -59.40732 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a184b477-0354-3a94-8d20-c595803bc70e | -5.59007 | -42.31713 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 49ea55eb-9733-3075-b7b9-aebfa05cfb7e | -7.64129 | -46.7142 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5613e530-1381-335a-8543-5aa05a4e2952 | -11.21199 | -45.32991 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc9a012d-b70d-37e0-af69-5e389acb9037 | -8.38688 | -44.988 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55db4e2b-b16c-367a-9fba-c776ede4e551 | -7.99222 | -44.33311 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 175.5 |
| e562b066-b32d-3b39-a0ac-9fdf3b257511 | -9.65772 | -46.05392 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31d138c9-1247-36a5-97dc-ab082b49adc5 | -13.57082 | -51.74119 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 67d98865-e50e-347b-be31-0bcc88835847 | -5.51355 | -46.6096 | 2026-08-31 16:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dbd2129-cca6-3785-9496-b819ed4790bf | -5.53715 | -46.59843 | 2026-08-31 16:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6728964f-077f-36fb-bc7c-788a95ff1219 | -13.41594 | -51.39272 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9be9e143-253a-3867-90bc-471021430439 | -9.47493 | -57.01896 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 465ddebf-d577-34c2-8f87-350a5be08005 | -9.57141 | -60.8389 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 24b2cca7-b344-3948-ad67-3a4f0fe04ce1 | -13.83163 | -54.09779 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc757e27-55eb-3239-a0ad-4a3b1f7dbe44 | -10.84773 | -45.33978 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| be3e9ac5-e9a7-37c2-bde1-561b9155cef6 | -7.2287 | -42.76653 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e78d3da5-6832-3160-871c-97533e0546a4 | -9.19665 | -51.563 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4219dfce-bd1c-3f96-83cf-9e7c15e5db25 | -10.74192 | -47.98211 | 2026-08-31 16:50:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c4c5c1ac-a7a8-3ba8-9e9e-8c0fc0ee1201 | -8.17208 | -54.92471 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 34447d71-0854-376f-94c3-e05c8515c236 | -7.79162 | -44.06872 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f03a621c-7c15-331f-b2cf-e2f48b5628a9 | -12.10264 | -47.27621 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 622623ef-ce83-37d3-a2e8-8e7e34b054b0 | -12.38133 | -48.16642 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 0352150b-625f-3822-9eb6-5bb2ccfd4ca6 | -7.43833 | -44.9459 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a4b2d806-2cee-39c7-9a57-29289ff1cdb7 | -7.0932 | -43.87967 | 2026-08-31 16:50:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce06527f-0ca1-3129-a409-943d872ae409 | -6.98756 | -45.39396 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 828ad5ef-7a56-37e4-9995-2485a268b0c3 | -8.87931 | -46.0309 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e655a4d1-42c7-344c-b629-6a80ab88a007 | -11.92137 | -45.08153 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 47f18e5f-5395-3ba3-9297-ca59111691ab | -11.93011 | -45.04634 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7654a9a8-807a-3e3b-a93d-af279b78934d | -11.25118 | -45.10693 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2eeb436f-dcd5-355e-a8d1-54bfa01ce039 | -7.52019 | -44.44925 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dff5918a-8882-30e5-acee-2d1f40dbf981 | -8.75506 | -46.46285 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| edebeea9-7145-30e1-aa08-c20acd6a2d14 | -11.24028 | -45.14616 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f1702ef2-1185-33a5-8f1b-b0dbd744e227 | -11.62206 | -49.41936 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 15f42708-997e-3cf8-a0c6-29088d7292e3 | -7.42341 | -44.25171 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 249787f5-807b-3e54-9eab-578777007c7a | -8.13481 | -45.58648 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 07961834-8b94-3670-8911-0bf41c82f84c | -11.24188 | -51.24485 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 35faf62e-8a74-38b5-a411-f011c497c6ee | -7.05966 | -42.2139 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7d0277cf-2970-3b2b-811f-9e93870ca412 | -9.19729 | -60.24747 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 53b8b775-7921-3987-ad25-2f3e961a706e | -11.49974 | -46.93463 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85c28bd1-8b46-3446-8478-321660c73707 | -9.30875 | -56.80441 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2374ee9e-eae2-3a72-ace3-0af19d325fa2 | -11.01915 | -49.69592 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb09626f-f1fb-38b2-82b7-1ba0a1add9bf | -8.39103 | -46.46697 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4d21995-a676-3e47-b43c-3ac6fea2c703 | -7.98311 | -44.27866 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 5c975855-e8c9-32b6-ac01-78e730f8e2ab | -11.71743 | -47.6396 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65a77c92-7127-31d3-a260-a10bd8708eec | -7.64938 | -46.72069 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 90d4b31b-6532-37f6-9546-24b4f8fd92e4 | -11.72128 | -47.64259 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 4f3476b2-6241-3462-91fb-bdbc7acfafa4 | -11.70595 | -47.60901 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 51a04572-a393-3be3-912a-2ce69c4a6dd7 | -9.79118 | -59.44811 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 833fae46-08a5-36bd-ae32-cae286422733 | -10.16047 | -45.72563 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c5497a09-9916-3214-9e55-81abd90721c6 | -8.4171 | -47.72193 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 16265683-d056-332e-82f4-387c2ac0f714 | -7.99304 | -44.338 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| eb974862-4e36-3b2d-86cd-14051135791f | -5.58359 | -42.33124 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 5da37571-dbcc-34ca-95e6-38b4ab77bdef | -9.97103 | -46.3093 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cd99b82d-fb90-3595-bde5-402be7f4b7e6 | -9.18767 | -51.55175 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5a8b9df6-1e3b-3375-8d0b-1fc0de555cda | -6.83656 | -52.42489 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f4231e79-9977-389a-be9f-0ded27a428d1 | -12.08896 | -44.99625 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| b55a5b69-8c86-3cb0-8ea9-603943193475 | -11.23473 | -45.13441 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2ebf3408-6ecb-3813-84a3-eec13f91f177 | -6.84639 | -41.70306 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0e75eb3c-6749-30cb-bfd2-c948779900c7 | -7.42423 | -44.25661 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 84b31666-af3c-39ee-8276-64050b6f3015 | -6.95034 | -56.51364 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9c81d0e3-aec2-3e2b-9206-3d82d2847a23 | -8.66474 | -49.54079 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README150.md)
