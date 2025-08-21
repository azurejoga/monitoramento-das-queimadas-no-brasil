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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d6db355-2a25-33ec-b44c-999f712bd32e | -12.6396 | -46.88181 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9d4eb17-8599-314a-8673-3e8580d6a14e | -11.30232 | -44.92778 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd704b1f-2b55-3349-a547-5044b455a9c3 | -12.71626 | -44.78913 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc7ba177-2b56-3857-b44f-d7f6e65c8f97 | -11.90781 | -44.8763 | 2025-08-21 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 377fe0fa-2a24-3021-a33d-3460966aa7e9 | -12.22112 | -45.41982 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d126eb4-5b92-30df-977c-e9c0d6585deb | -13.14442 | -57.12514 | 2025-08-21 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cb13928-cc30-3259-8132-2a6d5f7d508b | -12.97975 | -45.19783 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a70e4e99-edb6-35bc-b1f6-80d2fd502233 | -13.04853 | -46.82497 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e69c7c-79de-3d5e-b63e-c433a9c9bab4 | -13.02534 | -45.17971 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 644daef1-9249-3bc5-9888-66d6cf4e19ea | -13.14351 | -54.92405 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce54200-2b4b-3688-910c-8340f233ee58 | -12.58697 | -60.36285 | 2025-08-21 04:40:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6460d5ce-cc66-37d0-a5b9-a155a7a8488a | -9.66261 | -48.38309 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c82e0b5b-2bef-3492-a5d1-a6c8a7b7250a | -13.03952 | -45.20201 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 312074e0-78a4-3911-af34-2c0e6b53bc50 | -10.98335 | -55.23744 | 2025-08-21 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beeb821d-71cc-308b-9ec6-773c60bc6a36 | -13.63896 | -43.80727 | 2025-08-21 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc8d1026-fccb-367f-ad37-d6dfedba1449 | -10.72437 | -48.23476 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 002feaaa-7942-32b0-a1c9-2b0083e06325 | -11.30705 | -44.92457 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899f2268-7a83-3748-a83b-7f3844620761 | -15.88901 | -49.01444 | 2025-08-21 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34cd8130-ee1a-3318-8abd-8bbf00f26b46 | -13.03806 | -45.18137 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ff9fd66a-820b-3f90-8cd2-e4897494d085 | -10.71108 | -48.2288 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6c40222-0bfa-31e2-94bb-6fb62fe09622 | -16.11219 | -46.82592 | 2025-08-21 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99b7a304-390a-364b-9209-ae798e0b9f0b | -13.139 | -54.92799 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fabf2df9-1c42-3e70-95f7-6862dc2f6912 | -8.87829 | -62.42342 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d53681a-ce73-39fb-a8d2-f259e89f4c8b | -13.0343 | -45.20885 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7278e1ed-a90c-3a64-a74e-62f9dde42d0e | -12.97553 | -45.19721 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3afaee01-b053-306c-a4e1-030a638d4a88 | -14.47421 | -48.36894 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f935752-d8ef-3440-b717-578b9f0f82e2 | -6.93155 | -62.8903 | 2025-08-21 04:40:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a649c1be-43a0-35f7-ad6b-5ee5c60d2ccc | -15.56721 | -50.32187 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd086100-d536-3b39-8e12-2f06d1ecedfc | -8.85791 | -62.42484 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ff810a48-8359-3057-86fd-10a3712ef9fd | -13.59269 | -47.01673 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a59c4de-b55f-377a-8fc3-dbf89e6ec361 | -9.90915 | -62.14676 | 2025-08-21 04:40:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6cb547b-611b-3342-bdc7-d8bf8d09b0b9 | -13.16431 | -46.90779 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57de899f-a42d-3ec6-9421-7a37880eaab8 | -12.98047 | -56.87863 | 2025-08-21 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032ff71b-f02d-3ba6-b974-38c7897d0ec9 | -14.99889 | -54.82569 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7832ec8-b4de-3ab4-9f01-46a8f76e4cfd | -15.5801 | -50.30485 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7412fca-7ed5-316d-8ea4-45879fac6baf | -13.13979 | -54.92337 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70a4723-7192-364d-b6ac-82bcb0b47850 | -11.51417 | -50.53303 | 2025-08-21 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 188e190a-abdd-3caa-a40a-9b02012d0cdf | -9.89381 | -60.28627 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 973aa49d-7a7d-3edf-92dd-d08c3c7032df | -13.14489 | -54.93847 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36769670-aaad-3e23-a798-399a9dbd72bb | -13.38562 | -46.23552 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e8b755e-7971-3e1c-b1a9-ac936e9a677b | -7.54984 | -63.85348 | 2025-08-21 04:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57f2b1ce-a85c-315a-b25b-e62315c697b0 | -10.70476 | -48.22367 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30ce28b9-ab1c-31e4-a7e3-874d31686db9 | -10.40806 | -59.38114 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddc65fa7-fc13-3a0e-bf09-b9c215ef7a8f | -13.38587 | -47.50265 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39cf2837-9f34-338c-9582-a176bf73c094 | -13.02627 | -45.2043 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 939aff3b-ee63-3ffa-b484-6f78cf791231 | -11.17739 | -46.13658 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86fcb885-097f-35dd-9ad4-b2df29b50b11 | -9.90621 | -62.14771 | 2025-08-21 04:40:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dc2d189-fe9d-3f84-8ab5-812731444618 | -13.13822 | -54.93256 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b0adaf-2e82-3228-a710-a3a1b13047e0 | -14.4935 | -45.95247 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12878163-898d-339d-9da9-48b1bb71cbd9 | -14.63878 | -54.86853 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d2f706f-f779-3373-99b2-55badc0bf00f | -13.03491 | -45.17286 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a301abcf-d60a-3a8c-a5c7-83b8f406c35e | -12.08838 | -44.7239 | 2025-08-21 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448aee8a-fdd1-34ee-b0b0-57fa8bca91c1 | -14.85964 | -47.94178 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a16610a-82a0-3551-8544-82bf13f29e3b | -13.64362 | -43.80818 | 2025-08-21 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b92b1956-a614-3124-b7b4-c4c2c36fc7dc | -10.89278 | -48.48634 | 2025-08-21 04:40:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a45655b-03d8-364e-a376-cd3338399ca9 | -8.85925 | -62.41656 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7bd9891c-ef5b-329d-b0ec-13f42d582271 | -13.0185 | -45.16654 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b642b894-d079-32f6-94c3-970121420f72 | -13.57283 | -47.04784 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05bdd21e-c503-31fe-be28-da763ab5bc73 | -13.03473 | -45.20546 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c4c451b2-d1ee-3afb-9ecb-e9e4445313a4 | -12.98291 | -45.20639 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01871c87-80ef-363f-9130-24193f207b94 | -13.02643 | -45.17173 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71ae0c27-9a9a-3925-95df-eb524ee8951c | -12.90901 | -46.09184 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e557e1c0-9a25-318f-9537-5b75125472aa | -13.01317 | -45.17394 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 6bfa1664-9299-31f4-be42-e1ba86f39300 | -15.90994 | -52.22119 | 2025-08-21 04:40:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fa8268e-18f5-3f11-ad57-beb174244918 | -14.75008 | -56.02517 | 2025-08-21 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e913e54-a345-3ffc-a89d-d37fcaedcf32 | -13.01741 | -45.17455 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 30ca62e6-a02e-3d7c-b3c0-4389091bf815 | -8.88041 | -62.41259 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 845f44d3-efcd-3267-923b-19cda79ddeee | -10.72322 | -48.2424 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b246fb49-4c5a-3d9c-990d-d605c4f4417c | -14.85412 | -47.95445 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6c884373-f4c9-322a-9ae5-d7953550ce61 | -12.89262 | -46.0764 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11b8694b-41a5-33b1-9f42-5f8481b1f994 | -10.53979 | -42.5472 | 2025-08-21 04:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 62681b2d-a474-3f4d-a5e8-efb441125934 | -8.88703 | -62.41111 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7cead31-8419-3d91-82f5-223032daac81 | -13.32949 | -54.40435 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 473b3427-a9f7-3a2b-8182-271f577b6e03 | -13.02384 | -45.15912 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fea58b3-ad1c-3470-be56-a9b8f53ab5e4 | -14.6227 | -54.87455 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d08cef-e218-33e4-b71c-b7dcff3443c8 | -11.86052 | -51.60475 | 2025-08-21 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 300addb7-db24-32e7-bd8d-07fd76f0fc8f | -13.04327 | -45.17321 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9adf29ff-c737-39df-82bf-a4bb82645539 | -15.03153 | -54.85302 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73b4392b-0820-33a7-a258-607993444e81 | -15.50749 | -48.05255 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1073ad87-8c75-30cc-99ba-3f1a51f5ec26 | -8.87724 | -62.42878 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7c5de39-005f-30f5-9692-0f79046af042 | -8.86329 | -62.39762 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 47e8abf1-1df4-3d47-b77e-3978ff3ccf03 | -16.10326 | -48.00724 | 2025-08-21 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac519602-035a-376e-83f3-5824c9b457c8 | -13.04155 | -46.81913 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6cd35d6-b747-3527-99ce-d261f3cb8a55 | -14.84984 | -47.93166 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3411b9a4-3680-3854-8a8d-796172768c72 | -13.47995 | -47.05117 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66a17fe8-bd93-3962-8c08-3d2db5ada472 | -8.86435 | -62.42617 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 778b29e2-b032-3bc0-8270-5a38747f84cc | -13.54186 | -47.04781 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b92c5026-22fe-3843-80a2-4900f23d4e98 | -9.86613 | -45.98114 | 2025-08-21 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d24a2dc-812f-311e-9cc9-855709895028 | -13.02259 | -45.19971 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c71e27a6-5664-3c92-9f7a-531900b072fa | -13.48061 | -47.04648 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ca6477e-456d-36b9-8f72-fd2b1c0fa74b | -8.86773 | -62.40708 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a9ed0429-4854-3ec1-a80c-4fd7dd7a80af | -13.53574 | -47.03992 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f25187cd-c1a9-331e-931a-8709913f2c22 | -13.02588 | -45.17573 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86c2bce-bb99-3504-99f6-b5b95173262a | -15.5185 | -48.05427 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f3e7b31-d449-3cf5-8c2d-ae69bdf9c876 | -13.54021 | -47.03577 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17f9a282-9fed-369f-8d96-482237ba0afe | -8.8708 | -62.42747 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5500e2da-2837-39f0-980d-58caa0c0faa2 | -16.10634 | -48.0122 | 2025-08-21 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5620738f-522c-3494-84f4-500366b341cd | -8.84274 | -52.05069 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b94f473a-d0df-33a7-a892-b951a494e1db | -13.3871 | -47.49395 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 40b400ed-ec20-3138-89aa-74389cebbc8c | -9.91503 | -49.24931 | 2025-08-21 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
