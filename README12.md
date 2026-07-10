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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c95443fd-d373-3e7a-b8a4-5281929e414f | -8.72287 | -47.838 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5926740-35b5-358f-98de-fc9b5006bedc | -10.12349 | -50.18188 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54d9d042-45f4-3dd4-8609-1a31a86c13b4 | -10.4011 | -61.21405 | 2026-07-10 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e2cd3d0-0983-3c19-a6f1-58eb9225cedf | -7.90738 | -55.42591 | 2026-07-10 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c976286d-5e3b-3ba4-a137-286fbde3986c | -11.28008 | -55.79496 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa13c0b3-d68b-3cd6-9dc6-56e32c5e6f5a | -7.90683 | -55.42971 | 2026-07-10 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2397345b-3b23-3170-93ec-1b5a2d52c305 | -11.47487 | -52.92212 | 2026-07-10 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48310d45-0cce-30b2-a6f4-86478d49b656 | -8.72366 | -47.83145 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa227864-c376-36c2-beb8-e968dc357cbf | -8.03302 | -47.42115 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31f88055-70c4-3e84-bd00-e43e2e6231ab | -6.55541 | -55.16 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2a00cf8-0486-3ad7-9c87-82df632451a5 | -11.46923 | -52.92464 | 2026-07-10 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9cc6451-c53a-36fe-9cad-20f1d8994f8a | -11.27638 | -55.7902 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 063b5f16-0501-39b1-92c1-b6a909105947 | -6.57158 | -55.14624 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9a0d5b7-a274-3cf7-b621-35740b0ca438 | -11.27694 | -55.78609 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68385aa1-5da8-3cd0-aae4-f64f77dd7671 | -12.45647 | -49.58098 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43f679e9-3cb2-36d3-b26c-8263345f8a1e | -10.12951 | -50.18192 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34593158-40d5-3ac9-a403-c1112dd6a330 | -9.26449 | -59.81001 | 2026-07-10 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601b0113-24c6-3b09-a8e3-70cd706d716f | -8.72269 | -47.84291 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93967437-d3e7-31df-bdd8-3a736300460f | -10.40165 | -61.21055 | 2026-07-10 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bce1c9b5-e993-3f92-9ec6-1690b7f61731 | -8.52601 | -54.75806 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc48d4c-d918-3902-b5b0-fa224967e63b | -9.09608 | -59.40011 | 2026-07-10 05:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a87b0e-f1c5-322c-9605-aa90ee9c6a20 | -11.48633 | -52.92136 | 2026-07-10 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbe4e04-f93a-3d20-9735-7fd99819cf3a | -6.42301 | -55.79493 | 2026-07-10 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04ffad2b-8b1e-3a7e-a267-bddc52c492d8 | -8.03661 | -47.42859 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9943f655-413d-378f-91f5-a6d6bd3708b3 | -12.45583 | -49.58672 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11bd8c5d-f106-394b-8ceb-fa01c6d9a5b1 | -10.40441 | -61.21458 | 2026-07-10 05:27:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5b6686-f144-3070-a370-8275ac898049 | -10.39249 | -56.76565 | 2026-07-10 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c2794dd-d663-34ca-a659-4a317c01e5e0 | -6.56488 | -55.15367 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c17d23a-2eab-3607-9fd6-24412533f2d2 | -12.45034 | -49.58508 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c517a73a-562e-3cb5-95ab-8c2d49f3f660 | -8.50452 | -48.06403 | 2026-07-10 05:27:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16fec9a1-d9bf-3a21-a4fe-bce70359f614 | -12.44929 | -49.58591 | 2026-07-10 05:27:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8158a603-3059-3649-a24f-398611a7b775 | -8.03916 | -47.42909 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07c4b438-1443-3770-a889-97ae910e4bbf | -6.42648 | -55.79899 | 2026-07-10 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27231ba6-11c6-3645-abc7-34fb47bef2b5 | -8.49879 | -48.06506 | 2026-07-10 05:27:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d87b5f96-a1bf-3082-8774-d4daf0162078 | -6.57214 | -55.14238 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26749525-4d0d-3026-a5cc-208ce5359063 | -8.12856 | -47.8738 | 2026-07-10 05:27:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6e22192-fd8c-3766-b86b-5f4d0edc45f1 | -8.72354 | -47.83622 | 2026-07-10 05:27:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bb50f5c-02b7-3e0a-b45e-1d6427365c04 | -6.55655 | -55.15236 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59185da-3104-3b35-8ceb-1b24d0670154 | -10.12277 | -50.18594 | 2026-07-10 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c6dfcfd-f057-3a14-ac69-f30a57ff1806 | -11.2721 | -55.78959 | 2026-07-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c23146b-fe28-3bbd-bf51-aecfd57e9cc5 | -8.50371 | -48.07027 | 2026-07-10 05:27:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba1e9ea9-179b-3c10-911a-d86c8d09734e | -6.56071 | -55.15303 | 2026-07-10 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b24b4e90-be6e-3cd2-b104-f5df674e2fc9 | -12.1661 | -59.76088 | 2026-07-10 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e4fe3a44-b8ee-3af0-8a98-1813f3c7571c | -18.02769 | -54.35588 | 2026-07-10 05:29:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3af7145-bd69-35d5-ae14-ce9df002a0a5 | -13.36751 | -54.37364 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 372317ec-61f4-3cac-ad9f-f7c0cc69e363 | -13.37305 | -54.3689 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73518809-a503-312b-9a09-13dacdcc9d96 | -13.60461 | -56.599 | 2026-07-10 05:29:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0209b12d-ce43-3fae-aeab-361dd84857f5 | -12.84971 | -58.31181 | 2026-07-10 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5252a00a-b1d4-398a-a77b-e1a6a0b9c76c | -17.5358 | -53.99801 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01bce2ca-28cf-31b8-8b8f-2eb56253adc1 | -18.02695 | -54.36234 | 2026-07-10 05:29:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bee45ec-cf23-3806-bf6c-c2030d078808 | -17.53986 | -54.00724 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed62c37-2949-3a83-b472-ed513510b26c | -13.37237 | -54.37429 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73a78f86-562d-3e2d-a7b8-7a2c1a7bc10e | -13.35913 | -54.36155 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d413e831-2126-3b94-8173-12aba10095ae | -17.54055 | -54.00084 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1feaa86-7055-3674-9637-e1d0358d8721 | -13.95439 | -53.90754 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b1b53f-6e6e-3938-8573-79df137ce1f5 | -13.95405 | -53.91039 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 018d72cf-e2d5-3a86-b11c-39acee619ad6 | -17.53507 | -54.00439 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c6cb852-1939-3c38-b719-6f0ff4d64cca | -12.85036 | -58.30727 | 2026-07-10 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cb24bf5-749f-3148-808c-12795d0ccfe5 | -15.66579 | -56.06928 | 2026-07-10 05:29:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 03dd39a6-db79-3714-b056-a4bb6a98c867 | -18.02732 | -54.35911 | 2026-07-10 05:29:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4073639c-fd23-3cab-a35c-d8d1b93fc6a5 | -13.36265 | -54.37297 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20fdcdc1-cdfd-3200-86b1-f6b2ec0e0b4b | -17.53999 | -54.00815 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b1371b6-1854-3394-83b2-931c87378a29 | -18.02658 | -54.36552 | 2026-07-10 05:29:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24876503-8ef2-3fbd-a946-9c9dc3ed38fd | -17.54072 | -54.00178 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8e90a0d-49b2-3e74-83bc-f9db0032bbf5 | -17.5402 | -54.00406 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e79fb476-570e-3cb4-96a1-565677ec1487 | -14.14753 | -52.88132 | 2026-07-10 05:29:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6359f8c8-e111-326f-baf2-2792e06387f6 | -12.85345 | -58.31236 | 2026-07-10 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95bfec4a-4a13-3377-9e8e-37526aa6fe63 | -17.54035 | -54.00499 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 165f41e3-8433-3837-b5f8-83820fb6f9f2 | -14.09201 | -59.45518 | 2026-07-10 05:29:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed9440bc-e7a6-314f-98f1-1669cccb5e7d | -13.36333 | -54.36758 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c302882c-08cf-3222-989c-ccf01a3491b8 | -17.53544 | -54.00121 | 2026-07-10 05:29:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f8f6774-9cb9-3605-94aa-b07460021f40 | -14.14709 | -52.88498 | 2026-07-10 05:29:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2249ee14-a3cb-34e4-9149-a00980c5a4cd | -18.02622 | -54.36868 | 2026-07-10 05:29:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4846288f-d8b0-32c3-b4e6-e4fc09714155 | -13.36818 | -54.36826 | 2026-07-10 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a3ac444-9d5e-3fd0-bb61-13c6dd4ad61a | -21.76335 | -56.30368 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff62ae62-ff36-3967-a293-f575871ee447 | -21.10116 | -57.46837 | 2026-07-10 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70352dd1-cac7-3150-a80e-365c04683708 | -21.76813 | -56.30428 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06ab4a3b-8ff4-30ce-9bbd-f2ab003688d0 | -21.76392 | -56.29823 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d48630e6-08c6-3d18-b10d-64fa225aaedb | -21.09688 | -57.46547 | 2026-07-10 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a88d9ec8-a5ac-316a-aa36-37879ce4b72f | -21.76407 | -56.29636 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1611450-e318-38d4-87e8-bec66d3afa69 | -20.18415 | -55.39686 | 2026-07-10 05:31:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebb34372-6835-37e8-b4d5-b2d924df1496 | -21.09677 | -57.46777 | 2026-07-10 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32c08dde-f1ca-3424-a375-c6bee1c487d9 | -21.76824 | -56.30239 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8e9769e-19fb-3cbd-bf29-3819b0bad5d5 | -21.76886 | -56.29691 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84e3fb32-c97a-3b28-a621-b7429d24d84b | -21.10127 | -57.46608 | 2026-07-10 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa5b706c-ea74-359e-b5c1-3d018899cdc1 | -21.76871 | -56.2988 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a060ff9-521f-372a-982c-0adaf3ddee32 | -21.76345 | -56.30182 | 2026-07-10 05:31:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 678a7953-5d26-39ee-a413-0cded9c894e1 | -8.74129 | -71.18582 | 2026-07-10 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b42eccda-1291-3bf3-814b-aa0632c777b2 | -8.74071 | -71.18973 | 2026-07-10 06:14:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f502ca23-8a72-3189-9c94-ee128fd97289 | -6.08098 | -43.99731 | 2026-07-10 06:37:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cb4cca68-6a09-3c81-9711-7c0c89a72966 | -4.34092 | -47.76643 | 2026-07-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b0f7f790-f017-34c9-b525-a9ac38934bb8 | -6.0792 | -44.00984 | 2026-07-10 06:37:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 261e99cf-158c-3f02-9429-56d6de597558 | -6.49749 | -42.20243 | 2026-07-10 06:37:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| ca6fd49e-0e5f-38b3-9e4d-5c60d4741d8c | -6.50383 | -42.21053 | 2026-07-10 06:37:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 7c2919a3-d2bc-3a93-8960-f1d20ae4ab34 | -13.75853 | -46.26612 | 2026-07-10 06:40:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0b5ffbf7-be18-36da-a116-74d072158201 | -12.44625 | -49.57341 | 2026-07-10 06:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3978e24-118a-3114-907c-8140be79ceae | -12.35229 | -47.41887 | 2026-07-10 06:40:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c899812-9384-343f-a4b8-066e113e462e | -12.45367 | -49.58378 | 2026-07-10 06:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 08f4cc61-5e20-37d5-a202-75a87fb0dd9a | -12.45505 | -49.57478 | 2026-07-10 06:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4ec0e543-208d-363d-8732-901ae1ca3052 | -8.135 | -47.86972 | 2026-07-10 06:40:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README13.md)
