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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f7e14b5-3c3d-3f98-afe4-297e9d407b32 | -0.1012 | -51.2738 | 2025-12-27 05:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 029b5934-a740-360d-8abc-cc300f46a91a | -10.95062 | -49.42125 | 2025-12-27 05:31:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88e5ae82-24b4-31d9-947e-5c001b278468 | -3.46731 | -52.80478 | 2025-12-27 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3916a022-b93e-3cab-83ec-9919b9632fc4 | -4.17341 | -48.58769 | 2025-12-27 05:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f971e514-da25-3228-a5f6-dfc9e78da2e5 | -3.46777 | -52.80164 | 2025-12-27 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa7dc0ca-e6d4-3551-8d6e-f4d7a964b086 | -4.22088 | -56.08308 | 2025-12-27 05:31:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44c697c8-2f89-32d3-bd9a-9f637b2631e4 | -11.46382 | -54.35427 | 2025-12-27 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5165c5e9-ff9f-34df-b556-4a9b6b2cbbab | -9.28525 | -56.8929 | 2025-12-27 05:31:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73fdcf83-c455-347c-99d6-853fedeb7674 | -10.94647 | -49.42284 | 2025-12-27 05:31:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd143825-2f14-3d19-adb3-1203e915471e | -9.72225 | -60.20302 | 2025-12-27 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 182c9d82-8050-3a1b-96bf-d4f31442fbfb | -3.46645 | -52.80494 | 2025-12-27 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b856ef7-0558-3e4d-8f80-a25dc7713f7b | -3.46692 | -52.8018 | 2025-12-27 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15a0d9c-4bd0-3a2d-b172-c79189a05e16 | -11.45817 | -54.35666 | 2025-12-27 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50bb052-7933-3994-b66b-f1efcf13bc26 | 2.5247 | -60.982 | 2025-12-27 05:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 14877533-b7f7-35c6-b36f-407397c9399a | 2.5065 | -60.9822 | 2025-12-27 05:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bb719076-6c06-3729-8b9d-2174e909b004 | 2.5247 | -61.0009 | 2025-12-27 05:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 62861160-feb8-3027-bc9b-e4665429719d | -0.0828 | -51.2946 | 2025-12-27 05:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0e7d9f60-9e72-3a64-94fe-a661b62fc6a6 | 2.5065 | -60.9822 | 2025-12-27 05:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 781d4869-8668-3e6a-9229-1d6de1eccb15 | -0.0828 | -51.2738 | 2025-12-27 05:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 96b85583-a25d-3f94-930b-be58062d3192 | 2.5247 | -60.982 | 2025-12-27 05:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9ea4dd7e-470f-33d8-ad98-6c480800c4ec | 4.02789 | -61.13684 | 2025-12-27 05:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64a29bbb-422e-3e6c-a5c3-bce7f976f121 | -1.47664 | -54.2046 | 2025-12-27 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a72263f-daeb-38cc-85db-22170295d3e4 | 2.51125 | -60.98463 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6faa2fa1-f943-3998-97ae-08e32fe7b36f | -1.47759 | -54.20541 | 2025-12-27 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf4510d-0e3f-3b89-8be1-f3f67fed6209 | 2.52091 | -60.99099 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 66e15ec0-64ad-370d-81c5-f97082adbafc | 3.22699 | -61.19144 | 2025-12-27 05:59:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7bd018-0e7a-3a9f-8bb7-6f0513c4482a | 2.30453 | -61.62406 | 2025-12-27 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c50fe8e5-e1b4-39ef-a737-3f260ba6c896 | 2.52028 | -60.98715 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 85573203-ce5d-3efd-825b-c4db54dd3397 | 3.57282 | -60.40683 | 2025-12-27 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f185930-187e-3829-8406-87e2424c0494 | 2.51251 | -60.99231 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 041d9407-195d-3dc0-aded-dfe16b2f3785 | 2.51188 | -60.98847 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e84b7e71-ca82-3db5-8f57-49f001f6ff1e | -1.47861 | -54.19896 | 2025-12-27 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb6538e2-8ce7-3d17-80d1-8aec0a93775b | 2.51671 | -60.99165 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 79755dbe-e95c-3274-9db9-051939734119 | 0.46424 | -60.41729 | 2025-12-27 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f10f4e04-e6a4-398b-a2cf-216fcaafff02 | -1.4776 | -54.19818 | 2025-12-27 05:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25244d1b-4cb3-3ac2-b6e9-4ab731c7ace9 | 2.51608 | -60.98781 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5ffbce52-9e24-3901-9b77-a5eb141f9226 | 2.51545 | -60.98397 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 86b055a4-ad37-34b0-9130-3b976928e4fe | 3.38533 | -60.41808 | 2025-12-27 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4013cc6a-7e59-383d-90ee-cba70b1e980a | 3.57459 | -60.40506 | 2025-12-27 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b66f03-d2eb-3fd2-ab18-bf5ce0a0b977 | 2.51062 | -60.98077 | 2025-12-27 05:59:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d628dc2c-821c-32d0-8ef8-51f16926a876 | 2.5247 | -60.982 | 2025-12-27 06:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3d90bf7e-2fb4-39a5-8bd6-bdaf21f81c63 | 2.5065 | -60.9822 | 2025-12-27 06:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 83e9af3a-0a2d-3180-af96-234f831ab3e6 | 2.5065 | -60.9822 | 2025-12-27 06:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| fac1c813-8365-3b76-96c9-efc499413aa9 | 2.51287 | -60.99379 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1457064a-db25-3107-a541-393e8488d5b7 | 2.5133 | -60.98561 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e2fb9ace-6480-3515-9fcc-99a4552900f9 | 2.5197 | -60.98463 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d90cb1bd-bb83-3313-889c-fde0c75c8470 | 2.52059 | -60.98984 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4f9add96-3486-3116-aae2-3061aac96cc6 | 4.03167 | -61.14042 | 2025-12-27 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1f5ee01-5c8c-31b4-b275-c827cffec300 | 4.03157 | -61.13359 | 2025-12-27 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af322ffc-381f-3f3d-b9e7-ffe1ec145200 | 2.52149 | -60.99509 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4d6f5ac-3399-3e23-b39f-ba7651f01d41 | 2.51201 | -60.98854 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 737824f5-2aa2-393b-b43a-155a2f8e4ad4 | 2.5142 | -60.99086 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a74989cb-0e90-3a6e-8a11-59a3d6af08fa | 2.51509 | -60.99608 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bcd46ec7-fd78-37b4-a4d6-92b3dfa4ce1c | 2.51114 | -60.98327 | 2025-12-27 06:18:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 035e03fb-50eb-3413-9c30-9ec6a461c2cf | 4.03238 | -61.1384 | 2025-12-27 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 864abca7-eedc-3773-9d1a-5084366a05cb | 2.5065 | -60.9822 | 2025-12-27 06:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cdeef599-0d4b-3ad1-9ee7-3d6229d254cd | 2.5065 | -60.9822 | 2025-12-27 06:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| bf4429f9-d3e3-3488-9481-09ef268b15cc | 2.5065 | -60.9822 | 2025-12-27 06:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bd53ba1d-db09-30c4-9b43-7780cb563706 | 2.51839 | -60.99171 | 2025-12-27 06:58:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 68b3ea0d-72b0-3570-a2ed-be0845391c8a | 2.51675 | -60.98083 | 2025-12-27 06:58:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 4b0af791-d52a-3535-ac09-3dd9b95602f1 | -0.1012 | -51.2945 | 2025-12-27 07:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 377750fd-59a0-3be5-be85-2f54fb542fa8 | -3.9069 | -42.5672 | 2025-12-27 07:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 23060456-bc6d-3b6f-911a-83b83097664b | -0.0828 | -51.2738 | 2025-12-27 07:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e5f00c09-b51f-303b-85a8-cf2ffd0d3a8c | -0.0828 | -51.2946 | 2025-12-27 07:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c914606c-2856-3fc6-8280-34793bbb80a3 | -0.1012 | -51.2738 | 2025-12-27 07:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| faf75293-c280-3988-bbf4-f1104f8bf1c8 | -0.0828 | -51.2738 | 2025-12-27 07:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 2b8415c2-a944-3e8b-b622-6ae2522e76a0 | 2.5247 | -60.982 | 2025-12-27 07:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c883a25d-2dde-3864-b697-39646f17d094 | -0.1012 | -51.2738 | 2025-12-27 07:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d3da197d-7bf7-3b8b-9ad3-ce71508a055d | -0.0828 | -51.2946 | 2025-12-27 07:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 242f3f19-45f0-3b53-9271-157f0d9cac60 | -0.0828 | -51.2738 | 2025-12-27 07:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 10a7bc07-5cd3-39de-b1b4-52dc05ae7502 | -0.0828 | -51.2946 | 2025-12-27 07:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4d47e2d5-c23e-3283-981a-e8565c72b98e | -0.0828 | -51.2738 | 2025-12-27 07:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 5da94037-088d-31e9-ba07-3e5524b1245b | -0.1012 | -51.2738 | 2025-12-27 08:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 2f88779d-d690-32b8-a365-964fa72f137f | -0.1012 | -51.2945 | 2025-12-27 08:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8ba26d69-a321-3164-8d29-95eae9d72b80 | -0.0828 | -51.2738 | 2025-12-27 08:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 155.1 |
| d4916d60-9870-313b-b7bf-1494ddf51540 | -0.0828 | -51.2946 | 2025-12-27 08:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 26ae04fc-968d-3520-b730-e71692d2c1e8 | -0.0828 | -51.2738 | 2025-12-27 11:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 81.6 |
| aefb58f9-8d2e-3df2-986d-32c8155ab6ca | -0.1012 | -51.2738 | 2025-12-27 11:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 9e6a666e-c3f6-3e34-a93a-ef5e5c1a4c98 | -0.0828 | -51.2738 | 2025-12-27 11:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 87f98d77-dbc5-3d73-8b40-a1580b12a619 | -0.1012 | -51.2738 | 2025-12-27 11:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 9ce6aafc-ccc3-3624-a918-ea536fe01cbf | -3.90088 | -42.55053 | 2025-12-27 11:34:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 5b8ba6d9-f1d8-3ec8-9a90-3bac98d813d4 | -4.5278 | -39.37477 | 2025-12-27 11:34:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 36.4 |
| f7f9bb97-4077-3c55-b153-b004a35fc02a | -3.65384 | -42.3549 | 2025-12-27 11:34:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 05ad8326-1be6-32b9-8f48-9400210a99d8 | -5.33887 | -37.06207 | 2025-12-27 11:34:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 471dcc88-6632-3ce7-b886-6b0238af50d0 | -4.10902 | -38.51109 | 2025-12-27 11:34:00 | TERRA_M-M | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 96e668ba-9724-3a29-b71b-7eac0c899360 | -3.90977 | -42.56619 | 2025-12-27 11:34:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 8a81d053-6259-3b6d-bbd8-2fc3ae76b227 | -5.19621 | -38.64789 | 2025-12-27 11:34:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 653515fe-faa1-364a-8b51-60ba6c2e451d | -5.34017 | -37.05284 | 2025-12-27 11:34:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 9f6a84d5-61f0-333a-84bc-fa15d16fb018 | -3.89876 | -42.56466 | 2025-12-27 11:34:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 25762db3-656c-3008-9031-386998cf406b | -6.94783 | -37.86942 | 2025-12-27 11:36:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0bd6feef-d950-3479-94d4-5e39da31698b | -9.60905 | -41.71213 | 2025-12-27 11:36:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3e5a89be-492a-3f10-8580-5f96dcfc9369 | -7.86082 | -39.86001 | 2025-12-27 11:36:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ffba5bc3-78ef-334e-8466-086037037840 | -5.30206 | -38.67817 | 2025-12-27 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 495a5f9f-90de-31c4-81e1-ee5cdf6a41e1 | -6.0327 | -38.02318 | 2025-12-27 11:36:00 | TERRA_M-M | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2f4a09d8-002e-3d91-acbc-6f371fae6e7d | -6.50545 | -37.6111 | 2025-12-27 11:36:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e32c84fc-7c5c-32b1-8b5a-ef64a2b8ff6c | -5.7304 | -39.0315 | 2025-12-27 11:36:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 3e06bab4-9dfc-32e1-b1b0-728e3c7f4504 | -6.55021 | -35.17364 | 2025-12-27 11:36:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b56e3594-2cd8-3771-9e20-b31bcc2edc7c | -7.98225 | -38.83014 | 2025-12-27 11:36:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 271317a8-c04e-3771-a1b5-35450055c6de | -7.59667 | -37.12975 | 2025-12-27 11:36:00 | TERRA_M-M | OURO VELHO | PARAÍBA | Brasil | 2510600 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cff8be45-ed8f-3dfc-bbe5-1dcbd0802342 | -5.88281 | -39.69812 | 2025-12-27 11:36:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |


[Clique aqui para ver as próximas entradas](README15.md)
