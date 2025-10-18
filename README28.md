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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe6d4c26-5509-3676-aae5-b21d9cc38178 | -10.15947 | -44.53274 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aac004e0-dc8b-3ad6-a8b7-7402c5c45906 | -10.67927 | -44.56689 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e20eb26-e7fb-38b6-9c5e-4d977e0870f6 | -10.23678 | -44.06512 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f01ba9b6-5557-3e51-8fd6-a5cea17a069a | -13.46354 | -43.7662 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43976a18-0ee5-3e91-a68c-81ac81c26361 | -12.17312 | -45.08319 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42df566e-fc53-39d3-832d-60dd6605b1ab | -7.46304 | -42.1687 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc8ea7bc-90c3-3849-b20f-f171b3a705ba | -11.35597 | -44.27413 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cad1848-dcf6-3b3e-a7e2-07b73de95d93 | -13.75898 | -43.80771 | 2025-10-18 04:02:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 628ac7f2-4aff-3b16-a9cf-5e5445a57fc6 | -10.62764 | -42.30903 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88b01fa2-a584-3ca6-a6e6-5db829a4931a | -6.88945 | -45.44971 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b4d44ae-169f-3086-a249-78604151d72a | -6.99429 | -45.67407 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e6e20ca-d5cc-308f-afe7-f85ae002d481 | -10.33542 | -47.77272 | 2025-10-18 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b914b6df-c9f7-36b9-87a2-8bec252e7846 | -8.38482 | -46.24187 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c4612c-c60d-3e3a-881d-a44a18457e92 | -13.13127 | -48.02871 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebf55590-5d8d-39f4-979e-299f02c3b4f9 | -10.50416 | -43.45606 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8bcbae13-f422-3cd9-8f88-2d8d2ec2ccfe | -9.50446 | -47.26849 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8e72a938-54eb-3c45-922d-2dd7dc74d354 | -7.34787 | -43.86235 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b2939d23-f8f3-3717-8b17-18d72c1a2b79 | -7.92845 | -44.12837 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 09be10ce-d1eb-3dbe-acd7-d8a905c3d720 | -10.23146 | -46.70914 | 2025-10-18 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8010600d-f85d-3e33-8b52-32afa4f3e788 | -11.35953 | -45.25995 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 760d87f3-68dc-3d82-84ea-80bd6485c1ad | -11.61253 | -44.08782 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b2b6e2fc-1dab-3eb0-86ff-5aa47872431c | -9.41919 | -47.01031 | 2025-10-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 237b9a02-58a9-3c7e-bd9b-b1424c4717d4 | -8.61391 | -40.19501 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d9324521-dbf5-3ca4-a347-55f46b4a319f | -13.03951 | -46.94384 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee35d933-3882-333f-b78f-f23ed2511c42 | -10.71393 | -44.54094 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6658f4e-cbf2-3caf-aa4a-8d670e3e4f51 | -13.40416 | -48.58498 | 2025-10-18 04:02:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a0c7ef-3069-3329-b7f8-9c4fb7936f82 | -8.16149 | -47.0294 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 128f2431-23d3-389e-a4ea-76f549154087 | -12.9131 | -48.57827 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65f7cba7-2818-3c51-bc81-aa3f7941fb00 | -6.99374 | -45.20354 | 2025-10-18 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6a38509-01d1-3da2-9c33-a8891ca72cdf | -8.44619 | -44.1734 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e8245d4-77aa-3a48-ac5b-52b4ff04d1b1 | -8.22295 | -46.83337 | 2025-10-18 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d59bb999-7c19-3c14-bc6f-c3d4797b1ed2 | -13.0027 | -43.85328 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef0b82ba-0fa9-35e7-8707-5a1da9759305 | -14.09503 | -43.62412 | 2025-10-18 04:02:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0264ac5-652f-3382-a2b0-6f0b92a4b59b | -9.8863 | -49.12164 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd3e01b3-fe03-3cf5-afcb-5615045cc019 | -10.16316 | -44.53349 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a64720d-00e2-3f1f-8432-f9c909e8a1e7 | -10.53327 | -43.36675 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 517181dc-dbcc-38e0-b814-c2b7ebea0850 | -8.23447 | -43.99939 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44ab8a73-45e5-31c8-b8f8-b1a9aa34d719 | -10.46773 | -44.06158 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241f1ea9-cf45-359f-9aae-9fb227654da9 | -10.69846 | -44.5656 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46115975-aca7-323b-bc5d-164a015b4049 | -11.38402 | -44.26154 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b6c3ecc-f173-3d9f-8a2c-4a6d5b38c48f | -10.11416 | -44.55249 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f505e255-f618-3ec9-8810-d8dbd24bbaa5 | -10.95948 | -45.46455 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d30965fb-dc48-3643-b9b8-ec75d19ba1a2 | -7.36004 | -44.22914 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63d761ab-663e-35b5-b929-6b5aa129f987 | -8.60678 | -40.19743 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f3a7ca1b-1936-3044-a546-035f591f83bd | -7.58213 | -44.98229 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3cb10b27-a3a5-3cbc-bf6f-d98ec1167416 | -7.17222 | -42.37868 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4a85767a-fc8a-3cd0-804f-9c1ede2c30d8 | -9.08292 | -45.14137 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d52890ed-721d-31a7-af98-15d6a21d85ee | -13.76995 | -48.23107 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fbe04ed-8278-3ba9-89de-d30a62a29acb | -9.1202 | -46.61882 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5e1e365-04a4-3c47-91ee-4b86b4864030 | -13.77623 | -48.24631 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab98eb9f-7b82-3bd4-b093-9e026dd58696 | -11.5028 | -44.0489 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f20106a-8074-3623-977a-9ac527b24889 | -13.75834 | -43.81157 | 2025-10-18 04:02:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 782353ef-e803-32d4-9e42-c6d47912a9ec | -13.20097 | -46.43422 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e80df036-fae9-3cd1-8c44-fa166dfb1080 | -6.97957 | -44.86997 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc186e60-748b-3d48-a8e1-7a142d23463c | -9.12091 | -46.61475 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ca36ee3-da43-30bb-abf5-f59a22feb474 | -10.10892 | -44.56087 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32653aa3-adcd-33fe-824c-3e7a5fa34621 | -11.49079 | -44.23076 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca627cc-cd8c-35d6-9897-5b10fa478b7f | -8.7939 | -40.43638 | 2025-10-18 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b413690-2b9a-3f52-ab0a-9e10da3e8ff4 | -10.24531 | -44.03584 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 190cb5d2-cdae-3dcb-b935-1d87be66d129 | -10.68889 | -44.55475 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b1c1170-ed73-3d8d-804f-1abbc389bbad | -10.43578 | -45.01898 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13691468-f433-3fdd-919e-fce34bef85b4 | -12.17402 | -45.05583 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f63c914-d73f-3abe-ab35-ee520d8b3dc3 | -8.47884 | -44.18409 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62d9cda5-7de4-3eb7-a60a-467db3c78775 | -10.16611 | -44.53869 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 658c911a-0cbd-3c96-8254-04db46df6065 | -10.23973 | -44.06977 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5b6177c-2fa7-377d-97e7-aab943ed2d42 | -8.22162 | -43.30912 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2a3233b8-74dd-3798-aad2-32dc625a9cc6 | -13.53208 | -47.99601 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbd838f5-43d6-3634-a7fe-79538257f8a0 | -6.93461 | -43.68882 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6994244f-95d9-3e81-8293-a5e72c407325 | -13.51029 | -47.99174 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1b3bbf5-c37e-3284-ba92-952dca251b20 | -13.04087 | -46.95975 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 669f8c74-f2f7-391a-ae55-ebc2e60b3f37 | -10.61726 | -47.38417 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6d57f4-32fc-394a-99e2-c401d2e49509 | -13.23015 | -43.97969 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 911fa953-c1f2-3315-8ef7-f028f1a71457 | -7.2947 | -41.94722 | 2025-10-18 04:02:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ce5c7d79-b429-3062-9872-a8e89bb70b6c | -10.14837 | -44.53064 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 885f349c-a22c-30ed-ab7d-b53fd82e0e01 | -11.59177 | -44.05883 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 422f073f-b16e-383c-9eb8-806f631007d4 | -8.77376 | -47.84134 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de194d5c-2dd5-3cdb-ae53-0101ff726a67 | -12.45552 | -45.47571 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 110e0b2c-b8a4-3d6d-a9d3-ab12eb2bdc24 | -10.49195 | -43.42129 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95f30749-be6f-3441-ae04-11b3aec1b3c9 | -13.20342 | -46.42019 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 489b3030-1435-3e6c-9ce7-d27f239b863b | -13.7787 | -48.23313 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3acd2da1-df3f-3ea8-b31b-129112a32a21 | -10.95814 | -45.44901 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5119d0f6-79f7-31c9-96b3-7e1defccd186 | -10.95039 | -45.44775 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68e8ef8a-e283-3b1a-8a57-3506b376010c | -10.91091 | -47.91289 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 660dace8-8ace-30a6-bb98-efb0b9fad829 | -7.16311 | -42.3693 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 350c46ef-15f8-3a4e-aca6-b524df769ddd | -11.13806 | -45.07793 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e5d64ae-4d01-3ea9-a930-b05808112f17 | -12.46012 | -45.47169 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fb2a484-be14-3012-9d5e-d04bbe470fa0 | -12.14557 | -37.97658 | 2025-10-18 04:02:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e69736b5-fdcf-3049-a133-4d4e905b9587 | -8.18946 | -42.34943 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06439028-9dc7-3251-aaa2-35cf912d7472 | -7.75657 | -42.50671 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4eb6963d-d473-398a-9a3b-34da5c01badf | -8.61008 | -40.19795 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c9b1112c-9873-3b78-8e23-706d0658419f | -7.45208 | -42.68838 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bec15196-3946-3d57-b3fb-ba9a42ce2ed8 | -8.82634 | -49.68464 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75f89bc-df24-3826-8eb0-2a4c41d9e7a9 | -10.68446 | -44.55857 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef3d440e-1952-3859-b2f0-7fda8cc1ed1c | -8.0969 | -44.10232 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9009828e-de85-391f-a67f-0536cdc6ce48 | -13.19728 | -48.31646 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30e4f51a-b575-3366-ba90-68a2c28067b2 | -8.53959 | -50.08073 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb718967-e115-3d6a-80af-73b1d32314de | -10.48362 | -43.42815 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a2ad5c61-f46c-324d-9d3c-8e0cf42b32a0 | -7.75311 | -42.50615 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36b5faf4-3614-38a1-b83b-94fe487497d9 | -13.45664 | -43.76502 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b370aee0-dae6-3517-9eab-cab9165e8f7c | -12.15371 | -45.08456 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README29.md)
