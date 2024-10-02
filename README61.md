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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e58a4560-703f-3cfd-9b90-20ad1ed1182a | -6.6356 | -42.10616 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e593ec4d-3364-33d5-9160-1069fe43f46a | -6.63485 | -42.11057 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bfc5f53a-31b9-315e-abea-14ec5a7bedd0 | -6.63409 | -42.10804 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 06178291-d3ee-36eb-88b2-0cc7d825fea2 | -6.63338 | -42.11246 | 2024-10-02 03:51:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ef4762d-5131-315b-adca-d0c7c1f7d99b | -6.60787 | -42.98765 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8299e35-d635-363a-bf92-20e6bd2038f5 | -6.60688 | -42.98985 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7abdf0e0-edf7-3d48-856b-a786ce5f7a59 | -6.60311 | -42.99199 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5247eeb-32ce-353a-9c10-9e74af4901e4 | -6.60294 | -42.98918 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3623d35-3d9b-3afd-ab71-1ba6b096ae8e | -6.5072 | -43.15366 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06225ce7-9767-3b79-bfec-44552c03b7f1 | -6.50321 | -43.153 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37132c8b-fee9-3c8e-9426-9ca428f81812 | -6.4998 | -43.1489 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0ca3ccb-189e-3e88-9153-7843fcdcd839 | -6.49524 | -43.1517 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d705e46f-0cfc-3277-a6c5-173095368c3f | -6.49465 | -43.15517 | 2024-10-02 03:51:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1978330-3583-37f7-ac2a-b622f299fc85 | -7.29512 | -42.26929 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a933017-95e0-3045-bc28-5110b4c01e77 | -7.29062 | -42.2732 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bbdf1801-8630-3604-946d-6d5032917bfa | -7.28991 | -42.25455 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 69470c86-46ae-391d-8af7-44315c1ed387 | -7.28915 | -42.25907 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50a519f9-7440-3109-8d08-bc381d8a8e9b | -7.27572 | -42.24767 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea6d1b2f-5ea7-35b5-97da-2882d1302bf8 | -7.27419 | -42.24958 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 348d70bd-f3ff-34c3-b767-2edbc59f2ac2 | -7.27198 | -42.24708 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a23c873d-5d06-354c-b2aa-2e5922b57938 | -7.27122 | -42.25159 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f3b8e9a-ebf6-36e8-9e1f-62cb9d5ad358 | -7.27046 | -42.24899 | 2024-10-02 03:51:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98a4e32d-73bc-3147-8d8c-8f99dc63c137 | -7.22762 | -43.39018 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 143c001c-f07e-3674-999f-bda3e652316a | -7.22361 | -43.38953 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 89e6b7d6-b3ab-3bb3-af21-7a643c0455aa | -6.98724 | -42.90512 | 2024-10-02 03:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 277b77fe-fd6e-32d4-97a8-5f162253eda7 | -6.95365 | -42.50245 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 219fb9ad-f22b-31fa-a9ef-628619239492 | -6.95287 | -42.50717 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4d2b815f-cce2-3410-8380-4ec4bf7d3692 | -6.94906 | -42.50655 | 2024-10-02 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7c060b49-ce06-3898-9f02-0bbb91369742 | -7.32497 | -43.33495 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e8090c6-29a1-358e-9d50-1b28da2530b9 | -7.31978 | -43.31733 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ba4b06a-e351-3bc7-a64c-52513f2d3f98 | -6.94033 | -43.40694 | 2024-10-02 03:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a9f02d7-f53b-3da3-8ac7-2864f517db45 | -6.72283 | -43.56195 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3dbdacd-2645-3520-a329-8b68dd27e840 | -6.72241 | -43.56197 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4db23a9-0b07-3b9c-9fea-3bf17e598bfb | -6.67843 | -43.50153 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c31173e-218b-3c38-a3a0-169928392cc8 | -6.67436 | -43.50088 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8fd4982-0a13-39e0-8103-202932dbed5b | -6.46889 | -43.48162 | 2024-10-02 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 268fd410-ff6c-382b-836e-f16dd030f877 | -3.47121 | -43.35723 | 2024-10-02 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b24496d1-756d-38b2-9733-58e6323f78a8 | -3.46698 | -43.35653 | 2024-10-02 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5020aa8a-80d6-3c8e-a6ca-2bbeaa0095e8 | -3.46635 | -43.36045 | 2024-10-02 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56785537-2b72-335c-b844-0ec4516ff2e6 | -2.78971 | -43.3377 | 2024-10-02 03:51:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17c4f2d5-d0a5-3c53-baf1-807e63d227b2 | -4.94298 | -43.68466 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc21c4ee-251c-3e6c-82be-8004ef037ed4 | -4.78541 | -43.79851 | 2024-10-02 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8dea2c3-c35a-326a-9e8f-c1de6e47b6c1 | -4.6654 | -43.76229 | 2024-10-02 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6913f94-048c-3369-9cc8-297f50fdece7 | -4.6618 | -43.75761 | 2024-10-02 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4412167-5928-3d28-ad92-9a73d46233f7 | -4.66113 | -43.7616 | 2024-10-02 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 023596c5-7602-3cc3-9e6b-95add00dac30 | -6.00963 | -43.91932 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9f1f4c1-4917-37d3-8a02-e288f148dc20 | -6.00917 | -43.92178 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f0bb897-0998-3179-879b-a2a1c6568ea7 | -5.94667 | -43.69485 | 2024-10-02 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 712ba749-f202-3fb8-84fc-cc23c8ba235f | -5.94393 | -43.69356 | 2024-10-02 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e75b5e5-3a0c-3e59-ac33-0e1a4fbd8de6 | -5.89258 | -43.97306 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3248f3e-b5db-3624-88ac-982818f1998c | -5.89198 | -43.97171 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13b48cdb-5ff2-3122-9a10-90bca340a202 | -5.88617 | -43.72382 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a376d3d-b371-3821-a1b1-7c75e0ae0aad | -5.88263 | -43.71929 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e8a9daa-ba07-355d-9463-a0a702258175 | -5.88199 | -43.72315 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d3f5c708-6c93-3a70-9d2c-e583b2c9a691 | -5.85303 | -43.74203 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37c436c8-110f-3629-984a-fb4c9efd7090 | -5.84885 | -43.74133 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40040029-94cb-3363-b36c-19a981194656 | -5.83864 | -43.95617 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8816f716-6cfe-348a-bbd3-64103ddf501a | -5.83439 | -43.9555 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e8e7615-58b1-3d6b-b1e6-02427b80d49a | -5.81116 | -43.83458 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef0aa06-b74f-38fa-88fc-dd20e2804dbf | -5.71464 | -43.94436 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48227113-b4ea-3bef-96a8-025e5514c025 | -5.71176 | -43.93552 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 515af7ef-f70c-34d1-bd16-3aa293e342b4 | -5.71108 | -43.93959 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9f5209-4946-3360-9716-71848fecf4ce | -5.71038 | -43.94368 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d11b12f6-534a-341a-a30f-1cfa522bcc0c | -5.70752 | -43.9348 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5e25753-9941-3d10-9a07-041d6afe10a6 | -5.70683 | -43.93887 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd091209-2ba6-3bab-a860-556ca7faba77 | -5.70613 | -43.94296 | 2024-10-02 03:51:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd55291-916a-391c-87fe-08dc5ee92563 | -5.40391 | -43.43925 | 2024-10-02 03:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dbfe7c9-393d-337a-8d07-3b7ec516877c | -5.39977 | -43.43863 | 2024-10-02 03:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c822d50e-2dd9-3c5a-850e-75111ba888dc | -5.82245 | -44.1315 | 2024-10-02 03:51:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a92888-08d8-32f0-8d50-7c2531acdc10 | -5.81816 | -44.13077 | 2024-10-02 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07641451-2974-332b-b527-8d759961ee10 | -5.68656 | -44.18933 | 2024-10-02 03:51:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7853b98d-fad3-3a11-9150-ac89e5cbcf5b | -5.68223 | -44.18865 | 2024-10-02 03:51:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672b9a77-868b-3e31-90c3-8009178c8c54 | -5.68154 | -44.19274 | 2024-10-02 03:51:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 518a6117-e1d4-317c-a414-1f75093db5a5 | -5.57198 | -44.09516 | 2024-10-02 03:51:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66a8de8c-0a2a-3d0e-9385-348badb0476a | -6.49777 | -43.82978 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 42ab7665-e5d5-316b-86d1-4492114f3c8d | -6.44695 | -43.97641 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84260881-af57-36fa-a28d-56388b4588be | -6.44628 | -43.98033 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9851510e-4976-3e27-82ef-bff6295ec382 | -6.44271 | -43.9759 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2786c3dd-4cc2-3a43-b7d8-66b3766559ef | -6.44233 | -43.97629 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c322a02-3052-3a21-b237-d68376dad6d1 | -6.44203 | -43.97988 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65f957c3-52bb-3d0b-8612-f8385addaef4 | -6.44168 | -43.98027 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db4853ea-9596-3bbc-9ef3-9102ab9a0072 | -6.39668 | -43.83615 | 2024-10-02 03:51:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949f0791-9575-3650-8785-2037366d1ac7 | -6.36738 | -43.59204 | 2024-10-02 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b59ff651-2243-3bd9-aa08-38245a14cb95 | -6.19404 | -43.62471 | 2024-10-02 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e19f4726-679f-3349-8fd3-abd48a18e533 | -6.1934 | -43.62852 | 2024-10-02 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f34ccd2-b5c1-34f9-84ac-d8ef52e96a63 | -6.11561 | -43.54731 | 2024-10-02 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4be0840-68f7-3878-9145-2da9e1942948 | -6.1115 | -43.5466 | 2024-10-02 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ae59619-22b4-3da8-9875-5dc52625b01f | -6.29847 | -44.76719 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cea92b5-aa87-34d5-a541-ebbc1f1c2ff5 | -6.29726 | -44.76562 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dc7cdeab-0daf-376c-8246-2c7575d4c677 | -6.29401 | -44.76644 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cceab48c-900a-3817-a570-e8d448b86be5 | -6.10031 | -44.054 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 783ef8ec-72ea-37dc-95e7-13e0f9d6fc77 | -6.09949 | -44.05267 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8906935b-1641-3c7c-bc60-692ea9057041 | -6.09862 | -44.03767 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fa042dd-ed7d-3f20-8f95-db53285aa754 | -6.09793 | -44.03627 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39078937-cbc7-30e6-89c5-4398d6b7469d | -6.09722 | -44.04039 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44756857-0a81-3fcf-bc29-b35450462d48 | -6.09608 | -44.05313 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e377950-9e9a-3d8e-ac9d-16d8e6ecd561 | -6.09526 | -44.05183 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acc6fbaf-b5bd-3997-8c31-6d25ade5f9a7 | -6.09437 | -44.03694 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d20e5b-5c68-3200-bb61-222a6b819428 | -6.09245 | -44.04861 | 2024-10-02 03:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67e338d5-3894-32eb-bc13-448e1f75c8b4 | -7.31836 | -43.8195 | 2024-10-02 03:51:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
