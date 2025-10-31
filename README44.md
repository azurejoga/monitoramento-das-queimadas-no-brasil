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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 782f5d40-0458-32ff-9291-d5ae11fa0c3e | -4.0055 | -42.09706 | 2025-10-31 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 95bde108-a9be-3f20-a218-bca6f1b5a51e | -3.70639 | -42.31376 | 2025-10-31 11:57:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 16a87de8-62f2-3d0a-927c-f97ade359aba | -5.37331 | -42.64968 | 2025-10-31 11:57:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9422dc9b-f874-352a-8819-ebd8fe0911f8 | -4.65274 | -42.52588 | 2025-10-31 11:57:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 2509d645-509c-3f50-9969-0c147cf8f2c1 | -6.27857 | -41.81158 | 2025-10-31 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cfe1bbfe-5bbe-3735-887a-d689003007a0 | -13.35089 | -44.92187 | 2025-10-31 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f8ae0478-7e81-3ef4-acbf-1bf36a7372b2 | -12.88871 | -44.98897 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 846baa95-ae6e-30e2-9c29-a80911573b13 | -8.60045 | -43.95126 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2101e1a0-be2d-32e1-a81d-529e8402f67d | -7.08133 | -44.94042 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 16093f4b-16eb-3138-8b69-14c23f9e267d | -7.00492 | -42.79329 | 2025-10-31 12:00:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c9d5dd92-b090-3547-a77f-3a1a4b538957 | -7.34974 | -44.99825 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dc5a75ed-629c-31fd-8939-7e19afba65a3 | -9.86144 | -44.86182 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| da23a5d3-3c04-30e4-844c-3e9bd8fdfbb7 | -11.30095 | -44.48437 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 471b9a9b-83d5-354d-8bc3-4741cfa9af02 | -9.24389 | -45.53575 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1bcb8596-8300-3099-bf41-d97f2fc853d4 | -9.86417 | -44.84311 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 15652845-28f6-379f-aaa0-ccd852fdceca | -6.2776 | -43.61917 | 2025-10-31 12:00:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b97dcfd6-df33-3194-9310-3bf7b718f884 | -10.62355 | -42.31906 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 1f3bac53-2ede-3e39-b31c-d016e11127ff | -7.0735 | -44.92927 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 2f6bbf5b-8434-343e-8ba1-2bad33298d35 | -14.45167 | -45.28974 | 2025-10-31 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| d2ea45e3-4e0e-3567-8764-69b8b530600c | -9.8628 | -44.85246 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d2cc3c88-d6ed-3913-a16b-f09df52dd037 | -12.82799 | -43.48863 | 2025-10-31 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 70cd39ab-bd09-3bed-bf72-d1a48f6c92e4 | -14.11274 | -46.38149 | 2025-10-31 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 05e080b1-c61e-3151-9137-16de02e4422e | -15.96625 | -44.44804 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ce543786-d8b3-3036-84f8-61d834f6c3f9 | -10.5394 | -44.77522 | 2025-10-31 12:00:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c52e3ba2-e7be-3e5e-b526-e5b03bb92bae | -11.29964 | -44.49339 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fff656f1-a79b-36c9-9e99-738ecd623247 | -10.24636 | -44.56686 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 27bc24e6-8a31-3aa2-943f-8737ea4c7fea | -7.07493 | -44.91945 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 888430c8-5f54-3ac3-8437-6c17689c7a57 | -6.84899 | -43.43746 | 2025-10-31 12:00:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0638b534-6eb0-3e40-bb48-8140b98ddc82 | -10.65434 | -45.24324 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 36.5 |
| f57e1825-c14c-3288-8212-ceea69d6ef55 | -14.45032 | -45.29889 | 2025-10-31 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 92842ded-9f72-3824-8556-4d62833ab579 | -8.36291 | -40.28096 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 8facef90-82e0-3a77-932a-685ae03a92a1 | -7.22905 | -44.30691 | 2025-10-31 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 98125fbc-2052-37ca-be2b-d9fa5d502c20 | -7.41215 | -45.76446 | 2025-10-31 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 72be81d8-55c9-3c3b-94e3-49e8bb3b3b7b | -6.90426 | -45.52119 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb6a244c-63af-3034-a8d6-a9ed427e647e | -14.62836 | -46.82274 | 2025-10-31 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 138342c9-6d65-3b50-8c25-cb6b667a314c | -14.66435 | -41.52244 | 2025-10-31 12:00:00 | TERRA_M-T | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 6de5c905-9c70-3aaa-82d4-1d4a74f22675 | -11.79788 | -42.62136 | 2025-10-31 12:00:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 398e5a94-c307-3068-a818-51b6e024aafd | -13.06921 | -43.01973 | 2025-10-31 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 98a0872c-060a-37a0-b099-0f211fe437de | -10.92496 | -45.22463 | 2025-10-31 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 159b02d3-fd5b-3c5c-b91f-e43761cbca26 | -7.38991 | -43.01318 | 2025-10-31 12:00:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0198e7c5-a0e3-3487-a73b-e1561cf07169 | -10.44111 | -44.31173 | 2025-10-31 12:00:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c5c16dc6-d768-3375-aaa4-b24b87d8af65 | -10.43095 | -44.31939 | 2025-10-31 12:00:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b26b1dfb-e352-3ed0-9d33-556ea1856dda | -9.22689 | -43.00891 | 2025-10-31 12:00:00 | TERRA_M-T | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 55712b2f-ff81-39f8-9de5-28f0a47d7e79 | -12.60455 | -43.11179 | 2025-10-31 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 6bcc13c7-7779-3b55-80ab-af494df357a9 | -15.85458 | -44.89938 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19bac761-a808-3e9a-b0f2-422a4e3f952a | -14.66697 | -41.51773 | 2025-10-31 12:00:00 | TERRA_M-T | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 98e01c23-828b-3909-8f5a-04e09f094c7a | -11.05557 | -44.01811 | 2025-10-31 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d4517b24-3448-38e0-91af-7f38e1dc5293 | -10.63258 | -42.32031 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 140.4 |
| b4d29388-8cc1-3c68-9d0e-057f39758145 | -7.65637 | -43.59885 | 2025-10-31 12:00:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 49ad7d81-aafd-3f93-a774-f4dbd069ef6b | -8.10546 | -45.18497 | 2025-10-31 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 76016ccf-9f12-36b4-ad62-e039f7a9608a | -9.87891 | -44.87043 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 42e4b73a-1ebc-3f78-99e6-36c1b454d32e | -14.44437 | -51.56432 | 2025-10-31 12:00:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 39.7 |
| d7d15032-9dd3-3ca1-a5ca-b1d37b4e759b | -7.31846 | -44.95378 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 086d85f7-2f12-3f88-b6f3-8215f534d36f | -10.27249 | -44.45023 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e6b939c7-bdec-381b-8fd5-a9df0de54c16 | -7.08419 | -44.92081 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ac6769a6-57e2-3c12-aa4d-fae7ec0759d4 | -7.81704 | -37.59332 | 2025-10-31 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 27.6 |
| a87066a7-77a1-3b0d-aef3-e53909053292 | -13.80698 | -42.28002 | 2025-10-31 12:00:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d907ecf4-3b44-3f61-8b27-865655c849cd | -7.21867 | -44.31495 | 2025-10-31 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3fbce61f-8b2b-32b9-b9e2-02b4f0924908 | -7.28926 | -44.95952 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8340cc0f-675b-3c56-b8d9-e2e884ee09e3 | -13.37852 | -43.64809 | 2025-10-31 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 24eefba5-0df7-3024-8eec-33546d0cd970 | -8.02466 | -42.50782 | 2025-10-31 12:00:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 0e6f8c06-596e-31d4-afb8-fb680acd2e18 | -8.92196 | -40.54355 | 2025-10-31 12:00:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 261a47f7-cffd-3887-ac5e-fa84040a6421 | -12.96697 | -44.77483 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6a7a952c-12da-328e-b956-f7d16e5f6c8a | -10.42078 | -44.32711 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| cb8b5b70-cb16-3466-b8c2-fd8f7c4fbb6b | -13.67891 | -44.70879 | 2025-10-31 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| fec97cfe-394a-3162-88a0-7fa74c7a2a18 | -9.85379 | -44.85118 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 14e6102c-d81c-369b-954d-4c475a0a21c2 | -12.7698 | -43.4525 | 2025-10-31 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e60f3c70-109f-36a1-8eb5-d3f0a1e3bd1e | -10.89519 | -44.36317 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88a6211f-a38e-33fc-8bf3-13572b742bc2 | -13.38265 | -40.63476 | 2025-10-31 12:00:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 787515ad-82de-3225-97d7-d75624c9eeca | -10.2636 | -44.44894 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 249f760f-0886-3079-acd8-08d29a0eda83 | -10.50171 | -42.40076 | 2025-10-31 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e6eee030-4594-3510-8d83-05441d89512a | -10.43226 | -44.31046 | 2025-10-31 12:00:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3cc0443a-466f-3b0a-a251-6d16cc9ffa56 | -10.41946 | -44.33613 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5220f729-c574-3d67-958b-e3c8a86b819a | -8.10986 | -45.15545 | 2025-10-31 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 228036e9-f8d2-3f0e-acaf-660df3a0404d | -9.88029 | -44.86112 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| de145e01-4b04-355a-83dd-e159a9eda8d6 | -14.24212 | -44.2517 | 2025-10-31 12:00:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d9399988-6d87-33d2-abe7-dad421064f43 | -10.54917 | -42.7228 | 2025-10-31 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3509105b-d497-3a95-a597-09c3fb74b024 | -8.80167 | -42.81843 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 46fd83b1-28fd-35f8-9c1a-addc08bb2e92 | -13.47074 | -40.66437 | 2025-10-31 12:00:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 1f473469-f70f-35b5-a6f8-a714a3af53a7 | -7.70181 | -40.54201 | 2025-10-31 12:00:00 | TERRA_M-T | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 81498a9d-ce5d-3b99-8777-7d0d549f9068 | -13.34203 | -44.92054 | 2025-10-31 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 642b41ad-c4cf-34ed-8aa8-202545e3ce03 | -10.66199 | -45.25411 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d6cc4479-a0a4-3c62-88c6-7cee7b9853b5 | -10.27117 | -44.45927 | 2025-10-31 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b9e34ded-7a51-33cb-b8d8-df37e4d1a28d | -7.23335 | -37.29203 | 2025-10-31 12:00:00 | TERRA_M-T | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 7739a8ba-5f76-38e7-b5d3-6c0a7a71c7aa | -12.89005 | -44.97984 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3c1be63f-a4cc-319e-9a0a-12328d8680ed | -7.3199 | -44.94402 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 9e433fa4-828a-3913-8c29-0cc6006235c8 | -11.01078 | -42.97655 | 2025-10-31 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 13d63456-5358-39f3-8678-7417131e68c8 | -8.59029 | -43.95896 | 2025-10-31 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b87b2f40-94bd-3ef7-9b7a-e0882686e842 | -13.75027 | -43.81921 | 2025-10-31 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c4a46f7a-9816-3aab-9fb2-7da11a804d1d | -14.58973 | -46.63883 | 2025-10-31 12:00:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eab5d9ef-64ab-379f-b1a0-5b7da922012b | -12.53325 | -43.7564 | 2025-10-31 12:00:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8334df28-3f92-3c1f-9008-03556ea98862 | -7.31413 | -44.98304 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1b0c2f88-07fa-3248-abef-5f99c9b7716b | -8.59159 | -43.94999 | 2025-10-31 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8d2e3ce4-4e04-383c-8d2d-77918e4063bc | -7.64624 | -43.59135 | 2025-10-31 12:00:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6208184e-0b1e-3eb3-9df0-2bed80c51460 | -7.31557 | -44.9733 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2e62fc26-7a49-3ad2-9c67-d53859a3a793 | -14.5035 | -45.93382 | 2025-10-31 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd535d2b-c588-3717-a8c9-ed7693146d10 | -8.11474 | -45.18631 | 2025-10-31 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d062a7aa-abc8-3cc3-b76c-9bac0508fbbc | -10.64527 | -45.24189 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f720bcb5-befa-3405-93f2-f943967810c9 | -7.08276 | -44.9306 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 0e934f4e-82c8-3c84-be8a-fd9b4e064f8b | -8.12402 | -45.18763 | 2025-10-31 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 274.4 |


[Clique aqui para ver as próximas entradas](README45.md)
