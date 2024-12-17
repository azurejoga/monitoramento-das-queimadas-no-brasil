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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7312637-7900-3836-9edc-a624be691953 | -0.16762 | -51.35046 | 2024-12-17 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d837f90-522d-32e3-be95-4ed67c3f6bb2 | 4.18602 | -60.19451 | 2024-12-17 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7328100-121c-39ed-b0cf-af4794ee6592 | 4.44831 | -60.98939 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1eba90a-5ab5-3b0c-9be4-8d032738445e | -1.40705 | -47.47435 | 2024-12-17 05:05:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8c0452-54f0-323d-a505-1c1d15a2d6d4 | 4.44335 | -60.9861 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 28b9e394-371f-37c2-a884-0b1fc6b79ed5 | 4.43964 | -60.99102 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 514a9d15-1102-370a-90b5-dc8d7b328d2e | 4.44397 | -60.99017 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 309c25ce-2dfc-3950-80ac-d752fcc1ec5d | -1.29674 | -52.836 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d2cafef-039d-364b-9f01-ec84976b408c | 3.98295 | -59.97971 | 2024-12-17 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f8d982a-bf5b-3b00-bc5f-09ab43a91a7e | -1.5412 | -53.73208 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 135f47d0-b9a3-31bf-8665-5c70e84aac56 | -2.76141 | -47.39589 | 2024-12-17 05:05:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 094f66fa-340a-3907-a735-117bbd6b7979 | -2.57052 | -45.9613 | 2024-12-17 05:05:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 054558d0-203e-3dcf-8b74-2c49e626abd0 | -1.37416 | -53.47721 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea882aeb-eb02-310e-9d99-0c5c6041180f | -1.37768 | -53.47774 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02555355-72fe-39a3-a729-2e1a4a955e82 | -4.56689 | -46.58207 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1147b8b1-2918-3b4e-a9d0-bed7b89efe35 | -5.1138 | -43.20465 | 2024-12-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ccb905c-befa-3935-8916-a1216e315d42 | -6.9224 | -43.51456 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2adbd53f-b4fa-3b5e-8fb0-54c665c21c32 | -3.50264 | -53.95937 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf9fd7f-887f-3304-9539-554303f18b0f | -3.3796 | -53.25119 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8212d0f-b2b4-300d-becb-fa2af638139a | -4.37657 | -46.5517 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9a66141-83cd-3eed-b98e-672bbde2b7c2 | -3.01991 | -48.0318 | 2024-12-17 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c427f7d0-d49c-323c-8adf-c8a2764614f0 | -4.0536 | -46.92598 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b17569f-920a-3c80-ad66-72ab666dfa83 | -2.17903 | -53.74252 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 430390fa-fba0-3187-82ce-5d3fa00764e9 | -3.02867 | -52.52863 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a39aa0f2-759b-3e17-a0c2-ec492d9f8d1e | -3.43729 | -53.98209 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 677e0f75-58b0-3f7d-8791-632d3d4fa20d | -2.93121 | -52.71157 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 251a5950-4d8c-3d71-9ce1-049f50465f58 | -4.65792 | -44.33004 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69b59092-0e6f-3512-bd67-0552e03c1608 | -3.13799 | -48.60783 | 2024-12-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b863e24d-f0dd-33a1-8cec-61a095c68725 | -4.80966 | -48.37785 | 2024-12-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7cc694e-b7a9-32f8-9dd8-52a8a014575d | -2.58195 | -51.92261 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a210b94-ab01-36ae-8d34-8ca5bf0094fc | -3.78393 | -47.1119 | 2024-12-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52fc1929-fc24-3dd1-960d-b81fa61cdfe3 | -2.68445 | -51.91272 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e87e925c-37fc-374f-9e7a-b2415e7672e4 | -3.23789 | -46.80717 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0416780-9c40-31f4-9e7b-5efa5b0dd5e5 | -6.99155 | -43.56609 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9c49cbc-466f-34bb-b351-85b3e08f5336 | -3.09742 | -53.25991 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f401fc1e-7cfa-3527-8956-5ee3b4f691d3 | -3.30547 | -53.36516 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd175ccc-226b-3cea-8a33-c51663375308 | -2.95726 | -53.71856 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8398d9ff-c4c5-3252-9cfd-281ff149b50b | -2.65362 | -51.87556 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0f1e0e5-d721-37a7-9f63-7216eea3e07b | -2.18254 | -53.74308 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa18b3b-314e-3419-918c-bc2d51d048bd | -2.7944 | -54.4636 | 2024-12-17 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e04454-af4e-3cd1-82a6-cf3aadb878f3 | -4.56804 | -46.58205 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a5400c5-e936-30d6-8b1f-b629d5648490 | -2.77674 | -48.58144 | 2024-12-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64c25ba-58c1-3815-a2c8-2a384e005c64 | -3.19296 | -52.88831 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425ecb93-589e-3af6-b264-12989e7786ea | -3.43669 | -53.98595 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6be96c4-5d7f-3c9e-bb3d-597ddcf606ce | -5.20493 | -43.30517 | 2024-12-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c050804-3610-305a-b76b-c947c2f6f570 | -2.55049 | -54.70099 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5df87306-bfd5-355e-b11a-635273bee011 | -4.37717 | -46.54751 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fab6d6f6-caab-3143-a498-75d30030c73d | -4.67242 | -44.0377 | 2024-12-17 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdc6d04c-8a17-3366-8b5f-a7bc4c136073 | -4.20204 | -44.3644 | 2024-12-17 05:08:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da03a054-2128-33ac-bcdd-f0c2e0abf24f | -3.95838 | -47.03419 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268e0787-9b66-36bc-af7a-6e6a4e734f43 | -3.59009 | -52.43116 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da789baf-39f0-3d90-aef7-53b160c8e866 | -3.95943 | -47.02686 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4940c35a-2f2c-3168-a071-50b443795c67 | -3.55578 | -54.72494 | 2024-12-17 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74156ab6-c1d4-3ebc-9e2b-3e8f0069b72f | -5.70495 | -46.79362 | 2024-12-17 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 452d0694-0a13-3248-9078-8eaef376bf6f | -6.92959 | -43.51533 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 289fcc74-608f-3e20-8182-a497d17747b3 | -4.79607 | -46.39559 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 921d47b2-3399-32f9-b8f2-0c0b9bfcbfec | -3.0148 | -48.03107 | 2024-12-17 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ff4956f-ff63-3dfe-9dc6-44d1e232bd39 | -4.6554 | -44.3319 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| abad4321-624f-35b2-ae40-cde00cc548f6 | -2.96666 | -53.72813 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9badebb2-a883-3efd-b502-36bf92b3e47a | -2.17842 | -53.7464 | 2024-12-17 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62bdbc9c-ca6a-3ca0-9b98-aa112ff8913d | -1.93865 | -54.55654 | 2024-12-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a209c6ce-d343-3e80-9859-59b9dd0b72e7 | -2.57177 | -49.41103 | 2024-12-17 05:08:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ec0f06c-e6a4-32ee-a8cb-29fb89521261 | -2.58229 | -51.92479 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2526d726-0e75-3e28-a8fa-ab2f56b294e9 | -4.89475 | -44.17775 | 2024-12-17 05:08:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61c4fb2d-9f17-365f-9833-be39b5a31628 | -3.15479 | -53.18122 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f8cb0eae-a0af-3b3e-84e8-92b5ddab744f | -5.09903 | -43.91218 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe54c5f1-cc36-3141-af91-928648991bdf | -3.12313 | -53.23797 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa135391-3765-3a58-ae60-81551e76da76 | -3.87877 | -47.0419 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41858432-8b67-3357-8842-7ae24cf80abe | -4.57374 | -46.58329 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ffc736d-3dd2-3419-91b2-0c5b23d6150a | -2.93052 | -52.71609 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e843d06f-e9f7-3bf8-93e2-d20af1fcd6b6 | -4.04802 | -46.92517 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f94e746-7a5b-3d6c-b15a-88f60978acdd | -5.09215 | -43.91151 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6d6b47af-3ce4-33d3-aa05-72a4bf6d0265 | -3.50032 | -53.95098 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0a37045-0b7f-3d4b-9715-86b64c282bb4 | -4.47805 | -48.11897 | 2024-12-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 240e66cf-fbab-3fab-8760-5bc63f0aa620 | -3.96005 | -47.02745 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1ebeee-0db4-3ecf-90f0-7d528de6b86d | -5.09816 | -43.91846 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bbc0296d-7a8b-390b-b0c2-ebd339dd1fd5 | -4.06195 | -46.90815 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c222cda-bd49-3351-84f5-17e431b3b30d | -4.70869 | -44.38628 | 2024-12-17 05:08:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a24a470-ae2f-357c-80d2-9e3b9fccf8bd | -6.91744 | -43.52673 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7be1d62-1ddd-3138-a54c-25be1ba9e596 | -3.15415 | -53.18546 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 28eac185-410a-3dfd-bb28-8b4e5beb29bd | -3.30185 | -53.36464 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 26de7478-76bd-3d76-96ba-67f7a3db2de0 | -5.21683 | -43.30185 | 2024-12-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20bb27cd-c54f-31dd-9421-a017e1de5be0 | -5.11664 | -43.20823 | 2024-12-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c6e1251-3764-3ae0-a4c1-8df709ff551d | -3.26628 | -53.089 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f348fe90-cac1-30d9-a488-e6064461c56e | -4.18508 | -48.62391 | 2024-12-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b66991fc-fe67-38c6-971e-5d0820de8cc7 | -4.04744 | -46.92907 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 348e74ce-53c4-3460-ba8b-7f74cc8ff3f9 | -3.21596 | -53.09899 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5bf378d-f8a6-3f1b-9d84-aa88385b4a2b | -6.09024 | -46.66628 | 2024-12-17 05:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8e24bd-060e-3589-92c5-8a8c2470c368 | -3.0239 | -47.82969 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97f2e1f-31b4-3558-86cd-e6b6f0f63a8b | -3.237 | -46.80743 | 2024-12-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 453a7a4a-f0a7-30ab-93a5-e2c9a38794cd | -3.8688 | -47.03272 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d8b039cc-a714-35ea-b613-4245aaefece5 | -4.3823 | -46.55272 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c3a90ab-4632-3257-9a92-a59750aabf5d | -3.18588 | -46.69715 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bbbbf2d-7ed8-346c-be18-8f42cfc3b10c | -3.45782 | -54.04057 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fad06dc-8946-3e7d-a170-463492347175 | -5.11756 | -43.20128 | 2024-12-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eff45e14-185f-3bbc-9ae6-189e0849de92 | -3.29696 | -53.37232 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55255433-720c-3235-9829-52fc7b3412a7 | -3.96444 | -47.0314 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a880c91e-d0ce-33a3-a94b-6837f8af2176 | -3.02484 | -52.53083 | 2024-12-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93a605c7-45fb-3748-b51b-0d4690d301f0 | -4.78909 | -46.39886 | 2024-12-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c3572bf-ab92-34bf-bac4-b2496419ec80 | -2.68732 | -51.91572 | 2024-12-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
