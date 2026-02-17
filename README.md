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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de4a9e22-3edc-3f6d-82ba-0676d98afb7f | -20.3118 | -49.581 | 2026-02-17 00:00:00 | GOES-19 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 79.6 |
| ddde42e8-921e-3ddf-9aa0-656f8878150f | -20.3118 | -49.581 | 2026-02-17 00:10:00 | GOES-19 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ed83872a-ad80-37fc-960a-b9e205c4cf86 | -21.15005 | -48.59245 | 2026-02-17 00:24:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| eb1e8735-d7f1-3d65-910d-05e3d0f50eb0 | -22.784 | -49.36111 | 2026-02-17 00:24:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 800602d2-3bf2-3596-a224-6273a271dfc5 | -16.03175 | -41.18943 | 2026-02-17 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| def7c717-0cd6-316f-8662-204e7aef2c32 | -21.52682 | -48.79866 | 2026-02-17 00:24:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c73dbd6f-14a1-32da-80c2-7901a906e362 | -15.44234 | -43.64318 | 2026-02-17 00:24:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 6433b35a-e570-3e9e-8c79-4753cd7651c9 | -20.3068 | -49.59553 | 2026-02-17 00:24:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f56a8957-b8e8-3e14-9b4e-a26ca800e913 | -20.78251 | -49.57804 | 2026-02-17 00:24:00 | TERRA_M-M | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1c311f42-d6cf-3d7b-a391-5d9dbcb1c6e5 | -20.51544 | -49.86783 | 2026-02-17 00:24:00 | TERRA_M-M | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| afa9d468-3c9b-3583-9509-b3dab53fd4e2 | -20.3055 | -49.58536 | 2026-02-17 00:24:00 | TERRA_M-M | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 89.6 |
| bdf14db2-53b2-3927-b1c2-028912bfc2e5 | -21.52812 | -48.80853 | 2026-02-17 00:24:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5733160f-a998-3008-8aa9-c3f21b8c9337 | -16.65875 | -41.9682 | 2026-02-17 00:24:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 959baa3f-9d00-39f3-8506-0b5a9d34aca7 | -13.43786 | -48.22318 | 2026-02-17 00:24:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38c49d29-c6b9-31a6-bd5e-212d7f7ac3e2 | -16.0256 | -41.19546 | 2026-02-17 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| ca3c3b8d-9376-36e0-bff7-0e3839527fb0 | -21.78499 | -49.82601 | 2026-02-17 00:24:00 | TERRA_M-M | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| e27c1e7b-5064-3b22-a70c-e7a5ca5cf6fc | -16.60682 | -43.35762 | 2026-02-17 00:24:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7ede5193-276f-32aa-876c-82bfd965bfd2 | -18.97651 | -52.925 | 2026-02-17 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ae6ae361-02ea-3ab5-9342-7ad7b0237a92 | -21.37412 | -49.1073 | 2026-02-17 00:24:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 03c3ca1a-4a5b-3598-b955-d196b908fb63 | -21.78631 | -49.83679 | 2026-02-17 00:24:00 | TERRA_M-M | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 100cfb19-9024-3c28-9f8a-c04a746e2530 | -15.17052 | -45.64777 | 2026-02-17 00:24:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e565dfcb-f77d-3864-831c-4362d54f0cd7 | -16.02162 | -41.1725 | 2026-02-17 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 02846fe5-022e-393e-b5f7-518c85e03891 | -16.01792 | -41.19125 | 2026-02-17 00:24:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 5c5414f9-d494-3d66-be36-204a5c9e0eb0 | -22.78534 | -49.37175 | 2026-02-17 00:24:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 996a9923-ef98-3018-91f2-116d22ea80f2 | -16.6464 | -41.97268 | 2026-02-17 00:24:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 7c1bf1af-574b-3e86-aee3-ec99cfc18993 | -18.97821 | -52.94002 | 2026-02-17 00:24:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7f9e7484-712a-3127-8f05-cadfed8f3053 | -11.19564 | -43.56025 | 2026-02-17 00:26:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 456fef6c-0b8d-3643-a716-d3347b262852 | -11.05197 | -45.39028 | 2026-02-17 00:26:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1de6e4f1-3476-31e7-9d4c-69ae3841b50f | -11.94078 | -44.80682 | 2026-02-17 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 279b478d-d813-3831-b763-1ee8c51d9e38 | -10.92703 | -44.66432 | 2026-02-17 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 19dc9c8d-1aef-3b23-9726-00e8ee42a40d | -11.88979 | -45.29904 | 2026-02-17 00:26:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9d899743-94e2-3e50-885f-449e45c0ca04 | -11.8877 | -45.2854 | 2026-02-17 00:26:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| cfec7803-41db-3660-8005-4ee5d2906eda | -11.94117 | -44.81314 | 2026-02-17 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fef9225b-a231-32f7-ad20-469fa24fb8a5 | 2.66424 | -60.15368 | 2026-02-17 00:30:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 742857ec-6ae1-3dec-81b9-c6828c580852 | 2.90087 | -60.9191 | 2026-02-17 00:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ea799def-055a-3c85-8594-bce6b4350c78 | 1.06032 | -60.57993 | 2026-02-17 00:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e50a9214-5e96-332d-83f6-d06ace150d57 | 1.06431 | -60.55239 | 2026-02-17 00:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 20eeb8f9-46b6-3471-b848-c41edd502a84 | 2.6557 | -60.17049 | 2026-02-17 00:30:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| b4818ab9-c665-3547-b546-00facee2d83c | 2.90082 | -60.91257 | 2026-02-17 00:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 5c42d9eb-cd58-3e69-ac5d-a543c5a8be4c | -20.2992 | -49.569199 | 2026-02-17 00:32:00 | METOP-B | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04a2f97f-3fac-3ca3-9d58-e18b4e89cbeb | -20.3127 | -49.5826 | 2026-02-17 00:32:00 | METOP-B | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 041a799d-a93b-3a1e-9227-541d8dbef2b1 | -22.793301 | -49.350498 | 2026-02-17 00:32:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b18b338e-cda5-38c2-a08f-82480ceffdc4 | -21.525999 | -48.794601 | 2026-02-17 00:32:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a68fc93f-23d4-3e78-ab89-1dcf9dd1b4db | -18.9734 | -52.912998 | 2026-02-17 00:32:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dcae582a-1ddf-3a56-bdd0-6ecb0a3699c2 | -21.1562 | -48.588001 | 2026-02-17 00:32:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f30b336-3fd2-3283-8943-10c439ad05b3 | -21.7845 | -49.822498 | 2026-02-17 00:32:00 | METOP-B | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86fdba9e-d9c5-3d93-9576-ac121403e8bf | -21.1542 | -48.579498 | 2026-02-17 00:32:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cb82f25-c35a-3d9c-8cc1-c9df5e953db8 | -20.5221 | -49.8624 | 2026-02-17 00:32:00 | METOP-B | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b01c8dd3-0de0-38b0-b302-23d05d8aeb47 | -20.7854 | -49.569099 | 2026-02-17 00:32:00 | METOP-B | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f85b06d4-d54a-350f-8465-2083121439e4 | -16.6502 | -41.941502 | 2026-02-17 00:32:00 | METOP-B | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72763185-9126-3fdc-ac44-23a65a161d07 | -21.144501 | -48.5821 | 2026-02-17 00:32:00 | METOP-B | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d70fbf6c-a031-3c75-9781-685bf3f65688 | -21.7827 | -49.814701 | 2026-02-17 00:32:00 | METOP-B | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b676e9cc-cf83-3605-aef6-760d22aea758 | -20.5203 | -49.854599 | 2026-02-17 00:32:00 | METOP-B | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ec0aeb07-a97c-3941-8431-fe5d9a583aef | -16.012199 | -41.147999 | 2026-02-17 00:32:00 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c86c3895-c95f-337f-a9a2-4437bc0fe64f | -18.975 | -52.9203 | 2026-02-17 00:32:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bda72ebb-6011-31ca-af76-7f6f18ca2b48 | -11.8844 | -45.276798 | 2026-02-17 00:32:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b28e35c6-73dd-3980-9eda-ce1b4bd9d758 | -18.976601 | -52.927601 | 2026-02-17 00:32:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2433796a-e839-338c-8de3-1d89047ab557 | -20.3011 | -49.577202 | 2026-02-17 00:32:00 | METOP-B | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff8d202-335e-3296-b3db-42535f3e32df | -22.783501 | -49.3531 | 2026-02-17 00:32:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c550669d-8f7a-3364-8eb5-d4c36ded232f | -11.8798 | -45.258701 | 2026-02-17 00:32:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d20029ac-7bd6-300c-9719-29fd1eb09fca | -21.191099 | -48.560398 | 2026-02-17 00:32:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d88e9791-f09f-34f6-b15a-b548a550f376 | -20.309 | -49.566601 | 2026-02-17 00:32:00 | METOP-B | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f195f0b2-fec6-33b9-b896-c00f571c3ff7 | -20.310801 | -49.5746 | 2026-02-17 00:32:00 | METOP-B | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| deb17a0a-0bb3-3270-a27d-4c5b73f16acf | 1.0663 | -60.5606 | 2026-02-17 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2171924b-39cd-3bfa-ad95-88955d74d258 | -16.0332 | -41.1809 | 2026-02-17 00:40:00 | GOES-19 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 61f0a135-d123-36e4-9b2f-ba5f900e48b6 | 1.0663 | -60.5606 | 2026-02-17 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7e778bda-ee85-3d4a-ac5b-bb11f1fbd51f | -22.7953 | -49.360802 | 2026-02-17 01:08:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7f28a339-0715-38d3-be56-9c2e9307f0f4 | -20.3092 | -49.5811 | 2026-02-17 01:08:00 | METOP-C | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9889e12-82aa-3c8e-a6f2-14a4635a9e46 | -21.7869 | -49.8255 | 2026-02-17 01:08:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 038bcc61-d685-36ee-b1ad-93f89b6dd238 | -22.7836 | -49.3549 | 2026-02-17 01:08:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 042dc49a-a8b6-3f97-9983-c2d0d9612911 | -18.9786 | -52.928902 | 2026-02-17 01:08:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 35815f02-b691-3ec3-a5de-c2019e2b8b24 | -18.976999 | -52.9216 | 2026-02-17 01:08:00 | METOP-C | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 004debdf-7f1d-3d10-b28b-6f7989ebed99 | -21.784901 | -49.817101 | 2026-02-17 01:08:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8691d51e-b91a-3198-8898-16a3e37c9f0c | -20.3071 | -49.5723 | 2026-02-17 01:08:00 | METOP-C | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e5c6e381-f823-32f8-8c21-ba89a6f3584a | -22.793301 | -49.3522 | 2026-02-17 01:08:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c75118f7-b67f-37d0-a9d4-8becec0e1a46 | -20.5208 | -49.8582 | 2026-02-17 01:08:00 | METOP-C | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 96f2edac-a4a4-3530-b9e0-48136094372f | -21.1565 | -48.590099 | 2026-02-17 01:08:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbdf692c-30d1-39c4-b303-f846ca52afa4 | -9.9497 | -36.2836 | 2026-02-17 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| ac57c281-038d-3b1e-acd8-3b63e6de3a20 | -9.9502 | -36.2566 | 2026-02-17 01:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 545f2fb0-a3ac-384e-a1b5-6cb07f38887f | 1.0663 | -60.5606 | 2026-02-17 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5c0d383d-cedb-301b-bd83-a147207cc5e7 | 1.0481 | -60.5796 | 2026-02-17 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c4213bd4-412f-3075-bde0-143595243307 | 1.0663 | -60.5795 | 2026-02-17 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c254a28e-b6ab-3a5c-89fb-200e12118dbd | 1.0481 | -60.5607 | 2026-02-17 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bb6fa95d-27ce-3e81-be85-ae9d3040b694 | 1.0481 | -60.5607 | 2026-02-17 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9c8cc519-4df9-3433-bd45-e0864ac66c0b | 1.0663 | -60.5795 | 2026-02-17 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4107e03f-e6f9-3de4-a57b-a830f3888b51 | 1.0663 | -60.5606 | 2026-02-17 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b01c32f1-1781-3716-81c2-806b5f77c39e | 1.0663 | -60.5606 | 2026-02-17 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 72b16f02-9e90-3650-a3cf-e369c49768d5 | 1.0481 | -60.5607 | 2026-02-17 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e19d92bd-23c4-36db-898d-191e698f1e89 | 1.0663 | -60.5795 | 2026-02-17 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5a4764aa-23ff-396b-9ec0-79525d996abd | 1.0481 | -60.5607 | 2026-02-17 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 52872b76-8160-366d-a291-18f89ab85d11 | 1.0663 | -60.5606 | 2026-02-17 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 54f4a098-8671-3e5d-8f9f-301258796207 | 1.0663 | -60.5606 | 2026-02-17 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 317ef0a8-a763-3745-8c67-ce1b979bd680 | -6.5631 | -51.1126 | 2026-02-17 02:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 90bd07e3-7d3b-309e-8ed8-89ce7df5f577 | -5.09193 | -37.59719 | 2026-02-17 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42105933-3b20-3d1c-9c78-3f71fce4a4d3 | -9.41799 | -35.53539 | 2026-02-17 03:04:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bb5f3c05-dada-3d0c-be38-06392d1431a6 | -9.41877 | -35.53125 | 2026-02-17 03:04:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2c4062ea-8d71-34c5-9b77-f77727b3140c | -5.09068 | -37.60413 | 2026-02-17 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 79365797-e3c6-39cd-994f-0183f01c2f76 | -5.09383 | -37.6027 | 2026-02-17 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d01bddeb-271d-3d2e-9e9a-32b4fd2041a6 | -9.41215 | -35.53414 | 2026-02-17 03:04:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e08d3c3-67d6-3626-b88b-5ad4128a8bcb | -5.08672 | -37.60144 | 2026-02-17 03:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README2.md)
