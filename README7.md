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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd684f6b-d6cd-306d-80b7-aff5f883c979 | -3.2321 | -46.7836 | 2024-12-17 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a794431b-f3cc-3bfe-b2a8-3c47772fea35 | -4.7952 | -46.4012 | 2024-12-17 02:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1d073703-439b-311c-b5a0-eabcbb09c98c | -3.232 | -46.8056 | 2024-12-17 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| bbfa48c4-2efe-3bbd-8123-d5ed8a09b5e4 | -3.2507 | -46.7829 | 2024-12-17 02:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ecf321b0-018a-3146-9cca-952cda11b61b | -3.2506 | -46.8049 | 2024-12-17 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 206.9 |
| 3733632b-9833-3ef7-80b0-a2cb24550380 | -3.2969 | -53.3547 | 2024-12-17 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 28c141e3-d56a-33c4-84a2-1ef3df85f4a0 | -5.1123 | -43.9164 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 69782d75-a9ba-3934-8638-84899bffbb17 | -3.2506 | -46.8049 | 2024-12-17 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 990adc05-cbe9-3dd4-be2f-73a9db3feca1 | -4.7952 | -46.4012 | 2024-12-17 02:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8c929f18-c0e6-39cd-ab96-d75e8b4b3e07 | -5.0936 | -43.9176 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 679.3 |
| d6d71317-f4a2-35fc-9e53-d7bd951d82f6 | -3.232 | -46.8056 | 2024-12-17 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 8b62e886-e443-34fe-a1f8-ca9c6639ed5a | -3.2321 | -46.7836 | 2024-12-17 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f2dc1082-fc81-320a-9b08-7d9fce6ce48c | -3.2968 | -53.3749 | 2024-12-17 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7cabdb05-3704-3d81-9760-901b814791b3 | -5.1125 | -43.8933 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| c78bada7-4720-3d42-8127-a429703e283f | -5.0938 | -43.8945 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 496.3 |
| bc696cd7-e196-3db2-990e-d34e70526e5e | -5.0749 | -43.9189 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 246e80b5-08f8-3d75-a5b8-fd367d92a6d5 | -6.214 | -46.2202 | 2024-12-17 02:50:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1ec80e8e-afcf-3cbc-b68f-4c44ca94846f | -5.0751 | -43.8958 | 2024-12-17 02:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| d63b139a-5395-343f-a918-55f6824064a5 | -5.1125 | -43.8933 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 0036d817-49d1-3eba-8234-d3137767b27e | -5.1123 | -43.9164 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 13bc54a2-a3b8-34a3-97ea-c0c1835a53c3 | -5.0936 | -43.9176 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 460.6 |
| 9a3c3a4c-c2be-31a5-987c-e1fb7c936921 | -4.7952 | -46.4012 | 2024-12-17 03:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2f7d2b38-2f0e-381b-94c9-7aa311b50fb0 | -5.0751 | -43.8958 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 01889405-dec6-3486-85d1-18cc9643572c | -5.0749 | -43.9189 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| e326f336-3b65-3149-8205-9f292c174304 | -3.232 | -46.8056 | 2024-12-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| f950fec7-973f-3f69-b7d0-a90dcf60da54 | -5.0938 | -43.8945 | 2024-12-17 03:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 342.7 |
| a5831923-3366-328a-9615-5364452fe9f4 | -3.2968 | -53.3749 | 2024-12-17 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b8f05d1d-4325-32e4-8b83-0c85f5b05a76 | -3.2506 | -46.8049 | 2024-12-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4e5d4858-35d7-372d-9483-f28864e8c1bf | -5.08 | -43.87 | 2024-12-17 03:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3d931f7-76e4-3342-b060-b3d36ea5f6a5 | -5.08 | -43.91 | 2024-12-17 03:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bce0aa7-dc2a-311a-a91e-200bf23f3f2a | -5.11 | -43.92 | 2024-12-17 03:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8de86776-94c0-39ea-a3db-dff4576e49e7 | -4.73718 | -37.80427 | 2024-12-17 03:04:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7414cc57-5794-3063-a02f-f5fd4661e0b3 | -4.74044 | -37.80179 | 2024-12-17 03:04:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a3e3ff1d-49eb-359f-92f6-b262120fe8fb | -9.27782 | -35.91058 | 2024-12-17 03:04:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6715a52f-94aa-338f-bc9a-c20c6d671f0a | -9.2766 | -35.91217 | 2024-12-17 03:04:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc317110-1a3a-3dc9-9242-3d0fec87a3bf | -6.74639 | -34.98051 | 2024-12-17 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 505a31bc-cb57-3520-8fef-8a503cb462b9 | -8.75801 | -35.74958 | 2024-12-17 03:04:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cae159b3-eccb-35c6-b9f9-5280f3a871c9 | -6.74697 | -34.97718 | 2024-12-17 03:04:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b55075e-103b-3af5-9252-8fd6ef47f730 | -5.52682 | -39.18236 | 2024-12-17 03:04:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 404344e5-f1a8-3779-8bf3-b834c6b6f171 | -5.53386 | -39.18378 | 2024-12-17 03:04:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4382f05b-4445-363d-b1d0-0d8b514d7301 | -8.75857 | -35.74895 | 2024-12-17 03:04:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47993491-04f7-34ee-a958-952a7f9c77c3 | -10.60522 | -37.00177 | 2024-12-17 03:06:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8efa7e5e-cac7-3d06-942c-ab80dd45c869 | -10.60449 | -37.00554 | 2024-12-17 03:06:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5a017ac6-8ddf-34bb-b244-8ea472a88231 | -5.0751 | -43.8958 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 35ebd329-efaf-31f1-8ae0-77aaa69f014e | -6.9346 | -43.5168 | 2024-12-17 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 9f4aae17-9f19-3ade-8064-6e2bdde3352f | -5.0938 | -43.8945 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 293.4 |
| 26f66460-9968-3bc7-85ec-66e6aa1948a4 | -3.2968 | -53.3749 | 2024-12-17 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| e4317c0b-f29a-36ac-9cfa-1165696469c8 | -5.0936 | -43.9176 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 342.6 |
| aa9f892f-4692-3126-8757-b43cdc61e312 | -4.7952 | -46.4012 | 2024-12-17 03:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| af9fa767-003b-38eb-a8b3-37beeea273cc | -3.232 | -46.8056 | 2024-12-17 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6aabba2e-d314-39dd-af74-4861939edffc | -5.1125 | -43.8933 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 2c2af46c-90e8-3f91-9898-ab7df40c7c2c | -3.3152 | -53.3744 | 2024-12-17 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c7105a0a-74f4-3c5a-af72-599e30a3df73 | -3.2506 | -46.8049 | 2024-12-17 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6b5bc2b1-4f56-36b3-a164-0b0205c34dd0 | -19.1043 | -52.8493 | 2024-12-17 03:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5dd94a38-4a47-3cc2-9142-da706418bd7d | -6.9349 | -43.4934 | 2024-12-17 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e22ecfec-3144-37f3-8b73-e4c07a908a4d | -5.1123 | -43.9164 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| c2472d39-3843-31dc-a807-159ae0f01585 | -5.0749 | -43.9189 | 2024-12-17 03:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 39cef573-52f1-3483-94a9-ead0009a1147 | 4.4435 | -60.9657 | 2024-12-17 03:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b6ef2d1a-2048-3612-a3de-97918bfe1ddd | -5.1125 | -43.8933 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 0a3982ac-6fe3-3238-99ce-f55b5e785e9d | -3.2968 | -53.3749 | 2024-12-17 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| df63844f-7259-3420-a95a-c5399d9a994e | -19.1043 | -52.8493 | 2024-12-17 03:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c82151bc-011e-3615-8d8c-72385c043921 | -3.232 | -46.8056 | 2024-12-17 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 56900d8b-6969-3191-ba75-e109c003d4c7 | -5.0749 | -43.9189 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| c13dfe69-9ac8-3793-9094-dd873cf682f6 | -5.1123 | -43.9164 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| f2eefe27-8f90-3b51-b24c-4a658c8c811c | -6.9346 | -43.5168 | 2024-12-17 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 67eb09a9-0858-3a08-a966-9050bfe82892 | -3.2969 | -53.3547 | 2024-12-17 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| dfab65bd-9e81-3dbc-aa77-c09053de5004 | -15.0672 | -59.6504 | 2024-12-17 03:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 544aa50c-6a16-32fa-a3d9-e178184563f1 | 4.4435 | -60.9846 | 2024-12-17 03:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 112.3 |
| a11ce386-6a39-30b5-a0e3-96f148ba391f | -5.0938 | -43.8945 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 308.1 |
| c9a89cf6-9012-334d-a299-665f94fb8a49 | -6.9349 | -43.4934 | 2024-12-17 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 14fbebbc-b518-3fd5-b111-ea4e7f6af3e8 | -15.0865 | -59.6487 | 2024-12-17 03:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5db59718-f88f-3874-a0d5-253717013cc7 | -5.0751 | -43.8958 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 33df80f5-c58f-3d75-91c2-9604c6ccb88d | -5.0936 | -43.9176 | 2024-12-17 03:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 330.5 |
| db531930-ac9c-3be7-b869-18eaf2e8d513 | -6.9158 | -43.5185 | 2024-12-17 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b420aba6-8160-3b02-922e-051ec3d1bbf7 | -4.89881 | -42.08321 | 2024-12-17 03:25:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3fa57102-2d5c-3798-9c42-51675f95c762 | -4.89982 | -42.08318 | 2024-12-17 03:25:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0e0a524a-5446-3fe4-9963-57a4636044e0 | -4.65603 | -44.32952 | 2024-12-17 03:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d3b162ca-b9cc-3b91-9e4b-2b47949566fe | -4.73975 | -37.80407 | 2024-12-17 03:25:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9756548-24bd-361d-980a-ec58097d924f | -4.65492 | -44.33575 | 2024-12-17 03:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 78f8546a-4189-3cf6-87cd-f2311d367dd0 | -4.16215 | -40.93162 | 2024-12-17 03:25:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d796871-33e0-3d50-aa7d-6820b630fac1 | -5.13511 | -43.241 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48915c9e-633b-31f0-99f0-9baf1cdfcb71 | -5.13938 | -43.23819 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34a96bdd-ed23-323f-890a-a3741a8c8c4d | -5.51116 | -36.83951 | 2024-12-17 03:25:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eb0c9b6d-8283-3bcf-8f20-9507ee2e814f | -4.96416 | -43.72411 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eac8939-2ea9-3d9a-9746-a4444eec515e | -5.21538 | -43.30378 | 2024-12-17 03:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e8f5dba-70ff-3cc3-99d5-87f253833439 | -4.67489 | -44.04594 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd64b068-152c-36aa-a902-2d2e1019cf60 | -6.21364 | -36.67958 | 2024-12-17 03:25:00 | NOAA-20 | SÃO VICENTE | RIO GRANDE DO NORTE | Brasil | 2413003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 508bff12-12f5-3a01-b9bb-e05ef34088b1 | -5.08345 | -43.91873 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 54a3af74-3be1-3dcc-b1d1-131d1c8d0ac2 | -5.09191 | -43.90895 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| bc4f849d-d92a-38f5-9920-08c518f8d74f | -4.95861 | -43.71776 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d57801b2-0f2d-38e4-8e67-f2843223c9e5 | -5.12017 | -37.33492 | 2024-12-17 03:25:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0cd78dcd-5cda-3156-9e88-b30206dc52fb | -4.74045 | -37.7998 | 2024-12-17 03:25:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee9fcd47-e48a-3b0e-a7ca-9546f5f2b5c2 | -4.67986 | -44.04379 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 318d5c3f-de30-3be5-ab1f-07f0780c74df | -5.09642 | -43.92146 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| cf29894b-fbe9-33b4-93b0-c8e84d219400 | -5.21187 | -43.30251 | 2024-12-17 03:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fb6fdd2f-d3ef-38b5-9485-e9d8fdcf4287 | -5.11536 | -43.20652 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a2abe6b-0a06-34a9-b698-1513cf280e3c | -6.39384 | -35.986 | 2024-12-17 03:25:00 | NOAA-20 | SANTA CRUZ | RIO GRANDE DO NORTE | Brasil | 2411205 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 021a5677-e222-3b16-8b04-ccc9016e1928 | -5.14131 | -43.24243 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a06db8e9-1865-3a1f-b847-a0d14e6255c7 | -4.39724 | -41.43723 | 2024-12-17 03:25:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 344ee075-abca-3c94-b6ea-4ab8fbc0c9b9 | -5.39315 | -40.66642 | 2024-12-17 03:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
