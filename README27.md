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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3190e65d-416d-3473-b3f0-58dcf52b15d5 | -11.62977 | -46.54639 | 2026-08-21 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca933fd7-dd44-3a5f-9931-93eef5067d26 | -10.63058 | -51.6039 | 2026-08-21 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| de901885-cda7-3e94-b574-d2e3e893942a | -13.74254 | -51.8588 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e02fbe4-5bf7-3027-99e2-1e1ccf5a0e89 | -12.79344 | -48.45422 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4429685-2df0-363f-9a50-dda66aaa33f0 | -12.84006 | -48.45311 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a47353c-84ae-3fa7-9fff-b1b1845aeee4 | -10.7593 | -50.30839 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5393ff1d-adc1-3886-82fa-d8abf5d241c5 | -8.71734 | -49.61691 | 2026-08-21 04:02:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10c27ae9-944c-3303-b39e-294e903d2084 | -13.64077 | -51.76945 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4244326e-9f67-3273-90ea-add5f7d2d8bc | -11.32722 | -45.01597 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a11e4474-d924-371e-9501-420916743019 | -12.74956 | -48.46682 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4751c0b-780c-3b03-a4d6-9dca38e0c53a | -13.67862 | -48.76827 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71d58a11-987b-3256-8882-00861fee5ea5 | -12.79265 | -48.4034 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4a72c3a-56a5-3406-9abe-1c39b057017f | -10.8082 | -50.27457 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3aab46a8-48f7-3b29-b138-56c7bb9f9ea7 | -13.74198 | -51.86171 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 142c4a68-cfc2-3e41-b426-c1e3e38950f6 | -7.71889 | -46.16106 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25cca300-e725-3834-8944-14e3fb994090 | -10.29672 | -48.23133 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6726b0d7-3bf1-345c-aa25-5017df0e5224 | -10.80739 | -50.27878 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d4e99ff-1dae-36a8-a8fd-65d085d45f5c | -10.51985 | -50.78173 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b7a0bcaf-4f38-3c80-b143-ef8f07b834ec | -12.72058 | -48.48255 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c5d0013-bf7e-30fa-ba5c-df78b89b83ee | -10.75433 | -50.33381 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5080000d-f168-30a5-818e-ee8fb6b6eb4b | -14.72579 | -47.13724 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a237ca77-790e-3d44-8cde-b41501779798 | -12.8482 | -48.43768 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eddf9a81-3106-3957-82f7-101d61b65745 | -11.29216 | -46.30559 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cd749e2-3965-3fd9-aaf4-0f11ac3bc80d | -14.45724 | -45.62302 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2830734-db5e-3cf4-9ddf-eb08d5d79bc0 | -10.72468 | -44.7806 | 2026-08-21 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28dc79e5-3bd8-3138-8352-89a40af722a0 | -11.48577 | -45.08668 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e2ddea9-5d90-3f3b-9c8f-51be42433f30 | -11.63341 | -46.55196 | 2026-08-21 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97be4df7-5823-38dc-88a5-c126f55ec97c | -14.45322 | -45.62222 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4245851-3fc9-3386-8447-c2586e12c5ec | -8.08801 | -51.66959 | 2026-08-21 04:02:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65c474f2-aa3e-350d-9318-f1ede4ce4efd | -12.27125 | -43.15652 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d2d1565-8fe1-30c8-8f58-c7db0f6b86b8 | -10.36086 | -48.23887 | 2026-08-21 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dad35efa-1666-3b94-8628-388fa9e33d1d | -12.84715 | -48.44312 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe524521-ee53-3215-8e3f-afe90f0748d6 | -11.3716 | -46.36414 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a004186b-4eea-3a4f-9c6d-2aec93ff50fa | -11.18173 | -54.00906 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38804393-56ed-35d1-8242-0c71dfcf7523 | -8.0922 | -51.66144 | 2026-08-21 04:02:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ba72a39-bc98-3566-81a6-2f48dd4c6471 | -13.64176 | -51.76479 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fafeb78-6f9b-31aa-9e40-694c96d85abf | -16.2504 | -40.30914 | 2026-08-21 04:02:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9cf5f0c-bc9b-39bc-b00b-b6a249201c11 | -10.72873 | -44.78136 | 2026-08-21 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 310664b6-de9d-3474-9ef5-87c118f34bb1 | -9.06475 | -50.88062 | 2026-08-21 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0b3d2e6-f4b2-3f3b-801e-21dc193c80ab | -12.84309 | -48.43739 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 412ad114-6bb0-37dd-aae3-a6a34137111d | -12.74185 | -48.48007 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed9eeec4-afd1-35b5-a9bd-9a3b17add1e0 | -9.01354 | -40.99796 | 2026-08-21 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c407043e-b711-3898-9732-feba4c535a3f | -10.77012 | -50.31501 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94d19a88-3512-3cb6-8659-c89df9043b94 | -12.7973 | -48.40697 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a421e371-f741-3752-8be2-4e3ac898c6c0 | -12.80018 | -48.4183 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d45636e-499a-3f51-a6e1-1171cd9c839a | -12.25383 | -43.17116 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e7cd6b89-7082-3bfc-b112-089eedc5a073 | -11.28185 | -45.78568 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6a0bbe26-c92a-3883-9d65-009bb1dd60f8 | -15.44457 | -41.38483 | 2026-08-21 04:02:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1cb3aa36-57ce-3d1e-9d1c-f4d7694d1c8d | -7.78335 | -46.04077 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f985032b-1a78-3796-bafa-daab3a111868 | -13.44036 | -51.815 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43dcbffc-8465-35f5-bce1-1ae9826e3820 | -12.80076 | -48.41568 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb027bbd-71a3-39e8-a67d-227080e92931 | -14.80689 | -43.56379 | 2026-08-21 04:02:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88de114f-694d-38ff-b74a-7bbb03bb628f | -15.0633 | -45.3272 | 2026-08-21 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ceb03b95-1aec-33bb-b72b-aba08733d4dc | -8.46374 | -45.57897 | 2026-08-21 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2017036-873f-3de5-9000-ca618f2365ef | -12.25743 | -43.17193 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1f0adce4-0819-30f0-921e-5d6f90e49b6a | -12.74218 | -48.45119 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc6f1a7-6f10-3dc5-816d-699b6f0e5a91 | -7.72924 | -46.15718 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8226fdd1-cc64-360a-957e-dabba62d0964 | -9.44264 | -51.63577 | 2026-08-21 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7fcc0cc-0b9b-3eaa-ac75-da4e21560b7d | -13.43711 | -51.79971 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79d0ca03-6409-3dd1-b7cd-344a7bbb1807 | -10.30694 | -50.38415 | 2026-08-21 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 724ae57f-7e95-3579-9a14-376bfd7f470a | -12.85173 | -48.41931 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f453f9b9-2852-3b99-bfa0-56f3adf77225 | -13.38778 | -54.39139 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 49b8c0b3-c512-3588-8e6a-1ad1e0314f79 | -14.28354 | -47.42419 | 2026-08-21 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d577ecb-2aa8-3396-88e9-c40ad6784cfd | -7.73295 | -46.16347 | 2026-08-21 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d8c80b7-2341-3c95-b688-1ff38f818c4a | -12.86158 | -48.42183 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec2bbb80-c23f-38c2-90e7-ea49e523f149 | -14.45388 | -45.61858 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c161c79b-4f08-3ed7-ae1e-ca2f6bad3194 | -11.66102 | -48.35181 | 2026-08-21 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2009bc43-36da-36f8-a0a2-41ebdbf779b2 | -13.39463 | -54.3771 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a00f5bdd-7b3c-3581-ac69-666630ad8e26 | -10.77177 | -50.30655 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3cab445-da03-3871-b163-dbd1311cf5d4 | -10.33477 | -40.61717 | 2026-08-21 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6007e7d6-dd65-32a8-b9d6-8bf22d19597f | -8.94813 | -38.0027 | 2026-08-21 04:02:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c42165bf-6885-30ab-8193-e44782eb9ad8 | -12.26765 | -43.15578 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 662d33a1-edca-382e-b1e6-6836ec481990 | -10.80158 | -50.27755 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3f0b65-4929-3176-9f3e-f16821a71b74 | -10.8251 | -51.00572 | 2026-08-21 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c02b88ea-1949-3e17-bf6a-10ddc627d4fd | -13.15589 | -42.41206 | 2026-08-21 04:02:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3a76c96b-a44c-3d9a-a4a6-d4997ca3851d | -12.79964 | -48.42119 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d95aece8-de9b-3524-98f3-9d3732e61682 | -11.18021 | -54.01623 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47da3f83-03e8-3003-b784-f1ee9c97f029 | -8.33245 | -46.50273 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1ac940e-ba7e-3fb0-8a18-e2579af67b58 | -8.69011 | -47.49596 | 2026-08-21 04:02:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8d5aacf-5290-35ed-ba8f-0f4cae339a4c | -13.40331 | -54.37139 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ad0c290a-59c2-36d7-b3a3-cf7a89b30e04 | -9.99652 | -48.56284 | 2026-08-21 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a067433-65b1-3760-8c54-4649b9e19efa | -11.55441 | -46.93943 | 2026-08-21 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9124e19-edea-3c03-8b79-0508ea5123f3 | -9.99713 | -48.5596 | 2026-08-21 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a824f106-3f12-3da9-93b8-b7c1a0e1fd90 | -10.90303 | -50.27898 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd8b73f-582d-368b-9353-b55e2d83fe10 | -10.83117 | -51.00699 | 2026-08-21 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a7846d5-04a2-3ddd-a451-f02200b1bb85 | -12.77636 | -48.40763 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21f52ad9-9490-319f-9b51-173bcf97037d | -11.35847 | -46.34592 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5398b972-62ca-37c5-a4fb-834e64c9b837 | -12.74678 | -48.48143 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25b96427-15e5-3b59-a281-3d3c4a8c5366 | -12.00487 | -53.43063 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8305674-a521-387d-bf0c-eab767ff635c | -10.99034 | -43.7104 | 2026-08-21 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0082ec8-4a4f-350e-8433-9ac8386df595 | -10.76347 | -50.31807 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62ea9313-dfd0-33de-b4fd-97f61ff76e27 | -12.75024 | -48.46328 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f405e62c-d955-3990-98eb-c55ef63af414 | -10.7535 | -50.33806 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21169ba4-bf1d-3516-a27f-b39eeb711815 | -13.73594 | -51.86023 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e22bc0c1-bba0-31a7-88c7-2c25621e2154 | -12.00303 | -53.43908 | 2026-08-21 04:02:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f8b00863-4b2d-3b20-ac38-5303159c8a21 | -13.67923 | -48.76508 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a383c22-f1f4-372d-ae98-18fe0db6a1a7 | -8.09105 | -51.66754 | 2026-08-21 04:02:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c257b29-99ab-35f0-bb23-26f7b790e84f | -9.26588 | -45.64841 | 2026-08-21 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 668dc97c-9ca1-3e1f-b60d-b3e143714751 | -13.15524 | -42.41593 | 2026-08-21 04:02:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b2a74449-18de-345f-be41-6ae8ee7bcdd8 | -14.8262 | -45.52568 | 2026-08-21 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README28.md)
