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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a08acd-ac1f-3f27-af39-3a9bd49dca79 | -5.13369 | -55.9478 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfb65061-44ee-3e71-a5b7-94029bfeb2e1 | -5.15521 | -49.4398 | 2026-09-15 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2326ebe-87e2-3109-9509-3bd9e3e1176c | -7.22913 | -46.15342 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 066cd982-876a-31dc-ad77-84f120a834ef | -1.22631 | -54.13612 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fadbbe98-565e-3e58-81d7-ab5531454a57 | -3.49758 | -50.37944 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e03cbc2-5f8c-3317-b722-402d1040eed9 | -2.8218 | -51.33905 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af848d44-927b-393f-93bb-855d05778e7f | -2.94661 | -50.40797 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e056be9-5833-3a12-a49d-59b85e1cd1ac | -3.49447 | -50.37387 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3b0f2d3-2c9c-3374-b629-2a62a97a9bb6 | -7.44321 | -45.48029 | 2026-09-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 899ac9c4-d6fc-36d9-9403-74954c5ad713 | -7.08542 | -42.12398 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12878d61-af92-3647-b471-64dee842f46e | -6.15723 | -55.70316 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80969eec-ca66-31af-bea2-ab69600a917b | -8.09486 | -43.78094 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 921a2d62-b4b8-39bc-a4db-12521d47f939 | -2.66107 | -57.56958 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9be5094d-d097-32ee-8ef1-df81833a0e40 | -3.41623 | -58.22343 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f71f1eb-78dc-34c9-88dd-dde1504e90e7 | -2.82686 | -49.22528 | 2026-09-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4362c083-f7de-3b6b-86df-fe6b29967809 | -4.38463 | -55.20486 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5934a7c-1899-3736-9412-18684fa54c0d | -5.60446 | -44.84531 | 2026-09-15 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 90c90514-841a-3533-b1c3-8e871cac4de1 | -2.69429 | -57.52731 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c35d45f-14c0-31f9-a582-ca71d3ddd74d | -4.09963 | -51.0881 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac7434e1-0a38-364c-bcda-3dbaed0d2906 | -3.07776 | -51.19941 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c44c6c0-3eb2-34cb-ab42-dc629c7e3fd2 | -2.89417 | -50.43067 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35e87808-3ddb-3a4c-9ce1-15607b45de9f | -6.15213 | -52.73892 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e44c8677-a68a-3959-bbc7-fc06bcb3ca8b | -7.11407 | -42.09549 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1cb121d3-6215-3ee6-84b7-2c074a92b16e | -7.97611 | -44.02026 | 2026-09-15 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1dc7cfe-4556-36e1-ae80-e2ebfdef0fa5 | -2.90709 | -50.40154 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a92d856-04d1-3f52-9895-dbda92417863 | -6.26149 | -41.97885 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d58a1964-df30-3f38-8aa8-068acb1033ad | -1.23278 | -54.09664 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e885109-1b3f-3a55-9bdf-8650d7e9f30c | -6.95046 | -42.56001 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6a79e9f-3f3e-3367-a8e9-03b9e2e4f3a9 | -2.69344 | -57.5325 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2322bb9c-68aa-30fa-8cee-dcb810c1b587 | -7.23248 | -46.17533 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeeb69f0-5aac-33dd-a7c3-623268e988f7 | -3.84785 | -51.76445 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc5c862d-ffbc-3958-8aaa-a4dc8b617853 | -2.66193 | -57.56438 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 822a47e2-2087-3ab5-9834-3ed0cf622386 | -6.6649 | -54.98465 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd95ee2e-59ce-369c-b10c-ff6af8a16cac | -3.42181 | -58.23019 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d22a993-34c3-3073-ba6a-33e7a3ed74cc | -3.0943 | -51.29131 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2659141f-7a29-3a8d-80af-9a6df3277827 | -2.91104 | -50.40217 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e5af88e-5fcc-3760-b617-e8aa97037176 | -1.22164 | -54.13189 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ef57921-776d-3936-b608-204663e0f516 | -4.86246 | -47.40947 | 2026-09-15 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c3c06ce-b8a1-3e58-9d69-a8aae757f51e | -2.90459 | -50.41673 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 504f9edd-50c3-3f94-987b-37a006017850 | -4.51136 | -54.97188 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e1187a-b43d-35cc-9bf7-0759420755fc | -7.08372 | -42.10868 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10803f3a-1ae7-37ce-ab32-0c424ea905af | -2.88952 | -50.41767 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abd6c04c-f366-3417-991a-a5c16e12ad80 | -7.32821 | -45.36728 | 2026-09-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e5419e2-589b-3b09-af35-038f3d30a13e | -5.85548 | -52.10262 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c362722a-6a4d-3f46-a407-323d1c976032 | -7.29123 | -46.75 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ede3ea9c-76e8-3418-9ebd-5e2ea9e4a67c | -4.18723 | -48.68717 | 2026-09-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b4718ec0-75c9-38d0-884a-db4ad4edf5fd | -3.33574 | -53.26826 | 2026-09-15 04:32:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae34f48-4ad1-3c6b-9ffb-63d5663d4a40 | -3.75599 | -51.14755 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6be3d7e-a1ac-38a0-a704-2e1753bc17aa | -5.7988 | -43.6475 | 2026-09-15 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 407bf79f-2564-3815-859d-34109faa13a8 | -3.32675 | -54.19162 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a5483e-431e-30fb-b0ef-2550d3f1bcc1 | -7.17524 | -43.60681 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90c5144c-ee85-35e6-97f4-e7100ec6ed6f | -2.66455 | -57.55962 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7b48a75d-da22-30bb-986d-148cc4e75bcd | -6.51426 | -44.05502 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19da7b30-2031-3d84-aa66-92e71fdb39dc | -7.45827 | -46.14332 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72e6cfe7-93c6-3dc9-a3f1-414e1ff25599 | -6.8066 | -43.17919 | 2026-09-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aab4836c-d124-39fb-8876-927168093e20 | -7.16193 | -43.52451 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8ac1fde-2c65-3ca2-af34-981f1bc3b87d | -7.07908 | -42.11301 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b179df2d-05a4-3f65-8459-ca4f00f43398 | -6.14487 | -52.78204 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8e89287-9560-3096-8a8f-42abeaf22545 | -2.94742 | -50.40293 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c04ae755-4aaa-3cdb-88d4-1b0539d69e04 | -2.89334 | -50.43571 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d26c99f-cda1-390f-9186-4e2838b72854 | -4.51191 | -54.96858 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79e73d07-693b-36a2-ac9a-dd880063562e | -3.23084 | -50.5863 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da3a446c-1980-37cd-8f72-81b1edef3130 | -3.85971 | -51.98302 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0386eec-79ee-36a4-8a23-79873aacc615 | -1.1967 | -54.12037 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecfe3b3e-ae43-308f-8a22-752044f30a65 | -7.11011 | -42.09246 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db3eadbe-0a02-3a0b-8069-d485d7421981 | -7.2959 | -42.36044 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46bad779-228b-3cef-9c2f-995a09360202 | -2.96637 | -50.41116 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b30fdc2-deae-3452-9d77-2ea8d7d6b4ce | -7.17166 | -43.60624 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96ad6616-1a4d-3f16-a3fb-7c38beaed48a | -7.23634 | -46.17238 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40e0c7de-da4c-37cb-9cd0-3451fb8fb8d4 | -5.84864 | -52.06641 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a748e4e6-db36-3493-b92c-f6c29836adae | -4.55309 | -50.46293 | 2026-09-15 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45390672-6d5d-34ba-a6d1-ad5826b7ae62 | -2.68558 | -57.59012 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc1c36aa-bc13-33e8-a565-038a5117723e | -3.23001 | -50.59144 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04022f26-93c9-3e88-ab84-3275491eb24a | -5.88138 | -52.07808 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f280ff3b-6232-372a-a3ad-5865c85a2a4d | -3.33497 | -54.19365 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f1bcf1f-2800-36b5-9828-e4fdf780f14d | -7.17357 | -43.90094 | 2026-09-15 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8279ac68-e658-31da-8225-2b24b0941280 | -7.55401 | -46.87033 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24ee1d5d-c51c-3a2b-babf-534501d86412 | -3.53839 | -53.99704 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 48a60f38-756f-3614-b752-64027c3aa6fe | -5.55637 | -43.43651 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4646ac2c-a09c-3cee-9db1-c00242782550 | -4.66615 | -42.08928 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 2252431a-f8d6-3064-a7c3-c39c21f78c0f | -4.67511 | -42.08125 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7875cdc-ca88-3c31-9e08-a483b7510d44 | -3.39938 | -50.75634 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e38a0e2-3ac9-3dc5-bc61-f30b8056703e | -7.58863 | -43.07195 | 2026-09-15 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a06fb1a2-e8a1-3055-840c-d83839bc007d | -3.16944 | -58.65141 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2efd3c0c-ea31-39ce-b205-0f1c44b1f2a7 | -7.07836 | -42.11789 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37719dd8-be0f-3f93-868e-1cf1f5cd68ec | -7.6087 | -47.29534 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34c63eba-4cfe-3721-8f1c-a9155a713d52 | -5.61618 | -45.24479 | 2026-09-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78ae5360-4571-39f7-8d2d-5cb16068ac5f | -7.23911 | -46.17638 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c0102a3-900f-3e1b-9479-1dff6e588412 | -4.18787 | -48.68319 | 2026-09-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd0f777-82a6-3171-b32a-343e49a31b74 | -6.33493 | -39.39052 | 2026-09-15 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eec0bd1c-1276-38b1-abf3-7d74c7b7eed0 | -3.41995 | -58.20998 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d814aa9-636b-3a0e-a8d0-d06e9d0d5368 | -6.94596 | -42.56172 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb05ddd1-848a-33fb-ae59-67a1bac95d6d | -2.91333 | -50.41294 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1d85869-1bde-34b9-8240-2b56886a51e4 | -5.82469 | -50.15769 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f356a8-7503-349e-86d6-d5b46997228a | -3.06964 | -50.57112 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 353483a0-6726-30a2-9103-f3e912e49a27 | -7.2319 | -46.15742 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 000a279a-e809-3bc7-b849-89b997416257 | -7.08445 | -42.10378 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4484d1a5-47d7-38b5-b771-3739b063ef2c | -2.94975 | -50.41364 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46f20e14-e1ae-3597-8232-df92de12280f | -7.0922 | -43.53614 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 996d5859-ec6a-3620-b2a0-6ad7e20eacc2 | -3.54339 | -53.99781 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |


[Clique aqui para ver as próximas entradas](README41.md)
