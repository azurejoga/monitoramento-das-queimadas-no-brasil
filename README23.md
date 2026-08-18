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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52210341-cd5d-3aa8-8ee9-41d10dfe8b51 | -4.01245 | -48.90812 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 9cb35631-977a-39d4-9a1a-8dc3e18c51a6 | -8.03927 | -50.10588 | 2026-08-18 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4093ddd9-2e61-3a3d-8542-a0e990f18b5d | -8.33003 | -46.48779 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b854e2be-46d9-37ea-8bb2-8becd42aa0f6 | -8.58124 | -54.73735 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| aa5664b8-1d58-3e1e-9d9b-c6b188dea6da | -8.56283 | -54.7006 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 17de916c-cd4b-3728-827a-15b0e9341744 | -8.5497 | -55.3149 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e636615-96be-315b-ba71-499efe8fe81d | -8.56963 | -54.69078 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3049534b-eb62-3cad-8eb2-1e3a52762484 | -6.7465 | -59.17095 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d9bd63c4-e28b-361e-b1cf-abe866ed6fd4 | -5.27018 | -49.0479 | 2026-08-18 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 358e1634-4abf-399c-b59d-b74ebd3adc58 | -8.55125 | -55.30613 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fd1dda3-5fee-35e9-944c-a8ec0898befa | -8.20531 | -55.02571 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1ee84f3-c6d7-3e67-9e27-98eba789bd76 | -3.6824 | -47.64676 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d1845f09-b6e5-3680-aef9-b72aabf0ee77 | -8.54681 | -47.49168 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7003869d-9594-3e78-bd0e-ed9ad4824540 | -9.12668 | -45.17766 | 2026-08-18 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2f60d6c-636f-3a09-ab3d-70916099a4ee | -5.56981 | -47.44936 | 2026-08-18 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93b970da-5aa7-3574-87f5-edede6bf9dfa | -8.49221 | -48.80222 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a7944ee-ca67-3621-a410-e41d67888166 | -8.55418 | -47.38143 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53c706a2-4722-3f40-8e66-bd6c0183ae10 | -7.13482 | -47.51336 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e29ab8-a0ba-3e32-8aaa-cd0796e36c1b | -8.63748 | -54.70308 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3db36cd4-7eba-3646-bde6-f4e954aa8ab0 | -7.16514 | -43.13853 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a32e5431-8947-3f16-9369-eb6a5bf851c5 | -8.55639 | -47.38897 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2d4b6ee-3206-3976-b006-3d34612237cb | -7.62896 | -45.74118 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06af9b2a-3c43-3c58-a493-4662cbf20602 | -6.53582 | -43.11452 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5176404-d2a3-3eb7-8d60-6135bb2bfed1 | -8.5822 | -54.73204 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f93b5b32-2059-3147-bf71-f2010e10e6a6 | -7.5342 | -55.58167 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ea7fd7-cce4-3da4-9437-2b72a5f8013e | -7.56517 | -55.558 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5cf9741-5853-39bb-89a5-d9c6d7077cb6 | -8.56265 | -55.31762 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d11131d-7bce-329f-b425-2d14fd28f585 | -4.53323 | -42.93758 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3223f9d-368f-3504-8406-024280276100 | -8.57933 | -54.72017 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 24be1c94-91b5-36e1-96e4-93c9f71cb4ee | -8.49193 | -48.8253 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9ddb7327-14bb-3d55-8bb8-ab4e9c58e908 | -9.77178 | -47.28011 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cac92aee-46d1-3cb2-a30e-67d63e88c595 | -7.02107 | -45.90551 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b27a51d-4812-328c-9113-745a7bf8eb49 | -8.5952 | -50.35412 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bff6524b-76b2-385c-a7f1-fdd976b2c857 | -6.10633 | -57.7429 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a2f9c03-c49c-35d8-809c-bb952d0d945d | -8.37083 | -46.3583 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a04feb51-46c4-3b9a-8d88-82bed1107416 | -5.14336 | -56.27912 | 2026-08-18 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9f3bf19-52f3-36ff-901d-c8f04db0b25b | -9.89869 | -47.7357 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd96e8f7-26b9-3efa-9d59-c98b80a80332 | -3.51079 | -48.0317 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0de18f99-7216-306c-af38-f1f0b15ec431 | -5.67152 | -43.57941 | 2026-08-18 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b05ce1e-492c-3bb5-b822-4ee6428f0688 | -8.57448 | -54.71925 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| a99af7fb-4766-39fc-a662-77dc798d7180 | -6.70567 | -58.93519 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c35b1f9-59c9-30ad-a7ed-7b5faea623dd | -9.19858 | -49.965 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cdaa3bfc-7f94-3ee9-a202-6021e8b8c916 | -6.73868 | -59.17583 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 150535a0-b9a8-3611-b41a-969032123c33 | -6.96116 | -59.03585 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 464e2631-4638-30c2-8a5e-d22c3f485575 | -7.62829 | -55.62289 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fdbc6d8-cc7c-3b79-931d-090a43b86d2d | -9.07811 | -50.84128 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ef50e97-ea13-3c7b-897c-cc3c28392274 | -3.42566 | -51.51527 | 2026-08-18 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4868068-08ed-327e-8560-abef86698714 | -9.06551 | -50.82459 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 491a4ac0-14f2-3f0e-8656-f6f62cf3cd3f | -3.67355 | -50.94716 | 2026-08-18 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acbbcee7-2a3c-32c2-af83-653cd6b79652 | -9.02606 | -45.84944 | 2026-08-18 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c28f63a1-dbdc-34e4-97ca-285d8da9ac40 | -7.64104 | -55.64204 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faf0a626-5663-3e6b-b8d8-82fad09602a8 | -7.1236 | -47.54052 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14f863e3-48e2-37cc-8220-e715a90aeccf | -7.17682 | -43.13587 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f85196f-779e-3526-adf2-b8db045eb6fb | -3.50567 | -48.03508 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50415485-af95-32f1-b2f3-a9135dc4946b | -6.751 | -59.18341 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3c3474a-9949-3092-b716-0f33f8295692 | -9.79502 | -47.30538 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68808113-6643-3aaf-86ee-aa9caaf4d455 | -8.37028 | -46.3618 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 397b6bc8-2a39-3000-9bcc-e7822e494849 | -8.50615 | -50.4213 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b495a9-08e0-32b0-87b2-48d09e279a22 | -8.49536 | -48.82587 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 991fa965-88a5-34a2-b2ad-c92a23f371d2 | -6.16028 | -47.79667 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab1d9ff2-1e6c-35f2-8505-86ef38cde3d1 | -7.15647 | -43.1461 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c081e83b-f6d0-3b14-8159-e6e94465032e | -10.289 | -48.23844 | 2026-08-18 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1711e077-dfd3-302a-909b-d6dfea9e7cbc | -7.12581 | -47.54819 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3111ac4b-d393-3cb0-aa77-6f9001f70ebd | -6.30578 | -47.89029 | 2026-08-18 04:38:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f20ab533-c84c-3d7d-bb3d-a21a25650719 | -6.17823 | -47.81438 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d9f893d-983e-325c-936a-e601574b3c59 | -7.02162 | -45.90199 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0036e614-c04e-3624-87b5-b524859bebe6 | -8.63262 | -54.70228 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97daa50e-e285-38d4-b378-cb246f1e1851 | -8.34051 | -46.46444 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91c77be9-ea1b-381a-b208-ddbab6a78312 | -7.60539 | -60.83594 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ff70e9e-adbb-3c75-9bea-e319572435c5 | -6.84727 | -59.00052 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b487cfb-9eb1-3e07-8448-f97185fc5f5b | -8.59742 | -47.36691 | 2026-08-18 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba8bcdf8-e979-39a7-a729-c018a01718a7 | -8.4877 | -54.91016 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a91d36d-0f55-350a-8fb3-ab4f6ff641c5 | -6.75087 | -59.16854 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 864731fa-1397-3b8b-97f0-55a9803fd8d5 | -3.20831 | -49.05924 | 2026-08-18 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f8f9d68-c1ce-3151-bcac-70ed2666856d | -8.18718 | -55.01556 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a328ab8-3813-3673-b775-d2a14e4add2d | -8.10453 | -51.65788 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e79caa32-7785-3569-85eb-c412bacff510 | -8.48869 | -54.90459 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c1df814-7d65-3169-a015-d8ff4a3fe4c7 | -9.40694 | -48.24874 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f94aa7-33ad-36df-b570-0a1cb865a423 | -7.53364 | -55.58485 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5564270f-0f38-347d-a290-b309ab9a9a9f | -9.89926 | -47.73219 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c7d976-df74-3423-a521-a25f4595ae56 | -8.56439 | -54.70364 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f07ccf38-288b-3d2d-b0dc-011ba0a3e150 | -8.57638 | -54.73645 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2d1edfe6-35de-33f7-b72f-10b1aee659f2 | -6.85483 | -58.9965 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7899781e-0e04-3935-a631-0b2e0d4714bd | -5.26595 | -49.05138 | 2026-08-18 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff1328b-f71e-3f89-a0f1-0c4d5b7356d3 | -6.40407 | -54.94884 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c85044-5ac6-33c0-a6fa-c16f82863311 | -8.7968 | -49.20564 | 2026-08-18 04:38:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dae963a5-e03b-3f99-900f-837328bf1a1f | -7.64602 | -42.76163 | 2026-08-18 04:38:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 969fb1fe-2c36-3bc1-84de-f8e97a438455 | -8.59739 | -50.34107 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cfb71aa-71f2-3f2b-ac1d-63f1944f695e | -8.5996 | -50.35041 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 859eb9a4-c36b-3899-9c8b-4ebac588f38d | -7.63231 | -45.74171 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d83e6269-5f9b-39ed-a667-10e590d0a2f3 | -7.56285 | -55.57081 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01433bb-c551-37d7-aad6-01e803f2ab10 | -7.282 | -44.07341 | 2026-08-18 04:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2295b1e6-e8ce-3743-b8a8-06584484f7fe | -7.17143 | -43.12184 | 2026-08-18 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0a7f6c1e-4aeb-3b59-970f-ddf6283d6333 | -7.6128 | -60.95889 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ddbcaa5-acc5-3953-8063-d5e12714a40f | -8.55813 | -55.31377 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc0673f9-9864-3c48-a25a-35def5464ca2 | -8.56252 | -54.71436 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35cf1cc0-582f-3d8c-9c2f-82f421f99c3c | -6.74538 | -59.17682 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1c84218e-1774-3435-9b8a-b09cb0851e5e | -9.0707 | -50.83951 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1ec78b9d-c2f3-3420-8dd2-e9559b130c80 | -3.51324 | -48.03235 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b76c811-aefa-3a96-ba96-f3a0438df08f | -6.75857 | -59.16413 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README24.md)
