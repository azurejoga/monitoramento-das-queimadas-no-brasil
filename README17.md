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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6879da0-8918-34bc-9a27-5e66a658fed4 | -12.21843 | -45.5332 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 768c86af-356a-31d9-912d-dd7d46cef928 | -9.31418 | -44.72702 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65682571-8da2-3510-b9fe-2a9ca7df5e33 | -5.78352 | -43.46173 | 2025-06-20 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa36a870-a723-32cc-a970-f111366e9613 | -9.45638 | -57.8474 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14e253f9-02d8-3eac-a104-605d1ca091b9 | -10.9414 | -49.43569 | 2025-06-20 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e0951ef-b83a-343b-9af9-13f6b886f46c | -5.48603 | -42.13997 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d902c3a2-d125-38f7-95b7-9b5813f9fe19 | -5.1314 | -45.02763 | 2025-06-20 04:51:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2aaaf09-5e8f-318d-84cb-f1208ac9ea4d | -4.94958 | -47.47332 | 2025-06-20 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad39c1bd-6da5-3e65-b727-bfe8ef727d06 | -10.22978 | -54.29682 | 2025-06-20 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b1805b6-b455-3dfc-86b2-31f415209bdb | -10.47169 | -47.03983 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4dbf7cf9-e1cb-38a5-9ce5-ec4522d44d48 | -11.15584 | -46.64976 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 11eb4025-2ebb-3f4a-9f3a-87a719fd55aa | -9.33422 | -47.84354 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ac61c56-73cc-397e-afcb-793875d38b8c | -9.45721 | -57.84253 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4f4bf33e-220c-3142-ad40-09f8c830f667 | -7.39347 | -45.40445 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dda1db10-d69d-3612-8f69-2ecba569401f | -11.57761 | -47.62672 | 2025-06-20 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dc4c2f9-f4d5-3610-b3a8-42f2b887779b | -10.45533 | -47.05998 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6aa28604-a928-31cc-828a-896d87e3b9cb | -7.02167 | -44.59345 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92150896-398a-3d61-bcac-ad13451d137b | -3.85771 | -54.0823 | 2025-06-20 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bece10d-a2ea-312e-92a1-a91ce5c69a4c | -9.49543 | -56.09088 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1b62ee7-5889-351f-8f23-d9409d94487a | -8.24979 | -44.96255 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3b077fe-d9e6-3041-8474-471215f9e447 | -9.33528 | -47.8358 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aae8436-ac64-3f49-b061-bf46f5ec8421 | -11.31698 | -45.20053 | 2025-06-20 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8fbccd0-21e3-32a0-b676-7fecd9cb7238 | -11.14917 | -46.62873 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eae01244-a686-3a57-a6df-95034b3f9126 | -11.80303 | -48.09483 | 2025-06-20 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa3484bf-cc8f-3078-932f-ff625201fc18 | -9.46657 | -57.83405 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdad79e4-e07c-3774-a742-b11b2c0d57fd | -12.26697 | -44.60118 | 2025-06-20 04:51:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6c0b59de-bdf2-3813-be1a-01e06430c8f3 | -8.72385 | -47.99253 | 2025-06-20 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec4f0239-c824-391f-a268-25ee2c8af33c | -7.02127 | -44.59637 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 333c9246-90b2-338f-8555-0c10f412aeb6 | -11.14391 | -46.63291 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e50424e0-377e-398d-aa58-e4991297ce0a | -11.79933 | -48.09025 | 2025-06-20 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 391a69f4-9f1d-318e-a0dd-17cc19fa7145 | -7.39416 | -45.39932 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59d31b1d-d5e2-3be1-8be6-c30f7fb7d626 | -7.87275 | -47.89318 | 2025-06-20 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5cf0be3-5666-3d54-95d0-d2845c1c812e | -10.46543 | -47.05249 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7d23c100-4813-3532-b9cd-c607b93c8cad | -7.21192 | -43.06982 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 210d1d23-b9b0-3870-80c0-a68f23eefda0 | -11.31617 | -45.207 | 2025-06-20 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 950f4480-2aca-30a5-8972-73b8421979ae | -6.66615 | -44.24674 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 249fef29-39ff-3ddc-9217-901b5851b225 | -12.26614 | -44.60809 | 2025-06-20 04:51:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2823b0b3-e003-3293-826f-c298a4e7dacb | -10.42508 | -47.08261 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f9bbbba-7c64-3cf2-a9b0-a5f20f2bb806 | -10.42005 | -47.08635 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f93f151c-152e-3ce8-ae90-b23726350291 | -12.21299 | -45.53554 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13f99de6-1ebc-340b-8532-b9a8dfbfd148 | -9.30575 | -47.79047 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8042d5f-9d9b-334b-9f5b-02250fc827a9 | -9.45886 | -57.83279 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05fe5a53-0bc3-3c95-bd1b-22899c5d2e02 | -9.48324 | -56.07257 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e5241a9b-fdce-3127-b627-258958ce92b9 | -10.73289 | -49.56314 | 2025-06-20 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7820e866-5e3e-3bf2-b8d0-f472b89d01fe | -10.52498 | -46.64588 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdcb41c7-ee29-32f8-9394-19d03a946682 | -9.84236 | -44.70782 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c60df56-dd46-3f6e-8b76-5f57105026aa | -10.46098 | -47.0518 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ab27bec6-0c11-3df4-98f3-7311112bbed3 | -6.16215 | -47.26775 | 2025-06-20 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edb23e67-494d-30ed-9a97-9bfdb91fed8e | -4.28035 | -48.18336 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3380effc-02a0-3c1e-8af3-cd22804398ba | -7.97114 | -46.21711 | 2025-06-20 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d10da98-0b45-36e0-8532-4cecb074ca2d | -10.66429 | -49.3657 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd6feec9-e65f-36bc-8a91-b05e680c43f4 | -5.49686 | -42.14442 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e0d2478-2a64-3d62-9f15-20f7448c4d01 | -10.47615 | -47.04045 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| c14e76c7-1f44-3b20-8df5-2a4a085570e4 | -12.20865 | -45.52874 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4d5314b-d2ec-385f-9033-aa0cceb18b39 | -7.72329 | -46.61076 | 2025-06-20 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e1f5a7-05a8-354e-81ba-2fbfe8318d0f | -8.25517 | -44.96033 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b09297c-943b-35e8-a3ee-bd6a34f58083 | -7.22255 | -43.07538 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0b4aa9e9-f0ed-370c-bc58-d515c60bde13 | -11.57916 | -47.87322 | 2025-06-20 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecb577ce-1e57-3dea-ac2c-2ebb98a42bc4 | -12.20897 | -45.53535 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f41be6b-c240-32e9-95f9-a02407038bf5 | -4.95008 | -47.46987 | 2025-06-20 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a8900d-6c7c-3a88-afe4-88eb37ba813b | -8.27093 | -44.95653 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93b1b0dd-0e8e-3624-ae21-f973ff9f15eb | -9.87163 | -49.3368 | 2025-06-20 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d03643c7-94be-38df-8c1a-f5fa9d371dd3 | -9.30103 | -47.79372 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9309b0db-bce9-3070-bbc4-e8f26da6917c | -7.15417 | -44.05971 | 2025-06-20 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b6fe46d-3650-3cd3-925a-30b7a416a1ad | -10.08703 | -52.74899 | 2025-06-20 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f5111ef8-89e0-368d-989d-f860954b7726 | -9.45804 | -57.83765 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6440c84-26a8-3e64-8f28-be733dbe6097 | -9.48556 | -56.08519 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 60d34cd6-adeb-31c4-8315-df38710f4849 | -6.1616 | -47.27146 | 2025-06-20 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a238276a-f2cf-3f15-908c-22f739138a09 | -11.45922 | -47.301 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 761de7e4-fe25-31a8-be66-eec48732dac5 | -8.27053 | -44.95948 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3fea8cb-3b74-3c55-94d7-d0d11d0e4937 | -5.18642 | -48.07814 | 2025-06-20 04:51:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a066f55-d06b-33a1-a923-e3de7219eac5 | -7.01748 | -44.58672 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a33ea26d-354d-3e5e-bedb-7cfe10a991cc | -7.15343 | -44.0598 | 2025-06-20 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33f392b0-d012-3e6f-bb41-03724e6daf15 | -6.67046 | -44.25321 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1e3adda9-a94c-37db-b272-fd81846cdaa9 | -11.15122 | -46.64905 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27503d0f-3a9b-3f4d-8805-9b1d7fa35704 | -8.37269 | -48.42427 | 2025-06-20 04:51:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe018c7-d7ca-3daf-92c3-5913536527f1 | -10.55794 | -46.96274 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ad22eea-1e4a-3f1c-a908-3b0d470bdb9d | -9.30609 | -44.72837 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cdc7da7-14dd-3d9c-a11a-b0804356e067 | -9.30688 | -44.72214 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f60a539b-dba7-3f8d-a1db-fdf5b5b597a5 | -10.43486 | -47.111 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b2ae04a-07f6-34e3-a19d-4b4fef8beb00 | -11.64262 | -49.18764 | 2025-06-20 04:51:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c28cf523-e07d-3975-a7be-85e8f0b0c538 | -5.44581 | -43.57612 | 2025-06-20 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a04d641f-9626-31cf-8efc-68d3cec99c39 | -10.43546 | -47.10653 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9133ce3-c20a-330a-9973-0e3cc1649e3a | -4.77791 | -47.25006 | 2025-06-20 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 227266d4-a34e-315e-bcaf-c78bab7ec26d | -9.31885 | -47.78809 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59f46cc5-9b20-3ec2-bd28-1b4f76834be0 | -8.72437 | -47.9889 | 2025-06-20 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db5f5a36-b061-3d22-95c7-d19a7399cd5a | -9.48337 | -56.07666 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 80ef6a55-8c47-35a2-9b25-cc1010860da2 | -7.70784 | -49.3452 | 2025-06-20 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5694ed0c-402c-3f5b-9005-c8b397b7183d | -10.72069 | -45.16389 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86c83efd-75be-33bb-b829-0c7e8f0ae354 | -9.09972 | -50.03084 | 2025-06-20 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d9d6289-6991-31ab-87ad-8a18f3caadfb | -9.48907 | -56.08576 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f5a48a9f-d37b-358d-96f4-ba599a79715b | -9.30649 | -44.72525 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83cee087-ebc7-325f-867f-5568a898d4c8 | -6.84369 | -42.79951 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd184b28-277f-3cac-8cc1-2f2997324688 | -10.49838 | -47.01109 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b7c8aca-ac6d-326d-a9e0-8452405ea244 | -8.37342 | -48.41911 | 2025-06-20 04:51:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfe0b3fe-0aae-38f3-bc76-a55d5e976e79 | -10.94033 | -49.43224 | 2025-06-20 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d40de92e-b1df-3e0a-a76c-280f84a204c6 | -4.37741 | -48.08063 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0daca7b-c397-34c2-8463-2e1164309f85 | -10.85882 | -53.76099 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd750fda-d6d8-3fab-ba4a-f90102a5cf73 | -7.11791 | -43.14193 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45adf18b-32a4-3806-9291-e60c4ab3e97b | -12.21521 | -45.52693 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
