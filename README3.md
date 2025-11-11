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
| 5b74ff53-bde9-34ed-9d06-eda103aa987d | -2.867 | -45.4182 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 8272d232-8da5-3b88-9d3b-690b59145933 | -3.7837 | -47.7677 | 2025-11-11 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d1bbf391-b01a-34ff-91c2-dd822c935cca | -2.9233 | -45.2812 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 470dc9c2-7ff5-327a-9cf2-8569c1d93be7 | -3.9739 | -43.7994 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7522a6f9-7457-357a-91c4-330c60adf4c1 | -2.9424 | -45.1679 | 2025-11-11 00:10:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 0e798016-5100-37aa-93c5-3b22b1028fa7 | -4.7204 | -46.4497 | 2025-11-11 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 4266c4a4-b1cc-3770-a9eb-7cfd61f250e5 | -3.9367 | -43.7782 | 2025-11-11 00:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| e674414e-b4dd-3046-a703-cdbf86ec02fd | -3.7838 | -47.746 | 2025-11-11 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 82a780d3-f32d-30a3-ab45-7f727e9dbd5a | -3.9554 | -43.7773 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| d5ce8ef3-7cf7-3cf4-9895-749ef91039ff | -2.9047 | -45.2819 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b93c6bd2-4c3a-3e12-ab73-4064d3f3cb56 | -4.7391 | -46.4487 | 2025-11-11 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9f9e0d76-031e-31ed-b411-dabdf945bb1b | -2.8854 | -45.44 | 2025-11-11 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e1df5416-ddf3-3475-93c9-b42181899bb1 | -19.7424 | -58.0465 | 2025-11-11 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 04842758-bba7-30bf-ab00-60083e0ed23b | -9.9828 | -44.4581 | 2025-11-11 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| fcb9c4e9-518f-3be3-b4b8-67dd4bd0f1b4 | -3.9742 | -43.7532 | 2025-11-11 00:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 36d29fc4-e9dd-32b4-ad3a-106ead05ec95 | -11.05082 | -45.41159 | 2025-11-11 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16d9e19d-bf26-3040-a486-21703eec828f | -10.7328 | -41.32776 | 2025-11-11 00:11:00 | TERRA_M-M | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fd6fe10a-bb9b-3a8e-94d5-201dc4d05964 | -15.73087 | -43.4864 | 2025-11-11 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc2403bc-7c13-3447-9726-69cafd00eeac | -10.9413 | -44.01144 | 2025-11-11 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 379282c0-1f20-3123-8da3-1a29aeb62b4b | -11.04056 | -45.40355 | 2025-11-11 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b83c5c28-4077-3838-b4f3-2af70fe0a7d7 | -18.48035 | -53.40657 | 2025-11-11 00:11:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 151647c9-e979-3a10-9bba-ae704bb5a619 | -10.69925 | -44.04982 | 2025-11-11 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 796bdf93-a0e9-3dec-a36e-53d790f5088a | -10.94255 | -44.02041 | 2025-11-11 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 03dacdd0-c872-3dc5-814d-fdd50c74a938 | -18.48146 | -53.40095 | 2025-11-11 00:11:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d4179a92-7f7b-3529-b16c-aa051925e2bd | -16.69815 | -51.84534 | 2025-11-11 00:11:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 5186353f-b4be-324b-9149-f1975abdc721 | -11.16565 | -43.57347 | 2025-11-11 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9efd795-2184-3b68-b562-cd705c5b462e | -11.04955 | -45.4023 | 2025-11-11 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 85cbfb47-52de-3b72-9eff-7dca34b1dc7a | -11.04183 | -45.41285 | 2025-11-11 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0f5d01f-1f1a-3c1a-8489-9a412fd88d20 | -11.17629 | -43.57529 | 2025-11-11 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c8b5e218-e5f4-3dd6-b3cb-eb862a6e7b2b | -5.4202 | -44.65064 | 2025-11-11 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| fbcb2666-0f5c-350a-8393-a01559e05196 | -4.66515 | -42.82213 | 2025-11-11 00:13:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9251317d-b915-3172-98fa-77ef09e21bc1 | -6.33843 | -38.91469 | 2025-11-11 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| bcec6a62-74aa-3166-90d9-1ce14b8ecf4d | -6.44448 | -45.65582 | 2025-11-11 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 15f5269b-f276-380f-832c-9b6e2d70f6e2 | -4.68435 | -45.05013 | 2025-11-11 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| feec48ee-fdd6-39a5-a35f-51bd1bdbaad8 | -10.50412 | -45.0443 | 2025-11-11 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88641877-57fd-371d-8ba9-aaaf55d5ac35 | -9.9795 | -44.44615 | 2025-11-11 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c1779ae9-f781-31f6-a31b-1f4907c4d864 | -9.67388 | -43.89988 | 2025-11-11 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f3453fd7-bd8f-3c3a-9a1c-62a729ba4540 | -7.06829 | -46.04301 | 2025-11-11 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ecde3401-9f99-31b7-a193-5a61d3ba82d2 | -4.64255 | -45.75227 | 2025-11-11 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f26843a5-467c-30ba-b861-5f9870fe1716 | -4.65138 | -45.75101 | 2025-11-11 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efb0fcda-cdf5-33cb-8aa9-fd5cd009e6ec | -5.40194 | -45.24891 | 2025-11-11 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7ebc3d4d-69fe-3b22-b520-1d1c1fcc2669 | -4.67754 | -43.24926 | 2025-11-11 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b4caefb1-9202-339f-aed6-dc7df4b9f497 | -5.18537 | -43.44236 | 2025-11-11 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 180d0215-f1e6-3aa1-907e-f1b0530c7836 | -7.12218 | -45.35775 | 2025-11-11 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21bdaf60-46a0-3d8c-9674-da085e1e3403 | -7.28219 | -45.05197 | 2025-11-11 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8c002cad-d5de-362e-b865-54c23bf8978b | -10.50288 | -45.03524 | 2025-11-11 00:13:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2b24c9d6-2d9b-3de2-8ddc-a38d0e592d98 | -5.12068 | -45.60352 | 2025-11-11 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f86db00e-2eb2-3a49-abca-1f025dbd0254 | -7.51178 | -41.83665 | 2025-11-11 00:13:00 | TERRA_M-M | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8cdacfee-7421-383d-b894-6d667aac61be | -5.63375 | -41.08747 | 2025-11-11 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 51604328-2317-3911-9807-f9967be8c6be | -7.30231 | -45.06716 | 2025-11-11 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a14ae79b-747e-3150-81d6-85f4d749d99b | -4.73944 | -49.52752 | 2025-11-11 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4e498c73-560f-30b5-9d14-c97b3776b823 | -5.89005 | -46.04908 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 763f6e2f-bde7-3119-ae27-6c0ce8c88f81 | -6.97771 | -46.32248 | 2025-11-11 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f4b378e-c30d-362a-bbdb-3a32f37b40f6 | -4.66669 | -42.83294 | 2025-11-11 00:13:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fd4c2687-86b5-3316-9e19-28dd49d5f828 | -5.64068 | -41.05883 | 2025-11-11 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d27fe3c1-3dee-368b-ac6d-9e2d54b462a5 | -7.06954 | -46.05212 | 2025-11-11 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1248e9e3-d06a-308e-bb5c-87f6e1c8b483 | -5.53191 | -47.7404 | 2025-11-11 00:13:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| fb8327a9-edd7-3e2c-91ae-601ebf9ca483 | -3.66492 | -40.90466 | 2025-11-11 00:13:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 593ea283-ffad-3a67-ab5f-8c6382bc2cc9 | -9.18367 | -41.03091 | 2025-11-11 00:13:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 01b1e66d-dff6-3de1-aeb8-86b204688db0 | -6.0708 | -45.81435 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2265f0b3-1c65-3c4c-b805-169a5afec531 | -7.89245 | -42.47264 | 2025-11-11 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 60d537a9-7609-3bd7-9d77-59d9dba96f23 | -5.42852 | -44.84106 | 2025-11-11 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 32b2c5bb-99ab-363d-af95-8e463722c4a1 | -4.90437 | -44.31953 | 2025-11-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3630d710-7d88-3661-b704-8345cd8afbbd | -3.85402 | -41.58112 | 2025-11-11 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 9b6af20b-e93b-3eff-b39d-fc89b53d92c3 | -5.64091 | -43.92149 | 2025-11-11 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0af8f387-2065-37db-8187-2d554f258e8d | -4.99974 | -46.87293 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 2490c071-bc13-3cb3-873c-c49c410a5589 | -7.89779 | -43.91986 | 2025-11-11 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb1aa18d-59a0-382e-9cff-4af2954510de | -5.11946 | -45.5947 | 2025-11-11 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 017c3414-ca7f-37dd-8a09-bcae6762dc7c | -6.33873 | -38.9211 | 2025-11-11 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| d6b3ea91-f16c-3c8e-bb73-139bacd12669 | -5.40497 | -46.00206 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bccce584-733c-340b-bde9-fe6fb5fb990a | -7.59764 | -43.68432 | 2025-11-11 00:13:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8566708d-a3e0-3860-8deb-731700421716 | -9.98074 | -44.45507 | 2025-11-11 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c2eaacf1-1951-31d8-b0b3-2a75f88902eb | -5.41964 | -44.84232 | 2025-11-11 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a1b457a4-14d0-39d4-ab16-995c541030f8 | -10.63219 | -45.24183 | 2025-11-11 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbca4daa-03b5-3d9d-809e-191126370a52 | -3.97255 | -43.78307 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1478b697-d2b7-3d32-aebe-e74243dc51c0 | -5.1283 | -45.59346 | 2025-11-11 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e9e922bf-abbc-3bc7-b619-703b6003f532 | -4.31158 | -43.20055 | 2025-11-11 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae343baf-256a-38be-b79a-328124a29c70 | -7.03397 | -39.75825 | 2025-11-11 00:13:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 22e13e4b-fa8e-3df1-bd77-0d2d282de43c | -5.90838 | -46.24794 | 2025-11-11 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8e552cfa-b2f5-3c2e-b3ef-05340337b9c5 | -4.90565 | -44.32872 | 2025-11-11 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 25a5f1a3-4b83-35d8-ade1-5c8b1cb09f89 | -4.72158 | -46.456 | 2025-11-11 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8b2b42c6-7dea-336e-a46e-50616947fd34 | -6.54657 | -44.46539 | 2025-11-11 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0c62d1c-f2d9-3295-bc20-47ee39c077c3 | -10.21837 | -44.04684 | 2025-11-11 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dcca8b47-4b71-3eb3-852a-6732e5e4b76e | -4.54289 | -46.02439 | 2025-11-11 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b7af185e-e775-390d-a4a7-4cac6f3b36c7 | -5.63179 | -41.07399 | 2025-11-11 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 90f34441-d0dc-3414-aa7a-47c018484e37 | -5.80963 | -43.94233 | 2025-11-11 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c095960d-8f2d-3a42-98e5-5306294fc3a1 | -7.54544 | -43.64122 | 2025-11-11 00:13:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6ba6e89a-4771-373b-bbd1-fb8220611d49 | -6.75141 | -44.21476 | 2025-11-11 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e33cc50-b9d5-3c5a-a7c8-b0c1f1bc3b6a | -4.82593 | -44.74438 | 2025-11-11 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 43c91fb5-ae73-38b0-931c-1169efc90c8d | -6.09191 | -41.56507 | 2025-11-11 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f1057c31-55e4-3ccb-ab86-f6715a919a98 | -3.96188 | -43.77458 | 2025-11-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 9e28c632-7982-3b2b-8754-316a02656728 | -4.91466 | -44.32738 | 2025-11-11 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4020ad44-0531-3715-a0f5-a3ec99523ad4 | -5.12952 | -45.60227 | 2025-11-11 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8486c637-34ce-3aa8-97f1-9690d79286e6 | -5.77589 | -44.02944 | 2025-11-11 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ee6bb606-c8b4-3b15-a62f-8d3b96a50712 | -7.89398 | -42.48305 | 2025-11-11 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 9fdf00a0-f503-3720-bb85-edc37afc8c1d | -6.4736 | -43.23009 | 2025-11-11 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 542eb13e-d62f-36bc-b69b-8ab0cceeb921 | -4.69064 | -45.69473 | 2025-11-11 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e25fc5f1-cbc7-389d-9330-c5691ca1f6d1 | -6.37531 | -44.03234 | 2025-11-11 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6429b211-cbe0-303e-a8cc-c6b9d8bd86c8 | -5.4409 | -44.66005 | 2025-11-11 00:13:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 760dbdbe-9776-371d-ade7-4ca04b808674 | -5.38007 | -46.35835 | 2025-11-11 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README4.md)
