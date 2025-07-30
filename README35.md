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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4746024b-b683-3f27-959e-8db52ec5fce6 | -9.6312 | -43.8518 | 2025-07-30 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 09e6928b-ea80-38f8-98d6-ed25f634d66a | -8.6431 | -45.5081 | 2025-07-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 82e6b180-0a55-3c4c-a59c-81b350f66af7 | -12.6129 | -48.0673 | 2025-07-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.9 |
| c535c049-98e1-3c20-b72e-dfaee98c3452 | -7.0943 | -44.3819 | 2025-07-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8655fae0-3394-3453-95a2-60816b9a888b | -12.8225 | -43.0889 | 2025-07-30 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 353.5 |
| e95d6fde-0736-3c36-a569-8aebe4e7b4b9 | -7.0946 | -44.3589 | 2025-07-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 8cf4f50b-7b7b-3147-99ef-2c6e7b4e5c94 | -7.6529 | -46.504 | 2025-07-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| faa2dc86-626c-3feb-88f5-b94fbe6591c4 | -9.6312 | -43.8518 | 2025-07-30 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 12c2dc10-d3ba-34d0-85b6-c5d02bf0a73d | -13.5238 | -45.6693 | 2025-07-30 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f8215f5a-94fa-3a96-ac32-b44a12c54fac | -7.6527 | -46.5263 | 2025-07-30 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| bb346d57-ad47-3c89-ba2c-70d9bbb3ead4 | -13.5243 | -45.6462 | 2025-07-30 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| ff3a68ef-22a0-3dbe-9990-4a0fa24bde78 | -11.3153 | -50.556 | 2025-07-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6f9cd156-dffd-3f36-8644-6d02bced8ec8 | -11.315 | -50.5774 | 2025-07-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| fa030237-bf51-3873-ae16-5d4693fe9cb4 | -8.6242 | -45.5101 | 2025-07-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bf0bf030-5dff-3f77-a26c-8d2ea4133744 | -13.2237 | -47.2195 | 2025-07-30 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e0012d59-1a55-3a3b-b66a-a65a9e97f770 | -7.1131 | -44.3802 | 2025-07-30 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e5da3b0f-3a9c-326b-bebd-50b08affd3f4 | -9.6312 | -43.8518 | 2025-07-30 14:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 207.0 |
| 627eb07f-1455-3bc0-89a8-c82e3fd0311f | -7.1131 | -44.3802 | 2025-07-30 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a87dd16f-2f0b-36bb-af44-adbe40146fc5 | -13.2237 | -47.2195 | 2025-07-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7be0cf8e-7cf8-31a8-84ec-b167e17fb933 | -13.5238 | -45.6693 | 2025-07-30 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 2e199bd4-b6cb-3769-98cd-aa713944ce49 | -13.5243 | -45.6462 | 2025-07-30 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 282.1 |
| f2e49b1b-351f-35b0-ba03-7a5c911198bf | -9.2899 | -49.4798 | 2025-07-30 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8b3f18b0-bc71-3cbe-be12-bf13732b5c76 | -7.0946 | -44.3589 | 2025-07-30 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bb87d702-48cd-308e-a519-ea6dcee053b0 | -12.8225 | -43.0889 | 2025-07-30 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 321.1 |
| 1dc1365c-aa08-3a3a-9391-6792549ce154 | -8.6242 | -45.5101 | 2025-07-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 9856aa66-1565-350e-9138-c14e87f3c6ab | -12.6129 | -48.0673 | 2025-07-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| e4494182-46d1-3739-890a-64bd4ce6878e | -12.6129 | -48.0673 | 2025-07-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 618c6cc7-ad02-3e67-949f-870caffcbca4 | -13.5243 | -45.6462 | 2025-07-30 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 5a7d0262-9a2a-3cf1-8886-d92c82db4aa8 | -7.7728 | -45.866 | 2025-07-30 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 865ad8ab-4406-3111-95d5-46a195131812 | -13.5238 | -45.6693 | 2025-07-30 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| aa485692-5c4a-3bcd-b0da-f68bb8d00d73 | -12.8225 | -43.0889 | 2025-07-30 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 396.4 |
| 016016bf-9714-36d8-8a5e-88186ac648eb | -13.2237 | -47.2195 | 2025-07-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 758a468e-a7ea-3a90-8ccf-447fa662beb4 | -6.5075 | -56.1932 | 2025-07-30 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d30dd67b-3cd2-3dfe-94d0-8091e7883b7d | -7.3078 | -43.7842 | 2025-07-30 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 76f0e646-fed5-3fb9-8529-ec6f21cbba85 | -9.2899 | -49.4798 | 2025-07-30 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b223bcfc-28d5-35e3-acf8-9ddabc314047 | -11.3153 | -50.556 | 2025-07-30 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 4596c3aa-a2d0-38ec-aff7-d0a668831517 | -6.4889 | -56.2139 | 2025-07-30 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 90d2f3f8-5b94-3a18-8a82-0c632582d101 | -6.5074 | -56.213 | 2025-07-30 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| dc403aa6-2d9f-3b1f-84a7-28dc19a98f50 | -11.315 | -50.5774 | 2025-07-30 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| de2f8287-ed1c-3a93-ab3b-4c87f20c6090 | -7.6529 | -46.504 | 2025-07-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 32dcee4e-ee2a-3192-aa69-7b8e99c8573c | -7.6527 | -46.5263 | 2025-07-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| affe1df7-5f7f-3cfc-aa81-5aeabb069f09 | -7.3129 | -46.7338 | 2025-07-30 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 80bb9847-d806-3b22-b5ef-1447bef8c6b8 | -7.5452 | -44.4086 | 2025-07-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6b391a5f-e3b8-3fd5-bddc-f8f32c1b3a26 | -12.8225 | -43.0889 | 2025-07-30 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 286.3 |
| d18744b7-a07f-389a-ab29-7ffc80569cae | -8.6431 | -45.5081 | 2025-07-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 283.9 |
| a772476c-430b-350c-bfc1-91d82da02cb9 | -7.3078 | -43.7842 | 2025-07-30 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 61f1cdef-ac01-3eda-8521-db7f57d71a59 | -13.5238 | -45.6693 | 2025-07-30 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 8a0e9cd3-8e76-3a52-b3ac-65ef3d326934 | -13.5437 | -45.643 | 2025-07-30 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 49a214d5-587e-3b33-9fed-1403dd921339 | -13.5243 | -45.6462 | 2025-07-30 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 404.5 |
| 978d0354-da1f-37da-97f9-230f0a1051e8 | -8.6242 | -45.5101 | 2025-07-30 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a84944a4-c7be-3ba4-a24d-d50b1b1eb917 | -13.2237 | -47.2195 | 2025-07-30 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8166f78c-8524-315f-a9a6-8d964d9065b0 | -9.2899 | -49.4798 | 2025-07-30 14:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 97e4ba02-2f54-303b-81da-36e698ddeb67 | -12.6129 | -48.0673 | 2025-07-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 2aa2cd0c-6744-3f23-9156-98681e5b5447 | -6.5075 | -56.1932 | 2025-07-30 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| dbc30676-66d3-3d4b-8e91-ffa5ac7a65f5 | -6.5074 | -56.213 | 2025-07-30 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |


