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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9e21089-0421-3181-8715-dd1de5d0bb56 | -14.23345 | -46.11401 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 58e2cd1a-9e4b-3692-bf08-884ec5c4156b | -13.1828 | -47.80415 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f357779d-09ec-3dc8-9112-ab1bbca5e745 | -15.25092 | -48.18153 | 2025-10-02 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 538300b8-df72-34bb-9cbe-b4232c59143a | -17.57766 | -44.2421 | 2025-10-02 12:38:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 176dfb19-aacf-3353-864d-47708628665d | -10.87117 | -47.80587 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0adadd95-0bdb-382c-8719-f6b20bd5e0e0 | -14.47989 | -48.40814 | 2025-10-02 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 33d5bd5b-ac98-3dff-9ad6-0a9f257fe11c | -14.41786 | -46.15328 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a8739be1-9316-32dd-b481-d5b2852073f7 | -13.18516 | -47.78516 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 62e2c9a3-05f8-3744-9344-bac707bdd6d2 | -11.83162 | -45.03348 | 2025-10-02 12:38:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 8a8b9584-72a7-312a-b626-109e01704663 | -12.42172 | -45.02848 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a97541b7-277b-36da-878b-de626d454b2e | -15.26003 | -49.31806 | 2025-10-02 12:38:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 15715ba4-fc01-3785-819a-4307806117e7 | -13.56551 | -48.21529 | 2025-10-02 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d84548cc-0052-31bf-a918-5525b4680e60 | -11.1753 | -47.28034 | 2025-10-02 12:38:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| e5d8fd00-c4c3-34c4-b686-a2faccf4522d | -10.87731 | -47.75753 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ef439eb6-0040-37d0-94be-b34d65c6fb1f | -11.20888 | -48.20878 | 2025-10-02 12:38:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 692dc019-81fd-367b-a8b6-0e5b4d972172 | -13.21952 | -48.51741 | 2025-10-02 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9bfab010-ab61-3dcc-be7b-1c1ff20b2f32 | -12.20072 | -47.80046 | 2025-10-02 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4a2d23ef-879e-3878-b697-56cd8203e554 | -13.37976 | -47.27673 | 2025-10-02 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b5cd56cf-1c2d-3619-8d37-1c5776e1227d | -11.56107 | -47.00789 | 2025-10-02 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1aac6920-43f6-3a4f-863c-200da6823b9d | -14.22849 | -46.09504 | 2025-10-02 12:38:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3c73c613-d41f-37af-babd-2bb7ece06cae | -14.37796 | -45.9463 | 2025-10-02 12:38:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 9185c379-1115-3836-b8f9-9c2b60f99d2c | -16.03815 | -50.90379 | 2025-10-02 12:38:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| feccedc1-8486-3de2-8b45-9cf0ca2b24a6 | -12.98677 | -44.57658 | 2025-10-02 12:38:00 | TERRA_M-T | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a29ba695-981e-3c94-ad2c-fb462c4c8d8b | -14.84573 | -47.21386 | 2025-10-02 12:38:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 047c324b-2c8a-3980-8029-c15d3dee02ba | -11.84799 | -47.69603 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 98c6047e-f356-31bf-98a1-e09d4a73fa21 | -11.84355 | -47.70134 | 2025-10-02 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| e85943cf-da9e-3c7f-8ace-520e719fa7ca | -10.97191 | -46.67905 | 2025-10-02 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 4529e562-a3b8-3530-90b4-43e0d32e4734 | -11.10494 | -47.85353 | 2025-10-02 12:38:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 852a184b-290f-347d-90af-832a4dd633b9 | -13.0088 | -45.19472 | 2025-10-02 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 642406bb-1a77-3a57-8843-4179e53bf49f | -16.0221 | -50.8989 | 2025-10-02 12:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b08b9298-603d-3b24-993d-4bf99f6c515b | -10.9367 | -46.6843 | 2025-10-02 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 617c8e3a-c5a3-3f5f-bcc7-34951482732f | -11.9085 | -47.8745 | 2025-10-02 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| b9724980-c8a2-3ea3-ba6b-e81ef5dfeb08 | -8.5204 | -47.8167 | 2025-10-02 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d6a0b6e6-7fef-312d-bafe-f0dac1a90658 | -10.212 | -48.2128 | 2025-10-02 12:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| beb50b15-e2cf-3585-bb96-49af5025b27f | -9.336 | -45.9305 | 2025-10-02 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 188aab0e-11ad-3af9-96cc-52d0798977d2 | -14.4947 | -48.4329 | 2025-10-02 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9fd7d483-0496-3b18-8a63-25917d1d00cd | -8.5599 | -44.6494 | 2025-10-02 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 255.5 |
| 89436f00-bd34-30b4-abf8-47928d570173 | -13.1928 | -47.8512 | 2025-10-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8ca7b4db-e1ca-3bcc-8123-1bd90f73d79c | -7.7755 | -42.5152 | 2025-10-02 12:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| fbc069d6-3bc1-3df6-9d14-6b2a47c38131 | -9.08 | -46.7215 | 2025-10-02 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| a7b3ad68-b988-38c0-9a94-6190abaebb28 | -9.4083 | -47.5742 | 2025-10-02 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 196.6 |
| e7d6ead9-eca3-3334-a5fd-fcb7918c098e | -7.8882 | -47.281 | 2025-10-02 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 898a7d91-7766-3d8b-9b47-e48031c09b01 | -13.1743 | -47.8093 | 2025-10-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c0c10d42-909a-38a2-befb-4c1c822636ce | -7.8879 | -47.3031 | 2025-10-02 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9ddb0d39-c0b3-3fcc-94ea-5320a0bae88d | -9.9567 | -43.6927 | 2025-10-02 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a07dafc7-1b35-3c90-85ae-f9cf776b8347 | -9.9372 | -43.7187 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 066608a4-8d63-3307-94d5-c1a56bf9b307 | -12.902 | -46.9299 | 2025-10-02 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| bc7cda29-3527-398a-81c5-610d88fd4e6b | -9.9182 | -43.7212 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 1551f316-3751-36c5-b40e-be1092a3bd15 | -9.9365 | -43.7657 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 177.6 |
| dac8b9a3-876b-3249-9f6c-25937d119aa1 | -11.9276 | -47.8719 | 2025-10-02 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 375.0 |
| 8d31ba6a-46e6-3d76-ad63-99b59e30b865 | -12.9024 | -46.9073 | 2025-10-02 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6e1c48c9-4735-3406-9bb1-842fbddec71b | -11.8234 | -45.0364 | 2025-10-02 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c140a167-c210-38e4-b015-3e84054ab999 | -7.7752 | -42.539 | 2025-10-02 12:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 232.8 |
| b8f221ce-5a01-33b2-8686-31e25ad085ae | -13.1932 | -47.8288 | 2025-10-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 97057e59-ab98-3151-85b7-1785461ac257 | -8.2105 | -47.0084 | 2025-10-02 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9d8e2546-ebe6-33be-82b5-f63b93a3d7ee | -14.9074 | -47.242 | 2025-10-02 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3c15931c-dc2e-314a-b732-5397ddf78e2a | -15.2738 | -49.3073 | 2025-10-02 12:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1ff90964-8fa0-342b-a9d5-2764556ce93c | -9.0803 | -46.6992 | 2025-10-02 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| cf84cd99-0469-31a7-a3b4-7e414536f70a | -7.7941 | -42.5369 | 2025-10-02 12:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 159.9 |
| 7f1de4ae-48cf-3a1d-b0d2-df6d93ff4f5a | -14.1917 | -46.1552 | 2025-10-02 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 04be092a-5dd8-330a-9924-bd439f04ebd7 | -15.3185 | -46.278 | 2025-10-02 12:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 944fd282-8f6f-380c-9c39-4c4cdeec2a3e | -14.1921 | -46.1321 | 2025-10-02 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 140.3 |
| b6826b03-021f-38ca-a981-0f9e92bb5023 | -8.2094 | -45.5301 | 2025-10-02 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c048cb4b-9808-3757-a7d7-3061f9e290db | -8.8929 | -46.6072 | 2025-10-02 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 1f06667a-0659-3a17-a481-648d14c4281e | -9.3389 | -45.7266 | 2025-10-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 1020be66-7b85-36b0-9a05-d103543b2a95 | -13.3001 | -47.2529 | 2025-10-02 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3ede6392-5281-32c2-b609-c767e2e166f6 | -8.8932 | -46.5848 | 2025-10-02 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8c7ef2f0-6cd1-3516-b8d3-ef8c98a81150 | -10.3061 | -48.2461 | 2025-10-02 12:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6bdb7ba9-8466-3924-b966-890da62b94e4 | -11.8238 | -45.0132 | 2025-10-02 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7f88a745-7763-3d76-8096-5e38966a9596 | -14.5937 | -48.3281 | 2025-10-02 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b7a700e0-9fd2-3665-8999-cb5500e61bdd | -8.6722 | -47.6924 | 2025-10-02 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 19ba8e24-a786-39c6-8a04-b5e554da35c7 | -16.0567 | -45.7204 | 2025-10-02 12:40:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 8e6c26fe-65f0-33d8-ab96-6dda69b31444 | -8.5596 | -44.6724 | 2025-10-02 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7a987d5e-d15c-3d3c-ad8d-fff5870df278 | -11.9272 | -47.8941 | 2025-10-02 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c8279e78-63cc-3100-8e43-122d915b6a86 | -8.6911 | -47.6906 | 2025-10-02 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 95b4e7f5-b116-382b-9da1-a52db663bb3b | -14.425 | -46.1381 | 2025-10-02 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 5275a5af-3552-3161-88f4-62ec024225a2 | -9.9369 | -43.7422 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 5cbac06e-0d9a-3b66-900b-8ae3b88e5378 | -14.4753 | -48.436 | 2025-10-02 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0a594e35-2598-31e7-956f-7174981675d6 | -7.7944 | -42.5132 | 2025-10-02 12:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 33afee07-942a-391f-8118-58f3e34bc751 | -9.3392 | -45.7039 | 2025-10-02 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 24d2a7c0-db87-3243-8fdf-7078b68214e8 | -9.9178 | -43.7447 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 169.0 |
| 307d2034-a641-36c3-8942-4a87c48e10f5 | -13.1542 | -47.8568 | 2025-10-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6cf133b2-ed68-33b6-aba8-1e0fc5a9cb01 | -14.4757 | -48.4137 | 2025-10-02 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 134.6 |
| c816b8b9-6500-3469-8777-504d827e21ec | -8.5201 | -47.8386 | 2025-10-02 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1ac2e768-272e-3722-bae0-101ab7ec8f8e | -12.6729 | -46.851 | 2025-10-02 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 34b5a9d2-6d4c-3387-8bda-64e965eab419 | -16.0417 | -50.8959 | 2025-10-02 12:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| efc47ba1-63fe-3c7e-8780-84c57c2e439f | -9.9563 | -43.7162 | 2025-10-02 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| deb89431-7465-3d83-9d95-39ebe4f74ecd | -9.4086 | -47.5521 | 2025-10-02 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 9887021c-a580-3e90-8294-a011d83b1ebc | -9.4272 | -47.5722 | 2025-10-02 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 3e2aaac9-a703-3de1-9695-415ed57b12c4 | -15.2542 | -49.3104 | 2025-10-02 12:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| c2100f0b-ae7e-3d7c-9e9f-1c7d9d601861 | -13.0119 | -45.1988 | 2025-10-02 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 5d06fa28-f1f3-3c5e-902a-6bf8c52c323c | -13.1735 | -47.854 | 2025-10-02 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2428f10f-df88-3dcf-abb4-212dae37ffe5 | -14.4951 | -48.4106 | 2025-10-02 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3928904f-83c4-349b-ae64-4c331417e02b | -13.0543 | -49.1523 | 2025-10-02 12:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6779146c-ee9d-3c0d-b325-fb48391f1f7a | -18.19475 | -53.29251 | 2025-10-02 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5e1bf1be-4630-30ea-b874-02e80c0f8b1c | -18.19342 | -53.30223 | 2025-10-02 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 014cf90c-7d99-35b9-bb9b-eca0ac695262 | -18.00483 | -49.5964 | 2025-10-02 12:40:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 4fafc577-216f-3bfd-855f-2b38aa6a68b4 | -19.76754 | -47.97422 | 2025-10-02 12:40:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| dff34e18-cd0d-31b5-8351-f90c18677868 | -18.2474 | -53.31007 | 2025-10-02 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 97b927d7-45a6-3ce6-8ea2-7c252765810b | -18.20491 | -53.35217 | 2025-10-02 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 18.3 |


[Clique aqui para ver as próximas entradas](README151.md)
