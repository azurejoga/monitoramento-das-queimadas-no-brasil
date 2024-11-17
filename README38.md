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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b6a49e1-3d97-3b70-8107-285d9d3e62d6 | -2.66929 | -46.86002 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a99bd7-48cd-3500-a298-58f25d2e3c7b | -3.52241 | -50.26049 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc8c0fc7-0987-38a0-a28b-87cd065d5f13 | -1.28452 | -52.47079 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8dc2c18-656b-3141-ad34-d280d708c494 | -2.67023 | -46.18155 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b214fa7-63b0-31fa-bacd-c7bd7f29e17f | -2.62128 | -46.2555 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6e856c5-be82-3d1d-9557-c04a4a860bb8 | -3.70945 | -51.84378 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5aed97ce-6528-3df8-b8cf-0405a010361c | -2.62631 | -46.02802 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d7d97c-0ef6-3e47-bccd-bd2cdcf07ccc | -2.20587 | -46.04513 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c67afc54-3428-33cd-9646-d924e8d595bc | -4.15791 | -50.02074 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02fa336b-57e5-3e13-951c-671e60a4194a | -4.00254 | -51.02845 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58a4cd16-0d10-359d-b49c-ec4c6035f26c | -2.61558 | -46.18349 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b166487-b69f-389b-931b-0f91d3ff7fd2 | -2.67585 | -46.2109 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2271c700-c7e7-3704-abcd-6786dd25435e | -3.79877 | -51.3753 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9973335d-23f1-3c82-9233-16dd41726c81 | -3.8196 | -50.23358 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d07f9bf-a3b2-3833-95d7-9ce089d94baf | -4.54621 | -46.41428 | 2024-11-17 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f165a4c-7fee-3221-bda7-ddd425ccd5c9 | -1.52316 | -47.4699 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8713b28b-f0a1-3333-84e5-27fc3324ad72 | -2.92207 | -48.95737 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fec823e-7996-3c30-b676-a875cdf7a9e0 | -2.90839 | -46.85133 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e5679ba-f192-350c-b420-e60fc094a8fe | -2.60235 | -47.56453 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d54d89c2-dc39-38fa-97b6-106cad741b96 | -2.97003 | -53.8659 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a7e031-217f-3586-811e-3ef00eb8a16c | -4.35862 | -45.86938 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6b0e34d-3859-3bf5-b5f2-acc8578939fb | -2.86421 | -46.72114 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 31fab614-a1c2-321a-8f82-c48a33d0dd2c | -2.64439 | -46.19506 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3d566aa-d3ce-381e-851f-be3a8ffd1286 | -2.80618 | -46.65928 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d78d5e1-e11d-38a0-aa6a-f844a3232b0a | -3.53657 | -50.25341 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbb7dc69-9eba-32d4-9ea3-e88447d13bac | -2.64153 | -46.14828 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e1284e1-5888-3690-90eb-0b8e37bfac04 | -4.84519 | -44.48733 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bfd705d-0085-39c7-926b-2926aba4056b | -2.20366 | -46.29695 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 751495e9-e05f-3811-bc37-57c7f6bb0bc8 | -2.55521 | -47.28176 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70745d9c-187d-3a1b-b22c-64810449bea3 | -4.28735 | -48.21301 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71ce78b8-3649-3696-809a-fbf5403d0162 | -4.14811 | -50.77755 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bca8be62-126d-3635-b3c1-9b34e63b38b0 | -3.62561 | -50.22556 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f663999d-06c2-34fb-a0ce-236ebae92d99 | -2.13611 | -48.89313 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9070625d-3ad4-3860-aaec-19f41e8312a4 | -2.60453 | -47.55072 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32a9c814-f5fd-3de4-b911-574115c503a0 | -2.27817 | -48.81661 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e0b5bad-1b51-334f-9417-702918eb21f4 | -2.16257 | -46.40719 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3659594-121d-349d-b7b3-dc1e019503e3 | -1.65093 | -47.88642 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4982fec4-7698-3a8d-9fa6-8742469fce82 | -4.45583 | -44.54798 | 2024-11-17 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abfa395a-f1a9-3f12-82bb-16c51e84d519 | -1.39557 | -51.08915 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbc9ba0c-2a35-3958-80de-7b59c89b537a | -4.00398 | -46.5806 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d95391-edd6-31f4-8f9f-e492218ccb54 | -0.77786 | -49.48091 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242e27c1-b4ee-38ae-a4d6-474cf2d69ae6 | -2.14609 | -48.27952 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ccc71a-555d-37ac-8b1f-8fc0eca4b202 | -4.22423 | -50.67633 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15201e4d-e1eb-39bc-9d73-aea810b37219 | -5.59131 | -45.21113 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a567e4ee-2544-3432-97b5-45d5f54c8d18 | -2.66426 | -46.2198 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c2973bc-75a4-3e72-9407-6df8d28b610b | -3.94209 | -46.41058 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 075fdf36-afe1-383f-a868-3dec3e003f07 | -2.22578 | -53.6087 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91342541-ef01-395a-bcd8-c38074896aa6 | -3.85373 | -46.64993 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a357abb1-d32d-395e-a5df-dec7a62581a7 | -3.74565 | -54.72489 | 2024-11-17 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53073860-9a36-31b8-b223-f5662d594a4d | -3.51575 | -49.93583 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a8bd043-13c8-361e-9c7f-f5df59264a6f | -2.53879 | -48.24966 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a309abd5-db05-3d0c-b37a-850133bae7f0 | -4.12634 | -45.89972 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73cd112c-883d-386a-a11c-ecf5a3f77ee4 | -4.47666 | -48.1111 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3119196-c632-356b-b8a9-8ce175cae4e2 | -4.13754 | -46.94193 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d898eb12-d8c2-3dc4-81e3-d334cdf2037d | -5.50835 | -46.42929 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a57c67a-09f5-3ce0-8c78-8b4dff03f4f9 | -5.18082 | -37.99672 | 2024-11-17 04:29:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41953d28-dda8-3215-a8a9-815f01e10a4b | -4.09935 | -46.88294 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1978b6e-9ed9-371c-af9c-aa0b6ea2392f | -2.31354 | -48.46365 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd3c1b3d-656e-3a27-a02b-da29b5fd8dbe | -2.41114 | -54.62893 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd7f94f4-da0c-3ef0-9317-b6ed0646974c | -3.35457 | -46.06176 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c97f0be-65fe-328d-a310-179bb4e5d134 | -3.51653 | -50.25113 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7b2177c-a4ca-305b-a77c-74bd74732fce | -2.65592 | -46.20783 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7d601f1-1d7d-3a34-b31e-1aa4bac489b3 | -2.37408 | -48.9185 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b2f3f11-4715-3249-b784-8414b424a830 | -1.28284 | -51.958 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33eef111-7549-3fbf-98b4-2e3f74f01c22 | -1.51984 | -47.46938 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 276ab7e1-aba7-3e33-9217-63acc7c8c4fe | -2.31296 | -48.46725 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454dc3fe-1517-3e5b-9948-0105dc19b561 | -2.10033 | -48.39353 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93503079-a6d2-30a6-8faf-0a9f569f8cc9 | -3.24325 | -53.52406 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b35d533e-01c1-3630-b1ef-02ddc5b29c2e | -3.55434 | -46.39324 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66de5d3b-bdba-3686-89d7-884f6c83b329 | -3.35456 | -46.64944 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf1c4267-e633-3c13-bd8b-cee288b27f20 | -4.24996 | -48.53147 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9b66edb8-3818-306d-bcde-49c211558260 | -1.37932 | -51.09157 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63cddb31-fbc8-3c27-882b-8af113a0fa36 | -4.24604 | -48.53448 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 225e2e39-c732-3c5a-a767-5c4824066813 | -2.10836 | -48.89311 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ff000aa-b6cb-342c-9283-176e9fcda6e9 | -3.19881 | -46.53703 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc8998aa-df2a-3748-a885-738437366111 | -2.63059 | -48.564 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a2407fc-156c-3fde-a432-ab98e1c9c318 | -2.67748 | -46.20047 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 952003ce-435a-35a8-8423-7583048ba4dc | -4.56332 | -45.10423 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf0d4f1a-356a-3cba-bec2-c6b7b6481971 | -2.21056 | -48.51402 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d18411b7-0b68-39f2-9667-f24b749c26b6 | -5.41509 | -47.56919 | 2024-11-17 04:29:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53e9e9b7-f8cd-39f1-ab55-e84291c889f5 | -3.09454 | -45.96708 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04fd123f-1ee9-34d3-8c10-e3746487d11d | -3.83741 | -51.30587 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fb85d7e-7d31-3c42-8a24-e09aa2922bfd | -0.78537 | -49.50278 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51b94e6a-a74e-3750-ae77-65147b158da0 | -1.79738 | -48.44292 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fdad8c4-572a-39eb-94f1-ea1ff4e5a34a | -3.3551 | -46.646 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6303311e-4411-31d3-b666-063c1142cef5 | -5.7077 | -41.65083 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03d7ee20-e26f-3a76-a3f6-362ddb5e65ab | -2.8161 | -46.66082 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bdd6351a-484d-31d9-85e3-43d98cf8f8df | -4.47389 | -48.10712 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 794f0ad4-5a04-3dce-baf3-a7c8462e194c | -1.14184 | -51.69299 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 702ad8e9-5839-30d9-8de9-f54ef58fa67f | -2.18866 | -48.35954 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10c88524-507e-3917-8efb-f161cd96ced9 | -3.76662 | -54.56804 | 2024-11-17 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f675f5b1-068f-3b60-8fb2-d426a2c0ab32 | -2.65762 | -46.21877 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36c8e2a3-935c-30c2-8b9e-27c9cac9bd91 | -3.19266 | -46.51129 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a8e9d9-29b6-342d-acb6-80812b3aabf0 | -1.75651 | -47.52021 | 2024-11-17 04:29:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd03bf76-1df9-3e32-9269-8b25c23aae0c | -3.86723 | -51.17002 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aca855b0-4fc4-3949-9134-364f9b4804ad | -6.38307 | -45.68715 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac8088b2-9098-3b28-badd-d1cc05b2a30f | -3.89578 | -46.62072 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2007e441-176a-387a-875c-6a2be4d4050f | -3.63853 | -50.14412 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab19abb-b256-3861-ba76-561efe94844f | -2.6261 | -46.18155 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b603f82-b036-339d-8e39-f9416ab15c3f | -2.17964 | -48.39491 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README39.md)
