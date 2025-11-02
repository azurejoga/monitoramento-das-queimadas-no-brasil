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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b05cbd20-39f6-3674-b7aa-2806c3ad4a04 | -18.51736 | -53.49661 | 2025-11-02 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9ea2e2a-533f-33c3-a8eb-a6ebaa97cc35 | -15.46712 | -43.20522 | 2025-11-02 04:23:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c68c540-b23d-3d47-9c4b-0e7f998c3de4 | -13.67809 | -43.43462 | 2025-11-02 04:23:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9617831e-5542-35c0-8486-4a5ae570d60a | -14.45805 | -51.52874 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d711de-91d9-3dfa-a9aa-604f70c57a7a | -16.97091 | -51.88593 | 2025-11-02 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 181aa2a1-dbf3-333b-ab73-55a0e7dd218a | -13.54509 | -44.07933 | 2025-11-02 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85791e0b-9e93-3f95-9b2e-76b188c31bb2 | -18.45669 | -51.62983 | 2025-11-02 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3d33868-1d57-3b4f-be91-19b8a1e6ff4f | -12.87504 | -50.86566 | 2025-11-02 04:23:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52dd035a-9ce0-322d-af8d-90275c988c82 | -18.48859 | -46.95625 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f6586d-ae88-3f96-83c2-88345f7f362d | -18.50456 | -46.9627 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5d87e57-d7d6-300d-bc9a-7c6332344968 | -15.82799 | -43.27003 | 2025-11-02 04:23:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1f49c351-884f-3984-9a65-d12bba636fc4 | -15.3244 | -42.04239 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c775b64-aec7-3eb6-9d5e-6a95b0fa7f1a | -18.50125 | -46.96214 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9670f806-cadc-3668-8440-3191aea4f75f | -14.6641 | -46.61793 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e118c6-f057-3dc5-a441-6477cfc4b9ff | -14.0217 | -43.48351 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 00efe412-20bc-3862-8391-00231ce4caeb | -13.61314 | -48.2641 | 2025-11-02 04:23:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb0e73a6-72ee-37b7-a300-833acc3a359a | -18.63009 | -46.87576 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3cab665f-5f12-3368-8c44-83a43e645934 | -18.63671 | -46.87689 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dbd2899-67a8-3e54-beb9-025e16a0cc7d | -14.0223 | -43.47942 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 16f461b8-f897-3fa2-ac80-efe680b8062c | -14.67158 | -46.63726 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77a25355-0760-335c-a245-b7d3070cce43 | -12.24526 | -54.38957 | 2025-11-02 04:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddbba497-ec8f-3fb4-875d-0c3b7e4f555d | -14.02643 | -43.47589 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 34368708-2943-3e37-84df-062fb4ce410b | -13.79555 | -48.87782 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b4f11d4-5440-3e0c-8213-795ee277c574 | -15.11321 | -47.24173 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47b15194-196e-302e-b0e6-4bad2c74234e | -18.62678 | -46.8752 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 666fe077-9120-3c8c-b689-39c1f8c3675a | -14.45741 | -51.53234 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b20f446-d13e-351d-8ca2-4007e9468b90 | -13.72424 | -51.45853 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3620cf30-03b4-3600-9a3b-aa9cf55ee49b | -18.51817 | -53.49245 | 2025-11-02 04:23:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7477138d-0c14-323e-b6f9-b53d1964b2ef | -13.8673 | -47.34895 | 2025-11-02 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbc5bc62-1c32-3d66-8f7d-52f73da4a882 | -15.62448 | -58.22486 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5077601e-acf4-3583-a69b-238951b1756e | -15.11874 | -47.24983 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82c3fa98-1080-3951-93bb-55370440dbee | -15.88055 | -54.39543 | 2025-11-02 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97333585-aca6-31a0-b0e0-5f11b745afd5 | -14.74392 | -42.46238 | 2025-11-02 04:23:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1af55406-490a-3dee-a929-a5695ae8c05b | -14.60068 | -46.65477 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 321954f8-423e-31a9-928a-684242bac14c | -14.87502 | -43.55681 | 2025-11-02 04:23:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0262966-8386-3d72-9f80-54df4393d914 | -18.49189 | -46.95682 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09992b8-bd28-37f9-90dc-9f1e0a704a48 | -13.7214 | -43.63723 | 2025-11-02 04:23:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9547ecf5-56c2-31da-aa15-75220568f0dd | -15.3261 | -43.88817 | 2025-11-02 04:23:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81c6a80b-1d40-39d4-9e16-ef28e59ee84f | -12.42302 | -54.49295 | 2025-11-02 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 754e1cbe-163f-31f4-b6c4-b594f119c257 | -18.50069 | -46.96576 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9dfa7a85-90fc-3b0c-a01e-122effacd106 | -14.87372 | -43.86853 | 2025-11-02 04:23:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbf0ee08-f272-3fcf-bb74-f3e1902c3a70 | -13.97402 | -52.45253 | 2025-11-02 04:23:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eca3a9af-375c-3737-9750-e6e5957c9566 | -15.97317 | -48.0703 | 2025-11-02 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f63e1bd7-786b-3a68-ad1b-5187c52d1668 | -14.02877 | -43.48458 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19576314-9ec3-3b4f-8aee-dcb1b656acfe | -18.4985 | -46.95796 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3bb295b-de7c-3533-bc22-7e32d56c249f | -18.80316 | -48.25997 | 2025-11-02 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c57024-7c17-3513-a673-6df7abf1a6ec | -11.72901 | -59.30706 | 2025-11-02 04:23:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f65e13cb-fb96-3697-b1bc-e3e710aeedf9 | -14.22912 | -42.95179 | 2025-11-02 04:23:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c88060e2-ae61-323b-97e6-7fb1fdbc4d1f | -13.79904 | -48.87849 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 951802f9-0e14-3949-843d-31853b34aa7f | -13.79037 | -43.28269 | 2025-11-02 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 595485f8-f9d6-353a-8684-0a5a8c685d62 | -14.29767 | -52.49459 | 2025-11-02 04:23:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b6fe258-ab57-3187-b5d4-7d586acbd280 | -15.6235 | -58.22943 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0bf374c-c163-3975-bac0-7151936627af | -14.15088 | -44.27101 | 2025-11-02 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 603352c5-8c6b-374b-a94e-15187f2ae11a | -12.87057 | -50.87344 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95968a97-0939-3c83-b8c3-b38cf1d55813 | -15.06649 | -52.79029 | 2025-11-02 04:23:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b80a3906-1f7d-3a09-9141-e25ff008ba5b | -14.45405 | -51.52798 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f1c5501-8d75-37ed-aa56-e5488d4fac09 | -14.02524 | -43.48404 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cb26eded-f3dc-3647-bcb0-27e2ba62e4ea | -14.61389 | -46.65696 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 809ba040-2f80-3725-98d8-34caa6c15938 | -14.65531 | -46.60918 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c1ba51d-1163-3e90-8089-de30198f9c97 | -12.87529 | -50.88708 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6749596-1bf7-30c9-aa99-914c8c9df872 | -18.52546 | -47.72037 | 2025-11-02 04:23:00 | NOAA-21 | GRUPIARA | MINAS GERAIS | Brasil | 3127909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddefeea2-bb6a-3469-8c24-62f07d682a44 | -15.07465 | -44.2984 | 2025-11-02 04:23:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecd09cac-4c33-305a-883c-2fd77e2b983a | -15.14101 | -47.21698 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c4d5b81-a3f5-341b-94d3-ced1b5c2f78a | -14.10456 | -44.20498 | 2025-11-02 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32e9e3cd-b673-3605-8a22-37b28aecb8a3 | -14.02464 | -43.48812 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 714c4b90-1c9b-3a30-a586-b6b415f8b877 | -13.44892 | -42.94693 | 2025-11-02 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6a5a014-c738-357b-8b7f-8c1f116816f6 | -14.66191 | -46.61028 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dc641a8-a972-30ec-a2b7-373343cedad9 | -11.7359 | -59.30828 | 2025-11-02 04:23:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 39b22473-bc2a-3460-a4d4-bbc7122c3a1d | -18.45062 | -44.90807 | 2025-11-02 04:23:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cb0f975-112b-371e-8917-f77bb1bfc03d | -12.87017 | -50.87012 | 2025-11-02 04:23:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6eb18504-925c-3838-91e8-84ec5f2248b8 | -13.84419 | -47.04655 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51963713-8e74-3bd6-9832-fd606fd98d37 | -13.84692 | -47.05071 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea6de0f0-cd75-3f50-9354-f49bdcf3fbbb | -14.86975 | -51.806 | 2025-11-02 04:23:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73826fa6-a656-3d6f-babf-eb946695a7e3 | -15.11542 | -47.24932 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00cbaf63-6f49-305d-befc-d403f784660a | -12.8711 | -50.86495 | 2025-11-02 04:23:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ff12eda-28ef-3f3b-944f-a068774f0444 | -16.85337 | -40.69711 | 2025-11-02 04:23:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a988f6c8-17d0-30d1-882e-d315b9c24297 | -18.56682 | -43.56959 | 2025-11-02 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e87727c9-8ad5-3db2-8ce6-bc7eb0d9f203 | -15.29672 | -42.95798 | 2025-11-02 04:23:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb787a9f-8025-3787-b591-ab9fd920179e | -13.83938 | -49.52488 | 2025-11-02 04:23:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4505635f-ebae-3528-b437-2024fb0f995a | -13.84966 | -47.05488 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6f6e7fa-f35a-3d6e-95c7-ed448a9128f4 | -12.87831 | -50.89297 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aafdeff-ef2c-34a9-bf74-2d2a86ea838e | -14.59291 | -55.99791 | 2025-11-02 04:23:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03316e2c-1ac8-39f6-b93c-a432308116c3 | -15.62948 | -58.23086 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5ad774a-4566-3ee9-99fc-78ddf81f01b8 | -14.30825 | -47.12458 | 2025-11-02 04:23:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15c27486-81ce-3f8f-b1b7-525860958749 | -13.76352 | -46.8909 | 2025-11-02 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d44cd46-aa37-3977-b2e4-b4f075d1b722 | -11.72769 | -59.31339 | 2025-11-02 04:23:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4315c728-7441-34ba-a951-73dac7dc04b7 | -16.35229 | -46.32708 | 2025-11-02 04:23:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d03a438-e46b-3e4b-be34-a1e00313c53e | -14.02583 | -43.47997 | 2025-11-02 04:23:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 26064637-bb4a-3301-9793-bd1bc26be28c | -15.12929 | -46.23226 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdeeaabe-77c2-3ed5-bd3a-5ae9ba2ea34f | -14.87429 | -43.86451 | 2025-11-02 04:23:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbd2d54d-cb78-3bb3-be0a-02415a9f05b8 | -14.66884 | -46.63317 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e377389f-7bc9-31a8-9bd9-0f232c2f2b4c | -15.83386 | -44.68397 | 2025-11-02 04:23:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f96bf46-17ba-3dc3-8ade-9d3adde8497a | -14.66721 | -46.62197 | 2025-11-02 04:23:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe0a6fa5-4f5f-36ae-bb88-88c73f9b14b1 | -15.60732 | -46.04309 | 2025-11-02 04:23:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b016a3b7-66ae-3dc6-a45d-7740beaccb39 | -15.12984 | -46.2287 | 2025-11-02 04:23:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9522104c-2385-3006-b322-179359492fe3 | -12.87274 | -50.88453 | 2025-11-02 04:23:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1a85002-c2f7-3514-95f5-2c5f79dd1f70 | -16.74003 | -44.15813 | 2025-11-02 04:23:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cdeb5ed-dbcf-3557-8df8-cbe5ad53e3e5 | -15.46774 | -43.20085 | 2025-11-02 04:23:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd0c1a0a-dc5d-318e-a1b5-3885d8f8a2f9 | -14.87857 | -43.55736 | 2025-11-02 04:23:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d46b644f-edea-3fc3-92ac-21287d098df1 | -18.4952 | -46.95739 | 2025-11-02 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
