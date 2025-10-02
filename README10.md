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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 122022c6-0143-3f13-9419-a74da3d282ff | -7.41217 | -45.20029 | 2025-10-02 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea99fc4b-fda4-3fad-a1cf-e1dbab770df8 | -6.13377 | -47.2502 | 2025-10-02 00:13:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c10e1e0a-965d-3381-9d7e-c583cf8afd6e | -6.733 | -44.15182 | 2025-10-02 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0a541bdc-fbf3-3ce8-bbe6-03e47ff43909 | -10.24198 | -50.35419 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 5536920c-5a87-399d-a37a-f3c353ed5055 | -8.56833 | -49.61655 | 2025-10-02 00:13:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ae7437e2-c21c-3ee5-b62e-7ee7a2120e60 | -6.39 | -43.8683 | 2025-10-02 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7bf475fe-9992-3564-a58f-e7fdcf45d959 | -3.80669 | -51.30656 | 2025-10-02 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fab9a080-93e4-3f3a-abb4-c9b0d3a826fe | -7.5301 | -46.90759 | 2025-10-02 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e28b8059-5644-394b-a8c0-8fab6238cda2 | -6.4771 | -44.43114 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6c93d3e-a105-364b-b0e2-284ce9f0831c | -6.37995 | -43.86077 | 2025-10-02 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad461c48-664a-34f5-96d2-1c38a8a0b45a | -3.8152 | -47.58191 | 2025-10-02 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4ea6de08-f9b9-38aa-87b4-0c79faebcd4b | -8.51754 | -47.81339 | 2025-10-02 00:13:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 919317a6-ec5c-3dd0-b099-d98fe40d8346 | -4.14138 | -44.4029 | 2025-10-02 00:13:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83d7eb43-282d-3f8d-abb7-a56025d91e8a | -4.93471 | -43.41766 | 2025-10-02 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4d447369-f6cb-38ae-80af-1c0777ad0c70 | -6.7827 | -45.5838 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1948a0df-c814-3d4d-b1d7-2386327f0a26 | -6.96914 | -45.32998 | 2025-10-02 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| edfb5a6b-cbae-321b-85b6-fa1b651750e2 | -10.21019 | -50.31447 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 71f92a46-4526-3c49-8c1b-35887e44c46b | -7.02772 | -44.47853 | 2025-10-02 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf64f274-3b78-391f-b758-969881002b5d | -9.45555 | -50.90631 | 2025-10-02 00:13:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 55b9a892-9ed9-3901-af83-4320a1157acd | -8.77558 | -40.35822 | 2025-10-02 00:13:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 4a175f35-fd19-3838-b31e-217a0dbf97f7 | -10.24467 | -50.37574 | 2025-10-02 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 685cc6df-6ff6-343a-855c-a7c89037be3f | -7.78085 | -42.54624 | 2025-10-02 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 2df753e1-b1f2-3282-b93e-ad18299104c2 | -7.60619 | -47.33216 | 2025-10-02 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 074a7fdc-ca86-3239-b74f-a72e925bec29 | -7.77046 | -42.53817 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 7341f25b-fcd0-3f9b-9e2f-0cdbecea0f0e | -3.8178 | -47.57512 | 2025-10-02 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b6d3939-0e27-3a87-8c96-b55e806cb590 | -3.75418 | -41.03972 | 2025-10-02 00:13:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7b8bd788-8aab-3880-b07b-561fb92df027 | -5.89751 | -45.64585 | 2025-10-02 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c462a20-1fc3-3538-9aae-139b8f9ca6c5 | -6.39029 | -44.665 | 2025-10-02 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 545db587-cbf0-3387-a1ed-1a6874c0af91 | -6.73177 | -44.14301 | 2025-10-02 00:13:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 43a93096-a464-3502-9f83-80dbb9c258e2 | -6.79127 | -44.90075 | 2025-10-02 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a7fb4cc5-e009-3152-9066-776e262cf761 | -2.92222 | -48.29581 | 2025-10-02 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6f6aa2a5-80ee-3352-930a-87db8f6d8cf2 | -0.90605 | -47.54638 | 2025-10-02 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| edc570e5-535b-33a7-9422-3f4bf83c72a2 | -1.37355 | -49.29063 | 2025-10-02 00:16:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 42d87562-1de6-362c-aa3d-4bc668677626 | -1.26454 | -49.03845 | 2025-10-02 00:16:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ca0ec2bb-c2dc-3b6c-acaf-cd3cf3ec244c | -2.73919 | -48.67563 | 2025-10-02 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c1534201-3fa0-3ee3-a0d5-db0e7f4f32a3 | -2.96342 | -48.60229 | 2025-10-02 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8536d30a-32bd-33c6-be25-07cec1811c4a | -2.70112 | -48.83728 | 2025-10-02 00:16:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2e62dbf4-2e06-3d8d-9c70-1b1d025d4d8a | -2.42607 | -47.14154 | 2025-10-02 00:16:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 46a93c57-809e-331e-9aa0-db069d81c608 | -1.58141 | -47.30361 | 2025-10-02 00:16:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4f36cc95-cefc-3c23-9287-d152923d259e | -2.26608 | -47.8444 | 2025-10-02 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4db6f09f-a76e-35c0-b828-1a2664dc4de9 | -3.49764 | -50.27418 | 2025-10-02 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c1763e3a-c155-3baa-bd64-aa34741527d8 | -2.42741 | -47.15131 | 2025-10-02 00:16:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1200520e-df8f-3532-84c3-7f9e02dbd060 | -3.09163 | -47.0162 | 2025-10-02 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 72c0f258-40b6-3bb9-a302-1964389fbfb2 | -2.24301 | -47.89073 | 2025-10-02 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 424c59ee-0769-3c12-93c1-21f94c5645ed | -2.92377 | -48.30732 | 2025-10-02 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b9086515-c443-3ced-a953-0534f5d825ae | -2.66081 | -47.8686 | 2025-10-02 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 78bae704-433d-3872-887a-1aa139b768e5 | -1.58274 | -47.3134 | 2025-10-02 00:16:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4cda3596-3853-3512-b1b3-2ff569c70ae5 | -3.09028 | -47.00647 | 2025-10-02 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3c810b3d-bfb3-33fb-b33c-ef6256e76091 | -3.0492 | -46.9825 | 2025-10-02 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 75c21c61-a65a-3d1a-b8a9-cba5d90906c3 | -3.48529 | -50.09539 | 2025-10-02 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3dfd55ee-4c8b-395a-9ba1-e17b8b1a1fa2 | -1.33155 | -47.9596 | 2025-10-02 00:16:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 490603c5-6f1d-3478-9035-88ffc506d3e3 | -3.45998 | -50.08285 | 2025-10-02 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 920c72dd-213f-3ac0-b967-d9388d94c425 | -2.19772 | -44.82005 | 2025-10-02 00:16:00 | TERRA_M-M | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d9eb326c-ee68-3063-8232-b4c98c81e168 | -3.46208 | -50.09849 | 2025-10-02 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1267cb13-74cf-3bbc-8192-354857eaa486 | -2.47447 | -44.95073 | 2025-10-02 00:16:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6573e63f-0e22-32ac-a348-0022551ff073 | -2.26755 | -47.85496 | 2025-10-02 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3fd4fec2-4a6b-3e43-bdf3-0207705efecc | -14.3119 | -45.9736 | 2025-10-02 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bedbf20f-8e6a-3a0a-a831-88b00dfc0cf9 | -11.5947 | -47.226 | 2025-10-02 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| e1383314-6e53-35d5-b42e-59ebce48a6fd | -12.8355 | -41.5343 | 2025-10-02 00:20:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| cba84193-bd78-3ffe-a49f-83b467a7f9ac | -15.2738 | -49.3073 | 2025-10-02 00:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8af8f86a-946c-368e-a837-782b8ceeb2c9 | -15.2547 | -49.2883 | 2025-10-02 00:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a11d784e-38fa-3b52-bd65-4cef13de374b | -7.7755 | -42.5152 | 2025-10-02 00:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| b3baf470-43e1-3d2e-8ecd-8b24261318db | -11.5951 | -47.2036 | 2025-10-02 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| be923e9a-00d0-3fc1-9d83-bc5178ed8999 | -5.9858 | -44.589 | 2025-10-02 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| dbd0192d-04ff-3e7a-8b4c-64e2a2c43b62 | -13.3278 | -47.8313 | 2025-10-02 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 19d7aea1-24c0-3c57-8484-51682c8a25de | -14.426 | -46.0919 | 2025-10-02 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 1548aeb7-fe9d-332f-a388-c1ed47888565 | -6.2411 | -45.3198 | 2025-10-02 00:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| ceda9cce-9b58-3387-af7d-0af8dcfda243 | -10.8428 | -46.6064 | 2025-10-02 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| eb5a92eb-b67b-383a-98f2-ca0391c6114d | -14.4065 | -46.0953 | 2025-10-02 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d4a7437b-5305-3520-839e-89a31e386052 | -13.4248 | -47.7945 | 2025-10-02 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 136ea693-ce31-3556-bbdc-112a0518ed1e | -13.8637 | -51.2517 | 2025-10-02 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e2c37eb1-1ac3-3957-920a-b196557c8323 | -14.4255 | -46.115 | 2025-10-02 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| a56b1215-f0f0-3952-bfd7-6f33f351d011 | -13.0119 | -45.1988 | 2025-10-02 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 10b86d19-5a33-3ca2-a5b0-242d6c32cc37 | -13.1546 | -47.8345 | 2025-10-02 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f4b4ae1a-1d95-30f5-a1fa-126e38c9af4c | -13.0114 | -45.222 | 2025-10-02 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 5edf3a0d-d960-3187-a719-5e8660ecceda | -5.9671 | -44.5904 | 2025-10-02 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 14075651-d087-3d96-9580-7288b16f4f88 | -9.8713 | -46.8801 | 2025-10-02 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 92ced8f6-ef5a-31a2-b3a1-b11ab4304af3 | -15.2742 | -49.2852 | 2025-10-02 00:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 12f70a94-084c-302f-8b3a-260897dff8cc | -12.4207 | -54.3536 | 2025-10-02 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 7e7de09b-d8af-32fd-823d-d84a4bdd61c2 | -8.6035 | -50.3952 | 2025-10-02 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0fc2f2aa-45dc-3720-983c-5b8f9a500188 | -6.7211 | -44.1618 | 2025-10-02 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e386377a-9214-3aff-b2c1-57e2a7e09154 | -8.5748 | -49.6095 | 2025-10-02 00:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7c00af23-2257-31a8-85fb-6ff49749af61 | -9.8523 | -46.8823 | 2025-10-02 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8c1c9e4d-e413-3fb2-b989-6186cd701a5e | -5.986 | -44.5661 | 2025-10-02 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 86b94900-ee17-3ac7-8862-0c88e221cbee | -13.3085 | -47.8341 | 2025-10-02 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 24a14f3a-2542-380c-89e8-e54ded329318 | -12.4737 | -47.2621 | 2025-10-02 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6431a993-1157-3a4d-9fc9-2934a7fa6372 | -6.7213 | -44.1387 | 2025-10-02 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a495c1d3-500f-37bf-9705-927f20d2a571 | -10.8424 | -46.6289 | 2025-10-02 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2df89bb4-d5bc-350f-a659-8d58405e7436 | -4.8596 | -45.2109 | 2025-10-02 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 974b1943-5516-3ad6-b0f2-54ee45608d3c | -8.6223 | -50.3936 | 2025-10-02 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| abf80d2f-ca54-3fdc-844d-faea63662f48 | -5.9856 | -44.6118 | 2025-10-02 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b5a41424-4999-37a4-acdd-895aa3c933e7 | -12.122 | -43.4215 | 2025-10-02 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d041f190-7bdc-3718-9620-2dd9164bf16b | -15.2542 | -49.3104 | 2025-10-02 00:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9aaa5418-392b-3c99-9d25-03bcf8675d8b | -7.7752 | -42.539 | 2025-10-02 00:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| dcbfe028-4159-3caf-9e95-3f5da3cb15d8 | -6.0046 | -44.5875 | 2025-10-02 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| d28627e0-e401-3272-9247-78446b7e8113 | -7.7752 | -42.539 | 2025-10-02 00:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| f450d5e4-4e9f-31ef-9e45-0bfcbf9eb3e8 | -11.5947 | -47.226 | 2025-10-02 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c710ab0c-8fce-36b3-8e1b-0f7e28e9dd5a | -18.5058 | -44.0386 | 2025-10-02 00:30:00 | GOES-19 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c2f11711-8c8c-38ec-a6c9-dff9b7e65098 | -5.9671 | -44.5904 | 2025-10-02 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 841bb01c-d812-3227-8201-396ed54e71b9 | -18.131 | -42.4121 | 2025-10-02 00:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |


[Clique aqui para ver as próximas entradas](README11.md)
