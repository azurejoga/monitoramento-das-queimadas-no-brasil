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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74b224bb-32c2-3895-b885-b2cf27a8b1df | -5.97461 | -44.35834 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b16b6ffd-623e-39e4-8f11-6f7d17c9bee6 | -6.64005 | -42.78149 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| db77bb0e-b8e6-37a3-a1a5-e061d8def6ba | -7.43272 | -46.51495 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11c4cc18-4d24-3d9c-af5c-ea773b35be42 | -10.19017 | -45.53543 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5c7ce41-5e67-378d-bfb5-508066f7c9d0 | -7.02845 | -42.7696 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6ae56990-a7e6-3d59-a372-dec088525e19 | -4.87679 | -45.85603 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58c60075-25b7-34a9-96a7-b62952857442 | -7.74122 | -42.61547 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 63f734e7-102e-359a-b4ac-4a0f6d63479c | -5.92115 | -43.32269 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9320b8c-c894-31c3-ba62-c02de58a775a | -8.58404 | -46.30666 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 0be96274-c504-3446-ba46-7e23c439796c | -7.7192 | -46.2711 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b660b4b9-86b0-3f71-ba1e-41ef2f54dea2 | -4.31269 | -48.0952 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a2faf852-26e3-3df5-8115-30675b1171d0 | -9.05548 | -47.0134 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44e0f507-07fe-316b-a532-d3a9fbd7547a | -5.70861 | -42.62872 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 459b2b2d-240c-3e64-b863-4da06f020077 | -7.11729 | -44.17308 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ee7a405-55bf-355b-9df2-216a1552d1f2 | -8.8561 | -46.79853 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cacf00e9-4664-3fbe-aab9-fde1f96cf243 | -5.32234 | -42.65495 | 2025-10-05 03:53:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0c6a813-8899-3d74-9205-d068eefae8ae | -7.44771 | -39.22455 | 2025-10-05 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d196d343-cbb0-36ba-9249-05833c419f2f | -6.33112 | -43.46529 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3da8b5ea-79b0-3a2d-8456-ca84f73a3f66 | -10.27715 | -44.35214 | 2025-10-05 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c7a8d60-36f6-3041-8cc2-839f397904b8 | -6.66944 | -42.38646 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 865b24f5-9d19-3572-8f43-5c5d140928e2 | -9.06 | -47.01225 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fae49902-6db5-3672-87ac-1cff6d40c0a5 | -9.27829 | -46.00621 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90bc8e1a-51f5-331c-ae1e-426bb6f44f4c | -8.60302 | -46.28276 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 13f91f1e-3fa5-36e8-8427-e1146930b48c | -5.84558 | -42.8709 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| efd7951b-ad18-3ce7-9d2a-aaf6d8dc2a1c | -5.01097 | -47.2187 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01be4ac2-8a35-300b-b3af-694ec79dce4a | -5.25247 | -42.64096 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 603e0ac6-660a-345e-aaa2-5d3825f307f3 | -8.86197 | -46.85124 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd7fff04-9466-3f59-938a-8bc9450ba960 | -5.22606 | -42.98822 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 070160d9-8ef8-35e2-9f1e-5349879c71b4 | -9.30154 | -45.77135 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd39c094-b1e4-3f95-93ec-a8c9f5c2c226 | -5.2116 | -46.1855 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6329a03-0f49-386a-838e-f38a319714ed | -5.77632 | -42.94365 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dbb8df87-e8e2-38a5-b363-22335c57161a | -4.31407 | -48.08711 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cec9009d-4f9a-394c-bd68-80fe752c44b3 | -5.24853 | -42.64029 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9c2c4cf-3caf-3037-bd05-b62f30fbfb9f | -5.41629 | -43.99878 | 2025-10-05 03:53:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab7334df-2db7-3333-97f7-77f6afc27237 | -6.92165 | -37.43474 | 2025-10-05 03:53:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 38d4c17c-4178-3c1f-86ac-08c063860ee7 | -6.60071 | -44.32085 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cf886e1-ccfe-3802-8c61-3a648500fd2c | -10.62516 | -43.28394 | 2025-10-05 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0159c42f-9c11-3fba-abaa-1b64b385cde3 | -8.57836 | -46.31092 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e4b29cce-874e-3767-9648-366e1e88b2c7 | -8.14108 | -44.09725 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c8403d6-0872-3e7c-aa0d-764c746e6242 | -7.80374 | -42.5186 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ec1dde45-1f68-3e55-abcd-33f07f7adb78 | -7.03313 | -42.76541 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4a2bc4d-5974-3ddf-8e3c-b181049bedc3 | -6.71386 | -45.02005 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02aef1e2-8dcf-3622-b793-bfa99db1ccb1 | -5.18054 | -46.21693 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a749d22f-7592-309f-a028-9b8f807253ea | -6.14763 | -44.64015 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c3da426-46ed-36ea-bd19-78258aafb0aa | -5.87558 | -42.54224 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 879a82bd-0eef-3a48-9858-9e66102c2d40 | -6.06025 | -44.16802 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c9eac07-4fea-3060-b78c-10e626d0dc0c | -8.85457 | -41.1936 | 2025-10-05 03:53:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b835ab88-99ea-35b5-9ef4-7ad39714ce1e | -7.48777 | -43.02956 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fff48dbe-7d39-3eb9-91c4-ed0e9dee7c1e | -8.5506 | -46.27391 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2db6aead-d431-339f-a358-3088230b8d5b | -6.44298 | -44.15646 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6cebcbbc-4ecb-353a-b496-4a5bed76e1cc | -7.75603 | -46.31677 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dccbab1f-05fb-3eca-8ca7-95a2fc3a1410 | -5.88245 | -42.9103 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e4cdf4ea-b897-3a7f-be37-80ec4e184df1 | -7.48314 | -43.03272 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 372cbf5a-3ef3-3b38-a966-e2db42273a0c | -5.86714 | -42.52103 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a18e1acd-aba3-3070-b8c8-8920adc97529 | -9.32169 | -45.65915 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f46e7fce-4168-3ce0-b53e-316150bb9e77 | -8.41007 | -45.66656 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b94ebb19-7395-3674-bb25-f1769fa43f3e | -9.28671 | -46.01237 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d05a9704-178e-3d0d-b940-68ec9e2f21a6 | -6.09486 | -43.47851 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8da2905c-4d69-3db6-b195-318dd4573e6c | -6.43059 | -46.02603 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c637cf7-27a9-3b4f-83d8-7ad28eb4ff0b | -8.63259 | -44.90245 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6e7fae9-0506-3d7e-b2bd-7a4fd1eb584a | -5.99346 | -44.35305 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c72cdb2-b486-31f2-8866-88f7b9db6cb2 | -5.25263 | -42.97783 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba614b7b-1c32-3972-9b61-b711cb4fb3e1 | -6.32826 | -43.45747 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18fb83ab-9edf-363a-9e64-7049724d2a55 | -5.9695 | -43.51237 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33d74867-e84f-3406-8bf9-dafd26c5edb4 | -8.23081 | -46.8097 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 17614d35-1370-3718-bd48-713d6cec64a9 | -8.23575 | -46.8107 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 94085cdd-edc5-3fa5-9aed-6b65217992ef | -6.60503 | -44.32152 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bfdcf66-af28-3caf-966c-358cb5d5c05b | -5.92523 | -43.32337 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b883d4b1-dee2-369c-a7d2-089ef2d4d399 | -7.4262 | -46.5027 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9042a6bc-936f-38e5-b890-750687381a7f | -10.3918 | -45.41684 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e29bdd2c-3e9f-309c-a1fa-115a39df00d4 | -10.01268 | -48.26774 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad28fed-dfcf-300f-9724-652023c17c60 | -5.96881 | -44.366 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c987a36-2f67-308a-b2fa-f03214801cfd | -6.23754 | -44.27086 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cb4c594-7ba2-3d6c-93cc-2cf00d13ac63 | -5.71252 | -42.62936 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bdd5fcab-7244-3610-982a-6e58ebe72384 | -6.70152 | -42.16879 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c42685c-db08-384e-b751-9cb26d07a8a8 | -6.01874 | -44.02293 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 233f287b-e4c2-31ca-8a21-58cd0c7e868b | -5.87717 | -42.5326 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 81a1d660-07f3-3fd7-9d35-3254a645d67e | -6.70077 | -42.17334 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1d9c4996-c1b9-3845-9df3-ce8dde29888b | -10.1894 | -45.53982 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0243f699-2953-3e75-a497-5e9850869e00 | -7.51788 | -38.00787 | 2025-10-05 03:53:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 72f55a0b-9809-373a-9d0d-76f253607dd3 | -6.10311 | -43.47969 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ff4faa9-6b34-3687-bcdb-0570460912fe | -10.19468 | -45.53556 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 237bd8ec-642a-3d3d-a0ed-506823174b86 | -5.84386 | -42.88137 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0c75897e-74ba-3824-a6cf-778242255c9a | -5.78677 | -45.7937 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84087e75-6350-34f1-8c75-4276e2b85a32 | -7.72453 | -42.3898 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3e477fb-ac64-3f9b-99ee-ff5aca834ad2 | -6.07966 | -43.47653 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fffc8438-fa7b-34b2-a092-412b50d8ede8 | -7.15974 | -46.21603 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31016504-309e-3c61-8bd8-4ff47b25f566 | -8.13282 | -44.09574 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37766fa2-af0d-3edc-96f0-f285a05b654a | -7.78212 | -42.60048 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 00f5b398-a51a-3907-937d-0efddf4efb9b | -6.79076 | -42.28571 | 2025-10-05 03:53:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0566530d-072f-351b-b6ca-412142a4cc52 | -5.84301 | -42.88656 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c8f991e7-1350-3a49-ba6d-79c0bb39e4dc | -5.90099 | -38.48214 | 2025-10-05 03:53:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8907b9ba-132e-35a4-b710-ec8235e022c8 | -6.22167 | -42.92654 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0c84876-aad2-3ea0-b0a0-8543763e000f | -5.60951 | -43.11351 | 2025-10-05 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8b83e0c-1efe-3f18-8cf3-9e314f8e6d88 | -9.29294 | -46.00414 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 78a08701-1983-3cdf-8dde-c1d65906819f | -9.14926 | -50.06294 | 2025-10-05 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1b67271-7d5d-3433-a423-0c33bb0f8b28 | -7.05631 | -42.76945 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac401b25-d74b-3961-a502-3940fb0a3cef | -7.16239 | -46.21785 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df7213f8-67a6-3194-bb4f-4ae950141048 | -6.19145 | -42.72332 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d6f72fa-7fb1-3894-b22f-97a26a967044 | -9.20112 | -46.92123 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README40.md)
