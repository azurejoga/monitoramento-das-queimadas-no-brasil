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
| 6ba9d1a3-5a28-3c03-a9d3-594aaca418da | -12.55628 | -57.16596 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e1b3158-1140-3ff8-ac7b-2d3fa084a55d | -12.54019 | -57.18399 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2260fa60-1f5d-38ee-8f33-2e74bc4c3514 | -14.01774 | -53.3588 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64d1ad58-5fc3-3b40-b9d3-9fd3ee7bee57 | -11.18136 | -55.91647 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a57ecd7-3b5b-3d68-b837-44f88e6901a4 | -12.0427 | -47.33469 | 2026-05-24 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c213c8bb-bc37-3ebd-a9c2-0b5fd191fb47 | -11.45076 | -54.09433 | 2026-05-24 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 173f4692-4d02-3fd0-9d2f-092820d2090f | -10.53695 | -46.46883 | 2026-05-24 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f73987e-8cd4-3d0e-a205-79856cc9623f | -14.01717 | -53.36179 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8850da5-c20a-37da-8f39-76b85d90089d | -10.28108 | -46.61185 | 2026-05-24 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 631884c2-3a22-36b3-9244-0b3061ff86a5 | -8.72298 | -47.91233 | 2026-05-24 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a96bac-b6aa-39c1-a2b7-bfb202eb6399 | -9.6049 | -44.4342 | 2026-05-24 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7fa6852-689d-3872-aefa-089f412999de | -12.04984 | -47.33589 | 2026-05-24 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c56385-684d-3cff-ba61-5828a563fba3 | -11.44597 | -54.08946 | 2026-05-24 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e58a3cbf-977e-39d9-a2bb-cb637d6b5f27 | -20.92084 | -46.79052 | 2026-05-24 04:17:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6b4073bb-3eb1-3ff7-88aa-4641f4420270 | -11.91118 | -57.03351 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0247da2b-de6d-3c16-823b-6c86bf4b82d3 | -12.89038 | -58.19814 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 238b3750-7e53-3b8b-a37b-e5069e029ff0 | -11.21668 | -53.82759 | 2026-05-24 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9b31eb9-1671-32c9-a2af-79cbc17d07aa | -12.53789 | -57.1953 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d92a2a6-5431-3818-83c8-15e7a8be1b98 | -11.04572 | -49.5971 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15e8df3a-f5c0-34a9-9f19-21c700184a17 | -14.77248 | -52.66796 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af8bece6-e58f-359e-a9cf-8a80c79a4bdb | -12.05341 | -47.33649 | 2026-05-24 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d43ac86d-d7f9-31be-a383-91cee15ef785 | -11.27528 | -53.96909 | 2026-05-24 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc1e4869-5c8a-3dcb-aab6-bc1f716c20a6 | -11.63645 | -47.87841 | 2026-05-24 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a4a2d0-fd53-3736-9bf6-6b14829ac62e | -14.32552 | -49.84304 | 2026-05-24 04:17:00 | NOAA-21 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8a5cb80-16b9-3a27-8f51-c58b67c841ca | -12.55511 | -57.17155 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5dd89b5-26b3-3055-907c-1611f151db69 | -8.71063 | -47.91523 | 2026-05-24 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d888451-24cf-3914-a1ed-8b680a09ddd8 | -14.01387 | -53.35182 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00539602-eded-33dd-81ed-10036f18048a | -10.65115 | -49.73041 | 2026-05-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce6e1abc-6feb-3050-bc03-c49b46d751c6 | -14.73336 | -52.69223 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4aa736c-fe83-38e0-9da7-3712c4d239b6 | -12.54104 | -54.61473 | 2026-05-24 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7128ca05-b35a-373d-9ea3-3b61fa933819 | -20.91753 | -46.78992 | 2026-05-24 04:17:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0ec4f41-f362-350e-8f58-60aa85cb8e9c | -12.54861 | -57.17008 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cf36d11-5064-305d-af2a-0503539d1999 | -14.01329 | -53.3548 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd00439d-8a9a-3fc1-92e7-d7af5fb61036 | -11.04985 | -49.59785 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea4dc005-fe05-3ebd-92e0-66fa66ec26af | -19.97714 | -44.85784 | 2026-05-24 04:17:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dbcc030-d032-3a2c-9946-4bfbe8d0cf7f | -14.70788 | -48.33649 | 2026-05-24 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b308740-45b7-31ae-9c09-9f73926bac9c | -10.45641 | -46.25149 | 2026-05-24 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36213cc1-c5da-39b0-810e-8c00c405fb47 | -11.54149 | -56.96142 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f071717-598d-3be1-bfe9-59105faa91fb | -8.87433 | -46.93733 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9192517-2623-3188-ac52-e5f328b3c27d | -12.54179 | -54.61092 | 2026-05-24 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a5d7c3-eccd-30bc-894e-43a5d4776350 | -12.53736 | -57.1912 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bf9cd7f-a5f5-32cb-974b-d94d5804367d | -11.63276 | -47.8778 | 2026-05-24 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1841285d-fe69-3939-944d-015ad878de8a | -12.88351 | -58.19669 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 007b4ff1-e8c9-3a85-953d-ffeb6346dfb2 | -11.54623 | -56.93824 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4814d3ec-de10-3274-a495-391d8963cfc0 | -11.92552 | -43.8656 | 2026-05-24 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a3f3572-8411-39a5-925b-6ebbb66dcf16 | -14.73917 | -52.65871 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17f33d2e-9d78-3252-8fad-180b1019589b | -11.04275 | -49.60002 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0796cce-011b-3d0b-9f7e-0beb8343667f | -11.6096 | -55.33577 | 2026-05-24 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a92e53e-db6a-3d86-96fd-3f096d2fa697 | -12.53855 | -57.18556 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66c8789f-5e1b-348f-931a-68315da685ca | -8.86636 | -46.94037 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b9107e9-f342-3678-b3f4-e000232da36b | -12.54255 | -54.6071 | 2026-05-24 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce0950ee-828b-3a35-8f02-c85cf5b41f35 | -11.94755 | -49.30095 | 2026-05-24 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9946ef28-2337-3856-82ab-3f20961ae23e | -11.0434 | -49.5962 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78583740-153a-3415-903a-dda48adce478 | -11.33714 | -46.26088 | 2026-05-24 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e642859-0b81-3cb8-ade5-313c91bd3156 | -12.54977 | -57.16458 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 637a9eb2-e257-3096-a604-4cef6e58e973 | -14.01831 | -53.35582 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe015e18-77b6-339e-8773-a31be0f2d1ca | -12.55013 | -57.16853 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e403e80f-b433-3d09-9dc9-6f1a6c8618b5 | -14.01659 | -53.36479 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 879397e1-0cff-373b-ae9c-801c3e29a6b8 | -9.4109 | -49.40416 | 2026-05-24 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ca5c4fb-7b3c-3f06-aa35-aa23448ea601 | -8.87069 | -46.93672 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 059684d1-8301-3283-8935-7d0d5c2e4e1a | -11.54384 | -56.94993 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14890ba2-aa12-311e-9043-bc596622c6a3 | -8.86272 | -46.93978 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 788b7afb-4741-3c4a-8b9e-0e548429d83b | -11.92415 | -45.00373 | 2026-05-24 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8962b641-e37b-3751-9b7f-df0c22649f28 | -11.04917 | -49.60166 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae320f65-2320-39da-a6b6-9d361aaa83df | -12.53903 | -57.18966 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0cd8e1a-abba-30b1-aef6-ad29ccb00f26 | -11.54503 | -56.9441 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6953ebcf-4de2-315c-97fb-14a6a044aa81 | -20.91423 | -46.78932 | 2026-05-24 04:17:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bfa4581d-da1c-3b30-885c-7e52073a2b7e | -12.89465 | -58.17823 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9078e999-02f3-3481-a8d5-a750d91fd78a | -11.34057 | -46.26147 | 2026-05-24 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18cb0b4f-f5b0-3239-95b7-4b9cdb01760a | -14.73943 | -52.66093 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37ba25b3-6642-31f3-8c2c-e01777409039 | -14.02219 | -53.3628 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f3e9a6dc-cfa1-3bea-8237-324ce077095d | -11.44603 | -52.92692 | 2026-05-24 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 015586d5-d41a-3084-8bbb-f4c62747509a | -15.0904 | -57.63025 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db5f1290-7130-3e72-a041-2c48d476ccdf | -15.09913 | -57.62082 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bff1d3f-0921-3e00-b5fc-9db980e3e4aa | -15.10437 | -57.62764 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63154873-aeea-34a6-9001-aeb4ee0a1401 | -18.65536 | -48.8736 | 2026-05-24 04:19:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0692e30b-f013-38e1-b863-522d6d90f6d4 | -18.65181 | -48.87293 | 2026-05-24 04:19:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1446d0ea-8308-3ef8-819a-9dd17c9e880a | -15.08924 | -57.63566 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c6ff6d3-dc13-3a44-8529-03b0f9decd8b | -15.09797 | -57.62624 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0b68473-7b60-33ee-b3c2-5c34eed0b3b0 | -16.1506 | -51.72305 | 2026-05-24 04:19:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2a9b943-8f6e-3e21-a051-720500afde64 | -17.7272 | -53.04861 | 2026-05-24 04:19:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6a37781-1bac-3101-901f-d8e5e545c094 | -15.08282 | -57.63428 | 2026-05-24 04:19:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d272f321-2d1d-3b60-9437-3777edb377a5 | -8.7052 | -47.91597 | 2026-05-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd5e6d4c-011a-3218-a5ab-8eb0da34eba6 | -6.08301 | -44.00755 | 2026-05-24 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f47e0a88-f419-38bf-9588-6936c914559b | -6.85413 | -48.73529 | 2026-05-24 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14879945-78eb-36c4-b578-d5a79b21365a | -8.44149 | -51.53571 | 2026-05-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18040b82-0427-34e5-a91f-1e773cdeff18 | -7.22071 | -46.96013 | 2026-05-24 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc462b7d-e7f6-3a25-a6f5-94acb0276951 | -6.85133 | -48.7312 | 2026-05-24 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6e898a-176f-3064-829f-a062d28123b2 | -8.70868 | -47.91652 | 2026-05-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2128c673-4ead-338f-b599-02499c8d47c2 | -8.87301 | -46.93845 | 2026-05-24 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92ccff62-bf16-34cb-82b2-fede422dff73 | -8.1421 | -41.18076 | 2026-05-24 04:46:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 239f6d6f-e70f-3a1a-be1d-441e7887e105 | -7.13531 | -44.06986 | 2026-05-24 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb80f61e-952a-3b5d-935a-d7efa3a57c0f | -8.44488 | -51.53626 | 2026-05-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccf121e7-e8dc-39aa-bc9e-80ee5c76e67b | -5.20385 | -56.04602 | 2026-05-24 04:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 966d1b34-f0ef-3b42-bfc9-64da9f2e8d59 | -7.30306 | -49.61797 | 2026-05-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36da2d18-eabf-3755-a4ea-c09ff88f6cd2 | -8.72059 | -47.91406 | 2026-05-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51dab06f-2f0b-3872-88d9-dd0ac55c0e39 | -8.14166 | -41.18396 | 2026-05-24 04:46:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4da9ba62-bb7a-3ba7-8dcd-18b70138523c | -6.89886 | -52.19486 | 2026-05-24 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31998bdb-4105-3917-bf41-1d94e0cbb6c8 | -12.55309 | -57.17531 | 2026-05-24 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b3f7fd8-1c9c-3088-9d74-1f46c9c2ad30 | -14.01311 | -53.35859 | 2026-05-24 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README4.md)
