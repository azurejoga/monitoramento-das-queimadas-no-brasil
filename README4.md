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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2968476-5743-3126-8b0f-35e4d7b3e995 | -9.31669 | -45.47985 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ac26cfa3-55c3-32b1-9efa-7d418e2247e1 | -8.30552 | -48.24235 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14104c90-e54b-32e0-bb19-cce68141b2cb | -5.41709 | -43.90294 | 2026-06-10 03:55:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51b36967-1696-3638-bc58-559a82a5e0ea | -5.83347 | -43.59139 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e22e1cee-1ff6-3d67-93d7-18cd35dd8cb9 | -8.30144 | -48.23409 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31b9c356-f82b-3287-bc7d-6f1d2bb1c774 | -5.73301 | -49.10176 | 2026-06-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffb95eb5-b229-3f46-8d2e-5014f7ae8ce9 | -9.31149 | -45.48346 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a04c0cfc-d1ed-3c0b-b7d9-e11249061b19 | -6.85845 | -45.42465 | 2026-06-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0c11f2e-67d6-35bc-8e21-619e79f3653d | -5.80437 | -43.79452 | 2026-06-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2463056d-6792-39e3-bc7c-22f676c21d0c | -8.32178 | -45.39431 | 2026-06-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 074466d2-c2cf-3d37-b957-257811e291d2 | -9.31959 | -45.4895 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4a98b67-8864-3d98-bf23-a12255854fdf | -11.93629 | -43.39601 | 2026-06-10 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0d7e129-589b-3174-ad6c-108df9019ff3 | -9.29974 | -45.47216 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 56c21b60-3eff-3635-a008-14a4ae84352c | -5.7338 | -49.09731 | 2026-06-10 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ff18eb0-08e9-3385-98c2-641db8268eea | -9.30051 | -45.46776 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 050d85d3-b64a-30ce-a175-6a0c3d1cc32c | -7.1024 | -46.52281 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49dbc328-d29f-395e-9c4a-a93598eda6e4 | -8.30429 | -48.24156 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd5b2f48-2949-393f-a37e-6061a442464b | -12.85392 | -44.37317 | 2026-06-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9e066341-8b26-339c-9f13-6b000b99429c | -9.29531 | -45.47134 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 2585b31a-9e00-3879-885d-eeec8c53a292 | -7.10443 | -46.51146 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea588768-05d0-395c-bfee-16d61226d62e | -9.76315 | -47.43102 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa920650-c467-3391-b0e9-fba2e115dc10 | -12.85481 | -44.36812 | 2026-06-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0bf36f66-86ab-30cf-b484-b2a3d1a1e794 | -8.99388 | -45.73798 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12452431-2dc1-3be7-9a94-694e92c22aee | -7.7242 | -44.16281 | 2026-06-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6adea72c-af5c-3280-ac3d-0d0a5e7c5c23 | -6.95902 | -44.55374 | 2026-06-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 533b090b-f5ea-3e7f-a195-de979b9e05d7 | -5.93427 | -43.48486 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 915be07c-5965-3ac1-9dc7-8cfb301e1fcc | -7.72098 | -44.56997 | 2026-06-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76360222-f3c1-38e7-92a2-c7a6ed4419b0 | -9.31466 | -48.96952 | 2026-06-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b5980fb-a9f9-3374-9e4e-b5fc55cbc1f1 | -9.76262 | -47.43401 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52c9d57a-2301-3fc7-b8b4-87e72560259b | -10.012 | -48.21594 | 2026-06-10 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e63116-e0cd-3a2d-9aa6-222d4fcf57a7 | -8.30078 | -48.23764 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2acc0cd7-b517-3c3c-b069-6221a3cc5d7d | -7.09752 | -46.51445 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c914cdf-a74a-3b84-9f35-83d33e4e10c2 | -5.76243 | -46.0464 | 2026-06-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0fe7747-c558-3e5c-92bc-0a4d67b35a03 | -11.93706 | -43.39145 | 2026-06-10 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a23ec5bc-62c4-3c6e-888c-0f346b1ba472 | -12.03062 | -47.80116 | 2026-06-10 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 097470ec-854b-348f-b4f4-5f5b5022e060 | -9.30706 | -45.48264 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5cec06f7-3787-301d-be82-d381c0171c00 | -8.30015 | -48.23327 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12100de6-4a4c-3ec1-85d8-94c37ba1a5de | -7.40106 | -43.8647 | 2026-06-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d212048-f0a4-3e0f-abe1-dd4077753219 | -8.8599 | -44.97828 | 2026-06-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22dc9a84-afe8-303e-a144-754b7901ef54 | -9.77358 | -49.75101 | 2026-06-10 03:55:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9858a331-4e7a-321d-aeb4-a0aaa3966345 | -9.41304 | -44.69442 | 2026-06-10 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c20c247-643c-34d8-8b75-f2cf7a51a191 | -6.86314 | -45.03759 | 2026-06-10 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0451ee6-7988-3e72-a440-ef119d1f0dda | -5.8252 | -43.59 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5550400-7e90-3a4d-85ae-bff593dccaec | -11.16437 | -44.68853 | 2026-06-10 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a2565ef-c023-38b0-a211-be19edb40e7e | -9.0781 | -50.60053 | 2026-06-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9a1602b-aac3-39a2-be80-cf61d507696f | -6.4491 | -41.74752 | 2026-06-10 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e463369-0eb4-3d5a-abf2-2a397a0d795e | -7.98929 | -46.05436 | 2026-06-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d89dd3a-3d99-3a53-afd2-b427141dc548 | -5.93488 | -43.48117 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04e188ef-3862-3f15-ac75-c56f65ad37c0 | -5.28592 | -43.95955 | 2026-06-10 03:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b3d4a8b-3c44-33ec-94a9-20fa987ade68 | -9.31226 | -45.47905 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9e39dc5c-3699-335d-8b89-36f36880cf40 | -9.32035 | -45.48508 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fd144c96-5eb1-3a95-90a2-ba232284b8ba | -5.76341 | -46.04084 | 2026-06-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8e48f70-ce64-3dbe-96fe-77b973b2259b | -8.29952 | -48.23683 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d899e1-2590-3cb4-b652-088e0cfcbfa2 | -9.29608 | -45.46695 | 2026-06-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9ac91970-c10b-3d88-96c4-1a4532941840 | -7.16618 | -44.07099 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b34625e-2a03-3ad6-90cf-7ad17c780512 | -7.10151 | -46.52087 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fad22afb-35fa-3b04-9a8d-c42aff3293cc | -12.85782 | -44.37387 | 2026-06-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9dd4594c-514e-3118-9ab3-b11d54ff87af | -5.76519 | -46.0451 | 2026-06-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2f5fd0c-48dd-3e46-995c-615b40e40088 | -9.3034 | -45.4774 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d72a0ba8-cb6f-34d1-98f4-375e4f3fe4f2 | -9.30783 | -45.47822 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| cdb445de-0b99-3dc9-9372-6c215a07b06e | -9.76262 | -47.43066 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbf8a2f1-d07d-3de4-beda-ba656685f7fa | -6.39289 | -44.17561 | 2026-06-10 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7251cb1a-cc27-3348-8f91-1e007a6fd7b8 | -7.75616 | -47.58328 | 2026-06-10 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 870c65fd-8953-3ba3-96c4-efabbbd7d9c6 | -6.44312 | -44.58023 | 2026-06-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf89a24-952c-34e0-8ffd-718767b176a7 | -5.82583 | -43.58618 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b6cfa8a-35f2-391b-ae23-0dc9a97e4e18 | -7.10342 | -46.51711 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd4a5e44-6e09-3f5a-ac57-51c1839b0e18 | -4.57125 | -48.0251 | 2026-06-10 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd414b0-5d59-3ac7-af44-638f089e97d1 | -7.14592 | -44.06357 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df68ec50-ba1e-3a37-bd4a-112eaa953956 | -9.77435 | -49.75212 | 2026-06-10 03:55:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74a2a55f-13e0-378c-bd05-45436fad9cf3 | -12.85091 | -44.36742 | 2026-06-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 16e9dbb5-9c6f-3fe9-a7e4-f1866be26595 | -8.29475 | -48.23212 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1664e13-aa4c-3e20-b0d8-3140b9cb2b21 | -8.29601 | -48.22511 | 2026-06-10 03:55:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb08c7c0-d415-3e3b-94f1-ba6dd9549c21 | -9.76206 | -47.43364 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e00b3034-b4ba-3403-b508-2bcf0892fb1e | -9.31392 | -48.97347 | 2026-06-10 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 22f34bdd-cefa-3418-8b47-bfc6f1093882 | -8.49934 | -47.0222 | 2026-06-10 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75e434d9-a41e-32f9-a760-1c390d761c66 | -7.09655 | -46.52009 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5baa4d1-b315-3c7b-8ec1-b7cfcf52228e | -7.16264 | -44.06641 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b42da389-9b39-34a2-85de-d11621b7b2d8 | -7.16683 | -44.0671 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e90085-a137-36e8-bf3d-e0480e320f6e | -5.82997 | -43.58685 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8268d7e7-8258-3bf6-bfc9-721b75571919 | -9.29897 | -45.47657 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad7154bd-f110-3df2-a9fb-7155dcd6e6af | -5.93365 | -43.48857 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16529c6a-5745-3c66-998c-f01386185257 | -9.76151 | -47.43662 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2725b93-e8dd-3f15-b108-54410b81a5ce | -9.7003 | -48.61074 | 2026-06-10 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a8340b-d75f-33a0-a982-45ef727e329f | -9.08208 | -50.60359 | 2026-06-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cfdaeaa-58be-342b-bae4-62cad0431c29 | -6.19426 | -45.1694 | 2026-06-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a2af15a-f829-32b4-be60-0d6bf1126aca | -12.02851 | -40.11895 | 2026-06-10 03:55:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 41db5a82-0f19-3c52-a648-a4aadb6194df | -9.32402 | -45.4903 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e80d40e9-9fbe-3b16-b0da-ebe857347baf | -7.09744 | -46.52203 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a94d743b-620a-31fa-bee7-01a237d5439d | -10.299 | -40.71395 | 2026-06-10 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6223f020-bd55-3d4a-b07c-51394c5a3312 | -7.22309 | -34.82669 | 2026-06-10 03:55:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 42c4fb30-da6b-3da8-b31f-6259abb98f0a | -9.74898 | -47.8772 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21f96d46-95de-3705-b8d5-d7655cbf74af | -7.26789 | -46.81283 | 2026-06-10 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f981371-2091-35f3-8f67-c0801be89d3d | -6.00702 | -47.07735 | 2026-06-10 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75ae5906-0d0e-39b0-ab59-86539686f304 | -7.16198 | -44.07037 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06159371-f612-30eb-98e1-2b6510c7b409 | -6.78346 | -39.19231 | 2026-06-10 03:55:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b214f51d-32a2-3846-b2fc-771ccc54f2af | -9.21085 | -48.58066 | 2026-06-10 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3904ae1-bc63-351c-9a91-13b7b3aa1b49 | -9.30494 | -45.46857 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5b384e06-f4fa-36fc-9435-5dd6835f4f77 | -9.22449 | -48.56834 | 2026-06-10 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b38762da-722b-3670-b34f-e1ef19ec6386 | -9.3086 | -45.4738 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 16171b0f-c797-389b-a068-afaaa2502f9d | -19.41414 | -40.68137 | 2026-06-10 03:57:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README5.md)
