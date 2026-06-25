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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42abd7ef-b1a0-3fc0-965e-c236904eb549 | -17.3449 | -42.6084 | 2026-06-25 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 05902b51-9ba2-3c94-8613-ae90523c6561 | -12.216 | -55.4968 | 2026-06-25 01:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6d4ef869-945b-3814-ad3b-692ce5aa8c90 | -6.9793 | -42.8798 | 2026-06-25 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 33b9b2fc-51f5-3a09-b357-bf00c04c2fb7 | -9.1933 | -45.3114 | 2026-06-25 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| af4d09ea-7624-3af8-ac97-73ea61d846d5 | -7.7498 | -44.6184 | 2026-06-25 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| eb476f6c-291a-33a7-9a19-f6f8351f4007 | -12.7373 | -44.4521 | 2026-06-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| b00440b1-277a-350e-bd1b-8d5007f4b3e6 | -12.7566 | -44.449 | 2026-06-25 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0dce5e8e-6969-3d69-ae29-d6af23589196 | -6.9791 | -42.9034 | 2026-06-25 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| c78c62a6-f1a6-34c4-ac3b-e10a44eed39c | -17.3442 | -42.6333 | 2026-06-25 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9e6545c6-d941-3960-a97f-b541a1bdf97e | -6.9982 | -42.878 | 2026-06-25 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 54695baf-76fa-3e9a-a6b9-111b26260a20 | -12.7566 | -44.449 | 2026-06-25 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 90271fac-066f-3102-846a-f0a858cad3e1 | -17.3449 | -42.6084 | 2026-06-25 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ad39dfb2-d413-3df9-b55f-187e9965f9bd | -6.9979 | -42.9016 | 2026-06-25 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| e4f14e23-5cd4-3a9d-948c-09259098a98e | -8.6889 | -47.8664 | 2026-06-25 02:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 42d39573-0287-36fe-b492-ab38b559fab2 | -12.7373 | -44.4521 | 2026-06-25 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e8872415-45ea-359f-8ede-428a3df16bc7 | -7.7498 | -44.6184 | 2026-06-25 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 6b8e62a6-7b48-3bb3-ad54-f4f3bf5a940c | -10.6061 | -47.1727 | 2026-06-25 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 216edeab-6376-3289-91ca-8a36d74f0797 | -8.6889 | -47.8664 | 2026-06-25 02:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 28db3e98-9235-3886-91c5-4deae1dc2184 | -10.6251 | -47.1704 | 2026-06-25 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 598ac21b-7ad6-31c3-af99-793555f4d41b | -12.7566 | -44.449 | 2026-06-25 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fc6cb458-360b-34d7-a410-0175f814d53a | -7.7498 | -44.6184 | 2026-06-25 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| def31a9d-c689-3c71-ab6d-b4d984ea1ebf | -12.216 | -55.4968 | 2026-06-25 02:10:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bdff431f-4a9d-32c0-8664-2b17e15da19e | -12.7373 | -44.4521 | 2026-06-25 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3e0f17d3-6ede-3632-8fd0-f8bb68961b20 | -10.6254 | -47.1481 | 2026-06-25 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 90828f9c-70e6-3515-8252-6236ed8464a8 | -6.9979 | -42.9016 | 2026-06-25 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 687ea3a5-abd2-3a4e-9341-a1ca6a95089c | -8.6889 | -47.8664 | 2026-06-25 02:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 03bceced-215b-37b3-9d2f-1f8956743fa0 | -12.7566 | -44.449 | 2026-06-25 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| daa07120-c134-32f9-8c79-93f7efe1538f | -6.9791 | -42.9034 | 2026-06-25 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| e91fc38b-3279-3e59-a7ac-066a555ecf9f | -7.7498 | -44.6184 | 2026-06-25 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| d38a8e07-c2f1-339c-8d96-1a6ec6e7087f | -12.216 | -55.4968 | 2026-06-25 02:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2afeb295-c5b3-3ddd-9dc3-26795a6ac1c3 | -12.7373 | -44.4521 | 2026-06-25 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| eacea9a0-46bf-3551-8943-e03aebd5ceaf | -10.3023 | -44.6943 | 2026-06-25 02:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 29ac63cd-d32c-39ea-9791-b028617e47a8 | -12.7566 | -44.449 | 2026-06-25 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3f8a08af-dba0-311c-88f7-2873e2fc6256 | -6.9793 | -42.8798 | 2026-06-25 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| bcc98a9b-ee31-3683-89a5-ef16ae88d88f | -12.216 | -55.4968 | 2026-06-25 02:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 24eaf249-fa61-354c-b43e-6ab58ff15589 | -12.7373 | -44.4521 | 2026-06-25 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 569d869b-fce2-33ee-8153-7e685e56ff7f | -8.6889 | -47.8664 | 2026-06-25 02:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a75bc9b6-458a-37e2-9571-9d17ba23bf94 | -7.7498 | -44.6184 | 2026-06-25 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1c1e29b2-05e8-3c03-a8fe-fca825a27cf7 | -12.216 | -55.4968 | 2026-06-25 02:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d3d275a5-dda4-33aa-9b46-3485fc548d99 | -7.7498 | -44.6184 | 2026-06-25 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3300eb70-51e2-3cbf-9944-707110bc9d51 | -6.9791 | -42.9034 | 2026-06-25 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| f6306451-7996-3112-845a-afd128db7d32 | -12.7566 | -44.449 | 2026-06-25 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 16ef18b4-1a09-3e24-8f8c-94f37b85a10c | -12.7373 | -44.4521 | 2026-06-25 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1f4065fb-2aff-3747-b45c-e3717ca1b217 | -12.7373 | -44.4521 | 2026-06-25 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ade4e917-c331-3289-b836-fa40f7b17e9f | -12.7566 | -44.449 | 2026-06-25 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1153ec28-27bb-3fce-952c-45b810feff6d | -7.7498 | -44.6184 | 2026-06-25 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4b99ac08-e0d1-36ac-b310-668eb316f8d5 | -12.216 | -55.4968 | 2026-06-25 02:50:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ddba9f78-f085-310b-91ac-ca22a38b5780 | -12.7373 | -44.4521 | 2026-06-25 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7eec5c61-0769-34f5-a197-c31d4c765cfd | -12.7566 | -44.449 | 2026-06-25 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1dc38394-d7e9-33fd-a347-d27b9b0d84ee | -7.7498 | -44.6184 | 2026-06-25 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ad6aad69-8f1d-3a3b-b370-0096bcae541c | -12.216 | -55.4968 | 2026-06-25 03:00:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 63571f9f-3829-3e43-b653-915cea71fe04 | -7.7498 | -44.6184 | 2026-06-25 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 9dde5fd3-1d3f-3971-8a7b-2368a257c536 | -12.7373 | -44.4521 | 2026-06-25 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 558dcb64-e673-35f8-8707-339709171054 | -12.7373 | -44.4521 | 2026-06-25 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7c6a46c8-2cd2-34d9-a7ae-60033aacb237 | -7.7498 | -44.6184 | 2026-06-25 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7a6a4272-8a46-36da-98a7-39af76b3132f | -5.5102 | -35.60101 | 2026-06-25 03:25:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66b28ae2-e8b4-3b32-ae2a-4d18689f2d24 | -5.51081 | -35.59734 | 2026-06-25 03:25:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56fc8470-7bf7-3269-834e-095f335264f9 | -5.64345 | -36.59386 | 2026-06-25 03:25:00 | NOAA-20 | ANGICOS | RIO GRANDE DO NORTE | Brasil | 2400802 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1b1fb38-e1b7-34b6-b0a8-4c52ee5db09c | -9.18613 | -45.3239 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3c238b5-b3e1-3e3d-b8e1-2e41350849f9 | -5.82212 | -43.58913 | 2026-06-25 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb2d3481-8620-3f32-9907-7c1bf39c5c83 | -11.9137 | -43.40886 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0dc177b-9c49-3f5c-b786-20e9cc009465 | -6.50651 | -42.22356 | 2026-06-25 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ac494de-2dd5-3201-bc44-a6a83ea50131 | -6.99239 | -42.8958 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| a9a33c2a-73ae-3b97-a0df-e926b81a6b54 | -10.29192 | -44.69376 | 2026-06-25 03:28:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 494d498d-6f2e-3807-bf49-6706ced9bc12 | -9.19326 | -45.32547 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2cebd109-901b-326e-aa60-ff862826586d | -7.00064 | -42.78101 | 2026-06-25 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f12c7f9f-6a5d-3399-85c7-ea1026b0b309 | -7.74088 | -44.61124 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e08b4b5d-aa61-3c20-967d-1334fa75df16 | -7.74668 | -44.61899 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c2ca8a6-4503-3216-8fd8-5c4e2bf1dfd2 | -7.7404 | -44.17414 | 2026-06-25 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5498f8d9-890e-38e4-aac3-20e0d4791271 | -9.21467 | -45.33013 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd307394-9f5c-3cc3-bf08-539945fbf6bb | -11.3158 | -43.3213 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a51126d-0a58-3c8d-a8b8-5af26ef73631 | -11.31478 | -43.32637 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da0c6217-2c2f-3b95-81ac-bcbc74379673 | -7.74404 | -44.63256 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d542172d-70dd-3f9f-a67f-662780eb9850 | -11.31991 | -43.33273 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c147ea2b-a0c3-3c54-91a5-289f8e7011c7 | -9.18382 | -45.32235 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69c09576-ff05-3deb-80e2-f3a0fbb09ba9 | -9.20039 | -45.32704 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c498053e-5f98-30e3-92d3-5cdd4ff0fcf8 | -11.24544 | -43.32622 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c75ccde-8ce6-381b-9275-b43c9694f232 | -6.97955 | -42.893 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e654d36d-7808-3b67-99e8-ab556502afd0 | -5.82088 | -43.59586 | 2026-06-25 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 607de5ea-2e9d-39f1-a150-c306701c6eba | -9.20753 | -45.32859 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 128f6c50-3bef-3c0a-9639-98a0ceea6b9b | -11.32091 | -43.32775 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eace0969-d9a7-360c-944a-a802a89a0561 | -11.90887 | -43.39846 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b60019a-52e0-3b20-9c63-aa61263cd566 | -6.97965 | -42.8921 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 10d7a5f2-322c-3ba7-9ac0-037f5887d234 | -6.99525 | -42.77441 | 2026-06-25 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61813cf4-13a3-3463-aa3f-051489a9158e | -6.98699 | -42.88896 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| d8c141bf-69b1-3c71-bc21-001a63d6b831 | -10.29328 | -44.6871 | 2026-06-25 03:28:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 24e58e3a-29af-3ae9-8447-2a99e9b29567 | -6.98054 | -42.8877 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6a0ad4e5-a7dd-3fe4-87da-32628885aeeb | -6.50556 | -42.22879 | 2026-06-25 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e752c3a6-9bac-3540-bb61-7d9b7a42368e | -11.24441 | -43.3314 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 920bd25c-d72b-36cf-b59d-8956b7bfa82b | -7.72554 | -44.1773 | 2026-06-25 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6febba3f-5784-3f0a-bd0c-0efe7e8b8d89 | -7.75243 | -44.62704 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b83bc783-18cf-3f79-b470-a101743e8533 | -11.90788 | -43.40328 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffbf173c-95f5-3fa0-b565-e0eb32bc9d43 | -6.9722 | -42.89634 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4df49928-f84e-3488-a167-f2030442a4a9 | -7.73825 | -44.62476 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 81c8a453-9ad2-34a5-bc52-8c927dcd681b | -6.98496 | -42.89976 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| a984ffff-40b8-3c4d-8c75-73d60eb518ed | -7.73955 | -44.6181 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5894b59c-2b98-3e30-a229-8f3e805cda98 | -5.75435 | -43.18829 | 2026-06-25 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f61bdf21-e7dd-3c23-81fe-79bdf24eba77 | -11.20658 | -43.35985 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50d0065f-838e-30b4-b560-549876f5da51 | -11.31377 | -43.33136 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d388f561-d85a-379c-bb73-e5ded13e5d16 | -11.2075 | -43.35529 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
