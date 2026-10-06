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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f1bc0b8-4d55-3989-ad24-b74f8d5620cf | -12.1206 | -42.35803 | 2026-10-06 15:33:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b828d1ce-fb68-34e8-b270-4d121c47a135 | -16.72405 | -42.04886 | 2026-10-06 15:33:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 1687e2cf-3dbb-3990-ae8e-88d02cf1f7e7 | -15.11743 | -39.91663 | 2026-10-06 15:33:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e2de6e56-faaa-3ab9-a595-6fa297f657f2 | -12.28094 | -38.74487 | 2026-10-06 15:33:00 | NOAA-20 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6ade50e4-0ceb-31a4-8cf7-28c8a3d17582 | -14.61646 | -41.41171 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 080c1dca-a23f-33ae-83bc-7a08df1db15c | -11.88337 | -42.54675 | 2026-10-06 15:33:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ba493a35-351c-31fd-938f-d471c084ab47 | -9.86275 | -38.51278 | 2026-10-06 15:33:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| abf55b60-d6be-3129-8d69-dddcc905ea77 | -14.28515 | -39.10637 | 2026-10-06 15:33:00 | NOAA-20 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 95ebc777-d403-3e23-9ecc-abba0558edff | -15.25024 | -40.91599 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 14a5d9dd-32be-3aaa-b90f-4ba9bad7c2eb | -14.76195 | -41.40268 | 2026-10-06 15:33:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 88b9276b-c30e-3bbc-b90f-926615749e43 | -15.89268 | -40.72565 | 2026-10-06 15:33:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 83a490d1-0db2-3f3e-a83c-5fb923bf976e | -14.3154 | -40.95862 | 2026-10-06 15:33:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 684845eb-8108-3d01-b177-2c1a9dbd5294 | -15.89206 | -40.71912 | 2026-10-06 15:33:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1669a31b-c4eb-31a3-80ce-2811913897ac | -10.55925 | -39.45977 | 2026-10-06 15:33:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8985a52f-7525-35be-8a0e-35866b455343 | -15.60658 | -41.67852 | 2026-10-06 15:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| ae626873-1c6d-322a-b86c-ce0a33549ba2 | -15.6059 | -41.6714 | 2026-10-06 15:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| f2a1f933-bfc0-31a3-aeb0-53b6d3903d13 | -13.29334 | -38.98496 | 2026-10-06 15:33:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1f36c048-8b1c-38b6-9255-7089ca1253c5 | -10.45916 | -39.5092 | 2026-10-06 15:33:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 64181aab-8c7d-33b9-b61d-1fb0b2a5a2b6 | -10.45866 | -39.5051 | 2026-10-06 15:33:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 04d0f14c-b404-388d-acb6-b1353fa8945f | -12.12157 | -42.3521 | 2026-10-06 15:33:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 90f30fba-44b4-3680-80f0-380d6f244c73 | -15.37172 | -41.00814 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2b590f37-6e19-3ff4-a33f-b82b85583a53 | -14.80613 | -42.00536 | 2026-10-06 15:33:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f07711c4-b581-3c23-8b36-17af7f8c98cb | -14.60712 | -41.15159 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 3202d372-c511-37bc-8d62-199535207b24 | -16.17848 | -41.93262 | 2026-10-06 15:33:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| aa50648b-b1fb-3de0-a46b-d2f143bd3958 | -14.56253 | -41.9911 | 2026-10-06 15:33:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b911995b-20a0-3935-a343-016131a3b812 | -10.19314 | -39.55993 | 2026-10-06 15:33:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0d7f5d1b-2b57-34b2-a11e-9ce51b76e5c0 | -9.18727 | -36.0494 | 2026-10-06 15:33:00 | NOAA-20 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cb5d9c3c-5155-3fb8-a52f-1e5f508256b9 | -15.51931 | -41.34997 | 2026-10-06 15:33:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| be4af547-d68f-3444-8237-d1657023ba45 | -9.75618 | -41.9955 | 2026-10-06 15:33:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8177affb-cc3c-3b66-a8a4-88fb2518643b | -9.86812 | -38.51224 | 2026-10-06 15:33:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a83f8f83-45ef-3103-a4df-7accc4d99f81 | -14.04382 | -41.43238 | 2026-10-06 15:33:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 2dea82cc-574a-3388-a8c3-5607d3750e83 | -15.60448 | -41.67138 | 2026-10-06 15:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 852d47f7-f184-3bd9-ba78-c0668d0aafb2 | -14.35956 | -41.28382 | 2026-10-06 15:33:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 0bc63fe5-f4ea-3eb1-a30e-65d61c491f8e | -11.23814 | -38.96505 | 2026-10-06 15:33:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4ce1bb70-37d2-3fa6-888c-7f1a432a6bb6 | -15.35356 | -40.83202 | 2026-10-06 15:33:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b4017cf7-a478-34c0-a1d2-04e53e2a6814 | -16.0579 | -39.27078 | 2026-10-06 15:33:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 64bb8c08-9395-3889-8ac5-c1f7cc0122e7 | -14.86682 | -42.04324 | 2026-10-06 15:33:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 031f0d7d-aad6-3a90-9713-ad8f64ea2d8c | -16.46584 | -41.25004 | 2026-10-06 15:33:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8e18f1d8-3378-35b9-b94b-c5dcf895ad88 | -12.73035 | -38.28089 | 2026-10-06 15:33:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ed2e2953-e443-3b45-88a4-7d3d4ddbda60 | -15.24344 | -40.91536 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 40.0 |
| 90f482ef-d3bc-31f2-bbe6-7fa002b09f88 | -11.0888 | -38.79675 | 2026-10-06 15:33:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2b89e89a-ec5e-31b6-8174-21245284a811 | -14.60428 | -41.15741 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 3876e5b8-acfc-3ac3-a014-db819d5a389a | -15.93111 | -40.73321 | 2026-10-06 15:33:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ed3ec5e0-7b0e-319b-8337-6d5d889bf89f | -14.72497 | -41.7284 | 2026-10-06 15:33:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e9314823-dbcf-3254-90e0-96018d6e1530 | -14.32006 | -40.95855 | 2026-10-06 15:33:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 9d135a1c-20e8-3ef3-a99d-6c2c98d76f5b | -14.80876 | -42.00534 | 2026-10-06 15:33:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| df72ecfc-0af2-3db0-9d46-935070833363 | -9.90213 | -38.81538 | 2026-10-06 15:33:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4d23def8-2832-3b70-af9f-4a0b5158562a | -12.12228 | -42.35857 | 2026-10-06 15:33:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| c099c4b2-0e84-3c12-87d0-80394527f4c8 | -8.96505 | -35.63395 | 2026-10-06 15:33:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 58bc2c6a-1cf9-34de-95ef-f53d353cb6ed | -15.58183 | -40.29661 | 2026-10-06 15:33:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 6d5df00a-3874-3d15-b45e-0acc22805fdb | -14.11513 | -40.68995 | 2026-10-06 15:33:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 4d290544-f969-3d5d-84bf-3f94c4f2e891 | -14.61102 | -41.15699 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6680ae32-17a8-3298-95d0-874d48205872 | -16.10661 | -40.3609 | 2026-10-06 15:33:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0f06a712-0e70-3394-9a63-d536f0e1413c | -8.95218 | -37.60081 | 2026-10-06 15:33:00 | NOAA-20 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f5490b4e-5d04-3e45-b6de-6b4c1ed233c9 | -12.34246 | -38.92566 | 2026-10-06 15:33:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9ba1342f-0681-33d2-8f6a-67030b9df1c3 | -15.58722 | -40.29679 | 2026-10-06 15:33:00 | NOAA-20 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3f21f76c-742c-3072-b3b6-d237b183433c | -15.5883 | -40.29617 | 2026-10-06 15:33:00 | NOAA-20 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f728c0d6-6345-341b-9395-285d8b1ab799 | -15.11793 | -39.92173 | 2026-10-06 15:33:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| a83c14b0-c61e-3eb0-a271-42587f207c6a | -14.60104 | -40.61643 | 2026-10-06 15:33:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0364c8fe-4e56-3ada-9078-4898cfdb2c46 | -15.24969 | -40.91071 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 5d10fa69-e4e1-32ab-8ec9-c8a134b4696b | -12.96427 | -41.0615 | 2026-10-06 15:33:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 67fd90b9-a307-336d-870d-c24263d8806a | -15.37436 | -41.00326 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 0cc2e409-ce68-3490-bdf7-b1a4af8bc2f1 | -13.72998 | -42.39529 | 2026-10-06 15:33:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3993bae0-d62e-3f8a-af74-1d3a6b9c90b5 | -15.24719 | -40.91043 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| f627b043-e8b4-3891-89ea-9bb8bd1ee911 | -14.27436 | -42.17982 | 2026-10-06 15:33:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e1cd0d45-bf4b-3238-9174-522bc57ef77b | -9.86857 | -38.51563 | 2026-10-06 15:33:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 59d6d102-4197-31e0-9660-b5610edddb87 | -14.98146 | -42.33139 | 2026-10-06 15:33:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0dabcbd2-0657-377f-b168-e4440db0697f | -14.35885 | -41.2768 | 2026-10-06 15:33:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 2fa4a8b4-05c7-3c34-b1b2-9d50c18de446 | -15.34697 | -40.83315 | 2026-10-06 15:33:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| fc86f847-7c9b-3d02-93b1-3b9dee40e18a | -15.90298 | -38.90629 | 2026-10-06 15:33:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 4bf2e6bd-da5a-39d9-9e5e-2ca154445aa0 | -15.11964 | -39.9174 | 2026-10-06 15:33:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 57c5f67e-16a1-321b-a0d3-ed4a89930c99 | -15.12019 | -39.92253 | 2026-10-06 15:33:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 08a09013-e933-3291-907c-8ff5cf03af08 | -12.36488 | -42.15135 | 2026-10-06 15:33:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f144ca7d-34b4-3638-9255-c8dae5d7d593 | -14.04318 | -41.42642 | 2026-10-06 15:33:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 44b31a24-c891-3df0-99f4-b9025c26e7e4 | -15.3711 | -41.00209 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4cd6a84b-9c5d-369d-8916-53a9557b31e3 | -15.24769 | -40.91565 | 2026-10-06 15:33:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| 4601c480-ecec-3c89-ae44-8e20b6bb941a | -12.11993 | -42.35157 | 2026-10-06 15:33:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 930c5eb5-90ce-3348-bef0-4e595ccb96a2 | -15.35127 | -40.83379 | 2026-10-06 15:33:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| ab9a8033-4185-315d-b508-20212385fa99 | -15.51957 | -39.22918 | 2026-10-06 15:33:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 5987939e-a1c6-3f4d-a533-4e2249f48869 | -14.36558 | -41.27596 | 2026-10-06 15:33:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 90e249b7-95fb-3068-8d4c-4e1520679a6f | -14.60771 | -41.15766 | 2026-10-06 15:33:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 3a8695e5-c18e-3591-904a-e020a263efb2 | -14.31951 | -40.9531 | 2026-10-06 15:33:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 190c61cf-825c-38a4-9e9f-25a5481a4c13 | -12.7393 | -38.16728 | 2026-10-06 15:33:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f212e901-656b-3bbd-8711-e0ff59747357 | -14.80388 | -41.53683 | 2026-10-06 15:33:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c2344435-5860-3628-a97e-659404b8eb0b | -13.72598 | -42.39336 | 2026-10-06 15:33:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2c484c30-d85b-3b2e-a9dd-5357967496d5 | -11.0895 | -38.79662 | 2026-10-06 15:33:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4414f9a0-fa66-3f19-9c03-caabaca77c6e | -15.55089 | -39.94654 | 2026-10-06 15:33:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7417fcc7-646a-3c55-a067-f57548992b8d | -15.60512 | -41.67851 | 2026-10-06 15:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 2d5a45d1-a712-38a8-b8f4-cff3df0eb9e8 | -14.78323 | -41.46679 | 2026-10-06 15:33:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 57510b10-f04c-344a-8964-db5b987444d4 | -15.93371 | -40.73382 | 2026-10-06 15:33:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| dc1f11ad-3f87-3a29-b9b0-21c86c3751e6 | -14.98224 | -42.33931 | 2026-10-06 15:33:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| bc773462-ccb1-36d4-a383-f19f237d70e4 | -16.10708 | -40.36263 | 2026-10-06 15:33:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 59808d21-bd76-379b-9670-d6a5b98980c5 | -14.60077 | -40.61679 | 2026-10-06 15:33:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 10cca65e-a381-3d0f-9477-8398e0bfa161 | -13.79294 | -41.13797 | 2026-10-06 15:33:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 17ff88b6-ec2c-3519-aad5-8f025150e557 | -14.32191 | -40.95695 | 2026-10-06 15:33:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| adfaf76c-db18-3fa0-979c-2c19f4f91263 | -14.80356 | -41.53781 | 2026-10-06 15:33:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b32c56b8-19cd-3e70-a182-3260c135c692 | -13.53351 | -39.7844 | 2026-10-06 15:33:00 | NOAA-20 | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 02257664-5e76-3324-82db-4edb8b294a4c | -12.72977 | -38.28113 | 2026-10-06 15:33:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ced3a024-5a3c-3012-b9bb-b582560ba993 | -5.61408 | -35.61517 | 2026-10-06 15:35:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 22e868f5-dbdf-34f3-99ca-c0ffca20c5f7 | -6.89981 | -43.62511 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |


[Clique aqui para ver as próximas entradas](README88.md)
