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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59f9710d-1669-3fc1-b0fd-221a38adca81 | -27.42356 | -50.61653 | 2026-04-23 04:34:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd5df3ba-0f9f-3c9f-ab0b-630359636a16 | -27.93759 | -50.20363 | 2026-04-23 04:34:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b33ddbe9-b0b7-30a1-8a00-9822866efad0 | -27.95502 | -51.06816 | 2026-04-23 04:34:00 | NPP-375D | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6b165d8-1d2a-3f81-b55e-102e8fa0256a | -29.6785 | -52.79279 | 2026-04-23 04:34:00 | NPP-375D | CANDELÁRIA | RIO GRANDE DO SUL | Brasil | 4304200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fbaa364c-884e-3f49-ac77-87d11ed3b93b | -24.95554 | -49.6339 | 2026-04-23 04:34:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7a2f9fc-8acc-384b-b856-c6c2549e5cae | -27.29376 | -50.53822 | 2026-04-23 04:34:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8cc0cc6b-3eb3-3ab8-8356-37081f2ea52b | -27.94424 | -50.20498 | 2026-04-23 04:34:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 09e914f6-95ea-3a77-944f-7cb267b6af9a | -29.83909 | -51.793 | 2026-04-23 04:34:00 | NPP-375D | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 10b9ee30-99c6-3d7f-9dec-e2ddf9e1fcd5 | -27.94361 | -50.20889 | 2026-04-23 04:34:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf2910d8-aee9-36c9-bf60-45fb7f5b5fa2 | -26.2664 | -48.88942 | 2026-04-23 04:34:00 | NPP-375D | JOINVILLE | SANTA CATARINA | Brasil | 4209102 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b9f0019e-2226-3304-88fd-448b8fe76fda | -26.9671 | -50.38064 | 2026-04-23 04:34:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8723d75f-9264-35c4-b76c-bef402331866 | -27.29709 | -50.53891 | 2026-04-23 04:34:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa33084a-042d-3880-b665-a97fb07973a5 | -27.65899 | -51.0381 | 2026-04-23 04:34:00 | NPP-375D | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 74ba3286-c5cf-32c2-bfb8-a1612ab52462 | -3.85553 | -54.07889 | 2026-04-23 04:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f8a62f0-34f6-368d-896a-13ecf09860db | -2.35204 | -51.16217 | 2026-04-23 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4cb033c3-23d8-347a-8dd4-e8f5ead333ab | -10.00306 | -48.67833 | 2026-04-23 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d30fd649-9286-3abe-8423-f5d5547e84fa | -11.7744 | -43.66154 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2338342d-537c-35d2-8809-eb86ce1fd99b | -5.28379 | -56.0174 | 2026-04-23 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 516669d8-cb90-3cc5-851d-748311ffd9e2 | -11.79098 | -43.61316 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1e392c3-a5f5-31d4-bdf4-a1615a95d9e9 | -10.00792 | -48.67039 | 2026-04-23 04:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39139043-891c-3382-aa95-309f29240611 | -11.0619 | -49.50061 | 2026-04-23 04:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad23716d-d2e7-3976-bc00-c675059e20ad | -11.77125 | -43.6453 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 291b43ea-39b7-360a-becc-a5856455ee46 | -11.77008 | -43.65458 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee870d44-16a1-3bd0-8a12-1033042c2b36 | -11.79058 | -43.61627 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a28b475f-a76f-3801-8074-42192a0548fc | -11.77164 | -43.64219 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4339d098-f943-3464-a6c5-bffb0fad27bd | -11.78939 | -43.62558 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77becc8b-ba67-32ac-80ab-ea6546e66a33 | -11.77911 | -43.66541 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7731c948-6523-3dcb-8ee6-0c4142155122 | -11.76575 | -43.64766 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d3b2624-0077-33e8-b93d-5a020747693f | -11.78466 | -43.62177 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bded64a5-5f4e-306f-beec-ab397a76bcfe | -11.77519 | -43.65533 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 135d5a5d-aa7f-352d-9f39-ea3fc183e467 | -11.78545 | -43.61558 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aede2521-1ead-387c-a9d1-01a812ef38c1 | -11.77047 | -43.65149 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea511e45-7f47-3a65-9ae4-646970208d9f | -11.76102 | -43.64381 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbd728e5-75a5-35b2-8df1-9b620c85ec29 | -11.7799 | -43.65918 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfac812b-08fd-3781-ac62-ca7a62dca84f | -11.78506 | -43.61868 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f86357a0-7161-360f-a22b-56136e4cd1ab | -11.7846 | -43.66313 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1811c3a-7087-366b-879c-2acaab4eab6e | -11.76968 | -43.6577 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af629b5d-f0b6-3317-b7ad-72688e2daece | -11.77951 | -43.66227 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a76c921e-bdcc-31e0-a2a6-6518a33bccd4 | -11.77479 | -43.65842 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdc4c364-520e-308c-b968-96d595c1492d | -11.76614 | -43.64456 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24b92339-6ab2-3c28-8daa-d0776294994e | -11.77597 | -43.64912 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 614f4f10-ccc6-3c55-9847-f42a20fa690f | -11.77204 | -43.63908 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d41fc21f-9a59-3c01-a5df-333292725367 | -11.78979 | -43.62248 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f938e093-ca43-3f43-bdda-89a8b13e4ed3 | -11.77086 | -43.64839 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7c6e666-2587-3897-9b9e-3fcfed802e62 | -11.79531 | -43.62009 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 629e1828-0c38-3a59-83ba-68541826177f | -11.76653 | -43.64146 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e329023d-3335-38b8-8d9e-9b48ed2fc0b6 | -11.79571 | -43.61697 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9d12690-f25c-3b60-b828-2d3a16841b97 | -11.76536 | -43.65076 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1088ca97-297e-39a0-9042-d54e6ee90d35 | -11.79018 | -43.61938 | 2026-04-23 04:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d975c2b1-8303-33f9-9c97-9c798e89a660 | -13.99289 | -56.64962 | 2026-04-23 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b8df3d6-e7d7-3e08-8f0e-505dbb7d1808 | -14.09785 | -47.20896 | 2026-04-23 04:51:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e778132-6fc2-3981-8967-a5fa32408bad | -11.60258 | -55.32716 | 2026-04-23 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a132e1b3-fd82-3904-a2ff-76c96d40ee4b | -18.12349 | -45.76052 | 2026-04-23 04:51:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 650f4981-50d4-3122-95f3-93925fe8a33e | -12.02457 | -47.76678 | 2026-04-23 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6391286f-c122-3eb3-9508-76c6aa4824db | -12.01215 | -49.27938 | 2026-04-23 04:51:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69e42ab0-d3cf-3767-8f14-417f3cced663 | -12.28348 | -44.62332 | 2026-04-23 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4106c466-0a69-3a38-9a23-7884895c6b9e | -12.56509 | -45.47499 | 2026-04-23 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0abe9d2d-25a1-3759-a0f7-d1d1e60bc2ae | -18.11802 | -45.76544 | 2026-04-23 04:51:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| ad391978-30ce-3aa7-bdb2-22d6e1178196 | -12.30188 | -57.17725 | 2026-04-23 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec01975d-41be-32f0-8aa2-d34f6742ca0a | -13.38145 | -45.32719 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7211d05e-59fb-34ab-b88c-9b419869e1f1 | -17.98901 | -54.17581 | 2026-04-23 04:51:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6cc9882-e21a-3a46-a987-e3b389b13289 | -12.27864 | -44.62274 | 2026-04-23 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53fc050f-de77-3d8a-94fa-00b47181d990 | -18.28635 | -52.88736 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a10506f-710d-3ad8-9bff-dc89785f0f20 | -16.43045 | -54.91545 | 2026-04-23 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b42f76-a11f-32ca-9a26-863dc54e1203 | -18.30914 | -52.89498 | 2026-04-23 04:51:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c51d085c-14a9-378c-b0fd-79d31aab73c3 | -17.48234 | -51.08669 | 2026-04-23 04:51:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20c1d60b-acae-3316-a35d-b0ec75210793 | -18.27579 | -52.88934 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acfc6957-2ab1-3c14-a02a-41d98096a178 | -18.30247 | -52.89386 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef126df-98a2-321b-a5ef-6f66a1da5870 | -12.58461 | -45.46787 | 2026-04-23 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7439635f-17a2-32c1-bb58-62c0cc61609c | -18.26912 | -52.8882 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4453eae2-0852-373f-a397-0726c8a1cb5b | -16.42707 | -54.91484 | 2026-04-23 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c3cdb65-425d-373d-8989-047e20a9f811 | -12.05479 | -45.34316 | 2026-04-23 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b249d356-ab59-3f20-b30b-b9ca5e85ac75 | -12.56965 | -45.47563 | 2026-04-23 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| debd3a84-0320-3f0e-8921-e2fd4de576e9 | -12.05458 | -45.34518 | 2026-04-23 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b762d43d-a9fa-36b6-ad41-c747936b7cfc | -13.37678 | -45.32656 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b55adafa-9046-3454-897d-ccd847a2f6c4 | -12.09285 | -51.22465 | 2026-04-23 04:51:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f51bc048-92e7-3bf6-9aa5-a1b9cd0027b6 | -13.50679 | -56.85413 | 2026-04-23 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9658607f-0650-32d7-a7bf-3fae3b56adad | -12.27933 | -44.61736 | 2026-04-23 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d36da28-0a54-36ff-8d25-f71134f2477c | -13.38273 | -45.31718 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bec4ce2-dc5f-35ac-ba51-d477c59ff95d | -17.48583 | -51.08727 | 2026-04-23 04:51:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2773b2d-b549-3037-a81e-8875312c3c97 | -18.28358 | -52.88311 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c26bd06-ed84-37fd-9d3e-5423ea8ee562 | -13.38612 | -45.32781 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95127630-299b-37f1-97d5-34df7b51c633 | -17.48524 | -51.09129 | 2026-04-23 04:51:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07729144-1dd5-37f0-b5d6-6866f35dac04 | -18.27969 | -52.88623 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44dff8ed-f3e9-3983-b26a-896abf11c188 | -13.02729 | -43.5899 | 2026-04-23 04:51:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc8615a-da81-3255-9393-5c19f5202015 | -16.42244 | -54.92181 | 2026-04-23 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7b84f9f-caa0-3785-9056-5d77d8fa9b59 | -18.28302 | -52.8868 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40ad6714-6194-382f-9e79-7fda1b3f21f5 | -11.57337 | -54.56834 | 2026-04-23 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 875fcded-3f7c-381b-9681-396d1a8ee085 | -12.55457 | -45.48045 | 2026-04-23 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f11c55ef-2cf3-30b8-910a-d84a8e1b53b2 | -16.42644 | -54.91862 | 2026-04-23 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5175fca7-e704-3de0-a59d-d9371dce4711 | -18.28913 | -52.8916 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dcf764a-71cf-3967-99fb-43bde66caf7e | -13.38209 | -45.32219 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d50d201-af4c-3bb1-aa4d-386010c861db | -12.30581 | -57.17797 | 2026-04-23 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fda315d-7c2b-3751-addf-640516e376fa | -13.54618 | -47.89085 | 2026-04-23 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db5d2494-03a3-3104-b4e9-2d376b900e6f | -12.28417 | -44.61794 | 2026-04-23 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bac7e73-e559-3cd6-a5e0-4e2140dfdc6b | -18.27635 | -52.88565 | 2026-04-23 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5aa41296-d6ae-3acc-914a-3d5fb47f024e | -13.38677 | -45.32281 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd1e1f80-8781-3654-9cb2-242c4e77f1f9 | -13.37742 | -45.32156 | 2026-04-23 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ad709b9-d20b-3703-aa0b-23eab2729f32 | -18.13892 | -54.23542 | 2026-04-23 04:51:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77756e2c-fa08-3c21-9a72-e1b0e89ec282 | -12.58399 | -45.47266 | 2026-04-23 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
