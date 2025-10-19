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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6da88b38-7f05-33cf-a19e-d41abecc6baa | -4.98414 | -43.85211 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa9ff7a0-6500-36ef-b3de-685733df16ad | -7.20402 | -42.19546 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5896b223-7324-33f5-afbd-a04bf244aad5 | -5.71389 | -43.82112 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea9a7b5d-b53e-3e8e-b67f-9e34d2c98e55 | -5.64539 | -46.58496 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9aad0e41-026f-3d49-8328-50277ed65416 | -5.30292 | -45.07679 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4d65e619-8bd8-33d4-9e12-c950f6127d4a | -9.75679 | -43.95507 | 2025-10-19 03:42:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1399bab-0693-3224-966a-9577a061e7bc | -8.34757 | -46.22232 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95304e46-dee1-3088-ab20-88f3299cad91 | -10.15981 | -42.20983 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2208808f-5fe2-3367-95c8-0df77fed5689 | -7.16588 | -42.3587 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 688ce3af-68d7-3037-95b2-93a8e801e28c | -8.21615 | -43.96416 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7768037e-2e8d-3c1b-9cd2-38f8b0a23067 | -4.57693 | -45.88186 | 2025-10-19 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8dc84067-3ad8-3cdc-8f50-d7e391bf80a0 | -4.91423 | -45.41765 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0968cb2d-5cf1-3c2b-8f1d-db8774f2494c | -5.95695 | -44.1936 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95c03a78-85d2-3924-863f-4d0e56bc6996 | -4.96316 | -45.91586 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b5a9c2c-3bbf-3b29-950b-ebe7228d527c | -8.61582 | -40.19086 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 81cb3dcf-6c45-3775-801b-9e3139deae31 | -5.10157 | -46.13443 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 71a6bb4e-054c-3f76-aeaf-c3356d768d61 | -4.2453 | -44.68048 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9275feed-d593-3f47-96bf-17d99fa2b2df | -5.49106 | -43.54515 | 2025-10-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 354b860b-02f5-3c80-8978-94534c8af038 | -4.92309 | -45.70837 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddfbba82-5f38-387f-af6b-d659a4dc930c | -8.21668 | -43.96124 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f9d07c-e47f-36fc-a8f4-74b2ede03c1e | -7.19785 | -42.20397 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b362d85c-8ae7-343b-8359-6f3612910e9a | -4.30907 | -48.06559 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d871964c-8e83-3ec2-83bb-535c5e801d88 | -8.24267 | -43.99011 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dfcbd24-e238-3817-8b1b-ae9e7abade6e | -6.05528 | -44.51889 | 2025-10-19 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdafa932-4b8c-31ae-a1ba-539069d6e2fd | -5.64025 | -44.81123 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8450517f-e2d9-3db7-af08-f832c31cc0e9 | -4.13991 | -47.65869 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87b3ada7-fea6-3e31-824b-dd06c9ae9bd0 | -7.18512 | -42.21738 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ec511512-e811-37b2-b9b8-1723d43ebcaf | -4.97071 | -44.61286 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e64c87c-1633-3316-8aff-02fe0ed08338 | -8.60309 | -38.84632 | 2025-10-19 03:42:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5c7efea-09ed-30b3-87b3-ab21b18b03f7 | -9.13469 | -43.24328 | 2025-10-19 03:42:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 83628c85-fcc5-391e-8439-0cebc1dcf999 | -4.24595 | -44.67665 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f87d6218-9c32-3b79-a34b-ba7efe103950 | -5.47989 | -43.13012 | 2025-10-19 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7cefe50b-38af-34c6-b6e6-278c29ec11c1 | -4.25139 | -40.35019 | 2025-10-19 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 883578c5-9931-3859-970e-94b3f8fb06fe | -8.6197 | -40.19154 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 68eb8685-ade7-332d-805f-8ee01a88ed7a | -7.41723 | -40.07534 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 10014f45-9e11-3a7f-8e1a-6eda77c43e28 | -7.18967 | -42.21812 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 85d9c825-ea36-318b-8ae3-e39bf08378a1 | -8.55486 | -44.57476 | 2025-10-19 03:42:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4958fa36-42b0-3c85-82e6-856ad183c4b9 | -9.66803 | -44.55724 | 2025-10-19 03:42:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de4ede6f-334d-3292-a722-d493007b36ec | -6.79264 | -46.47106 | 2025-10-19 03:42:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afe1ee65-13d9-34ab-8e97-a10c7c7f8749 | -7.95618 | -45.94192 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1327c2bf-eb52-37c6-9425-04dc60a1a5c1 | -8.02745 | -43.9246 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25c80d02-68f6-3c51-a9b4-b29a67fa2955 | -7.15878 | -42.37208 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 28bd519f-a994-36a7-8aeb-b03dbc6192de | -5.67565 | -47.9891 | 2025-10-19 03:42:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692314a8-dac0-3642-8512-55094791799c | -9.17974 | -43.23595 | 2025-10-19 03:42:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a50341a4-12a8-3b25-a33d-f42874da00d9 | -8.4267 | -44.14346 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fccf97ae-d468-3731-b0fd-d2ab62b51b58 | -7.27824 | -42.30913 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c62b3169-048e-3499-ada3-b6e84dea47dd | -4.23877 | -43.09855 | 2025-10-19 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52416866-8ab0-396a-8a79-fd4d4f47b106 | -4.85425 | -44.59719 | 2025-10-19 03:42:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48c1ee5b-da97-3c34-a28b-d691507f309b | -4.59183 | -45.3834 | 2025-10-19 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4d15986-16d7-3ff9-a088-3889432723f6 | -6.00485 | -40.22388 | 2025-10-19 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c847cadd-e246-3e81-93f6-5b5564be6389 | -8.61756 | -40.1983 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 06f14235-0516-3a40-9535-ad40835b3a31 | -7.05055 | -41.8299 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bd1d107a-c4b7-39d1-a8d8-4d31bd442ab1 | -4.44467 | -43.22012 | 2025-10-19 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d42b65a-9359-3412-940e-093fd6f9e9d1 | -7.65666 | -44.6325 | 2025-10-19 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c7975f3-1957-3738-a3bd-606e02d81ab0 | -4.58074 | -45.37755 | 2025-10-19 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ecda9372-2dff-3185-ac7e-97ec245d710f | -8.65771 | -41.03616 | 2025-10-19 03:42:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 105cf2e3-4bbd-3878-bfc5-73008ab9138f | -5.64656 | -46.58821 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fe16661-2c25-3a3d-b9f1-0288a0be8533 | -6.36726 | -45.75148 | 2025-10-19 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6613cb96-46de-330a-8eaf-f9341fc6882c | -5.6451 | -44.81146 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e92b528-0c33-318f-b602-5e3099971208 | -5.31712 | -44.84511 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 32042dc6-9a94-355f-8b81-19ee4ce92830 | -5.10726 | -47.79362 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa5c6476-fc5e-3f23-bde2-6cf83674aa17 | -5.10074 | -46.13907 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 14f97929-691e-33d4-b5e7-c859fb0dd6f9 | -8.43223 | -44.14183 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f46856f1-e810-3f5b-8e5c-c5e5b4c68069 | -3.97687 | -47.58046 | 2025-10-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d68fd7-3638-3705-a899-5d21599b7cb3 | -4.99635 | -39.06318 | 2025-10-19 03:42:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5b8e49aa-8b04-384e-9fb9-104e06c4f3c6 | -8.08207 | -41.07364 | 2025-10-19 03:42:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed3f627a-2678-30cf-b687-c53ac443f3ff | -5.55784 | -44.95334 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a27ea69-a638-3c7a-b26a-e16ffc0457a3 | -4.58547 | -45.37741 | 2025-10-19 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c58fd4a0-82d7-3b70-830e-4c728ceb4a2f | -6.00841 | -40.22451 | 2025-10-19 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 33aee9e6-ee0c-3c0a-aa08-75448dc921e6 | -4.95734 | -45.09441 | 2025-10-19 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2b66660-93f2-3a97-8dda-8dcc7280168f | -8.44615 | -40.57661 | 2025-10-19 03:42:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c48adc7c-c535-36e0-8f25-0ad3a75bdaa4 | -7.97291 | -43.8837 | 2025-10-19 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c27abf3-2db4-354a-8833-a12f71a4ee3e | -4.82959 | -43.01675 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d415fbd8-9ffe-387a-b8b9-902d778f5df5 | -4.92296 | -45.67388 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 395f9a6c-3ccc-30d6-8ee4-b6d5c0e33738 | -5.7144 | -46.45212 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 578b2a78-4f96-3842-86b7-e2119d83bbaa | -4.95903 | -45.09369 | 2025-10-19 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f42e51b7-1318-3088-baeb-b75477d425db | -7.96786 | -43.88296 | 2025-10-19 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b86fbbcb-013c-3d12-81aa-8bac8e2e7084 | -5.10604 | -47.80025 | 2025-10-19 03:42:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03af39a6-d855-3401-8f7c-21635af533d5 | -7.04832 | -41.82228 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b23e774d-d4bd-3710-8c4f-3f188ed77d15 | -8.19936 | -40.45768 | 2025-10-19 03:42:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 535a6020-405d-3d8a-a5d8-27c537c7d402 | -5.35449 | -47.21554 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6be4e94f-759a-3e2b-b23e-1b74df9a00b5 | -5.6412 | -46.58228 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf54813d-c917-3b99-9d79-e45813397474 | -7.83845 | -41.75258 | 2025-10-19 03:42:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0779f99e-0f33-3487-a387-407dc47c47db | -5.36092 | -47.21698 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 15fde404-e8d8-30c6-94d4-9f0258d760cd | -4.24718 | -40.34952 | 2025-10-19 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00e2683d-91da-3ecc-a93a-1875609e0a51 | -5.60548 | -42.67765 | 2025-10-19 03:42:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5af1ac5a-ca42-33db-a407-57be8101a184 | -7.19577 | -42.18921 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6eec618b-e328-3bf5-937e-3cea2f90b623 | -4.24333 | -43.10236 | 2025-10-19 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02c6aceb-7bb0-3d3d-99ad-96bbb5155484 | -6.8615 | -46.2984 | 2025-10-19 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35dfb54d-7894-31af-bc34-3adf027fd0c7 | -4.24465 | -44.68432 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0f12e9d-1bc4-333e-9ee3-44666243ac7a | -5.71096 | -46.50634 | 2025-10-19 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa5d5899-c702-334a-88c6-efb9f7c627df | -5.64521 | -44.81572 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 052b08e1-2587-35ce-856d-643b5a98cf2f | -7.19143 | -42.17995 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ec767140-9a20-3927-9f33-2f4452fb9ecf | -5.3209 | -44.84522 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 344ece93-43bf-365c-a5d3-0a5e28a515a0 | -6.00171 | -44.18071 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8165f5f4-279d-38c6-b3ab-357c22f0e657 | -7.19949 | -42.19466 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 209b7fd0-1c46-3716-b4df-254ccad21557 | -4.83508 | -43.01465 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 730d1a13-ab3f-37b8-8edc-c96eaa606d32 | -5.71445 | -43.81798 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 406a5b6d-11a9-3729-bc5a-a278de7a2d7a | -8.2477 | -43.99108 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92d388fb-f5e9-3287-8561-066b08d808d7 | -8.61496 | -40.19583 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |


[Clique aqui para ver as próximas entradas](README12.md)
