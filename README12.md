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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fad79ee2-da3e-3d2e-bd8f-d9a70a002ca2 | -14.02252 | -55.14297 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 182f1e43-d8f8-39bd-99ce-75bfde04551d | -15.26277 | -51.48011 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c0a356a-0bee-3f87-ad45-b6b292128606 | -13.14706 | -56.81462 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9dd6d26c-2d80-36f9-b0bf-55afad68d49a | -13.85427 | -59.72801 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f72f898-c43d-387d-b909-e730daf18922 | -13.39411 | -56.9165 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c4a18e6-a2ba-3384-850d-84d18a7e8274 | -17.66806 | -46.68588 | 2025-05-17 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6d4825b-81e3-3ec0-a0f6-6b9ddc8f4a58 | -13.6205 | -54.88291 | 2025-05-17 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d011dc-8f8a-3fb1-9960-e7c8acccee49 | -13.38989 | -56.91571 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9a99e879-8dbd-32ff-a222-fafe472f494e | -13.82446 | -59.66552 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb6845ff-32ce-31a8-aa68-1aea06011f92 | -15.26721 | -51.47353 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00ed7949-84b2-3452-b1e3-4b79263d6ca1 | -17.57809 | -47.48806 | 2025-05-17 04:40:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 063b9f5d-f22f-3828-8fa1-c46e24e231dc | -18.95508 | -52.2453 | 2025-05-17 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57b7c98b-6287-3f3b-ad51-7eb6c0c3bc9a | -13.70461 | -47.17843 | 2025-05-17 04:40:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5fe117f-3463-35c5-9fcb-e139edd0b739 | -19.06276 | -53.45819 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a90f273-e620-3773-bf56-7a953ceb25fd | -17.76087 | -56.30787 | 2025-05-17 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e0835890-bb7d-3e6a-a60f-c584d862ca5c | -20.41473 | -43.55393 | 2025-05-17 04:40:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b58c360e-5061-3c46-9c1c-76b8c4c900e0 | -15.71405 | -58.82584 | 2025-05-17 04:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 857cb3f7-c853-3082-af94-946d6edbeded | -13.39482 | -56.91253 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76678e49-382a-360f-89d8-8265a5a729a7 | -12.44786 | -57.19892 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c8a25af-59b2-3d36-bcb3-b90a877033f4 | -18.95234 | -52.24108 | 2025-05-17 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e432d850-1a1f-3e29-9edd-8fbebf7a69ee | -13.0422 | -53.71688 | 2025-05-17 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f4793f-19a1-352e-a646-5a1e1fe9ada7 | -14.02411 | -55.13374 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68aaba3a-3d23-3950-8e61-1082e5bbe37c | -15.26334 | -51.47654 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad905228-8ccb-3570-afd2-98dc69493efe | -13.85041 | -59.72082 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba93d2d-7802-3af5-bdd5-d7f20914b6ad | -14.02628 | -55.14366 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0ca2fe-0fb9-304e-a20e-e1f0bff2f765 | -12.39822 | -55.01097 | 2025-05-17 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c3f122-dab2-3e2d-b62d-27e70817fdf6 | -17.22735 | -47.48723 | 2025-05-17 04:40:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d7175a4-12c1-3259-a664-6ec56a3b8256 | -13.06311 | -52.02058 | 2025-05-17 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0d6978f-8ceb-31e3-ac77-1116d0d9cd54 | -15.2639 | -51.47297 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50ec556e-8ea4-31af-9fec-1447549af89d | -15.27109 | -51.47052 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f45fd82-5f72-349f-81bd-6e0e07613439 | -13.82504 | -59.6625 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d5ec34-b2d5-3b3b-86bb-25f30896c7db | -14.01093 | -53.02134 | 2025-05-17 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d91a5d1e-f919-3cc4-bc99-2b17edf28901 | -13.13517 | -56.8082 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78659d0c-15c1-3aab-9660-9663237ef82e | -17.664 | -46.68528 | 2025-05-17 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 430c3f1f-08d0-3f04-83f9-a5cbc1808c84 | -13.1597 | -56.81696 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5bff699-42d1-3769-9db4-2d7059594158 | -12.64452 | -57.18826 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4520444-a1d0-3990-a19a-12024c0c0582 | -13.04926 | -53.71816 | 2025-05-17 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acadcbed-c392-3d2c-b90a-9bf6f6d953ed | -17.66448 | -46.68154 | 2025-05-17 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e45b2632-bf0a-3aff-b340-9c8297f90548 | -13.14849 | -56.80673 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 79109e80-9827-33e3-8cb1-e0ada8557e3a | -12.72303 | -54.97352 | 2025-05-17 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54fe1acf-c065-31a0-b282-98a055614b54 | -12.45222 | -57.19977 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a89adb2-5a3c-3d82-9f4c-823434d013ae | -17.75583 | -56.30951 | 2025-05-17 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 842df427-ce85-3eee-b620-fb6eafd4cfdb | -19.97744 | -47.19103 | 2025-05-17 04:40:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07c47ab1-e22c-36f0-be06-e7d334d1df0b | -14.02332 | -55.13836 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 070a1db3-d827-3149-a8bc-13ba7f251b68 | -15.56962 | -47.8536 | 2025-05-17 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41d61766-a64e-345c-851a-84e94986aa66 | -14.02707 | -55.13903 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02a8a195-45a0-32f3-8707-a605bdcc29bb | -15.26834 | -51.46639 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8040fd4-b6ee-383e-9933-d0e74bb72010 | -13.47305 | -47.44787 | 2025-05-17 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd7e9a28-e30b-32d2-b1cc-14bc7dcd39b6 | -13.04573 | -53.71751 | 2025-05-17 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de0063c6-e020-3d76-916a-9ff14ef8865e | -12.08633 | -56.89161 | 2025-05-17 04:40:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d95503e-301a-3231-ade9-152ee142319c | -15.26665 | -51.47709 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7945a011-88dc-3613-a0ad-029c18c892b9 | -12.64963 | -57.18493 | 2025-05-17 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 993086db-8461-314a-bcc4-e040d05e7c3f | -13.15548 | -56.81622 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6577df5-ce25-33f8-a096-523e62bf3d38 | -15.27052 | -51.47408 | 2025-05-17 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2eea21db-295c-3670-a47b-9f8b433fe54c | -13.84983 | -59.72387 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c14faead-3f77-3ea3-9663-d123c0370a8a | -19.06337 | -53.45446 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bd008cd-06ba-3e30-bfed-da0b2c0b4b1d | -12.68462 | -58.12651 | 2025-05-17 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99934024-7cbb-3859-8ada-ee46d2d6e3c9 | -13.39887 | -56.91203 | 2025-05-17 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e6e91ea-b142-3d3a-b38e-c5cbfc1bfd68 | -19.05272 | -53.45638 | 2025-05-17 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1d6c4f9-9941-362c-bb99-c50972d97806 | -17.26628 | -49.00618 | 2025-05-17 04:40:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6bf9205b-9904-3895-b615-60ca79cbcec0 | -15.59346 | -52.87088 | 2025-05-17 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 953aa483-c263-3fe1-bb11-5d0e202bedb7 | -18.92636 | -47.00144 | 2025-05-17 04:40:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccea301e-562f-3f7a-ae39-40f49682c80d | -13.84924 | -59.72696 | 2025-05-17 04:40:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae462b25-e51b-3af3-b8a5-f151a4b52b09 | -14.019 | -55.11859 | 2025-05-17 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7b9e74d-6c3a-34e3-9d3f-49e761fe1ecb | -19.11573 | -52.71107 | 2025-05-17 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc52c330-072f-3346-bbdb-2c6eadb85f65 | -25.18452 | -50.10706 | 2025-05-17 04:42:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 171666f9-620f-3b68-8632-b8b513311a4e | -21.60378 | -51.59815 | 2025-05-17 04:42:00 | NOAA-20 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a43be88-eea3-3e6c-a93c-7ec8aae63c4c | -22.17807 | -49.97131 | 2025-05-17 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f1639d0a-61b4-306e-9efa-8554de02195f | -20.9559 | -56.61149 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b26c63c-429f-3ed8-a3fb-42f598a9ebe0 | -21.60322 | -51.60199 | 2025-05-17 04:42:00 | NOAA-20 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 959f2231-777a-3b37-b6fe-6fb7a7f7581b | -20.19102 | -55.06396 | 2025-05-17 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84f29859-6065-39fc-bedd-7362565b4fa2 | -24.24354 | -50.74015 | 2025-05-17 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14ee97d6-c219-323e-882e-5df983bbbf99 | -21.96832 | -57.30491 | 2025-05-17 04:42:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fb12de3-6735-38e9-8246-cceb3f9a6a9f | -21.7272 | -48.4338 | 2025-05-17 04:42:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2cd8021-71c7-346c-89c0-84b6f9001af4 | -20.94936 | -56.60545 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1b51bf00-e824-3eb7-94b8-34fc3ff5aa96 | -20.95304 | -56.60617 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b6ea623a-729a-38d5-87cd-d0b3d7d37cb5 | -20.99652 | -51.79075 | 2025-05-17 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7d6e1416-2e64-3ff6-97c6-a6e9abaced4b | -20.94854 | -56.61004 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48528b50-4fb4-3dc7-9eae-925fe1578803 | -20.47581 | -53.67551 | 2025-05-17 04:42:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9e80562-a346-32a7-974c-71267ab54aad | -22.2095 | -56.19867 | 2025-05-17 04:42:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d95236c0-1a61-393c-b4fb-6600cd5c644f | -26.6138 | -52.60401 | 2025-05-17 04:42:00 | NOAA-20 | SÃO DOMINGOS | SANTA CATARINA | Brasil | 4216107 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e7414f55-2097-3d00-a85d-6f63a43c092b | -21.81575 | -57.55908 | 2025-05-17 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70149d16-a599-378d-8840-0827b0ae4377 | -21.60435 | -51.59432 | 2025-05-17 04:42:00 | NOAA-20 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68c30d28-5747-3290-ab17-e8b7f04ba079 | -23.59482 | -49.01144 | 2025-05-17 04:42:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 351aecf3-61e0-33c1-ace1-bb311e43d644 | -20.18755 | -55.0633 | 2025-05-17 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa98246c-4290-3f14-93ef-5f1d80e39f4c | -21.17345 | -56.48655 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1c7a1d4-25b0-3ce3-988b-41cbbeecbe54 | -21.8167 | -57.55402 | 2025-05-17 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1dabe3c-2a45-3404-a9e8-c18a41761f39 | -23.2958 | -55.30099 | 2025-05-17 04:42:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6848090-174a-395f-b11e-b1c356a3e24f | -22.53985 | -48.81306 | 2025-05-17 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8371ccf9-5b01-3b5a-a1d5-efbc272638d4 | -23.29512 | -55.30497 | 2025-05-17 04:42:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b808aec8-e734-3554-bf0f-3a2fae545811 | -20.95222 | -56.61076 | 2025-05-17 04:42:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 361020b7-8a2a-3101-a3fd-6dbc1eb02605 | -23.59418 | -49.01648 | 2025-05-17 04:42:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7887fc98-9e5b-3ba8-b735-fb54c30d82f9 | -29.15887 | -51.88924 | 2025-05-17 04:44:00 | NOAA-20 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d61ed56-95e5-338d-b724-0c9c0b721742 | -29.15471 | -51.89314 | 2025-05-17 04:44:00 | NOAA-20 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4473e282-48e6-386e-9335-fc22bf3717ab | -29.15532 | -51.88857 | 2025-05-17 04:44:00 | NOAA-20 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcdc58c2-37a3-3f0d-a01b-b96f53282f96 | -5.09225 | -44.80899 | 2025-05-17 05:04:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 53abf2c4-711a-3312-9554-97f529f7b595 | -5.09628 | -44.78412 | 2025-05-17 05:04:00 | AQUA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 7316f5f4-d36f-3e43-a130-67984c0ac561 | -10.39424 | -57.55608 | 2025-05-17 05:29:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70535ff2-4cf7-3367-ba21-740b27aff50b | -11.42491 | -54.29671 | 2025-05-17 05:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d1f25a7-ce54-3efc-bde6-5c925826018f | -7.95043 | -49.76595 | 2025-05-17 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README13.md)
