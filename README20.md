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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47964a2-c7ad-339b-928b-f1e41af67ccc | -4.65356 | -43.81843 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66931de1-36ed-3453-b789-816511d9036b | -4.62443 | -39.66999 | 2024-11-02 03:23:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 730e15d6-394b-35ae-a97e-85692f7cb26e | -4.44961 | -43.64528 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de817ee9-a8ca-3781-af43-c059a5409660 | -4.44376 | -43.6374 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16c6b436-9ef7-37b9-b546-f0d3e3a5b7b6 | -4.44252 | -43.64436 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e046b26-0b50-392b-8cdc-1dd1bf8f4900 | -4.41442 | -43.47941 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a4a29d1-2d05-3f45-b731-65e59c24b05c | -4.40986 | -43.47156 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e621cd49-ce7f-393c-af0d-d020f22ec2b1 | -4.40869 | -43.47822 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c76ddc2c-6aa5-3383-8abe-e9c8d79196ab | -4.40867 | -43.47146 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| abb89f17-96a7-31bd-83c6-e457cbede1d2 | -4.40751 | -43.48495 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3c8fd36-6854-397c-a0ae-3a32ee4cc478 | -4.40745 | -43.47816 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9935f4e7-895c-3d11-9a48-4203a45fe254 | -4.40623 | -43.48487 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf1c41e8-8084-3a4a-976c-7d0e231e1082 | -4.40292 | -43.47012 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 913fcafe-e9e2-3bd3-8868-517ab7e6467c | -4.40172 | -43.47013 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ae46b351-136b-3832-8ab6-2fd304c65c4e | -4.40171 | -43.47699 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9aeabdf5-7c54-3e15-9212-1c1b8932c9af | -4.40053 | -43.48372 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56e3c554-299b-36f6-912c-14fce5911d89 | -4.40047 | -43.47696 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4f6e1b8d-3c14-35c0-96fb-780bf42be20c | -4.39925 | -43.48365 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 90ed588b-1ef1-368d-afaa-b49a1afe7ed9 | -4.39707 | -43.46254 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| df9a2184-5638-30e0-8392-fe2dc43b50fb | -4.39592 | -43.46907 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9c9f4b1a-7a70-32bd-b502-7cb927619710 | -4.39591 | -43.46259 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e6d6227b-1042-3a75-81bb-081e3bdc9376 | -4.39471 | -43.46909 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d76cb63-c6df-3170-99f0-2bcaffec4f90 | -4.39242 | -43.4889 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2620b9e1-27f9-3727-9a72-dc3728f23123 | -4.3911 | -43.48882 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 242591c0-29d6-3bd0-aaec-e9db05171e8a | -4.39007 | -43.46143 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bef21e1a-66f0-3aba-b698-a7601ada9d0a | -4.38892 | -43.46794 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 49a26930-595b-30b2-b8ab-5b6b5ef7c82c | -4.38548 | -43.48744 | 2024-11-02 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 62b17ae0-1e5f-3950-9d96-4cf35d8462de | -3.78068 | -43.54472 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e8086bab-72df-33f4-9b1f-db988fd63821 | -3.77949 | -43.55162 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2d52f338-5996-32d1-81be-cce3f424ea3e | -3.77833 | -43.55837 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4242643d-34a2-3f07-b74e-8ba2e7036236 | -3.77793 | -43.54431 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9428e2ae-da02-3878-a9d2-71577fdb7a48 | -3.7767 | -43.55119 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6d035ae8-2231-3a75-917c-862d90946bd8 | -3.77549 | -43.55796 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 80d1ad28-bed6-3e74-b462-46d2000de4f4 | -3.77249 | -43.54995 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bf0a55ad-7b09-3c97-9fb7-66d609141354 | -3.77128 | -43.557 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f86ca6fb-a570-3311-bf1d-1b1f2a7c8059 | -3.77092 | -43.54278 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6856c17f-87bc-341f-b555-5a1f339625fa | -3.76971 | -43.54951 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b67ae434-d120-3a8f-b09e-78c90707e13c | -3.76846 | -43.55651 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 91fac355-2ebd-3da5-bffc-9ba095626e24 | -3.76658 | -43.54199 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 665bdc80-b0bb-30c3-9801-86a0987e18f5 | -3.76543 | -43.54867 | 2024-11-02 03:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 65930b2a-e1fc-3217-b2d3-65b7501997f9 | -3.54876 | -43.57216 | 2024-11-02 03:23:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb88fe16-e1bb-3675-bc14-90caf46ccd30 | -3.53313 | -43.62043 | 2024-11-02 03:23:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c108c3d-edbb-334b-acd5-206d0bd7c9a3 | -3.53028 | -43.61592 | 2024-11-02 03:23:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e102afc-7abe-37a3-b4d0-90352749b080 | -3.52896 | -43.62328 | 2024-11-02 03:23:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ff555d2-dbf4-3e63-a7fd-48eca0c38e8a | -3.39836 | -41.64094 | 2024-11-02 03:23:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| cbd9b0de-a800-3f0a-87ed-e4a39e507c40 | -3.39746 | -41.64618 | 2024-11-02 03:23:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a1ff8d4a-62d2-3823-bb02-087864b6088b | -2.89438 | -40.51739 | 2024-11-02 03:23:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8b4ce77-c88e-39f2-b36c-1f4f6b5c2951 | -2.89135 | -40.51541 | 2024-11-02 03:23:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a78a110-d101-3ab4-b755-93d3efefa439 | -2.88839 | -40.51649 | 2024-11-02 03:23:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f372e87-a11f-34c0-b927-115b077f5ddb | -5.31352 | -43.06845 | 2024-11-02 03:23:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faa2432f-537c-319c-89f3-fbb2057501af | -4.45084 | -43.6384 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b1950f5-4c67-3589-b07b-cb0b0811901e | -9.28355 | -40.84547 | 2024-11-02 03:25:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7618a884-5141-3363-aad0-c1458e0b3cd3 | -10.73609 | -37.02452 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 29272e1c-18d3-374c-9704-2de8d3a58a93 | -11.5655 | -42.18724 | 2024-11-02 03:25:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fba250b8-b3eb-3eb6-b2f0-2456efcc1e5a | -11.20828 | -39.90809 | 2024-11-02 03:25:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf45fef5-f86c-3dbc-9634-583dbf216379 | -14.03124 | -43.56098 | 2024-11-02 03:25:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 81620b81-ea4d-310f-b584-875ffa357c30 | -14.03028 | -43.56564 | 2024-11-02 03:25:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 266d58e1-21ce-3bde-a7c1-2f7c7759fad1 | -13.36463 | -43.92838 | 2024-11-02 03:25:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6924846b-bfb2-3dee-bc96-3b3f511900bb | -13.36321 | -43.92751 | 2024-11-02 03:25:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfe2fc83-8a5f-3eb9-b0b6-2b2018f7ab37 | -11.2079 | -39.9095 | 2024-11-02 03:25:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 652f6581-1d4d-3d21-8f2a-380190ed112b | -11.20775 | -39.91103 | 2024-11-02 03:25:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cdc74e2e-fbfd-30af-838f-94e8a7282fbc | -10.74157 | -37.01756 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2934bc64-c15f-366b-9cfd-b9f56e28a3d0 | -10.74091 | -37.02139 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3e59eca8-7322-3a29-97b5-60df9e3ce765 | -10.74025 | -37.02524 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 87b253cb-a673-3266-b51c-58333e249a6e | -10.73741 | -37.01685 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9393e4d5-f069-360b-81dd-387341617c82 | -10.73675 | -37.02068 | 2024-11-02 03:25:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f706d4fa-70a2-3ca6-bd5b-ab74dde81319 | -9.38189 | -40.33613 | 2024-11-02 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38f249e0-9ccb-36e1-8804-131d92f1eb52 | -9.38128 | -40.3395 | 2024-11-02 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 665eb81a-e041-39d0-bfb0-c28d9fefeeb9 | -9.37658 | -40.33519 | 2024-11-02 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edaa1522-46cf-34af-bd55-ea55004f2940 | -9.37596 | -40.33857 | 2024-11-02 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96c8db71-d2f8-303a-860f-50d8be6f7943 | -1.2014 | -53.9184 | 2024-11-02 03:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 04283c31-0dfc-3803-9400-06a194d8b0e2 | -1.4717 | -46.7214 | 2024-11-02 03:25:14 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5bc7d07f-177d-3f79-8d12-42fade52d5f6 | -2.2663 | -53.7422 | 2024-11-02 03:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| da2b54f3-4dbf-3a0b-abcc-631b4df4012d | -2.8061 | -51.6095 | 2024-11-02 03:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8b0329e0-f726-39ae-9cba-acced7cf3279 | -2.8386 | -52.8794 | 2024-11-02 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 63490ded-421f-3009-b0a1-cb0199e14e1e | -3.0088 | -51.5834 | 2024-11-02 03:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 86ff2883-5a8d-3ff0-9262-f4f67fdc7239 | -3.0734 | -54.167 | 2024-11-02 03:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b4213361-3587-3e5d-a66e-44f4702e5360 | -3.1097 | -54.2865 | 2024-11-02 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b84b03f7-6477-31f1-b508-30f1ed759c36 | -3.1098 | -54.2665 | 2024-11-02 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0db300b4-603c-3cda-8528-ae6885d799fa | -3.1281 | -54.266 | 2024-11-02 03:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d45847c8-8c19-35d7-a9b5-18e5dbe687d8 | -3.2021 | -45.2932 | 2024-11-02 03:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| ce3ca47f-bd22-3a4d-8643-cbe4d3f2c7fb | -3.2205 | -45.315 | 2024-11-02 03:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| baf90ff9-c475-366b-bbdf-b616a569b634 | -3.2207 | -45.2925 | 2024-11-02 03:25:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e77aa772-99b1-3dc4-9558-d7dc0afb8668 | -3.7701 | -43.5554 | 2024-11-02 03:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| cc8bd725-115c-34c5-a9bb-03893659c7aa | -3.7888 | -43.5545 | 2024-11-02 03:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4219c339-79c5-3d60-9e18-a59bc2676b0f | -3.9473 | -48.3666 | 2024-11-02 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| aa44f0d0-6c41-3543-b639-9b7657d96cf0 | -3.9474 | -48.3451 | 2024-11-02 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| efe326c4-5cd2-31d6-aafb-3ab94675a821 | -3.9289 | -48.3458 | 2024-11-02 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c6539ecc-6142-3359-a943-820a1d59c725 | -3.9288 | -48.3674 | 2024-11-02 03:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f0a6d939-c803-3e79-925a-4cf7bcb55414 | -4.3537 | -48.6068 | 2024-11-02 03:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| a67d447c-cfb8-3fb4-afa7-5d12f8d49eac | -4.3867 | -43.4757 | 2024-11-02 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 57fb825a-b689-35c1-8bb5-29dba1dd4e7c | -4.3869 | -43.4525 | 2024-11-02 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5b24ac07-8763-3ccc-a303-951f2e41f791 | -4.4054 | -43.4746 | 2024-11-02 03:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6eac81eb-43c0-3a38-8023-2f26531ed94f | -4.7902 | -47.1298 | 2024-11-02 03:25:33 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2f27524c-bc9a-30cb-a34f-418e3c653dab | -22.7812 | -43.04517 | 2024-11-02 03:28:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f68205b3-99f6-31a2-9173-a90770f5be36 | -22.78071 | -43.04191 | 2024-11-02 03:28:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a79de99-1e28-30f8-af6c-e181011b4159 | -21.65589 | -42.1144 | 2024-11-02 03:28:00 | NOAA-21 | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4d8d87d7-ed4f-3c45-9645-cce544718cf0 | -21.6255 | -43.46746 | 2024-11-02 03:28:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7b209b0-4217-3d0a-9e32-e398115ed574 | -19.71602 | -40.35388 | 2024-11-02 03:28:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d4fdf7f-b516-3370-b669-e3f1be1160f0 | -1.2014 | -53.9184 | 2024-11-02 03:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README21.md)
