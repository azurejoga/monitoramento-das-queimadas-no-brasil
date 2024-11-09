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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79aba050-8406-361b-a20b-3cbd5a646a10 | -2.12547 | -51.24494 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb05dff6-a8b7-3283-bdea-21b2d9fdf9ee | -2.72913 | -51.71402 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e1fab26-d67c-3bbf-a785-e968e7d605ed | -1.47911 | -52.08605 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a88ac9d8-37a3-3c34-9bf7-6a174ad0e69b | -4.38393 | -48.5794 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 861a5c7d-8f24-340a-a99f-9188f1bc9a40 | -3.74762 | -52.41466 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d036f7e-e0d3-36a1-a13b-a18d3daedaab | -5.19892 | -47.46479 | 2024-11-09 04:55:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f882661-65c1-3688-8fda-b1d4ebd3a421 | -2.58159 | -49.13733 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f2de88e3-9119-3162-bc9e-d8fbecbbe4b5 | -3.01907 | -51.39749 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8f3c9c-cb9c-354e-8c14-ad3e513b8d18 | -3.53321 | -50.32954 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| db5efb5f-722b-3237-8a20-536bb8b67bdd | 0.50069 | -50.69 | 2024-11-09 04:55:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b155d77-f2f1-3450-9eb6-219dba194b9b | -3.4031 | -50.01472 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8952cf5-2e7a-3ef9-9956-f63e0c6e20c1 | -2.60189 | -54.19175 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1144619-79d0-3f20-a8db-b98c5b48fe19 | -5.6615 | -49.99898 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b46607f-afd8-32b7-9e72-a0d42a99720c | -1.37995 | -52.26001 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b6e5ed0-230e-3450-94d7-f551e7a690f5 | -3.89741 | -51.92441 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9092cdc-704b-36c6-8cc6-6726da7a9dfc | -2.09393 | -48.89723 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ff32946-3c77-3fe3-834c-007fa94d9c33 | -1.8364 | -52.26321 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c80705e-2d5b-3951-af71-a4e8ab079878 | -3.10262 | -53.98025 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95f61c7d-2ba8-396e-b594-7e95dbd2961b | -3.25836 | -51.01191 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fffd6ee4-d66d-378d-bcc5-a182c278fd09 | -3.96687 | -48.1839 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 27f5905e-526d-39bc-aec1-d7ce2b887c20 | -1.59857 | -52.4856 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 415fcfb6-1da1-34f8-ab7e-5040a778a0b0 | -2.9758 | -47.92449 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87ebbac7-2bf3-3aca-9ac0-9c4296332ead | -2.4066 | -50.3044 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f4f06ab-591d-3f9a-82de-010274d1b748 | -3.83762 | -50.04776 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1a2a0f2-0d2e-3e5b-9f87-3eb200ab012d | -4.05338 | -48.24165 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d442fa5-67f7-3544-987d-249a62e60384 | -0.91551 | -51.66044 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5541aafc-8b2f-334b-8d1e-50266f377dbe | -1.21865 | -51.77541 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6fddcc4-90dd-3898-94f4-e41c10df8317 | -2.67712 | -51.82409 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9cdd0bab-2cc3-3971-bf3e-0fef63b6a267 | -4.74919 | -48.42988 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6772a746-a55e-3459-8cc8-e699285c1b2d | -2.46077 | -50.39396 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8030be-b6cb-369f-a734-662c771bc29a | -1.14761 | -53.64936 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6709f0e-8b06-3e0a-8827-427063710449 | -3.11548 | -50.1391 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd58ed7d-e435-36c5-9183-805eef307856 | -3.55145 | -54.74953 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e2ae5cf-2067-386b-8844-d7577cb65ab3 | -1.54143 | -52.00949 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 223c489c-6bb9-3196-8ec1-d2388e75b8b2 | -3.66902 | -50.22008 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abd762ac-50c4-317d-ae0b-802d9364b4e9 | -2.61754 | -46.16313 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c919600-148f-398b-8708-86637fb4b29d | -2.07744 | -52.04152 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ee0abe3-b693-316b-82ed-8837ef305016 | -3.46919 | -50.81582 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d6d626-5ab3-34f1-aab7-2564ab5d5b07 | -2.97288 | -51.45194 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 461266f9-1b43-3e20-812b-d8b05520793d | -3.0678 | -47.57771 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7036a01-a2f6-3a33-b2ca-ebe9e5b4f75d | -2.79906 | -51.48903 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edcd2bea-16fc-30a8-a4f3-128516b0997d | -2.08025 | -52.04556 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79391d82-f16b-3c00-a31c-1b547b7c7912 | -3.77266 | -52.05352 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c6928f6-4588-3245-8f20-af384ffb6d0a | -3.01902 | -53.8679 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bebff887-be89-39ad-be25-92fce9fe8510 | -3.09166 | -53.32039 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f00e96e-b591-3723-8635-61c7617d7fbc | -3.66603 | -54.65807 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f4663ac-eb7e-36f6-97ad-ae53ecb9125e | -2.46155 | -53.68769 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c630436b-090d-3a47-90cc-b29398e7719a | -1.94016 | -51.40104 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd548779-5a33-3fca-b708-80ad8cda0b4e | -3.81768 | -49.85727 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8ab071e-975b-3f8b-993d-791211fca17b | -4.22645 | -48.60894 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcdedd4d-e285-3e78-adbb-64b5b274bd28 | -2.22186 | -50.63077 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e12242d-de42-3539-9ada-68723865057d | -1.50511 | -47.17628 | 2024-11-09 04:55:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58b504d-40a8-3944-a150-633937b61daa | -3.96385 | -48.17577 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 23623c74-2427-31d1-9ff4-27893620c36d | -3.17656 | -53.85335 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 99923282-7d90-39e4-87e1-484dd038a485 | -3.12083 | -50.15276 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25ab0455-ad6b-341d-b2fc-cea7ae2b02e8 | -1.63462 | -46.11111 | 2024-11-09 04:55:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a686a4-3686-3e40-8488-55e128175350 | -2.28303 | -48.73125 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31f21d7c-ccaa-3db9-a3ce-d2054c7152d6 | -4.06789 | -48.28548 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04bd907f-99d7-32f1-a7ee-6d49cf6c88dc | -2.21416 | -50.44837 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc9ae599-fa58-3e76-b3d6-f90dc1b284fa | -2.68211 | -50.96236 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3a770ae-ce0e-3f8b-b897-3e7d715bfda3 | -3.29337 | -46.41273 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 610be850-c27c-392a-ae4b-85eae351e30e | -4.49713 | -48.49028 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe8efa32-83a4-3b5d-8684-56dbbb928c62 | -3.09556 | -51.29097 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d56ed6a-dd78-3f76-b815-feabdc075c10 | -4.10968 | -48.5014 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7c9d96d-e244-3a56-8266-9608c8428eb2 | -3.39966 | -51.5983 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc765d73-bcb7-340b-8cf6-3721abea35bb | -1.49566 | -51.99519 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fda9d82-980d-38f8-9491-8329531d16de | -0.80818 | -52.49754 | 2024-11-09 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 162207c8-9935-3fe2-ba0a-d83c62b10d80 | -2.75396 | -53.22839 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0fa0c7c-db12-3246-a321-234859f0f1c3 | 0.81138 | -52.01487 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d30ba2d-f0c6-3e4e-8035-445215d5007d | -2.28543 | -53.82037 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d576da0b-895f-3d16-abb3-9ab464098bd7 | -3.0747 | -53.87636 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1a411e-5216-3b67-bef6-f6ca047369e9 | -2.9196 | -51.68016 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6bba997d-8f09-3993-819a-de9f57f6387f | -2.83761 | -48.47175 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df07ed6c-b58d-3d1f-b500-d7a29652b314 | -3.27405 | -52.73941 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171327fa-030d-3917-bfac-c245530c73f7 | -2.29778 | -46.74417 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f1da3bd-aad5-318f-96dd-acad889ec014 | -4.21185 | -48.6787 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db601905-118c-3b3e-89cc-25f564e913a0 | -2.69803 | -51.69066 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 387c40b9-f43c-3a19-8fe9-8e804f4a1644 | -1.19609 | -53.49348 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc8131a1-50d0-38a9-b6fa-4aad91496686 | -1.26984 | -52.1856 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b619f57-1040-3480-b67c-2785a00b03d9 | -3.0983 | -53.32143 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 707e551f-17ed-3f6b-a1ec-79f0c3ae14fb | -3.03392 | -50.30137 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a4ec5417-8329-354f-88a6-3b16bf924212 | -2.35957 | -54.75292 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b1ab4b9a-ab38-34f5-aa36-7e39b189320b | -3.3618 | -53.38674 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74b3aff8-d6dc-35ad-81c5-5e30a8f4f61c | -3.74257 | -50.17784 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14a82b59-8060-3d3e-952a-d0a4ddb73264 | -2.43604 | -51.58046 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 823a2776-2e41-3d48-b9a0-5687978bc264 | -2.86387 | -50.32295 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd23330-8674-3562-9f15-b43e4b2ae094 | -4.24568 | -48.53624 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 463d7387-c114-36e5-8846-a3164ff9d3c1 | -1.33932 | -52.19995 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb06f41d-e9b8-35f6-a27d-17cf068d297b | -2.82517 | -49.43851 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d9c7e0c-5f97-311c-a9f8-5de5f0f8667c | -3.11702 | -54.25068 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e071d1b-bcef-34d3-93e9-e79e3fa52362 | -2.87581 | -51.46717 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef9bd426-e454-3c5f-87ac-340398b2c79c | -1.3794 | -52.26349 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c3a62e5-ad57-3673-9972-aba121f412db | -2.94428 | -54.45136 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ef3e614-3b0e-3093-800e-1f2c75decfc4 | -2.72888 | -51.71716 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3fa29bd-cbea-3027-85c2-0ae345e08daa | -3.37845 | -52.35773 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0542b659-4107-3946-859f-d24e980caeb6 | -2.3093 | -50.64707 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12b7dacb-4cb7-31d2-b3a7-024a78e0c0ac | -2.34425 | -50.5158 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42a460bc-c48b-3eac-8c1d-d0aba0579a26 | -2.88693 | -53.97473 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 953d73a0-3e82-3e29-b02c-a3c851804dfe | -2.43056 | -46.25045 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dfca67b-1ebb-3a45-a2d1-5cbeae2b315f | -2.98819 | -51.46109 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README85.md)
