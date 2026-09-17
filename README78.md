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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba8cfa49-9746-3177-a026-2bd325fb4a9c | -6.90299 | -59.02659 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87ae3be4-b7a9-3739-ba01-1eacc3273b61 | -6.71324 | -58.80327 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6a62f13-f1ae-36dd-aae6-0f1de9ea7920 | -6.317 | -59.97021 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db4eabff-ced0-30db-91de-48a490414353 | -6.4364 | -60.01476 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc49475-babf-3772-8fee-4ba2ec90b1df | -6.80132 | -58.78828 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd12fa75-4a5a-322b-b52d-7c27f7f47c70 | -6.0294 | -59.93151 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52eb12b8-e3ee-3cb5-af18-e6f288500827 | -6.70793 | -58.80545 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd95b9a3-22e3-3ad1-bcfc-048bc5f04d61 | -8.88311 | -62.38654 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b09c7d1-1ad2-3da7-9bf7-01d345fb8e82 | -8.49635 | -57.64435 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21ccdb2d-19cd-31bf-9c5c-6ec03dbf5fd7 | -9.08823 | -61.00846 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f50b1933-f986-36b7-b341-2787be262994 | -8.22246 | -55.46681 | 2026-09-17 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60debf7c-21b5-39d8-93d5-35e36233f22c | -6.10341 | -57.62963 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa755f80-09a4-3714-9f3d-38834b5e939c | -9.17099 | -58.30333 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c7ceb7d-4a17-3c5f-bc24-6a190b0e365f | -5.83888 | -52.09507 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e779fad6-38db-3125-9152-ae6b1553aa25 | -8.48719 | -57.65021 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 756c42c5-9109-3eea-8d2b-1f4c452e54e0 | -6.36913 | -55.82534 | 2026-09-17 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66cd96d4-4776-3a9a-969a-14cac1a91414 | -6.31397 | -62.67461 | 2026-09-17 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0427d6ea-83f5-32d4-abbc-58a6a371f390 | -9.10588 | -60.9613 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ffb0f22-e306-3122-ac05-9a4572b99a50 | -4.50422 | -54.97424 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcb52c38-b646-3ad0-b398-4883eadfcd5d | -4.41654 | -55.50689 | 2026-09-17 05:36:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0f65432-0d69-327e-b76c-db86ace993ed | -8.92183 | -62.39986 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88afe104-73d6-3630-9321-0eca2c5c8269 | -6.42656 | -60.00924 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c469f6d2-94a3-3f56-9b78-3288e16841a2 | -9.09791 | -60.99081 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2bc6c61-8539-3965-9271-df6033e397b6 | -9.09848 | -60.98706 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2f0ffb-3d75-329c-b473-fe491ba734b6 | -6.83057 | -58.98634 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a4d3925-a2c0-3458-8732-d9dd559ad6ca | -4.87768 | -56.06635 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ffc6153-f2da-3091-a64a-6bba17cf91c3 | -8.49281 | -57.64025 | 2026-09-17 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eba70c21-2d67-3b04-a583-e090863e5e03 | -8.15575 | -64.05663 | 2026-09-17 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67755870-6364-3d2c-ad85-a349c0c8f343 | -6.33202 | -60.01183 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bb57484-1db0-35d2-ba9d-2e29a607d098 | -6.81452 | -59.16701 | 2026-09-17 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49abca08-a585-3af0-981f-000b65bfa00e | -9.59042 | -60.52216 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a520e1-f5fb-36fb-bc94-d26e5d2cb4c5 | -3.70286 | -60.6061 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17d118b7-ae82-3113-bb34-adef1e6d654e | -9.10075 | -60.97204 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39ed7ca7-a039-3e42-aa93-3f7c2f673615 | -3.70007 | -60.60205 | 2026-09-17 05:36:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99c59261-5a0a-3734-b248-5f20c8dcbc16 | -5.14783 | -55.93788 | 2026-09-17 05:36:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edad4085-208c-3166-a341-e64e8645939e | -9.88993 | -57.79386 | 2026-09-17 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf048dcf-9e22-3f70-bb4e-03ea06c1dfb6 | -5.86018 | -52.0685 | 2026-09-17 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80330b0f-c0e4-3994-b786-e87737b1a750 | -9.09732 | -60.97151 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3983e225-5090-3237-87a6-eadfa3c2be2d | -5.92502 | -59.95158 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c4ae41-5625-3770-ba92-9ca324251b5d | -8.87925 | -62.38951 | 2026-09-17 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42df5d73-decc-32ec-bd63-06e429d8265f | -9.39313 | -60.29948 | 2026-09-17 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5cc1401-74ee-3706-a1b4-c7b9d9c1bb11 | -6.75899 | -56.32704 | 2026-09-17 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f5f81c-57d0-360c-9f8d-e2f08ff1441e | -6.12347 | -59.88663 | 2026-09-17 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda0ff7f-1c2a-3a17-a9c2-bb34800a7a07 | -9.18006 | -59.63307 | 2026-09-17 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d4daff0-71e2-37e6-94d2-7f9e980a1a40 | -6.70955 | -58.80271 | 2026-09-17 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e084e85f-49bc-3485-ad6e-a0bfb0c28e36 | -7.80027 | -66.91876 | 2026-09-17 05:36:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d33c20-d870-37d9-b4a6-773c5e3890b4 | -11.80715 | -58.17138 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| fc431bae-4738-3522-ab03-00c87c2c4b45 | -12.11371 | -57.1985 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f42eee22-c0ff-3c94-92cb-d9ceb6e2c890 | -12.11043 | -57.1916 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d04acc68-2a00-373b-8f42-3e232f0ef17e | -12.66091 | -50.76215 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93bf5a8c-42b9-3a19-b04f-fba767b50844 | -18.03003 | -50.9555 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8f326856-5b5f-3cbc-8102-e24888efdae8 | -9.05895 | -65.92722 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2d3ca5f-e314-3fb8-8ee1-15ddfb36e03f | -9.05774 | -65.92606 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 151fbffc-afb5-330d-adf9-fec03ed0d413 | -18.02532 | -50.95976 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 76d536ad-a6a2-31d8-91fc-36f6eedbe71f | -11.67894 | -62.10606 | 2026-09-17 05:38:00 | NOAA-20 | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6260355d-b2f3-3ed9-aed7-b05c874853e4 | -11.98514 | -52.4625 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8b3c967-9432-3711-a23a-736495de4c0a | -10.27883 | -60.53539 | 2026-09-17 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff12bdd0-2a8d-3358-9abf-890987e9b65c | -9.10709 | -65.93859 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9caea936-a6f9-3dd3-a98d-85a091fe393b | -11.81023 | -58.1795 | 2026-09-17 05:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7e9b8d41-856c-3690-ab16-3ead13926d4d | -10.65795 | -61.75425 | 2026-09-17 05:38:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9261a07-818f-3bfb-8ca9-f1369439a6bf | -10.59692 | -59.42094 | 2026-09-17 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2793c0-60b5-3984-8e7d-11ea8c4e7e03 | -9.34375 | -65.93368 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 954f3f40-f398-3f84-b03f-c5f00f8c33a1 | -10.29549 | -68.855 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33225531-3d7d-3b3b-993f-879442f18793 | -18.03241 | -50.96025 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a1b7f50b-d47e-38da-8fee-0f44ab3d509a | -15.29791 | -59.25952 | 2026-09-17 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90fedc3d-c197-3a73-9159-b7c3a1096a70 | -16.30779 | -53.85422 | 2026-09-17 05:38:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b85100ae-e324-3f71-abf6-84cf639c0eea | -10.38993 | -58.30913 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3ceb560-0b9a-313f-8cf8-f83b94c24672 | -10.39091 | -58.30219 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a4f1c34-1a3d-367b-8322-aa2b435d3e34 | -13.38166 | -57.02154 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a02d78dd-e654-3d25-a660-d6ab76e27939 | -13.38041 | -57.0311 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc002c82-1d7b-3edf-a05d-f022db35ef16 | -12.10603 | -57.19093 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60099810-532f-3a0e-9552-a8600e492486 | -10.52369 | -57.44708 | 2026-09-17 05:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53dfa9b4-b1e8-3006-8873-2c3660dbc8ed | -12.11365 | -57.20086 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ef38aca-3503-330c-bb9f-05c2b257bef8 | -10.29818 | -68.8567 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da882c1-9b9b-3c40-9214-22a10e3ad27f | -10.87699 | -61.39614 | 2026-09-17 05:38:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3330b3ce-fd3c-3ae0-9f36-661ee2e13f70 | -12.65415 | -50.76136 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| afc4e760-c34e-3462-8bfb-be5313038e38 | -9.18419 | -66.01739 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f28f3d81-c42b-3fab-8075-354568e415ef | -10.65851 | -61.75057 | 2026-09-17 05:38:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12231a6e-3a96-3c71-83d4-75b414f4eff0 | -9.92086 | -60.46471 | 2026-09-17 05:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a66919d-e523-3b5e-97e6-be520e5f2ea5 | -12.10924 | -57.20023 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80eb8083-96a5-3c83-8b55-b6c3b54b11d4 | -8.87523 | -66.67229 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4220c809-ffe3-3d83-a650-49db5c909650 | -12.66744 | -50.78934 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e9b2a21-7c27-3db8-b21d-c5777369dd5a | -9.05739 | -65.91431 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e70b60-00c5-3314-8433-412ba5a252be | -11.19143 | -55.03645 | 2026-09-17 05:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5f16f4-59be-3165-a64f-2b6441062dec | -12.11315 | -57.20278 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64cdddba-843f-3931-9425-c352b3f30f31 | -9.1064 | -65.94271 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e13761c-39aa-3960-9892-a4196aaa5201 | -10.9892 | -59.13572 | 2026-09-17 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7ccdd4-8729-3e58-b1a6-994a024569d9 | -15.45872 | -52.89421 | 2026-09-17 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b29efa9-b141-3969-b89e-92f1ab30559b | -9.16424 | -66.0482 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1204eefe-f890-3c88-ada2-a5d10b2fe566 | -18.03063 | -50.94836 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| d0214167-9348-34b0-8fd8-c2c1c565b2e0 | -10.39891 | -58.30339 | 2026-09-17 05:38:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c25bd032-352b-3f37-9b01-ee639ae7daa8 | -13.38103 | -57.02633 | 2026-09-17 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ef4fe40-5a42-3959-9bde-4a95f131cf41 | -10.29897 | -68.85954 | 2026-09-17 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d06287c-c35b-3aac-bed7-279928e7089a | -11.98458 | -52.46704 | 2026-09-17 05:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5651c79-6754-32a4-b48a-8b79a83c3a77 | -9.348 | -65.9301 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442cd87b-7675-3fbd-8ec1-37700f6acfb2 | -9.10489 | -65.92976 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c20f20e1-a973-3828-af6b-b09796503611 | -18.02666 | -50.94488 | 2026-09-17 05:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 80dd44b1-fb52-3e7d-b600-e8febf32f014 | -9.06029 | -65.91901 | 2026-09-17 05:38:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cbd108f-465f-309a-8c36-ae9d72b4ee5b | -9.74531 | -62.36457 | 2026-09-17 05:38:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63cb6396-6030-3aaf-b062-fc779a76e99e | -12.40364 | -50.75455 | 2026-09-17 05:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README79.md)
