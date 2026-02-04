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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a4d5015-0f51-38d7-94fd-3d4e535a8a00 | -5.87901 | -50.15709 | 2026-02-04 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c54c1ed1-5b49-37db-a330-1be6ec9b47bf | -4.86289 | -38.44138 | 2026-02-04 04:08:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9373ee72-b8d7-30b9-a7be-bef3b4e2ab18 | -3.48923 | -43.6386 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dc6e97f-5151-3e5d-8f1a-b9e9d6c72deb | -4.23426 | -40.39284 | 2026-02-04 04:08:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 285f720c-35d5-3c10-afd2-03498b72ca8e | -3.49275 | -43.63915 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1a47b3-71de-3dd0-9c7c-db48e1e1b24b | -5.40897 | -39.10179 | 2026-02-04 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b552a079-ffa9-339b-9ec2-2f9dff5e352f | -4.91995 | -37.43032 | 2026-02-04 04:08:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb9fd0e9-0a4a-3182-b4fc-baa45c1902ff | -3.52545 | -48.88621 | 2026-02-04 04:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10b794a6-3ede-37cd-ae08-094b1f92f655 | -3.43457 | -39.27652 | 2026-02-04 04:08:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a317b9f-9d1b-31d5-b20a-77d8bfa50c5c | -3.49564 | -43.64364 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4775604a-2fef-3ce7-a54f-a84ed0568e0a | -3.43872 | -39.02481 | 2026-02-04 04:08:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bbfa2400-8b20-3979-a209-03c58ec26ef2 | -5.8738 | -50.15665 | 2026-02-04 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f6ff701-9c07-3664-9458-84d090db18c2 | -2.99913 | -40.03983 | 2026-02-04 04:08:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92ab8147-e900-3616-80be-17f41405df40 | -4.21933 | -38.11749 | 2026-02-04 04:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3a951af5-0711-3fa0-bd3d-3d099f42eb1f | -7.60638 | -35.52473 | 2026-02-04 04:08:00 | NOAA-20 | NATUBA | PARAÍBA | Brasil | 2509909 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5cec5fb8-91a9-3fd2-bec1-d30aae3bce1b | -6.15719 | -40.3164 | 2026-02-04 04:08:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84550133-0e86-3605-9c41-df530464898d | -5.43663 | -38.56861 | 2026-02-04 04:08:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aac43ae4-20a3-38e4-ab6e-485a0f0b64e4 | -5.93446 | -39.69192 | 2026-02-04 04:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92d2e87a-b472-3825-b764-a2eca7c48a22 | -6.58061 | -38.57872 | 2026-02-04 04:08:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3bcfc0a4-cce4-3d31-ba80-e42246c443dc | -7.54962 | -35.17406 | 2026-02-04 04:08:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| dd8dbfc8-d6fa-3eb2-ab47-69ce6d352050 | -4.86322 | -39.00584 | 2026-02-04 04:08:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e4c72305-9a35-3b82-b079-5ac80868c968 | -5.47153 | -39.12252 | 2026-02-04 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dfffe258-1cca-3748-9fae-88d992e1575b | -3.49211 | -43.6431 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c460b8b-d5b2-3a59-bb7a-85e35bea9d54 | -4.9445 | -38.73302 | 2026-02-04 04:08:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 876f48bb-3f45-3728-a0de-f670ae682ba1 | -6.43863 | -35.46142 | 2026-02-04 04:08:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c747c31e-9548-3712-a74e-7f4a6c4e8039 | -5.4697 | -39.12296 | 2026-02-04 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fb79a79-3489-37bf-b0a1-40b5847de770 | -5.82017 | -39.08762 | 2026-02-04 04:08:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4d3d19e-756c-3ab1-9032-08aabd85b649 | -4.94099 | -38.73249 | 2026-02-04 04:08:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 40eb46a9-0c5f-35e8-8bea-b3907ab818c0 | -7.59811 | -40.2372 | 2026-02-04 04:08:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87523480-7afb-3ca6-a6da-e83dbe880f96 | -7.55416 | -35.17461 | 2026-02-04 04:08:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| cde6b45d-b10e-33d0-a4fa-435f5838a274 | -6.60268 | -39.35587 | 2026-02-04 04:08:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bba2b37c-dd4e-3e64-9ccb-f1772b542588 | -3.49339 | -43.63521 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c54a43-bf8b-34bd-a9d5-10d48a222875 | -2.99968 | -40.03635 | 2026-02-04 04:08:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75b83d1b-fe69-3913-9bbb-4382c4abad2f | -4.77364 | -40.07434 | 2026-02-04 04:08:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94380945-5757-3f60-9e6c-cdc1a348d20e | -5.47317 | -39.1235 | 2026-02-04 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9b860f1-f0d3-37bf-9126-44bb26642722 | -4.94038 | -38.7364 | 2026-02-04 04:08:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6301df7a-065c-3d25-8671-b6bff6fcbb1f | -3.65191 | -43.52715 | 2026-02-04 04:08:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ffa4bea-dcf2-3b61-83b6-947731748715 | -6.05855 | -43.25805 | 2026-02-04 04:08:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8b972b3-d098-3cfd-b35c-72775492bdc5 | -3.45632 | -42.9945 | 2026-02-04 04:08:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46c58391-6422-351e-8266-342ca0adda2a | -3.48859 | -43.64256 | 2026-02-04 04:08:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac6cf8c-32f6-32f6-85a8-f5dd3d38ee64 | -4.36637 | -37.89912 | 2026-02-04 04:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f03cdff-3d11-35bb-a53a-acc5b9806889 | -4.45971 | -38.38338 | 2026-02-04 04:08:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de13a1f5-8485-3056-ae1f-598123527a05 | -5.27364 | -35.97128 | 2026-02-04 04:08:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f03996c6-7eda-378d-8eed-a13c19a87621 | -5.11754 | -39.0867 | 2026-02-04 04:08:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 38227967-b90c-3be5-bb0b-d74f8efaa986 | -5.87329 | -50.15957 | 2026-02-04 04:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e1e1b24-1ec1-3acd-9ece-dfeec1b30893 | -5.93503 | -39.68821 | 2026-02-04 04:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48284ce4-1f8c-305b-a428-52bc4292a7d8 | -3.65253 | -43.52323 | 2026-02-04 04:08:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c484d45-bd52-3857-983a-69c0ead2c2b4 | -11.13256 | -37.19276 | 2026-02-04 04:10:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 44843a14-8f49-38c0-bc2a-78e559e3f5da | -9.49798 | -35.59328 | 2026-02-04 04:10:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 71672473-f32e-3977-81b7-8303b63a07f4 | -10.32454 | -36.77574 | 2026-02-04 04:10:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bbb634e6-5b04-3e3a-be8d-547489877edc | -10.80209 | -44.48605 | 2026-02-04 04:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 109dfa13-500d-3db2-9c2a-f76c0e567a62 | -8.7037 | -35.11771 | 2026-02-04 04:10:00 | NOAA-20 | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f011b1c2-7449-38f4-84db-d863141c8042 | -8.73071 | -36.69547 | 2026-02-04 04:10:00 | NOAA-20 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c1ee573-ee87-30c6-8a4a-f2f6586017c1 | -10.31976 | -36.77908 | 2026-02-04 04:10:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c100295-473d-3ebd-870c-1f1d88359209 | -10.65068 | -37.13111 | 2026-02-04 04:10:00 | NOAA-20 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d43b4210-6e72-3428-ade6-f3799d612fbe | -10.32398 | -36.7797 | 2026-02-04 04:10:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e749421f-f57e-3e44-8876-71dd1f2e5d74 | -11.1331 | -37.18894 | 2026-02-04 04:10:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0860d18e-09ad-3041-a292-7568a34770bc | -15.25657 | -39.2779 | 2026-02-04 04:10:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2768b5d3-60dc-30f2-9139-3c6cc1b1b75c | -10.53001 | -36.69273 | 2026-02-04 04:10:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc0f0ca3-93e0-3e31-973d-e79dfde6b1fb | -9.34987 | -40.68287 | 2026-02-04 04:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f796114-2854-3d85-89b8-1a8cfb942548 | -24.40309 | -51.46193 | 2026-02-04 04:14:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39415253-5ebf-34eb-9c09-79cee5c2f782 | -24.40234 | -51.46202 | 2026-02-04 04:14:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0322eda0-5f83-3741-b82d-e20630cf3e0e | -30.47799 | -56.37672 | 2026-02-04 04:16:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 88f1cb1c-67e2-3aa9-91a0-f65c35f6d539 | 4.41647 | -60.5835 | 2026-02-04 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c11932e9-c405-34a0-923b-7846e4c0798d | 4.37645 | -60.35173 | 2026-02-04 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ef6eba5-701c-38c8-8499-732866afdca3 | 4.37596 | -60.34843 | 2026-02-04 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1996f0dd-6b00-3e24-b698-d3b4a433a788 | 4.35594 | -60.93678 | 2026-02-04 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92327338-1ca1-3635-b851-ddf95237e678 | 4.37747 | -60.35848 | 2026-02-04 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10cd2cb1-e600-3e5d-9478-505f25c6020e | 4.35683 | -60.94306 | 2026-02-04 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d7e3c1-ab77-36d9-9480-f2980ff485a9 | 4.35639 | -60.93995 | 2026-02-04 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d123f2d-65d3-3861-8cb6-6b81cb61f4e5 | -1.50811 | -47.33301 | 2026-02-04 04:57:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25adeab2-f922-3bea-a392-03981fc60d70 | -3.1485 | -48.14753 | 2026-02-04 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dad4ed62-9df4-3f51-9965-da92aa463a4b | 0.79199 | -51.96665 | 2026-02-04 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce288bf-296c-378f-896d-111d0e01cbe2 | -5.87569 | -50.15539 | 2026-02-04 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eeeb7ba-9c1a-3870-b4b5-75cd01057972 | -3.44172 | -54.09921 | 2026-02-04 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e248055-f4d8-3c6c-a185-201d0bf4bc2c | 1.83487 | -60.84385 | 2026-02-04 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5fb606f-af09-3ac2-8b51-67b32243d06f | -3.27478 | -42.3787 | 2026-02-04 04:57:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c04b68d-406a-34ac-826c-fcc61fbb6332 | 1.55133 | -60.40543 | 2026-02-04 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a78cad-d9c1-3ebe-be75-a7b1df58701c | 1.83532 | -60.84679 | 2026-02-04 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38e34cd2-be5b-31ec-a123-b2f51c14719c | -4.00322 | -50.32554 | 2026-02-04 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d545c05-e3ff-3758-8a90-799959fe2be0 | 1.35391 | -60.04859 | 2026-02-04 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55942ba4-d31b-3082-96b7-442c50d0f399 | -10.80455 | -44.48439 | 2026-02-04 04:59:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 414f32b2-af0d-3834-ae4b-4ebbc9b7214e | -12.80092 | -62.15765 | 2026-02-04 05:01:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 210be2dc-f108-3808-ad42-a0727a33eeb1 | -16.4534 | -58.17445 | 2026-02-04 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b3716f09-e876-3e92-bec9-f057d0a02f4e | -16.45401 | -58.17073 | 2026-02-04 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b0aa8aa6-a5c1-3ece-b34d-5321842ef9f5 | -12.80526 | -62.15843 | 2026-02-04 05:01:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fadc4ced-abd4-3c05-801b-50874ae6eb52 | -30.47843 | -56.37551 | 2026-02-04 05:05:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| f0bfc0e4-5dfc-359b-b92a-4ebaf7e1d734 | 4.35978 | -60.93482 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 234922de-b139-33dd-a223-83511a293712 | 2.51596 | -60.98959 | 2026-02-04 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ce4f470-7694-37a7-b9d3-0868d21e699b | 3.76552 | -61.32138 | 2026-02-04 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b22d7958-d9df-3a9c-8a47-348a547c765d | 4.35623 | -60.93535 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 987bcd1d-6985-36b6-8ca6-d5e8967fde0c | 4.36747 | -60.9376 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b9eeb8-a140-344d-b4bd-0eae0648dc71 | 4.35485 | -60.94304 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03f2dd92-f126-39e1-b00a-29125fe2fc76 | 3.44859 | -60.68266 | 2026-02-04 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66ee1ce3-f879-37a9-bddf-88879395e9e3 | 3.22271 | -61.19862 | 2026-02-04 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 219c77e9-86c6-3b4c-9d71-fbd05c4bcc11 | 4.57359 | -60.31557 | 2026-02-04 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7af60b9a-46ec-3b9e-b520-3e067370ff9e | 4.35716 | -60.9346 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53cd6c94-68f3-3ccf-ab3e-23c8e562dfa7 | 4.36687 | -60.93367 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2f8dfa-8ebf-3964-be1c-4f933d5bd380 | 2.15425 | -60.53674 | 2026-02-04 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef61c0e9-f413-3196-a5f1-57a19922b2d2 | 3.21916 | -61.19918 | 2026-02-04 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
