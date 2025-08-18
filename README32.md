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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67bb67cf-af08-315d-838b-e7969c2250fa | -12.98299 | -56.84805 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 249e6a4f-dbf1-3379-b1b4-cd5867ecd9bf | -20.40909 | -54.69093 | 2025-08-18 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7115cd26-9a9e-3009-97bc-64aa54e29880 | -13.00362 | -56.84745 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db8161c-6c7c-388e-a1bf-0881aac1ae60 | -15.61365 | -54.31305 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8fc146e9-3278-3664-950a-20e4e89de136 | -12.98768 | -56.85172 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1420c5fb-f5e5-3d84-8529-3a578c6730d4 | -12.99782 | -56.85286 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0547d23-3699-3b52-a8d3-a973f50b1472 | -15.6203 | -54.30906 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c3d46e6-fea9-33df-a226-b1369111b13e | -15.03983 | -56.03076 | 2025-08-18 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a76fb41-c187-37af-8da4-f7c79286a16e | -13.14011 | -57.14654 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2599d694-ebe7-3eda-9e4c-ff52623a7c02 | -12.99818 | -56.84988 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36df9f78-7340-3e49-b1d8-609f6601a54c | -13.1421 | -57.16237 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 786602e0-a1cd-3bbb-bb68-3621cca2810e | -14.99575 | -54.79416 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ca7d52a2-aee9-396c-9940-b8cede23660f | -12.99745 | -56.85585 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b97d0555-4495-321e-acb6-e8f8fe1bf524 | -15.76468 | -56.2965 | 2025-08-18 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd6dc828-2f4a-37d8-a788-015a28293ac8 | -12.99348 | -56.84632 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8bdd3dd-b66a-30fc-8b5b-a7a9ef26537a | -13.14064 | -57.17368 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9addd9a7-139f-35e1-a04c-ebd7a6aeaeaf | -13.13942 | -57.15225 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 156153ca-e45d-34b2-8805-dd3bbacd85ce | -14.99074 | -54.7851 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2de8f602-5555-35b6-9352-13ec3369fce2 | -13.02278 | -56.85879 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 591909bc-08b4-3850-a6be-b480077530c9 | -12.98262 | -56.85107 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d64f1ca-aab1-32c2-af06-8dc95cffb038 | -12.98696 | -56.85765 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9280ee62-aefa-31db-87a8-d3618db5727a | -13.45774 | -55.10979 | 2025-08-18 05:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d182cd49-d31e-3906-b5b2-1eb368909720 | -12.99636 | -56.86477 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66f9248b-ac11-3509-9b4c-3d9516385c5f | -14.86964 | -59.60915 | 2025-08-18 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7948f4a-8912-37fb-9299-324f690ae0a6 | -12.99385 | -56.8433 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66fe2062-73ee-3018-9b01-3885ba9df799 | -13.4343 | -57.02792 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bcf178b-b6e9-3b35-a77c-c3f29188efea | -12.99311 | -56.84932 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21a05d4e-f0f1-3d77-8d6d-9d56c0b9466e | -13.00795 | -56.85405 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be7c6832-78aa-33fa-85ad-400a09f76f3b | -13.01919 | -56.84632 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2315c2b6-4e3c-33ba-8645-5bd4d640eeb3 | -12.99855 | -56.8469 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b932dba1-b886-3c48-a2eb-7a8fb052a36d | -15.61406 | -54.31258 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d04394bb-b369-369f-b966-80098ad5f17e | -13.43933 | -57.02858 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a6b9a822-5215-3605-b5b2-c26cf288f962 | -12.99202 | -56.85824 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fa808d7-02dd-3059-9483-3f5f7c812723 | -13.13858 | -57.15043 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d10bbf9c-82a9-3714-8b85-cba182db7bfd | -15.00842 | -54.7885 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 15e3bf57-91e0-33b2-9593-d88af12df6a5 | -14.96813 | -54.77159 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68f6855c-14e6-3b22-b8f5-229fe2535b55 | -13.02388 | -56.84993 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf7dab68-9247-33e5-9c2f-634561927a65 | -14.98983 | -54.79328 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 718336fc-a7f5-3f80-a29f-dc5d1cd28343 | -13.02351 | -56.85292 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef98c3b-358b-37b8-ab47-8002c5756505 | -13.45821 | -55.1058 | 2025-08-18 05:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 125db65c-d637-313f-8944-c631a12afb91 | -12.99238 | -56.85528 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8850d4bd-4597-3768-b099-45e7f9ea3fcf | -13.14706 | -57.16299 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 691e2192-a70f-3154-9fa2-11f307085ed9 | -12.98916 | -56.83959 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695f74af-927b-366c-a253-57fc99235314 | -13.01808 | -56.8553 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56dc2a28-0577-3b0b-9216-47b7b3a2c394 | -12.98804 | -56.84873 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e1c984-11ce-336b-8720-58396d93c7ed | -14.96765 | -54.77596 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec7f9830-e3e2-3268-8c51-05a0a696513b | -13.47455 | -55.77154 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92a9e2b8-dbb3-3dab-aa73-78c582aa5d82 | -13.13669 | -57.17491 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355bdf1c-8fc6-3580-8291-a57867a9d07e | -14.97947 | -54.77804 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea109b59-05ea-36bd-b083-b93335920b52 | -12.99929 | -56.84087 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9207afef-c5c5-38f8-afcf-cbb9aa1ac1a9 | -13.43468 | -57.0249 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8af73e45-fd43-3791-868a-e06a76983091 | -15.60891 | -54.30254 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6cf41066-e6fb-3068-b2e9-779670890418 | -15.61458 | -54.30781 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9dcf3733-23fe-34d5-878d-13d52b8ed133 | -13.13568 | -57.17303 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b88997-6193-37b3-b9e4-936fe07379c1 | -12.99892 | -56.84389 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4063cdd4-8c0c-322e-afc7-686e7651745c | -12.98841 | -56.84571 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fc49c57-6edc-33a2-a732-831af988636e | -14.99027 | -54.78932 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f160affe-4e1a-3aaa-a9da-3f0ff73b5add | -15.61414 | -54.30827 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57b51bed-bc34-33cb-984c-e3ff35e05262 | -14.62891 | -54.91275 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 530ec1db-0a94-3ac1-93cb-786d3fc35469 | -13.13434 | -57.14416 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48c7fcd8-a2f6-36d2-8a4a-01cb88a8d115 | -13.219 | -50.7566 | 2025-08-18 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 29bb8843-0db9-39a8-98a0-a9b59c39aff4 | -13.2186 | -50.7781 | 2025-08-18 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 360.1 |
| 0b69b1a8-bc69-339b-957f-02965802b8f9 | -13.1994 | -50.7806 | 2025-08-18 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 7635f2cb-5fbe-3351-8b5b-c65033f29096 | -13.1749 | -54.9132 | 2025-08-18 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5f63f363-d617-3d37-9c49-42730bb0b14f | -13.1746 | -54.9337 | 2025-08-18 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| feea1b22-dfb0-3246-a883-0be2d16de889 | -13.2183 | -50.7996 | 2025-08-18 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| be2b5403-10a2-3741-91c4-0dcee235da70 | -13.2378 | -50.7756 | 2025-08-18 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 65a7aae8-017c-3da6-8d03-c13f2a5d6362 | -22.20324 | -56.03787 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05da0dca-aa05-3fdc-aba6-8139ee8c57ef | -22.19979 | -56.04161 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1160e916-3f37-3d18-afb6-3a8b9f9125f6 | -22.20248 | -56.04692 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f278c90-82e6-3dd0-83f6-a744cfd3b54b | -20.87102 | -54.97752 | 2025-08-18 05:40:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3db0dfc1-a29d-36d1-820f-f791997940ff | -22.19938 | -56.04609 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20578f18-1a03-39ec-96dd-94e75a33cc8c | -22.19725 | -56.03751 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d5a5a9b-f8a0-3c1b-872e-1a6693d9ae24 | -22.27102 | -55.95199 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10bfc8e8-bb45-3ddc-aad9-d6ebfa4ef14b | -20.87152 | -54.97165 | 2025-08-18 05:40:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8100ce36-5b79-3dc0-b45b-0b7e6230c38c | -22.2002 | -56.03709 | 2025-08-18 05:40:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60a8b70d-fdc4-39f2-999f-6ff282fa8942 | -13.219 | -50.7566 | 2025-08-18 05:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5008a56d-b4c2-336b-9a89-7f59b82009bb | -13.1746 | -54.9337 | 2025-08-18 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c5153eb1-5a81-32d6-93af-b1c6b552076f | -13.2183 | -50.7996 | 2025-08-18 05:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4a689457-18b2-30d4-b526-0425cb4ef674 | -13.1994 | -50.7806 | 2025-08-18 05:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 1ed8eb22-8739-3c27-93c0-36df027d5660 | -13.2186 | -50.7781 | 2025-08-18 05:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 2bf5703b-cc6a-32cc-bbf8-bc12409694ad | -13.1749 | -54.9132 | 2025-08-18 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 88859a27-cf7e-3a29-88b2-b26a8c504e16 | -13.2186 | -50.7781 | 2025-08-18 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 367.7 |
| 314558db-2520-3c61-9104-d389828f97c0 | -13.2183 | -50.7996 | 2025-08-18 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5fb13566-1b81-3e66-a593-6bbbdd66edfc | -13.1994 | -50.7806 | 2025-08-18 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 4c96977f-ae6d-35be-af9f-d95118cccb66 | -14.9815 | -54.7743 | 2025-08-18 06:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 57b3f672-11f5-3372-a52f-4547130a19d5 | -13.1746 | -54.9337 | 2025-08-18 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| bdff67ba-acd6-32d7-b79f-3a500b8200a0 | -13.219 | -50.7566 | 2025-08-18 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 84c5c208-91e7-32a2-8e05-bd1774750b87 | -13.1998 | -50.7591 | 2025-08-18 06:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 46406759-271c-3f5d-a518-4499d2d9badc | -13.219 | -50.7566 | 2025-08-18 06:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 7b3c84ae-60a9-3ee4-84b2-c06eac8eedff | -13.2183 | -50.7996 | 2025-08-18 06:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9b9cb758-2d09-31ea-92a8-d21cffba6998 | -13.2186 | -50.7781 | 2025-08-18 06:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 8c45b4e7-8b74-3264-ba91-9952b56db636 | -13.1749 | -54.9132 | 2025-08-18 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f92271de-16c0-3a08-b89a-e18d143b6e53 | -13.1994 | -50.7806 | 2025-08-18 06:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6ce080f7-710b-34f6-ad56-4198193e8190 | -13.1746 | -54.9337 | 2025-08-18 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| b6f69c85-a593-3412-b7e7-5a7e3d1e1f1e | -13.1749 | -54.9132 | 2025-08-18 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e4287149-6497-36ee-8945-17f07c6fc065 | -14.9815 | -54.7743 | 2025-08-18 06:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 38910fc7-063a-3d5e-b016-75bde8fa6679 | -13.1555 | -54.9357 | 2025-08-18 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9b2b1ab9-feea-3a21-b89c-5d3aba16adfe | -13.1994 | -50.7806 | 2025-08-18 06:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 15b54e58-2d87-35ce-8975-978a059781cd | -13.2183 | -50.7996 | 2025-08-18 06:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |


[Clique aqui para ver as próximas entradas](README33.md)
