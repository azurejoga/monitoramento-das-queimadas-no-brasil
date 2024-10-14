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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65d29af4-8dfd-3528-b0e0-149ec03e7d4e | -7.25025 | -44.96239 | 2024-10-14 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd278b74-709a-3e93-9400-1478e8977484 | -3.05436 | -44.47361 | 2024-10-14 05:08:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 620a3c7b-c9ad-3991-8bc2-0e113064b000 | -3.05354 | -44.479 | 2024-10-14 05:08:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32486489-1345-338f-bf95-56cade84c4b5 | -4.90513 | -46.00616 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3dc76df-bedf-3b17-85a9-ec3c270ccbed | -4.90452 | -46.01043 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41a78cab-f85e-3329-b65a-c36911fc7f89 | -4.84566 | -45.85025 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72245922-aad1-34a4-b7ea-2a1e2e5e54fd | -4.83954 | -45.84956 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e51d5a7-3c68-3f27-81b3-f16d7a60fd1c | -4.83906 | -45.85951 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e209fa90-b9f2-307f-9071-a33a055018f0 | -4.83825 | -45.85849 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5404ae4f-4c08-3d34-9065-feb0d69c520a | -4.83761 | -45.86294 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab1e4a3a-e841-380e-b972-ba1d79887471 | -4.83543 | -45.79162 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bacc6c11-0073-31b6-9f3a-bcbb60bda46a | -4.83303 | -45.85815 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23600064-2775-33f6-8a00-46a5057a5a47 | -3.19195 | -50.3045 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77ef6b42-9602-3846-974a-ff670308df03 | -4.82921 | -45.79146 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1308abf-d1c8-3524-ab09-50467f358768 | -4.8032 | -45.75468 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d62fc97-6efc-3272-967a-ce726f7b5786 | -4.80257 | -45.75917 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b36cf44-0409-3edb-ad3e-7603efc0ae94 | -4.77915 | -45.79253 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e0bde23-455b-33d1-bb7a-2c1e0eb92022 | -4.77851 | -45.79707 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ff06f36-73ea-32a7-8982-73ff58ec5120 | -4.71937 | -46.15477 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64539228-bb42-331f-8da3-078e8cf80c5a | -4.71869 | -46.15943 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 661b2173-1179-3ff1-996a-0a2701b9e9a2 | -4.71647 | -46.15257 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30c27007-61de-3d0a-91a9-c98be5dce8d5 | -4.71584 | -46.15712 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22ca12cc-d291-388c-bba9-684b03d9f286 | -4.71334 | -46.15439 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7280d63-5171-390c-bf49-0987762c2b1c | -4.21079 | -45.77835 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047873fa-57fb-3f2f-822a-fdb5dd200808 | -4.2068 | -45.77186 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 440da0bb-79fa-3814-a44c-f43244360b91 | -4.20617 | -45.77639 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5c243b1-b46c-3ddc-b88a-5d27f1686c74 | -4.20536 | -45.77311 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f88a133-5c4a-3132-ab34-36db0b7a5631 | -4.2047 | -45.77758 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5356a6-d194-3be8-a0d9-e34aba530285 | -3.90252 | -45.70177 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79a9487b-63ea-3a32-8b33-f11303f56b77 | -3.90185 | -45.70633 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b2e2c39-652b-3d17-bc6a-887f7647cbc0 | -3.89705 | -45.70307 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5db61ec-8124-32c6-a650-cb2a5586964b | -3.89579 | -45.70539 | 2024-10-14 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa3d68db-abf3-3fd7-8828-3601eaacad9b | -3.86805 | -45.97596 | 2024-10-14 05:08:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d77eb2a3-7d97-3ea4-8f38-46e90182a3a7 | -4.63008 | -44.86385 | 2024-10-14 05:08:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56fb5dae-d1bd-38ae-a125-1c21acde58a4 | -4.62287 | -44.86821 | 2024-10-14 05:08:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2c626e6-d0af-3d96-b9c4-c8e57c5e2acd | -6.23188 | -46.45683 | 2024-10-14 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62d2851c-2c8f-336d-9551-0794973f2d02 | -6.23127 | -46.46115 | 2024-10-14 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a06dcab-6ade-365a-889c-77d3dd1ec241 | -6.07606 | -46.00241 | 2024-10-14 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39807016-f951-35d6-a8fe-88792520e972 | -6.0699 | -46.0017 | 2024-10-14 05:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3be4af0-ce46-38d0-ad48-6435e584c549 | -5.22804 | -46.02424 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaf100bc-8da5-352a-bebd-3d1bacd11889 | -5.22737 | -46.02891 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e03a2cd5-017d-3d58-b981-b40c53e3288a | -5.22197 | -46.02341 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43517b9e-1236-35fb-bcc5-22a119ab48b3 | -5.22127 | -46.02836 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf42eed9-7458-311e-8cff-21410942c1fd | -5.13628 | -46.06276 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aefe4148-b511-3455-8636-9582058cc1df | -5.13509 | -46.06006 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c38ef8e-92e7-34c5-a405-cef32af4f589 | -5.13442 | -46.06474 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c5e2e7e-6c80-35fb-83a2-05b8bf869437 | -5.07073 | -45.76593 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f01563d5-3b67-3ea7-a399-0546fe3a6a61 | -5.07054 | -45.76768 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1224ba97-e72d-3037-bb40-bc90247dc051 | -5.07011 | -45.77047 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f18693c-5289-3bb2-9eea-bd18deac67a2 | -5.06868 | -45.87197 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdf303b8-f83e-3515-90f2-a45fb15e85f8 | -5.06803 | -45.87667 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1cc0609-9ce7-390f-9697-21c4ccc07e4c | -5.06775 | -45.87351 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6df343f6-9f93-3a83-8731-568756b81242 | -5.06707 | -45.87817 | 2024-10-14 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5942bfa-8387-3e1e-ade4-18997010562e | -5.28083 | -45.6079 | 2024-10-14 05:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ec8c871-ea87-3587-8cdc-eb9e22bc6683 | -5.23818 | -45.1123 | 2024-10-14 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91c8ac37-5069-3fbf-b8f8-af9d9ca918c1 | -5.23747 | -45.11736 | 2024-10-14 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61cad71f-3e22-368d-842a-3de6fb468c26 | -5.16096 | -45.38699 | 2024-10-14 05:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2a35649b-afa6-36a7-b400-8ae79c6ee69e | -7.41891 | -46.56152 | 2024-10-14 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe1e38bc-dfd5-375c-bf29-262e54919741 | -2.74832 | -46.75541 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20aaed87-05d8-3d7b-816e-10b9c3d957e2 | -2.74273 | -46.7547 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9be2bf13-ba5d-3366-b291-e9e3b8c74bfe | -2.45408 | -46.02412 | 2024-10-14 05:08:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 116cb5c0-0b5a-3e14-ace9-6cd9de5bf47f | -2.44745 | -46.92105 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3e2845c0-8884-3137-bbdc-25f8133d125e | -2.4471 | -46.92126 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 968dbc2c-fa96-3323-b97b-a555a181e5d9 | -2.44693 | -46.92461 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| da0cfb46-ebd3-35f7-ae7e-d8ec464ef99c | -2.44655 | -46.92484 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a950c9f-c385-325a-b900-12e9b58f3cb9 | -2.44641 | -46.92819 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc48b85c-0538-3b6f-bf8d-1e178b22a433 | -2.446 | -46.92842 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adebc02c-121b-32c6-8289-0af3135847c6 | -2.44297 | -46.9133 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 878ad0e8-3667-3648-a051-5d28320f0193 | -2.44267 | -46.91356 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 377d5ca2-b900-3d52-ab8b-cc2c1e9dec4c | -2.44247 | -46.91675 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 0c006ec9-6b82-3b51-a051-c1a3c836e2a3 | -2.44214 | -46.91701 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fc08e868-ad00-337c-a5a1-b15bde4b0726 | -2.44196 | -46.92021 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 989923f9-81f4-3bec-9f1d-786ea695ba02 | -2.44161 | -46.92047 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c7e35044-df88-3392-9dc9-af3419e4e9ce | -2.44144 | -46.92375 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b8a9557-e023-3c6e-8d85-4a2233b1222b | -2.44107 | -46.924 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9965b3c2-58eb-3c31-8e72-c7e2849c915f | -2.44092 | -46.92733 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9be23fa-78ff-3958-8672-bee533787daf | -2.43666 | -46.91614 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ae637325-afaa-37fa-ac95-3b7c0fd9fa8f | -2.43612 | -46.91962 | 2024-10-14 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0888045b-a6aa-353b-8515-2965a7bc34c2 | -2.42199 | -46.15734 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9045e23c-7eb6-339f-abf2-7806b53d34b4 | -2.41622 | -46.15646 | 2024-10-14 05:08:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 163ae100-ceca-3161-958c-d0e5b80c905c | -4.70793 | -47.29565 | 2024-10-14 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88e1da9-0deb-35fa-b65b-f7c6c9e9d6a7 | -4.70744 | -47.29904 | 2024-10-14 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a92b60a-b395-36b1-860e-8dccf0aeb20b | -4.70646 | -47.3058 | 2024-10-14 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0015a6-e1b4-3e10-9bcc-7bdd3f8214c2 | -4.70093 | -47.305 | 2024-10-14 05:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4279637b-544c-32d7-8982-2bc083e35d11 | -3.82124 | -47.50287 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6faeb8ab-463b-3f5e-a58c-427242b8ad1e | -3.82074 | -47.50629 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 17a311f7-d026-308b-856a-d3d251816fc4 | -3.82024 | -47.50964 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aacb7b0c-7109-3cd4-ba91-8d0d140a1543 | -3.81975 | -47.51299 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fac374ab-d7fb-30da-be00-7960d58090bf | -3.76238 | -47.50991 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6cce1a5-1590-332c-8f7e-8a923f05f76f | -3.75962 | -47.51043 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a54752a-87ba-3985-8084-3983b212170c | -3.757 | -47.50909 | 2024-10-14 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 684b7c9e-dfa7-3b18-869e-27257dbf1c9e | -4.17834 | -46.73761 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75f12366-c12a-3136-a09f-1ae39a296c8b | -4.15136 | -46.86867 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac2cb103-e416-3c7b-8c2d-cd426ac480af | -4.14628 | -46.86397 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f962c3-52a5-3b5d-8fb3-67326f79ca38 | -4.14569 | -46.86798 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 102d4880-f73c-37e6-a39e-2a808d3e1466 | -3.94737 | -46.44136 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699be522-ece6-3596-8343-ef832949edc4 | -3.94156 | -46.44062 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833875d8-1554-3307-9e19-fb029949602b | -3.93118 | -46.43046 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac8c52e6-7a33-387a-998e-429fc2d62394 | -3.93075 | -46.43066 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fa40e88-69ad-3692-9a69-4d47dd2e444d | -3.93058 | -46.43464 | 2024-10-14 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README106.md)
