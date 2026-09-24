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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e1aa2b-802d-3d0c-9152-a40ce0933a93 | -12.13699 | -44.91458 | 2026-09-24 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc83ea7-02db-36b4-86ca-f1d27468dadb | -13.78718 | -54.07082 | 2026-09-24 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 26ef7add-e741-39ec-bf1f-902bffbb6939 | -10.7234 | -48.74858 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94dec727-74a2-3aa9-96ae-45ad2acc4297 | -11.41117 | -47.36316 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4886373e-cfea-38ae-81f1-3b5a86c37652 | -12.14721 | -50.7241 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 299854dd-4827-3b49-9c02-a794fe5d90e8 | -10.07028 | -46.01632 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0a5cea3-fd56-3866-86a7-9180af2d9f37 | -11.64947 | -43.48264 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e312b86-c90b-3708-9ed8-fda653a8c6dc | -14.75456 | -45.60794 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a159c3e-9547-3f4d-86d9-1b3970b39ab4 | -14.57526 | -54.13018 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5324291-e9ba-30c3-9f2f-3968f7f2c330 | -11.11073 | -48.29738 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff466cc0-5b66-3092-92ab-4558b2cbb228 | -11.94652 | -50.74119 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ae24efd-f41b-3f9e-be48-946453d0c1f7 | -10.08126 | -46.01804 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2b3670fb-7287-3883-9a99-74624d43d616 | -10.07395 | -46.01689 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ddfa9f1b-4a37-3dea-94e0-3ad6936ff9f0 | -10.11138 | -46.01751 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5ce5172-75fa-368a-b1ed-ec41c9c7956b | -12.15665 | -50.75307 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2553757-bffb-3b4c-ab3d-49dda6a8f5d8 | -11.31729 | -44.0079 | 2026-09-24 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f332dad-9dcd-3def-92c1-d91984d63a52 | -10.26876 | -49.95532 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db32b185-e8b6-3252-ada3-a0877a4aa6d1 | -13.08386 | -40.70603 | 2026-09-24 04:10:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f5364e5-31ed-301c-9518-2bfd9bf2e72c | -11.70002 | -43.46552 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8325142-42fe-33c4-929d-f675d55a4d7c | -15.1642 | -43.56707 | 2026-09-24 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29ddf105-4d5d-3528-a5cd-56aff9bcd2e6 | -11.7993 | -50.04277 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8a18ec0-50ed-35d3-a6f7-16f2cac5d8c0 | -11.2294 | -51.37924 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb4cbe26-1567-3a47-a69f-c4476f69aef3 | -12.13001 | -50.73716 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| a0b345d7-6824-3c6c-a5f0-235d9c645ff7 | -12.16426 | -50.76543 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f0ebf6-2d1e-3a72-acd9-89d91149a021 | -10.0753 | -46.00862 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d53679-0c46-3bc3-8315-0d2d83f9684d | -11.23333 | -51.38618 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fea60fe5-2837-3597-a762-2febb214ba27 | -12.92749 | -50.91468 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8788d69-e155-3a0e-af3f-663bec350553 | -9.96772 | -47.98552 | 2026-09-24 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02e2d462-b5ca-3b92-bc11-4a0d8806431e | -12.14712 | -50.75127 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3711aaee-0e10-3c03-a1b7-94dccfbcbe28 | -10.08515 | -46.01722 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e157b0b9-6bec-3580-a70a-c6119901832c | -10.44028 | -46.27562 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 222566ab-64bc-3590-a27d-452c7660b06b | -10.09679 | -46.05948 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 313480b0-3147-3db3-86f5-2d4790f2ea6f | -16.86795 | -43.20427 | 2026-09-24 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83fef157-7895-374a-a66f-29e9f38034b2 | -10.07638 | -46.02462 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8d823b4d-9e0d-381c-b6d7-952bc5217802 | -14.57447 | -54.13416 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bab2a826-591d-3832-80ad-bd19299a65a5 | -11.23671 | -51.3682 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7f0c1d4-04d8-34ec-94c7-e7cc5593425d | -10.43736 | -46.27043 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a90a0f6c-698a-374f-9d99-ccda984d0208 | -10.141 | -50.21986 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f354fb96-5152-3e55-8e7c-118243ab79f7 | -10.07993 | -46.04795 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b25418c4-d2dd-33a9-96f3-5f2b009caae1 | -13.69955 | -48.79063 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6867bac-7983-3850-a16c-fd5d12efc0d8 | -13.84877 | -48.587 | 2026-09-24 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27069463-a0aa-3fd4-846d-b0da65e2c06f | -10.07966 | -46.00496 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15f3ebec-6c17-33b9-a490-a43c28eedc2f | -11.23053 | -51.37325 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c71c3a2a-600f-305d-96f3-061129f2eebc | -11.63495 | -50.60969 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9b8cef48-c2d4-363a-a50c-792398c94556 | -10.0888 | -46.01783 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d65090af-c980-3f2a-b840-de8b86fae37d | -12.41457 | -46.95687 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 86845589-f8af-3b83-acff-e506efd9bc7e | -10.0877 | -46.00162 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a9a1e3e-1d08-303a-b381-2792fb84dbee | -11.21162 | -54.12613 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ac1652e-f2c3-32fd-91d6-dda8bfe4260d | -11.2608 | -51.35107 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a320dd6a-8044-3f32-b53c-f8438b2a6e0c | -10.93711 | -43.85365 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dce92e0-9def-3088-a78f-a20a153e2308 | -10.94606 | -43.84043 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31a9379c-cd67-37b2-8b46-a835d768e95f | -10.26977 | -49.96339 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 738c586c-1f0f-3bfa-8ff2-9c146a9af56a | -10.10335 | -46.0652 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1f4aeef-09bc-3d66-8f63-577d6a11d7dd | -14.56305 | -54.11394 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf1ad97e-3ad8-3752-87fa-62d0e1401907 | -11.36208 | -43.38507 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 820ebc75-b025-38c2-8996-0f2613045b97 | -12.14235 | -50.75037 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6632b7ce-46ea-3e4f-861b-108b78e54fe0 | -14.72723 | -45.60331 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 426e4b8f-d6e1-37ad-afd2-08bacfeafd90 | -9.8539 | -48.50122 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e20bb753-d6fa-3d1f-8686-0d8ec7a9b986 | -10.23637 | -49.98838 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78998c1e-7b0a-3929-8d79-0f8a226e7d11 | -12.17285 | -47.37019 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fdcd488-cd9d-35e5-9ab8-5ee3a757dd75 | -10.08659 | -46.00871 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6c73cac-1128-373e-ab58-8967bf644f23 | -8.59818 | -54.60238 | 2026-09-24 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1d4bc6-8e9d-3270-a8f9-12c53fa8b70f | -10.07916 | -46.05383 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab6294f4-fbde-3d62-9d1f-d7036e49f25a | -11.43553 | -47.40709 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba8b4160-de30-3217-b9f7-9bf24df0019c | -11.30793 | -51.37841 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a119475-4f94-367d-aba9-e8d677d7d9a5 | -10.2157 | -44.14795 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d503909d-5ebb-37ca-9214-dbecfc7d17bd | -10.08734 | -46.02646 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0fd781-38a1-3054-ab66-3d9823769c56 | -11.89678 | -45.77003 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffb743c3-07db-3ad5-8ef1-c9b3f8abeb34 | -11.96275 | -50.76072 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c98e4c5d-86cb-3c85-9124-bc5f2b3609b4 | -10.27811 | -49.95699 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee87b99d-3a90-347d-979f-1cc38cc14e3e | -10.08953 | -46.01353 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d0777e6-8e8d-3d49-89f9-254f2553ed5d | -12.13866 | -50.71706 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b24de419-c79c-34f0-8c2a-b61354884c1e | -11.30644 | -51.37965 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6015159-1ac6-3d55-91fb-3f0a07ebc6b3 | -12.16901 | -47.36956 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0e32acd-ec10-30d9-969c-c9181f80f8bb | -13.78571 | -54.04852 | 2026-09-24 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3358da7-cca9-36a3-bb35-e78174310275 | -10.43883 | -46.26158 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17e68314-9981-3c08-bfb2-2274977e5d31 | -14.2268 | -42.04551 | 2026-09-24 04:10:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43f2d891-80fe-3e36-80e0-666c14ab922a | -11.35381 | -43.37291 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2d46368-4ced-3420-b428-087526842cf8 | -12.17201 | -47.37503 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efc50181-b798-3ce0-b641-fcdf52272328 | -11.23952 | -51.35325 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5e1885-c331-3e62-861d-42444b4b8404 | -11.65554 | -43.48723 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f1f6d222-b49b-30ab-a320-25df1abb9b50 | -10.78459 | -42.94625 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd3bc03e-0267-31d9-abb7-317bf180c877 | -11.23951 | -51.38113 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 649e145e-3e3d-3e76-8a7a-71421db25252 | -14.72787 | -45.59948 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39cad12d-189e-3096-bcab-6578ad2d09f4 | -15.34134 | -48.11425 | 2026-09-24 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40416045-e078-34b6-94c6-2d049090f60d | -16.39668 | -43.33247 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3370f2ac-93ea-3584-ae30-a82f37ac1bde | -10.28278 | -49.95781 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82898a98-b3a1-3fc6-9156-137cff27979f | -14.71469 | -45.59377 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f08b2510-421b-3618-aaab-59dd17c1b9d8 | -10.08576 | -46.05791 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a43440be-c40a-3d5c-b423-72a570134d34 | -12.53777 | -50.06853 | 2026-09-24 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bd2ff73-d72b-368b-8261-28add52a3f95 | -11.22884 | -51.38224 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76c5307d-5040-3650-b9e9-d06669bbad99 | -11.64891 | -43.48616 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9df5129e-fda3-3fa4-b263-c47a3e70ba2d | -10.09462 | -46.05008 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c2c9a0f-9263-3fe7-9d40-cbd0dedf24fd | -10.10205 | -50.18801 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 24c80685-2095-3b13-be22-1763b7acbce7 | -10.56216 | -46.7099 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e864869-8fc9-3ef2-8d63-4f519e547289 | -12.91898 | -50.90764 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d1bfe8e-904c-359c-87f8-6872740b9cbf | -11.65223 | -43.48669 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8428dac4-fa42-38ce-a988-b7e5aa88262d | -10.21292 | -44.14374 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bdbec44-b1f8-3464-933a-d666eb3de048 | -11.79341 | -50.98473 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dedd29d-4496-35ea-b310-d65c9aa44061 | -13.07076 | -47.40129 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
