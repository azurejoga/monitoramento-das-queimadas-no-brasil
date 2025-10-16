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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02738fbc-bded-379b-a1b0-d49176664fde | -17.28484 | -39.27384 | 2025-10-16 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc4ce5bf-28e7-394e-a070-c3fd50af2a7b | -8.19898 | -43.31849 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d4916bcf-ae08-3d78-9394-2f35258f3fa0 | -7.9525 | -44.147 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e081acdd-f71b-3236-b8de-0bf4cf8d064f | -8.46315 | -46.19273 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0da9de9a-484c-380a-93a4-77235783a9cf | -8.19848 | -43.32076 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 271a74cb-a8a1-3a58-96c3-1b2dbcccd9a3 | -7.16805 | -42.50994 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 664fbc8f-496c-3149-b221-b14704cb6028 | -8.47039 | -46.24288 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 741f178d-46e4-32b3-bf78-35a28b7a2d5e | -19.77356 | -47.97613 | 2025-10-16 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9c9f2a1-7b7f-3e4c-ad42-b7949a0616c2 | -9.155 | -41.05775 | 2025-10-16 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 199f52f1-51fd-37e8-b472-777041c6dc59 | -7.17043 | -42.18638 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ee73b61-f51e-35c0-b287-0fd55ff22e6e | -8.48618 | -36.69916 | 2025-10-16 03:49:00 | NOAA-20 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9f1dc762-d224-33e4-a0b6-4958c1028cdf | -8.4701 | -46.21455 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e1059d7-06a7-3bb7-ad17-58739ef09267 | -8.23597 | -43.41786 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68c0a3a5-ac7d-36f2-8251-804c2fc14dc7 | -7.21873 | -45.1702 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ea13ad7-59de-3a9e-8748-10c83d5f4c84 | -12.24029 | -49.38914 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48afff18-6fb9-3511-9f9e-82d0516fed63 | -17.28152 | -39.27327 | 2025-10-16 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48206590-5a08-3701-b0e8-bc1d7b15b059 | -7.22716 | -41.21646 | 2025-10-16 03:49:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1676cc6-06db-36d6-a911-7a99bfb244b2 | -7.39429 | -44.7497 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c279d19-c22c-367e-8247-6f45b2ff2b5f | -8.19147 | -43.97231 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bd3c366-0ca8-375f-8c3e-cf0d6902774b | -8.45667 | -44.18019 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| fa96e40f-fd54-3958-a342-d7de0c7e24e1 | -7.96903 | -44.13504 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d33d70cc-33a2-3106-bcca-69c348c0c044 | -14.1226 | -42.62728 | 2025-10-16 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc31c422-505f-3bc2-a3b4-14116eeedfc3 | -7.28482 | -42.95561 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57f23b3d-6a6c-3ec2-9bc7-b0d662b6cc53 | -7.93564 | -44.13388 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 342688bb-9c63-3bd1-afc2-a7c27af84c84 | -9.55935 | -36.89444 | 2025-10-16 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e06a4484-9e57-3773-802e-2c84a00c89a2 | -15.78706 | -43.65252 | 2025-10-16 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09052e5b-04bd-32b6-99ba-59f80be3ba99 | -8.21859 | -44.00365 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e474020-bd88-3cc0-853e-03a10621df58 | -7.40899 | -44.75233 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8749fd07-537a-39f6-ac9c-8caae659ae93 | -7.17394 | -42.19082 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3da47f2c-251a-3b04-ba32-df81b4b6ecd9 | -8.07142 | -45.43532 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f941a25-e853-3187-ab86-b52898a89ae3 | -7.93099 | -44.13305 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08af5ce0-fb81-3873-a268-7d90b4b0f6b1 | -8.21109 | -43.99253 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84db5ee0-4069-3a51-a3e7-eb1823578865 | -6.94757 | -42.6841 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0e3fab0-149e-34a8-8932-231f6845d1d0 | -8.45977 | -46.24088 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6463d366-24e4-34dc-be79-ce18b9255cc6 | -8.26469 | -43.35657 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 73daa452-55bf-363b-966b-82e35c5815d3 | -13.22802 | -43.39838 | 2025-10-16 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91f50b31-2c3f-3563-9e4a-3989a3f612b4 | -8.2026 | -43.32359 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9b6ecd14-a3d1-38c4-84f1-8b4fca0495e7 | -15.02433 | -47.31765 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02fd27f9-e748-3981-a705-f0a93f87040b | -14.05091 | -43.54836 | 2025-10-16 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 441dc11c-f92a-31ef-9b13-ceb2bb3d1037 | -6.74767 | -44.94675 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bcef384-0ba8-304d-8e74-7ff5768cb89c | -8.18459 | -43.32278 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 71277cec-82c8-329c-baba-819e9fa0d7bf | -7.73117 | -42.46753 | 2025-10-16 03:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ae411e0f-ccaa-334d-8d9b-f6d773a0b7d5 | -13.67251 | -44.2834 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab6dd85-3ceb-325f-9124-ebca6f00ee47 | -17.20842 | -47.65701 | 2025-10-16 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0a1852e-248b-358d-8513-b0842c9bc2cd | -13.04314 | -43.02993 | 2025-10-16 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2b588eb3-05ff-37d6-89d9-6a6b09fa1781 | -7.48876 | -42.74298 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6703f64-c8b5-3f2b-9274-0bab28bcce68 | -18.7327 | -45.02423 | 2025-10-16 03:49:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72b34c55-333d-3fdc-934f-b06f929f42bd | -13.27511 | -42.4041 | 2025-10-16 03:49:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42b873b4-972f-385f-b80c-0fa1f723e12d | -8.25367 | -44.07425 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e27c9b24-bd47-373d-9f8c-f7d1177ef3cc | -7.03616 | -41.81512 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 929dc545-4984-3083-9442-6bbb0ea828a3 | -8.22524 | -44.01963 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2462f509-8ab7-373b-bc60-37c62e486464 | -8.83516 | -44.41155 | 2025-10-16 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e641fe5d-95c9-3968-8c1c-df2e20f74632 | -7.67489 | -42.56622 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 454bd9ab-3565-3114-804d-dd43b938e69e | -7.92494 | -44.12498 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d28314c-614f-3522-811c-5b5618bc7e37 | -8.46785 | -44.19048 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bb10a206-9def-3fef-8faa-34cd5f259a05 | -7.67111 | -42.56519 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bcd833e4-bcc8-3654-9078-7f0e49c06399 | -13.70194 | -44.58328 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cad63ae-3424-3921-a22b-5688d37e0a17 | -15.93191 | -43.52075 | 2025-10-16 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c91d3032-24ea-3c58-9ea3-2b6c8aa4c30d | -7.28895 | -42.31397 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 73fe934e-2378-3c39-86d5-40320aff6675 | -7.94582 | -44.13065 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4bc3694-862e-36c7-931e-5c3616705def | -7.47246 | -42.76117 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f8dd8ee9-c905-3e53-8a5d-d8f3d6b5948b | -7.29984 | -41.86167 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a07afca0-04a6-3d21-b8c0-e45a18d67043 | -7.56031 | -43.91396 | 2025-10-16 03:49:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e52b0b1-c6e6-349d-9e31-eb90de71d275 | -8.45799 | -46.191 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7f52016-3b8f-3305-9d19-94b21d5b70f7 | -7.30449 | -41.85872 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb47f148-8bab-3b4f-b5cc-cb844cd9862d | -7.85995 | -45.97589 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1e4bc85-236e-3919-9fa0-628cca71f6dc | -13.57446 | -44.44027 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6609f39a-9a17-34b6-b4e9-7e24dff3e25f | -8.40247 | -46.23454 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b2406db-71e2-3ee8-a57d-edad06c00411 | -8.20252 | -47.01777 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 504db0fb-740f-3db5-9107-c429125da8fb | -7.407 | -44.74623 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8077d2f9-e1b2-3eec-8db9-7eedc26ee5c8 | -7.62829 | -44.08814 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b4ff523-c4ee-345d-91c5-c9ea41ea7a98 | -8.25117 | -44.08865 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0820e0da-a866-3166-b075-3a84063b1818 | -7.20649 | -43.64799 | 2025-10-16 03:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428b6dc4-c987-33f2-bdc1-d4d0ff966a9c | -7.20684 | -43.83781 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd301b50-443e-32c1-a0b8-71170fad9d58 | -7.66712 | -42.38201 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bf5492c7-ae96-32ab-a334-dad3d289da59 | -7.034 | -42.73596 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a34db370-009f-354b-9c46-dd69880e04ac | -13.71624 | -40.98624 | 2025-10-16 03:49:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3aa71c4d-8705-31a6-9295-106b5f4e335f | -16.19498 | -44.2169 | 2025-10-16 03:49:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01440f65-7e62-312a-abbb-95e9fb80fc4f | -9.55881 | -36.89793 | 2025-10-16 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4227873b-ffd1-34af-aca6-e65222eaf88b | -15.96 | -43.01778 | 2025-10-16 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c453cfc-6cbd-357a-8b2b-3b18bc07e38e | -8.40187 | -46.23787 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46247b8b-d802-30b0-a563-1b92933dab3b | -7.40412 | -44.75128 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7cd0da8-7c73-32fb-ae4e-7fc6aa81e088 | -6.95069 | -47.74853 | 2025-10-16 03:49:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca951efc-4da8-370e-9610-a1983ba8b817 | -6.54819 | -43.92048 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15f2d24d-071f-315a-9c32-de264687a33b | -13.60708 | -43.57119 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d52e80d-40f1-3763-9ccc-29693eefa38a | -15.79666 | -42.02847 | 2025-10-16 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e15daad-b7c4-3347-9590-66ef4c696815 | -7.28961 | -42.31017 | 2025-10-16 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 950c2e21-289f-3aa6-bb59-126099405c03 | -9.15423 | -41.06231 | 2025-10-16 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 27c03e6f-a202-3033-a2a5-2321681c6cd2 | -7.67618 | -42.55853 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 83cd7d5f-0955-34ce-8f4f-fe612fabf1d4 | -7.15894 | -42.51238 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82a86878-0972-3e4c-9831-9c80dcc82aba | -12.23934 | -49.39376 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2bfd988-8db5-3ee3-9809-c823d60b041b | -8.24935 | -43.34062 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6b87b56c-4086-3981-8913-efaf3c7b0d85 | -13.72069 | -44.00019 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 230133cb-0383-312c-ba10-f84864e585c5 | -7.67553 | -42.56241 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee001229-d569-3907-8abc-3d6f830c0052 | -8.28575 | -43.38966 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 85015b20-ba75-352c-9fc2-4dda11947ee7 | -7.07472 | -45.44883 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f832c384-7551-39a1-9f3f-af15d5ddc8f6 | -8.19986 | -43.97583 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3850fe0-0c85-30b4-9cd9-c7e7a95976a8 | -7.29284 | -41.95249 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ace8f83-e403-3416-bf7b-238e56a40806 | -8.40907 | -46.2591 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25cc43ca-10f3-35f4-9fea-47edb7b983a4 | -7.20682 | -45.49378 | 2025-10-16 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
