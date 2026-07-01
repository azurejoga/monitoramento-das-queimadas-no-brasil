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
| ecfa9668-1091-3c52-9a0d-7c8c5a039f84 | -12.84804 | -44.34696 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fe050e7a-2ea4-3d00-93be-b465a1021d1d | -12.77427 | -44.49085 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1009151b-eeb0-3d84-b525-d7b7241d2c9f | -12.82543 | -44.34773 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1af6950a-b2aa-3302-a3bb-53b6665f15b9 | -16.57979 | -45.87759 | 2026-07-01 04:57:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4970ed45-bf0d-3901-a5a3-1ca24cf9190c | -17.71374 | -46.79764 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 298b36f8-7d08-3e9d-80be-5d1d7bd0d266 | -11.42476 | -56.06709 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0e63badc-48dc-31a2-80f5-994740bdebdc | -10.85086 | -56.65305 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49d46a69-755a-3398-a6e7-f356d22473c0 | -10.77131 | -53.54016 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17873105-3a61-32d8-933d-760131af5847 | -16.3553 | -56.65834 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 7caf8873-182f-3fc9-833f-883a1d7a8914 | -11.42196 | -56.06265 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd95298d-93a0-3295-ae0d-5cdbb2ff2827 | -10.80163 | -53.54147 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91201fc3-c2f4-3ae6-bbe4-9f2282fa84e5 | -10.77406 | -53.5442 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b11708bf-b477-37ee-b3b4-61cdfc888d6b | -15.2407 | -48.56505 | 2026-07-01 04:57:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e573c6-0fb9-36c2-a114-fbec49e3a65d | -10.76414 | -53.54259 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3051d50-def1-395f-8a5a-f6673e9038f2 | -10.84277 | -54.03157 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57f01d11-7c5c-326f-84e3-4155806897b0 | -13.26528 | -56.79632 | 2026-07-01 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8783f53c-73dc-33e3-81db-33d54333358d | -11.6328 | -59.01282 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce276048-176a-3172-99bd-c06ff14fbde9 | -16.36269 | -56.65579 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c98b7f10-f9de-3542-a885-d652247baf5f | -12.46035 | -49.58145 | 2026-07-01 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a04afa2-818b-3a57-ab43-658cd831aa86 | -10.67575 | -54.52466 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| acdd6992-02fe-3eb3-b6b1-7c9470f70831 | -10.67462 | -54.53173 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab5afcc6-2c04-39c3-bde0-c261b7851181 | -11.62878 | -59.01209 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bca62760-300f-35fb-ae2a-a1ae466fcd00 | -12.76924 | -44.48657 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 0f022970-7166-37d5-b84b-66e1bd5ccbb9 | -11.4336 | -56.0567 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c41c99f-c14d-33a4-8dd6-1511cc845c54 | -12.76337 | -44.49265 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f5107176-1840-3717-8610-1aa714a073eb | -13.72359 | -47.88169 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d189f99-6b29-3432-9b27-b4f56ce1c88b | -12.46354 | -49.58698 | 2026-07-01 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbea11b7-ed6f-359a-b37d-e5850d94e145 | -10.77201 | -54.11343 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18a2e135-6c79-3cef-b7b7-380952d1fbfa | -11.84188 | -56.94815 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6505a091-b5ef-3445-819c-b82bfbd46478 | -10.67851 | -54.52875 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85146789-87a2-3e00-b05e-404286fb2e39 | -11.43567 | -55.9201 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0770d0a-3fa7-3cf7-b9f9-6b298d126302 | -12.77014 | -44.48248 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 9690cdd4-c3a1-3708-b672-ca10537f2d1f | -11.88938 | -57.13495 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42974c40-46f3-3572-8740-613402321455 | -11.3806 | -55.80558 | 2026-07-01 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d384c84e-fffe-3268-858b-66e142b2cfa0 | -10.77076 | -53.54366 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 059e3699-1e29-3c80-aa2b-54e650002b2f | -16.35805 | -56.6627 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 91e1ed03-fbde-3165-86f7-7b3d8ddbb971 | -11.89113 | -57.13705 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8785a144-62c8-325e-877c-d26d2e2616cf | -12.84205 | -44.34996 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| ae256cd9-369e-3f3a-8300-dd5857352cb7 | -16.58505 | -45.87826 | 2026-07-01 04:57:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70e5c59e-1d96-3882-87a1-feeeebfa55bf | -12.76252 | -44.49986 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 4ac34236-0361-340d-9fed-e0ff18f555e6 | -10.67016 | -54.53827 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ebc3815-9ee3-315e-98d8-960b76ac7d57 | -12.82588 | -44.34402 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 919bafbd-b6b3-3a30-998b-3c381a46e909 | -11.84544 | -56.94876 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5ccec90-943f-3b68-80dc-098a6bd1a13c | -12.83098 | -44.34844 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| edb85d98-6dac-3dec-a704-70006e9fbf86 | -10.91159 | -56.85303 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5e6fe6-e351-3134-a751-e1a63c9cf5fa | -12.75873 | -44.48473 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f28f9781-d8c8-3dd9-99e0-1c9a473db32c | -12.83651 | -44.34922 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 15e7d000-9fbf-3284-bcaa-1469431c01a1 | -12.75916 | -44.48111 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01b668df-0c47-3598-8f22-baf73ced2c91 | -14.63343 | -54.46562 | 2026-07-01 04:57:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 781f903a-87fc-3c4d-b7c7-93c378318794 | -11.42325 | -56.05495 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 901665fb-a868-34dd-8e88-ed38d6cfb2b5 | -11.21258 | -54.33371 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 220ac31f-0449-3874-8090-2d557a536789 | -11.43295 | -56.06055 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5307beef-512e-33db-b511-34d8bfd2328e | -13.7285 | -47.87865 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06a11008-44a2-35d8-9301-44a9eec2550d | -10.77644 | -54.10696 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07574283-e16f-3693-847a-3876f828fbc1 | -12.7583 | -44.48835 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 101dabd4-d201-3795-a07e-0c13d2c30675 | -11.89802 | -57.1278 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 115bf209-5f72-321b-a146-ac0990efe4e8 | -10.67518 | -54.5282 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 3a3e9be5-f607-3522-a1da-8654a033337c | -10.78674 | -53.54983 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff8beda3-9bf8-3827-bb9c-c785b83deb7f | -17.71908 | -46.79554 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42365575-d5f2-3f31-befe-2f00830071dd | -12.14798 | -57.22107 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9006ff7-3e88-311d-80fa-e3e49e34cfa7 | -17.71046 | -46.78211 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 010482fa-1186-33f5-ac56-a7744bbaf96f | -12.7999 | -54.86413 | 2026-07-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a3bf437-9874-3d8a-ad44-2bc5404d787e | -10.76469 | -53.5391 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6318d609-dd15-3aa2-8ff0-8a27ffd49e7f | -10.67632 | -54.52113 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7618a3e5-e76d-3c52-8e22-b40e386f1643 | -12.41832 | -58.38675 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3856fb17-2093-3f78-ada2-e497bb171fc1 | -12.76294 | -44.49626 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8903a418-7eca-3910-aadc-45dfb12776b0 | -15.07333 | -55.81048 | 2026-07-01 04:57:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b29fb54f-0257-3fd1-9324-34613f84d429 | -12.66946 | -48.22051 | 2026-07-01 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67da05a-dd56-39fe-b4df-56ed957bfb5e | -11.8973 | -57.132 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b95b7964-61cd-3113-b222-46d080bc097a | -12.83142 | -44.34474 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| db713ab9-a9d1-3745-8767-daab7e450aad | -11.90347 | -57.37866 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4544448b-3c8f-38e3-95e1-6de94b1da673 | -11.50201 | -54.5004 | 2026-07-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1443ba0-86c4-36c4-8f44-6fa302c41b5d | -14.63012 | -54.46507 | 2026-07-01 04:57:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86ede9dd-77f0-3838-9afc-d2d4ba823147 | -16.35868 | -56.65894 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 1a0f2901-7bf5-3256-afb3-9271efac6865 | -11.42821 | -56.06767 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 680421df-2cdd-3f8a-8254-1d8a1bc61b8f | -10.67738 | -54.53582 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6c0d64b9-fc30-3840-b311-a62b0fb28494 | -17.70893 | -46.79236 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d0bab64-96e9-3b4e-af0f-326e96bea152 | -10.28037 | -60.54023 | 2026-07-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fbebf3c-e7b1-31b0-970f-181e6a7a9df3 | -11.62815 | -59.01567 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ecc52234-3ea2-314e-bde5-0798328e6b03 | -10.85018 | -56.65716 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062f9784-2f88-3c1d-b92d-b39fc8b305b3 | -12.82499 | -44.35144 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 829cfb9c-e638-3486-b963-160b65f6b72b | -11.43166 | -56.06826 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 34f8f81f-fad3-3f8a-bd26-464d2978eb0e | -11.43753 | -55.90871 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e0fadd2-19bc-31f7-9424-7bc3f8483be0 | -11.53769 | -49.77368 | 2026-07-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70da7adb-1516-308c-89d2-863ba85ae526 | -17.7146 | -46.78729 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d99b0cae-6824-3b2e-8241-4f4820346c16 | -12.44479 | -49.57923 | 2026-07-01 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a8b5fb-041d-35d8-bcf2-d631a137e63f | -11.42886 | -56.06382 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 297498bd-b491-3546-be25-e20f760dc086 | -10.08098 | -60.49417 | 2026-07-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd03695-2739-3728-9c2d-e0acf1b6c4a1 | -11.79475 | -56.9968 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b070e41-e866-3e95-a104-8bf101354345 | -11.88754 | -57.13643 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f53477d-a966-3002-b3f8-bf57b926c70b | -10.67023 | -54.5165 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9c0827e9-6104-3c20-87dd-33071a175851 | -11.42757 | -56.07154 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ea0efba-e0b6-3603-9e1f-19baab958789 | -12.76465 | -44.4818 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 5d14a01c-d194-321e-afb3-050c2d064300 | -12.21618 | -56.56113 | 2026-07-01 04:57:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea1e9c58-bde6-3d82-a0ac-7a11efcaaad3 | -10.6674 | -54.53418 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a213bbfc-f6b3-36c0-9254-9a2d9a1831ca | -13.4776 | -47.8777 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596a1feb-3a2c-3538-b17b-d24b5be987b7 | -11.89613 | -57.12926 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89c7201a-4e86-3af3-9491-c27c0fd89d1b | -17.71427 | -46.79023 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad3cc7bf-92ea-3043-9a54-0747f016bf5f | -11.43629 | -55.9163 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57cab7ab-1e2f-31e1-99de-446279964f01 | -12.76843 | -44.49692 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |


[Clique aqui para ver as próximas entradas](README26.md)
