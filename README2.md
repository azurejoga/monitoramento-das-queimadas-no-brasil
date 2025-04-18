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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28b86085-89e7-3f3e-ad0a-5a4494b34d5b | -5.48259 | -43.33405 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47df99ee-33e9-3f44-8866-b72b423587fb | -5.65135 | -43.709 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137cd26e-43c1-381f-98fc-751fb646a871 | -6.95605 | -43.04223 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ccfb9df0-6790-344d-b68b-596e38ec8863 | -6.95119 | -43.04131 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 530582f8-e385-3d0b-a6a1-6e7773083ac3 | -5.8669 | -35.70154 | 2025-04-18 03:40:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20a18375-4309-3614-8001-cdca73088601 | -6.94728 | -43.03485 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be0525f3-ec09-3597-9293-b1609b020043 | -10.01295 | -38.58254 | 2025-04-18 03:40:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f995ed65-52d9-3d0e-9322-c3161ed20533 | -5.64558 | -43.71128 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8029aa6b-a6dc-3b47-adaf-26672329de64 | -10.55448 | -42.42076 | 2025-04-18 03:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 743683d4-2811-3300-ba0d-3e205ea2f57c | -5.16272 | -45.10589 | 2025-04-18 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c397de99-7f22-30b3-a887-8b63d1208c08 | -5.64613 | -43.70815 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6d26300-025f-37cf-a1bf-5e0a6fbd2a7b | -6.94634 | -43.04037 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d4e01e4-fbda-3009-892e-a5de7662cbd0 | -5.98344 | -37.27307 | 2025-04-18 03:40:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c39685e1-e705-353b-b594-407004e156c9 | -9.61878 | -37.03283 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d2aae87-d425-35b1-bcbd-d60e8ab5c393 | -5.65065 | -43.70914 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1ff0f9d-cc28-3511-8e0d-e1242fc8122b | -5.21147 | -39.50549 | 2025-04-18 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4cc1ebf-b23d-3bfa-a366-11f7d3a0363a | -5.64501 | -43.71446 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6415c3ce-41aa-38e7-a4b3-f17ec8feaf5d | -5.64543 | -43.70829 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ee024d9-4e49-3126-9cab-505d8041ef0f | -5.42215 | -43.19975 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b6b9878-9fe1-3872-ad3c-86ce4be19cbd | -5.4775 | -43.33316 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bae7199-6f84-3f5a-baf5-c480382e08d1 | -5.42163 | -43.20274 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce9812ec-c040-36de-a874-db6dbe5dea7f | -6.95452 | -43.03755 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 13840592-0ee7-3417-9d86-73e6d0bccfdf | -6.94967 | -43.03661 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2f582bda-9819-39fb-b0f0-cfc5767f4a63 | -7.07008 | -44.38008 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c14cf20-1a48-3063-ae5a-3010c3060e5f | -6.94481 | -43.0357 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1334ca14-4e52-3562-9459-85b9f00e15be | -6.95699 | -43.03672 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 292fd8b2-27f3-3f07-9119-c1a53c14461d | -7.07122 | -44.37375 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7651df0b-6f1b-3178-a87d-abcfe6e899b4 | -7.08126 | -44.37895 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aabfa402-f478-3e39-a849-c190b4a3c8b2 | -6.95213 | -43.03579 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f1c7726b-6d24-3468-bc1a-c85a4b50e5c0 | -7.07538 | -44.38111 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72efeca4-d7ca-3d15-9377-593965b2ac5e | -6.94382 | -43.04121 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19c024cc-2fb2-352f-b0b1-c96a5678c9e0 | -5.07037 | -37.71642 | 2025-04-18 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63eb4441-f50b-32bc-baf3-675fc9272c2b | -6.54699 | -44.47458 | 2025-04-18 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 623cb877-fbfb-314e-b604-0b5a7720f9be | -5.78558 | -43.62019 | 2025-04-18 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2af88d4-1385-3242-99ea-c2fe43a27f5e | -5.79127 | -43.61806 | 2025-04-18 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bf9a5cc5-ef5c-326b-b315-6e0cd73a91d1 | -9.6182 | -37.03642 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4f294829-6de1-33e9-8160-d050df31b50f | -6.95025 | -43.04683 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ce8d3b3-83bf-32d3-b3b3-0bb9a715b041 | -6.95353 | -43.04306 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6a60d8b-9b9b-3fff-a0e2-4cd5c8585c43 | -5.64436 | -43.71462 | 2025-04-18 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d3aca86-ee0e-3303-b739-79c0ad68404c | -6.5458 | -44.48131 | 2025-04-18 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3598abd-478f-3765-8439-20e1b2af2296 | -5.4831 | -43.33105 | 2025-04-18 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36978c44-73fb-385b-bfdf-20f90f39f825 | -6.5464 | -44.47793 | 2025-04-18 03:40:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 129af186-4259-368f-883b-dfe3a28e865d | -9.61485 | -37.03586 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0443aa5a-a20d-38d2-a2ac-195d591f86c4 | -9.84899 | -37.18898 | 2025-04-18 03:40:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ffea54bc-91a6-3310-9c41-85ae24c95a9c | -10.50681 | -38.33799 | 2025-04-18 03:40:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11725c0b-dbb1-39a3-bf6d-17f95f1da99b | -6.94539 | -43.04592 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdb4cd43-848c-3054-a1c1-42daacd7c5ab | -5.79074 | -43.62111 | 2025-04-18 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6bfcd8e-14a4-36ee-9fff-af6a43fade20 | -9.61149 | -37.0353 | 2025-04-18 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa4b73c7-3e5e-3c37-8c8e-60f3811cfee6 | -7.37821 | -34.88574 | 2025-04-18 03:40:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f90029c-7e5b-3713-9ca0-3dffd887920c | -6.94868 | -43.04213 | 2025-04-18 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b359de31-75f3-3c14-9e1e-360f5b6b78ac | -5.16202 | -45.10992 | 2025-04-18 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab13038e-37b8-3c32-8044-5e3749f4e854 | -7.07065 | -44.37691 | 2025-04-18 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffb5931a-c321-37ff-b43d-36964fbb8abe | -7.01737 | -36.6694 | 2025-04-18 03:40:00 | NOAA-20 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 055dff97-e273-363f-be56-3011c040ed49 | -16.67827 | -43.88502 | 2025-04-18 03:42:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c6240be-c592-32b7-a789-2d48ba94c9a9 | -10.96756 | -44.44457 | 2025-04-18 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a60f29af-3ea2-37a8-8cad-a14f5e12be19 | -10.96702 | -44.44747 | 2025-04-18 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43f5d164-2fb7-3575-a773-286aa563fd0e | -19.05293 | -44.35744 | 2025-04-18 03:45:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c022ff-5fa8-3c77-8533-e319fbb19b06 | -20.34675 | -40.362 | 2025-04-18 03:45:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e428dd67-6df7-3317-96e8-09ef6ecd441c | -17.09191 | -43.80478 | 2025-04-18 03:45:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c25056af-3bcd-3b1d-890d-1158fd50f561 | -25.18742 | -49.32673 | 2025-04-18 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c52c1a20-5e18-35e7-b631-58a6242c0b50 | -25.19263 | -49.32782 | 2025-04-18 03:47:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 80ef75f4-ce9e-36a1-b380-1ec1d2206550 | 0.69285 | -51.44764 | 2025-04-18 04:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e108ac0b-693b-3efa-8188-4774dbba8db6 | -5.15846 | -45.1072 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e02badbd-8f74-3f7c-b8b8-be798ff7c1e3 | -5.64817 | -43.70907 | 2025-04-18 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a202debd-3a1c-364c-90dd-5c3b52caef31 | -6.95496 | -43.03628 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2919468a-ddf4-376a-95c8-4e99142dde6f | -10.55689 | -42.42288 | 2025-04-18 04:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 899f7cda-1a2b-307f-ba4f-d20b0a2340ec | -6.01713 | -44.56261 | 2025-04-18 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f596ab71-f8d1-3307-9ea4-8f32fd2973c2 | -6.95844 | -43.04027 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93d23854-c200-3982-a487-0f673864986c | -5.1689 | -45.10875 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e19ced-0f80-3f06-944a-351d19865e79 | -9.61904 | -37.03332 | 2025-04-18 04:32:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ad9fcba-0821-38dd-8faf-20b12dc62067 | -7.0778 | -44.38171 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c6d67da3-9c01-3b95-b961-c582e42cfe2c | -5.79295 | -43.62093 | 2025-04-18 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| aa0bf320-d25b-3c0e-bd12-4666a23e0a28 | -6.95048 | -43.03912 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eaad60b9-cb5d-33e1-8cc3-5ee9d6e1cbfb | -5.7854 | -43.61979 | 2025-04-18 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77305718-96fe-3856-b958-6ccbf4dbb3ca | -5.16482 | -45.11208 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a8083ee-63a0-3e65-9e01-a821a9eeeb54 | -5.42602 | -43.20165 | 2025-04-18 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf7c530b-2d92-3e41-93cd-3a6ab5f49d83 | -6.95446 | -43.03968 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a65c66df-c65c-379c-bfb1-7391c94ab0e6 | -5.01132 | -56.17618 | 2025-04-18 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4b2919-4825-317f-86c5-aa8a8d1d3514 | -5.16193 | -45.10773 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62fcbb04-1ff8-32da-866b-2dc72a21cd0d | -6.95384 | -43.04393 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c92cd67-9032-3346-9af6-f2d1e6cef10a | -5.64749 | -43.71362 | 2025-04-18 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b000bf3-142a-3fa7-8b4c-94d88f7a1329 | -6.95098 | -43.03571 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fe6bfa85-7c90-3206-a3d7-8bfd21fd86fb | -7.08582 | -44.37834 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 743f99fc-42e8-3065-9ca6-10d603973848 | -7.08148 | -44.38223 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6fa4a71-bb87-37f4-bfb3-7ce5414f72fb | -6.54788 | -44.47288 | 2025-04-18 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3ac96e1-559d-3028-b0e1-987db2bb4ee1 | -7.07412 | -44.38117 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ffbe55fb-27f4-365a-bf3d-298940c00c66 | -6.94986 | -43.04337 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8a9b52d-1358-3497-b106-a533d01dcf2a | -3.48374 | -51.18737 | 2025-04-18 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 029ca8cf-cfce-3542-bd6f-ea0f7ba00aba | -9.61849 | -37.0331 | 2025-04-18 04:32:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 463fa916-4a49-3923-bf56-78c7c80c9211 | -6.62074 | -48.01874 | 2025-04-18 04:32:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df6c1771-7a77-3755-9dff-934483efbd88 | -6.94699 | -43.03514 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 08c570d5-4821-3e59-a96e-184d556f7812 | -6.55087 | -44.47772 | 2025-04-18 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cccca6e2-4209-3c99-90fc-58e6fe678e1e | -2.97596 | -48.68169 | 2025-04-18 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f156f91b-5173-3083-bd4a-a2ab9c8fa114 | -2.53572 | -53.95692 | 2025-04-18 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89967c57-5730-325a-9a3f-a57e23051faf | -10.48361 | -42.43175 | 2025-04-18 04:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bea67adc-904b-361e-91f3-802ac96c3eee | -5.48322 | -43.33377 | 2025-04-18 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4428e102-fe86-344a-9cf6-16bdbb102dd2 | -4.87618 | -47.4076 | 2025-04-18 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0716e2d-d8fb-3a5d-b417-abb23f6264b1 | -6.94588 | -43.0428 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c09229b3-f884-3386-94ae-59cfd125ed7c | -5.78918 | -43.62035 | 2025-04-18 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5dbd7ab-d917-3eba-bee4-0546c94ed8ed | -5.16253 | -45.10389 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
