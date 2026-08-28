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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 113170db-1b12-33ab-b7ab-d70fe624dfc9 | -3.1952 | -61.13823 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 443bd428-8235-32b8-98f4-13fe44c58bf0 | -6.84117 | -59.74108 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 00e995f6-a2e8-3101-8b7d-e7684a4a3d74 | -6.79494 | -59.40026 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 0b792cd9-df8c-3414-9554-e85154d9949f | -6.12427 | -57.82499 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 146f4c9b-e5e5-3401-9043-fe1fb9693bd1 | -3.28948 | -61.32242 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9044b814-56f1-3ed3-9a38-1d6fda2f06e5 | -8.60063 | -70.21347 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 300edfbf-1084-35da-a8a2-9d1b86e61b89 | -6.43286 | -55.52632 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd7d65cb-f697-3b0a-96bc-96091c11c869 | -8.80482 | -70.79106 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e3673031-68cc-3311-8ad0-7f431ef762a2 | -7.495 | -55.28443 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8852c838-acbe-348d-9e37-a9d01628eecf | -3.61262 | -60.53494 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 424b583f-3744-3698-8802-e914cac33c14 | -6.83677 | -59.95004 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3e0376e1-dcac-3642-a678-50296a97d811 | -7.64708 | -70.22049 | 2026-08-28 17:47:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1f8d0dc-aabc-3522-b583-d2733cff1c03 | -6.01791 | -57.7862 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ff093e3-8c24-31f2-9bab-509c7b1381d4 | -6.38706 | -65.23593 | 2026-08-28 17:47:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2bb9a58a-72b4-3aff-ab9f-027faf667928 | -6.91669 | -59.60409 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7779f57a-2cfd-301c-b689-d3c7d3d603bc | -8.15486 | -64.00562 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 89ed3346-3afa-3de7-ac14-9c2e29a0ecb4 | -7.5928 | -63.36375 | 2026-08-28 17:47:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| d2fe4550-f80a-3312-815f-b1ad29fedc8a | -7.66442 | -64.64925 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70f61d4f-efbc-3d2e-bb84-76435f6b697e | -5.91176 | -61.38834 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 151e356d-0a42-31e1-ab23-30b4554851a5 | -6.73468 | -59.64507 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf6d4249-5823-31be-a597-355fbe1e8033 | -8.90898 | -70.69092 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bc9a0c1b-31c2-3c8a-b3e8-9015b8fcc0be | -3.93407 | -59.33652 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ee4de341-9a62-36ae-8afe-2d383b8e7ca3 | -6.84413 | -55.60654 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 56fe5705-b829-33f3-b336-843f51367c38 | -9.28009 | -71.91101 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7996a7f8-4c0b-3b23-9c77-2aa50e5e3cea | -5.9917 | -57.68118 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 8c80762b-eb98-3257-abb9-96bdad50447c | -8.90383 | -71.39535 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 684d6712-8264-3923-b977-eb27f2d28e46 | -7.60069 | -61.34597 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 2e41ebaa-5416-3da3-902c-bc232aca0a9e | -5.90252 | -61.29185 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3f65e2d0-c31f-3234-a28e-3c000b7e22a3 | -4.30892 | -59.46807 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 76c020a8-7b61-39d3-9c3b-72b3ab58c825 | -8.2937 | -63.39845 | 2026-08-28 17:47:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 77535ebd-5f62-32b5-be3f-04629ca83efb | -7.53187 | -73.47908 | 2026-08-28 17:47:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4da298cb-e286-390b-9bb1-5e483dc772ea | -6.72077 | -56.3384 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2298f0b9-72d0-3fea-a9e8-9676e781bcd4 | -6.278 | -53.13673 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c0111b82-f519-3fd3-b30b-0c6f5b6fe91b | -7.8815 | -72.99285 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 110d80f8-0144-3c0e-bf53-f192b7d18e27 | -6.90835 | -58.92249 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5f955e06-85dd-330c-9a85-416acbff6cde | -6.11586 | -57.82623 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21a27295-e26f-33fe-8ad8-552bb027c98c | -7.48061 | -61.40707 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 857f770b-2741-3171-813e-bbc19adedd41 | -7.72017 | -71.42397 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7e35754-f8bf-3ba4-9211-441b5c0ba120 | -6.16025 | -61.77148 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce411ccb-b240-3fca-8648-4e9b98e155d8 | -6.00403 | -57.83236 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b6bdd01b-906b-3020-b39d-d452c9db75a3 | -6.12913 | -57.82828 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b74555d8-7d83-3320-9921-255792467f57 | -3.31347 | -58.25996 | 2026-08-28 17:47:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bcf76024-070e-3877-88e3-c9bf66e02610 | -6.20747 | -55.41152 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 994ca16b-2677-376f-9f62-f45649f279a0 | -6.94001 | -58.94714 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8fdc38d2-0e52-3f25-bd78-8ed98ca97d61 | -6.14274 | -57.64882 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e51cb68-1f2c-3228-93c5-80875facbd96 | -8.15605 | -70.52698 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49268607-218e-343b-ad25-ec88f8ce6793 | -4.44023 | -55.62989 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2deac924-e935-3fe8-bee1-783a98ddc666 | -6.69857 | -58.94251 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9b5de14b-e2d0-3e8b-a31b-9beb68769b34 | -6.12976 | -57.83212 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9a4798e6-da18-3a38-8bec-401299b3e9f6 | -6.77517 | -59.44555 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 891561e3-026c-36e8-803c-795828b58a43 | -5.82635 | -52.21211 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b725e91a-bc87-37eb-b423-bf8da8aee8da | -8.11722 | -71.30387 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4bbc0bf0-bf20-3167-9422-66875ce4cf5e | -6.77142 | -59.44618 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 30817796-3552-3b9b-be98-058ebe82d7e9 | -7.47988 | -61.35801 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b93cabd-32ef-3054-96f1-bd8098ee3eaa | -6.85199 | -59.4629 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 53d74344-dae5-3ea4-968d-e375774ae544 | -6.81717 | -59.70902 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e1509d8-a7e6-3a3f-9b5a-1cdb44f8672b | -7.53242 | -73.48315 | 2026-08-28 17:47:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b16cb82d-4e63-3039-acc5-ebfa523e457e | -6.72342 | -59.43509 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d73cdb79-cd40-30d3-a8e5-398018373569 | -6.46933 | -55.94269 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 67fed6b9-06d6-3907-b3b0-815cd9b726a1 | -8.91726 | -70.86979 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1d483587-ae41-34e4-903c-4216b86a9965 | -6.93136 | -58.95567 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 594dbe99-43f7-30f4-86d0-5cf894dde394 | -6.84201 | -59.93602 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0aa6264e-bb68-37ee-a576-dcbbcad44211 | -8.94704 | -71.56579 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b87fc805-2d88-3209-baf9-c00ab782e1e0 | -8.63727 | -66.5405 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ffb9cdf0-1fac-3a84-8bae-d7c465909d5c | -6.94291 | -58.95378 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 531680ff-6270-3daa-a36a-9bdde7b8ce4d | -7.52313 | -61.38905 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a4758abf-e2b6-3bb0-8647-3c4291dc2097 | -8.24905 | -70.105 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 67ef9841-2057-3f21-b1a5-51b1e7690c56 | -6.60125 | -55.45288 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a3fcf9b-7fdc-3824-9eca-558d1c5babe3 | -3.73732 | -57.2343 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c6947e6b-280a-35c6-9c77-36168c5a3c20 | -8.33806 | -70.28461 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c696161e-f67b-34bc-9607-cf319aeb4af2 | -7.48169 | -61.39178 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 02725791-deb1-3ea4-b3c7-0ff45aa1d976 | -8.88134 | -71.46395 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2a63fa74-6465-3827-823a-c4363dbe380b | -6.95257 | -59.48498 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| bc02638a-8b73-3514-8486-ad6a330314c1 | -7.9256 | -70.66344 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 41.3 |
| a6698d9d-d50d-395c-a418-4851ccf29db6 | -7.71738 | -70.2503 | 2026-08-28 17:47:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 13e8d3f2-5953-35e9-b18d-a8afbaf0af8b | -8.9055 | -68.8867 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b75b0391-9e87-32a1-82c4-25fa4aed4b05 | -9.09403 | -69.86039 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 95465fae-d2cb-3527-9932-bad515be4e31 | -7.43728 | -63.83714 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51e032a2-0f61-3a76-917a-32a98ce56e01 | -6.2025 | -55.41213 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3158b0dc-c500-394f-b98f-bfb9dc53c657 | -6.90449 | -58.92309 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8c05d694-80da-3a62-b2b9-6b261e6e5dc7 | -8.68498 | -70.6927 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| abd567e8-bb30-37c7-80b8-8ac3e0ebc4bf | -6.84985 | -58.97649 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ff8dfce7-d017-3837-962f-9ac3161089ae | -7.58982 | -61.32119 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6cddfd8c-d1e3-3cbc-a48e-0973c02c6030 | -6.28064 | -53.32719 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e93872f-a7f4-317d-92c6-1cedd6192adc | -6.71814 | -59.44995 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 317d5e00-7fdf-3fbb-a826-917f5a0c50b9 | -6.72565 | -59.4488 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35c108b4-220b-3b5b-9c95-d618eee8a87a | -8.68754 | -70.99211 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 24.8 |
| bc93b486-7ffd-3425-8518-1969b32b815b | -6.14219 | -53.70296 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07b15459-fb1d-3a0f-b031-fb1b6bf68410 | -8.89871 | -71.39603 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8a61fe58-3790-3c45-b548-8c513312f6cb | -6.92441 | -69.99618 | 2026-08-28 17:47:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 350acdc4-9ed0-3c33-846f-42eeb116b1c4 | -6.58276 | -55.4334 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| af6cf3e8-4b50-3d76-815e-f98d911b170b | -4.15322 | -60.75918 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a149e392-f63f-34ad-8139-949c1cd12abd | -4.96274 | -56.27386 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a2c766ee-4bc1-3405-b3c5-22c259613b9a | -7.91523 | -61.3185 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48acd5cf-3006-3b1e-a038-118906915a0f | -6.88494 | -60.04216 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6552bd4-dc48-300e-a947-23fb68ca2116 | -8.27276 | -70.85587 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a08ae396-0e9c-3dc7-817f-7856c235f145 | -9.20565 | -65.79871 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a3abf83-b2f2-3396-b49a-eced2c2ed5c7 | -6.16888 | -57.78188 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 38517251-ce3f-3cb6-8bbb-651234eaf138 | -7.57842 | -61.31536 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ffea18c5-5104-359a-9934-0a64b4686ef6 | -7.60409 | -61.34543 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README154.md)
