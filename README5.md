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
| 38112883-a5db-3035-82a3-4085a50c25f5 | -10.8025 | -50.6539 | 2025-09-16 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 121fce65-946f-3143-97f5-d6efe019b188 | -10.7833 | -50.6772 | 2025-09-16 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0457e4ad-a754-311c-9c08-f2b9dabacbdf | -15.8815 | -59.3961 | 2025-09-16 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 405d8d2d-78f1-3848-869a-f5a81ff6f0a5 | -10.7836 | -50.6559 | 2025-09-16 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f25ed2a5-e43b-3109-8e9b-2456616d927d | -8.992 | -46.2385 | 2025-09-16 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0e760a4f-28bf-3956-b0ef-8c72d8a23828 | -16.0192 | -59.2427 | 2025-09-16 02:50:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| fea58869-0379-39c0-bbd8-cb35154955fa | -9.1053 | -44.8412 | 2025-09-16 02:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c8b818d9-d259-311b-80fc-1096970af325 | -12.7875 | -47.9541 | 2025-09-16 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f23de142-7d71-3271-ab12-384edabddaa1 | -7.1318 | -47.9801 | 2025-09-16 02:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 693797e2-a03f-356b-9b66-abd9b53339b1 | -10.7115 | -46.488 | 2025-09-16 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 3760b461-a419-3710-92fe-674fb29fdd9b | -15.7793 | -53.4397 | 2025-09-16 02:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fa167711-a594-3b4c-8547-7aa4c0681b2c | -10.8025 | -50.6539 | 2025-09-16 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1c1f929c-8234-31ba-ada4-3efe6e1f1083 | -10.7201 | -44.7541 | 2025-09-16 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 9d84937d-67bc-3ab6-8e67-98fdb88862bb | -10.7306 | -46.4856 | 2025-09-16 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1ac908cb-9628-3bb2-9da6-e5b149097bc8 | -10.7392 | -44.7515 | 2025-09-16 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 57b11fb9-5fd4-3fc8-a4f1-0bdf31cd139b | -10.802 | -50.6965 | 2025-09-16 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3e1c47b4-5f59-337d-8442-c52ddad027c3 | -12.7682 | -47.9568 | 2025-09-16 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 165215dc-b8cf-359b-a906-f43c95739216 | -8.9731 | -46.2405 | 2025-09-16 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| dbb062cb-ab8f-348a-8816-e38591abc103 | -10.8022 | -50.6752 | 2025-09-16 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| e9261aca-619a-356c-bb47-4f0d0313500d | -10.7201 | -44.7541 | 2025-09-16 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 2e685936-2de9-3b0b-a034-d2f29ef3c2ca | -7.1505 | -47.9786 | 2025-09-16 03:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6cd3ba4a-b803-312b-b001-3f181a51d57a | -10.7392 | -44.7515 | 2025-09-16 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| eca1301c-5204-3158-ac1d-961a5ae44a0c | -12.6764 | -47.725 | 2025-09-16 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 8e707791-09f1-3de5-a064-989daf63a89c | -10.7205 | -44.731 | 2025-09-16 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c69c1c54-91ff-34f8-95b3-64b6fd64de00 | -8.9259 | -45.5231 | 2025-09-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2a8e5df2-57b8-318b-8d85-37708e803324 | -10.7836 | -50.6559 | 2025-09-16 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| dfe91a30-ad71-3874-ba4a-fca49f28e26d | -21.2014 | -44.3584 | 2025-09-16 03:00:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 793cecd1-9cfb-3d70-90c9-235c0a06f247 | -10.7833 | -50.6772 | 2025-09-16 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 97a445ed-b44b-37ee-a7aa-f53fe501413c | -10.8022 | -50.6752 | 2025-09-16 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| c0e9476d-6297-3506-b1f2-16ac45bd55bb | -10.8025 | -50.6539 | 2025-09-16 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f56806b1-a7a4-3f98-97e9-141c74f9a5d5 | -12.6572 | -47.7277 | 2025-09-16 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 0abbce85-d178-360e-b182-f5538bf56308 | -8.9452 | -45.4983 | 2025-09-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 084b100d-353c-385c-9f56-5fac80771af2 | -7.1318 | -47.9801 | 2025-09-16 03:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e2745755-d2be-3a1b-b6d8-cc8a2ea3c695 | -10.7112 | -46.5106 | 2025-09-16 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0fcad680-e2b3-3ac8-9145-6a1093094520 | -10.7306 | -46.4856 | 2025-09-16 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b9a7f440-f73d-312f-a9da-1c64dbf91ab2 | -8.9262 | -45.5004 | 2025-09-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 54a937e4-1827-3d8e-9bbd-f0b7fae33683 | -12.7678 | -47.9791 | 2025-09-16 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| db11718c-b197-30f9-96ee-0e9105263fe8 | -10.7115 | -46.488 | 2025-09-16 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| e354a8c6-bd86-387d-87b5-c1b9c0ffd585 | -12.7875 | -47.9541 | 2025-09-16 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| abe05167-48eb-333c-b753-0530c2573e4e | -12.7682 | -47.9568 | 2025-09-16 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| eb5fa192-9937-3fd6-a06a-fb443350ca57 | -16.0192 | -59.2427 | 2025-09-16 03:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5094ff0e-b35b-3308-a9ed-7d309401ec85 | -8.9259 | -45.5231 | 2025-09-16 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| acac0a79-53b7-330b-9a79-d35b0182b7a7 | -8.9262 | -45.5004 | 2025-09-16 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 263ab058-8e2a-3175-894d-0a0073cac598 | -7.1505 | -47.9786 | 2025-09-16 03:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d2ad9c0e-d312-30f5-b41d-566cc4ef62bf | -14.8214 | -51.6577 | 2025-09-16 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 459a8b5d-df9e-36d6-b075-8630949efadd | -10.7115 | -46.488 | 2025-09-16 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 218.8 |
| e074a477-f286-35c4-a580-3b8d8ee77aba | -10.7302 | -46.5082 | 2025-09-16 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 2b074296-ec2e-3c0c-ac8f-370bb5ad6756 | -7.1318 | -47.9801 | 2025-09-16 03:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b281f7f9-29de-3eb2-9b4f-a93cd98ec835 | -10.7833 | -50.6772 | 2025-09-16 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e0c50e9f-fc96-3e9c-bd72-ea70d6d076fe | -10.7836 | -50.6559 | 2025-09-16 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 93225cef-cf68-3e6f-bda5-59c3aa818125 | -10.8022 | -50.6752 | 2025-09-16 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a2bf796a-0110-373b-a734-50c53f001957 | -10.7112 | -46.5106 | 2025-09-16 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 148410eb-2a5e-367a-9a3d-7d24295984b6 | -10.7201 | -44.7541 | 2025-09-16 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 4c78283b-56bd-3d1b-8710-1de5d4154906 | -21.2014 | -44.3584 | 2025-09-16 03:10:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.5 |
| 256688b5-2df2-3add-97e5-4a362653b420 | -10.7306 | -46.4856 | 2025-09-16 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 896daf59-7868-3103-a5ab-2bc703e3c697 | -10.8025 | -50.6539 | 2025-09-16 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 4232e888-d1f3-30d8-b21a-e5b6f5740beb | -7.09174 | -39.67224 | 2025-09-16 03:10:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c0c51b7e-9a77-3beb-ace9-44441e390bff | -7.09137 | -39.67489 | 2025-09-16 03:10:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c66f47f0-8276-34cb-aaae-78956c59e78d | -7.07673 | -35.0978 | 2025-09-16 03:10:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 598c1c18-8208-3572-a754-8af82c2b26ca | -7.42161 | -40.0833 | 2025-09-16 03:10:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 62641717-9b6d-3835-a171-195a1930cc19 | -7.42401 | -40.08134 | 2025-09-16 03:10:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9221e895-46ca-362e-8908-7d7f3b773a3b | -7.0719 | -35.097 | 2025-09-16 03:10:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 731e5d81-55c9-3537-8cf6-b99664e5ced1 | -9.0573 | -40.5239 | 2025-09-16 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48df4187-b752-397b-a6e6-24d63e5843e7 | -7.09073 | -39.67778 | 2025-09-16 03:10:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 21051d66-d250-349a-b67c-494557a0e578 | -7.41745 | -40.07992 | 2025-09-16 03:10:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b063daf1-89c5-39ff-bf72-d82f68892ce7 | -9.05614 | -40.52971 | 2025-09-16 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e8fda58-b7b3-32bd-9f9a-372661ad9362 | -15.39677 | -41.71266 | 2025-09-16 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7aa19a77-0c92-322f-838a-93dfc5ee70bf | -14.64267 | -42.71791 | 2025-09-16 03:13:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a80806e-b490-3a36-8415-c76dbcd1a142 | -16.51186 | -43.55203 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2d0f5488-5386-361e-b04c-848096b2f9ee | -16.52612 | -43.7398 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e74ba2-ddd4-3541-bb95-42c094a6d41d | -15.7202 | -39.32186 | 2025-09-16 03:13:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 62c9bfb5-8d13-3a08-aaa9-6eadece25653 | -15.39792 | -41.70723 | 2025-09-16 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6bf9064b-6075-3730-820b-ed589d5661a4 | -15.40309 | -41.71407 | 2025-09-16 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c439f8a6-a941-3124-a20c-2d3f7f25075d | -14.64406 | -42.71148 | 2025-09-16 03:13:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e097977-8b23-3dc4-bdb2-f3301100c44e | -16.51203 | -43.54826 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 98ab29ea-de0b-3653-97df-a6e54a11476d | -14.64405 | -42.71666 | 2025-09-16 03:13:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 155138d3-fb18-3d7c-bb0f-723e28d43015 | -11.2038 | -41.61102 | 2025-09-16 03:13:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c3a09bae-6d6a-3d54-81d2-335e78ee38bb | -16.51046 | -43.55505 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1374fa42-c7b8-3471-b76c-02d155adcc91 | -15.71942 | -39.32564 | 2025-09-16 03:13:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a8ae111-5231-3cd1-8f9a-6912efe38575 | -16.52422 | -43.74126 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd0736e4-7b82-3a84-adb5-7dccb676b241 | -16.52593 | -43.73399 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d358a58f-9d2f-3130-a845-ff848d112bb7 | -15.39889 | -41.71156 | 2025-09-16 03:13:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 743ed23d-1b2d-3a9d-b0a7-7c365aa9afdb | -16.51338 | -43.54526 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 55239a75-988a-3098-95c5-e43a0191c8df | -16.52088 | -43.73076 | 2025-09-16 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb667fc7-64a3-3682-b51f-f29438e0275a | -17.86371 | -44.45158 | 2025-09-16 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 247abfd3-a3ea-3dd6-8311-00fe4bdb2b63 | -17.86292 | -44.44162 | 2025-09-16 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d43940d5-c3c4-396c-9474-58191d5c0a41 | -22.56783 | -44.73985 | 2025-09-16 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| fc23069e-5ae0-3d39-b78f-045e5c658699 | -22.56628 | -44.74611 | 2025-09-16 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 473e2c43-5708-3555-909f-517202dd839a | -21.19394 | -44.37183 | 2025-09-16 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 2c55c62a-ad62-3359-9208-5d4592aba497 | -18.86502 | -43.3534 | 2025-09-16 03:15:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b72653ee-ff2a-32dd-afcd-4e931d084fc2 | -21.2006 | -44.37311 | 2025-09-16 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 6bcf32c3-1ef7-3cde-ae8e-7efcf3de647f | -21.1925 | -44.37766 | 2025-09-16 03:15:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| e256d981-d676-38e8-95cf-47bcd7efc7d6 | -22.57199 | -44.74314 | 2025-09-16 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f9dc5d4a-6e3d-3471-915e-3d5a1282e20f | -18.54956 | -44.11165 | 2025-09-16 03:15:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7a12da9-4290-35c0-98e7-8c3b746ed6ac | -18.0066 | -43.93724 | 2025-09-16 03:15:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5be69b72-9efa-31a4-aace-e8f97277e3a7 | -20.20791 | -45.36897 | 2025-09-16 03:15:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f226f51a-b0cf-3f60-a5ac-6108da51bbaa | -17.86541 | -44.44442 | 2025-09-16 03:15:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8155d4e1-4b9f-37e4-84dd-2afab4cb7853 | -18.00807 | -43.9311 | 2025-09-16 03:15:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 093fef2e-e999-3fc7-a069-ec755c5a262f | -20.2011 | -45.36621 | 2025-09-16 03:15:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0ee22388-2b94-33e4-b63d-8f3e0d1098d4 | -22.57296 | -44.7472 | 2025-09-16 03:15:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
