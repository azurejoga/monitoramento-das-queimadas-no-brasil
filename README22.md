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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da915c0d-5d38-30c8-9629-1ac1215f89ff | -8.37925 | -46.57694 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35e4e8d3-e62c-3750-b72c-143588439f7b | -6.62538 | -59.9684 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d52b27c-ce79-344c-a9bd-da09d46d3e92 | -8.22557 | -45.05608 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1690af57-162e-396f-be00-808edebb5e4b | -4.25443 | -48.58675 | 2025-08-05 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76781473-b365-31e0-b71a-9ee033050a99 | -3.8618 | -54.22151 | 2025-08-05 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c76b813-e9f5-3219-8088-901a8d006c5c | -8.21963 | -45.05479 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6de0f701-1de4-33c4-8f99-f4cc9b323d57 | -9.18063 | -48.84677 | 2025-08-05 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8451e412-f461-33bf-8efb-c906b0e32a82 | -6.77108 | -44.98855 | 2025-08-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc1cdab-5935-300c-be07-736cc33db00b | -6.67928 | -49.79998 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d794fcc-bdcd-315d-9e48-f746a50ea93f | -8.26503 | -45.06548 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd01d8b2-c3cb-328f-9823-f151366328de | -7.99964 | -43.14358 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| a36b1c0d-0b7e-36e1-812e-4386831a1296 | -7.11752 | -43.44614 | 2025-08-05 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c3b07b1-ce46-3594-b269-a4c290a2c911 | -7.59604 | -55.19811 | 2025-08-05 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 585f07a3-6f93-3029-8eeb-af6e585752e4 | -4.1261 | -38.18486 | 2025-08-05 04:38:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b3f6f4a-75ab-3d95-9286-4fca09fd1563 | -6.78722 | -43.24583 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbeefc11-8234-32c2-ac01-0dc06ee468b3 | -8.94931 | -46.73738 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 75067d31-09d9-3ed7-8050-253e80e32e5f | -6.1526 | -57.91965 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37590a4a-dd25-3dc9-8604-1d0f047b04f0 | -8.25355 | -45.06021 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3feef75-24ae-318a-808c-bf736a1e242e | -8.56745 | -47.46672 | 2025-08-05 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db7eb31a-0230-363b-9cc9-6832869eb56a | -8.73636 | -46.43718 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4b2519f-bce6-34b6-ac0c-66181a952f8b | -9.39307 | -45.51118 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e0476f8-05e7-3f83-addc-2062aa69ee87 | -6.90882 | -43.90189 | 2025-08-05 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9513a6a-cbba-3245-bb90-0d79300c9ceb | -8.95327 | -46.73552 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69b7c6da-a273-3adf-aba5-f4842b27efbe | -8.23756 | -45.05786 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bd5512a-9796-33d3-a2e1-fe327cc3ddca | -5.81011 | -46.98088 | 2025-08-05 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa22602f-ced1-328a-8b1a-7c3df42885a3 | -7.77099 | -45.21554 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503cfe0d-917c-3ba8-be58-203fc03dd1a6 | -7.77046 | -45.21789 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5009aa7b-5fcf-3b19-b445-02a3e2636f93 | -3.11283 | -47.5032 | 2025-08-05 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d9a8338-5131-34be-8e1e-53fd9629f772 | -2.90523 | -40.13482 | 2025-08-05 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 944b13e5-b6ce-37df-8e55-994a2b0783fa | -8.94566 | -46.73685 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b66f7bc6-6dc3-3196-9194-47da106cd93b | -7.89916 | -45.53992 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac9b233-ad6f-3a15-b1d7-bf8e63cb17ab | -7.34071 | -44.677 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a848872d-9e03-3557-bcf5-ae3840ce503a | -8.94962 | -46.73499 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bbd2537-c31d-3b18-8d71-1541cd418410 | -8.42591 | -49.5799 | 2025-08-05 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1a61aad-6a5f-3eab-afd3-8d5e89f400c2 | -9.4017 | -45.5072 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80fd8f96-3cd7-3a14-b4df-fdee0b3d1a21 | -6.97171 | -42.86779 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2b2106f3-2deb-39f0-b41a-28c126f72c98 | -7.36231 | -43.71629 | 2025-08-05 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3cb54ac-6e7e-3ce5-bffb-58e5b8bd6545 | -7.21914 | -44.48311 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a0333b4-bc81-395a-9919-5cfc6c6d1552 | -8.45576 | -50.29603 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0669c359-e0a6-34ba-8108-92a1e9579410 | -7.57052 | -44.89217 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1db6f6e8-f65e-32d9-b1f9-8daf9b4a8241 | -6.90078 | -52.19447 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9545d0f-a234-3021-ba04-dbb96791256d | -7.75617 | -45.23398 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7560621e-02fa-38a8-9ea2-257979fecb2f | -8.38747 | -45.79071 | 2025-08-05 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9161143-81e5-3487-9694-b89b57debefe | -8.21512 | -45.05765 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8794c7c3-a671-3ef5-8cc9-abd3dc248cea | -7.56848 | -44.90592 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24a9af45-a22a-36f5-8edb-d634e9f2b004 | -6.3779 | -43.7219 | 2025-08-05 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a813a001-797a-3880-9c4b-a1fda96d4b44 | -7.11687 | -47.84377 | 2025-08-05 04:38:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08294998-4923-3f00-8419-fab7f15f714b | -8.00935 | -43.14031 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 050c467a-ef83-300b-a3b9-dd6b0c70efa5 | -9.0586 | -45.06155 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14e7bee0-52b2-36f7-9ebf-8abe9e2b4cbf | -2.89692 | -54.15324 | 2025-08-05 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3cc834f-7248-3ddc-8603-32b2ec2e0d53 | -7.75971 | -45.23691 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c21841bf-a096-3193-897d-676ac21556c9 | -7.99383 | -43.15206 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b6709f9a-3016-3bf9-9fa6-78150080f3a4 | -5.80952 | -46.98476 | 2025-08-05 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5d0371-dd29-345b-8303-12da29cf8312 | -7.60144 | -45.30575 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f38f03-061e-32aa-8d46-09bcbf50a2ce | -7.99447 | -43.1475 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 83eddcd4-b8e1-3877-b4a6-8bb5190676aa | -6.98167 | -43.39326 | 2025-08-05 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0fa8d051-6f6b-3a6a-b2b2-c15cb982ea04 | -4.77443 | -45.33459 | 2025-08-05 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6064756b-d007-374b-ad2e-646b7c786180 | -8.94135 | -46.74063 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70280810-f9c8-3ca5-b716-a0bd4e46e60b | -6.49893 | -45.54534 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 8e64b5f7-f30c-3908-949d-b97c760a3365 | -8.23406 | -45.05379 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5e50e11-b75c-3f3b-bb44-5fc746744ea9 | -9.4039 | -45.49194 | 2025-08-05 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ef19b91-5b93-33b6-bae9-b875c6c1b6e7 | -6.4635 | -43.02549 | 2025-08-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d34ba4ab-47ca-32c1-804e-4110312b43ce | -7.43528 | -48.09484 | 2025-08-05 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d32d9a89-5e37-35fe-8455-eb262251c065 | -7.37659 | -44.16163 | 2025-08-05 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8c48300-01bc-35d7-af68-90d9d01268b7 | -2.98281 | -54.49821 | 2025-08-05 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 397e2000-e0a5-30ab-bb60-fa1d65c31e6e | -6.2308 | -45.85955 | 2025-08-05 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02454a00-c4ea-368b-9405-4b76c6ad1f04 | -6.4643 | -43.03227 | 2025-08-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3413ebeb-0e1a-37e2-b7e3-829c95faafd1 | -7.81696 | -46.88517 | 2025-08-05 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34b269ae-e0dd-3971-b70d-e75b4e4d0e19 | -7.08449 | -44.69879 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65720bde-cc8b-3ed1-aa84-f2838a632337 | -8.94232 | -46.73389 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4059e630-5f92-3bc5-b2b8-e6cad4ffe793 | -4.06283 | -46.93494 | 2025-08-05 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b283dee-a19d-3d66-b73a-959f019a0bc8 | -7.54157 | -44.86651 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 504e7b71-3658-3634-82ea-7a1a8f3fd20c | -6.01152 | -52.15416 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6599ca86-d1ff-37b2-ba8d-71248506b159 | -6.15709 | -57.91615 | 2025-08-05 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0aba0be-3904-394d-8943-6ad07f601ac2 | -8.95869 | -46.74954 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1664be4-a2d9-35dc-9610-89f27c7a22ca | -5.244 | -46.77678 | 2025-08-05 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9cdcc4-c3e8-398d-8dbe-897cb3570467 | -7.9823 | -43.16845 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| df8bb915-0646-38f2-8a74-056ebea5330c | -2.9822 | -54.50195 | 2025-08-05 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7312223-2ac2-3937-9074-6576c5355898 | -6.65406 | -59.10258 | 2025-08-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e007a36-96d5-32e6-a9f0-cf98e6c454ce | -8.93771 | -46.74008 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4679ff88-e9c6-3d5c-9d24-3e93138133c4 | -8.00233 | -43.22254 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b925bee2-a168-3535-ae9a-518c0ba606f4 | -4.35927 | -47.46175 | 2025-08-05 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b26ce2-04f9-3083-9728-5babe90109b5 | -3.48831 | -59.37408 | 2025-08-05 04:38:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9f118b1-771e-3622-a081-458d66a99021 | -8.25704 | -45.06428 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deda6449-ea36-3a40-98e9-0329c2c7ca8e | -7.85456 | -46.73463 | 2025-08-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9116484a-62de-3a59-95b5-6b5ba3d78f2a | -6.76399 | -44.89983 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eacb09dc-20f7-3ec0-a753-ad8949275bee | -7.08399 | -44.69521 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b17e9a05-9055-3b02-ad9e-92eabb4c811f | -8.26953 | -45.0626 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69b76b7a-4268-3981-8be8-c73b673d20d1 | -8.26553 | -45.06201 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d67d9e81-506b-310a-abc9-9522a15282f5 | -7.21592 | -44.47994 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4c06d39-287c-34ea-b7c6-a78def8be968 | -8.21563 | -45.05419 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9850d93e-4e67-3458-aeab-d6824f16c7ed | -6.67542 | -49.80292 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 579bc8a6-3781-3dff-9b0d-787e46473532 | -8.95201 | -46.74419 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a4ef5ea3-8c14-3011-9282-efb498306538 | -8.2146 | -45.06111 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f37e0070-7ad2-314d-a746-26cb7ed77477 | -7.94742 | -47.59183 | 2025-08-05 04:38:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6863be9f-958f-32fa-972c-45a0d5101096 | -5.13748 | -36.36682 | 2025-08-05 04:38:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 85a7a95c-439c-3bf5-a40f-297589a87226 | -7.21182 | -44.47942 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab1a3982-e1b2-386a-89fb-e1b1927b0723 | -8.26852 | -45.06953 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae3d1acb-d2c3-3918-9dc6-309e0bd4e57a | -9.05056 | -45.06009 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6caba09a-50c8-3171-8db6-7d95b9b834b6 | -5.67489 | -50.26332 | 2025-08-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
