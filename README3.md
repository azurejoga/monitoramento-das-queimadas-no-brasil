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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8092d3de-293d-3335-9828-8e2cc6f04992 | -9.058 | -45.5313 | 2025-09-28 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 38662baa-c3a7-3de8-b7f1-96e7a2c2775a | -7.7975 | -47.0019 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d09bdcb5-fa34-3117-90c8-7cff8d9d38ff | -7.7787 | -47.0036 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 17d3c5b5-f63f-3c36-b827-0d15de069802 | -22.60921 | -49.03809 | 2025-09-28 00:50:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 39e3b163-d5f8-3f68-a294-dbb080a0c34c | -16.96114 | -53.69495 | 2025-09-28 00:50:00 | TERRA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4beb2123-8ce7-3240-8984-6dab5c1492c3 | -22.94377 | -49.88212 | 2025-09-28 00:50:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 9fffc3f8-9fb9-31eb-8e99-f355de427103 | -14.89132 | -45.55926 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1d489545-f0da-3841-9a4f-b29e53e113d5 | -15.92939 | -59.5211 | 2025-09-28 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 163c1c00-22a2-3b16-aea0-93c85f05c7ad | -18.19004 | -53.32103 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4a35cd4b-cb78-3980-984e-b7106d7f967d | -14.77508 | -45.64952 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 19fcf600-2fa9-3193-be7f-f10310951d38 | -14.76298 | -45.65797 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b6f55b1d-a47d-3605-9fd5-deed36f70646 | -14.89473 | -45.57925 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a131cc10-0971-3469-a621-bdf6bc19b3c1 | -14.93012 | -49.35931 | 2025-09-28 00:50:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5c100014-e113-3018-ac0b-83170688e4d5 | -15.78095 | -50.16617 | 2025-09-28 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 96a4b83b-8195-39fe-ad06-5beac1446a88 | -14.53749 | -48.41102 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 4e3b1595-be6f-3715-a491-d0fdd7104850 | -13.63087 | -44.40741 | 2025-09-28 00:50:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 0f9733d4-ac0f-3b40-b336-74dc77e0699a | -14.48008 | -48.56902 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a73533dc-b851-3428-8000-3dbf583ef622 | -15.96884 | -50.87983 | 2025-09-28 00:50:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8aa0cc64-b692-3785-9026-4106adf1d466 | -15.4417 | -48.22309 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6edabe1a-414c-3769-9783-2b16bb9cc57e | -15.54517 | -47.91165 | 2025-09-28 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1a792a1c-639e-36fa-9a4b-22cc0657e3d1 | -14.79467 | -45.68712 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 85c66bff-f232-3f5d-9b70-ac65fe92647b | -18.18086 | -53.32238 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 28.2 |
| d9dde331-5a52-3b91-9d31-f9156ed42233 | -15.03356 | -46.96304 | 2025-09-28 00:50:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 43234cfa-cf0b-30b8-9bae-912021962d99 | -15.9577 | -50.42269 | 2025-09-28 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 93bc1240-2b67-366d-b5ae-9d0c77b9a604 | -15.81202 | -56.41553 | 2025-09-28 00:50:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 60da383f-c082-3069-b7b0-b39767dbdcae | -15.61228 | -53.16356 | 2025-09-28 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdebc1e1-2ea6-3ee6-a1a8-ee0a9c2dce1b | -15.25445 | -49.41105 | 2025-09-28 00:50:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 323280c4-9449-386c-8590-a8bb5b3759da | -13.63311 | -44.40088 | 2025-09-28 00:50:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 384cc17e-e631-3f77-91db-0ad097db1ccb | -17.72734 | -46.71128 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d0a01484-a8b9-3d52-beeb-bc9848307257 | -14.78844 | -45.65353 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 96c80676-1ac6-3266-a533-423b47b94549 | -15.97792 | -42.00518 | 2025-09-28 00:50:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e5b1368a-dbf4-3a7c-8f66-f850a432e950 | -18.04918 | -51.17931 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e9e81af-9da9-3089-9ca7-e36bc10bdb9d | -15.88739 | -46.20925 | 2025-09-28 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0a2bf564-4f2c-3142-9d08-d777d1069673 | -14.77851 | -45.66932 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 017e9d20-c111-35f7-a54b-8e3eb5aa1d14 | -23.02568 | -49.55587 | 2025-09-28 00:50:00 | TERRA_M-M | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| df6e038d-8768-3e5b-bd5f-aa7aef411300 | -15.21231 | -48.07384 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2189a11-b79d-31f6-a546-c57d9a8491f9 | -18.03775 | -51.16221 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 625.9 |
| ec51a391-f946-3341-a289-885843534dd7 | -17.71626 | -46.71316 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 19115e02-2eb6-3d80-9c93-edf459ec9490 | -17.71655 | -46.70669 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 3325b287-0171-3a32-9d66-d88004377267 | -15.53247 | -47.9 | 2025-09-28 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 94bb084f-d7ef-3c7d-880c-81fa9738851d | -14.76969 | -45.69825 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bab1372e-8646-31a5-a1e8-f1b3370073ac | -19.32087 | -43.81866 | 2025-09-28 00:50:00 | TERRA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5ce8e18d-cd82-3bce-afee-9828caf1ecdc | -18.04036 | -51.1807 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bda1248-0f41-3c6f-bffb-921cd10c84c4 | -15.02758 | -47.13938 | 2025-09-28 00:50:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 92c4cc41-23ba-386c-ab30-7a1fd429cb70 | -17.7249 | -46.69607 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5eb5288c-d47f-38aa-9381-d27c32b62d17 | -15.60332 | -53.16483 | 2025-09-28 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aef03436-986d-3665-a3ce-f1da0d31c1c4 | -15.03011 | -47.1547 | 2025-09-28 00:50:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a908a299-0706-3b5f-9262-ebfc6f19baeb | -18.04658 | -51.16082 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5945cc58-22ad-3d9c-8149-4af811a2d947 | -16.59206 | -50.66203 | 2025-09-28 00:50:00 | TERRA_M-M | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2fc9b2bc-d167-389c-853b-2ab0faea1e63 | -15.92658 | -59.49534 | 2025-09-28 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| aa606325-ffad-3240-a0b0-084e5c2881e4 | -22.35925 | -49.47433 | 2025-09-28 00:50:00 | TERRA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f912091a-d005-3a10-b7c1-5b13a49f1d59 | -15.46194 | -49.62899 | 2025-09-28 00:50:00 | TERRA_M-M | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7e0dde63-81a6-3939-bc16-9c23f7f456a9 | -18.18221 | -53.33283 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fdc7533d-2a41-3a5b-92a0-0c766fbe8049 | -16.26754 | -50.20932 | 2025-09-28 00:50:00 | TERRA_M-M | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 8816fc06-9154-308a-8247-cbb13d0153e5 | -18.03905 | -51.17146 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 365.5 |
| b4850926-0b22-3246-9f2f-e8fb85ce0ac1 | -22.27197 | -50.68244 | 2025-09-28 00:50:00 | TERRA_M-M | QUATÁ | SÃO PAULO | Brasil | 3541703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2dd9ae7b-96da-36da-a2b3-3d00b381f156 | -15.81644 | -46.04294 | 2025-09-28 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d5fe01bc-7bdb-3758-a2a8-3ecefa8e9019 | -15.22283 | -48.07235 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 715f465c-8d3a-3d74-b994-f29320fe8463 | -18.04165 | -51.18993 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71d934ed-af19-3a62-8881-919425b24bd1 | -15.22074 | -48.0591 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ecbfe9a4-6402-3a8f-9d7a-e443a76ad229 | -15.32466 | -47.8924 | 2025-09-28 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca91341d-bf32-3a02-a03e-c9521fba8859 | -14.76929 | -45.6916 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| eae60d85-4b98-3b20-b7d4-15399d2ddcf7 | -15.77948 | -50.15626 | 2025-09-28 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1a9b59c1-1152-3fa7-9dfb-7da2147bd871 | -15.4354 | -48.25053 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 682e81ca-90b4-3ad0-b6aa-bf20ca2ab32f | -18.03645 | -51.15296 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 5e010915-b32e-381e-8971-0aca46b121b7 | -15.93538 | -59.51329 | 2025-09-28 00:50:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| deff9b0e-b80d-3f81-8034-6f702fa9cb69 | -18.29055 | -47.68375 | 2025-09-28 00:50:00 | TERRA_M-M | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c025e061-cd5c-3310-b6d0-fb821a7e4c70 | -13.77668 | -47.8935 | 2025-09-28 00:50:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e3176c45-1b5d-3a52-91d1-85fb0f8656e7 | -22.62838 | -45.00969 | 2025-09-28 00:50:00 | TERRA_M-M | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| f56939e1-adfe-35d5-b782-ab903af5829f | -15.81866 | -41.88443 | 2025-09-28 00:50:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 66cf878e-5209-30bd-97ff-48f04428e1c2 | -15.02899 | -47.14553 | 2025-09-28 00:50:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 11675a7f-09a3-357c-9e5d-ef161e23f2bf | -15.44368 | -48.2358 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| b0429ebf-70c2-3fc7-84df-558a02c97028 | -14.76579 | -45.67146 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d783374e-be43-3a18-b5db-6f1387d3d673 | -18.29258 | -47.69643 | 2025-09-28 00:50:00 | TERRA_M-M | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c625efbb-47ed-3ae2-9ecd-289703cace68 | -17.73012 | -46.71958 | 2025-09-28 00:50:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e606bcbe-77ab-350d-b535-f09d6e975699 | -17.42802 | -45.81599 | 2025-09-28 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 99de3d97-c4f0-3f2e-9d32-564cf1083579 | -14.7878 | -45.64723 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 43fd1e09-720e-388a-934c-d252dec9ee1c | -15.96742 | -42.00018 | 2025-09-28 00:50:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 4ce166de-0cdc-35fe-af39-56f934fd85d8 | -14.77902 | -45.67572 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 68b92284-e7c6-361e-b713-8b50f4fa9887 | -17.43997 | -45.81401 | 2025-09-28 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 34328beb-21aa-3c8a-a532-605fa0555ef1 | -14.79123 | -45.66714 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 13fd2dfe-d75c-3203-b1fe-d784625798c3 | -15.81367 | -56.42939 | 2025-09-28 00:50:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 867ed257-ce75-372f-b013-488cbc412912 | -13.78516 | -47.87659 | 2025-09-28 00:50:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ba6cc951-5b22-307a-9d31-95fd485150a0 | -15.61354 | -53.17294 | 2025-09-28 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 72e48a08-d9f0-37f4-b355-2811b41715ff | -18.04788 | -51.17006 | 2025-09-28 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4257f3a2-0881-3319-96da-e84283fd507f | -15.81364 | -41.8906 | 2025-09-28 00:50:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ef3d0c21-c150-3915-96d7-1f4948b446ae | -15.20405 | -48.47578 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4493ad11-c8c8-3769-8f24-62a6d5891b62 | -18.19923 | -53.31972 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 128.1 |
| f7dd4219-7a6c-32be-b901-00da3f787f6e | -14.58322 | -48.25058 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6dc7edc9-689f-36e7-b889-29433599e097 | -15.94884 | -57.48596 | 2025-09-28 00:50:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b826006b-ada9-341f-9eb9-234fef3cac79 | -22.28679 | -48.79231 | 2025-09-28 00:50:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fe9fcd24-c10d-3bfe-8f6f-d492ce1ef07d | -18.19791 | -53.30957 | 2025-09-28 00:50:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0b4e642a-2f56-3eba-9c6d-1d35135ee784 | -15.43333 | -48.23732 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| bd43dd2a-a650-3ef2-a18e-af6b62f11d49 | -15.61664 | -48.36224 | 2025-09-28 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 22312400-e148-3e0b-8763-0a36f4573b66 | -14.20737 | -44.6002 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1d5d5f7a-f64f-34a8-a457-445d74bb9d79 | -16.26899 | -50.21914 | 2025-09-28 00:50:00 | TERRA_M-M | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 0e120040-ab78-305a-9156-cc323c752a01 | -20.21164 | -48.6845 | 2025-09-28 00:50:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0185838c-44ab-3be7-b9f2-e82d2311abd3 | -14.58534 | -48.26397 | 2025-09-28 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 46194716-9339-30ea-856b-d9124bbfe6e1 | -14.76629 | -45.67788 | 2025-09-28 00:50:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 758726c6-8079-35d1-8d95-778b8d0d2b48 | -22.28832 | -48.80259 | 2025-09-28 00:50:00 | TERRA_M-M | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |


[Clique aqui para ver as próximas entradas](README4.md)
