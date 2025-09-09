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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 268ae20e-ec64-3dca-bab2-12d6197b90f5 | -12.95721 | -54.75924 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94b07bf7-ad30-3b2a-93da-ccef248ef476 | -12.9472 | -54.76306 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39285db7-2b9e-3914-856e-1cc90c5b14e6 | -12.88007 | -62.09481 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef1269c-9a86-3ec0-b0f3-5bd579775f87 | -12.41601 | -63.89124 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36fce39b-93a0-326f-9ade-97caad23fbd1 | -13.6398 | -55.02697 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 617b17a8-04de-364a-a4b4-c2253fc73fd7 | -15.25553 | -53.81303 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbee8e84-fc0b-3821-baef-b736af0e0c0d | -15.78784 | -53.53638 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e61c74cf-d371-3f2d-aff7-0cefab7b14c6 | -15.81945 | -52.25863 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25e118b1-146e-33e6-b379-095e43870f2e | -10.28378 | -48.81889 | 2025-09-09 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27d2f398-77bd-39c4-a183-34e3a003c349 | -11.89279 | -64.99516 | 2025-09-09 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ce12e4b-489e-368f-87c6-6d4ed8b4a66a | -14.71835 | -60.2457 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b423675-ab3a-3727-a291-213faa4cefea | -15.77148 | -53.54282 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac63478c-b1b6-3b0c-996f-3a6856138735 | -13.13193 | -54.91837 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ca839e1-f77d-3f4b-9b93-2ab4d03fa700 | -7.5012 | -63.50633 | 2025-09-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1d9641-7757-3440-828b-7a44259d896f | -8.41545 | -62.28698 | 2025-09-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f99688e-2bdd-3eb6-b28b-f375045ce883 | -12.87673 | -62.11598 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b632973d-5d0d-3cfc-82b8-a1fdee900e2e | -15.27246 | -53.80222 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2ad9937-47ca-31f9-a34f-640384d42393 | -15.81812 | -52.25978 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d61a5c-4d3a-3721-ac6d-720635f8a6fb | -12.96592 | -54.76532 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07059ae4-08de-34d3-9d76-31d190f38dd2 | -3.59359 | -58.53842 | 2025-09-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dae74f9d-f323-30cd-b760-12f98863e93d | -13.00912 | -54.81858 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf254277-c784-35dd-bfc5-4c8e7f2a56a0 | -12.8884 | -47.987 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05d01d2d-8297-3abb-8388-47b60d46d285 | -14.70222 | -60.25917 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d93a7e2-513e-3e32-a542-c9290bfbefc1 | -9.23826 | -57.06795 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1dba28dc-5dc2-3e53-94a5-7bb12c246ebd | -12.86955 | -62.11842 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb2b4f0d-6c30-3f30-b030-1fe90c340714 | -12.87509 | -62.10485 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1c0521d-2466-3a9c-81c9-f14d9fb8a4f7 | -15.2522 | -53.79672 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c4c4895-7d51-3c2a-b27e-a5d656d3d9cb | -11.7922 | -62.74137 | 2025-09-09 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e1ca4f7c-1724-315f-8016-7458d81784ae | -15.83 | -52.25759 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60f98dcb-cf3f-360d-9f45-2847814cab57 | -13.03234 | -48.02934 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 96baa126-55fd-35d3-94db-87b8839432d7 | -12.19981 | -53.88399 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3cf78c85-2709-305c-bacd-1ee43f1674b3 | -15.53836 | -48.40203 | 2025-09-09 05:23:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fff3cc3-44ac-34b6-80b0-2c800f39f072 | -12.42006 | -63.88803 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2703f334-4fdc-38a9-a28d-1e7528a69dc2 | -12.94853 | -54.75293 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bc6f129-41fc-3498-b70f-a159a95e3253 | -15.24747 | -48.81489 | 2025-09-09 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07169884-2b33-36f2-b9ee-27d926ea3a54 | -16.42937 | -49.29668 | 2025-09-09 05:23:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d092337f-015f-3aa2-92c8-8cd3f464ba64 | -12.8867 | -62.09589 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5847a5af-db0c-3447-bc11-94944da457e8 | -11.79553 | -62.74193 | 2025-09-09 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 357d9ccb-52d5-39c9-a479-066218660212 | -12.63433 | -56.97915 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f3851d5-c628-3fc0-80cb-6b967db5b95b | -7.48949 | -54.95498 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4732a42-51fa-39f4-81d1-2bdbee0300ce | -12.18926 | -53.88835 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6678fa0-2ddc-3360-a35d-0b675476dd01 | -12.95002 | -54.8137 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 561ae5ac-741e-3d75-8ffb-d30cbd29e741 | -8.07073 | -50.19551 | 2025-09-09 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1af9c89f-0842-3cff-9a4d-ceeb5c5f3459 | -12.20327 | -53.89574 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| cec8cd53-b4d5-3218-9613-6e3b2ae8833d | -7.87611 | -61.32933 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88384b20-2a18-3550-b3ec-a1b2f7379c6a | -15.78277 | -53.53783 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4166f008-7e2f-3945-9729-0af58bce7169 | -12.42628 | -63.89299 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cdda828-2412-3dbf-b87f-e809d2235227 | -12.92788 | -54.76542 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc0db7c6-22fa-3456-8239-44b723ba8e52 | -15.78859 | -53.52966 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc12d7a3-4d8e-3af9-bb87-0dfe3c3a8625 | -15.25074 | -53.80932 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16b3fc1d-c022-3cf0-b8f9-b2fb7af111ac | -12.96058 | -54.76973 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8221d897-d60f-39ed-a31e-a4dec1995ed3 | -15.81855 | -52.256 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d37be461-5d1f-3aa2-9598-5fdff8cd4581 | -12.82786 | -52.93708 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0183642-ef4e-39db-a02b-77c0b7526d4d | -12.42223 | -63.89619 | 2025-09-09 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91eb6b51-c5cc-3658-80f4-7a830406cf51 | -12.84329 | -52.94249 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37f29b8b-f8da-3cbf-8911-d46505bc583c | -7.87943 | -61.32986 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9064184f-f133-3a61-8fb9-3fae31ee6c5d | -14.53128 | -48.73928 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9820a624-9365-3a69-ae8c-ec3771a1a423 | -15.26287 | -53.79484 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c8be1a5-770d-3807-a351-69246b9d6acc | -7.39273 | -61.63513 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e4f941d-e49f-3b10-b83c-d0378b9b4b41 | -15.27283 | -53.79912 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1970a23-dc58-3bef-afae-d91670a4aa2f | -7.90592 | -61.78215 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8723b1d-8b18-3d5c-8f34-36f4fff238bf | -15.78476 | -53.52095 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9da4e9fe-477b-30bd-a28f-3fa20f34489d | -12.63181 | -56.96784 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f505e61-6ad4-3102-b12b-7580809a54a0 | -14.87292 | -55.80317 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3c19d98-5898-35c4-a29a-65e7ec336343 | -7.39662 | -61.63214 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 186f4a75-9c49-359d-86c6-dc59c809edfe | -10.29047 | -48.81933 | 2025-09-09 05:23:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de8251b5-88f8-3326-adeb-546d70472958 | -14.73345 | -55.9104 | 2025-09-09 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e3124509-1434-3eb9-ba8d-b0514453ea5e | -15.81697 | -52.27011 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c73d7020-3778-3a33-870d-6417311c1a32 | -8.04867 | -48.64036 | 2025-09-09 05:23:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 930f41a5-e3c3-3dea-83e9-1166b500eda8 | -12.82745 | -52.94043 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59cd4e28-a3b9-36be-bfbf-da604d64b248 | -8.08192 | -54.7623 | 2025-09-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe6e8274-8f28-35eb-b5fc-c5616ecec8ab | -12.90191 | -47.99696 | 2025-09-09 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fda8b54d-782b-38dd-8aea-88e99c9b97d6 | -14.54248 | -48.76722 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6f35295-9203-3a5c-8bd5-8c5271dc2583 | -15.10832 | -52.34868 | 2025-09-09 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b35a31bd-4158-3e4b-a795-b54f585874bc | -12.96124 | -54.76477 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a9fb679-aa6c-335d-a7cc-d835019650f7 | -15.26179 | -53.80418 | 2025-09-09 05:23:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a62145c-0513-37fe-921a-b1fe171dda26 | -12.92723 | -54.77037 | 2025-09-09 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efc9c715-472f-3649-b569-844069cb05da | -14.73287 | -55.91483 | 2025-09-09 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 52a49eb4-32c1-3c3e-8b08-a5afe8b94543 | -6.87591 | -47.91025 | 2025-09-09 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf384890-71f5-3084-aea1-0474f37f268a | -15.73434 | -53.58652 | 2025-09-09 05:23:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edacf69f-77ef-3c27-bc2d-424e7bcd8d5a | -15.70711 | -49.90148 | 2025-09-09 05:23:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed3b7298-061e-31cd-a4a8-6484649879be | -5.50076 | -60.13197 | 2025-09-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee1f3276-62a7-3f0a-999d-8f03001bef4b | -12.88063 | -62.09128 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1595b326-3864-335e-a120-213ca39d6e30 | -12.63131 | -56.97143 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c16cf8-cff4-33fc-b976-ce92ea8fd44b | -10.00642 | -51.67857 | 2025-09-09 05:23:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e576086-d402-3c84-8f00-1265ef89afc6 | -14.5297 | -48.7388 | 2025-09-09 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff62c0fe-23a1-3639-bab0-b6074f821de2 | -12.83273 | -52.94112 | 2025-09-09 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 895815db-0adf-38a0-a47b-b7fa9553ecb9 | -7.39718 | -61.62862 | 2025-09-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37726c88-20be-3061-9a04-091eeb5085fc | -15.50373 | -52.76294 | 2025-09-09 05:23:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 277520a2-cc67-314d-818e-82bd71e168b0 | -4.97617 | -48.94729 | 2025-09-09 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cb512d4-43a6-3471-a500-fb6ed04ebac1 | -8.23092 | -49.54557 | 2025-09-09 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74249b0d-a6e5-3f71-b89c-d9ebba7bf858 | -12.62582 | -56.98157 | 2025-09-09 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f321c7-ff5d-3e08-b9d8-f19924ae74c4 | -14.70338 | -60.25124 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abf80979-da1e-366a-b1c9-7e0682168882 | -9.2752 | -56.89338 | 2025-09-09 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 350c633d-a80b-3786-bb98-072b0fb0d576 | -14.87526 | -55.80643 | 2025-09-09 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1521a5c7-7ae0-30c6-88fa-a4f836ba221d | -12.87729 | -62.11245 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fe50a7c-3b15-3aa2-865e-92c61971fd04 | -6.39765 | -58.20592 | 2025-09-09 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e9efde6-0b71-3b44-9a94-c6f6ea15fb9d | -8.39977 | -49.10104 | 2025-09-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87bd0218-e8bf-3338-9426-93fd2359d65a | -12.87178 | -62.10431 | 2025-09-09 05:23:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 145d53d6-c7a0-3205-831d-ce528dc4c79c | -14.7051 | -60.26371 | 2025-09-09 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README59.md)
