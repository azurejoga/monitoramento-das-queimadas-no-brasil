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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5599fe09-dbc4-3e0c-b97b-e5bc1bcfb9c3 | -4.86514 | -48.56765 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f6d8f8c-857a-3da6-9b20-bcf6609f2655 | -4.84201 | -48.57612 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0e675014-8838-3c5d-a9e1-75b504fe443c | -4.84138 | -48.57998 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7da76c84-0d4b-3c56-aae4-6052debc935a | -4.71903 | -48.69258 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bf1ed9d-9cda-397e-afe8-813c4ef9aae9 | -4.59436 | -48.44777 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec6f0940-e90f-374c-8ad7-d2275c1da29a | -4.59015 | -48.44702 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46f5d8f3-60e4-3416-896d-d21f7a48711e | -4.93212 | -49.15243 | 2024-11-02 04:12:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 392064ab-c0c6-3535-894f-cb6e9c5a7998 | -4.71683 | -48.86886 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40ca3e5e-eff8-3467-a0a2-88b52d621de2 | -4.71422 | -48.86669 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e63b6d4-0644-30d8-a2b3-b775f901fff4 | -4.71348 | -48.87102 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cccf637-9e29-39ea-b058-26e18b75bf51 | -4.00719 | -49.0174 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c78587a-b27f-331d-b051-5cf47f998e6b | -3.95854 | -49.03643 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7d49566-23a0-3c1d-9d85-78d40ae2fa23 | -3.9501 | -48.89778 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd3368c0-4471-3748-ac5c-791789008721 | -3.9084 | -48.93143 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f955eff0-710e-38f7-9cfe-b1875300a1d1 | -3.904 | -48.93068 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc77c486-8532-3d45-9072-79c3de25cd67 | -3.82165 | -48.88351 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd27db3a-1f41-387a-8ae5-95eefdac59b6 | -3.8216 | -48.96761 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a76497-ce61-3cd4-a0b3-090d67e41de1 | -3.82018 | -48.97638 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d130cec4-d3d6-3f0e-991d-b41e07693b73 | -3.81948 | -48.98074 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 887d7eb1-3dc6-32de-8978-47c28ec1fca7 | -3.81576 | -48.97562 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7418903a-d4c3-3697-a105-be2a715379dc | -5.70992 | -49.22541 | 2024-11-02 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f14b56c-4cd5-3875-8710-ed8384faf652 | -5.70556 | -49.22465 | 2024-11-02 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71ab7df6-1d76-32f0-8883-73c0cff2ab81 | -5.65462 | -49.18104 | 2024-11-02 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43e65238-bf02-337d-a896-0196b78f4f9c | -5.51157 | -49.1422 | 2024-11-02 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfb13551-a006-39fe-97a7-1ff9a5cd14a8 | -5.50791 | -49.13729 | 2024-11-02 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 678fb19b-9822-3fcb-b466-b9fa4a3c39f5 | -5.47273 | -48.61642 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bf0ad98-be23-328f-92a1-2537bb238492 | -5.2313 | -48.08448 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f156c1f-03ca-3aa6-b756-d590bca125ee | -5.22782 | -48.08016 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8ea6c40-7e63-3066-b6b8-931f1b46338a | -5.22723 | -48.08378 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5da9a2b1-1b9a-303e-afda-21919ae2cb92 | -5.22435 | -48.07585 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42c515b3-7e6e-330f-8aa1-c4c8b9501759 | -5.22376 | -48.07945 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06052143-97be-300d-ba30-c7dc09c226d6 | -5.20232 | -48.23419 | 2024-11-02 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 885a7457-91e3-3773-add6-d7406286e7f5 | -5.19821 | -48.23349 | 2024-11-02 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d25a5d82-6ca2-31ae-9c56-c9fd39e3c142 | -5.17042 | -48.24775 | 2024-11-02 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a7d8d37-5aa4-30ff-898d-7e3e7f95cf7d | -5.16631 | -48.24702 | 2024-11-02 04:12:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6caa0080-e256-30fe-b101-3d288e4a5b6b | -5.1553 | -48.90239 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 945f0c0d-8a81-3893-a161-63fadf38471c | -7.0309 | -49.15636 | 2024-11-02 04:12:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e08569f5-7f9d-32d9-8c23-e6ea9623ada5 | -3.07299 | -50.24175 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20a28799-7860-36c5-aca5-18c5939f7c83 | -3.07084 | -50.2392 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3de39648-b595-3d65-b9a1-7beaadf526df | -3.06684 | -50.23286 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0990c8ad-7811-3963-9070-30cbb2e2e8bd | -3.06489 | -49.57854 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d799ceb6-9890-3f44-bbf3-a77539381967 | -3.06449 | -50.50285 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71d7fdd4-e46b-31c2-ab30-eabd0822de46 | -3.06353 | -50.50854 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60ebc4f4-09cc-31fc-85fb-0047cb136f85 | -3.05856 | -50.5077 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d83bb92b-56a6-35fc-a935-58b95293637a | -3.05837 | -50.50575 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 148dac29-5dcd-35cb-a845-e9f12dd2843b | -3.05454 | -50.50113 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5c6eafd6-4f5f-31a0-aeef-5a350fa78209 | -3.05358 | -50.50686 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a295a2d2-2d47-375e-983a-ba7a58091cd7 | -3.05339 | -50.50488 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 408bc589-15d2-3102-80bb-7a96cfef2fe9 | -3.04819 | -49.47558 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e03089-8ab6-3429-afd3-090aa650cb08 | -3.04355 | -49.47479 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a07a9dce-2286-3e1f-808c-a21d784c97fb | -3.03812 | -49.47882 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a0345e8-2bb6-3e7e-a76c-275ebe2b0cb2 | -2.97959 | -50.48692 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8880d83e-e269-3c89-98ad-3dd62c60e38f | -2.95926 | -50.4251 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3169cc0-de06-3768-bb9e-d2cc4e51edcf | -2.95838 | -50.29941 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afa0b0e4-47af-345a-8fbb-6c87418561aa | -2.9383 | -49.34147 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d79a0c1-ada6-3362-9eaf-e5060eb7e13e | -2.93754 | -49.34611 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 794fdc05-5b67-3048-a278-0f5b5c6b1718 | -2.93334 | -49.42904 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebb84a75-ea31-3e5f-985c-375c83784e26 | -2.90875 | -49.03404 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 201cd5f9-3a03-3057-9090-1acf70f610f6 | -2.89645 | -49.50771 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54d5f10c-2a3c-3b7c-95bb-d3660aa99ab7 | -2.89416 | -49.50536 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0de0bc90-1f48-3ad2-a64b-518049284fef | -2.88794 | -49.42464 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c34682a7-5339-3f95-850f-957e8ed3b165 | -2.88487 | -49.41412 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9c11126-2ecd-3a12-a541-6776c85f9b4a | -2.88029 | -49.26654 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b14e8828-fdf8-3f8b-a668-74e876bb914f | -2.85637 | -49.38464 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4283cc10-42d8-32e1-b012-b23892b31b0c | -2.85558 | -49.3895 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96121df2-b49d-351f-827f-33a77219eddb | -2.85487 | -49.36472 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5734cb7-5970-39be-a9d7-fa362d496249 | -2.85096 | -49.38869 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b9fb4d8-acd4-3449-b43b-7b041eb18488 | -2.84712 | -49.38311 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d0aec3d-6fbb-33e3-8fed-9088bd62c9e4 | -2.8425 | -49.38237 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ae513bb-70d6-39f9-a6dd-a4aa9acb5708 | -2.84175 | -49.86548 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 355738f0-6a48-3b09-b6b0-ca8e84a3ff2a | -2.8417 | -49.38722 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1724bf71-910b-372f-afbc-f40afc74c2c0 | -2.83823 | -49.49613 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13f94886-88e1-3793-9224-38ae2f132281 | -2.81755 | -49.27559 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a6b51c9-199f-3552-885a-e947f734411f | -2.81425 | -49.32372 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29695391-e89a-3007-98e9-66398481adfb | -2.79996 | -49.32837 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc908ea5-be50-38a9-bd6f-c5f1474ef67b | -2.79899 | -49.21657 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac7fb02c-1a65-36b8-8ac1-af72bc80b5a3 | -2.79804 | -49.33577 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 106008c8-bf52-39a7-a77d-e36470dab377 | -2.79458 | -49.33241 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 880d0438-5c6f-3a96-ae2d-5d0bf10ec5e0 | -2.79381 | -49.33723 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff54726c-8ec2-3a73-ae28-3190b7bee923 | -2.79342 | -49.33501 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b7e9a70-0f9d-3772-81b4-138198d05677 | -2.79262 | -49.33981 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc34f04-234b-3769-a8fc-dbf739cd6f6a | -2.77757 | -49.55934 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858b9786-1bee-3fcd-a678-50ddbbd09af2 | -2.77657 | -49.5212 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d53ffaf-a512-3a88-8262-475087179b0c | -2.77382 | -49.83134 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d3544c4-e8c0-3bbd-a2fc-f32f34607c0c | -2.7586 | -49.17639 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35b8fab8-439f-3f97-a77f-aafc8b3cfdea | -2.75783 | -49.18106 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c233d32b-a8ec-3e4b-af79-bbcaf5a663b3 | -2.75727 | -49.96262 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef528feb-c03f-373c-9cfb-25dce1acf379 | -2.75706 | -49.18575 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cac41b2-3ae8-3452-be07-b49634f9b7d0 | -2.75127 | -49.45401 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bd049d3-46b6-3057-b591-ee4d42162495 | -2.74687 | -49.63097 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b5d65e0-388b-39a2-b318-57238092eddf | -2.74493 | -49.49324 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a398a74b-be4e-306b-b5c6-44330ebb98b2 | -2.74396 | -49.55886 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3491333a-7528-34d9-9bc7-423796ccb3fe | -2.73927 | -49.55809 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e275952-8965-33b7-8523-b00b62fe7691 | -2.73847 | -49.56304 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 820f1a20-8d14-3d30-a2e4-49cdb3ce5cdb | -2.73773 | -49.30355 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 524447bb-529b-3724-a040-401758efcbb4 | -2.73234 | -49.30753 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fba8b605-85fc-38ca-9323-82362cfe0a23 | -2.72532 | -49.17827 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd949831-82b8-3e6a-9a6b-886a8f3758c4 | -2.72132 | -49.17493 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2e23435-824d-3687-8aa5-d13edbb155b9 | -2.72075 | -49.17752 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49be3cf1-3fa8-3e7b-a223-3c4033b02f60 | -2.71348 | -49.2828 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README46.md)
