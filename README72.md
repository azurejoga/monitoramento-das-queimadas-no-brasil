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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8eed6c-1b5e-30fc-a0ac-38b177ddf8b4 | -16.62284 | -52.58204 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86c5220b-de72-3541-9dcf-b4699ecf59ce | -16.62247 | -52.5843 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6a60051-13cc-34e9-8a7c-f02256015120 | -16.62188 | -52.58694 | 2024-10-01 04:14:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbd0786d-3863-3209-966d-b39ced8165fc | -12.90725 | -53.88503 | 2024-10-01 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10855e26-cccd-3455-8d11-8adf2c3441eb | -12.90657 | -53.8885 | 2024-10-01 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d711d7bf-01fb-3300-a5ff-e17e848d6d0c | -12.90402 | -53.88342 | 2024-10-01 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c065a0-0261-3edc-9e74-3847ccc1a42b | -12.90336 | -53.88693 | 2024-10-01 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69a4ed17-e5a2-3747-b810-124b0811cd71 | -12.90126 | -53.88741 | 2024-10-01 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33e6307e-1991-3b1c-bc96-1a3b2fbe4d2c | -12.77046 | -53.98831 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c1f8221-7cfc-3e4a-83f4-e69f2f242da5 | -12.76509 | -53.98726 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf79a7c0-8b4a-35f0-aeda-57568df37b29 | -12.68426 | -54.08726 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ea27bc-20e3-37d4-83a9-50a1fefa0926 | -12.67955 | -54.08262 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d00ee2e3-f6fb-34da-8cff-1384ef02a8e1 | -12.67884 | -54.08627 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d3db72f-e20b-39ef-b495-49a684843aa2 | -12.67813 | -54.08986 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19ada2c9-9df7-3b32-b7b9-e5b53b37bb23 | -12.66949 | -54.07666 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea46a23a-61bb-373c-beeb-608c0415ac75 | -12.6648 | -54.07195 | 2024-10-01 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8111fa0-93c3-31be-a6c6-3e37928dc9a1 | -16.4564 | -53.93508 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60367d33-153b-30b7-8c2c-04641082ba61 | -16.45578 | -53.93825 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2500e5dc-8618-3e4f-9b15-663402eb6862 | -16.45259 | -53.92804 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5260cbba-dabb-30e5-81c1-8b324343167f | -16.45199 | -53.93106 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 093545d9-0b60-3927-9d73-260a3ec7927c | -16.45074 | -53.93742 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 703ad6bb-6c4e-3d2e-8c29-21b4556617a1 | -16.45012 | -53.94061 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 347e01ab-cc8c-32c0-885b-fe159a1f08bf | -16.44888 | -53.94693 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6e8c901-eb0b-399b-a13a-2c0ad16329ef | -16.447 | -53.93002 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f2b1960-42b6-3178-8c86-ae8ed81794bb | -16.44573 | -53.93645 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 751b6e13-e14e-31bb-8549-291b6f8516a3 | -16.44511 | -53.93964 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 351b2e20-523b-3784-8893-d1d8c5811274 | -16.43871 | -53.91934 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf2da3b4-45eb-3915-88fd-43d9cb1e5055 | -16.4331 | -53.92141 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef8a2b31-6bca-3760-bd0f-6bc3261f50b5 | -16.42807 | -53.92057 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6774d38-64e7-368e-9c52-cd80325fbda2 | -16.42247 | -53.92262 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d10b9dc-a1ef-31bf-8ee1-ac6c84b9ecaa | -16.42186 | -53.92566 | 2024-10-01 04:14:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 409e6324-7be8-3ef1-a837-263aa0f03bdc | -16.08833 | -53.54183 | 2024-10-01 04:14:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee7703d4-f647-3bf7-83e7-983b4861a63c | -16.0872 | -53.54763 | 2024-10-01 04:14:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a12e8784-eb4f-3ca0-a574-5a7256bab006 | -16.08462 | -53.53465 | 2024-10-01 04:14:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c60b41ff-864d-3da2-b6b2-763152168aa0 | -15.68899 | -53.91726 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0286907-1287-3e22-a498-809b45e2381a | -15.68784 | -53.92312 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50a3e6c0-a118-31a5-a807-e04ee4aa1598 | -15.68725 | -53.92612 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec6c24ab-70f0-3a1d-9be9-6329aca0f47a | -15.68394 | -53.91616 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77742d32-d25d-3d21-979b-4fecdb50b3a7 | -15.68337 | -53.91908 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bde35e4a-cd7b-3a2a-9089-d435fda36000 | -15.68279 | -53.92202 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90bd7f9d-b96a-3c40-9671-f354f500119b | -15.6822 | -53.925 | 2024-10-01 04:14:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69645338-7387-32bc-99d5-ab5af75802b9 | -15.37319 | -53.75964 | 2024-10-01 04:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec83e1f-75bd-3a33-a6ea-fc3a0528cccd | -15.36815 | -53.75859 | 2024-10-01 04:14:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 033fa8a6-7af4-3b26-ba3e-506eb40e8d61 | -11.37559 | -55.12202 | 2024-10-01 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24ca759e-1b0e-3398-b165-7fc8a7f722ce | -16.64852 | -55.21232 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f4ef19bd-2f47-30b9-9e67-afdc2541b67e | -16.64703 | -55.21255 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 04d97b83-3d81-3c71-9393-67f4b5374d38 | -16.64463 | -55.20396 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ee31851e-b04d-3559-bdca-2306955248a0 | -16.64313 | -55.21112 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90a3eb09-850d-38ce-a027-458ee4d2422f | -16.64237 | -55.21472 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 210c5b50-ce33-37d0-9e15-7e81906e39b0 | -16.64091 | -55.21495 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| edf5c283-90bb-3a92-b930-5fcbbdc745a7 | -16.64001 | -55.19913 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3f0c7191-2331-387a-9d73-a6763daf7275 | -16.63926 | -55.20274 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1a220058-1fbe-395b-91c3-b8c0c1cd6d97 | -16.6385 | -55.20634 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bb34336d-c5c8-35bb-8ffe-95d705ab17cd | -16.63845 | -55.19932 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a12cc918-fb56-31d9-81a5-4a0e7ce3a8ea | -16.63774 | -55.20993 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 877011f8-cb5d-3c71-af3f-cb1447d3e34e | -16.63772 | -55.20292 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a731561c-ac55-3311-8e4c-bcf27e40767e | -16.63699 | -55.21352 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 34472a22-8f0c-348e-b202-e8a2f04d0078 | -16.63699 | -55.20654 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5cea906f-cb4c-39e5-8a22-0d263e235126 | -16.63625 | -55.21013 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b7393621-f7e7-33f7-ac05-b3c235750b54 | -16.63615 | -55.19072 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1ae9eb16-7b31-3283-be18-55f02ef37de6 | -16.63552 | -55.21374 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0d473dd6-67ad-3098-9c06-61c9fbde1a97 | -16.63454 | -55.19088 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8ffefcc7-b027-3055-ae4b-7f89b8069d64 | -16.63387 | -55.20152 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c86e3faa-2e85-34af-8bf9-966212c45d3a | -16.63312 | -55.20512 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 66430bb7-aabc-3d99-891e-51f2e17c5903 | -16.63084 | -55.21589 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d842d27c-27e4-3942-aadc-4ccdb31d08ac | -16.62843 | -55.19324 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1bafb47a-c600-3ca1-988d-f3669dc773dc | -16.62769 | -55.19685 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 53b65638-80ea-335c-8236-37faee074fdb | -16.62696 | -55.20045 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bb510aea-8955-3953-8d25-4b8cb90f6015 | -16.62622 | -55.20406 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ae0cac6-5f22-3277-9ef4-606b0500cc9d | -16.62549 | -55.20766 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4614ad41-23b2-342e-ad7a-320dc0f3398a | -16.14128 | -55.42523 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 198d7cce-5a32-3d2d-9773-d1bd661f84f1 | -16.14044 | -55.42935 | 2024-10-01 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e4827e9-4b71-320c-a45a-2673a4064f3a | -15.9145 | -57.21262 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ddf0bd71-be13-38c1-90b3-02b19e61777f | -15.91341 | -57.21777 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0f4ba73-3922-3bb8-be01-0c7153ace358 | -15.90951 | -57.17517 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56fddd6f-bc76-3579-bebf-3e0d3926ed6f | -15.9087 | -57.17895 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0202ba0e-df18-3336-9fcd-701851e7c00d | -15.90858 | -57.17327 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7653927f-df7a-3911-9abb-ce27ff979fe7 | -15.90784 | -57.18301 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e7e0c00-fd7c-3024-83fd-1b704d985697 | -15.90775 | -57.17702 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf8b2830-7d04-3063-83c3-6f8dd79c944c | -15.90688 | -57.181 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b26f6970-76ca-3b06-89ad-0798f5dc1231 | -15.90353 | -57.17294 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 471f92ae-0b09-32b4-b6b4-0dcdc3b6e295 | -15.90269 | -57.17688 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27782022-df66-3645-b810-00540a000e52 | -15.90177 | -57.1812 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c19e3327-37a1-36ae-b338-c66539194928 | -15.90083 | -57.17915 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5a8fbed-c7ea-30cf-b069-820a6080d553 | -15.90077 | -57.18589 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30ed1f3b-186e-3a19-934e-a9305f566341 | -15.89983 | -57.18371 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b7c5160-daaa-3d37-9df5-ca4124953bd2 | -15.89876 | -57.18858 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1166e244-50a6-3541-b884-4177d8301f15 | -15.89354 | -57.18955 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 633427d5-1185-3f7e-b4e3-8195d9d36329 | -15.89136 | -57.19284 | 2024-10-01 04:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd86ed81-27cd-3878-bc73-4bf582f60de1 | -15.62926 | -57.45933 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed84512e-3d7d-352a-8bdf-8051c086b86a | -15.62299 | -57.45783 | 2024-10-01 04:14:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92bbaff9-bfb7-3a23-957a-12217c2c0ba6 | -16.06922 | -50.35831 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80f0538d-3c05-3f8c-8f22-4257f05ae9c7 | -14.48055 | -45.23048 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ed2ae6d-f615-3179-9832-06dfcb43d3cf | -14.30785 | -44.73203 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ffab8bd3-8175-3699-9893-ac9093502bbe | -14.17599 | -46.46452 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 233648db-08fa-3308-8961-264853a4a1d4 | -17.20128 | -39.51219 | 2024-10-01 04:14:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7976af24-c6d9-37fd-abf7-1c9fa84a2343 | -16.94993 | -40.7639 | 2024-10-01 04:14:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 415412c0-fd90-3a50-9a75-e97643559b31 | -15.58612 | -42.07635 | 2024-10-01 04:14:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58556ae8-1303-3026-aaec-b29632ef0027 | -16.49555 | -41.44372 | 2024-10-01 04:14:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d433aefd-5dda-3bb7-99ff-d8e3376f4bb3 | -17.78529 | -42.89116 | 2024-10-01 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
