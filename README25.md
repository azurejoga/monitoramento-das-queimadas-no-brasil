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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 131e2a26-7936-3208-9d94-7d6bb3feee88 | -11.88984 | -56.41302 | 2025-06-07 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f3d9704-d2a6-31a5-b06c-cd2df9f4d635 | -10.6775 | -57.62873 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8b1204e-b7b4-3e1a-af0e-5f072a43d885 | -10.53566 | -56.38846 | 2025-06-07 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8ac0c64-3b64-328f-834a-46df186318a0 | -12.52805 | -58.34568 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 80c04334-2efb-3811-865a-8194df26cb57 | -12.52293 | -58.34962 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cfce3195-0027-3244-9958-42333a78d438 | -11.54329 | -56.44873 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5664a673-f917-3de2-bf19-45206a67d8b1 | -9.5831 | -63.50642 | 2025-06-07 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aa95ce5-1038-3a5c-b756-787503feaa63 | -13.09332 | -52.28816 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 63762e4a-4927-3ef7-91f0-f325df34d118 | -12.32874 | -52.47987 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d932bff4-33ad-30d4-b453-df08e5974d60 | -11.37095 | -56.56128 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ed494ac9-567b-3a82-8105-79c92821874f | -10.69403 | -57.64566 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4af14e-54b6-3c8d-9718-7dafcea43a9a | -10.29812 | -57.14348 | 2025-06-07 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2167ce0-363d-3179-90f1-c21b6d596e0a | -10.69867 | -57.64618 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1b8dae0-d1d1-38f4-a19f-8e703b9c53ab | -11.38747 | -56.55177 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d213c5c-ce4b-3741-8573-6ca15228db17 | -11.37125 | -56.56005 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00db2518-0732-3dc6-9d61-d39897d9686e | -10.54106 | -56.38615 | 2025-06-07 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ffd67d8-60de-321b-a5d2-0e47479f4be4 | -11.41401 | -55.08542 | 2025-06-07 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1d35031-00a8-3a5f-8b9b-ca2fc87cdf60 | -11.26657 | -60.7967 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1fd5c415-f303-3eb8-95ec-651b12a6c69e | -12.66673 | -58.22057 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd4204c7-42d1-381e-bd89-a53a25f2fe80 | -11.37163 | -56.55717 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 209ed3b6-d458-391a-8813-0a200c09524a | -11.37704 | -56.55494 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bc85f52-726f-35f3-8cd5-6d1e25340b8b | -13.29111 | -58.01241 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b15e632c-f9c2-324f-8383-8fe22e3e64e0 | -13.47157 | -56.85372 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7bb22e1-1694-3015-a3f4-83ca212a9b07 | -14.04074 | -55.13878 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc654d68-22ca-356b-8f67-688cbabcc154 | -12.66562 | -58.22401 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b70d2eb6-d108-319d-9016-026e04455206 | -11.26213 | -60.80087 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14b75f48-20a5-3a01-ba75-05eebed9e069 | -11.71168 | -56.45559 | 2025-06-07 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b2b64ec-db34-35cd-8f88-1bf18f3da978 | -11.13954 | -53.94223 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39e9e1c5-55ba-3773-808e-498eb3a53b3a | -11.37705 | -56.55327 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b817b40d-0112-3ebb-9a31-e9b4b2d2c4fa | -10.87654 | -54.30436 | 2025-06-07 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13c3c9e7-368c-3e36-b2c5-4ebedebe22a9 | -11.9043 | -63.32627 | 2025-06-07 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eac05d9-ded7-313d-a1b6-75aa1b6ad1c6 | -14.03019 | -55.12922 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f5bf6e6-c850-3fbe-a5f3-d692354856a8 | -13.51818 | -56.5626 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ed619b0-3cd9-3522-a729-8087f5413623 | -13.47119 | -56.85677 | 2025-06-07 05:38:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e65f8f37-a900-3eeb-8acb-ad38143c480a | -11.37131 | -56.5584 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59544362-014c-352d-b72b-342487864f3a | -10.6931 | -57.64686 | 2025-06-07 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a07c42ab-09d6-3d12-bf59-222a4cc94be7 | -12.53318 | -58.34175 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bb0af219-2fbf-3c53-a9eb-837f02993435 | -9.63469 | -63.50358 | 2025-06-07 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea0472b2-e2df-3ba0-9e27-9515db716b2d | -11.91822 | -54.82532 | 2025-06-07 05:38:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48a40d2c-d869-3df4-8429-cb187241887d | -9.36755 | -64.45723 | 2025-06-07 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4b8520-2429-3375-b478-3b1f064d6398 | -10.29407 | -57.13754 | 2025-06-07 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 120e65ce-fa66-3a86-a4de-0ce56970a37d | -14.03638 | -55.12576 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bead6547-e130-3c16-8238-bba8409f2e5c | -12.5339 | -58.34814 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1b177d8-e33d-374d-9472-dda5613d755c | -12.33536 | -52.48072 | 2025-06-07 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d5054e-a0ed-33cc-b2f9-3f6e54174f37 | -11.37741 | -56.55035 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3579d15e-d1b0-321d-afeb-e281301a9466 | -12.66733 | -58.21578 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89298b5b-b446-3058-ac41-3bef6618484c | -11.54405 | -56.44268 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af2eaf08-cfad-345a-9655-9cd5874e03ad | -11.50127 | -61.04805 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5052a500-2b79-3876-ac2a-fcc5d92db184 | -11.54044 | -60.99493 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6af0bfe-507c-39f4-8b7a-30c6f160729f | -11.25587 | -60.79033 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6b132d0c-1ec9-3d5f-a7cc-b7eac6d134dd | -11.37669 | -56.55619 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3d3b98a-3714-3d61-9f52-772bbccfb29f | -13.29073 | -57.94005 | 2025-06-07 05:38:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 998be127-0e89-3b04-99de-8890ceea250d | -11.3666 | -56.55652 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 27e2cbdc-6dea-3871-8394-f9bbe92f805e | -13.37109 | -54.26131 | 2025-06-07 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 470d4c5a-50ca-3b44-9687-454fb4595309 | -12.71005 | -58.24545 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ed8ecfe-072c-316d-b38b-e9c77b65d86f | -12.70151 | -58.23958 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09d03444-29c2-399f-9761-cd286f321638 | -11.25965 | -60.79094 | 2025-06-07 05:38:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d2799647-35a9-3745-9426-9440fbf6c44a | -13.72131 | -58.67313 | 2025-06-07 05:38:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3502417-e1eb-3493-941f-5915c3a4608f | -12.53132 | -58.35571 | 2025-06-07 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5d3147b-e76e-3201-b02a-761cb6f8c4b1 | -14.02927 | -55.1375 | 2025-06-07 05:38:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad5ea8ab-58c2-3807-9a57-f602ae4442a7 | -11.37202 | -56.55259 | 2025-06-07 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81178387-5e7a-39e1-8b32-9de2b306bc79 | -11.84068 | -60.92022 | 2025-06-07 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf19bc5a-3dc1-3c69-a884-498106d8b347 | -7.7176 | -44.1611 | 2025-06-07 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| cc7e1974-9014-31d4-91a9-8e6cd36168f4 | -7.7364 | -44.1592 | 2025-06-07 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4c8e3fbd-b9b9-37c4-b9fd-424995061051 | -6.9602 | -42.9052 | 2025-06-07 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 485ccaeb-3512-3f21-ac86-28e07282b6e0 | -7.7361 | -44.1823 | 2025-06-07 05:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 789984f1-b0ab-3d3e-b99c-5014c21880bf | -11.81776 | -44.25668 | 2025-06-07 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9d44c528-dd56-3f52-92a6-2fb39a124943 | -11.77858 | -47.40504 | 2025-06-07 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 70cb80e7-937d-3e5d-9cec-35acecac31e9 | -12.95091 | -46.75844 | 2025-06-07 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b7e04de-4169-3d2a-99dc-1f322e83ef84 | -11.8164 | -44.2662 | 2025-06-07 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 65590a46-73f4-3548-95a0-51899670d3ca | -12.28614 | -50.09053 | 2025-06-07 05:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b44fffcb-ea71-3cf4-966d-03ff618044a9 | -12.96117 | -46.75064 | 2025-06-07 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fd084deb-afac-3a59-966c-eaf62f87e099 | -12.7749 | -48.71711 | 2025-06-07 05:40:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 510d1420-f04d-3f04-a11b-666d6b1a4084 | -11.78007 | -47.39545 | 2025-06-07 05:40:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 88f92abf-f76a-3a02-a80a-376bc6f812a9 | -12.28396 | -50.10392 | 2025-06-07 05:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 41b20820-21ee-3ae9-9f25-22e3b67db81e | -12.29098 | -50.09714 | 2025-06-07 05:40:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 12ccc69d-27a0-309f-9b6f-8a4b83568c9e | -11.80915 | -44.25837 | 2025-06-07 05:40:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4a6a5e40-ffcc-3fb5-88dd-bef4fb67a64c | -12.95977 | -46.75981 | 2025-06-07 05:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 226ce63e-d31b-366b-844c-61d00052c93a | -20.73282 | -56.65809 | 2025-06-07 05:40:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b000f71a-c7df-3141-a2da-959bf3dedf3b | -19.08008 | -53.4669 | 2025-06-07 05:40:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40c1d712-8ff7-357a-a53c-8608c83adbcc | -20.72726 | -56.65667 | 2025-06-07 05:40:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce830a6-c086-3d2b-a0cf-c183a81e1be2 | -20.9393 | -56.5962 | 2025-06-07 05:40:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 429757ea-2b5f-3785-b5a1-582925070235 | -7.7364 | -44.1592 | 2025-06-07 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 35eaf148-7453-3559-8cf4-cb9477c74f5d | -7.7176 | -44.1611 | 2025-06-07 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 691bb984-ca99-34da-befe-2161153620e3 | -6.9602 | -42.9052 | 2025-06-07 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| b4059584-c990-3578-9dde-586cb93fc0cc | -5.6379 | -43.7175 | 2025-06-07 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c645ee28-8a03-34a1-8f2d-8e1108be42ee | -7.7361 | -44.1823 | 2025-06-07 05:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 84803c0c-3f8d-35de-ac7b-effb1968e731 | -5.6567 | -43.7161 | 2025-06-07 05:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| faa3d327-30c8-322e-924b-29b05731a58f | -7.7361 | -44.1823 | 2025-06-07 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| dc8e4afb-d363-349c-87c4-a209a32d82aa | -7.7176 | -44.1611 | 2025-06-07 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5664014c-16ac-3ce4-8ffb-7aad864c5257 | -6.9602 | -42.9052 | 2025-06-07 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 0ce46d73-5540-3977-a2b5-3139003cc63a | -5.6379 | -43.7175 | 2025-06-07 06:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b7575080-15e7-38fd-9f25-2035b35f52a1 | -7.7364 | -44.1592 | 2025-06-07 06:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4e903dba-4c34-3b15-aac0-721c96a20f74 | -11.25505 | -60.79181 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc979d83-b272-36e3-a695-6fa2b90078d0 | -12.70942 | -58.02417 | 2025-06-07 06:03:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bac7d93-51f6-384a-888c-f336bddf04e5 | -11.26615 | -60.79739 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5c0c0d0-f081-33a0-8fe4-4a16f974ff54 | -11.90156 | -63.32691 | 2025-06-07 06:03:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0246aea1-3e43-33e3-86a8-138638513e8d | -11.25982 | -60.80085 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91f6632f-c370-3671-9510-7d6a9324a6a6 | -11.26032 | -60.79021 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66956d04-6bb5-311e-884a-f840baaf5eef | -11.26566 | -60.80133 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
