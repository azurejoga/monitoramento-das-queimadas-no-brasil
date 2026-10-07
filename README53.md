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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e21f0cb3-84d7-372a-881a-59122d5a004b | -3.81017 | -51.04073 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13215e94-352c-3d5a-acf7-76919cd3ab92 | -7.60917 | -42.37305 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 96e87aef-36f2-3b46-a445-07d01d18cf06 | -3.27632 | -54.02709 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a97c640-987b-38ee-be71-9da6ba3ce3d6 | -2.77441 | -54.10291 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 17d63383-5c38-3b74-8470-25d103608eec | -3.68574 | -45.84004 | 2026-10-07 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee488665-37b1-3b5b-b53d-908b490431b5 | -3.84241 | -50.9975 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb10d68-b497-3f37-9931-85500300219b | -7.86113 | -44.19764 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 420a81a6-594a-3286-b717-054ba8929b25 | -4.23601 | -49.98412 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d813fe6-8153-3441-9941-79e520cd4119 | -3.15914 | -50.43874 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 956de58c-7ce1-3d9e-a760-262afce40105 | -4.50736 | -45.99629 | 2026-10-07 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8fe0ce1-33ff-3b28-8203-2e50a62ec458 | -3.73184 | -48.87609 | 2026-10-07 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b353b4a1-c65b-3e6e-a7fc-de308822a94b | -3.62246 | -55.28358 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0d7ea781-dac2-3acd-96e3-7e05af6a003c | -5.72823 | -45.16491 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2ca6a5fd-05d0-39bd-8b49-95bcd250d2b7 | -5.05772 | -44.8645 | 2026-10-07 04:19:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5025eac9-5ee7-3938-84af-c903ba98671e | -3.08309 | -54.26928 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e5629e1-281d-326f-8ca3-91589fc16316 | -2.12411 | -54.80381 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e45050c5-f169-31e3-8848-8087f9cbfd94 | -8.18521 | -45.13669 | 2026-10-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e16afcb-761d-3578-ae19-fd52510e93d4 | -3.07163 | -54.14894 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe9e3e85-646f-34ec-bc0b-f195cec66d36 | -7.84347 | -44.15905 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bef6cb77-2e9d-3ae0-999d-c7b037630595 | -7.8462 | -44.20589 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d3e6648-a814-33a5-8c1b-55cee79c4d47 | -7.89469 | -44.17793 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07940564-b7cb-32c3-8d56-1da0fe7129b4 | -3.27096 | -54.02112 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb6aa192-212c-3624-a111-6766db997cdb | -3.27253 | -50.42022 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8ce408e-e1c8-36e7-9f52-0d9ca826f8c7 | -3.49935 | -51.68678 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 360bfaf5-2648-3ecd-a936-6bdc6de0845e | -5.46545 | -41.22725 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6d6cd4e-3de8-389b-8dcb-0ef3f5efe108 | -3.52115 | -52.7525 | 2026-10-07 04:19:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8a00b6c-c893-3e29-ac7e-6eb3f8ba7021 | -7.8683 | -44.21663 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 23f6762e-c23e-32e6-a6d1-5be7a0fb1f1f | -3.05418 | -54.15264 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f3ccac7-07fb-37d5-afc5-4337fdc0a5aa | -3.28624 | -54.07237 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4f434fc-2722-3998-97c3-413f0abad0ed | -7.27851 | -46.15338 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 872c7a68-dc89-39e1-8fe2-bdb7666f05d0 | -4.13288 | -54.9127 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 296ad6a3-21b4-376d-bf6d-83cd80cb31d0 | -3.02633 | -54.5217 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a3dc52-aab9-3918-b842-910d75659d52 | -8.6409 | -44.88314 | 2026-10-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bb9e9cb-da4d-3ef5-9145-21d7a88ef139 | -5.78072 | -41.9261 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66d1b6d6-02e0-398f-a51b-047de571012f | -3.2825 | -54.02822 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6c0e180a-1cf7-3f6d-8180-10e7d36371b4 | -3.61934 | -55.28379 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b845350b-0e2e-3734-91b5-e39c888fe1ef | -2.41418 | -46.03967 | 2026-10-07 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3c9585d-3873-3235-b8f1-25cf05c87555 | -8.38364 | -46.28733 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e393b57-bcfc-3ba3-8e33-dd31ee153115 | -3.0604 | -54.25045 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd426f5d-39c8-343c-bdc3-7fd16bd48252 | -2.97652 | -54.13311 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35f3c04c-4385-3cc6-b624-445ca75f3567 | -3.28787 | -54.03417 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9e6cc193-0f1d-3f83-af6c-c60a43a56d39 | -3.46775 | -49.93576 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bed314ea-2237-3103-b280-2b4eb5bb878e | -4.15395 | -55.16743 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33c584ee-14c0-3b00-a00d-f9999cb9aa2d | -2.78961 | -51.67739 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0835703-0347-303a-bbdb-8ca1b3d92aa9 | -6.59198 | -41.55186 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2297e22-88bc-3b6b-9891-ec90fbdb53e0 | -2.76523 | -54.08049 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bd83568d-0757-34fd-a376-804dc40e6c98 | -6.58234 | -41.59176 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb3eda4e-3936-322f-b8dc-db9ba5932fa5 | -3.84828 | -55.99006 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 252c701b-b068-328a-8b6f-b7302e0aa19c | -3.16893 | -50.44048 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7381d9c5-d1a4-33a2-b285-b7df0843858d | -5.23782 | -50.9188 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 800ead02-d8ac-3147-a608-9246163624e4 | -3.51968 | -54.6417 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13bd461f-8f33-36ec-ae2a-9c764a95f7f3 | -2.95847 | -54.14673 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a78ca2aa-0b74-346d-99aa-f45acbbe2223 | -3.07767 | -54.26309 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04dcc2bb-f72e-32d1-bbcc-5624fd0f568f | -2.8163 | -49.25247 | 2026-10-07 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ead3aaf6-e3ab-343e-b6ec-f48a4ef76d11 | -3.28413 | -54.0186 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e4143d2-e0ae-3171-9d12-88dc41dfca1e | -2.13071 | -54.80495 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4460ee5c-d844-3751-abb8-1de5d3eec34c | -2.90825 | -49.17402 | 2026-10-07 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 715830e9-9434-337b-8732-6515b7853d55 | -5.67466 | -42.58118 | 2026-10-07 04:19:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dde54647-d4e6-3686-b08e-64116c8a600d | -3.28539 | -54.07721 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ac93738b-52e4-37b5-833e-12025922717b | -6.33711 | -43.82465 | 2026-10-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9c1cb95-d539-38cd-9bb1-e6b8cb45fe72 | -3.17381 | -50.44141 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 202541f7-0c33-341c-9641-13eaf15d5c8e | -4.2867 | -43.64102 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d4e25d-e0a7-39d5-ac62-da08c8bdc34c | -6.7337 | -45.80276 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2409bbd-3bb5-3d8a-a365-bfaacacc769f | -2.12651 | -54.80174 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 26ded674-081e-372b-a856-d2577df3495b | -2.98271 | -54.05729 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c87953f3-c2ac-3430-9a34-72d297424269 | -3.27924 | -50.41027 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f43ea05a-e12a-363c-9afd-da8d0aef6097 | -5.24168 | -50.90942 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c5d94f1-65c1-36f3-bb83-37b4ca3a7266 | -3.05334 | -54.15761 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 834127fb-3476-355e-9a6c-57c27f16b09f | -3.52976 | -54.65339 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0699f23-eefe-3227-90ac-eddc69a977ad | -4.79158 | -45.80795 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae666dac-dfaa-3ad0-ba31-f8c448d52a6b | -3.53606 | -54.66117 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5c417591-0c39-3287-8e39-48ba062ae32e | -6.89321 | -43.68237 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64bb2129-07a8-3e4c-8f78-de1adbadd49f | -2.78368 | -51.67991 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e79ba9d9-1ed5-3bba-b42e-463513c1de51 | -3.80131 | -51.99441 | 2026-10-07 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41aa570c-fa91-34ad-8c07-c79e55ad6978 | -6.59481 | -41.5561 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4162485f-5b7f-3ea3-b005-5da07483d484 | -3.10593 | -53.77004 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d23ce2fc-eaec-335c-919b-df55fc087891 | -4.75026 | -55.65823 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82fd5196-128a-3980-8fd6-0938220287fb | -3.28462 | -54.05337 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| daf85b1b-d3de-333e-9beb-35f9e7cece78 | -5.44411 | -44.55816 | 2026-10-07 04:19:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b0462e3-4768-3edb-b8e0-a3e9b9032d9f | -3.26766 | -54.04055 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 86bebf5c-c199-3688-9ad4-b7e82f5c9ec6 | -3.26949 | -50.40858 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0221b26e-c2a1-387f-90c6-f3f97e9912a8 | -3.05237 | -54.22224 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efd8e74d-ef13-331d-a865-23f0cff48211 | -3.18669 | -50.55779 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3bcca83-647a-3ce7-88d1-012d45382f66 | -3.47143 | -50.08711 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5bd919f3-4aea-31db-9f93-44b54fc7eb20 | -2.93991 | -54.12098 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 280df119-615e-385f-b169-53582ed66c1b | -7.97118 | -44.50682 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ea3fef-efc6-36ca-9ec8-9e90838af440 | -7.60582 | -42.37252 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aee1bdc0-8b0d-3601-8835-74b07217c01e | -5.581 | -48.9516 | 2026-10-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a20ca84-7c5c-3dd3-ac09-04a7b7d4e559 | -3.28711 | -54.06741 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f07cb088-1944-3cb4-b720-2f99a0dfafeb | -2.20789 | -48.1503 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96a3614c-89b9-335b-b066-493c2cea7d95 | -5.72024 | -41.68305 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69a60b8d-d7f0-305e-94ab-0b844e402a6a | -4.75143 | -43.26296 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 802fdd69-df80-3f69-a513-007b415cbab8 | -3.24372 | -47.25021 | 2026-10-07 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16fcaa58-1efe-3b3d-a892-515f87fe5a12 | -7.76242 | -43.79289 | 2026-10-07 04:19:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d7199aa-7292-3909-8030-d2040c2c2381 | -3.15519 | -50.4447 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398f471c-5674-303f-960d-58c76b62c9e3 | -7.45063 | -46.83598 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e011d25d-b59d-30a5-83e5-4c99fd0847bc | -3.93648 | -51.01748 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ecdac07-94c3-38f5-9a6c-ebbe3a8929d8 | -6.21754 | -52.83358 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d539c6-0572-3ff2-ac9f-22d34fa08b60 | -3.00668 | -54.12893 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ba877c1a-e627-306a-9130-b65792e5fd78 | -6.15344 | -51.73222 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
