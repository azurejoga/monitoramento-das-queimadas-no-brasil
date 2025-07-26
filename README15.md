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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b179b8b-ce88-39f6-b42d-58179a8f15b9 | -6.66043 | -58.85699 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| e010c3a8-26d3-317a-bf64-5b9385c6b1aa | -9.46254 | -57.85088 | 2025-07-26 04:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58328750-837b-3f67-94e1-81001ce35c7a | -7.83893 | -46.88493 | 2025-07-26 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c64fcdb-acbb-328a-b30f-595154a2d9bf | -6.58269 | -45.6054 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3f6863a-8414-3797-bb65-123416a257b1 | -6.64614 | -58.82573 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b3c35bec-e67a-3556-9599-443f871cd6b8 | -7.94872 | -44.8845 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09137d6a-7bd5-3cf2-ab91-dfa8c65ab88a | -9.00224 | -45.34512 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c315269-6f5c-3ee4-9c94-a950e004397a | -7.53621 | -42.42363 | 2025-07-26 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4f300603-05f4-3339-9db2-1e76e87386c6 | -9.04287 | -45.374 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c58256c7-a1fc-3e70-8893-c18abba2b15f | -5.14236 | -45.17328 | 2025-07-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff50068-69f1-33ea-b109-36babb1995f8 | -6.57263 | -49.50039 | 2025-07-26 04:25:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 822c86cf-f973-39e2-a7ac-405057d78e15 | -6.41261 | -41.14872 | 2025-07-26 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02aab926-6787-384e-8ee8-d81718760d29 | -6.63445 | -58.85182 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f29737ce-ffdf-3782-9796-eed5a70122ce | -6.65381 | -58.93414 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eff1184c-c9b2-3e67-bfe8-0e63f3b1ce1c | -6.3282 | -44.09776 | 2025-07-26 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f91077d-a8a1-33e2-9b23-912c33d2ebfd | -6.86784 | -43.68259 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b426043c-ecfb-38cc-a7d6-3d61025aacbd | -10.66303 | -46.63674 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a04d47d-2227-3505-9257-b7c6795c3681 | -9.36205 | -40.30783 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 4216c9e4-74a6-3112-8992-845fd59771bd | -9.24898 | -50.22562 | 2025-07-26 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08225f9d-ec0a-3dd7-8792-297844673150 | -9.73499 | -48.01752 | 2025-07-26 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d418ce9d-8c99-3368-9a69-6d4a558de6d0 | -9.02594 | -45.34887 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63441ff1-0c01-3fbf-ad91-161b345c9f45 | -6.65605 | -58.84448 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 181.1 |
| bfc970b3-100d-3d5a-bf95-3ec31ad54b81 | -7.23821 | -43.06133 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f54a0b59-824f-3300-a467-9c582c42a850 | -6.90377 | -44.29903 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a024bbb1-b3e2-3373-8e16-0890c0c51895 | -6.63302 | -58.82614 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 610d8ae6-52be-325d-be60-fba2e5b18035 | -6.32752 | -44.47119 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92436095-e909-3fc5-baf0-7186c88216e8 | -6.70269 | -43.06711 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca911935-b352-3648-b18b-e061d16f1df8 | -6.66694 | -58.85817 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 1c901e75-886f-3483-8b4e-d67e1f7fd951 | -4.57663 | -48.01784 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f342ba-7446-314d-bcf9-1f9e681f686c | -6.63654 | -58.8436 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1dc4115e-f6fe-35da-9bf9-fb5b027bf333 | -6.23362 | -43.71582 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c3a50d6-f924-3c4b-960a-6a30422ea30c | -6.23183 | -43.72749 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 88d9f47a-b60e-3727-8c18-aeb67eb4e26c | -3.75504 | -49.05301 | 2025-07-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07711691-3a76-3835-b439-90cb424a7c38 | -10.63082 | -48.11226 | 2025-07-26 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eb3fc06-b27e-3eeb-9b9a-ef566b64e4ee | -6.65841 | -58.87147 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b5a117e-c729-3913-9457-6cd6d4cf13b1 | -6.63006 | -58.84229 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 12482db1-1a15-3b01-924f-75f0f03c9dbd | -5.74577 | -43.97283 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5963195-9147-3220-a576-f40bda4ef1e4 | -5.67946 | -42.78888 | 2025-07-26 04:25:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3442929a-c4b4-312f-8b89-2048846ff595 | -9.13516 | -45.87128 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca478097-c934-39d3-a493-5b976b4ea0d7 | -6.2283 | -43.72701 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9a2f27d-a1d3-34d2-959f-983fe611e82d | -10.43245 | -44.18097 | 2025-07-26 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83e1b5e-c92a-3b78-b4e9-765015d2ded8 | -6.67243 | -58.86842 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a27ece2b-b7ae-3b5d-840d-becd7ed0ac1b | -9.27082 | -50.25848 | 2025-07-26 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 664cc8dc-c612-3b78-b79c-8de43f8844b4 | -8.81122 | -46.75217 | 2025-07-26 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ade0d4ad-9d55-36bd-9b93-22983de09125 | -6.55936 | -41.50504 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c0ae6997-125a-3bfd-bd5e-1437ff02c294 | -9.36717 | -40.31432 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| f21a38e5-1232-3a99-9c3e-e0aa2e39923f | -9.71358 | -48.94706 | 2025-07-26 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427ac1be-b953-35ed-992f-38098a642fe3 | -6.68851 | -58.85085 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8953d1c-7a95-3d2b-9fce-e2e10eae3a9a | -6.32081 | -44.08521 | 2025-07-26 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77ace358-b83c-3686-b011-995c71074278 | -10.13368 | -46.72249 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25040493-3067-3657-bcc5-a407d8a25674 | -7.24181 | -43.08236 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9fe8cbb7-cd5d-337a-af31-f84939b44772 | -5.13902 | -45.17278 | 2025-07-26 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2566f445-1f42-3854-870a-8f0e9bcda215 | -6.65427 | -58.92561 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00c1246c-dc64-3c52-89fd-88fdd43e92eb | -6.65027 | -58.91635 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50081d6e-dec8-34e2-900c-8fe8e29025e5 | -7.56512 | -44.48629 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65a4656d-d701-3d2e-9fd9-247c1cb2e9c1 | -6.68399 | -58.84158 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| e41a4984-77af-3baa-9091-82650f762b25 | -10.84355 | -46.69807 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4b2e143-ef81-3df6-b077-782dd6b0678f | -6.87675 | -43.67168 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 789cdcb5-dbae-31c2-92ca-8b776e21986a | -10.36913 | -44.08583 | 2025-07-26 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b816d660-39e4-3579-b08c-6436d12d3a29 | -6.6655 | -58.83232 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d370f2b2-f6bb-3209-9543-afad57578fe3 | -6.88028 | -44.1975 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a05c494a-1332-3205-b3ca-2c4565d666a1 | -6.65166 | -43.08257 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03217925-efa7-34f4-a2c6-22457da7c019 | -7.78881 | -44.55319 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a6a2083-54d9-3283-a8eb-01e689d5b5cd | -10.59328 | -44.74694 | 2025-07-26 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45dc34fa-5225-367b-ac1e-a773679aed6d | -5.96204 | -46.4659 | 2025-07-26 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35e08086-4e81-3e7c-b6a6-a53859f7b106 | -6.65393 | -58.859 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4beb4083-7021-3f45-9c0e-f698d5bb8198 | -9.73442 | -48.02105 | 2025-07-26 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1f1dc82-23d9-3760-bb73-c32a2be85a5d | -6.14562 | -43.82251 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d843478e-db43-32cd-a17e-64e80d4e07dc | -6.42025 | -41.15351 | 2025-07-26 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 233b71ac-abf5-32d0-a32f-95f1b96fc73c | -9.37044 | -40.31368 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| e8fbc2e5-faea-331e-b6b9-0ea7005becc3 | -6.99213 | -47.08395 | 2025-07-26 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 279f2b3f-1ccd-3329-a47f-7028cce6e5f2 | -8.87168 | -45.57774 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab27364-f794-3a6d-a9ad-3a3375a6d7e6 | -6.65916 | -58.82798 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 87d937e6-123f-36bb-87e1-2ac0757b7419 | -11.59664 | -43.20612 | 2025-07-26 04:25:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d938719b-e775-31fd-a6a2-32e904053e7d | -6.65076 | -58.87254 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39da4298-27f2-3ea7-96cf-caa0bd6223ae | -7.36333 | -46.21684 | 2025-07-26 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f9b8c89-8b10-3e88-a145-18c2e031a6f0 | -6.65773 | -58.91246 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d8da412-dd05-337c-ae1c-b947c0b1fdab | -10.35992 | -46.64355 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 742fd086-1470-3fd9-be95-dd6c57113ae0 | -6.12121 | -43.15255 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1587d070-45b2-3776-85de-5df5fc653c47 | -6.6453 | -58.8657 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 698349b3-3d62-3928-b041-30a9589f4172 | -6.67449 | -58.85386 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 80d4dac4-6400-384b-8e04-ebaec12dae60 | -5.74346 | -43.96474 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edfdd7c9-78a6-3d37-9e79-7a8a6f14baf5 | -6.00962 | -52.17237 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c45a5a20-f814-30dc-b405-604b27e873d1 | -6.40854 | -41.14805 | 2025-07-26 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f641c018-e21b-3617-809e-2bd75efbbe5d | -9.36264 | -40.31366 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| cbd0a288-4054-386f-94ff-9a0914830013 | -6.5289 | -44.5962 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da82387e-569b-3a3f-bddf-58b82c35be07 | -6.63861 | -58.82994 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 23f953f7-9590-3aca-8f14-56a5b9d5b5a7 | -5.4532 | -42.65182 | 2025-07-26 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 798470f2-3e44-38ff-976d-09e7e9e852bc | -6.65102 | -43.08679 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46cdb77d-4201-3bb9-9016-7069089d853a | -6.65265 | -58.82685 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| cb715ea3-f090-3845-a22a-4c19c39fa488 | -6.83663 | -43.62423 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30855d3b-3666-3bea-838e-ce5c056f082b | -5.24633 | -48.49907 | 2025-07-26 04:25:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 995f75d3-d794-39b3-b39c-9dc383f8a1ea | -6.67951 | -58.82916 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 104b929f-2763-336a-a118-0dd6452b6320 | -6.8853 | -43.11919 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5db4a3c-5cce-36f5-91d2-9bf1940b7f22 | -6.66462 | -58.8347 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 2e4e53bc-57b7-30c1-b008-64ea6eca2be5 | -6.33224 | -44.09454 | 2025-07-26 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4247c69-81b1-3467-90f5-c299c7376151 | -9.12759 | -45.98675 | 2025-07-26 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0bf2416-1861-3205-b0d7-c94c1e324449 | -6.68517 | -58.8327 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b05f319c-1ce4-33ca-82a0-238f82a12965 | -6.65189 | -58.87024 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 619a5582-864d-345a-bf72-70ee1098c4c8 | -7.24069 | -43.06439 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README16.md)
