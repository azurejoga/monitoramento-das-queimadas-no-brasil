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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbda6f2b-8b9a-3e11-8b47-fe2bd9f59e41 | -8.0377 | -49.8898 | 2025-07-17 03:53:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78ecd7d1-cd5c-3eef-97bd-762ba4124a4f | -5.66556 | -43.71474 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| f4f4f868-4201-3ff5-944e-b389e71a77fe | -3.38762 | -47.49677 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 868b323a-963b-3d89-bdde-685b7d4d47c2 | -8.11441 | -43.14536 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6f0506c4-a97d-3b28-89d0-7d35e456ad7e | -7.1332 | -43.40905 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b05f660b-7af6-3f0a-98a2-dcafa5805086 | -3.38842 | -47.48847 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73845a29-e027-3273-806b-671b1809fd5b | -6.84508 | -42.74854 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f06975b8-48fa-3566-b77c-bddde922d1f1 | -5.92766 | -43.37505 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb83cbac-5795-338f-ad59-9e0684eb35a4 | -6.93699 | -42.37721 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad03c727-c53c-3a63-8dd7-ebcda6e8963b | -6.8838 | -47.24113 | 2025-07-17 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3025f6e-84f8-3168-8971-46f8d1e1d67e | -3.04288 | -49.42796 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69f850d7-6c44-3686-8ae7-722f8a3e4a7f | -4.58949 | -43.31239 | 2025-07-17 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 103226c3-35df-3297-a879-8a47d1f05c27 | -7.61007 | -44.29809 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8161f335-88ae-332f-bc2d-b0e264ace581 | -5.79557 | -45.10571 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd427b9d-d6a8-3d7c-80c3-4f03be4abce6 | -5.65732 | -43.71335 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 33cc582e-5203-3f52-afb5-18788e2af13f | -5.53152 | -43.89048 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bff87b84-8d35-3421-bbe6-caedff1d1009 | -6.70956 | -43.91037 | 2025-07-17 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa1e7514-4c43-30a3-b910-38a8bf7073dd | -6.71165 | -44.32845 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 89a5903e-ab65-3a36-8d0c-252e1687d538 | -7.89553 | -44.49085 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef917923-286f-3107-9011-8b54a3698f1d | -6.56778 | -36.55647 | 2025-07-17 03:53:00 | NOAA-20 | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb67c547-1610-3786-b35a-f83a6601e716 | -3.04204 | -49.43299 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 760eb990-a433-3232-94f8-3bc9cc3b8ad9 | -6.8851 | -44.74712 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 183f44bc-82a0-3bed-9eaf-1ea8338e9d8e | -7.00399 | -44.21757 | 2025-07-17 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d9990d6-f4f1-31f0-8cb5-2ea8763d4070 | -6.8187 | -43.78597 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f52200-a8a1-30fa-b277-90b36266f3a0 | -6.88601 | -44.75014 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52fbfbd4-58da-3316-b535-f5730973b74f | -6.7321 | -44.33601 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5b10ccb-94c7-3d50-b4e7-3c413cc8ce98 | -3.38823 | -47.49304 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3a3441b1-5948-3dc9-ab20-549b01454033 | -8.08962 | -47.62177 | 2025-07-17 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef1c750c-d9ac-3be9-a5fc-2c8753792a99 | -6.71652 | -44.32531 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 17f51251-d2d8-3409-924b-26cbe40d6468 | -3.58545 | -47.52811 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3feab44-a4f3-3bb5-8d57-2bec939e6195 | -6.88439 | -44.7514 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab43fd2a-c03b-3345-a3ab-0a9fa2677831 | -5.65669 | -43.71704 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6af74e7b-6b21-3765-b314-f793fd395e63 | -7.21129 | -45.33354 | 2025-07-17 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 864f0ecb-95a6-3efc-abce-f1ba07ea9d08 | -5.44531 | -42.62703 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5304f564-e729-3d45-943d-7389f2bcadba | -7.23517 | -43.49708 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cdae9251-8253-3d5d-bc98-dece193efff8 | -3.3827 | -47.49212 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0b7a1128-d23a-3d92-ac90-66e1f66cb19c | -3.40244 | -47.5062 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afc828ce-e38e-3634-aeeb-831600cf1e6d | -6.70893 | -43.91402 | 2025-07-17 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97c73188-3a18-3148-bdfa-792c017f7a0b | -7.20485 | -45.32996 | 2025-07-17 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3552b733-b40e-3d19-987e-7651a06f0f68 | -7.61942 | -44.30298 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2c7d8b1-698a-3159-bcb0-9fed744dcf40 | -7.15146 | -46.09665 | 2025-07-17 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc527345-6271-3f4d-a112-d863fda850a3 | -6.52033 | -42.36907 | 2025-07-17 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc1ba18a-9d29-3648-9f6f-26ea59209211 | -6.84628 | -44.76602 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 497cb65e-1552-3b13-9275-0bfe8fe4ab57 | -7.2343 | -43.50224 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c36ae3e-c4dd-3301-b94b-6e9c3d58a3b6 | -6.72806 | -44.33329 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c458af9-0b86-3955-8851-7ebf47f6fba1 | -6.51886 | -42.37133 | 2025-07-17 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1182148b-e5cc-3c93-be70-59222fbb1012 | -7.2113 | -43.16001 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56515489-c2b6-3db5-9d23-f0cebeef1fa4 | -7.20931 | -45.33083 | 2025-07-17 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ed116e2-20e4-36f9-959d-e9be600912aa | -6.73228 | -44.33402 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0646c09a-5394-3601-bbb7-18b101f8ebfc | -6.87483 | -42.75794 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f916a78b-09c8-39cc-ba4d-a665084c0db2 | -5.79339 | -45.0911 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a858ea6-ae93-3d8f-a8cc-de5c0ec0016c | -5.79634 | -45.10115 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91ba345f-63f7-3b7d-9a1f-6ec90054e1e6 | -4.58593 | -37.80535 | 2025-07-17 03:53:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3fa01cb8-e68e-3fab-be7f-1a2d39306cda | -3.39693 | -47.50517 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0aac9f2-c2db-392a-9894-a1cf7a2640f2 | -6.85878 | -42.76041 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 816229ca-710c-35ce-ba6d-6a6dd32c38bd | -6.66091 | -45.19407 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d033c47d-ab5f-368e-b800-3adc6d3d59b6 | -6.34348 | -44.75064 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd1d9f73-aad0-3167-9938-7ec7465685cf | -6.37555 | -44.74704 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d7625a5-3e11-364b-916f-f03dec473f2e | -5.44917 | -42.62766 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e2860c0-3552-3ff5-903e-adf26d414326 | -5.52865 | -43.88208 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd0bd17a-f6d4-3c4b-9b5f-a4befa9ddcc1 | -8.11824 | -43.14601 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a47a828-7d01-3f0d-9f39-869ab489647c | -5.79107 | -45.10486 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8f493f5-052a-3883-a6d1-51141f9504fa | -6.34064 | -43.74839 | 2025-07-17 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a332b27-365b-341e-8068-9c75416e6f87 | -6.84554 | -44.7704 | 2025-07-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0c2652c-f30b-344e-8e8d-3040f0f5d104 | -7.03687 | -42.10806 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 262d65e6-8601-3dd3-b2a6-4ba0fbe9cc72 | -7.70178 | -45.88049 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d46965c9-8f89-35b5-b95d-4230b0b5c0ec | -6.94889 | -42.37457 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8bdb76f-f26a-3783-984a-4115282f0e22 | -6.3792 | -44.75198 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 877190bb-d9bc-3550-b9f9-c3230d89d9a5 | -3.38884 | -47.48933 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70022d77-6a2c-32e0-8349-06fc928d5570 | -7.052 | -43.48877 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d30c9a0-f3db-3009-9036-1ab0e6507325 | -6.99669 | -43.74508 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d0e02a5e-901b-3223-bfab-a141c9e98c92 | -5.65606 | -43.72076 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| bbda500a-f739-375e-abdb-5691ddb4097a | -9.58559 | -40.34514 | 2025-07-17 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2f911540-a3b0-3a59-9fcb-911792bc8650 | -3.40794 | -47.5073 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a493764a-4f4a-300f-93aa-7a0cb0dd0832 | -8.75327 | -46.59085 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0bf024a-6305-372d-a901-3e7153af3cc3 | -7.05321 | -43.5306 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27fb3e24-043d-3834-bf0a-db0914ce7362 | -3.38479 | -47.47655 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0c5b38bf-5da2-3bbc-bef7-3a1f020fa268 | -7.20236 | -45.33179 | 2025-07-17 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2187320a-b9e6-3333-bcd6-afa52f152cc3 | -5.51266 | -41.32502 | 2025-07-17 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c7fc2865-d91d-35f1-b733-4ca22d49b646 | -5.65794 | -43.70969 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 93d5c5bf-2909-380b-8a11-81efac76ae8e | -8.75235 | -46.59598 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a294988a-48b4-3695-831d-a425eada4527 | -6.58335 | -41.44966 | 2025-07-17 03:53:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f51565f-c73e-388d-8f0d-6d41bc380b67 | -6.82336 | -43.78304 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbf511ae-978c-3263-9881-a04b6e9a1e03 | -6.97993 | -43.74583 | 2025-07-17 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dccb11d7-a451-342e-821b-39324a894a7d | -6.72431 | -44.33064 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 297c19a7-625e-3f33-a70a-12f73aebdfd6 | -3.38353 | -47.48385 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 640fc0a7-c20b-32c7-ae79-6777b21fccd3 | -6.88184 | -47.24023 | 2025-07-17 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01fabec5-16ca-3ac9-9cb3-0c3550ef5a52 | -3.39808 | -47.50235 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebff7031-70b0-38cc-8b21-ddac08aeb1da | -8.0983 | -43.14752 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cad494b0-7fc5-333b-9993-d4984f4bbad1 | -5.78967 | -45.08569 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12637004-275b-332e-a156-ef6eb268ebe7 | -6.57002 | -43.47902 | 2025-07-17 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f692663a-4179-3376-90e2-100b42b0bc77 | -7.3499 | -44.19962 | 2025-07-17 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 329e7622-7274-35a4-8cb1-bb74e4201791 | -3.84736 | -47.75577 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8adb2ac5-56e3-3a32-9bed-873d7bc30d26 | -7.5872 | -46.33551 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f09d097-bd9d-3fe7-a128-e8d73229b17d | -7.57067 | -43.95665 | 2025-07-17 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1699fea-43a5-32e6-90b7-aae1c2723ff4 | -7.21378 | -45.33168 | 2025-07-17 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ae74315-5b19-3b3c-a07c-07facf48c518 | -9.48934 | -40.39567 | 2025-07-17 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7a3e93b-02bb-3ab9-81db-4cf6b07599d5 | -8.23885 | -46.2085 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc0b473e-f129-3ad9-8a37-80c948dc8dff | -6.72738 | -44.3372 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 75c77b09-70b2-3151-a25d-7117ea020e89 | -6.67254 | -43.03842 | 2025-07-17 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
