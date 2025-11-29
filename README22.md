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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc823be3-b1b1-3cf5-bb02-e63c1b1bfbca | -5.0677 | -40.82055 | 2025-11-29 04:42:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 85489f05-27e5-313b-85da-a966344e7a8a | -0.77144 | -52.33117 | 2025-11-29 04:42:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73da31f9-3b1e-3ced-a85d-ddb00b24eabc | -1.50855 | -52.57533 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5d2f95-d70e-3cac-9cf5-ae92f88863ae | -3.06442 | -51.24876 | 2025-11-29 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd32b475-b927-3dcc-8fd7-338312430892 | -2.78906 | -47.41732 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b9576f8-05b1-312b-ba76-7c5dcddd1a79 | -2.71152 | -53.18693 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a38f02c-37fa-3bf1-a11a-7bdc2d4868d9 | -2.31626 | -48.45712 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37304a55-f2d2-3d27-ad6f-97900d4abfa1 | -1.9553 | -54.40613 | 2025-11-29 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f9448a4-d920-3f10-9113-42c09822ef91 | -4.19897 | -48.90153 | 2025-11-29 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eead1c8-6397-3d6c-b483-628b2d716b78 | -6.71499 | -40.8134 | 2025-11-29 04:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 960ecdc9-16d1-325c-a84a-3f92dc9651e7 | -2.63467 | -48.54202 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0bdb6aef-7915-34ee-b2f0-94283ee7eeb4 | -2.47043 | -45.85233 | 2025-11-29 04:42:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec5f012-f732-30c5-b0c7-d5df977465b4 | -2.89535 | -49.46194 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 518c22cb-165a-3ebc-bea6-a5585827278a | -4.73936 | -44.43403 | 2025-11-29 04:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbbcd7f8-f543-3b0e-8b41-b950b8a31c53 | -3.24805 | -50.69588 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a067330-5511-3f87-a93e-15ff84f77d63 | -2.79186 | -47.42141 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1800e311-c015-3668-a208-bedfea321f31 | -3.25208 | -50.6927 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94dbe6f8-60e7-3cdf-9e2d-39b654abe3c7 | -6.73046 | -41.22367 | 2025-11-29 04:42:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 825d7aad-bb55-3aa5-a653-b343f1f46f0d | -2.7885 | -47.42088 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ffa1209-29e7-329d-9ef3-85ab5a153271 | -5.42244 | -44.85514 | 2025-11-29 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9946c2f5-ee4c-39d3-a76d-3becf469c6db | -3.88028 | -54.20401 | 2025-11-29 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d73263bf-da10-343c-afde-9f58ad3f2942 | -4.9977 | -38.53777 | 2025-11-29 04:42:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d47e5a82-fce9-31f9-9975-f6867b1435bf | -1.48531 | -45.78543 | 2025-11-29 04:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e971fb3-c51d-3189-91fe-4b2623c743ff | -2.78962 | -47.4356 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55198079-d72b-364f-ad01-16927f6590b8 | -2.63397 | -48.48191 | 2025-11-29 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31889997-9eaf-304e-b2da-5d0e8874fe4b | -1.33585 | -53.22412 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 147a05cb-7aa0-3a05-a806-1313cd77d234 | -1.40999 | -55.3865 | 2025-11-29 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba334e56-4030-33de-9c04-8ae272c466b5 | -3.3889 | -50.25359 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bca5b8cc-7344-36af-a8d5-02c109415f77 | -2.68303 | -47.36132 | 2025-11-29 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d36c8927-fd33-326e-bbbc-3505cade1867 | -5.36516 | -43.02703 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71ce29f4-5eb5-3fe1-8cf6-4661ed541a2d | -2.22542 | -47.51521 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9998abe3-ed18-337c-ba8c-36da90c18486 | -2.89202 | -49.46141 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be8c8ad9-57a0-3b5e-be23-d3eed931060a | -6.70183 | -41.46012 | 2025-11-29 04:42:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 829528cf-ac1a-32df-9698-1f345739e34c | -2.47398 | -45.85288 | 2025-11-29 04:42:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d9fedae-3989-3a37-80a8-5b25bea77a07 | -2.93841 | -51.42376 | 2025-11-29 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41ef5640-35c6-3699-8953-584d407cbc44 | -4.5223 | -46.47268 | 2025-11-29 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec261240-73a6-3684-93cb-8e1ee6760db7 | -1.68653 | -53.65612 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b3c387-4bc3-39d2-8f9e-d11de9c29ac4 | -2.17334 | -48.42028 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29a98c0c-d22f-333d-89a8-44a330397eee | -2.22933 | -47.51221 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad2eb54c-75de-384c-9ace-ae2282492484 | -3.20293 | -51.15036 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c43bca4-29b2-3f79-87fd-24fb218c094f | -2.7913 | -47.42495 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3aae5c8-6217-37b9-a1d6-43c3c87b06cd | -2.74702 | -49.3281 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65dc8d1d-f865-3cbf-a4e5-c278827cbc96 | -3.29261 | -50.0918 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63734439-6723-367c-acc4-ded26d0e5937 | -2.83832 | -51.80944 | 2025-11-29 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a953a468-0980-3622-b7be-13b171ecc621 | -2.90681 | -50.40584 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da017ba2-d721-3297-8f64-09f135588186 | -3.61814 | -50.37104 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b847615d-8bb3-3b37-a301-bd399dfedd64 | 0.79237 | -51.96768 | 2025-11-29 04:42:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a69e64-7cd6-3118-98be-4168b7f0f0df | -4.38764 | -43.83074 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2095ad48-db4e-3026-ae5d-904ba9777e97 | -2.92506 | -53.07906 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 632ac65b-83b7-3137-ac95-647b56d4198a | -1.12004 | -47.7357 | 2025-11-29 04:42:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3910d9e-5869-324d-8de5-a874abe85bf9 | -3.22878 | -50.31759 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 443c18fc-2eb8-305e-9737-f7e5bf9bd13d | -4.89377 | -43.96525 | 2025-11-29 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68aba70a-7336-3ec9-b09b-2071b7d9ce6e | -4.22201 | -46.50066 | 2025-11-29 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c26ef915-2d84-30ad-8949-0c4bad701aec | -0.75057 | -47.76266 | 2025-11-29 04:42:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ce240aa-c6ef-316c-81cc-d444f6fa4ee3 | -1.91025 | -45.67316 | 2025-11-29 04:42:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b82ab9-9654-304a-9888-11d52edf1f38 | -4.4228 | -43.31269 | 2025-11-29 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26fa2836-9895-3438-b15b-a6d253a8c1fa | -2.64153 | -48.02647 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78dc5fe0-15d7-3e30-8660-736df2030826 | -5.29812 | -44.7244 | 2025-11-29 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf53a74a-a8a6-3672-a44d-9563ed19ed9b | -2.24916 | -46.52429 | 2025-11-29 04:42:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 42a56f63-2608-311b-8aa9-f314cdb18454 | -2.97408 | -49.62849 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a12aee5-7847-3784-92ba-335dd09ea9cb | -6.98837 | -38.66359 | 2025-11-29 04:42:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc2f6097-1861-3494-8422-c3a291f2b9fa | -4.84618 | -38.74021 | 2025-11-29 04:42:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c6b30fa-81b9-300b-9783-8a1b95a30ac0 | -2.6382 | -48.02596 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c9bee5-ec2c-3926-9901-78b5d9a1249b | -3.02892 | -50.36497 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd21d344-57c0-3ab4-aa91-737a47de6e4c | -2.9999 | -45.42577 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51951539-c2fe-3026-965b-586619ffe70a | -3.17349 | -52.42381 | 2025-11-29 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4613109a-87b1-3a88-a1f6-332a4c1c2866 | -3.79926 | -51.14391 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8fc7c0d-29b6-343a-87b1-3b57722ae782 | -1.12336 | -47.73622 | 2025-11-29 04:42:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 350409a4-f150-38c4-8046-1e3bb1c7db28 | -3.0027 | -45.4286 | 2025-11-29 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2019db1-ec82-32da-aaa3-de3853dbcb77 | -2.30551 | -47.73544 | 2025-11-29 04:42:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdda3511-e0be-3df0-825b-30a0343cf525 | -1.88854 | -48.40046 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c123a307-b18a-3f45-afca-50eb192f13c1 | -3.68198 | -54.56462 | 2025-11-29 04:42:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a903cf08-6d78-35be-87a5-6b5873554e79 | -2.89147 | -49.4649 | 2025-11-29 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fe2c507-4d12-3eb3-bfc3-6af5f498f9af | -3.06243 | -50.35162 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 653f1177-ad21-3651-98a7-6153a227d2a5 | -5.36013 | -43.03071 | 2025-11-29 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c7403b5-cadd-3b11-b4c1-00b4ca2cf17c | -4.72726 | -45.49847 | 2025-11-29 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdce96e8-9fcd-368d-b12e-0f4418bc85b4 | -2.31167 | -46.99231 | 2025-11-29 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22665af2-c465-32ff-81f4-166feef56e4d | -3.38552 | -50.25305 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d50d1dd4-7fcf-32f2-aeb5-4a6db1ef400e | -2.61233 | -47.35032 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2917647-fa1d-333a-92c6-8333720ebbdd | -3.73442 | -49.86692 | 2025-11-29 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fb92bc6-c98a-31bc-818c-7c93e5941be4 | -3.21125 | -46.82484 | 2025-11-29 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44dc6718-308b-3f34-a28a-9ecab0afb06f | -4.11624 | -51.1025 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9049e55e-cee3-3f93-b5d3-7a2eb3ef5a20 | -1.68711 | -53.65248 | 2025-11-29 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a040a1-0c0f-349d-a09c-ba0c93f1ff6e | -3.33495 | -42.49706 | 2025-11-29 04:42:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 036293bf-7364-3f6a-b5f6-3a9ff026ad5e | -2.3954 | -48.51534 | 2025-11-29 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba5f06d2-e5c0-3e57-a403-ab622d449dda | -2.65442 | -47.38966 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 030b6707-4b21-3070-947c-f9a25daee46c | -0.96761 | -47.56654 | 2025-11-29 04:42:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54a4445f-4d87-3301-bc76-51f378e2e82f | -1.2889 | -53.17813 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2a88a66-4772-3b99-bcd5-f3cedbaae306 | -2.74925 | -49.33557 | 2025-11-29 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6915f853-8a29-3d9e-9613-8e6eb4ce723b | -3.07603 | -50.35378 | 2025-11-29 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af3fa895-3805-3612-ac28-4a3dc6f39e30 | -3.33756 | -50.2492 | 2025-11-29 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ec9021a-8408-3116-b297-3233f051185a | -2.95984 | -53.28434 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f796b7ff-4414-33f9-a8e5-b0e28966e2d0 | -2.73508 | -45.25751 | 2025-11-29 04:42:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb1cf369-192e-3904-b880-34153142c6e2 | -2.63765 | -48.02942 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8910237e-92a4-3c57-8ae0-2543c152c507 | -2.9332 | -53.27459 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c920419f-ffa4-32a4-8659-ed36e4cf426e | -0.89119 | -53.09256 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9934b4d0-1f16-378f-93c0-52f01446ceef | -3.14669 | -40.18105 | 2025-11-29 04:42:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dbcf38b-f5c0-39b1-aaa7-cfa2f68b6aa1 | -0.91122 | -52.43996 | 2025-11-29 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35242cf4-9cf1-3615-a4c7-ad4eadf32363 | -2.93113 | -53.26621 | 2025-11-29 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fd033f1-4b7a-385f-a3ec-b80bdd44ee20 | -2.79074 | -47.4285 | 2025-11-29 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README23.md)
