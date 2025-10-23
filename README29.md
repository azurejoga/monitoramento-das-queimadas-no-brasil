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
| d7066617-662e-3eba-871f-6632bff5c62c | -2.87293 | -50.71173 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2860ca54-7be1-3ff4-87fe-d1146d672c6d | -2.80989 | -50.27542 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d90d850-f0ad-3925-8cf9-e1fa814feb3b | -2.70232 | -49.85419 | 2025-10-23 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f5ca944-8fd5-3479-ae84-2ec65ed5fd4c | -3.02378 | -49.45263 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60194e0f-593b-37c0-989c-d7d83c16eec5 | -2.81393 | -49.13548 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14dfd746-b3e9-3704-911b-88c02ecd5b3b | -2.92508 | -48.31011 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e6a267c-a8fa-38a1-aaf8-c30e3f0ed604 | -6.32367 | -43.75054 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7299d68-bd0c-3877-a3b3-958cc3b6ea49 | -7.06424 | -44.09669 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11c64f57-1ce4-3a96-84dc-6c7e1afdd31c | -6.59959 | -44.22029 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61cdd8e2-4793-3ef2-9764-119232761b0b | -3.21633 | -46.80615 | 2025-10-23 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 346f8f1e-70ca-35fe-8eb5-c591282f5794 | -5.28917 | -50.57005 | 2025-10-23 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 377e2224-738e-3121-9090-99d19f2198a0 | -2.85761 | -50.74121 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e6b867-42bf-37bc-8128-2a9361ab56fd | -2.86882 | -50.71508 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ab0c5f3-224c-3263-b6db-4fecbbaf2fbc | -7.0637 | -44.10069 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9bb87ff-ec54-3c66-bf90-d900ac3876df | -2.444 | -49.37424 | 2025-10-23 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e278d5a2-1816-323e-8ec3-c0a913d2672a | -5.90202 | -51.43506 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ce08b2-8146-3075-9d35-59ec97502cc2 | -3.47742 | -50.06879 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b4216ce-2281-38bc-a894-41b6173aa5e6 | -2.87233 | -50.71562 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 553d7b4f-86bd-3b82-b04f-5ecfdeb5fa3d | -2.44964 | -49.01032 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faf8f5d5-e90a-30d5-873a-11a5d6f9a242 | -3.67325 | -47.62844 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f881ab0-7f6d-3df0-bae5-737c7e6c39aa | -6.55051 | -52.80039 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d77a60-976c-3bae-8810-0d2942f04488 | -6.85511 | -46.28923 | 2025-10-23 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c063a0e3-6c3a-3770-9eaf-03f714a824eb | -5.03307 | -50.58506 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 245d2270-8680-3a06-976b-e7e32e832797 | -6.59884 | -44.21336 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7a7b919d-ec05-3e16-a5ba-b14179f5a58b | -5.88507 | -46.28519 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 365dcfff-988d-3127-b17b-89a28443ad9d | -3.95194 | -46.96634 | 2025-10-23 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ba973fd-2e43-3c3f-8ed8-d72fa3727921 | -4.64044 | -49.54321 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9658b6cb-286d-3d83-bd73-a86fbc034ef9 | -3.02523 | -49.45111 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ddb164-fae7-37ad-9338-1fe08c921c79 | -2.2499 | -51.9203 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82ed55f7-25dc-38c2-b292-b78faacd547e | -3.02149 | -49.45055 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| db2213e7-35e1-3b96-9b84-aee0648daa4e | -3.47549 | -50.08148 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e63b727-7b38-3af3-97bb-a84c5d54445a | -3.46951 | -50.07184 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 659ae07e-f0df-324d-ace1-b8834ba1f087 | -2.85472 | -50.73678 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c03e205-9535-3189-a52b-75d670a11a64 | -3.79927 | -48.99352 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d744501b-b712-348d-b896-63e95c92b846 | -3.48041 | -50.0736 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f416273-42fe-39d4-91fa-701e554302b8 | -2.25045 | -51.91677 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddbd07f9-2276-39fe-af46-fe59249abbd2 | -5.37147 | -46.86742 | 2025-10-23 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66e1105d-7388-3093-bebe-d8d794a3aa34 | -6.53226 | -55.05398 | 2025-10-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b7eeea-b7ed-3a8c-b183-74a48ab23cde | -2.85701 | -50.74509 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9977cb6f-ba45-3a95-b1cb-5fe4b16078b0 | -3.84629 | -52.33298 | 2025-10-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8501ca00-9f91-3c05-9209-e0dce87f1b8c | -4.19869 | -48.36309 | 2025-10-23 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4dede0-166b-3ee9-a392-25e9f715d0bc | -2.35265 | -48.4865 | 2025-10-23 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 156fbed1-a3d2-3494-9889-79f2f36e329c | -6.32189 | -43.63209 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3281a014-b34b-3e54-a982-60f3c1dbb238 | -3.51761 | -52.82492 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd041f5-7385-3906-b956-b7694e7b6a75 | -3.47614 | -50.07724 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cdf8be2-bae7-3271-9070-1a880e674bb2 | -6.85922 | -46.29554 | 2025-10-23 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd3be415-484c-3952-a1f1-81c214e1cc3a | -6.53403 | -44.36209 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d581c5f-2ad4-3741-8918-7c39b5cb8bd7 | -6.90768 | -46.12825 | 2025-10-23 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edfefa3c-ac22-38bd-b6d4-9a31ba1c1e6e | -3.02355 | -49.48758 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2e87f39b-cb7f-31a0-9e5d-00b0fe2f51aa | -2.25269 | -51.92435 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbf5becb-96eb-3d93-a66c-0de6816a8f4f | -6.3242 | -43.74658 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b00fb929-d3f2-3629-b465-e38fd76dc4cb | -3.24436 | -48.76566 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcf9597a-d82b-3889-ae1f-aef65259e066 | -3.73742 | -52.26913 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0f4e84-7743-3b67-bcaf-5efa6e100f6a | -6.79237 | -45.45761 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5137cf6d-1892-3e44-af69-d8d9572755ba | -3.02117 | -49.47802 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d618a50f-7de5-3529-a02e-db81bbffb453 | -3.46887 | -50.07609 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 436f9dcd-83c8-3977-aae3-8ea881eb7744 | -2.89763 | -49.17009 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2262127-f6cc-36be-8dbb-8f56addca812 | -4.32832 | -46.79458 | 2025-10-23 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31cb1a4d-5b5b-3530-9bae-b8cca839e721 | -4.27906 | -48.19219 | 2025-10-23 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fafb5371-afb4-3bc1-9410-275177b0cea8 | -3.11853 | -45.23491 | 2025-10-23 04:55:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3db3ad4b-275d-3fb2-b6a9-0feaf5fd295b | -3.94683 | -46.97006 | 2025-10-23 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 529622fb-197f-335e-9df1-4e824fd11e67 | -5.37079 | -46.8722 | 2025-10-23 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 834b3704-83c6-3a89-a503-7503dfc2b177 | -6.9627 | -44.01472 | 2025-10-23 04:55:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2430119e-55f6-3a8d-b6f4-f1fd0fda3b3e | -2.92962 | -48.30724 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8914d11e-6197-32d9-b9f6-abebcc1b8d5f | -2.73655 | -48.2881 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 469b0a7d-5102-36c0-8995-67fc6a97fbd3 | -4.28494 | -48.25706 | 2025-10-23 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5039621-dfd1-39c9-860b-b70f99325321 | -6.59444 | -44.21627 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82a71eb7-b5c3-3873-be04-680abe9cb001 | -3.14937 | -50.16048 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc765762-47ef-3904-b4c7-8d358f38ca61 | -6.7928 | -45.45454 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7295cd-fb97-3884-b348-7c406c4bbd15 | -4.18641 | -46.2305 | 2025-10-23 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d21e1c-4b10-32f4-b047-2b338a10e904 | -3.0463 | -49.51391 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3f6844-cac1-337a-9c97-5e44169687ad | -7.62866 | -44.57462 | 2025-10-23 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3a3acc4-c53e-3d21-bbfb-5ac3c03c852c | -2.53119 | -51.17478 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58d00465-9245-3b83-b64d-eda866045d4f | -5.68916 | -45.96887 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e450a95-0e65-3020-b543-dd368acd2a8a | -3.69289 | -52.59646 | 2025-10-23 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60ccb8bd-9f7e-3e50-a69b-61592874defc | -2.98258 | -53.99763 | 2025-10-23 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858a08bc-5d32-3e2a-8c3e-4212a77b6f2a | -4.28182 | -48.25649 | 2025-10-23 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a362088-2851-305c-8607-f7bf6c2d6ba8 | -7.1732 | -44.78679 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81be5189-81db-3990-9502-a237aaab8cdb | -3.12996 | -53.00138 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc10329c-92fb-325c-93cc-59307d23f508 | -6.78461 | -45.4375 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06b09a04-782d-3ac5-864a-56cce8153dc6 | -6.60007 | -44.21686 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 768bf76b-b76d-3db5-994c-ae576fafe2db | -2.89692 | -49.17472 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81266194-0f39-389d-a449-944284c87f74 | -7.27651 | -49.99105 | 2025-10-23 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 996cc10b-f9d2-33b9-96ab-89518869904f | -2.92614 | -48.30315 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53a814a7-19a3-349a-969c-1731f62e767a | -2.87201 | -54.86422 | 2025-10-23 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f9f012e-847c-3c26-a95a-bdc6d674a941 | -3.31186 | -51.26812 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72e25e3a-d181-3e4f-a661-09188d826c77 | -3.80411 | -52.1414 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 539dbc30-9282-308b-be68-1cce116ee8dd | -4.63624 | -49.54019 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e43ea1dc-77cf-3f25-81d8-200d950178fb | -3.32613 | -48.70359 | 2025-10-23 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c6bc21-6f1b-300c-92d5-3b3e7b10a0e7 | -3.21698 | -46.80172 | 2025-10-23 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3626b2a-44f3-3bd7-87f9-401a98fbe87a | -3.21379 | -46.80272 | 2025-10-23 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f9dadec-88cd-33bc-b493-e02381508189 | -2.80632 | -50.27488 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4afdb518-ce0b-372f-b31d-0d5a15e277d1 | -3.64626 | -48.9729 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e56c58f-0ab6-3575-89fd-eff9c9e72e0f | -4.3757 | -50.35382 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5927f9b-eac5-38d4-90a0-4dd8ff03cdd1 | -3.4725 | -50.07666 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8da40ed7-b2b0-35c9-b940-49b8cdd96e69 | -5.04608 | -46.88326 | 2025-10-23 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3384523-c18f-37ac-94c8-17e0511b0024 | 0.33309 | -60.52146 | 2025-10-23 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c55329d6-b628-3713-8b7f-2489a28abe87 | -3.80348 | -51.75801 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ebf0e0c-b792-3112-8bb7-ce61d974365d | -3.11355 | -45.2342 | 2025-10-23 04:55:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d570ed4-5c03-32ac-88bd-d6087fefac75 | -3.48105 | -50.06937 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README30.md)
