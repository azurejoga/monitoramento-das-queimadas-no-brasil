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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5d423af-0d0e-3d9f-9c4a-067d544f0076 | -11.4695 | -43.4062 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1052.1 |
| 20e60fa1-3276-3488-aa5d-ef43e4dd2240 | -11.1424 | -44.6029 | 2026-10-02 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 288.2 |
| c534951a-c9a4-3a3a-a652-fb60d1fadc29 | -11.6977 | -43.5128 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 56e402e3-c48e-333b-b4b1-1692e3f0c2b7 | -11.2753 | -43.5539 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| d5fe3ea4-dad5-3be5-8cf9-27a4e0f3e78d | -12.886 | -44.7314 | 2026-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 641.4 |
| 58aebfb6-54ce-3941-a866-ce6a565d000e | -11.4315 | -43.3884 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 611.6 |
| 26438ba4-3dbd-3509-b8df-4d847d29109e | -12.904 | -44.7984 | 2026-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5a67d325-a7f5-30b8-96bb-9813acde284b | -11.2242 | -44.2888 | 2026-10-02 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 774a2785-1046-380b-aa99-f51277a6762b | -11.4503 | -43.4091 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1380.7 |
| 8a46f643-b6b9-359b-908b-da60566ccec8 | -11.1615 | -44.6002 | 2026-10-02 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 944.2 |
| 3a30c57e-a828-3219-b1e9-64be99d83aca | -12.8667 | -44.7346 | 2026-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| aae03ba1-b5a4-30e9-ae50-6fa9135b5e06 | -11.3931 | -43.3942 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 9f462c93-9b14-3a84-88ce-e78d5fce71f6 | -12.5334 | -43.067 | 2026-10-02 14:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 229.0 |
| 757e6718-d226-326a-a16c-e0449e260771 | -11.4123 | -43.3913 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 286.0 |
| e4eaf55c-9249-31f8-9afa-b6a2fa415d70 | -11.2762 | -43.5066 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 93c6c873-b475-3527-b8e3-e7da6324a6c8 | -10.6921 | -45.31 | 2026-10-02 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| dd125140-05e3-3903-9689-f0d5f04b1298 | -11.7353 | -43.5542 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| eb7b0142-2fd3-3e54-8ae4-85c2cde0a96d | -12.4737 | -44.1435 | 2026-10-02 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 306.6 |
| 8402bfa7-de26-34b0-8ba8-7ff49d1cd06c | -11.3931 | -43.3942 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 0b537b3f-cfba-3a9a-bd92-780dd8a718a7 | -11.716 | -43.5573 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 17cfbc39-f89e-3b30-a2dd-7328d54fd8b4 | -11.142 | -44.6261 | 2026-10-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 2aae0096-f9c5-32d3-a0fa-e281febbda11 | -11.257 | -43.5095 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 7eda6bc6-7bd1-3d92-acf8-3eb3ef4862b6 | -16.0946 | -42.6058 | 2026-10-02 14:10:00 | GOES-19 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 71265f9c-8dae-3de0-8a9e-3ac7b0d565cf | -11.487 | -43.4981 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| e2ad5ad8-9b3f-3c80-a8aa-cce3189052c5 | -12.5334 | -43.067 | 2026-10-02 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 226.8 |
| e4613b9b-32c8-32a8-875e-ac3616dfd72b | -11.2438 | -44.2626 | 2026-10-02 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 954fe8a9-f7b1-3c09-a8ae-9006d323171d | -10.3034 | -44.6249 | 2026-10-02 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 217.3 |
| d18eb179-dba1-30c4-b8c8-0acc60b474ad | -12.5135 | -43.0943 | 2026-10-02 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 132.4 |
| 64d7a43b-52bc-3145-8fb6-1fa1fdff4554 | -11.4695 | -43.4062 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1149.7 |
| 47dba63f-7b59-3cc6-9f1c-b79d87a22b13 | -11.2758 | -43.5303 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e338d033-9c60-3cad-aa78-84a9b3083dfa | 1.7399 | -50.8235 | 2026-10-02 14:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 93.5 |
| bd22b0f6-8930-38a6-95c3-7f6fd4e3a8a6 | -11.1232 | -44.6056 | 2026-10-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 8dc391cc-a0b3-3677-8af0-194becf0367c | -11.2434 | -44.286 | 2026-10-02 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 436.4 |
| d473fad3-0aa6-33ed-a08f-6b6cef1ec897 | -8.34 | -44.1427 | 2026-10-02 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3f69376f-d5f2-3ba2-94b6-dec037e5e7f1 | -11.3927 | -43.418 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 3ce48b2a-4d16-3e1b-ab94-b48d2808c7ec | -11.2753 | -43.5539 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f8872a93-5080-3976-8ca5-5860163ae93b | -10.303 | -44.648 | 2026-10-02 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 86753a94-1e9d-37c9-840d-a30be3bc6acd | -11.1424 | -44.6029 | 2026-10-02 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 442.1 |
| 6b021de9-9673-3cd1-9abd-7b6f53767059 | -11.4674 | -43.5248 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 38e30dd8-6f63-3d77-9628-8104342edf2e | -9.8444 | -44.8218 | 2026-10-02 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 8d1e77c9-81af-3773-8a25-7f830b4c6789 | -11.2242 | -44.2888 | 2026-10-02 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 926a038f-4e15-3ea5-9eff-a9a03db30be6 | -9.9882 | -45.3542 | 2026-10-02 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6c574a26-88c0-3283-aaf5-47fc702547d2 | -11.4866 | -43.5219 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 6d6759d0-27c7-3e20-851d-f3f78cb3746f | -11.4315 | -43.3884 | 2026-10-02 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 357.4 |
| 204c92ae-1d4e-3945-9378-82cb7f5ff8ab | -5.7565 | -45.1293 | 2026-10-02 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 2f39f7f1-384f-37f6-bb17-913c2ad62ecf | -11.47 | -43.4 | 2026-10-02 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c108889c-74d7-36f8-9a8c-38cb49b6d02e | -12.8 | -45.19 | 2026-10-02 14:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 103e663f-b48a-324c-8550-72153d8fbba5 | -13.84 | -45.26 | 2026-10-02 14:15:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c4dd6d2-897a-33c8-8b5d-8927d7611290 | -1.29 | -54.55 | 2026-10-02 14:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3180e627-b7cd-37df-ab60-0ebda8610968 | -1.26 | -54.55 | 2026-10-02 14:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ad59af-398c-34ce-8811-5d00012a479e | -11.29 | -44.27 | 2026-10-02 14:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d717de4-c0a4-375e-9831-1d5d2614a76c | -11.2438 | -44.2626 | 2026-10-02 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 76e73ed9-035e-382c-9c71-e03bb1dbd56a | -11.1424 | -44.6029 | 2026-10-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 344.3 |
| 045ca862-ca5a-37cc-98ca-ca3e1351ee57 | -11.3927 | -43.418 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 988bb6b2-00d7-36b7-9b43-dd579f50bdc1 | -10.907 | -43.8433 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 0b6204ce-d9d2-37d3-bcc3-663a302fd644 | -11.1232 | -44.6056 | 2026-10-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| bf2c0f55-8f33-3993-8432-6224490ecc9d | -11.7353 | -43.5542 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 79fc44d6-fce9-3a18-99e0-daacdbc0b40d | -11.4678 | -43.5011 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| f14ec7c0-f9d7-336b-b015-e6e6ff57853d | -11.4866 | -43.5219 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 333.0 |
| a38fee37-ad96-3bbb-914d-f9398298661e | -11.3931 | -43.3942 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| dea13a64-2e75-3c1d-a3e9-3cfa05b49cc4 | -11.4674 | -43.5248 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| c38c6cf6-f43c-380c-b7af-dd924ae6b24e | -11.4123 | -43.3913 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 305.2 |
| a157fe5e-3f6b-3777-9386-c7cca8ba5d4f | -11.142 | -44.6261 | 2026-10-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 44d0eb36-e4ce-30cb-bb23-529b9a443d75 | -6.3952 | -56.4158 | 2026-10-02 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 894eae67-144c-3056-a1a9-242e162a0e4d | -16.0939 | -42.6304 | 2026-10-02 14:20:00 | GOES-19 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 31aeac4f-cab2-324e-baf7-5d8187f2fba3 | -11.487 | -43.4981 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.7 |
| 843dcb04-8731-3b8d-ad49-73e45ca641c2 | -6.5866 | -55.4147 | 2026-10-02 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 1a9d948f-2459-3850-a3e7-83452f994c1c | -12.5334 | -43.067 | 2026-10-02 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 260.9 |
| 9aa9419b-d8bf-3573-add7-0e2ce1b0ebf2 | -6.1976 | -52.809 | 2026-10-02 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 384039e4-2b73-3523-b0d9-cadb7ebac197 | -7.8682 | -44.169 | 2026-10-02 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1698a12c-f1ce-3965-9bcf-1c920733ad6a | -11.2629 | -44.2598 | 2026-10-02 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 663.6 |
| 600bc3bc-f1f3-37e3-ae1b-d472ca593a50 | -7.0275 | -43.6247 | 2026-10-02 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 64411730-6604-3338-9940-d5429dca0380 | -12.4737 | -44.1435 | 2026-10-02 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 271.2 |
| e3df7c08-79c6-39b0-b71a-ac9280e8b176 | -11.2434 | -44.286 | 2026-10-02 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| d6c7c4b4-a8b5-3eff-bfe1-8624e0129f2c | -11.2566 | -43.5331 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 3e34f416-9280-3cc6-8a2f-f27ea9b3be5b | -16.0946 | -42.6058 | 2026-10-02 14:20:00 | GOES-19 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 72508dc3-61e9-3b1b-89e8-9d7f0e675923 | -12.5135 | -43.0943 | 2026-10-02 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 233.7 |
| 0678837e-81be-37b8-bb60-656fa43aee76 | -11.716 | -43.5573 | 2026-10-02 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| d1ceac83-efc9-3fe9-93a0-4f964fdeb478 | -9.844 | -44.8449 | 2026-10-02 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 0a41b857-9b12-351f-8f10-97b00fba880d | -12.2441 | -42.1048 | 2026-10-02 14:20:00 | GOES-19 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 75905c12-1a21-3364-9875-c59924d37430 | -6.2129 | -53.2575 | 2026-10-02 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 17d579e0-316b-36c9-99de-61a8ba77c51d | -11.716 | -43.5573 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.5 |
| fafffcc4-ff95-3508-b260-69f5ee2c7dd7 | -11.6588 | -43.5425 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 432006c0-44a2-32c8-ae6d-8ffcb55f6a9f | -11.6964 | -43.584 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.4 |
| ecb81509-b4b1-3f0f-a4ef-f8ec2feadc93 | -11.4678 | -43.5011 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 2de5c92e-cd0d-3a6a-b476-b4bb14dd744b | -11.6395 | -43.5455 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 808ce9af-31de-3d7c-b94e-398c2424c5df | 1.7399 | -50.8235 | 2026-10-02 14:30:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 09f0faa3-53a6-312d-807a-a88a46fd939f | -11.3931 | -43.3942 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.5 |
| 8478aa60-0a29-388c-8898-78ccaf5c06c2 | -12.5334 | -43.067 | 2026-10-02 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 230.8 |
| 7bdcdc16-0b33-30f5-a469-313860321180 | -11.2629 | -44.2598 | 2026-10-02 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 570.8 |
| 68f0e27c-7b90-35ca-9ed3-263f6dd861fe | -11.6575 | -43.6136 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 863548c6-01e2-3a6b-b199-d8669efea33b | -15.3024 | -42.7788 | 2026-10-02 14:30:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 419862d9-b5e1-3332-be7d-2f4b0e036643 | -10.907 | -43.8433 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 81ab429f-518b-3fb8-8190-c0b1dd8a48df | -12.5135 | -43.0943 | 2026-10-02 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 197.8 |
| 28ffd329-fa61-3967-aeec-d38a0cae16c7 | -9.5149 | -45.3199 | 2026-10-02 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f321a9ab-09f4-329a-aa97-674409ca7770 | -7.1827 | -52.6078 | 2026-10-02 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| be1743c0-71ff-366f-8975-714a259d19d6 | -11.2566 | -43.5331 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 52544f5c-6f8e-314f-a7fd-f2aa39aa2980 | -0.5073 | -49.1326 | 2026-10-02 14:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d3f77121-1c55-3261-aed9-1e420f2718f1 | -11.6583 | -43.5662 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 37a417bf-db19-3889-a425-03673ffef35c | -11.4866 | -43.5219 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.5 |


[Clique aqui para ver as próximas entradas](README89.md)
