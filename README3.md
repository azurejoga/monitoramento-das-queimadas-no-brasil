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
| 17f9dc3b-49bf-3cb6-96fe-060ee9a59ecc | -11.03761 | -44.32142 | 2026-06-06 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1930eff-d375-379c-9f80-5a18a2738169 | -12.50479 | -46.28339 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c715753a-39d8-30e5-8f59-9311f914e670 | -13.3638 | -43.20049 | 2026-06-06 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 840e1952-a262-3b32-ba3e-f63eb8670580 | -12.5074 | -46.30395 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86d89291-cc40-34db-aa37-9b0a2c68f0a2 | -12.06018 | -45.98757 | 2026-06-06 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32ab898d-84fb-3c4c-bd39-8fc309ab75aa | -12.06188 | -45.98664 | 2026-06-06 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 314a9777-1afd-3de8-b9c5-547b434b2400 | -12.5021 | -46.2963 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 480f5494-d763-3741-82c3-b27a33a77d5d | -13.40081 | -46.60297 | 2026-06-06 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cbe79b84-660b-3175-bb66-db07a10b0827 | -12.5087 | -46.29773 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be8e7750-e828-3045-b0b4-c2ebe3e6664b | -12.00359 | -45.35365 | 2026-06-06 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0559cb3-a829-3e8a-ab03-b0c27fd3da63 | -15.31538 | -41.9016 | 2026-06-06 03:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 725636dc-30ef-34e6-9624-362a46681640 | -11.04363 | -44.32271 | 2026-06-06 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f75a0095-4c36-38ad-9690-354a9a13e624 | -12.52045 | -46.27441 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c5fe442-cde5-37c0-8fa8-9664036437ee | -15.17918 | -41.81306 | 2026-06-06 03:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8e480b39-6e9c-3c49-943c-aac5c524ce74 | -12.06305 | -45.98091 | 2026-06-06 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42301126-ea71-390d-8efe-e973721e6911 | -13.3631 | -43.20406 | 2026-06-06 03:32:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7ac9e6c8-998c-31a5-a28e-c303bcb54b48 | -13.30773 | -43.76994 | 2026-06-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bdd05d0-7758-3fb3-b916-6f13211c4324 | -12.50833 | -46.26649 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eff58b95-6fe2-3f18-8c3f-703389804e29 | -15.31645 | -41.89613 | 2026-06-06 03:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5ca3d4f-45bd-3b53-8d55-207ce0eb131a | -14.23817 | -47.97816 | 2026-06-06 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b710c54b-f392-3e0d-ad9c-5f20a5a02111 | -12.00791 | -45.35219 | 2026-06-06 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f0c462d-994e-3567-af3c-b3c85304410f | -13.30423 | -43.76996 | 2026-06-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ea6b91-d46f-3ccb-9328-b89afcccf964 | -14.23058 | -45.80986 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4366e390-96ca-3d43-baae-e13f3616bc37 | -11.03624 | -44.32125 | 2026-06-06 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f853e9c9-9a17-3388-9547-7db281ecd061 | -14.22646 | -45.79845 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 191acff3-20d2-35c1-8d82-8f7600a9ed5c | -14.22131 | -45.79201 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c17b341c-3ce0-3d68-9a92-a25da085b544 | -12.51655 | -46.29318 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71263bc6-12f9-3849-9e6f-51d7ffa8879d | -14.24254 | -47.97756 | 2026-06-06 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f47a2fad-c5c3-3fa1-bd39-50ca0291f18c | -8.93519 | -45.67948 | 2026-06-06 03:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2017fcb7-8048-352c-823f-4aebe4003a6f | -13.30695 | -43.77383 | 2026-06-06 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 015e7e72-f270-32e4-bba3-e35c42a312c8 | -14.22026 | -45.79695 | 2026-06-06 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 356fddf0-d727-3065-ba03-eaf12f8df896 | -12.50082 | -46.30239 | 2026-06-06 03:32:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1cfea00-eaa3-366e-b091-0ce19d0295f6 | -14.23449 | -47.98047 | 2026-06-06 03:32:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 934dc9ea-b9e5-3901-a0d7-107bd1088cad | -17.30478 | -42.64988 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3fcc283b-033a-378f-8472-b2d0e43aac5a | -17.31967 | -44.91855 | 2026-06-06 03:34:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56bb25c6-e2c2-383b-91af-aa5167b096fa | -17.30102 | -42.64331 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| acab8795-e0b1-3d46-beff-bcef8006d5b0 | -18.86927 | -47.64495 | 2026-06-06 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ec0422b-70b1-340e-931c-18363d7d6361 | -17.30935 | -42.64221 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24c1be70-5bc4-30a1-a2e2-6f74bf33160b | -19.43443 | -42.57042 | 2026-06-06 03:34:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ff017c69-9687-3819-b6fb-278a2636d854 | -17.30821 | -42.6478 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87159018-4844-3092-9e6a-2fd8127c400c | -17.31072 | -42.64529 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d08a7d5-0351-3800-8334-d70c3706b5df | -21.52411 | -48.62357 | 2026-06-06 03:34:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba05c07c-f860-30bd-a834-486a2ab3fbf4 | -19.68145 | -43.92633 | 2026-06-06 03:34:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf67092-34b9-3dca-84b2-8250eebe3d8c | -17.31882 | -44.92253 | 2026-06-06 03:34:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9eee382f-1b57-3938-9ede-6fd72965f75b | -17.30588 | -42.64427 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ab6fb45c-d022-316e-9967-2882388879ba | -18.86771 | -47.64578 | 2026-06-06 03:34:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c613d27-34c3-3b18-95cc-f1bc589f0f1d | -19.43905 | -42.57148 | 2026-06-06 03:34:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9a641913-d619-3380-bd42-01cebe9fc2ef | -17.29994 | -42.64884 | 2026-06-06 03:34:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b6a68346-865a-39c8-8e7c-254fb7ee5410 | -11.5499 | -52.7867 | 2026-06-06 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e894e893-89c4-3226-a2fa-78a1db46c408 | -11.5496 | -52.8076 | 2026-06-06 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 6ecc07af-4ec4-3abe-8c3d-ccfb6abe6554 | -12.5103 | -46.2863 | 2026-06-06 03:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cf4202cc-4e8d-3ac1-b1c5-1af4d53ad32f | -11.5499 | -52.7867 | 2026-06-06 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| e6b889f2-9312-33e7-82e4-2209fe866bb5 | -5.4945 | -37.24368 | 2026-06-06 04:04:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9c513070-ac0f-3252-8463-c58c485acf9c | -6.99333 | -42.87939 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 459c3d18-0bf6-39e6-a0b9-9aab9e3afbee | -7.15461 | -44.06158 | 2026-06-06 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd587cf-347a-34df-b24f-9209986db211 | -6.4384 | -44.58751 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa2e4d5f-caf8-3b5f-b8da-bf51a21c7481 | -6.9895 | -42.87872 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 11eada41-167c-30e4-be18-7364150cf4f7 | -6.43185 | -44.57381 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6292082-97d2-3fde-add4-bec325006749 | -6.82676 | -43.39761 | 2026-06-06 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d23fff5-0a70-38ba-8934-ff249a64fc2a | -6.84942 | -44.9696 | 2026-06-06 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f458103-2ba1-3092-9149-cea2f44a1844 | -5.30459 | -47.24308 | 2026-06-06 04:04:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1de6ef7-026b-3004-8773-0281a70d3641 | -6.98489 | -42.88279 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 39a6aebf-20fa-388c-b90d-194c34edfded | -6.43912 | -44.58329 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 406ee3c2-86a6-3ae3-bb20-879c50688298 | -6.99124 | -42.87698 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 52aa2343-4b7a-38f9-9fc4-4829479d99d9 | -6.4355 | -44.57847 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f0e7484-1590-3d6c-abf7-ead6b34cd33b | -6.45123 | -44.56418 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf09d4f9-1dce-37be-b7a9-4d7ef2e89a2f | -6.44622 | -44.56761 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8355f708-01c1-3d78-8ca3-d92ba7ea29f1 | -7.00197 | -43.86092 | 2026-06-06 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3774b452-4e13-3a27-b3fb-c088f59a8cdb | -7.15873 | -44.06229 | 2026-06-06 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58f37377-4b31-3d5a-8b17-d8856d427cec | -8.45734 | -47.00618 | 2026-06-06 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 419af4da-cb91-38ba-bc7c-dd49ce41c2fb | -6.10943 | -45.8523 | 2026-06-06 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58a389e2-98f8-3b09-9e29-d54fb0e29349 | -7.34605 | -49.83418 | 2026-06-06 04:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d074e87d-2f29-308e-9d9a-5affa9a93dd8 | -3.98426 | -47.9331 | 2026-06-06 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d257eaf2-29eb-3b9f-bc56-4010defb09b2 | -7.35208 | -49.83526 | 2026-06-06 04:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 322e1b69-93fb-3717-aeec-6de557740f26 | -6.98411 | -42.88751 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| cf633437-599e-335c-b0ff-fbe8d35bf8f8 | -6.85455 | -44.96619 | 2026-06-06 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3363d34f-1259-3565-a0e5-475a0dda8c10 | -6.98276 | -42.8804 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 025f27bd-3cec-37d3-8dca-be6c199d53f8 | -5.41435 | -44.31273 | 2026-06-06 04:04:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad395933-6003-3353-b672-11aa796f065a | -7.00136 | -43.86452 | 2026-06-06 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 233e666c-92e4-3bd8-bcb3-20cfafbb01bb | -6.04293 | -47.89296 | 2026-06-06 04:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c200edf5-4ccf-3dbf-ad05-ba36f30261a3 | -5.55717 | -43.97375 | 2026-06-06 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd90d519-26d3-3ea3-b967-fc0a832f8c6c | -7.33252 | -37.43233 | 2026-06-06 04:04:00 | NPP-375D | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee04be94-2713-36d1-9b16-213b3bdacbda | -5.55297 | -43.97303 | 2026-06-06 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1e5c2a0-9032-3402-b9ff-a0e2188e66cc | -6.72607 | -44.37031 | 2026-06-06 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa36db9a-44fd-355d-adc5-1ed7657c7bab | -7.15809 | -44.06607 | 2026-06-06 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e8b96a8-389a-3a9e-acf4-becd2d516dc2 | -3.98993 | -47.9339 | 2026-06-06 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9161af78-afbe-3bf5-85e1-5f398821ea56 | -5.81272 | -43.78952 | 2026-06-06 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e6db3eb-0c41-3ec3-96b6-46931238dcb9 | -3.05916 | -40.85053 | 2026-06-06 04:04:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8882394-feb4-30b2-9829-0f6fa2f9bc82 | -5.35184 | -45.18657 | 2026-06-06 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 085d518c-50e5-3114-81d9-154bd6c424e5 | -7.62828 | -50.04505 | 2026-06-06 04:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8833f48e-d91b-3298-8a92-5defa26f17b7 | -5.44756 | -44.81223 | 2026-06-06 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a2ee53b-a903-3b20-b81b-8847c27108e9 | -6.99044 | -42.88168 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 76e92675-cc46-3520-82bf-0e700721c131 | -6.9858 | -42.88573 | 2026-06-06 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6dad3550-2291-3848-afac-1cfce88b885d | -6.72115 | -44.37369 | 2026-06-06 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f04507f5-c231-3ec7-95c1-c21c1be21265 | -8.46327 | -47.00143 | 2026-06-06 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ced2bb7-1b16-3a38-96bc-0f6cf2ccacea | -6.72539 | -44.37439 | 2026-06-06 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2523a7ed-5ed0-3a6b-8fe1-900d8de53156 | -6.85004 | -44.97178 | 2026-06-06 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cea06a46-80a4-34c6-9a9c-24fab167d43e | -7.62913 | -50.04044 | 2026-06-06 04:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75b580ae-219a-37fd-ae54-da271e977d34 | -6.85074 | -44.96762 | 2026-06-06 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2f481f9-7466-3086-9c4e-bcac587a01a1 | -6.44691 | -44.56351 | 2026-06-06 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README4.md)
