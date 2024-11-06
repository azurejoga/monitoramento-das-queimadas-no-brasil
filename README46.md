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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67171dac-6a42-3d87-a87e-10ba58160c7d | -2.93694 | -51.05006 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 070d838f-da3d-36f6-9dd4-0d50603e50d9 | -2.85958 | -51.78152 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6f7bf42d-cfc7-3246-9380-f94f8f4bb065 | -2.73957 | -54.12674 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1ab4475-2678-315b-8723-00d9bca42c4f | -3.00991 | -53.42741 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b9c0e1e8-78c7-37bc-9f46-31a66bce0ea5 | -3.21234 | -51.16605 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2335f21e-4e22-3e22-a63d-25c268a457a9 | -3.01304 | -53.43324 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c484979a-725c-3889-9dc3-93e906de3b08 | -3.15055 | -51.32737 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce44adc3-57a1-3939-b10a-0a95f96fbcd7 | -3.00431 | -54.0921 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39e633d-2797-3de9-97ae-c9b914565f67 | -2.84366 | -52.90857 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 921c5c3c-aa27-3912-a2df-57c1c85d6904 | -4.49123 | -50.75697 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb6d8759-423a-36aa-becc-4e1862f36103 | -3.17707 | -49.09942 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eee51d49-0812-3b3e-b027-57c919c98616 | -4.06005 | -44.80791 | 2024-11-06 04:36:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2a6b28b-26da-3852-b706-89f55d71fbde | -4.12469 | -43.58223 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c28ef3a6-9755-3f0f-a0be-7d555dd6f945 | -2.84502 | -51.794 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f19ba39-34a0-3634-bf18-47efd1f81edd | -3.01253 | -53.42974 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 005241b7-b800-3bd8-90dc-0b9c37cbda62 | -2.81374 | -52.94764 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3ed7822b-52c4-3116-93c3-b766b6d3bc04 | -2.52698 | -49.19149 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50e7217-b10f-3716-a92d-ffcc2f852389 | -3.09089 | -51.35916 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e59019f-2775-3f01-a7ae-76c72cc10014 | -4.06061 | -48.25347 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b668b45-8bc8-398a-adcb-1bb82210288b | -4.28164 | -48.64212 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3408895-7f07-35ed-b273-5b7af1191765 | -2.84621 | -49.47206 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4591c57a-df66-3570-97c5-b31eebc30782 | -3.31763 | -40.03922 | 2024-11-06 04:36:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 43029443-9594-3c61-88f6-c6e019543731 | -2.91139 | -51.05386 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5dc6a73a-8987-3017-9fec-5824e666cdb8 | -2.59833 | -49.25578 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 104e3632-d1a9-30d8-8b3d-e2c52728dab5 | -2.78238 | -52.87434 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9225cc2-c5b2-310b-93a2-469604538f5e | -3.97581 | -48.16566 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f06c8e3-6d62-3fdc-aa69-34508febc06f | -2.82016 | -48.56087 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d94f72e2-dcaa-3af1-8ace-c7323830d9cf | -2.64963 | -48.52038 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec6cc6b2-31c1-3980-a2c0-a88649dd2dca | -2.82064 | -52.92934 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| de7b163b-4694-3d5c-82f4-85dcaf303d20 | -2.95029 | -54.80323 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6aaceed0-bba2-3c59-8d4f-47a1e8d6c9fb | -3.15469 | -51.32402 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21ab596d-85e4-3c1a-81fd-30ad8db5a5f5 | -4.14226 | -43.57735 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bad0648e-60e7-36aa-a19a-de9b89afe4dc | -3.80277 | -42.55229 | 2024-11-06 04:36:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 040ef5e5-cf5f-3a8e-8ec2-71e7da1d709a | -3.34121 | -50.14103 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5743e9e-38a1-30d6-903c-1f1323f53d46 | -3.21481 | -49.22532 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e32a919-9bda-3b6f-81ef-e810f7e65aee | -3.11246 | -51.1114 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa986d5-8650-3708-8e35-bb451a092464 | -2.5225 | -49.15541 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ae8cbbf-8e3a-3f11-8291-f640b301361b | -4.13043 | -43.57183 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e27ad91-8860-38c2-9488-a6df33b82bda | -3.04235 | -53.27325 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22828842-4d8f-3ac6-8063-5542068e6735 | -3.16924 | -54.47025 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 388f9c08-a751-39ca-a4a9-b94c2eb9d1a9 | -5.23894 | -46.65178 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 322a0900-f324-3859-9239-ad98c0fd30d5 | -3.02612 | -54.08799 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35b49104-b49a-35c1-856e-93c61a81b17d | -4.78255 | -48.91481 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d66b98-a4bc-38bb-9401-3e5d91a05d5d | -2.88244 | -51.66316 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddd6448-1a6a-3468-bf91-9e7e74e87d1f | -3.44408 | -50.13542 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d667336-162a-3841-a83b-23970ae3c27d | -3.78264 | -50.14421 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ce0be11-3b3c-30df-8cfb-1970b5a0b07a | -2.84899 | -49.47606 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8a767b4d-ec02-3db7-ba59-5cc4c03d2bbb | -2.78605 | -51.36224 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244b0774-e165-3958-a610-728f64f2daab | -2.65913 | -48.56754 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32107637-db6b-361f-b586-fbce167516c1 | -3.30407 | -50.1463 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6f99c1d-455a-3360-9594-ab4d42276917 | -3.97357 | -48.15821 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caf1d458-fa68-38f5-b781-5cd746f745bd | -3.29523 | -50.02818 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4f5fe7-3de5-33a0-a2ca-eeec135b1cf9 | -2.85417 | -51.78273 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d05c8b28-d145-32ee-b04e-b5740cdfd49d | -4.2557 | -50.98076 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bee90395-f6af-34d6-a4cb-b0bbdcff40fc | -2.4231 | -46.6922 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e60c00e0-ecc3-3662-9b31-facb7aa0827b | -2.89955 | -51.4675 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da79ceaa-5694-36e3-9c97-73c433e2a30d | -2.99443 | -51.05773 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 175b3ebb-2505-3343-abd8-e9ce5974dfc3 | -2.88602 | -51.66371 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2605ef49-575b-3bc1-829b-e376f171ed9f | -3.21865 | -50.37982 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 512b2153-8c8c-3769-ba20-0c8e7286b284 | -4.03142 | -48.28799 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d25a490-54a0-37bb-b05a-fcfb36c2c643 | -2.2491 | -46.59426 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65178670-f5fa-3bcc-96fc-7bdfd17bc2fb | -2.49148 | -49.17846 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31267b3-a576-3a32-84ab-5d7bbfd8b11b | -2.74628 | -49.13717 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ca38250-c6f6-3450-a679-a29ca88712e9 | -3.12694 | -54.25311 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d28e9e93-2dc9-3d1a-9364-1781f128da4f | -2.88778 | -48.73307 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b8a6d6-b158-3372-ba2e-2b9186b89991 | -3.5281 | -51.32092 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a60e3a80-0474-3cf2-be2f-919fb33e95b0 | -2.23936 | -50.69459 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5052eaec-899e-3d02-8fc8-ee39e06f7d6c | -2.99332 | -53.84737 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc6bc4f6-7a51-3e51-af10-ca1289a8a0e3 | -3.84964 | -51.39376 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d18fccf7-5a29-33a7-b69f-2dc216e80e2c | -2.96351 | -48.72738 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0abd750f-9737-3f59-9a86-ee553f2117a8 | -3.24525 | -53.409 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb150dea-a993-3e0c-9a98-3cc10590df9a | -2.46675 | -50.23394 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c6f4704-3bef-3541-9e24-7a709bc4824a | -2.90746 | -49.40724 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e4732f5-b99d-3a81-ac75-244aa0675e6c | -5.06798 | -44.23163 | 2024-11-06 04:36:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9ce32bf-c21e-3569-8f9b-b0bcd8b97c0a | -4.13675 | -48.24399 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9f64ad9-37c4-335b-976f-491bb59b171c | -2.81836 | -52.94345 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ecabfbdb-f328-36aa-ad7c-11c64dd5993a | -4.67217 | -48.77387 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce3259be-ac6b-3eac-b396-3fa40da42712 | -2.60162 | -49.25634 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0012c76-8938-33ae-b800-027ae87d9fd7 | -3.11905 | -53.1218 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6920884-861a-319a-84e1-76dd16c6a2aa | -2.81603 | -52.90911 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b64ccc2-8e6f-389d-ad7b-6b300b01723e | -3.63855 | -50.13665 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be6da77e-bdcb-3f50-a79c-33c132d367ac | -2.30608 | -50.67019 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a478ad2-4d18-3a86-8cfe-d237f261d12c | -2.82606 | -52.94464 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ddf26721-bba8-3e8e-bd7a-e845db74290c | -3.2198 | -50.37259 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 20acfab2-193c-3584-98ea-2bbb9c7312c9 | -2.4447 | -53.94028 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8280203-535e-378d-93d4-8bd40c23df63 | -4.27626 | -50.71945 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1661d31-3e8f-3cb3-ac5c-68e6f4d8ea74 | -3.62113 | -45.3942 | 2024-11-06 04:36:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c57b9f3-ce6f-318b-bddc-8a30faca5ec5 | -4.12989 | -43.57554 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ad08ce3-daf3-3f00-885d-8f88950fec56 | -3.08085 | -52.42576 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdb54f38-6220-3aa6-8793-5aa0ea508846 | -2.80655 | -51.48332 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f3ef70-81c4-3060-bbdf-1f2a1f523bb9 | -4.42738 | -50.08618 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78e04e88-a6f0-3395-b62c-07c690c21658 | -2.8914 | -49.3795 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4226e930-f5f3-3de7-bb23-6738bb454e4c | -3.03374 | -53.27697 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fecc7653-bcaa-325d-b198-9a469ce19bd9 | -2.82682 | -52.9399 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95968bc3-b7ba-3c89-9cf8-6bfe73fc246b | -4.06006 | -48.25693 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca90fa88-a548-3aed-8508-0a1f004bd5e5 | -2.64612 | -46.76748 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d82db05a-0745-3de9-8e25-4114d17b53cc | -4.44851 | -50.69786 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6850e6d7-8e96-3b4d-8590-9b3f0b1f6331 | -1.35308 | -51.94794 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fa3899-d684-3ce9-a5cd-63384e2a6e11 | -3.79982 | -51.41363 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52fd3ec9-8d03-3c87-9516-4babdef2b1d3 | -3.26614 | -50.34279 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README47.md)
