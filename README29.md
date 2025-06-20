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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f64d929b-a0c3-332f-ada7-a4d29701546d | -12.02574 | -57.09641 | 2025-06-20 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba025134-6d59-334f-967c-daaea7443e3d | -13.14147 | -56.81124 | 2025-06-20 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d30ff7e-1b40-333d-9b23-f21897f7f01d | -12.51108 | -58.35633 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 824eea3e-db0d-32f2-8cd6-f553cec084f4 | -11.95475 | -58.74319 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0456a6db-4ce3-3080-8a5b-f2550cb3d628 | -12.51071 | -58.35921 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a762522-73b4-3871-8460-62787d4a678e | -14.02623 | -55.12444 | 2025-06-20 05:42:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 711677a5-fa68-3d40-b315-a53feb15b627 | -11.53055 | -56.98444 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d18b37b-21d1-3b58-8462-5c1fefd79b41 | -12.55538 | -57.71878 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52474da6-048e-3114-9bf2-19d39616a3b2 | -11.53514 | -56.99203 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cd7e563-246c-365f-a7d1-cb89d4566a6f | -9.58721 | -65.88485 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a9e4990-a3ca-3c88-a9e7-3f73f71ea6f4 | -11.1377 | -55.19722 | 2025-06-20 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4a610e-37db-3fb1-bae5-c7a450b8319e | -11.83958 | -57.76077 | 2025-06-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84792d06-f4fd-36b8-af09-8eff5cab8f30 | -12.04506 | -63.77671 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 880bcc7d-5796-3ed4-afee-9924948776f7 | -10.02682 | -62.13293 | 2025-06-20 05:42:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b44461fe-ff9c-35ca-9d78-e133fd4cf6a3 | -13.6609 | -53.94426 | 2025-06-20 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1b486a1-afe6-3df9-a3d4-4060f5364f4b | -11.52896 | -56.98448 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0bd1a0b-2034-3f99-b830-7c4a8f0885d1 | -12.55095 | -57.71154 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0398ed7b-a797-3f86-ac94-bdfd1305ad4e | -11.94339 | -58.74296 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 556d548a-fe80-31c8-8315-cb8cc38737bd | -9.59052 | -65.88538 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dedfcc3-ec9d-3ff2-8f73-00ea8f2b9a48 | -11.52851 | -56.98795 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c3eade4-401d-399f-a0a6-8ef14ed88298 | -12.50644 | -58.35274 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87a88cb1-d636-329d-a313-a71ee1dcabf2 | -13.97012 | -58.10541 | 2025-06-20 05:42:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f83b03c-d185-39b8-8e3c-4aa00fdc17f1 | -11.52928 | -56.99482 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f5db2dd-b6e9-3222-b96a-eafb82175dc3 | -11.94434 | -58.74722 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f6d80b8-9ae3-3bd9-9a99-bcdaf5466506 | -12.42561 | -54.8745 | 2025-06-20 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f07cc8f5-d81c-37dc-aba5-67e324e4c7f5 | -11.94991 | -58.74246 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 355d315c-abf9-3208-a4d8-c8f93f532ae2 | -12.51146 | -58.35345 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e64edff6-9c03-36c5-ae2c-4a8c0d6d2c3a | -12.5057 | -58.35854 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5262636a-1470-3fc7-bee6-34fdc04d1ae7 | -12.52266 | -57.21026 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d18a17c-1d75-3da5-8f8e-9c7a11aaab36 | -12.0253 | -57.09988 | 2025-06-20 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4cfa90d3-bf70-32c5-a24d-adfddd070b84 | -9.95476 | -64.98775 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff1da8d8-9b03-362c-884d-fc8694b929c7 | -11.62194 | -58.29699 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ffa61ce-986c-3d6a-9c2d-f6e75193cb33 | -12.28564 | -57.27017 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 411520fd-1cab-3709-8e23-d67d96342b55 | -13.7792 | -54.19659 | 2025-06-20 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ec445db-95d3-3c76-8cd1-c894f013cc36 | -13.97051 | -58.10215 | 2025-06-20 05:42:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d3d1d73-bf4c-3593-a19c-13f47006aa2d | -11.8194 | -54.50182 | 2025-06-20 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d66811-3c5b-3f7a-b504-1752066a9460 | -12.52309 | -57.20678 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72d60c96-165c-3334-b316-a277867f0a7a | -11.95655 | -58.75587 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5cf371c9-ebae-3ad5-a12a-c856e1e1d7b6 | -12.42865 | -54.87328 | 2025-06-20 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9999a5df-2404-3c99-bbab-ebcb60e94343 | -12.0492 | -63.77317 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10bdabc-6c04-37ed-9273-d1a9c010f424 | -11.94824 | -58.74364 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8c411060-6669-3d49-a4aa-8470ac2a4d6f | -11.94687 | -58.75454 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50e7b40b-de8e-31cf-8c0a-b2843806c62f | -13.29014 | -57.07413 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ada0703-4556-370a-a634-03524aab6f3e | -11.94845 | -58.75336 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ad32091-69c3-3b18-9fb2-69ec6537ed7c | -11.13825 | -55.19262 | 2025-06-20 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833000ce-e651-38be-a355-b4bf3506df54 | -12.54571 | -57.71077 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f80d87-53a5-3d79-9834-148de8b6cd1b | -11.53472 | -56.99549 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8ffa7b3-baad-3880-94bd-9a4737a25271 | -12.02661 | -57.08948 | 2025-06-20 05:42:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d7eb0f1-a8e8-3aa5-9888-3b609c48a813 | -11.94755 | -58.7491 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 013d6982-f1f1-318b-8216-079b73a93558 | -11.5297 | -56.99137 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66920d06-4d0e-3f1a-b434-02c6a69bbdc2 | -12.51183 | -58.35056 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4523ebc-ac2a-3124-bb1e-936a3c1e890e | -12.55135 | -57.70826 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fc5f167-8648-31cc-9ddf-c55d873ec248 | -12.55054 | -57.71479 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c62dfc7-04fb-3073-a02b-5e35de71e555 | -11.94893 | -58.73814 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f44e1b33-47b7-3152-8aa6-10e2a7407018 | -11.95308 | -58.7444 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8eed2d9d-4a8a-36af-8a2e-07c90ba0ec72 | -12.89747 | -56.9856 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5efc367-ecc2-34ca-b811-ecb08b6dba63 | -12.89208 | -56.9847 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e752f2-ea59-363c-9ac2-5943a6babe94 | -12.42619 | -54.86938 | 2025-06-20 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deec64a5-0348-3f12-b668-3b4d6046a7fb | -12.05274 | -63.77372 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f955fb-247d-386d-bc1a-be559fb51231 | -10.54137 | -68.57106 | 2025-06-20 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e838edd-4188-3c75-840a-455024614849 | -11.94507 | -58.74175 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e56c38fb-a741-32c9-925f-fb5363e377b8 | -9.95755 | -64.99184 | 2025-06-20 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e0cfe3d-7b3f-3026-a18a-7630b6f93a0e | -12.51034 | -58.3621 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d7e4a7-63f5-3a02-adc8-04c6a3977324 | -11.95256 | -58.75946 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45b11e43-41e0-30e5-ae13-c289580c7462 | -11.5335 | -56.99205 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e92fb3fd-a1a4-3fc4-9b81-134f47286fed | -13.2897 | -57.07782 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a09f0f8b-6cfc-386c-8e6b-c92a246d7572 | -11.95328 | -58.7541 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8069ee63-22cb-3d42-8d35-9444e66299ac | -13.28926 | -57.08147 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c6ceaba-8e7e-347e-8241-76d930cb7635 | -11.53305 | -56.9955 | 2025-06-20 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77d68a5b-8496-3fcd-840b-0b754aaa3769 | -12.28026 | -57.26946 | 2025-06-20 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c64260a-b738-386b-8427-cccd322ab7ea | -11.62267 | -58.2913 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 940263eb-02f4-3261-bfbe-1ed67d993603 | -11.83918 | -57.76389 | 2025-06-20 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d7f337-f937-3cbc-a8d8-fd4b665a6d20 | -13.14192 | -56.80735 | 2025-06-20 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5474e97e-490e-333a-aaed-549b50e8bf4d | -13.14315 | -56.81153 | 2025-06-20 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d499ca3-a5b0-319f-a910-1161f7077209 | -13.77605 | -54.19999 | 2025-06-20 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f255802-6d45-3c28-802a-ba28f4b8557b | -12.50607 | -58.35564 | 2025-06-20 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b1497e0-3209-3e02-833f-6e92fbbdbab0 | -12.048 | -63.78132 | 2025-06-20 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dac39482-ee83-3493-becb-a74165546e46 | -11.95102 | -58.76068 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05e1df0f-7700-37f5-bc28-ae3fe20b5864 | -11.95401 | -58.74866 | 2025-06-20 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eab55afe-a39a-30b1-989c-6196a95405a6 | -14.17363 | -60.05245 | 2025-06-20 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359c4f21-7588-3c6a-b501-a9a94236d324 | -16.30106 | -58.25755 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6e95eaf7-659d-3616-b3c2-fba7bcb1a3e0 | -16.30637 | -58.25821 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0c848a90-a11a-398f-8168-791050ca324e | -16.31169 | -58.25893 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e1809cec-1e92-355b-bd92-04ca07907c40 | -16.30524 | -58.26834 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5b2f96ee-d958-3f4f-87e5-940879e79d76 | -15.62402 | -57.31118 | 2025-06-20 05:44:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64f3d86f-1c8c-3c75-8529-4af6650455db | -16.29953 | -58.2712 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b225639-9c63-3777-b270-6f8bbd5012c7 | -16.317 | -58.25964 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8dda2afa-3abe-3a5b-9e03-78935cf199e9 | -16.31131 | -58.26226 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 910705df-15cf-335c-9e35-cba557a38f73 | -16.29535 | -58.26036 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2bf5d658-8013-3eae-94fc-3d746a85a638 | -16.3003 | -58.26437 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 163dd02a-f1c0-3c6e-b576-188f48b019fa | -16.29459 | -58.26723 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eedcb42f-cfb5-3f38-8550-556b19726a58 | -16.30562 | -58.26495 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cb5b3698-5117-3ce0-89bd-b625464110d8 | -16.30068 | -58.26095 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 81630949-5048-39dc-a7c7-3f7bb31c52ec | -15.62445 | -57.30746 | 2025-06-20 05:44:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb70e2d1-68fd-37bd-ad31-a948811a684a | -14.16846 | -60.05656 | 2025-06-20 05:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcf85a7-8ae5-3354-ac9e-b290dfcab804 | -16.306 | -58.26157 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 58220729-4400-3c0d-901d-e58ccbc89e53 | -16.31093 | -58.26562 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e7b9e184-a3d1-3fd4-8afe-5687154d4fd2 | -16.29497 | -58.26379 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5d20d071-cd13-34f4-bf90-7e8888444e97 | -16.31206 | -58.25558 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 72b1e446-d518-3979-a3ac-9dcbb5290a66 | -16.29992 | -58.26778 | 2025-06-20 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README30.md)
