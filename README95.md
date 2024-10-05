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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9315d56c-819a-3465-84fa-7a9e2d1f848c | -17.0319 | -56.6749 | 2024-10-05 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 82f88de6-cb6c-3306-8a95-0747c1ca7f33 | -18.5058 | -52.841 | 2024-10-05 04:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 80a876a0-87f2-34cd-8166-096729d547fd | -18.5053 | -52.8626 | 2024-10-05 04:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 138.3 |
| a4a071e2-ed42-37d8-b457-66b4c1119fc4 | -18.4858 | -52.8442 | 2024-10-05 04:36:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 2aed126b-4e73-3ea7-965b-a384744e2130 | -18.4853 | -52.8659 | 2024-10-05 04:36:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 59096bdb-d687-311b-9f6d-44f8fbbd0365 | -18.6981 | -57.2915 | 2024-10-05 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 6ec03597-9b5b-3421-91f9-2cfd37d9074f | -18.6785 | -57.2734 | 2024-10-05 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.0 |
| eb7ff31c-7eae-3c39-9a63-58ebab69ab20 | -18.6586 | -57.2759 | 2024-10-05 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.3 |
| d2da3f89-6a5d-368e-82fb-f66c0a4132a2 | -13.52658 | -48.6054 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cf1f46a-3841-3bc3-b711-569893bbda46 | -6.84507 | -41.68962 | 2024-10-05 04:38:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d064a0ea-7030-39e2-a71f-11b176281ba0 | -8.33185 | -41.16351 | 2024-10-05 04:38:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4be024a3-73d1-3b5b-b240-c8634c82eb25 | -8.32673 | -41.1626 | 2024-10-05 04:38:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2233d52-d833-32ef-b33b-07898e1c3299 | -8.15311 | -41.34851 | 2024-10-05 04:38:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d20f6cf-f1fd-334c-ba8f-056d378977ae | -8.15272 | -41.35141 | 2024-10-05 04:38:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06d80ef2-8496-37d8-9dae-c156d8d2bc6e | -11.75811 | -42.93356 | 2024-10-05 04:38:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f81bfa87-5e4d-39d1-a9f1-b3ce2321e476 | -11.75331 | -42.93296 | 2024-10-05 04:38:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5be99b4-e093-3230-a5b4-05dd175ed493 | -10.83855 | -42.84916 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c696883f-111b-385c-b3dc-82e51cb6bf1f | -10.83827 | -42.84733 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 055431bd-a567-37c9-9774-b6bf79c7a908 | -10.83788 | -42.85434 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ab340694-eefb-3ecb-bd21-92a946622b65 | -10.83756 | -42.8525 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1f689edb-275d-397b-8878-ace32065981d | -10.83722 | -42.85951 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40ab35e1-9e98-393a-aa25-14feebc6d770 | -13.526 | -48.60935 | 2024-10-05 04:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1ab0568-830d-3388-902d-c249042e3c37 | -10.83685 | -42.85767 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7428d4b3-82b5-3a05-92f5-16e5e7387a17 | -10.83313 | -42.85368 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 71383120-afa6-35aa-9caf-c0c6c340d911 | -10.83281 | -42.85186 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a6f9c5-df76-3d5c-92c1-1cebc10e3333 | -10.8321 | -42.85702 | 2024-10-05 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21042e2b-5dcc-3c8a-839c-f8cc61c8cff9 | -13.53212 | -42.02842 | 2024-10-05 04:38:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87eb5046-d240-336c-ad4f-2088b6a16146 | -13.53173 | -42.03165 | 2024-10-05 04:38:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed05cc9d-6b0c-3198-ae0a-8d45ab6de3f5 | -12.67898 | -43.12124 | 2024-10-05 04:38:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cc6b0286-f0ba-3f83-b493-c5e293f40240 | -7.62822 | -43.70337 | 2024-10-05 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5833462c-f48b-3f76-99c4-0f654e482751 | -6.68389 | -43.5197 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78ae2ecf-2947-37df-97b6-38e5a82c77d0 | -7.1267 | -42.61164 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b857384c-1771-3c4f-bffe-1e0df7b9dabc | -7.12604 | -42.61637 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 76d3e4df-7b7e-391b-ac82-8460b7141bec | -7.12213 | -42.61089 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6192138-02d8-3d0d-a360-4965ea512ae3 | -7.12147 | -42.61565 | 2024-10-05 04:38:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ddd3de0-e148-319b-b9dc-c48dbc7b4870 | -6.84678 | -42.82759 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09df810c-d482-3b5e-84dc-60a6845f4902 | -6.84611 | -42.83219 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18e3e16d-002e-3de3-88b7-3943c63426f1 | -6.84295 | -42.82239 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dbf09b98-7b7a-32c5-a267-afd4dbbfd4a5 | -6.84229 | -42.82697 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91d467ae-fad1-372f-bea4-6f7860b62780 | -6.83846 | -42.82176 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8b163327-a9ce-3999-864f-f8062ba9f5e0 | -6.83779 | -42.82635 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 77b636af-a330-3019-9d84-17a0540356e6 | -6.83397 | -42.82109 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a871ccae-f0e8-3d2b-8d49-edc7890fdea9 | -6.83014 | -42.81581 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d9582ee0-8e05-35c0-aabe-c193545eb268 | -6.82947 | -42.82043 | 2024-10-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7b7c739e-7699-3e6b-b1df-deaf8e2f6d1a | -6.6602 | -43.05845 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c7d768b-c511-3d7b-ae7d-2b92c644c310 | -6.65579 | -43.05781 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2d56654-8646-376d-a5c2-b7f62af194ca | -6.65137 | -43.05719 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee121c76-286a-3960-927d-de6429e2936f | -6.65075 | -43.06152 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dcebdd9-f0a6-3050-91eb-1c7ac0bd9018 | -6.64696 | -43.05655 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8bd90a9-18b9-3a22-9592-901f567f678a | -6.64634 | -43.0609 | 2024-10-05 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4221b4b7-e952-33e2-a803-4191e5b31609 | -7.79741 | -43.10368 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1ebe683b-e62f-3e4c-8286-b2ac0526db0a | -7.7968 | -43.1081 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 87056cdd-97e3-3dc7-8067-a739d0d9685c | -7.79619 | -43.11251 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ec5b316e-01a1-3311-9004-870a88d6e818 | -7.79558 | -43.11694 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 719bf44c-39d1-323d-ab7c-a92e4f7f052d | -7.79393 | -43.10966 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dfe64fca-57a6-327e-8993-98fa5377fc31 | -7.79329 | -43.11406 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b07baa65-73f5-3225-a4d7-829599ca4329 | -7.79234 | -43.1074 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 350b8de0-7b7d-332b-9cc3-ec8eef6f1973 | -7.79173 | -43.11182 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1b2dd236-477f-3113-a528-fa7846fe9568 | -7.78947 | -43.10896 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8fe7458-ab58-34f0-acce-e799ae3e1e5c | -7.76321 | -43.06944 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 15b81f00-3c75-3393-9ca2-d3a8bb3a0833 | -7.7626 | -43.0737 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f0c7195-e1b3-3202-b120-71340363031a | -7.75302 | -43.07679 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4a52ee05-dace-32e7-8b0b-84e283e9df44 | -7.75242 | -43.08105 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8fdb6f87-65a0-3bfd-8a50-ce1d17da48b6 | -7.75228 | -43.04992 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 656496b6-88fc-3d2c-b5ad-6537fcbfd229 | -7.74779 | -43.04926 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebd5d06e-c941-32f3-b54e-4b502286a928 | -7.74716 | -43.05373 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea9d5577-43b0-34b5-b5c6-a4710c01c4c6 | -7.74653 | -43.05818 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 072272a7-1aff-367e-8e43-cb9c13d04d40 | -7.74467 | -43.07127 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dad13c85-9efe-3569-a54b-ab9c96e2e999 | -7.74407 | -43.07548 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 6fbe2dac-67b6-3df1-8ac6-2a076217b093 | -7.74142 | -43.06194 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2fbe78c-f814-3202-a7ec-d7fb05af049e | -7.74081 | -43.06625 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b7ff83d4-e212-3c7b-bfe9-4161da9de2c3 | -7.74021 | -43.0705 | 2024-10-05 04:38:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 289b70de-7c45-3b3f-92c7-74a89a8b5181 | -7.69757 | -42.98219 | 2024-10-05 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a04fdf86-7140-3b2d-8ba9-8bf51a8e640b | -7.69591 | -42.9789 | 2024-10-05 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 59c03af5-7a73-352d-8f7e-9d3177debd05 | -7.69525 | -42.98343 | 2024-10-05 04:38:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 57bc0095-8e89-3639-9fec-d3230a2c756c | -7.63646 | -42.48265 | 2024-10-05 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0766418-a13f-3ae8-b697-bb28c0222b91 | -7.63111 | -42.48686 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 36d19920-c2ef-3ba2-99f7-3dde70007cf0 | -7.63015 | -42.42659 | 2024-10-05 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 684d6023-93ec-3536-b5ea-c401857b7731 | -7.62945 | -42.43149 | 2024-10-05 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 89218913-092d-3baa-8c32-37f6cebdf825 | -8.17734 | -43.72315 | 2024-10-05 04:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9fd5d00-355a-3e1c-b187-051fa84339a8 | -8.36702 | -43.65481 | 2024-10-05 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebab3d1c-b46d-313b-973b-f325a9286350 | -8.36644 | -43.65905 | 2024-10-05 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9139261-5780-38f8-9e21-69bf89b4a5bb | -8.36265 | -43.65439 | 2024-10-05 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ce726e2-0133-33fa-b62a-ffeb61d37b8b | -8.17676 | -43.72723 | 2024-10-05 04:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9f7b24f-b0cc-323f-9442-693140bc050b | -9.23844 | -43.48858 | 2024-10-05 04:38:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a258b1e8-bd0d-349f-a372-27764b2f0a39 | -9.23738 | -43.48642 | 2024-10-05 04:38:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dce7ff89-bf2d-31de-af38-c52fbef72e77 | -9.234 | -43.48788 | 2024-10-05 04:38:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 750d1f64-8da0-3109-9a88-e2c04caa5e74 | -8.18422 | -43.73664 | 2024-10-05 04:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c94cf21-a011-3df6-856d-f2a3d8a7c94e | -8.17303 | -43.72252 | 2024-10-05 04:38:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9024337b-1b23-3976-b7b1-a929c0949b90 | -8.36382 | -43.64597 | 2024-10-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ff0ad07-3c47-34f8-b72c-066685f9cee5 | -8.36237 | -43.64737 | 2024-10-05 04:38:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b65b1cc1-16c5-3455-9e1e-536b5434d480 | -8.93153 | -42.59592 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4a39a399-4b6f-3848-82ef-32681e7dc366 | -8.92946 | -42.59889 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0057d5dd-e6d3-30dd-bc17-45f23fc5a757 | -10.47999 | -43.6512 | 2024-10-05 04:38:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b1f69de-6e49-3f00-9839-51a4f16bb8e0 | -10.172 | -43.90145 | 2024-10-05 04:38:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1f7a2e-ba8f-367c-a658-d90aae789cec | -11.76333 | -44.65031 | 2024-10-05 04:38:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ffcae0-c03b-3dd5-ac80-47114c346550 | -11.75907 | -44.64971 | 2024-10-05 04:38:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0041fe9a-f396-3013-bb89-ed967dfcaf91 | -10.98695 | -44.43512 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db4c9519-dfeb-33ad-980a-dc4708d3c87e | -13.01345 | -44.76482 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f900bb4-1035-38eb-bb76-caaa27c8b99f | -12.88055 | -44.6251 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README96.md)
