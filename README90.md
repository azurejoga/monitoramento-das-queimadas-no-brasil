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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 769e0f56-906c-38df-8848-15ae8d492639 | -6.72903 | -55.09496 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be2fab9a-11f1-3a82-9531-000de2dded6e | -3.90666 | -51.89174 | 2026-09-22 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2ec2e00-1eef-36a1-9b4c-3749cd7307f9 | -3.46332 | -58.40369 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2212cd24-fa44-39bb-bbc3-06ef3545a4ee | -4.14084 | -51.09896 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3353af6-6537-3090-844b-c5fcd58f9c88 | -5.85407 | -49.78028 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42374eb9-82fe-31d5-9650-8a2c84511a89 | -1.45268 | -54.23844 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7a6b36d-21c4-3a35-bca1-8b529e81565d | -10.87754 | -53.95684 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80e477d9-9509-3dd4-9719-89339963884b | -3.16288 | -48.08064 | 2026-09-22 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5be58e4c-6660-3e72-b4a4-4e9ed46099f0 | -6.83582 | -55.53043 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf820bf-0644-3a5b-89ee-8d268015148f | -6.79574 | -58.79158 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 786b87c8-f96f-3b4f-973a-c586878bcf85 | -7.33468 | -55.60187 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94c5f5dd-e8fc-3f58-9ef6-bc032f60b48f | -4.96899 | -55.82919 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b35eb22-6f80-383f-8fa9-1b2e609ea343 | -11.96677 | -64.04259 | 2026-09-22 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f326c3e3-81dc-3359-a653-0c27a29cd0d4 | -3.06972 | -54.41065 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5864230-0219-37c5-bfb3-e30d01e46cdc | -11.99154 | -58.07416 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a681882-0105-37bb-8c54-0c1ae52ba8a4 | -4.27533 | -55.44301 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8da1276e-f3bc-3a83-9dbe-26332dc6d858 | -8.67403 | -70.0277 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18ea622e-78a7-3f51-8b16-b2245de890fa | -5.98123 | -57.77354 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5334b68-e903-3283-9a3a-ab7827d1cf17 | -7.33527 | -55.59805 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eaa034d-d885-35a3-ab1c-344498b72285 | -3.7518 | -58.32533 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51ef8e41-75a2-3284-9a90-0b9f57aeafaf | -6.91511 | -59.63282 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92056179-4ed5-3673-bde4-5c9e1dba6d41 | -4.52316 | -55.66195 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9160a9cb-6047-3b36-954a-601dc9b7b1b5 | -6.46407 | -59.96741 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeaa755c-9e0e-3ed5-b791-23e554b5bde7 | -10.87552 | -56.23912 | 2026-09-22 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94589162-c675-3523-b3e7-7495c672c2c6 | -3.8531 | -54.21786 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17724b2d-5482-3ccd-a8df-6390a00ffe3d | -1.7474 | -47.13317 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e040154f-fa9c-3f57-8bfc-1314fdac4f2e | -6.1681 | -57.70314 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 073a2d8f-b6b5-34a4-a700-fe143a5ddb57 | -5.80526 | -53.51961 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6f809b4-6e2c-38f8-bc00-f860f6ac6bec | -10.86878 | -57.1712 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 820ef04f-a461-3d16-9d44-78956cfb3913 | -2.98011 | -54.15417 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6cc8726-5d7b-3b72-9725-af9d1d9f4bf7 | -6.04386 | -57.82276 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b1e06dba-15e0-3418-a40e-b45185868430 | -7.61024 | -55.34185 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 847d81b1-8a2b-32c8-b7e6-d26d184c9265 | -6.33777 | -59.94824 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f015b613-5bd8-3ae2-87fb-fed564c03ede | -7.59476 | -57.66656 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc752e1-2346-38b3-8dbc-976fe1eca78e | -5.91441 | -57.68384 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a2ad069-5e25-3a55-9ef6-2329992e0f5c | -2.48594 | -58.00843 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a616c511-5964-3797-8998-8fc08e59cfb9 | -6.43595 | -55.6151 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44fe2515-3f60-31e5-af75-e202de429a78 | -8.79529 | -44.27389 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 864691ce-f29b-3e2d-91b4-d8105c8a4142 | -3.08361 | -51.28448 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1fbbfbc-2790-3d49-a87f-86bfdd64c35c | -1.93392 | -56.60663 | 2026-09-22 05:23:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ada8913-83df-361f-b13d-2d9fb3c4e094 | -13.87626 | -48.56125 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d601c35f-72ba-3710-a832-ea58240c6042 | -4.30129 | -49.12164 | 2026-09-22 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46c7bb20-646b-3bbe-be4a-795565cfb538 | -2.61828 | -51.72419 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3d54a2a-884e-3a4a-8b87-ac1977db3b09 | -3.28769 | -57.86213 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a158c22-ca16-342e-b414-b96d05bd981b | -3.05235 | -54.40796 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061ee0dc-2486-3cff-82f1-0eb5034ca7a1 | -7.32661 | -55.60837 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc37393b-987d-3d2b-bd71-576107233cd4 | -6.72849 | -55.07519 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 577c5e41-4a18-3da6-92b3-5e3cf8193157 | -3.38843 | -59.52973 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f5b4bc9-3128-3c0b-b0b7-519ba8e7be21 | -5.81793 | -57.7401 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcbfc8d4-9be8-35df-87bc-fc985ab2d765 | -9.608 | -43.92181 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4af973ab-59a5-3e8f-a074-c8db5edc93f3 | -6.97711 | -47.50437 | 2026-09-22 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ef7f0b5-67d5-337b-bd64-d7d4628c60b1 | -1.33024 | -54.66102 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e6a02e1-259e-313f-8d0c-924949d2f817 | -6.4271 | -59.97385 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cff501ec-1c5e-33b0-b18d-1ef7c7289894 | -5.98364 | -44.73035 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 383a01eb-ed14-39d9-a35a-4882381eb7e2 | -6.73371 | -55.08786 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9327395-34f3-3a4b-83db-785201d141c0 | -11.50878 | -51.51196 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f80c8e96-65b4-3ff9-85d7-f02a18d907fa | -3.1577 | -48.07998 | 2026-09-22 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0f6f662-7d9b-34ff-b1d0-315fe32d0280 | -6.07612 | -57.72782 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b07a4a-e805-36e4-9ffb-c98ddfe1a505 | -1.30059 | -54.20481 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da101b76-73d1-3fe1-a0eb-a04d7abe428a | -11.32472 | -51.35868 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b670b9da-15ac-30af-80c8-515fde386be7 | -4.50111 | -54.96062 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d68561d-f90a-344c-a37b-99ffd6ba42eb | 0.0419 | -60.6143 | 2026-09-22 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 398c6969-bb3b-38a4-88b9-91e09e6e9eb3 | -6.52072 | -55.37965 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8f8807-8297-3ea3-9e87-cb300bb3b7a0 | -3.06485 | -59.30532 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3291d5ae-1dcd-336d-81ec-0992664be41b | -3.02614 | -54.18121 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea58b510-c9ed-3c8b-af37-970198d94e6e | -6.42853 | -55.61774 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e742b9cd-aba6-3db7-89ab-624fa4471545 | -7.44841 | -44.74207 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7abfafbc-f234-32a6-bc4f-916a9db865ea | -6.75853 | -59.06516 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 253abec8-2a18-3060-a9c6-ccc987e72ddd | -11.93229 | -46.51423 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 945611e7-c91e-32b1-85b1-e89d1e1d2d9e | -8.08544 | -55.34009 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01f75b51-b1a5-3d2b-8520-0210c3146929 | -6.7127 | -59.45734 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de68c9f4-ce4f-3c64-a36d-bde97d2feb13 | -7.32431 | -55.60042 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecba551e-d27d-3321-80aa-00b8ba0cc8b3 | -6.25855 | -55.43295 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a333c8db-f98f-3a1f-9bb3-6b7deada9ee7 | -3.2257 | -61.05662 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a757623-736c-3cb6-ad38-3cf6b17d7831 | -12.01719 | -47.80226 | 2026-09-22 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75e0bbb7-f3fd-3cfa-8568-f486b650429d | -2.9141 | -54.18458 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e03e30-deb0-3866-a652-2bf16a57586c | -8.3296 | -47.53652 | 2026-09-22 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1803643-38b0-37a1-bbaa-755a9191c7e6 | -3.5558 | -50.29265 | 2026-09-22 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 313e37d3-af73-3812-9ccb-deb3dba5f393 | -6.92613 | -59.6307 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 767ae3b5-0dba-3591-b3cd-82d22a8f95ed | -4.44942 | -55.60275 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb0ff306-d830-3606-8026-feb2b7eeb35d | -8.30776 | -50.38189 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963e0760-f563-3b74-9b6e-2201e0ef15ac | -6.83811 | -55.53848 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c4fac9-4ea0-37d8-b729-b123188acd8a | -6.00848 | -47.90368 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68987531-35e0-3cf9-b74f-560c9bbbd29e | -6.38021 | -55.2785 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb7685c3-356b-3fc3-b3a0-83936dd861d5 | -3.18503 | -57.87183 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4f53c7-26be-3a79-9078-57b60fd13838 | -2.5695 | -57.5059 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccec531e-9016-3f02-b36c-7f548e1ea4ff | -7.57869 | -57.68184 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758ca2d0-33e6-3201-b6dd-b4c4d88da190 | -12.86516 | -50.94667 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d52b9c1-aa6b-33b9-9e98-9988f5acbb59 | -4.60716 | -55.75127 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeff250d-68b4-34f4-af09-92182b0a1941 | -6.8398 | -59.01807 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a37ba968-857d-3565-9c86-aaea127b4574 | -6.26856 | -57.72965 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76158767-644c-30d5-a8c0-de712f9a562e | -6.64383 | -59.92693 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 41babcde-e819-3c4d-9641-05568bddf48c | -5.93884 | -57.70203 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 309e2643-691d-3d43-bfde-2c908669a6f0 | -6.06384 | -57.86889 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80393e80-045e-3ca1-bd1f-7e744d7ae448 | -5.80905 | -57.73154 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29ca4856-ef94-382e-8e65-895edff4685f | -3.20417 | -57.83836 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d408f1e-4dbc-390c-91ee-80ead6b64f83 | -3.47783 | -59.60109 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b5c6f2-46e4-3045-b0e9-954be8eb761c | -6.0433 | -57.82626 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cd070826-acec-3076-afa0-6ff1f1a8cbea | -6.46284 | -49.87938 | 2026-09-22 05:23:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02a44146-2dab-305f-aa14-63da1947b990 | -3.43957 | -58.02837 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README91.md)
