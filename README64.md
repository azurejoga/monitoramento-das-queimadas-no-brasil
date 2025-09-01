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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7368711f-84e6-33d2-8999-faf77a5545b0 | -13.16162 | -45.28725 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 888f9724-2d25-3abf-ba09-43a26ab343c4 | -13.59608 | -48.14443 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbc7330f-bd64-3fb0-bad1-4cf825cbf5b4 | -11.48819 | -46.81687 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6124da4-3447-3e15-b1be-4ae532b062be | -12.9482 | -48.10049 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74d1316b-0856-3d8b-a6ca-9b7e0194403b | -12.98141 | -54.75368 | 2025-09-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3c8683-6e5f-3fae-bb79-09cd7691b560 | -11.08028 | -52.05163 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58a08d78-571d-3e2c-8c1a-dec3ccd6098a | -14.33734 | -51.88094 | 2025-09-01 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dad26d03-1b7b-30a3-8072-9f1b9c2fa98d | -15.77699 | -47.80634 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f009a73c-e384-3ad8-ba89-b526e14020e4 | -9.11167 | -61.21324 | 2025-09-01 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ece9489-53bb-3f0b-912f-6a62d966aa7c | -13.37309 | -46.94548 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c73d34b5-4a69-35a0-8c60-735913235f38 | -12.95716 | -48.10939 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f91753b-f620-39c3-8c27-596c5b5883cf | -16.97503 | -49.30986 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18aa63b8-d602-335a-98b1-15566cd2fb9e | -12.63013 | -57.00659 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30dcbd04-e103-3e99-b3e5-d63ebb6e6f32 | -14.78868 | -46.71905 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 851e78a7-badb-366f-ae58-42b826726b18 | -10.84412 | -55.75225 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b76a470-b3ee-3254-acce-012bdd8fb196 | -14.76037 | -46.76222 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aeddc6d8-b78e-3750-b10e-c6b569d6f882 | -14.84898 | -47.09368 | 2025-09-01 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfb5f745-3d33-3dbf-ae96-efa501767e70 | -15.75906 | -47.75949 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96f19a90-eab2-320b-ab39-82a635085963 | -15.58319 | -48.33508 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb438f48-66d1-3b72-b2e4-7e6d0b3ec53d | -11.32811 | -47.36406 | 2025-09-01 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b187e7b1-5662-3bb8-857d-5b2387551e03 | -18.12185 | -44.98772 | 2025-09-01 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20fafdce-f94b-3ef9-95bf-e99f108bdae8 | -11.65108 | -57.36345 | 2025-09-01 04:34:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4cbf03bd-abb3-396f-a756-c3006f15d7e6 | -11.81424 | -51.45701 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 141bb69f-cb53-337e-ba5a-6541bcb8c475 | -14.20779 | -48.37928 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeaebfd6-1a63-39fe-a48b-80cce304075a | -15.59341 | -48.35962 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e3fe3cb-4dea-378b-bcc3-34e53a7a6e5d | -11.68025 | -47.5826 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c73ccfc1-185f-3387-8d86-870c93c4e156 | -16.41059 | -45.65054 | 2025-09-01 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 037419d7-da71-3d42-b5a5-006c1a28b297 | -9.43681 | -60.57267 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 268101a4-9314-3cc7-8082-5088d3fd13fd | -13.701 | -46.92347 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79aaa3d1-b51f-3283-8061-ab3a59605a5c | -11.34449 | -43.67605 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ab658f-0c21-3eb7-85fb-e9e1fa920686 | -12.66428 | -48.22275 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bf35dfa-d1b6-380d-a9fd-3a570f01df03 | -13.51359 | -46.99402 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4100686c-e0be-32dc-9d90-cb789d4dc729 | -13.69274 | -46.88108 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a883e00b-7074-3c8f-964f-746ada555f62 | -11.3794 | -43.63552 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5b45829-56fe-343b-af9d-cddbd4dca3a6 | -15.58429 | -48.32771 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d30871d0-ad0a-329e-af3b-690e975299a6 | -11.81167 | -46.41596 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| af4eacc3-8db7-367b-814a-bcd67a8c5707 | -12.59745 | -48.21979 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14e76e87-7bd5-331f-8d6e-d33804227c92 | -11.03337 | -47.04901 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df210751-4cbb-3ca3-a33c-bfaeee08fc39 | -11.26369 | -44.92863 | 2025-09-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c858a8d-c695-3c10-af7c-e7e4571a6b7a | -14.79233 | -46.73058 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 26b68be2-ad6f-361e-be3d-16b03c26add6 | -11.08954 | -52.0404 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8435eea3-bd88-3192-a7c8-2f585ee18989 | -13.2939 | -46.89294 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 565924df-b45d-3b61-acf7-4bbc8e3d70fa | -13.51766 | -46.9907 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2bf02dc-548b-3d39-b432-32543683e8ca | -8.76286 | -61.42836 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d729498d-3af8-32cf-b55e-5d72b221ef6b | -13.39531 | -47.06203 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e16b984-8926-3b62-91f2-1251d8684d03 | -15.71679 | -48.99949 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ac1f8473-9539-34ef-856a-e67008e1a03d | -11.02539 | -46.9861 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80eea6fb-e541-3b76-9bad-e66a153f1d7f | -13.70399 | -46.92768 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 139b7aa7-a10f-37b8-868e-36c1b8410ad8 | -12.8731 | -48.09619 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79b02e6e-6522-3989-9161-fa2d07a0b7bc | -15.69279 | -48.95456 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b1873e5-1c26-3ba7-8447-a33cc2a435fb | -12.85459 | -48.0712 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48f89cd8-d52b-33fc-8cb9-0d7b2d0c1361 | -13.33352 | -46.98849 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f72e0b17-9e58-3c66-a672-d03d48c3c467 | -14.78279 | -46.7091 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 341104e3-a83a-361b-95da-0b62c71ad5d7 | -10.27662 | -54.25733 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c24a6a7d-fbdf-3564-8de9-a16dcf7f04ed | -13.50122 | -46.98069 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df95627f-0f88-31b2-99d2-4ff8b860d85b | -15.22481 | -53.79229 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8780943-107f-3069-b0ec-14d7df842bc3 | -8.75499 | -61.43314 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 835547e7-bbd0-33df-856a-6a7db393a028 | -13.53048 | -46.9767 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b21a7e2-ab00-3f5a-8947-4b661699da5d | -14.7777 | -46.76901 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e55b5d90-c0d5-338b-b17f-1ac2a5bb2e6d | -8.7244 | -62.4235 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de2e60dc-78f0-374f-9bb1-53421994bfbd | -18.07194 | -45.94436 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4957ccb7-991e-3b46-bace-38387105429f | -10.8757 | -55.75792 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 11d2c2a2-2cf0-323b-8460-ac918c8bc9ec | -15.09688 | -48.1481 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 978ab8ad-fef6-34e5-a009-3b8780b885ff | -10.57382 | -52.27567 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c101c82c-8b12-3747-a91e-8d56784125a5 | -15.2974 | -52.78838 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05ce998e-4371-336a-a49d-5a4a7b117749 | -15.15139 | -52.34484 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f699f36-3740-38bf-a122-ec99c77f3669 | -15.70227 | -48.95984 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3470302b-b63c-3527-b6e7-25ddc7aaeefa | -12.87271 | -48.16659 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a618349-e13f-31b8-b244-61119c4f325d | -14.41899 | -51.66633 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 67b5c77c-db00-3257-814a-f5348189b906 | -14.80019 | -46.72688 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 048d5e09-3285-3208-899f-a77d90170cbc | -11.03109 | -47.06398 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a676712-d4d7-3678-b4c2-55f9bb1d7a04 | -11.20523 | -45.03842 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 523464c2-5238-30c1-994c-777a991a3a90 | -11.91965 | -46.68773 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7476c4e8-6e83-399f-bd1e-317615d31085 | -10.93372 | -48.24632 | 2025-09-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe95c463-cfd3-369f-b8b9-4e742d812822 | -11.04252 | -46.89602 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aad9f6d-2ec6-3062-ab39-d3087ade70a0 | -15.17282 | -48.01543 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2910de76-e75d-3a5a-9d1e-8bbd32c2b6d6 | -17.17169 | -46.08249 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd133d09-9ca2-32aa-9f62-2afdc9b7873f | -14.79477 | -46.73928 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dea7fec-81b0-3eee-b0f7-bc61b827c30c | -10.24065 | -51.10548 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 39f1e0c8-931c-3e5e-a843-e9b6547c6b60 | -11.05376 | -52.0557 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff6c9128-b803-38d5-b1a1-1d1a06e8eca1 | -12.40898 | -46.45511 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 361c75d1-8704-350c-87e5-5c0aa1e81c1b | -11.80814 | -46.41546 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 632a0206-1fcc-3e11-bc65-7cd9f03fedb2 | -11.87279 | -46.70562 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fb3dfe0-caac-38d7-9bad-0a2393f7654b | -11.68307 | -47.58681 | 2025-09-01 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f88c1313-a6db-34a9-a8a3-f1932f9799ed | -15.32964 | -46.05584 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74ff3645-6439-3187-ac9b-030a84edc99d | -15.7 | -48.90714 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61de1e2e-f03c-3864-b34f-c20e66790449 | -11.05169 | -46.90517 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1c27299-4a45-39c1-87cf-fc9fd87547ac | -13.47617 | -46.98044 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5218e028-f1f7-335f-aea4-17808a88ff41 | -15.17992 | -52.34552 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34989f97-6897-339c-972e-703d82ee9af9 | -13.31784 | -46.85229 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf6a25a9-adab-3c22-abc8-c8c101bd8d26 | -13.32894 | -46.85017 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b1db9c-87c8-3e01-a1df-554745fe22e1 | -13.33416 | -46.96018 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dadbae78-5f3d-3edf-b0df-749f7efe925b | -10.36481 | -52.29162 | 2025-09-01 04:34:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7ba53da-8ff1-37f0-b070-be32b23d68e3 | -15.71902 | -49.00729 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18553dad-432d-3a9f-bb8e-d147c234dc5a | -11.89343 | -46.69591 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2adee284-4b48-3f5e-912f-5083b690bc35 | -13.16194 | -45.2802 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 558cbdf1-ae80-391f-bf67-8824f43e32c5 | -14.76397 | -46.76268 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f77ea245-e2df-37e0-9e92-a70e794b62a0 | -11.01439 | -46.84892 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b0b0ad5-b09e-3e10-9b93-30c8a01f0d7f | -15.23063 | -53.80287 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c6f7c4c-84e1-30cb-9df8-68cc76d5cf8b | -13.48438 | -46.99774 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
