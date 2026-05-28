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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ae3b0d1-659b-33df-9fe7-b1bafd0a6e70 | -11.29808 | -54.02683 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6da3cb93-2573-31c4-a169-906545e47f53 | -8.40539 | -50.2485 | 2026-05-28 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39f3ae9a-cec7-38cc-acc7-a8ada6831232 | -9.34866 | -45.46727 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 825c9269-ec0c-3ca0-aa1f-9fca97e67dae | -11.47319 | -52.92387 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1ceb02f-374f-36a1-a27c-3f16989b6b9e | -6.53861 | -44.68578 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a91257c1-dd68-3be4-b0e5-d6c3f483af59 | -10.77876 | -46.90742 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c824c70-31d8-3eed-bfd3-2ebd90b9068c | -9.1675 | -50.0328 | 2026-05-28 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68fa882c-1e52-3668-ad04-c6cf02eb61ed | -10.44484 | -59.43234 | 2026-05-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf357cf9-e983-3eda-a115-b7f02fbf3521 | -9.27845 | -48.58505 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cdb8b34-90a1-3330-be89-b164c87da6b5 | -11.28935 | -54.01173 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b297575-fb0f-3e68-a52e-b55e633aecdc | -9.27791 | -48.58865 | 2026-05-28 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25c454d0-faa4-3086-893d-d1bee111a896 | -9.14683 | -51.28238 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d500ab35-5e3b-3f2c-8464-ff7f1293e86b | -8.91053 | -51.8522 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f051a0dd-b604-3799-8a4a-5fffb61f48f8 | -12.2677 | -48.80495 | 2026-05-28 04:40:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d3bb978-779e-3a8c-a4c0-4ac004fb2b98 | -9.60521 | -58.34044 | 2026-05-28 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 396dd971-c018-38a1-a25d-37791310f57a | -10.63237 | -48.32623 | 2026-05-28 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3b875e1-77c2-36e9-bd09-9e597c231dd5 | -11.44276 | -52.92359 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53077f61-79c6-3c45-8b27-af4d7d8737dc | -11.58933 | -47.45767 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| caa9dda5-fe3f-3729-9041-09e6b2404dbf | -7.0114 | -44.99071 | 2026-05-28 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02ecc29e-e2ef-3762-82ee-d12ef1cef7d8 | -11.59414 | -47.44963 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b41528e8-c5f6-3667-aef5-187fc27ad0e2 | -9.28854 | -48.58659 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e840cbe-a57a-33e5-b496-a5ebb7ca30ed | -9.14982 | -46.86154 | 2026-05-28 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0373ed26-30eb-33fc-a7d9-7917f70e2232 | -10.62909 | -46.90654 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 392a07e6-371f-3151-a0c4-5235c1bc58fe | -11.97044 | -47.37709 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 917a68b3-e67c-3f61-a619-bc01ebb19791 | -10.77571 | -46.90264 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3cda072-5d45-3eb6-908e-226ad18c4c72 | -8.68915 | -48.30634 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdb70763-51c0-341a-82d7-b64553c5e3a2 | -9.75664 | -48.06588 | 2026-05-28 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1910cb7-40a2-3e76-b4d8-5a67fe070d7e | -10.56863 | -48.0269 | 2026-05-28 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8baf33f-eddc-3499-a12e-c6ea322701d5 | -8.8985 | -51.8617 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5201e96c-c568-30c5-bae1-6e1353dff151 | -5.80235 | -45.1271 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49e59ce1-4f4f-3eb3-ac07-c3c7c55bae74 | -6.0339 | -43.9934 | 2026-05-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0d8fd7d-5d6b-320f-9d62-1fec851f510c | -9.13982 | -40.10775 | 2026-05-28 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 372d5eb2-4a6e-36c8-9db3-a904f8c7e1e8 | -8.72465 | -48.33421 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43e4705b-2ed3-3875-84a0-c26cf096570b | -11.2739 | -53.97045 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35b10710-a14b-303c-960e-679566f8f14d | -11.59712 | -47.45438 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 95e61975-1b17-3170-b2e8-83af08818756 | -7.9311 | -47.9677 | 2026-05-28 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3303d30-4afd-3964-8650-a1dc95a436cb | -11.82994 | -48.2134 | 2026-05-28 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49970692-041e-3147-a4da-8fc732f5e9a9 | -5.79856 | -45.12658 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad49ca1-341e-3ea5-b0da-b32774c0b20f | -10.77634 | -46.89823 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8cc0243-fb79-3548-b414-386572db2fd0 | -5.95907 | -43.49487 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 17bbd30b-d5d3-3f9e-b6b1-c4585902f122 | -10.14019 | -52.39926 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bd51f41-1cad-3956-a678-a2f7531e8573 | -9.09568 | -48.6499 | 2026-05-28 04:40:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d17657fd-b57d-3890-b123-675bea653830 | -10.05606 | -51.68185 | 2026-05-28 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9520cd9c-6456-397d-837e-cf461913b0ec | -6.03334 | -43.99726 | 2026-05-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b02fd79-8e0f-3f24-9641-4180fdc0d9b9 | -9.38875 | -48.43866 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25cb6bc0-3b7c-3acf-912a-2045af46cf35 | -9.35795 | -45.46495 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9574ecea-6b6b-3632-9e63-3a0b8199fe2d | -9.36255 | -45.46046 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e0aa8ac-d511-38dd-9c52-d4338d76ddce | -10.97743 | -44.6078 | 2026-05-28 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 456801d9-c61a-309f-b001-bc5ef5fa73b3 | -9.91562 | -48.24339 | 2026-05-28 04:40:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa0ac4b4-dc65-3a97-9a2d-018f0fdc861b | -10.62545 | -46.90599 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8bcac3b-a779-316f-92a8-0acb9c098507 | -8.1177 | -49.56704 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6463baaa-b3d5-3f55-86c0-323bd603f8c4 | -10.04137 | -48.68708 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69c2e0f8-89bf-354d-8df5-c1f2e5e73a5a | -10.62181 | -46.90545 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9690fb13-d9b7-3198-8b21-9fec59d48ceb | -11.83052 | -48.20952 | 2026-05-28 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56f73e8b-a30b-30b6-b414-8132493f7904 | -10.95394 | -44.17244 | 2026-05-28 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 978ecc9f-f4dc-3a78-a6fc-87353404556f | -11.59647 | -47.45891 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb04be59-07fd-3b1b-891f-4045c0af1de5 | -8.89508 | -51.86119 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88cc641c-dbfb-31f9-8ddd-910a9fdb45b6 | -9.44267 | -48.88967 | 2026-05-28 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f67600f5-6c60-367a-aa61-b7dd148e0c76 | -9.35182 | -45.4728 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3af5859-d615-3a97-aba1-cb8d0f1c82b2 | -7.00922 | -45.00546 | 2026-05-28 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 386e32ce-0fc1-315f-9faf-8d03912bffc7 | -10.64189 | -46.89537 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e73451a-d1d5-3769-a2f2-4fa676a50d18 | -10.1395 | -52.39864 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a528546-b68b-3e29-933f-9e04503ee419 | -5.48562 | -45.11964 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f678e2-9d7c-3f7f-aaa7-8ee915de2fd7 | -9.14741 | -51.27877 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90d436d9-1796-37de-a5ae-5d5c46a7547c | -11.59833 | -47.44597 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 722606b4-7374-3e25-bccf-a0f44fc00e50 | -5.78892 | -45.13923 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bc6f686-b8dc-3b71-bb82-4ad1165a85a7 | -9.04887 | -46.30639 | 2026-05-28 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ee60730-871b-3aec-b286-c90ce0dba6a5 | -10.97798 | -44.60388 | 2026-05-28 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26bf7a0a-6829-337a-ab3b-e37b55b2d561 | -8.52568 | -51.57781 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a89cba40-ab21-3a6d-8af3-cf8ff6baf3d2 | -11.99481 | -47.15731 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4ccb853-d775-302d-b891-d266da1140bf | -9.39213 | -48.43919 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552f470a-6b9e-36c8-b82a-0fbe04a737f2 | -8.72574 | -48.32693 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 86655867-58c3-32f6-af72-25d26767c037 | -11.30099 | -54.03188 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66d535a6-3151-36b2-b7a3-b662ee6b0ce3 | -10.65366 | -49.72644 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88406010-b84c-32b7-8efe-2e55e3bd24db | -6.54317 | -44.68398 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 028dbd90-52f7-34ea-ac3c-d01e8521f6c5 | -11.29732 | -54.03125 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d90ea26a-d822-313a-8707-e6ec723e0db9 | -10.62118 | -46.90979 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba885b88-f913-31c1-87e9-58f8a9132383 | -9.34877 | -45.4738 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fedd66a3-1d3d-3eca-ad8c-d9fdedfbd796 | -6.08229 | -44.00491 | 2026-05-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ec60f07-8191-3867-b885-55dcf0a4875d | -5.79719 | -45.13572 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40561912-7564-3fa4-8c85-bd128a7a8515 | -7.75395 | -55.34779 | 2026-05-28 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9987ff83-ef0c-3dc8-aeea-a93db1781bf7 | -10.70985 | -56.04223 | 2026-05-28 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8559994d-8cff-337b-b1a1-78cc164649ea | -8.73995 | -50.24145 | 2026-05-28 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75daef6e-35aa-3399-bfeb-f38c4a2537ad | -9.94246 | -48.02002 | 2026-05-28 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 850abf2a-7c24-32a9-b784-7fc6886a8ab7 | -9.73249 | -49.21756 | 2026-05-28 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebaab637-c2f6-3602-bd23-22447c227f0a | -5.79339 | -45.13519 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 465cc9e7-e868-36c1-8194-4a7c886db0aa | -8.30569 | -49.40546 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d71144a-1d09-3285-8b1e-6e40af01cac4 | -10.91463 | -44.18927 | 2026-05-28 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5debb243-5aba-35e5-a70e-13749c238f59 | -11.73209 | -56.83807 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d2762d5-5264-35ad-8502-8709ab6cda25 | -11.81133 | -57.35246 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2740dd9-b24d-3033-b62e-c7155db410ed | -13.21057 | -54.51785 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3352e224-e2cf-3e4f-a636-f97a2cd706da | -17.93253 | -51.33765 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aefa602-057b-386e-b88b-ce1714d40c06 | -13.19741 | -54.5064 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8de14ee-3cd7-3fd3-a117-d5fe850319f5 | -13.19816 | -54.502 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| befb2261-38ce-3af5-89ac-5fd5aab7aa50 | -17.93093 | -51.32657 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5866a3fc-5e4f-3f27-9ba7-d40e601713ee | -13.20614 | -54.52162 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88ebaea7-e61e-3a46-8386-6e684d8751f5 | -16.15935 | -58.47561 | 2026-05-28 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b16b71d5-7f8a-345e-a177-1d67eb224573 | -17.92706 | -51.32965 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3653ef2-e12e-3164-98bd-80b8eab7f90d | -15.7941 | -58.6462 | 2026-05-28 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d8728096-60c5-3c99-a53a-a87fe57b565d | -11.63618 | -56.866 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README9.md)
