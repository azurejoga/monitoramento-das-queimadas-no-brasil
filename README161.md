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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe1816a2-24f0-386a-b456-d8b2c4cb5557 | -18.1968 | -53.3638 | 2025-10-02 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b5246623-45c4-371d-bef2-1ac30cdf5cb8 | -11.6059 | -50.159 | 2025-10-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 88c60760-62a6-3fad-a4d0-9aae6d70ff97 | -9.3364 | -45.9079 | 2025-10-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 86200ca6-a03d-3275-8060-637fb2b9615e | -8.4756 | -46.8498 | 2025-10-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5c9c2e54-39d4-39db-9992-aad8b77296b8 | -6.679 | -42.8136 | 2025-10-02 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| d9235d26-4a24-360c-9a77-f11f1219ea3b | -6.6976 | -42.8354 | 2025-10-02 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 8c3456e6-69f9-3ff0-ac55-d848244688dc | -10.6802 | -48.5758 | 2025-10-02 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f6265f76-8c87-3b70-98aa-b35a33c5b11b | -18.2375 | -53.3145 | 2025-10-02 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 9459cae9-4c8d-33c6-987b-6bde2445238f | -15.3067 | -45.0713 | 2025-10-02 14:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 854303fc-35b9-378e-84e3-cdd3dea887db | -8.5013 | -47.8404 | 2025-10-02 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1d80c205-1f94-3656-a9ec-dcd9675a2f11 | -12.6095 | -50.5757 | 2025-10-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6fecce45-112d-3280-add2-701198792954 | -13.1932 | -47.8288 | 2025-10-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 194.7 |
| eb9520fe-ec5e-374d-8099-0920b8306e15 | -6.2411 | -45.3198 | 2025-10-02 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| cb0948cc-58d4-33a4-9d33-7a5f27ec9c25 | -11.8434 | -44.9872 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 78728a10-745e-340a-9466-93a749ff3e5f | -8.1513 | -44.1397 | 2025-10-02 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| bd620a06-e498-3013-9609-6c004894671c | -8.527 | -47.2658 | 2025-10-02 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| d9c97365-efce-316e-928e-f018ee7a6283 | -5.338 | -43.7623 | 2025-10-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| b046f4bd-d51e-399d-abe4-fd000354ce75 | -8.5081 | -47.2676 | 2025-10-02 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2d272512-c021-3919-8bf1-13a62a6dcf3b | -12.7627 | -50.5567 | 2025-10-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 029ab1cc-e49a-3fd2-9381-c4c3041ac609 | -18.1972 | -53.3423 | 2025-10-02 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 29e3cd93-680a-369d-b52e-895a5a6afe6b | -6.7814 | -45.5929 | 2025-10-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 06fa4c18-6d12-35e2-a8bd-6370d70bcdfb | -12.5005 | -50.2237 | 2025-10-02 14:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ab69d316-5844-3a67-a919-160643ee1854 | -11.6126 | -45.0443 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0151a2af-e46a-3fb8-86c2-c25abbc3738e | -8.1917 | -47.0101 | 2025-10-02 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| cdc23325-f4fe-3bf3-bdc4-5cdf8c45223a | -8.5016 | -47.8184 | 2025-10-02 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 56f7344a-55b1-34ed-b7c4-ced2bfe0cfb4 | -8.1702 | -44.1377 | 2025-10-02 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 200.4 |
| caa1325a-4a3f-34b5-a800-fd6a1ca4d5b4 | -16.0561 | -45.7438 | 2025-10-02 14:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| d98bd62f-1db2-3120-aaaa-36cdf02a1313 | -8.7844 | -44.8085 | 2025-10-02 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 67269ffc-419a-36e4-9267-1180041e19cd | -15.2031 | -48.0045 | 2025-10-02 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 489e3ddc-99aa-3332-aea3-b4b208086be7 | -9.3392 | -45.7039 | 2025-10-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 8aaf0cc9-a96d-34d0-96e9-1696d9c99759 | -11.8101 | -51.7957 | 2025-10-02 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9ee4a4a7-2819-3f42-95ca-647e55f81213 | -6.0934 | -43.1228 | 2025-10-02 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 17702b25-afcc-3a65-bad0-3411e97fa641 | -5.3379 | -43.7855 | 2025-10-02 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a632d5f7-84d9-34d6-a7e5-d542746a75f3 | -10.937 | -46.6618 | 2025-10-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 413.8 |
| 500a1710-540e-3de4-90a6-84a61bbc5da0 | -10.8622 | -46.5814 | 2025-10-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 434.7 |
| 9ee31c2a-ef9f-3105-b44b-72c814614515 | -6.9528 | -45.3299 | 2025-10-02 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f78eacf1-7c04-3c19-8f16-ec01f4d1ac2f | -9.3202 | -45.7061 | 2025-10-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 9a97f858-b110-3668-869c-4af10105e4cc | -5.3386 | -43.6928 | 2025-10-02 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 85830195-826b-3b4c-bfcf-e4ef77c36f51 | -12.4998 | -50.2668 | 2025-10-02 14:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| ae11c7e4-904c-373a-b53e-c234ad5b780b | -7.8092 | -47.6399 | 2025-10-02 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2fa9ac23-90ac-34aa-9c10-c47f604e433b | -12.481 | -50.2476 | 2025-10-02 14:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 011ca4db-b407-3731-b331-e3e21cfd8935 | -9.4275 | -47.5501 | 2025-10-02 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6242d7ea-dab0-3337-8bac-ee5855402155 | -11.1175 | -49.806 | 2025-10-02 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| bb697e89-82ee-3474-bf35-57e0298f2f3b | -13.1349 | -47.8597 | 2025-10-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 07704f9e-dd47-380a-a6f5-ecec8d23c2cc | -8.8929 | -46.6072 | 2025-10-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ed04bc41-4b7e-3e8f-a6b4-18f9a1d5cd4e | -5.3382 | -43.7391 | 2025-10-02 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3b446fa1-018a-3a8f-9037-98482420023c | -13.7864 | -48.0524 | 2025-10-02 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b0e19f5c-355a-3c4f-81bd-8409d674d992 | -10.8517 | -47.2541 | 2025-10-02 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| bf18c323-497d-36bb-8c78-b620a9ce6cc6 | -14.3139 | -45.8811 | 2025-10-02 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 2ef6fa4c-642d-3df6-bbdf-d44039289d75 | -13.7962 | -47.5362 | 2025-10-02 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9e2eaef5-9e52-395e-b8c1-4bdd24975dce | -9.3199 | -45.7288 | 2025-10-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 2b58024e-5bce-352f-a973-21f971bdb9e6 | -8.5272 | -47.2437 | 2025-10-02 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 150d3dc9-34be-354a-b479-40a740bcc20a | -14.3119 | -45.9736 | 2025-10-02 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 0e8f8199-513f-300b-b29c-64cbcbe88f5d | -7.8882 | -47.281 | 2025-10-02 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 489b6d96-ca61-364c-bb23-6030cb31485c | -8.5671 | -48.6408 | 2025-10-02 14:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f707f823-6820-32a3-8f57-502414cacd5b | -9.4083 | -47.5742 | 2025-10-02 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 92ac3b0d-bd02-3d98-8f2e-c0d315ab5826 | -11.8254 | -44.9205 | 2025-10-02 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 36df6dc8-2b1a-34b8-9834-f08cb74c7553 | -13.8065 | -51.2164 | 2025-10-02 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 888c5a46-e8e6-307d-9fd9-5f1373b77ee5 | -11.0238 | -51.0767 | 2025-10-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 42dc08fd-429d-3fae-89b7-da61f213f3b2 | -13.9779 | -48.1346 | 2025-10-02 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ddcdd9bf-d2b1-3616-bfb2-8e94f1aa66a3 | -13.1743 | -47.8093 | 2025-10-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 394325b9-b263-374b-b53a-2c08894a331a | -12.5001 | -50.2453 | 2025-10-02 14:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 26722ac1-4e7c-30d5-84d9-da0005635212 | -14.1917 | -46.1552 | 2025-10-02 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 9c682d57-27f6-3477-8e53-9f1f6791a574 | -14.2121 | -46.1058 | 2025-10-02 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d5ddaf5f-097b-3915-8cde-42fac40d1e70 | -6.7816 | -45.5703 | 2025-10-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 1d8e8ccb-a761-302a-9796-c1ade665d69b | -13.7684 | -51.2 | 2025-10-02 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a84bc014-e114-3f9e-a756-2279bacf6d9e | -9.9031 | -45.978 | 2025-10-02 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c4128ecd-c62a-3f97-b8ca-368fd2acd386 | -14.407 | -46.0722 | 2025-10-02 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 89ddd27b-ee26-3475-9f52-209a3b7385e0 | -6.6978 | -42.8118 | 2025-10-02 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 13c6c7d3-0bbf-3445-b2f7-78ed1fc9a4a3 | -13.5841 | -51.8845 | 2025-10-02 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 1e38a6c1-9360-3aa9-be56-936ea1043315 | -14.4065 | -46.0953 | 2025-10-02 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 406.7 |
| 9698b8a8-5002-3afa-a0ed-0296507e55a1 | -14.4255 | -46.115 | 2025-10-02 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 223.8 |
| c35233f6-1cb7-37fc-832c-52a7469c6845 | -7.7311 | -46.2289 | 2025-10-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 90aca183-0c37-307d-8425-30727b51fad1 | -18.2171 | -53.3392 | 2025-10-02 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 58cd1dbf-8d24-3c9f-899b-b8bf0562a7bc | -6.476 | -44.2748 | 2025-10-02 14:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8e5e671f-35b5-30d0-b6f0-2083dfc02467 | -13.194 | -47.7841 | 2025-10-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1893fd00-66a4-353e-bc7a-869ffabd8cf3 | -6.4945 | -44.2962 | 2025-10-02 14:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d70b12c3-372d-3c16-b553-4e31b442419e | -8.6534 | -47.6943 | 2025-10-02 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0f65c3d6-8eaf-3f4a-8cf3-87244b98a9ed | -9.8896 | -46.9226 | 2025-10-02 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c73e3f34-7f1e-3d16-8565-6565bddbfa71 | -11.8104 | -51.7746 | 2025-10-02 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1d8ff75f-3063-3821-be37-b2accb0f80f6 | -8.5204 | -47.8167 | 2025-10-02 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| f34c481c-0caa-3c4c-bd8c-c8b74be4fb3e | -7.9067 | -47.3014 | 2025-10-02 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2ae516e5-0f77-359b-9aa8-3e3bea939780 | -18.1782 | -53.3024 | 2025-10-02 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 805e923c-48cd-3efa-be50-98414996008e | -13.7864 | -48.0524 | 2025-10-02 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 97d48113-ba3b-30cd-91f8-925ee3086982 | -6.6978 | -42.8118 | 2025-10-02 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 9b166d15-952c-3d0a-ad84-df75d1576b6f | -9.7851 | -46.2851 | 2025-10-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 853e0818-2b46-389d-820d-faff3484d0b5 | -13.7962 | -47.5362 | 2025-10-02 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 881dd481-9814-3e9c-8737-9993e4348ee5 | -10.1267 | -50.3398 | 2025-10-02 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| bc3b6196-1219-3ac4-936b-1497b2513c29 | -11.5878 | -47.6502 | 2025-10-02 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bb652387-5111-3e5a-ab96-afd971217657 | -8.527 | -47.2658 | 2025-10-02 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 72d6a919-67c6-36f8-8c0d-cc2f0bf2a9d5 | -13.1743 | -47.8093 | 2025-10-02 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| a798e164-f207-3392-9850-0e35208ebe25 | -9.4368 | -45.4884 | 2025-10-02 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0545d1b2-a616-3581-a6c7-50db02bc6ea3 | -12.8442 | -46.9385 | 2025-10-02 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d2eea110-d7e5-3543-9224-3100250dd17a | -8.1917 | -47.0101 | 2025-10-02 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 00ee4dcd-f8da-33ea-86b3-93b16d29ace8 | -14.407 | -46.0722 | 2025-10-02 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 155.9 |
| a4aec9f6-10f1-3168-85c9-b1b11cc5abc0 | -9.938 | -43.6718 | 2025-10-02 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e688a585-662c-3f9e-a0e4-80c0e17ee191 | -8.6534 | -47.6943 | 2025-10-02 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 58cb6bac-f936-30c7-b60e-d51e43f18cd4 | -11.868 | -48.0126 | 2025-10-02 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8e2e4bc3-fa05-31df-94f2-dfbe60106fb6 | -9.4083 | -47.5742 | 2025-10-02 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ed767508-183e-3bb9-a01a-f174e124300e | -14.2121 | -46.1058 | 2025-10-02 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 153.6 |


[Clique aqui para ver as próximas entradas](README162.md)
