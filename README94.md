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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae9a3e7b-b68e-33c5-9193-0c39c59bafa3 | -10.4099 | -50.3324 | 2025-10-06 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 6b127744-f549-3dbc-82be-b90879230d73 | -10.86 | -47.9621 | 2025-10-06 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6067b34c-39fc-310a-b06a-208c2174a006 | -9.6801 | -48.4232 | 2025-10-06 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7dccd5f4-554e-3e26-96a2-d4af5cd54d97 | -8.595 | -46.3246 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 8ceaabc6-e252-3f79-8f5c-c2ebf68fd158 | -11.6849 | -45.2872 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 350ef695-0387-3055-9818-64f86cffbd75 | -14.8626 | -51.5234 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0a37afdb-3719-367d-a730-76f49e4965f1 | -9.9396 | -50.2304 | 2025-10-06 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2b436c56-2988-310b-950b-7d630f5ff539 | -6.523 | -45.207 | 2025-10-06 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| fac690e4-0d8a-3959-b65f-b9dcc496d3c0 | -10.7281 | -46.6433 | 2025-10-06 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ce09d3b0-cd3a-3943-bd71-1e8a24448b9d | -11.825 | -44.9437 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 85abe40f-b77b-3e35-9805-e74a3810d575 | -8.6141 | -46.3003 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 3c89f031-a16a-314d-9783-549cfa8566a5 | -17.3816 | -53.5947 | 2025-10-06 14:10:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 03e908c3-49d0-3857-983f-74ca0ea5e5c6 | -7.2094 | -45.8942 | 2025-10-06 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 28a22950-68f7-358e-9265-fce8abd62e28 | -7.3101 | -45.2531 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fb1f1808-3a0b-35e4-a1f8-02dfd57721fe | -9.7838 | -47.7324 | 2025-10-06 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b1eb8c51-1721-360f-8f09-7de412ec226c | -14.5438 | -46.9633 | 2025-10-06 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 73558a11-3919-34d2-b246-4f4e271461bd | -7.4091 | -46.5033 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a7731a7f-19b4-38f5-9de0-8b737c7990ef | -7.5329 | -43.8552 | 2025-10-06 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 02c235f3-3b88-321b-8053-ce8e837fffd5 | -16.0083 | -56.0155 | 2025-10-06 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 5c5535e0-56e5-33c2-8821-6ae804ba87ae | -8.5196 | -46.3323 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6129b463-c9c8-3ff9-a80d-7e470c45a60d | -15.5699 | -47.2854 | 2025-10-06 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 988d66d1-6b8d-35ac-9fed-cd98c87ff10b | -8.1327 | -44.1185 | 2025-10-06 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 72ce862d-998a-36bd-bf67-63fef986b7e8 | -10.1383 | -45.4725 | 2025-10-06 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 9e658102-c910-3503-a8cd-09f712dd0b5b | -8.0678 | -44.7929 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a8a12f37-986a-37c0-8672-a3c4bf079564 | -12.8205 | -50.528 | 2025-10-06 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 29d7dfe0-6bba-371b-8f55-62fb438c9321 | -7.448 | -43.0693 | 2025-10-06 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| d2554990-70d7-3183-a031-813898fe7223 | -7.5969 | -44.8165 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d42414b7-87f9-3650-8a81-64b3c337758f | -7.0369 | -42.78 | 2025-10-06 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 7ccb060a-adea-3d6c-a02b-70af013382c9 | -14.5433 | -46.9861 | 2025-10-06 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.7 |
| c3acfe48-1823-3f42-9d3c-2b84845dbaa9 | -9.9776 | -48.7622 | 2025-10-06 14:10:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 03badc4d-0f98-3dbc-9fb8-b207cbece450 | -11.8033 | -45.0856 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3b173454-b2a5-3bab-8bca-3217cc555adc | -7.8074 | -44.5209 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 41377a26-110b-3976-88fc-dfe585d79772 | -13.0033 | -51.0624 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 37121df1-3fcd-315f-a303-43bb5f630c18 | -7.7935 | -42.5845 | 2025-10-06 14:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| a81bc74d-4d59-3a21-8347-9bd762ac3a65 | -12.9841 | -51.0648 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.6 |
| d11dd55a-16d1-3f6d-8743-362d0967a0a3 | -6.6506 | -41.9613 | 2025-10-06 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 55a53c0f-e2e2-32cd-bf4e-14bf1958975b | -10.1389 | -45.4268 | 2025-10-06 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 582a703c-5160-3a61-9a89-d257d801360c | -8.6139 | -46.3227 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 54a4fd0e-7196-3b0a-94be-858dc4b7bea8 | -12.9844 | -51.0433 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 64b63528-520f-33bb-a121-f2e507ac968e | -10.3864 | -45.3955 | 2025-10-06 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 45927996-a513-3506-85a8-23667f453ba6 | -7.0558 | -42.7782 | 2025-10-06 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| df8462cb-3688-332f-ac46-5c402a281efb | -7.8687 | -44.1227 | 2025-10-06 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 5dc8b88f-6f7d-35f6-b4a9-cdee3cf37139 | -7.712 | -46.2531 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ff2b8312-49c6-32eb-9ab7-60c27bc8c506 | -7.2416 | -42.9957 | 2025-10-06 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| b68079a3-2950-3645-959c-46485fff0a42 | -7.2392 | -44.8727 | 2025-10-06 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ffe51de9-157b-3426-bd3e-0c106b6bcb0b | -7.6932 | -46.2548 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| a12b4295-0d88-3f5c-94f2-0b5e026ea4fa | -14.882 | -51.5207 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 21566659-4d90-315a-9690-a9751176cd20 | -8.4671 | -54.7035 | 2025-10-06 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8fc8fb1c-d81c-352a-852a-33931d770572 | -6.8388 | -45.4753 | 2025-10-06 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 60b549c1-a301-39b7-a42a-9b73ce475157 | -9.6804 | -48.4014 | 2025-10-06 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5c68e6f6-48d7-3e10-9731-791b4030fbae | -7.2662 | -44.1356 | 2025-10-06 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 7a879a81-1bd6-3a15-b055-736b356dbc55 | -17.2717 | -46.9164 | 2025-10-06 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 192fecd4-b4b0-3d25-afac-707e837c4d2f | -13.057 | -47.9155 | 2025-10-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6ad039ca-9b42-39d2-8062-136288360b81 | -7.2389 | -44.8955 | 2025-10-06 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3f1df0d2-8eeb-3af5-b3b6-bb3e91c56e78 | -10.4054 | -45.3931 | 2025-10-06 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a1b99804-b30a-3f6f-9285-c314c930abe6 | -17.0855 | -43.3564 | 2025-10-06 14:10:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 98006a41-872e-3ab3-aa71-a57020397fc6 | -11.449 | -43.4803 | 2025-10-06 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 250dc502-f3f0-32f6-aa43-e9949236d83a | -10.465 | -50.4547 | 2025-10-06 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| dc90168a-12ef-3fa0-9154-c9f5a357d12b | -9.3162 | -46.0005 | 2025-10-06 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2e52d11c-3712-3bc6-8246-86f37496f9fa | -8.2664 | -47.0474 | 2025-10-06 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cca13e3c-0c2f-3c2d-8891-e37445d53f21 | -18.018 | -44.9965 | 2025-10-06 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3bd881ce-3fcc-33fd-9c1e-b914ba77a368 | -9.9779 | -48.7405 | 2025-10-06 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c2001820-31fc-3813-859b-26259f4b0719 | -12.8954 | -47.2909 | 2025-10-06 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4ff8174c-6b09-3013-9d74-6dbb48008bfc | -15.2012 | -56.8435 | 2025-10-06 14:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c44b71da-8732-330f-aacc-2cd5d3978b6f | -7.7743 | -42.6103 | 2025-10-06 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 6c49906a-cc2a-3fa2-872f-2382430cc2f4 | -7.8265 | -44.496 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7a9a6901-73b9-3bbf-afd0-7cd8ea0dd8fa | -7.64 | -44.3534 | 2025-10-06 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0bb461b6-cc38-3a05-b810-a6485df69f9c | -15.3541 | -47.3235 | 2025-10-06 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 609efa11-4762-395c-a0fb-87d395e3a68c | -10.8597 | -47.9842 | 2025-10-06 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 339d2402-9b3d-3579-932d-f4a7a8bb041b | -8.5956 | -46.2798 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 83bccc9f-b672-38bc-968b-f77c0d5df8ec | -10.1393 | -45.4039 | 2025-10-06 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ebafce3e-8d17-3849-b3e6-2b95be4754c1 | -8.5193 | -46.3547 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 829ab645-f816-360e-a93d-dd933d40c345 | -16.0038 | -50.8365 | 2025-10-06 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 1ed5fbb4-5fa9-38e4-b0b6-4b7e428e4ddc | -9.4866 | -45.9813 | 2025-10-06 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 03a5fb94-3383-36de-aeb1-60bf850ca03d | -13.0763 | -47.9127 | 2025-10-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 5a0319a6-dc68-38d4-9218-6e55e8edff42 | -7.4276 | -46.5239 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 63a57332-9da8-33d2-a6f3-5cc88bc41be8 | -10.0028 | -48.3015 | 2025-10-06 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 51db4cf1-01b8-3fed-83bd-67fe7e97377b | -8.5004 | -46.3566 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| bd11f5d0-9dc1-39ec-98a6-45568ad6d366 | -11.8254 | -44.9205 | 2025-10-06 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| ecdd6a43-d13b-3292-9274-d14be1b96905 | -11.6859 | -47.4817 | 2025-10-06 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 48b5bdbb-17e4-3d5b-9c89-a4ce2ff135cf | -9.6614 | -45.6667 | 2025-10-06 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 810e9ef1-9082-35a3-a374-2178ed8f1873 | -10.1573 | -45.4701 | 2025-10-06 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4a0369ec-ca5d-330c-9b74-2c96ec5cf54d | -6.6503 | -41.9853 | 2025-10-06 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 52350cf9-9ee1-3fe6-a19f-2baac834f25d | -9.746 | -47.7365 | 2025-10-06 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| be8edb8c-cdc3-390e-a2a8-026acdf750df | -13.0759 | -47.9351 | 2025-10-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1fba34a1-3819-3301-92b4-961fce4cf9cd | -7.0058 | -47.487 | 2025-10-06 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4f021e65-736b-39fb-8078-f7676223cbb1 | -7.4669 | -43.0674 | 2025-10-06 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 442.0 |
| a7b4df10-48ad-316d-b34a-e8cd5f4c7f80 | -9.9207 | -50.2323 | 2025-10-06 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 594ea46b-4a4a-3c6e-b43e-f07bebfb09b1 | -16.0604 | -50.9364 | 2025-10-06 14:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b4c7b33b-3922-3cff-990d-2c4c9aefff2e | -13.2515 | -47.7979 | 2025-10-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 295b9a5c-e5b9-33cd-8b62-8348fe7c2bfb | -10.386 | -45.4184 | 2025-10-06 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 147.8 |
| cf1bd46c-fbd9-376a-97db-8c3a42c7df3e | -11.655 | -47.039 | 2025-10-06 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 92435a9e-18b2-3cf4-ad2d-17cc1f9c8f01 | -11.0911 | -47.7573 | 2025-10-06 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e8fb2283-cda6-3087-85bb-9f983935dab7 | -12.184 | -50.9478 | 2025-10-06 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 0691ee50-30a8-335c-88f6-66431f2946ba | -7.6463 | -45.4262 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0be576f1-7fc0-3dc1-a95b-97a4a0916dfa | -7.7494 | -46.272 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 060b1b39-6c31-3117-91ea-9ed4275239d2 | -7.2091 | -45.9167 | 2025-10-06 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b1cac6c7-a41c-37c3-a345-5a2ce71e1f94 | -16.0086 | -55.9949 | 2025-10-06 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 1669f366-ca0a-3838-82e3-5b437f8117af | -7.7496 | -46.2496 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| df59e4ad-7a53-32c8-8b38-d97b4793c707 | -7.2911 | -45.2775 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |


[Clique aqui para ver as próximas entradas](README95.md)
