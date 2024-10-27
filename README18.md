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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4da76909-c2e2-30c9-b569-e241d73694ff | -2.7793 | -51.964401 | 2024-10-27 01:10:03 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66bc211-ecf6-3a2b-9e4c-efcf5abe39e7 | -3.0736 | -53.236599 | 2024-10-27 01:10:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9e857c-7028-3df0-9754-2fd9c7c9a8db | -3.0752 | -53.243599 | 2024-10-27 01:10:03 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61b49412-1398-3594-8362-7951c9c33334 | -3.2571 | -54.168201 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67abbf8f-7375-36c5-b077-0322ac2a66f1 | -3.2586 | -54.174999 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f345a6-4936-32d3-8ed2-37deb6a1e2ca | -3.5502 | -55.4492 | 2024-10-27 01:10:04 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e2ae60e-476d-379b-b6db-ecb46463b754 | -2.5514 | -51.160801 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4184bd-9e24-36ec-9808-1a53cb319791 | -2.5533 | -51.169399 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d81722-3753-3620-840c-517c9f0cde56 | -2.5553 | -51.177898 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 333493fe-24c9-3723-b0e2-e0abb94cd83b | -2.5396 | -51.154499 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8e53c9-41fb-38a9-94ab-1dffd39424b6 | -2.5416 | -51.162998 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8744c3dd-31b1-3c3d-b073-ffb08d06e2ab | -2.5435 | -51.1716 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab12b36-f56a-3f20-983f-215c0940e211 | -2.5455 | -51.180099 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77bc3b42-fa7b-391e-9190-9866a50fd0ea | -2.5475 | -51.188599 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22c88dc-bb39-3fba-9fa2-60b37aa3e925 | -2.9739 | -53.028198 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec59af02-98be-3eaa-a696-3ec7cbfbfdaf | -2.9756 | -53.035301 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8b7d61a-22ad-3323-a352-e4aaeedfb1d8 | -2.9772 | -53.0424 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4642e6b2-56e6-331c-9a2f-8ac9ba40cfb9 | -2.5298 | -51.156799 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 003cce8e-db20-33e1-922e-005dcb58d3a5 | -2.5318 | -51.165298 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a17a82-964c-3561-8027-2e33bf271af3 | -2.5337 | -51.173901 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31f00ef5-f8ee-3108-a042-de8cc9f688b3 | -2.5357 | -51.1824 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b10ba6-6f30-36b8-8867-3f83f7731941 | -2.9641 | -53.030399 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6624e0ad-550c-3426-abb7-06c2adaf6387 | -2.9658 | -53.037498 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a484736-a804-3caf-9f5c-a928f8b65bef | -2.9674 | -53.044601 | 2024-10-27 01:10:04 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d1da54-f546-3c09-8129-bd14cb94b510 | -3.119 | -53.702099 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c13260-8f54-3646-9eca-f4d0950667ba | -3.1206 | -53.709 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27babc9e-df61-3d17-9617-a42393da19eb | -3.1222 | -53.7159 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f1c7ae-1de5-316a-ae3c-a0436c421ffe | -2.52 | -51.159 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6cfb7c6-65c9-3436-ab91-fc5b9a7a7e95 | -2.522 | -51.1675 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca82cf70-6b71-3972-b31d-ccec560a097d | -2.5239 | -51.176102 | 2024-10-27 01:10:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd28e402-37ed-374d-9674-64d72501610f | -2.8405 | -52.539902 | 2024-10-27 01:10:04 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1c552f-217a-3f05-b318-f712a28b9d92 | -2.8422 | -52.547298 | 2024-10-27 01:10:04 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d13ad9-071d-3095-8724-06c00c8694b3 | -2.8341 | -52.5569 | 2024-10-27 01:10:04 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8eeafc9-b54c-3797-bf33-47615765c71f | -3.0993 | -53.706501 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c69b495a-9630-32a8-ba7e-88e28c19635b | -3.1009 | -53.713402 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd3e141-952d-3071-9050-67a535e99502 | -3.1025 | -53.720299 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911ae96a-1032-3cb0-9374-c7c3923ab479 | -3.1041 | -53.7272 | 2024-10-27 01:10:04 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5854eb5-be59-3732-af2e-d09c7e011555 | -2.9853 | -53.2565 | 2024-10-27 01:10:05 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe748b4-785a-3552-a6d9-0aded85ec5d2 | -2.987 | -53.2635 | 2024-10-27 01:10:05 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8bc6b50-ab41-3683-b4f8-0d2ee5ee0dbd | -2.9755 | -53.258701 | 2024-10-27 01:10:05 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f347b92-6fb3-37e3-83b1-264a0b0bdead | -2.9772 | -53.265701 | 2024-10-27 01:10:05 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1b2a28-a928-37dd-b981-2e174358de82 | -3.0839 | -53.8186 | 2024-10-27 01:10:05 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf95e15-beb7-3dec-8397-ff8c5e5977ca | -3.0855 | -53.825401 | 2024-10-27 01:10:05 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce0b102f-f664-3c16-ac3c-5f508e305995 | -3.0871 | -53.832298 | 2024-10-27 01:10:05 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6e7a9b-2bad-335d-9c0f-e35573a9c6ce | -2.599 | -51.765099 | 2024-10-27 01:10:05 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d578e786-da36-3b49-93fa-845383130786 | -2.6009 | -51.773102 | 2024-10-27 01:10:05 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6101e861-7237-3f1b-80c3-b4b1d37978d4 | -2.6027 | -51.781101 | 2024-10-27 01:10:05 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5c01c9b-b898-3e2d-b5a7-a81193f42026 | -3.0757 | -53.827599 | 2024-10-27 01:10:05 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f712a32-3d02-336f-8fc7-e48c971429df | -1.7889 | -48.428299 | 2024-10-27 01:10:06 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2ae70c-e3df-3c95-a50a-2a33d747e9e2 | -1.7919 | -48.441101 | 2024-10-27 01:10:06 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcefa8df-da39-3be0-88ee-49409b799919 | -3.1338 | -54.2603 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b85345-583e-3b4a-a885-5779fc88773b | -3.1354 | -54.267101 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e0b363-a1e2-3e0f-8dd1-292416987031 | -3.1369 | -54.273899 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06aa1d4-673c-31ef-8a6a-b360b48c15d7 | -3.1385 | -54.2808 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 140b74e4-2b83-33f3-8872-93a2afa7e80f | -1.8139 | -48.622398 | 2024-10-27 01:10:06 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c009c47c-c867-33be-a95c-bedc1fa7fb62 | -3.124 | -54.262501 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 430e45b3-4dfc-311a-aaf2-4e9ed5bd4592 | -3.1256 | -54.269299 | 2024-10-27 01:10:06 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9abd22e-ea33-3ef7-a503-d41987eed93c | -2.263 | -50.630798 | 2024-10-27 01:10:06 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582a01fa-f8dd-3aef-ab12-383ee7b1f22a | -2.2652 | -50.639999 | 2024-10-27 01:10:06 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8bed56-b419-3fdf-8008-df5518768c3f | -2.8839 | -53.308899 | 2024-10-27 01:10:06 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c75d65-de1c-3da4-b211-725fd2c9f7ba | -2.8855 | -53.315899 | 2024-10-27 01:10:06 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967d2a50-b1bb-30d7-9d44-7ede73b54296 | -3.0793 | -54.157799 | 2024-10-27 01:10:06 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df4df42-0eb1-3333-aade-4552be691bef | -3.0809 | -54.1647 | 2024-10-27 01:10:06 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e15d502-965b-3802-9a63-3cff0d7c214f | -3.0825 | -54.171501 | 2024-10-27 01:10:06 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa1010a5-b997-3fb9-aadc-58b116e0c8d2 | -2.8561 | -53.322498 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a265eb9d-a5c8-3be3-80c0-26bd2288972b | -2.8578 | -53.329498 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a704ecaf-ac72-3e04-93f1-52542b995325 | -2.8447 | -53.317699 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1966019-5cb3-347f-8b58-e88be13badef | -2.8463 | -53.324699 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41913b24-4790-3314-a62b-0b797fae1184 | -2.848 | -53.331699 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c694ba88-7d6e-3f14-80ee-e00ab911b24c | -2.8496 | -53.338699 | 2024-10-27 01:10:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013a611d-581a-3445-b4ae-22b037391a9e | -3.0225 | -54.134701 | 2024-10-27 01:10:07 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c42e5ac-6109-3c33-b0b2-5cb0a94131f0 | -3.0897 | -54.4277 | 2024-10-27 01:10:07 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1ffb98-cd50-3af9-97b5-94a72e9029fc | -2.6233 | -52.448399 | 2024-10-27 01:10:07 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d123080d-5b88-3c03-a1f3-7abeef98bd47 | -3.0111 | -54.1301 | 2024-10-27 01:10:07 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf806e8-6f7e-3495-ba03-eb2807f4a516 | -2.9937 | -54.234402 | 2024-10-27 01:10:08 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2017d7-ec1b-3f70-a566-ae3fd17f75f8 | -2.9953 | -54.241199 | 2024-10-27 01:10:08 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207dd7e2-a952-3190-a1db-be562293d838 | -2.9992 | -54.347801 | 2024-10-27 01:10:08 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541e1e57-ebcc-33c6-80b6-a274405bced4 | -3.0007 | -54.354599 | 2024-10-27 01:10:08 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af0f369-95d3-3c6d-afbf-0eb1201c186d | -3.0023 | -54.361401 | 2024-10-27 01:10:08 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 381e351e-e62a-3d75-9659-3a4954a75848 | -2.9501 | -54.673599 | 2024-10-27 01:10:10 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c05f802-3f05-377a-83ea-df5233dd598f | -2.9517 | -54.680401 | 2024-10-27 01:10:10 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbb31c7-cc42-32d4-876b-598d0a104812 | -2.9532 | -54.687199 | 2024-10-27 01:10:10 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e86cdbf3-66bd-30ca-8fd5-e3cdb7e5b0c1 | -2.7743 | -53.952999 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf00d7c-0150-3fb0-9aed-778409b76ae8 | -2.7885 | -54.014599 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7122c84-06ad-392a-8249-95ca20a25c6a | -2.7901 | -54.0215 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374b6d2b-fe83-3bf4-be87-4f30267683cf | -2.8074 | -54.096699 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32e67a6-d8cd-3775-b402-101eb3b3a5fa | -2.7976 | -54.0989 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca04d94-624b-32b4-9327-927f72d591e5 | -1.5203 | -48.597301 | 2024-10-27 01:10:11 | METOP-C | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f1a95b-854c-3347-b065-dcef32277f83 | -2.7607 | -54.028099 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e77f91-7979-32d0-8295-238f7276b9aa | -2.7622 | -54.034901 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 288b22f9-15c0-3f39-8e3d-2e44a3c6d6b5 | -2.7509 | -54.0303 | 2024-10-27 01:10:11 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a11d17a-a9d5-312d-a625-2b21026af5db | -2.5731 | -54.019699 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f08d4491-6d82-3107-91d3-8ac79fdc91c8 | -2.6343 | -54.286098 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533b770b-3a79-352a-aba2-2120aa6beaa9 | -2.5471 | -53.996601 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d08ac4dd-c95c-31be-8b4c-e649548c5918 | -2.5456 | -53.989799 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d69b1da6-3957-3743-8b30-567930d876c0 | -2.5633 | -54.0219 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c14be853-410c-3ff3-9e95-8883d9a25f1c | -2.5617 | -54.014999 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f892450d-7a56-357d-8275-f650ee6a406c | -2.5601 | -54.008099 | 2024-10-27 01:10:14 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a7ea4b-9de8-3b39-b88d-eedf96aa9648 | -2.639 | -54.306599 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba5b9a7-ee64-38f9-9a03-7e299c668b7f | -2.6374 | -54.299801 | 2024-10-27 01:10:14 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
